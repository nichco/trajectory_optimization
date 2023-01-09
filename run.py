import csdl
import numpy as np
import python_csdl_backend
from odeproblemtest import ODEProblemTest
from timestep import timestep
from modopt.scipy_library import SLSQP
# from modopt.snopt_library import SNOPT
from modopt.csdl_library import CSDLProblem
import matplotlib.pyplot as plt
from skmd import tonal


class RunModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('options')

    def define(self):
        options = self.parameters['options']
        self.create_input('dt',options['dt'])
        self.add(timestep(num=num), name='timestep') # add the time vector to the model
        
        # add dynamic inputs to the csdl model
        self.create_input('control_x',options['control_x_i'])
        self.create_input('control_z',options['control_z_i'])
        self.create_input('control_alpha',options['control_alpha_i'])
        # initial conditions for states
        self.create_input('v_0', options['v_0'])
        self.create_input('gamma_0', options['gamma_0'])
        self.create_input('h_0', options['h_0'])
        self.create_input('x_0', options['x_0'])
        self.create_input('e_0', 0)

        # create model containing the integrator
        optionsdict = {'options': options}
        self.add(ODEProblem.create_solver_model(ODE_parameters=optionsdict, profile_parameters=optionsdict), 'subgroup')

        # declare variables from integrator
        v = self.declare_variable('v', shape=(num,))
        gamma = self.declare_variable('gamma', shape=(num,))
        h = self.declare_variable('h', shape=(num,))
        e = self.declare_variable('e', shape=(num,))
        alpha = self.declare_variable('control_alpha', shape=(num,))
        cruisepower = self.declare_variable('cruisepower', shape=(num,))
        liftpower = self.declare_variable('liftpower', shape=(num,))

        # max power constraints
        self.register_output('max_cruise_power', csdl.max(cruisepower))
        self.register_output('max_lift_power', csdl.max(liftpower))
        # only for min dt case
        self.add_constraint('max_cruise_power', upper=options['max_cruise_power'], scaler=1E-6)
        self.add_constraint('max_lift_power', upper=options['max_lift_power'], scaler=1E-6)

        # final altitude constraint
        self.register_output('final_h', h[-1])
        self.add_constraint('final_h', equals=options['h_f'], scaler=0.01)

        # min altitude constraint
        self.register_output('min_h', csdl.min(h))
        self.add_constraint('min_h', lower=options['h_0'] - 0.01)

        # final velocity constraint
        self.register_output('final_v',v[-1])
        self.add_constraint('final_v',lower=options['v_f'],scaler=0.01) #0.1
        
        # pitch angle constraint
        self.register_output('theta',gamma + alpha)
        self.register_output('max_theta',csdl.max((theta**2)**0.5))
        #self.add_constraint('max_theta',upper=np.deg2rad(15))
        
        # flight path angle constraints
        self.register_output('final_gamma',gamma[-1])
        #self.add_constraint('final_gamma',equals=0)
        
        # acoustic constraints
        self.add(tonal(options=options,num=num), name='tonal')
        # self.add_constraint('max_spl_gl',upper=np.linspace(120,60,num),scaler=1E-2)
        # self.add_constraint('seg_ospl',upper=70,scaler=1E-2)
        
        # compute total energy
        energy = e[-1]
        self.register_output('energy',energy)
        self.print_var(energy)
       
        
        """
        # for the minimum energy objective
        self.add_design_variable('control_alpha',lower=-np.pi/2,upper=np.pi/2,scaler=5)
        self.add_design_variable('control_x',lower=0, scaler=2E-3)
        self.add_design_variable('control_z',lower=0, scaler=np.linspace(1E-3,1,num))
        self.add_design_variable('dt',lower=2.0)
        self.add_objective('energy', scaler=5E-3)
        """
        
        # for the minimum time objective
        #self.add_design_variable('control_alpha',lower=-np.pi/2,upper=np.pi/2,scaler=np.linspace(0.1,10,num))
        #self.add_design_variable('control_x',lower=100, scaler=1E-2) # 1E-2
        #self.add_design_variable('control_z',lower=100, scaler=np.linspace(1E-3,1E-2,num))
        #self.add_design_variable('dt',lower=0.5)
        
        self.add_design_variable('control_alpha',scaler=1)
        #self.add_design_variable('control_alpha',lower=-np.pi/2,upper=np.pi/2,scaler=1/options['control_alpha_i'])
        self.add_design_variable('control_x',lower=0, scaler=1/options['control_x_i'])
        self.add_design_variable('control_z',lower=0, scaler=1/options['control_z_i'])
        self.add_design_variable('dt',lower=0.5)
        
        self.add_objective('dt', scaler=1)
        





