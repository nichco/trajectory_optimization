import enum
from multiprocessing import connection
import numpy as np

# from csdl_om import Simulator
from python_csdl_backend import Simulator
from modopt.csdl_library import CSDLProblem

from src import AIRCRAFT_FILES_FOLDER
from src.caddee.caddee import Caddee
from src.caddee.concept.geometry.geocore.ffd import FFDRotationXParameter, FFDScaleYParameter, FFDScaleZParameter, FFDTranslationXParameter, FFDTranslationYParameter, FFDTranslationZParameter
from src.utils.base_class import CsdlInputVariableInfo, CsdlConnectionsInfo, ConstraintModelInfo
from src.utils.enums import (
    AcStates,
    AllowableOperatingConditions,
    CaddeeModelNames,
    FfdTypes
)

# Geometry
from src.caddee.concept.geometry.geometry import Geometry
from src.caddee.concept.geometry.geocore.component import Component
from src.caddee.concept.geometry.geocore.utils.thrust_vector_creation import generate_thrust_vector
from src.caddee.concept.geometry.geocore.utils.generate_corner_points import generate_corner_points
from src.caddee.concept.geometry.geocore.utils.generate_camber_mesh import generate_camber_mesh
from src.caddee.concept.geometry.geocore.geometric_outputs import DisplacementCalculation, GeometricOutputs, MagnitudeCalculation
from src.caddee.concept.geometry.geocore.mesh import BEMMesh, VLMMesh
from src.caddee.concept.geometry.geocore.actuation import Actuation
# Concept
from src.caddee.concept.operating_conditions import OperatingConditionsInfo
from src.caddee.concept.concept import Concept
from src.caddee.concept.feature import GenericFeature
# Mass properties
from src.caddee.weights.mp_computation import MpComputation
# Tool Dependent
from tool_dependent.propulsion import BEMRotor, BEMSolver
from tool_dependent.massproperties import (
    AircraftPointMass, DwMassPropertiesSolver, 
    LPCMassPropertiesSolver, M4WeightsRegressionSolver, 
    Tc1BatterySizingSolver, MotorSizingSolver
)
from tool_dependent.aerodynamics import VLMAerodynamicsSolver
from tool_dependent.powerenergy import ECMSolver, Tc1PowertrainSolver
from tool_dependent.acoustics import TC1AcousticsSolver
from tool_dependent.powerenergy import BatteryPack
from tool_dependent.motor_analysis import Tc1MotorAnalysisSolver
from src.caddee.power_energy.power_energy import PowerEnergy
from src.caddee.power_energy.powertrain import Powertrain
# Mission
from src.utils.AircraftState import VehicleState
from src.caddee.mission.mission_segment import (
    CruiseMissionSegment,
    HoverMissionSegment,
    ClimbMissionSegment
)
from src.caddee.mission.eom_model import EulerFlatEarth6DoF, EulerFlatEarth6DoFGenRef
from src.caddee.mission.mission_analysis import MissionAnalysis
# Others
from src.caddee.concept.ffd_dvs import FfdInfo
from src.caddee.optimization.v_stall_constraint import VstallConstraintModel
import time
import numpy as np
from vedo import Points, Plotter


t_setup_start = time.time()
mm2ft = 304.8
mm2ft = 1000.

ft2m = 1/3.281

class ActuationEnums(enum.Enum):
    ElevDef = 'ElevatorDeflection'
    AilDef = 'AileronDeflection'


caddee = Caddee(
    name='LiftPlusCruise'
)

# region Concept
concept = Concept()

# region Features
aircraft = AircraftPointMass(
    name='LiftPlusCruise'
)
wing_feature = GenericFeature(
    name='Wing'
)
horizontal_tail_feature = GenericFeature(
    name='HorizontalTail'
)
pusher_rotor_feature = GenericFeature(
    name='PusherRotor'
)

# region Import
# stp_path = AIRCRAFT_FILES_FOLDER / 'nasa_lpc' / 'lift_plus_cruise_stripped_down_4.stp'
stp_path = AIRCRAFT_FILES_FOLDER / 'nasa_lpc' / 'lift_plus_cruise_final_3.stp'
geo = Geometry()
geo.read_file(file_name=stp_path)
# endregion
# exit()
# region Components
# Wing
front_wing = Component(stp_entity_names=['FrontWing'], name='front_wing', nxp=2,nyp=10,nzp=2)  # Creating a wing component and naming it wing
geo.add_component(front_wing)
# Region ffd
# ------------------------------------------
front_wing.add_ffd_parameter(
    FFDScaleYParameter(degree=1, num_dof=3,cost_factor=1) # This is in the chord-wise direction; z would be thickness
)
# ------------------------------------------
# NOTE: on FFDScale(Y,Z)Parameter
# - Y refers to FFD coordinate frame; 
# - X refers to the long direction;
# - Z stays "up/down" in the body-fixed frame
# - degree refers to B-spline order-1; 
# - num_dof = number of b-spline curve
# - cost_factor: default=1; if this is a inner optimization variable (should be 1 in most cases; important if you have multiple "parameters" of the same property (meaning ScaleY) with different degrees (e.g. linear and quadratic)
# - value: needs to be numpy array of length num_dof (specifying scale-y along the span); not needed if you want to run inner optimization
# - connection_name: if you have an upstream model that calculates the value, it'll look for a name that would make that connection

# ---------------------------------------------------
front_wing.add_ffd_parameter(                                    # This is to translate the wing in the "long" direction ()
    FFDTranslationXParameter(degree=1, num_dof=2, cost_factor=1) # If you want more num_dof, make cost_factor a lot bigger compared to hub ffd cost_factors
)
# ---------------------------------------------------
# For wing twist
front_wing.add_ffd_parameter(
    FFDRotationXParameter(degree=2, num_dof=5, connection_name='twist')
)
# FFDTranslationXParameter: for allowing movement span-wise direction
# - nom_dof: 2 would mean specifying left and right side (ends of FFD block)

# NOTE: Rest of geometry
# 1) Booms: connected to wing --> point on boom to point wing or hub 
# 2) Fuselage: connect to wing, tail 
# 3) Vertical tail: connect horizontal tail
# 4) Rotor disk: connect to hub (hard coded at the end?)


# H-tail
tail = Component(stp_entity_names=['Tail_1'], name='tail', nxp=2,nyp=10,nzp=2) # NOTE: nxp,nyp,nzp refer to the number of control points along the axes in the body-fixed frame 
geo.add_component(tail)
tail.add_ffd_parameter(
    FFDScaleYParameter(degree=1, num_dof=3,cost_factor=1) # For changing tail area via chord 
)
# -----------------------------------------
tail.add_ffd_parameter(
    FFDTranslationXParameter(degree=1, num_dof=2, cost_factor=1)
)
tail.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1) # For changing the tail moment arm 
)

