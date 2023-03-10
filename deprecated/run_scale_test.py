import csdl
import numpy as np
import python_csdl_backend
from odeproblemtest import ODEProblemTest
from timestep import timestep
from modopt.scipy_library import SLSQP
from modopt.snopt_library import SNOPT
from modopt.csdl_library import CSDLProblem
import matplotlib.pyplot as plt
from acoustics.skmd import tonal
plt.rcParams['font.family'] = 'Century'
plt.rcParams.update({'font.size': 12})


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
        max_cruise_power = csdl.max(cruisepower)
        max_lift_power = csdl.max(liftpower)
        self.register_output('max_cruise_power', max_cruise_power)
        self.register_output('max_lift_power', max_lift_power)
        # only for min dt case
        #self.add_constraint('max_cruise_power', upper=options['max_cruise_power'], scaler=1E-6)
        #self.add_constraint('max_lift_power', upper=options['max_lift_power'], scaler=1E-6)

        # final altitude constraint
        final_h = h[-1]
        self.register_output('final_h', final_h)
        self.add_constraint('final_h', equals=options['h_f'], scaler=1/options['h_f'])

        # min altitude constraint
        min_h = csdl.min(h)
        self.register_output('min_h', min_h)
        self.add_constraint('min_h', lower=options['h_0']) 

        # final velocity constraint
        final_v = v[-1]
        self.register_output('final_v',final_v)
        self.add_constraint('final_v',lower=options['v_f'],scaler=1/options['v_f'])
        
        # final flight path angle constraint
        final_gamma = gamma[-1]
        self.register_output('final_gamma',final_gamma)
        # self.add_constraint('final_gamma',equals=options['gamma_f'],scaler=1)

        # flight path angle constraints
        theta = gamma + alpha
        self.register_output('theta',theta)
        self.register_output('min_theta',csdl.min(theta))
        self.register_output('max_theta',csdl.max(theta))
        # self.add_constraint('min_theta',lower=-np.deg2rad(17))
        # self.add_constraint('max_theta',upper=np.deg2rad(17))
        
        # acoustic constraints
        self.add(tonal(options=options,num=num), name='tonal')
        # self.add_constraint('max_spl_gl',upper=105,scaler=1E-2)
        # self.add_constraint('max_spl_gl',upper=np.linspace(100,70,num),scaler=1E-2) # 110-75 min e,
        # self.add_constraint('seg_ospl',upper=80,scaler=1E-2)
        
        
        
        
        
        
        # for the minimum energy objective
        """
        self.add_design_variable('control_alpha',lower=-np.pi/2,upper=np.pi/2,scaler=5)
        self.add_design_variable('control_x',lower=0, scaler=2E-3)
        self.add_design_variable('control_z',lower=0, scaler=np.linspace(1E-3,1,num))
        self.add_design_variable('dt',lower=2.0)
        """
        self.add_design_variable('control_alpha',scaler=1/options['control_alpha_i'])
        self.add_design_variable('control_x', scaler=1/options['control_x_i'])
        self.add_design_variable('control_z', scaler=1/options['control_z_i'])
        self.add_design_variable('dt', scaler=1/options['dt'])
        
        energy = e[-1]
        self.register_output('energy',energy)
        self.print_var(energy)
        self.add_objective('energy', scaler=1/1155)
        
        """
        # for the minimum time objective
        #self.add_design_variable('control_alpha',lower=-0.05,upper=np.pi/2,scaler=np.linspace(0.1,10,num))
        #self.add_design_variable('control_x',lower=0, scaler=1E-3) # 1E-2
        #self.add_design_variable('control_z',lower=0, scaler=np.linspace(1E-2,1,num))
        #self.add_design_variable('dt',lower=0.5,scaler=1)
        
        self.add_design_variable('control_alpha',lower=-np.pi/2,upper=np.pi/2,scaler=1/options['control_alpha_i'])
        self.add_design_variable('control_x',lower=0, scaler=1/options['control_x_i']) # 1E-2
        self.add_design_variable('control_z',lower=0, scaler=1/options['control_z_i'])
        self.add_design_variable('dt',lower=0.5,scaler=1)

        energy = e[-1]
        self.register_output('energy',energy)
        self.add_objective('dt', scaler=1E-1)
        """





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
options['h_0'] = -0.1 # (m)
options['x_0'] = 0 # (m)
options['alpha_0'] = 0 # (rad)
options['h_f'] = 300 # (m)
options['v_f'] = 43 # (m/s)
options['gamma_f'] = 0 # (rad)
options['max_spl'] = 100 # (db)
# initial control inputs
"""
options['control_x_i'] = np.ones(30)*2300
options['control_z_i'] = np.linspace(800, 100, 30)
options['control_alpha_i'] = np.linspace(0.7, 0, 30)
"""
"""
# min dt seed (nominal)
options['control_x_i'] = np.array([2104.7695022,  2115.4134416,  2153.00470178, 2213.72873331, 2243.58835329,
 2265.31092023, 2280.0773581 , 2277.0607596 , 2305.60716744, 2322.78056034,
 2335.96183508, 2360.01621271, 2378.15612254, 2399.29355443, 2413.2400634,
 2406.85330201, 2441.97650291, 2438.0228724 , 2452.43674488, 2456.94948004,
 2459.63063656, 2432.70304404, 2441.10719955, 2433.44848836, 2423.97212453,
 2413.07552057, 2401.03752593, 2389.37685222, 2373.43758947, 2368.63876932])
options['control_z_i'] = np.array([1385.9572475,  1378.98939011, 1352.12694977, 1153.93501213,  936.79757382,
  763.80069359,  664.8801888 ,  596.09227073,  538.42229699,  493.78067537,
  470.99409501,  444.99857618,  449.23781374,  458.06379036,  443.96877129,
  428.0284761 ,  402.17005138,  366.89480855,  331.66057602,  297.94748818,
  261.1913302 ,  229.43816243,  197.82240036,  168.18468783,  138.34289863,
  112.30607352,  100.03654335,  100.04349879,  100.05216305,  100.01703125])
options['control_alpha_i'] = np.array([6.14377795e-01, 8.60604153e-01, 9.85703418e-01, 4.43511814e-01,
 3.53745726e-01, 2.49629804e-01, 1.67155793e-01, 4.33161417e-02,
 8.75236776e-03, 5.54205951e-03, 1.73237101e-02, 1.65553491e-02,
 1.65612931e-02, 1.04217025e-02, 3.32734549e-03, 2.31559127e-05,
 3.83681218e-03, 3.88737050e-06, 1.67743048e-06, 5.77316785e-05,
 4.79544581e-06, 4.84186801e-06, 6.75598944e-04, 1.21478833e-05,
 5.90373745e-03, 3.13436882e-03, 5.28815936e-03, 3.92249315e-03,
 1.28720498e-02, 7.33241619e-20])
"""