options = {} # aircraft and mission parameter dictionary
# aircraft data
options['mass'] = 2000 # 3724 (kg)
options['wing_area'] = 19.6 # (m^2)
options['aspect_ratio'] = 12.13
options['wing_set_angle'] = 2 # (deg)
options['max_cruise_power'] = 468300 # (w)
options['max_lift_power'] = 103652 # (w)
options['span_efficiency'] = 0.8 # finite wing correction
options['cd_0'] = 0.02 # zero-lift drag coefficient
options['cruise_rotor_diameter'] = 2.1 # 2.7(m)
options['lift_rotor_diameter'] = 2.0 # 3 (m)
options['num_lift_rotors'] = 8
options['num_cruise_blades'] = 4 # 6
options['num_lift_blades'] = 2
options['cruise_mac'] = 0.15
options['lift_mac'] = 0.15
options['c_sigma'] = 0.19
options['l_sigma'] = 0.095
options['energy_scale'] = 0.0001 # scale energy for plotting
# mission parameters
options['gravity'] = 9.81 # (m/s^2)
options['v_0'] = 5 # (m/s)
options['gamma_0'] = 0 # (rad)
options['h_0'] = 0 # (m)
options['x_0'] = 0 # (m)
options['alpha_0'] = 0 # (rad)
options['h_f'] = 300 # (m)
options['v_f'] = 43 # (m/s)
options['gamma_f'] = 0 # (rad)
# initial control inputs
"""
options['control_x_i'] = np.ones(30)*2300
options['control_z_i'] = np.linspace(800, 100, 30)
options['control_alpha_i'] = np.linspace(0.7, 0, 30)
"""

# min dt seed (nominal)
options['control_x_i'] = np.array([2124.13625581,2131.85137181,2173.32871553,2221.14842109,2211.97107647,
 2253.94998617,2283.94352147,2295.5992903 ,2316.90292026,2342.79358487,
 2371.42128359,2390.58872052,2409.09692677,2417.24569485,2431.01859621,
 2435.37545702,2433.47574519,2445.19160333,2444.59070292,2443.17137773,
 2438.93740276,2431.62005851,2422.94582173,2414.71572079,2406.74762457,
 2395.13693941,2379.00683575,2368.49732601,2360.80539598,2363.20423794])
options['control_z_i'] = np.array([1391.03885706,1412.28184079,1412.88860698,  75.09129593,1415.95990782,
 1398.94466644, 162.73287255, 160.01535156, 446.44999321, 691.36592683,
  814.3809006 , 684.99600039, 538.1194686 , 322.28483515, 178.86236356,
   92.83576285,  89.98986905,  70.9233124 , 102.82238731, 113.09650619,
  132.71345529, 146.66168001, 151.09341074, 145.44429626, 130.38432298,
  110.05903573,  99.83456811, 100.76277145, 101.29060202, 100.30287394])
options['control_alpha_i'] = np.array([ 6.05104362e-01, 9.17275848e-01, 6.28184348e-01, 8.18451160e-02,
  5.70286893e-01, 3.71744776e-01,-6.27051734e-02, 1.26402913e-02,
  8.65766877e-03, 5.87690705e-03, 2.09147476e-02, 1.84744231e-02,
  1.56924716e-02, 8.11560687e-03, 2.85936566e-03, 2.31221376e-05,
  2.65966992e-03, 3.88602372e-06, 1.67717346e-06, 5.74405904e-05,
  4.79364564e-06, 4.84033968e-06, 6.52660577e-04, 1.21426324e-05,
  5.07808276e-03, 3.01812672e-03, 5.17933611e-03, 3.92630144e-03,
  1.27397383e-02, 7.33241619e-20])