# V-tail
vtail = Component(stp_entity_names=['Tail_2'], name='vtail', nxp=2,nyp=2,nzp=2) # NOTE: nxp,nyp,nzp refer to the number of control points along the axes in the body-fixed frame 
geo.add_component(vtail)
vtail.add_ffd_parameter(
    FFDTranslationXParameter(degree=0, num_dof=1, cost_factor=1)
)
vtail.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
vtail.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
vtail_point_location = np.array([20.843,0.,8.231])
tail_point_location = np.array([30.550,0.,8.008])
vtail_ps,_ = geo.project_points(vtail_point_location, projection_targets_names=['vtail'])
tail_ps,_ = geo.project_points(tail_point_location, projection_targets_names=['tail'])

vtail_tail_connection_ps = geo.subtract_pointsets(tail_ps,vtail_ps)
geo.add_constraint(
    DisplacementCalculation(vtail_tail_connection_ps)
)

# Fuselage
fuselage = Component(stp_entity_names=['Fuselage'], name='fuselage',nxp=2,nyp=2,nzp=2)
geo.add_component(fuselage)
fuselage.add_ffd_parameter(
    FFDScaleYParameter(degree=0, num_dof=1, cost_factor=100)
)
fuselage.add_ffd_parameter(
    FFDScaleZParameter(degree=0, num_dof=1, cost_factor=100)
)
fuselage.add_ffd_parameter(
    FFDTranslationXParameter(degree=1, num_dof=2, cost_factor=1)
)
fuselage.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
fuselage.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
fuselage_point_location = np.array([2.889,0.0,4.249])
tail_point_location = np.array([30.550,0.,8.008])
# wing_point_location = np.array([8.890,0.,8.5])
fuselage_ps,_ = geo.project_points(fuselage_point_location, projection_targets_names=['fuselage'])
wing_fuselage_ps,_ =  geo.project_points(fuselage_point_location, projection_targets_names=['front_wing'])
tail_fuselage_ps,_ =  geo.project_points(tail_point_location, projection_targets_names=['tail'])
fuselage_wing_connection_ps = geo.subtract_pointsets(fuselage_ps,wing_fuselage_ps)
fuselage_tail_connection_ps = geo.subtract_pointsets(fuselage_ps,tail_fuselage_ps)
geo.add_constraint(
    DisplacementCalculation(fuselage_wing_connection_ps)
)
# geo.add_constraint(
#     DisplacementCalculation(fuselage_tail_connection_ps)
# )

# Rotor disks
# Front left outer
lift_rotor_disk_front_lo = Component(stp_entity_names=['Rotor_1_disk'], name='lift_rotor_disk_front_left_outer',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_disk_front_lo)
lift_rotor_disk_front_lo.add_ffd_parameter(
    FFDScaleYParameter(degree=0, num_dof=1, cost_factor=100)
)
lift_rotor_disk_front_lo.add_ffd_parameter(
    FFDScaleZParameter(degree=0, num_dof=1, cost_factor=100)
)
lift_rotor_disk_front_lo.add_ffd_parameter(
    FFDTranslationXParameter(degree=1, num_dof=2, cost_factor=1)
)
lift_rotor_disk_front_lo.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_disk_front_lo.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_flo_point_location = np.array([5.070,-18.750,7.355])
lr_flo_ps,_ = geo.project_points(lr_flo_point_location, projection_targets_names=['lift_rotor_disk_front_left_outer'])
wing_flo_ps,_ =  geo.project_points(lr_flo_point_location, projection_targets_names=['front_wing'])
lf_flo_wing_connection_ps = geo.subtract_pointsets(lr_flo_ps,wing_flo_ps)
geo.add_constraint(
    DisplacementCalculation(lf_flo_wing_connection_ps)
)

# Front left inner
lift_rotor_disk_front_li = Component(stp_entity_names=['Rotor_3_disk'], name='lift_rotor_disk_front_left_inner',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_disk_front_li)
lift_rotor_disk_front_li.add_ffd_parameter(
    FFDScaleYParameter(degree=0, num_dof=1, cost_factor=100)
)
lift_rotor_disk_front_li.add_ffd_parameter(
    FFDScaleZParameter(degree=0, num_dof=1, cost_factor=100)
)
lift_rotor_disk_front_li.add_ffd_parameter(
    FFDTranslationXParameter(degree=1, num_dof=2, cost_factor=1)
)
lift_rotor_disk_front_li.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_disk_front_li.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_fli_point_location = np.array([4.630,-8.217,7.659])
lr_fli_ps,_ = geo.project_points(lr_fli_point_location, projection_targets_names=['lift_rotor_disk_front_left_inner'])
wing_fli_ps,_ =  geo.project_points(lr_fli_point_location, projection_targets_names=['front_wing'])
lf_fli_wing_connection_ps = geo.subtract_pointsets(lr_fli_ps,wing_fli_ps)
geo.add_constraint(
    DisplacementCalculation(lf_fli_wing_connection_ps)
)

# front right inner
lift_rotor_disk_front_ri = Component(stp_entity_names=['Rotor_5_disk'], name='lift_rotor_disk_front_right_inner',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_disk_front_ri)
lift_rotor_disk_front_ri.add_ffd_parameter(
    FFDScaleYParameter(degree=0, num_dof=1, cost_factor=100)
)
lift_rotor_disk_front_ri.add_ffd_parameter(
    FFDScaleZParameter(degree=0, num_dof=1, cost_factor=100)
)
lift_rotor_disk_front_ri.add_ffd_parameter(
    FFDTranslationXParameter(degree=1, num_dof=2, cost_factor=1)
)
lift_rotor_disk_front_ri.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_disk_front_ri.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_fri_point_location = np.array([4.630,8.217,7.659])
lr_fri_ps,_ = geo.project_points(lr_fri_point_location, projection_targets_names=['lift_rotor_disk_front_right_inner'])
wing_fri_ps,_ =  geo.project_points(lr_fri_point_location, projection_targets_names=['front_wing'])
lf_fri_wing_connection_ps = geo.subtract_pointsets(lr_fri_ps,wing_fri_ps)
geo.add_constraint(
    DisplacementCalculation(lf_fri_wing_connection_ps)
)

# front right outer
lift_rotor_disk_front_ro = Component(stp_entity_names=['Rotor_7_disk'], name='lift_rotor_disk_front_right_outer',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_disk_front_ro)
lift_rotor_disk_front_ro.add_ffd_parameter(
    FFDScaleYParameter(degree=0, num_dof=1, cost_factor=100)
)
lift_rotor_disk_front_ro.add_ffd_parameter(
    FFDScaleZParameter(degree=0, num_dof=1, cost_factor=100)
)
lift_rotor_disk_front_ro.add_ffd_parameter(
    FFDTranslationXParameter(degree=1, num_dof=2, cost_factor=1)
)
lift_rotor_disk_front_ro.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_disk_front_ro.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_fro_point_location = np.array([5.070,18.750,7.355])
lr_fro_ps,_ = geo.project_points(lr_fro_point_location, projection_targets_names=['lift_rotor_disk_front_right_outer'])
wing_fro_ps,_ =  geo.project_points(lr_fro_point_location, projection_targets_names=['front_wing'])
lf_fro_wing_connection_ps = geo.subtract_pointsets(lr_fro_ps,wing_fro_ps)
geo.add_constraint(
    DisplacementCalculation(lf_fro_wing_connection_ps)
)

