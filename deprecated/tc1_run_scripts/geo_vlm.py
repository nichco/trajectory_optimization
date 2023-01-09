import enum
from src.caddee.concept.geometry.geocore.ffd import FFDRotationXParameter, FFDScaleYParameter, FFDScaleZParameter, FFDTranslationXParameter

from src.caddee.mission.mission_analysis import MissionAnalysis
from src.caddee.concept.concept import Concept
from src.caddee.concept.geometry.geometry import Geometry
from src.caddee.mission.mission_segment import CruiseMissionSegment
from src.caddee.caddee import Caddee
from src.utils.base_class import CsdlInputVariableInfo
from src.utils.AircraftState import VehicleState
from src.utils.enums import AcStates, AllowableOperatingConditions
from src.caddee.concept.geometry.geocore.actuation import Actuation
from src.caddee.concept.operating_conditions import OperatingConditionsInfo
from src.caddee.concept.ffd_dvs import FfdInfo
from src.utils.enums import (AcStates, AllowableOperatingConditions, FfdTypes)

from tool_dependent.aerodynamics import AerodynamicSurface, VLMAerodynamicsSolver
from tool_dependent.propulsion import BEMRotor, Rotor, C172RegressionPropulsionSolver, BEMSolver, PittPetersSolver
from tool_dependent.massproperties import AircraftPointMass, C172MassPropertiesSolver
from src.caddee.mission.eom_model import EulerFlatEarth6DoF
from src.caddee.weights.mp_computation import MpComputation
from src.caddee.concept.feature import GenericFeature
# from csdl_om import Simulator
from python_csdl_backend import Simulator
from modopt.scipy_library import SLSQP
from modopt.csdl_library import CSDLProblem

from src.caddee.concept.geometry.geocore.component import Component
#from src.caddee.concept.geometry.geocore.geometric_calculations import MagnitudeCalculation
from src import STP_FILES_FOLDER

from src.caddee.concept.geometry.geocore.utils.generate_corner_points import generate_corner_points
from src.caddee.concept.geometry.geocore.utils.generate_camber_mesh import generate_camber_mesh
from src.caddee.concept.geometry.geocore.mesh import BEMMesh, VLMMesh

import numpy as np
from vedo import Points, Plotter

# make it the same line number
mm2ft = 304.8

caddee = Caddee(name='SuperC172_Test')


class ActuationEnums(enum.Enum):
    ElevDef = 'ElevatorDeflection'
    AilDef = 'AileronDeflection'


# region Concept
aircraft = AircraftPointMass(name='C172Aircraft')

# stp_path = STP_FILES_FOLDER / 'rect_wing.stp'
stp_path = STP_FILES_FOLDER / 'rect_wing_0012.stp'
geo = Geometry()
geo.read_file(file_name=stp_path)

wing_comp = Component(
    stp_entity_names=['RectWing'],
    name='wing')  # Creating a wing component and naming it wing
geo.add_component(wing_comp)

wing_feature = GenericFeature(name='RectWing')

# front_wing_feature = GenericFeature(name='RectWing')
concept = Concept()
concept.add_geometry(geometry=geo)

top_surfaces = ['RectWing, 0, 3', 'RectWing, 1, 9']
bot_surfaces = ['RectWing, 0, 2', 'RectWing, 1, 8']

left_lead_point = np.array([0.0, 9000., 2000.]) / 1000
left_trail_point = np.array([4000.0, 9000.0, 2000.]) / 1000
right_lead_point = np.array([0.0, -9000.0, 2000.]) / 1000
right_trail_point = np.array([4000.0, -9000.0, 2000.]) / 1000

point00 = left_lead_point
point01 = left_trail_point
point10 = right_lead_point
point11 = right_trail_point

fwing_lead_left, fwing_trail_left, fwing_lead_left_mid, fwing_trail_left_mid = generate_corner_points(
    geo, "wing", point00, point01, point10, point11)
fwing_left_top, fwing_left_bot, fwing_chord_surface_left, fwing_camber_surface_left = generate_camber_mesh(
    geo,
    fwing_lead_left,
    fwing_trail_left,
    fwing_lead_left_mid,
    fwing_trail_left_mid,
    top_surfaces,
    bot_surfaces,
    "RectWing",
    num_pts2=[11],
    num_pts1=[3])

vlm_mesh = VLMMesh('C172AircraftMesh', [
    fwing_camber_surface_left,
])

aircraft.add_mesh(vlm_mesh)


wing_lead_mid, _ = geo.project_points(np.array([0., 0., 2.]), projection_direction = np.array([0., 0., -1.]), projection_targets_names=["wing"])
wing_trail_mid, _ = geo.project_points(np.array([4., 0., 2.]), projection_direction = np.array([0., 0., -1.]), projection_targets_names=["wing"])
wing_lead_left, _ = geo.project_points(np.array([0., -9., 2.]), projection_direction = np.array([0., 0., -1.]), projection_targets_names=["wing"])
wing_lead_right, _ = geo.project_points(np.array([0., 9., 2.]), projection_direction = np.array([0., 0., -1.]), projection_targets_names=["wing"])
chord = geo.subtract_pointsets(wing_lead_mid, wing_trail_mid)
span = geo.subtract_pointsets(wing_lead_right, wing_lead_left)