"""
# min e seed (nominal)
options['control_x_i'] = np.array([1413.51319542, 1753.71102218, 1728.87276412, 1399.89367014, 1392.52378402,
 1386.93435368, 1400.36858451, 1422.7035186,  1467.58011543, 1517.77141772,
 1541.46126329, 1541.41195974, 1530.897933 ,  1517.56486893, 1510.49175146,
 1510.9059217 , 1514.51576295, 1519.456195 ,  1522.77545268, 1524.5415462,
 1520.37811981, 1518.77123738, 1532.64602281, 1558.62303483, 1590.60344804,
 1605.23621351, 1563.17053215, 1467.44094911, 1353.45810529, 1283.94980524])
options['control_z_i'] = np.array([1622.92466456, 1107.07708667,  684.03697425,  359.62226127,  205.54080207,
  173.58805183,  107.55597198,  100.19190181,  100.,          100.,
  100.        ,  100.        ,  100.        ,  100.,          100.,
  100.        ,  100.        ,  100.        ,  100.,          100.,
  100.        ,  100.        ,  100.        ,  100.,          100.,
  100.        ,  100.        ,  100.        ,  100.,          100.        ])
options['control_alpha_i'] = np.array([0.87190034, 0.46127608, 0.19230684, 0.15067009, 0.10096179, 0.07442622,
 0.05460498, 0.03274503, 0.02643667, 0.01866871, 0.01497499, 0.00867657,
 0.00695788, 0.00875725, 0.00911545, 0.01233707, 0.01199045, 0.01170604,
 0.01289388, 0.01201674, 0.01109781, 0.00996596, 0.00741877, 0.00729881,
 0.01016355, 0.01307813, 0.02133539, 0.02541958, 0.01869125, 0.00592693])
"""



# ode problem instance
options['dt'] = 0.9095393 #1.21333051 #1.27790049 #2.70794719 # 3.5
num = 30
ODEProblem = ODEProblemTest('RK4', 'time-marching', num_times=num, display='default', visualization='end')
sim = python_csdl_backend.Simulator(RunModel(options=options), analytics=0)
#sim.run()
#sim.check_partials(compact_print=True)

prob = CSDLProblem(problem_name='Trajectory Optimization', simulator=sim)
optimizer = SLSQP(prob, maxiter=2000, ftol=1E-5)
#optimizer = SNOPT(prob,Major_iterations=100,Major_optimality=1e-3,Major_feasibility=1E-3,append2file=True)
optimizer.solve()
optimizer.print_results()
# plot states from integrator
plt.show()

# print total energy
print('dt: ', sim['dt'])
print('total energy: ', sim['energy']/options['energy_scale'])

# assign variables for post-processing
v = sim['v']
gamma = sim['gamma']
h = sim['h']
x = sim['x']
e = sim['e']
dt = sim['dt']
alpha = sim['control_alpha']
cl = sim['cl']
cd = sim['cd']
lift = sim['lift']
drag = sim['drag']
control_x = sim['control_x']
control_z = sim['control_z']
cruisepower = sim['cruisepower']
liftpower = sim['liftpower']
cruise_spl_gl = sim['max_cruise_spl_gl']
lift_spl_gl = sim['max_lift_spl_gl']
ospl = sim['max_spl_gl']
theta = sim['theta']

# post-processing
fig, ((ax1, ax2, ax3, ax4, ax5, ax6), (ax7, ax8, ax9, ax10, ax11, ax12)) = plt.subplots(2, 6)
fig.suptitle('trajectory optimization')
ax1.plot(v,color='b')
ax1.legend(['v'])

ax2.plot(gamma,color='g')
ax2.plot(theta,color='r')
ax2.legend(['gamma','theta'])

ax3.plot(h,color='r')
ax3.legend(['h'])

ax4.plot(x,color='c')
ax4.legend(['x'])

ax5.plot(e,color='m')
ax5.legend(['e'])

ax6.plot(cl)
ax6.plot(cd)
ax6.legend(['cl','cd'])

ax7.plot(alpha,color='k')
ax7.set_title('alpha')
ax7.set_ylabel('rad')

ax8.plot(control_x,color='k')
ax8.set_title('cruise rotor speed')
ax8.set_ylabel('rotor speed (rpm)')

ax9.plot(control_z,color='k')
ax9.set_title('lift rotor speed')
ax9.set_ylabel('rotor speed (rpm)')

ax10.plot(cruisepower,color='k')
ax10.plot(liftpower,color='r')
ax10.set_title('power')
ax10.set_ylabel('power (w)')

ax11.plot(cruise_spl_gl,color='k')
ax11.plot(lift_spl_gl,color='r')
ax11.plot(ospl,color='c')
ax11.set_title('spl')
ax11.set_ylabel('spl (db)')

ax12.plot(lift,color='k')
ax12.plot(drag,color='r')
ax12.legend(['lift','drag'])

plt.show()