# rear left outer
lift_rotor_disk_rear_lo = Component(stp_entity_names=['Rotor_2_disk'], name='lift_rotor_disk_rear_left_outer',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_disk_rear_lo)
lift_rotor_disk_rear_lo.add_ffd_parameter(
    FFDScaleYParameter(degree=0, num_dof=1, cost_factor=100)
)
lift_rotor_disk_rear_lo.add_ffd_parameter(
    FFDScaleZParameter(degree=0, num_dof=1, cost_factor=100)
)
lift_rotor_disk_rear_lo.add_ffd_parameter(
    FFDTranslationXParameter(degree=1, num_dof=2, cost_factor=1)
)
lift_rotor_disk_rear_lo.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_disk_rear_lo.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_rlo_point_location = np.array([19.200,-18.750,9.635])
lr_rlo_ps,_ = geo.project_points(lr_rlo_point_location, projection_targets_names=['lift_rotor_disk_rear_left_outer'])
wing_rlo_ps,_ =  geo.project_points(lr_rlo_point_location, projection_targets_names=['front_wing'])
lf_rlo_wing_connection_ps = geo.subtract_pointsets(lr_rlo_ps,wing_rlo_ps)
geo.add_constraint(
    DisplacementCalculation(lf_rlo_wing_connection_ps)
)

# rear left inner
lift_rotor_disk_rear_li = Component(stp_entity_names=['Rotor_4_disk'], name='lift_rotor_disk_rear_left_inner',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_disk_rear_li)
lift_rotor_disk_rear_li.add_ffd_parameter(
    FFDScaleYParameter(degree=0, num_dof=1, cost_factor=100)
)
lift_rotor_disk_rear_li.add_ffd_parameter(
    FFDScaleZParameter(degree=0, num_dof=1, cost_factor=100)
)
lift_rotor_disk_rear_li.add_ffd_parameter(
    FFDTranslationXParameter(degree=1, num_dof=2, cost_factor=1)
)
lift_rotor_disk_rear_li.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_disk_rear_li.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_rli_point_location = np.array([18.760,-8.537,9.919])
lr_rli_ps,_ = geo.project_points(lr_rli_point_location, projection_targets_names=['lift_rotor_disk_rear_left_inner'])
wing_rli_ps,_ =  geo.project_points(lr_rli_point_location, projection_targets_names=['front_wing'])
lf_rli_wing_connection_ps = geo.subtract_pointsets(lr_rli_ps,wing_rli_ps)
geo.add_constraint(
    DisplacementCalculation(lf_rli_wing_connection_ps)
)

# rear right inner
lift_rotor_disk_rear_ri = Component(stp_entity_names=['Rotor_6_disk'], name='lift_rotor_disk_rear_right_inner',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_disk_rear_ri)
lift_rotor_disk_rear_ri.add_ffd_parameter(
    FFDScaleYParameter(degree=0, num_dof=1, cost_factor=100)
)
lift_rotor_disk_rear_ri.add_ffd_parameter(
    FFDScaleZParameter(degree=0, num_dof=1, cost_factor=100)
)
lift_rotor_disk_rear_ri.add_ffd_parameter(
    FFDTranslationXParameter(degree=1, num_dof=2, cost_factor=1)
)
lift_rotor_disk_rear_ri.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_disk_rear_ri.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_rri_point_location = np.array([18.760,8.537,9.919])
lr_rri_ps,_ = geo.project_points(lr_rri_point_location, projection_targets_names=['lift_rotor_disk_rear_right_inner'])
wing_rri_ps,_ =  geo.project_points(lr_rri_point_location, projection_targets_names=['front_wing'])
lf_rri_wing_connection_ps = geo.subtract_pointsets(lr_rri_ps,wing_rri_ps)
geo.add_constraint(
    DisplacementCalculation(lf_rri_wing_connection_ps)
)

# rear right outer
lift_rotor_disk_rear_ro = Component(stp_entity_names=['Rotor_8_disk'], name='lift_rotor_disk_rear_right_outer',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_disk_rear_ro)
lift_rotor_disk_rear_ro.add_ffd_parameter(
    FFDScaleYParameter(degree=0, num_dof=1, cost_factor=100)
)
lift_rotor_disk_rear_ro.add_ffd_parameter(
    FFDScaleZParameter(degree=0, num_dof=1, cost_factor=100)
)
lift_rotor_disk_rear_ro.add_ffd_parameter(
    FFDTranslationXParameter(degree=1, num_dof=2, cost_factor=1)
)
lift_rotor_disk_rear_ro.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_disk_rear_ro.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_rro_point_location = np.array([19.200,18.750,9.635])
lr_rro_ps,_ = geo.project_points(lr_rro_point_location, projection_targets_names=['lift_rotor_disk_rear_right_outer'])
wing_rro_ps,_ =  geo.project_points(lr_rro_point_location, projection_targets_names=['front_wing'])
lf_rro_wing_connection_ps = geo.subtract_pointsets(lr_rro_ps,wing_rro_ps)
geo.add_constraint(
    DisplacementCalculation(lf_rro_wing_connection_ps)
)

pusher_rotor_disk = Component(stp_entity_names=['Rotor-9-disk'], name='pusher_rotor_disk',nxp=2,nyp=2,nzp=2)
geo.add_component(pusher_rotor_disk)
pusher_rotor_disk.add_ffd_parameter(
    FFDScaleYParameter(degree=0, num_dof=1, cost_factor=100)
)
pusher_rotor_disk.add_ffd_parameter(
    FFDScaleZParameter(degree=0, num_dof=1, cost_factor=100)
)
pusher_rotor_disk.add_ffd_parameter(
    FFDTranslationXParameter(degree=1, num_dof=2, cost_factor=1)
)
pusher_rotor_disk.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
pusher_rotor_disk.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
pusher_point_location = np.array([32.,0.,8.])
tail_point_location = np.array([30.550,0.,8.008])
pusher_ps,_ = geo.project_points(pusher_point_location, projection_targets_names=['pusher_rotor_disk'])
tail_ps,_ = geo.project_points(tail_point_location, projection_targets_names=['tail'])
hub_tail_connection_ps = geo.subtract_pointsets(pusher_ps,tail_ps)
geo.add_constraint(
    DisplacementCalculation(hub_tail_connection_ps)
)