# region FFD
wing_comp.add_ffd_parameter(FFDRotationXParameter(degree=3, num_dof=5, connection_name='twist'))
wing_comp.add_ffd_parameter(FFDScaleYParameter(degree=1, num_dof=3, cost_factor=1.))
wing_comp.add_ffd_parameter(FFDScaleZParameter(degree=3, num_dof=5, value=np.array([0., 0.7, 1., 0.7, 0.])))
wing_comp.add_ffd_parameter(FFDTranslationXParameter(degree=1, num_dof=2, cost_factor=1.))

geo.add_input(MagnitudeCalculation(chord), connection_name='chord')
geo.add_input(MagnitudeCalculation(span), connection_name='span')
# endregion FFD


# elev_def_actuation = Actuation(name=ActuationEnums.ElevDef.value,
#                                geo=geo,
#                                origin=fwing_trail_left,
#                                end_point=fwing_trail_left_mid,
#                                actuating_components=[wing_comp])

# endregion

# region Cruise 1 Mission segment
cruise_segment_state = VehicleState(mach=0.15, altitude=1000.)
# cruise_segment_state.Theta = np.deg2rad(3.125382526501336)  # First specify Theta
cruise_segment_state.Theta = np.deg2rad(0.)  # First specify Theta
cruise_segment_state.gamma = np.deg2rad(0.)  # Then specify gamma
cruise_segment_state.Psi = np.deg2rad(0.)  # First specify Psi
cruise_segment_state.Psi_W = np.deg2rad(0.)  # Then specify Psi_W
print(cruise_segment_state.__str__())

cruise_args = {
    'name':
    'Cruise1',
    'stability_flag':
    False,
    'dynamic_flag':
    False,
    AcStates.u.value:
    CsdlInputVariableInfo(value=cruise_segment_state.u),
    AcStates.v.value:
    CsdlInputVariableInfo(value=cruise_segment_state.v),
    AcStates.w.value:
    CsdlInputVariableInfo(value=cruise_segment_state.w),
    AcStates.p.value:
    CsdlInputVariableInfo(value=cruise_segment_state.p),
    AcStates.q.value:
    CsdlInputVariableInfo(value=cruise_segment_state.q),
    AcStates.r.value:
    CsdlInputVariableInfo(value=cruise_segment_state.r),
    AcStates.phi.value:
    CsdlInputVariableInfo(value=cruise_segment_state.Phi),
    AcStates.theta.value:
    CsdlInputVariableInfo(value=cruise_segment_state.Theta, dv_flag=False),
    AcStates.psi.value:
    CsdlInputVariableInfo(value=cruise_segment_state.Psi),
    AcStates.x.value:
    CsdlInputVariableInfo(value=cruise_segment_state.X),
    AcStates.y.value:
    CsdlInputVariableInfo(value=cruise_segment_state.Y),
    AcStates.z.value:
    CsdlInputVariableInfo(value=cruise_segment_state.Z),
    AcStates.phiw.value:
    CsdlInputVariableInfo(value=cruise_segment_state.Phi_W),
    AcStates.gamma.value:
    CsdlInputVariableInfo(value=cruise_segment_state.gamma),
    AcStates.psiw.value:
    CsdlInputVariableInfo(value=cruise_segment_state.Psi_W),
    'range':
    CsdlInputVariableInfo(value=80000.)  # 80 km
}
cruise1_segment = CruiseMissionSegment(**cruise_args)

cruise1_aero_solver = VLMAerodynamicsSolver()
cruise1_aero_solver.add_feature(aircraft)
cruise1_segment.add_solver(cruise1_aero_solver)

# cruise1_rotor_prop_solver = C172RegressionPropulsionSolver()
# cruise1_rotor_prop_solver = BEMSolver()
# cruise1_rotor_prop_solver.add_feature(feature=pusher_rotor)
# cruise1_segment.add_solver(cruise1_rotor_prop_solver)

cruise1_elev_def_oc = OperatingConditionsInfo(
    name=AllowableOperatingConditions.ElevatorDeflection.value,
    csdl_input_var=CsdlInputVariableInfo(value=np.deg2rad(0.)),
    feature=wing_feature,
    mission_segment=cruise1_segment)

# cruise1_segment.add_actuation(actuation_obj=elev_def_actuation,
#                               oper_cond_info_obj=cruise1_elev_def_oc)
# caddee.add_operating_condition(cruise1_elev_def_oc)
# endregion
# region Mission
mission = MissionAnalysis(fmRefPt=np.array([[4.5, 0, 5]]))
mission.add_mission_segment(segment=cruise1_segment)
mission.add_eom_model(eom_model=EulerFlatEarth6DoF)
# endregion

# region Structural mass properties computation