# min e seed (nominal)
options['control_x_i'] = np.array([1268.12845284,   0.1        ,2100.05144236,1637.80845084,1422.82487331,
 1449.12620821,1432.42592742,1458.51977539,1498.01497006,1550.37734396,
 1588.70767717,1605.86949897,1606.56935326,1598.52105182,1589.89260952,
 1584.40178191,1582.24986872,1582.02425475,1581.83729048,1581.02686546,
 1579.62734004,1582.64839274,1597.014704  ,1621.22673579,1647.30669562,
 1655.65950271,1618.48311923,1525.05580994,1395.92881723,1314.59194183])
options['control_z_i'] = np.array([ 916.16472451,1111.21476252,1031.41891259, 543.02059942, 266.17233874,
  165.81708044, 132.79973794,  96.58519443,  63.35745738,  58.22244513,
   47.912574  ,  33.63755818,  26.94805193,  25.53175259,  26.37558143,
   29.44014377,  32.34648929,  34.00752665,  34.50828915,  33.12491224,
   30.92078578,  28.63260224,  26.83452308,  27.75859342,  33.32778457,
   43.32309535,  56.77658476,  61.41226523,  35.95231821,  44.73794297])
options['control_alpha_i'] = np.array([1.15685929,1.1730702 ,0.22861054,0.18186629,0.11234771,0.08482388,
 0.061465  ,0.04177486,0.02470949,0.02222445,0.01733366,0.00947816,
 0.00589977,0.00495858,0.00566789,0.00742648,0.00889243,0.00969476,
 0.01004468,0.00978091,0.00863016,0.00700407,0.00574239,0.00584951,
 0.00827442,0.0133891 ,0.02024075,0.02581288,0.01699641,0.00553164])


# ode problem instance
options['dt'] = 2.47851665 #1.68188698 #3.40197917 #2.70794719 # 0.9270615 # 3.5 for min energy objective
num = 30
ODEProblem = ODEProblemTest('RK4', 'time-marching', num_times=num, display='default', visualization='end')
sim = python_csdl_backend.Simulator(RunModel(options=options), analytics=0)
#sim.run()
#sim.check_totals(step=1e-3)

prob = CSDLProblem(problem_name='Trajectory Optimization', simulator=sim)
optimizer = SLSQP(prob, maxiter=100, ftol=1E-4) # 1E-3 for min energy 1E-2 for min dt
# optimizer = SNOPT(prob,Major_iterations=500,Major_optimality=1e-5,Major_feasibility=1E-5,append2file=True)
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