# ------------------------------------------------- Booms/Rotor support ------------------------------------------------- #
# front left outer
lift_rotor_support_front_lo = Component(stp_entity_names=['Rotor_1_Support'], name='lift_rotor_support_front_left_outer',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_support_front_lo)
lift_rotor_support_front_lo.add_ffd_parameter(
    FFDTranslationXParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_support_front_lo.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_support_front_lo.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_flo_point_location = np.array([4.200,-18.750,7.612])
lr_flo_ps,_ = geo.project_points(lr_flo_point_location, projection_targets_names=['lift_rotor_support_front_left_outer'])
wing_flo_ps,_ =  geo.project_points(lr_flo_point_location, projection_targets_names=['front_wing'])
lf_flo_wing_connection_ps = geo.subtract_pointsets(lr_flo_ps,wing_flo_ps)
geo.add_constraint(
    DisplacementCalculation(lf_flo_wing_connection_ps)
)
# front left inner
lift_rotor_support_front_li = Component(stp_entity_names=['Rotor_3_Support'], name='lift_rotor_support_front_left_inner',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_support_front_li)
lift_rotor_support_front_li.add_ffd_parameter(
    FFDTranslationXParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_support_front_li.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_support_front_li.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_fli_point_location = np.array([3.741,-8.250,7.900])
lr_fli_ps,_ = geo.project_points(lr_fli_point_location, projection_targets_names=['lift_rotor_support_front_left_inner'])
wing_fli_ps,_ =  geo.project_points(lr_fli_point_location, projection_targets_names=['front_wing'])
lf_fli_wing_connection_ps = geo.subtract_pointsets(lr_fli_ps,wing_fli_ps)
geo.add_constraint(
    DisplacementCalculation(lf_fli_wing_connection_ps)
)
# front right inner
lift_rotor_support_front_ri = Component(stp_entity_names=['Rotor_5_Support'], name='lift_rotor_support_front_right_inner',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_support_front_ri)
lift_rotor_support_front_ri.add_ffd_parameter(
    FFDTranslationXParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_support_front_ri.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_support_front_ri.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_fri_point_location = np.array([3.741,8.250,7.900])
lr_fri_ps,_ = geo.project_points(lr_fri_point_location, projection_targets_names=['lift_rotor_support_front_right_inner'])
wing_fri_ps,_ =  geo.project_points(lr_fri_point_location, projection_targets_names=['front_wing'])
lf_fri_wing_connection_ps = geo.subtract_pointsets(lr_fri_ps,wing_fri_ps)
geo.add_constraint(
    DisplacementCalculation(lf_fri_wing_connection_ps)
)
# front right outer
lift_rotor_support_front_ro = Component(stp_entity_names=['Rotor_7_Support'], name='lift_rotor_support_front_right_outer',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_support_front_ro)
lift_rotor_support_front_ro.add_ffd_parameter(
    FFDTranslationXParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_support_front_ro.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_support_front_ro.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_fro_point_location = np.array([4.200,18.750,7.615])
lr_fro_ps,_ = geo.project_points(lr_fro_point_location, projection_targets_names=['lift_rotor_support_front_right_outer'])
wing_fro_ps,_ =  geo.project_points(lr_fro_point_location, projection_targets_names=['front_wing'])
lf_fro_wing_connection_ps = geo.subtract_pointsets(lr_fro_ps,wing_fro_ps)
geo.add_constraint(
    DisplacementCalculation(lf_fro_wing_connection_ps)
)
# rear left outer
lift_rotor_support_rear_lo = Component(stp_entity_names=['Rotor_2_Support'], name='lift_rotor_support_rear_left_outer',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_support_rear_lo)
lift_rotor_support_rear_lo.add_ffd_parameter(
    FFDTranslationXParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_support_rear_lo.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_support_rear_lo.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_rlo_point_location = np.array([20.000,-18.750,7.613])
lr_rlo_ps,_ = geo.project_points(lr_rlo_point_location, projection_targets_names=['lift_rotor_support_rear_left_outer'])
wing_rlo_ps,_ =  geo.project_points(lr_rlo_point_location, projection_targets_names=['front_wing'])
lf_rlo_wing_connection_ps = geo.subtract_pointsets(lr_rlo_ps,wing_rlo_ps)
geo.add_constraint(
    DisplacementCalculation(lf_rlo_wing_connection_ps)
)
# rear left inner
lift_rotor_support_rear_li = Component(stp_entity_names=['Rotor_4_Support'], name='lift_rotor_support_rear_left_inner',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_support_rear_li)
lift_rotor_support_rear_li.add_ffd_parameter(
    FFDTranslationXParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_support_rear_li.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_support_rear_li.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_rli_point_location = np.array([19.497,-8.457,7.971])
lr_rli_ps,_ = geo.project_points(lr_rli_point_location, projection_targets_names=['lift_rotor_support_rear_left_inner'])
wing_rli_ps,_ =  geo.project_points(lr_rli_point_location, projection_targets_names=['front_wing'])
lf_rli_wing_connection_ps = geo.subtract_pointsets(lr_rli_ps,wing_rli_ps)
geo.add_constraint(
    DisplacementCalculation(lf_rli_wing_connection_ps)
)
# rear right inner
lift_rotor_support_rear_ri = Component(stp_entity_names=['Rotor_6_Support'], name='lift_rotor_support_rear_right_inner',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_support_rear_ri)
lift_rotor_support_rear_ri.add_ffd_parameter(
    FFDTranslationXParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_support_rear_ri.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_support_rear_ri.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_rri_point_location = np.array([19.497,8.457,7.971])
lr_rri_ps,_ = geo.project_points(lr_rri_point_location, projection_targets_names=['lift_rotor_support_rear_right_inner'])
wing_rri_ps,_ =  geo.project_points(lr_rri_point_location, projection_targets_names=['front_wing'])
lf_rri_wing_connection_ps = geo.subtract_pointsets(lr_rri_ps,wing_rri_ps)
geo.add_constraint(
    DisplacementCalculation(lf_rri_wing_connection_ps)
)
# rear right outer
lift_rotor_support_rear_ro = Component(stp_entity_names=['Rotor_8_Support'], name='lift_rotor_support_rear_right_outer',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_support_rear_ro)
lift_rotor_support_rear_ro.add_ffd_parameter(
    FFDTranslationXParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_support_rear_ro.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_support_rear_ro.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_rro_point_location = np.array([20.000,18.750,7.613])
lr_rro_ps,_ = geo.project_points(lr_rro_point_location, projection_targets_names=['lift_rotor_support_rear_right_outer'])
wing_rro_ps,_ =  geo.project_points(lr_rro_point_location, projection_targets_names=['front_wing'])
lf_rro_wing_connection_ps = geo.subtract_pointsets(lr_rro_ps,wing_rro_ps)
geo.add_constraint(
    DisplacementCalculation(lf_rro_wing_connection_ps)
)



# Rotor Hubs
# Front left outer
lift_rotor_hub_front_lo = Component(stp_entity_names=['Rotor_1_Hub'], name='lift_rotor_hub_front_left_outer',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_hub_front_lo)
lift_rotor_hub_front_lo.add_ffd_parameter(
    FFDTranslationXParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_hub_front_lo.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_hub_front_lo.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_flo_point_location = np.array([5.070,-18.750,7.355])
lr_flo_ps,_ = geo.project_points(lr_flo_point_location, projection_targets_names=['lift_rotor_hub_front_left_outer'])
wing_flo_ps,_ =  geo.project_points(lr_flo_point_location, projection_targets_names=['front_wing'])
lf_flo_wing_connection_ps = geo.subtract_pointsets(lr_flo_ps,wing_flo_ps)
geo.add_constraint(
    DisplacementCalculation(lf_flo_wing_connection_ps)
)

# Front left inner
lift_rotor_hub_front_li = Component(stp_entity_names=['Rotor_3_Hub'], name='lift_rotor_hub_front_left_inner',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_hub_front_li)
lift_rotor_hub_front_li.add_ffd_parameter(
    FFDTranslationXParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_hub_front_li.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_hub_front_li.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_fli_point_location = np.array([4.630,-8.217,7.659])
lr_fli_ps,_ = geo.project_points(lr_fli_point_location, projection_targets_names=['lift_rotor_hub_front_left_inner'])
wing_fli_ps,_ =  geo.project_points(lr_fli_point_location, projection_targets_names=['front_wing'])
lf_fli_wing_connection_ps = geo.subtract_pointsets(lr_fli_ps,wing_fli_ps)
geo.add_constraint(
    DisplacementCalculation(lf_fli_wing_connection_ps)
)

# Front right inner
lift_rotor_hub_front_ri = Component(stp_entity_names=['Rotor_5_Hub'], name='lift_rotor_hub_front_right_inner',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_hub_front_ri)
lift_rotor_hub_front_ri.add_ffd_parameter(
    FFDTranslationXParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_hub_front_ri.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_hub_front_ri.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_fri_point_location = np.array([4.630,8.217,7.659])
lr_fri_ps,_ = geo.project_points(lr_fri_point_location, projection_targets_names=['lift_rotor_hub_front_right_inner'])
wing_fri_ps,_ =  geo.project_points(lr_fri_point_location, projection_targets_names=['front_wing'])
lf_fri_wing_connection_ps = geo.subtract_pointsets(lr_fri_ps,wing_fri_ps)
geo.add_constraint(
    DisplacementCalculation(lf_fri_wing_connection_ps)
)

# Front right outer
lift_rotor_hub_front_ro = Component(stp_entity_names=['Rotor_7_Hub'], name='lift_rotor_hub_front_right_outer',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_hub_front_ro)
lift_rotor_hub_front_ro.add_ffd_parameter(
    FFDTranslationXParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_hub_front_ro.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_hub_front_ro.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_fro_point_location = np.array([5.070,18.750,7.355])
lr_fro_ps,_ = geo.project_points(lr_fro_point_location, projection_targets_names=['lift_rotor_hub_front_right_outer'])
wing_fro_ps,_ =  geo.project_points(lr_fro_point_location, projection_targets_names=['front_wing'])
lf_fro_wing_connection_ps = geo.subtract_pointsets(lr_fro_ps,wing_fro_ps)
geo.add_constraint(
    DisplacementCalculation(lf_fro_wing_connection_ps)
)

# Rear left outer
lift_rotor_hub_rear_lo = Component(stp_entity_names=['Rotor_2_Hub'], name='lift_rotor_hub_rear_left_outer',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_hub_rear_lo)
lift_rotor_hub_rear_lo.add_ffd_parameter(
    FFDTranslationXParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_hub_rear_lo.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_hub_rear_lo.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_rlo_point_location = np.array([19.200,-18.750,9.635])
lr_rlo_ps,_ = geo.project_points(lr_rlo_point_location, projection_targets_names=['lift_rotor_hub_rear_left_outer'])
wing_rlo_ps,_ =  geo.project_points(lr_rlo_point_location, projection_targets_names=['front_wing'])
lf_rlo_wing_connection_ps = geo.subtract_pointsets(lr_rlo_ps,wing_rlo_ps)
geo.add_constraint(
    DisplacementCalculation(lf_rlo_wing_connection_ps)
)


# Rear left inner
lift_rotor_hub_rear_li = Component(stp_entity_names=['Rotor_4_Hub'], name='lift_rotor_hub_rear_left_inner',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_hub_rear_li)
lift_rotor_hub_rear_li.add_ffd_parameter(
    FFDTranslationXParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_hub_rear_li.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_hub_rear_li.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_rli_point_location = np.array([18.760,-8.537,9.919])
lr_rli_ps,_ = geo.project_points(lr_rli_point_location, projection_targets_names=['lift_rotor_hub_rear_left_inner'])
wing_rli_ps,_ =  geo.project_points(lr_rli_point_location, projection_targets_names=['front_wing'])
lf_rli_wing_connection_ps = geo.subtract_pointsets(lr_rli_ps,wing_rli_ps)
geo.add_constraint(
    DisplacementCalculation(lf_rli_wing_connection_ps)
)


# Rear right inner
lift_rotor_hub_rear_ri = Component(stp_entity_names=['Rotor_6_Hub'], name='lift_rotor_hub_rear_right_inner',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_hub_rear_ri)
lift_rotor_hub_rear_ri.add_ffd_parameter(
    FFDTranslationXParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_hub_rear_ri.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_hub_rear_ri.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_rri_point_location = np.array([18.760,8.537,9.919])
lr_rri_ps,_ = geo.project_points(lr_rri_point_location, projection_targets_names=['lift_rotor_hub_rear_right_inner'])
wing_rri_ps,_ =  geo.project_points(lr_rri_point_location, projection_targets_names=['front_wing'])
lf_rri_wing_connection_ps = geo.subtract_pointsets(lr_rri_ps,wing_rri_ps)
geo.add_constraint(
    DisplacementCalculation(lf_rri_wing_connection_ps)
)

# Rear right outer
lift_rotor_hub_rear_ro = Component(stp_entity_names=['Rotor_8_Hub'], name='lift_rotor_hub_rear_right_outer',nxp=2,nyp=2,nzp=2)
geo.add_component(lift_rotor_hub_rear_ro)
lift_rotor_hub_rear_ro.add_ffd_parameter(
    FFDTranslationXParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_hub_rear_ro.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
lift_rotor_hub_rear_ro.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
lr_rro_point_location = np.array([19.200,18.750,9.635])
lr_rro_ps,_ = geo.project_points(lr_rro_point_location, projection_targets_names=['lift_rotor_hub_rear_right_outer'])
wing_rro_ps,_ =  geo.project_points(lr_rro_point_location, projection_targets_names=['front_wing'])
lf_rro_wing_connection_ps = geo.subtract_pointsets(lr_rro_ps,wing_rro_ps)
geo.add_constraint(
    DisplacementCalculation(lf_rro_wing_connection_ps)
)

# Pusher rotor
pusher_rotor_hub = Component(stp_entity_names=['Rotor_9_Hub'], name='pusher_rotor_hub',nxp=2,nyp=2,nzp=2)
geo.add_component(pusher_rotor_hub)
pusher_rotor_hub.add_ffd_parameter(
    FFDTranslationXParameter(degree=0, num_dof=1, cost_factor=1)
)
pusher_rotor_hub.add_ffd_parameter(
    FFDTranslationYParameter(degree=0, num_dof=1, cost_factor=1)
)
pusher_rotor_hub.add_ffd_parameter(
    FFDTranslationZParameter(degree=0, num_dof=1, cost_factor=1)
)
pusher_point_location = np.array([32.,0.,8.])
tail_point_location = np.array([30.550,0.,8.008])
pusher_ps,_ = geo.project_points(pusher_point_location, projection_targets_names=['pusher_rotor_hub'])
tail_ps,_ = geo.project_points(tail_point_location, projection_targets_names=['tail'])
hub_tail_connection_ps = geo.subtract_pointsets(pusher_ps,tail_ps)
geo.add_constraint(
    DisplacementCalculation(hub_tail_connection_ps)
)
# Magnitude calculation (only)
# end region

# region Thrust vector
front_lo_thrust_vector_origin = generate_thrust_vector(geo, lift_rotor_hub_front_lo)
front_li_thrust_vector_origin = generate_thrust_vector(geo, lift_rotor_hub_front_li)
front_ri_thrust_vector_origin = generate_thrust_vector(geo, lift_rotor_hub_front_ri)
front_ro_thrust_vector_origin = generate_thrust_vector(geo, lift_rotor_hub_front_ro)
rear_lo_thrust_vector_origin = generate_thrust_vector(geo, lift_rotor_hub_rear_lo)
rear_li_thrust_vector_origin = generate_thrust_vector(geo, lift_rotor_hub_rear_li)
rear_ri_thrust_vector_origin = generate_thrust_vector(geo, lift_rotor_hub_rear_ri)
rear_ro_thrust_vector_origin = generate_thrust_vector(geo, lift_rotor_hub_rear_ro)
pusher_thrust_vector_origin = generate_thrust_vector(geo, pusher_rotor_hub)
# endregion



# Region Corner points
# bot_surfaces = [
#     'FrontWing, 0, 3', 'FrontWing, 0, 7','FrontWing, 0, 11','FrontWing, 0, 15',
#     'FrontWing, 1, 23', 'FrontWing, 1, 27','FrontWing, 1, 31','FrontWing, 1, 35' 
# ]
bot_surfaces = [
    'FrontWing, 0, 67', 'FrontWing, 0, 71','FrontWing, 0, 75','FrontWing, 0, 79',
    'FrontWing, 1, 87', 'FrontWing, 1, 91','FrontWing, 1, 95','FrontWing, 1, 99' 
]
# top_surfaces = [
#     'FrontWing, 0, 4', 'FrontWing, 0, 8','FrontWing, 0, 12','FrontWing, 0, 16',
#     'FrontWing, 1, 24','FrontWing, 1, 27','FrontWing, 1, 36','FrontWing, 1, 32'
# ]
top_surfaces = [
    'FrontWing, 0, 68', 'FrontWing, 0, 72','FrontWing, 0, 76','FrontWing, 0, 80',
    'FrontWing, 1, 88','FrontWing, 1, 92','FrontWing, 1, 96','FrontWing, 1, 100'
]
# # Corner points left

point00 = np.array([12.356, 25.250, 7.618 + 0.1]) # * ft2m
point01 = np.array([13.400, 25.250, 7.617 + 0.1]) # * ft2m
point10 = np.array([8.892,    0.000, 8.633 + 0.1]) # * ft2m
point11 = np.array([14.332,   0.000, 8.439 + 0.1]) # * ft2m

fwing_lead_section_1_left, fwing_trail_section_1_left, fwing_lead_left_mid, fwing_trail_left_mid = generate_corner_points(
    geo,
    'front_wing', 
    point00, 
    point01, 
    point10, 
    point11)
fwing_left_top, fwing_left_bot, fwing_chord_surface_left, fwing_camber_surface_left = generate_camber_mesh(
    geo, 
    fwing_lead_section_1_left, 
    fwing_trail_section_1_left, 
    fwing_lead_left_mid,
    fwing_trail_left_mid, 
    top_surfaces, 
    bot_surfaces, 
    "front_wing_left_section_1")


point00 = np.array([12.356, -25.250, 7.618 + 0.1]) # * ft2m
point01 = np.array([13.400, -25.250, 7.617 + 0.1]) # * ft2m
point10 = np.array([8.892,    0.000, 8.633 + 0.1]) # * ft2m
point11 = np.array([14.332,   0.000, 8.439 + 0.1]) # * ft2m

fwing_lead_section_1_right, fwing_trail_section_1_right, fwing_lead_right_mid, fwing_trail_right_mid = generate_corner_points(
    geo,
    'front_wing', 
    point00, 
    point01, 
    point10, 
    point11)
fwing_right_top, fwing_right_bot, fwing_chord_surface_right, fwing_camber_surface_right = generate_camber_mesh(
    geo, 
    fwing_lead_section_1_right, 
    fwing_trail_section_1_right, 
    fwing_lead_right_mid,
    fwing_trail_right_mid, 
    top_surfaces, 
    bot_surfaces, 
    'front_wing_right_section_1')


# ------------ Tail Section ------------ # 
# bot_surfaces = [
#     'Tail_1, 0, 43', 
#     'Tail_1, 1, 51',
# ]
bot_surfaces = [
    'Tail_1, 0, 127', 
    'Tail_1, 1, 135',
]
# top_surfaces = [
#     'Tail_1, 0, 44',
#     'Tail_1, 1, 52',
# ]
top_surfaces = [
    'Tail_1, 0, 128',
    'Tail_1, 1, 136',
]

# for name in tail.embedded_entity_names:
#     surface = geo.input_bspline_entity_dict[name]
#     vp_init = Plotter()
#     vps1 = Points(surface.control_points, r=8, c = 'blue')
#     # vps.append(vps2)
#     vp_init.show(vps1, f'{surface.name}', axes=1, viewup="z", interactive = True)
# exit()
# Corner points left
# Maybe change projection direction towards surface x-direction --> keeping y and z exact
# plot fwing_lead_section_1_left...on top of control points (n2 diagram in prescribed actuation model)
point00 = np.array([27.806, 6.520, 8.008 + 0.1]) # * ft2m
point01 = np.array([30.050, 6.520, 8.013 + 0.1]) # * ft2m
point10 = np.array([27.428, 0.000, 8.008 + 0.1]) # * ft2m
point11 = np.array([31.187, 0.000, 8.013 + 0.1]) # * ft2m

tail_lead_left, tail_trail_left, tail_lead_left_mid, tail_trail_left_mid = generate_corner_points(
    geo,
    'tail', 
    point00, 
    point01, 
    point10, 
    point11)
tail_left_top, tail_left_bot, tail_chord_surface_left, tail_camber_surface_left = generate_camber_mesh(
    geo, 
    tail_lead_left, 
    tail_trail_left, 
    tail_lead_left_mid,
    tail_trail_left_mid, 
    top_surfaces, 
    bot_surfaces, 
    "tail_left")


#  Corner points right
point00 = np.array([27.806, -6.520, 8.008 + 0.1]) # * ft2m
point01 = np.array([30.050, -6.520, 8.013 + 0.1]) # * ft2m
point10 = np.array([27.428, 0.000, 8.008 + 0.1]) # * ft2m
point11 = np.array([31.187, 0.000, 8.013 + 0.1]) # * ft2m

tail_lead_right, tail_trail_right, tail_lead_right_mid, tail_trail_right_mid  = generate_corner_points(
    geo,
    'tail', 
    point00, 
    point01, 
    point10, 
    point11)
tail_right_top, tail_right_bot, tail_chord_surface_right, tail_camber_surface_right = generate_camber_mesh(
    geo, 
    tail_lead_right, 
    tail_trail_right, 
    tail_lead_right_mid,
    tail_trail_right_mid, 
    top_surfaces, 
    bot_surfaces, 
    'tail_right')
# end region

# Region: Inputs and constraints to geometry model and geometric outputs
# region Geometric Outputs
# ---- Wing ---- #
root_chord_ps = geo.subtract_pointsets(fwing_lead_left_mid,fwing_trail_left_mid)
tip_chord_ps_left = geo.subtract_pointsets(fwing_lead_section_1_left,fwing_trail_section_1_left)
tip_chord_ps_right = geo.subtract_pointsets(fwing_lead_section_1_right,fwing_trail_section_1_right)
LE_length_ps = geo.subtract_pointsets(fwing_lead_section_1_left,fwing_lead_left_mid)
TE_length_ps = geo.subtract_pointsets(fwing_trail_section_1_left,fwing_trail_left_mid)
span_ps = geo.subtract_pointsets(fwing_trail_section_1_left,fwing_trail_section_1_right)
# ---- Horizontal tail ---- #
root_chord_ps_htail = geo.subtract_pointsets(tail_lead_left_mid,tail_trail_left_mid)
tip_chord_ps_left_htail = geo.subtract_pointsets(tail_lead_left,tail_trail_left)
tip_chord_ps_right_htail = geo.subtract_pointsets(tail_lead_right,tail_trail_right)
LE_length_ps_htail = geo.subtract_pointsets(tail_lead_left,tail_lead_left_mid)
TE_length_ps_htail = geo.subtract_pointsets(tail_trail_left,tail_trail_left_mid)
span_ps_htail = geo.subtract_pointsets(tail_trail_left,tail_trail_right)
# ---- Tail moment arm ---- #
tail_to_wing_distance_ps = geo.subtract_pointsets(fwing_trail_left_mid, tail_lead_left_mid)
# ---- Rotor diameters ---- # 


# region geometric design variables
# ---- Wing ---- #
geo.add_input(
    MagnitudeCalculation(span_ps),
    connection_name='wing_span' # connection_name: looking for this name to make connection
)
geo.add_input(
    MagnitudeCalculation(root_chord_ps),
    connection_name='wing_root_chord', 
)
geo.add_input(
    MagnitudeCalculation(tip_chord_ps_left),
    connection_name='wing_tip_chord_left', 
)
geo.add_input(
    MagnitudeCalculation(tip_chord_ps_right),
    connection_name='wing_tip_chord_right', 
)
# ---- Horizontal tail ---- #
geo.add_input(
    MagnitudeCalculation(span_ps_htail),
    connection_name='htail_span'
)
geo.add_input(
    MagnitudeCalculation(root_chord_ps_htail),
    connection_name='htail_root_chord', 
)
geo.add_input(
    MagnitudeCalculation(tip_chord_ps_left_htail),
    connection_name='htail_tip_chord_left', 
)
geo.add_input(
    MagnitudeCalculation(tip_chord_ps_right_htail),
    connection_name='htail_tip_chord_right', 
)
# ---- Tail moment arm ---- #
geo.add_input(
    MagnitudeCalculation(tail_to_wing_distance_ps),
    connection_name='tail_moment_arm',
)
# ---- Rotor diameters ---- #
flo_1 = np.array([5.070,-13.750,6.730])
flo_2 = np.array([5.070,-23.750,6.730])
flo_3 = np.array([10.070,-18.750,6.730])
flo_4 = np.array([0.070,-18.750,6.730])
flo_ps_1,_ = geo.project_points(flo_1, projection_targets_names=['lift_rotor_disk_front_left_outer'])
flo_ps_2,_ = geo.project_points(flo_2, projection_targets_names=['lift_rotor_disk_front_left_outer'])
flo_ps_3,_ = geo.project_points(flo_3, projection_targets_names=['lift_rotor_disk_front_left_outer'])
flo_ps_4,_ = geo.project_points(flo_4, projection_targets_names=['lift_rotor_disk_front_left_outer'])
flo_ps = geo.subtract_pointsets(flo_ps_1,flo_ps_2)
flo_ps_2 = geo.subtract_pointsets(flo_ps_3,flo_ps_4)
geo.add_input(
    MagnitudeCalculation(flo_ps),
    connection_name='flo_diameter'
)
geo.add_input(
    MagnitudeCalculation(flo_ps_2),
    connection_name='flo_diameter_2'
)

fli_1 = np.array([4.630,-3.499,7.736])
fli_2 = np.array([4.630,-13.401,6.344])
fli_3 = np.array([9.630,-8.450,7.047])
fli_4 = np.array([-0.370,-8.450,7.047])
fli_ps_1,_ = geo.project_points(fli_1, projection_targets_names=['lift_rotor_disk_front_left_inner'])
fli_ps_2,_ = geo.project_points(fli_2, projection_targets_names=['lift_rotor_disk_front_left_inner'])
fli_ps_3,_ = geo.project_points(fli_3, projection_targets_names=['lift_rotor_disk_front_left_inner'])
fli_ps_4,_ = geo.project_points(fli_4, projection_targets_names=['lift_rotor_disk_front_left_inner'])
fli_ps = geo.subtract_pointsets(fli_ps_1,fli_ps_2)
fli_ps_2 = geo.subtract_pointsets(fli_ps_3,fli_ps_4)
geo.add_input(
    MagnitudeCalculation(fli_ps),
    connection_name='fli_diameter'
)
geo.add_input(
    MagnitudeCalculation(fli_ps_2),
    connection_name='fli_diameter_2'
)

fri_1 = np.array([4.630,3.499,7.736])
fri_2 = np.array([4.630,13.401,6.344])
fri_3 = np.array([9.630,8.450,7.047])
fri_4 = np.array([-0.370,8.450,7.047])
fri_ps_1,_ = geo.project_points(fri_1, projection_targets_names=['lift_rotor_disk_front_right_inner'])
fri_ps_2,_ = geo.project_points(fri_2, projection_targets_names=['lift_rotor_disk_front_right_inner'])
fri_ps_3,_ = geo.project_points(fri_3, projection_targets_names=['lift_rotor_disk_front_right_inner'])
fri_ps_4,_ = geo.project_points(fri_4, projection_targets_names=['lift_rotor_disk_front_right_inner'])
fri_ps = geo.subtract_pointsets(fri_ps_1,fri_ps_2)
fri_ps_2 = geo.subtract_pointsets(fri_ps_3,fri_ps_4)
geo.add_input(
    MagnitudeCalculation(fri_ps),
    connection_name='fri_diameter'
)
geo.add_input(
    MagnitudeCalculation(fri_ps_2),
    connection_name='fri_diameter_2'
)

fro_1 = np.array([5.070,13.750,6.730])
fro_2 = np.array([5.070,23.750,6.730])
fro_3 = np.array([10.070,18.750,6.730])
fro_4 = np.array([0.070,18.750,6.730])
fro_ps_1,_ = geo.project_points(fro_1, projection_targets_names=['lift_rotor_disk_front_right_outer'])
fro_ps_2,_ = geo.project_points(fro_2, projection_targets_names=['lift_rotor_disk_front_right_outer'])
fro_ps_3,_ = geo.project_points(fro_3, projection_targets_names=['lift_rotor_disk_front_right_outer'])
fro_ps_4,_ = geo.project_points(fro_4, projection_targets_names=['lift_rotor_disk_front_right_outer'])
fro_ps = geo.subtract_pointsets(fro_ps_1,fro_ps_2)
fro_ps_2 = geo.subtract_pointsets(fro_ps_3,fro_ps_4)
geo.add_input(
    MagnitudeCalculation(fro_ps),
    connection_name='fro_diameter'
)
geo.add_input(
    MagnitudeCalculation(fro_ps_2),
    connection_name='fro_diameter_2'
)

rlo_1 = np.array([19.200,-13.750,9.010])
rlo_2 = np.array([19.200,-23.750,9.010])
rlo_3 = np.array([24.200,-18.750,9.010])
rlo_4 = np.array([14.200,-18.750,9.010])
rlo_ps_1,_ = geo.project_points(rlo_1, projection_targets_names=['lift_rotor_disk_rear_left_outer'])
rlo_ps_2,_ = geo.project_points(rlo_2, projection_targets_names=['lift_rotor_disk_rear_left_outer'])
rlo_ps_3,_ = geo.project_points(rlo_3, projection_targets_names=['lift_rotor_disk_rear_left_outer'])
rlo_ps_4,_ = geo.project_points(rlo_4, projection_targets_names=['lift_rotor_disk_rear_left_outer'])
rlo_ps = geo.subtract_pointsets(rlo_ps_1,rlo_ps_2)
rlo_ps_2 = geo.subtract_pointsets(rlo_ps_3,rlo_ps_4)
geo.add_input(
    MagnitudeCalculation(rlo_ps),
    connection_name='rlo_diameter'
)
geo.add_input(
    MagnitudeCalculation(rlo_ps_2),
    connection_name='rlo_diameter_2'
)

rli_1 = np.array([18.760,-3.499,9.996])
rli_2 = np.array([18.760,-13.401,8.604])
rli_3 = np.array([23.760,-8.450,9.300])
rli_4 = np.array([13.760,-8.450,9.300])
rli_ps_1,_ = geo.project_points(rli_1, projection_targets_names=['lift_rotor_disk_rear_left_inner'])
rli_ps_2,_ = geo.project_points(rli_2, projection_targets_names=['lift_rotor_disk_rear_left_inner'])
rli_ps_3,_ = geo.project_points(rli_3, projection_targets_names=['lift_rotor_disk_rear_left_inner'])
rli_ps_4,_ = geo.project_points(rli_4, projection_targets_names=['lift_rotor_disk_rear_left_inner'])
rli_ps = geo.subtract_pointsets(rli_ps_1,rli_ps_2)
rli_ps_2 = geo.subtract_pointsets(rli_ps_3,rli_ps_4)
geo.add_input(
    MagnitudeCalculation(rli_ps),
    connection_name='rli_diameter'
)
geo.add_input(
    MagnitudeCalculation(rli_ps_2),
    connection_name='rli_diameter_2'
)

rri_1 = np.array([18.760,3.499,9.996])
rri_2 = np.array([18.760,13.401,8.604])
rri_3 = np.array([23.760,8.450,9.300])
rri_4 = np.array([13.760,8.450,9.300])
rri_ps_1,_ = geo.project_points(rri_1, projection_targets_names=['lift_rotor_disk_rear_right_inner'])
rri_ps_2,_ = geo.project_points(rri_2, projection_targets_names=['lift_rotor_disk_rear_right_inner'])
rri_ps_3,_ = geo.project_points(rri_3, projection_targets_names=['lift_rotor_disk_rear_right_inner'])
rri_ps_4,_ = geo.project_points(rri_4, projection_targets_names=['lift_rotor_disk_rear_right_inner'])
rri_ps = geo.subtract_pointsets(rri_ps_1,rri_ps_2)
rri_ps_2 = geo.subtract_pointsets(rri_ps_3,rri_ps_4)
geo.add_input(
    MagnitudeCalculation(rri_ps),
    connection_name='rri_diameter'
)
geo.add_input(
    MagnitudeCalculation(rri_ps_2),
    connection_name='rri_diameter_2'
)

rro_1 = np.array([19.200,13.750,9.010])
rro_2 = np.array([19.200,23.750,9.010])
rro_3 = np.array([24.200,18.750,9.010])
rro_4 = np.array([14.200,18.750,9.010])
rro_ps_1,_ = geo.project_points(rro_1, projection_targets_names=['lift_rotor_disk_rear_right_outer'])
rro_ps_2,_ = geo.project_points(rro_2, projection_targets_names=['lift_rotor_disk_rear_right_outer'])
rro_ps_3,_ = geo.project_points(rro_3, projection_targets_names=['lift_rotor_disk_rear_right_outer'])
rro_ps_4,_ = geo.project_points(rro_4, projection_targets_names=['lift_rotor_disk_rear_right_outer'])
rro_ps = geo.subtract_pointsets(rro_ps_1,rro_ps_2)
rro_ps_2 = geo.subtract_pointsets(rro_ps_3,rro_ps_4)
geo.add_input(
    MagnitudeCalculation(rro_ps),
    connection_name='rro_diameter'
)
geo.add_input(
    MagnitudeCalculation(rro_ps_2),
    connection_name='rro_diameter_2'
)

rro_1 = np.array([31.94,0,3.290])
rro_2 = np.array([31.94,0,12.290])
rro_3 = np.array([31.94,-4.5,7.790])
rro_4 = np.array([31.94,4.5,7.790])
rro_ps_1,_ = geo.project_points(rro_1, projection_targets_names=['pusher_rotor_disk'])
rro_ps_2,_ = geo.project_points(rro_2, projection_targets_names=['pusher_rotor_disk'])
rro_ps_3,_ = geo.project_points(rro_3, projection_targets_names=['pusher_rotor_disk'])
rro_ps_4,_ = geo.project_points(rro_4, projection_targets_names=['pusher_rotor_disk'])
rro_ps = geo.subtract_pointsets(rro_ps_1,rro_ps_2)
rro_ps_2 = geo.subtract_pointsets(rro_ps_3,rro_ps_4)
geo.add_input(
    MagnitudeCalculation(rro_ps),
    connection_name='pusher_diameter'
)
geo.add_input(
    MagnitudeCalculation(rro_ps_2),
    connection_name='pusher_diameter_2'
)


# geo.add_geometric_outputs(geo_outputs=geo_outputs)

concept.add_geometry(geometry=geo)
# end region

# concept.add_geometry(geometry=geo)


# Region mesh
# region Mesh
# VLM mesh
vlm_mesh = VLMMesh(aircraft.parameters['name']+'Mesh', [
    fwing_camber_surface_left, fwing_camber_surface_right,
    tail_camber_surface_left, tail_camber_surface_right,
])

aircraft.add_mesh(vlm_mesh)

# region Actuation
elev_def_actuation = Actuation(
    name=ActuationEnums.ElevDef.value,
    geo=geo,
    origin=tail_trail_right,
    end_point=tail_trail_left,
    actuating_components=[tail]
)
# endregion

caddee.add_concept(concept=concept)

geo.assemble()
geo.evaluate()
# endregion