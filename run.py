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
        max_cruise_power = csdl.max(cruisepower)
        max_lift_power = csdl.max(liftpower)
        self.register_output('max_cruise_power', max_cruise_power)
        self.register_output('max_lift_power', max_lift_power)
        # only for min dt case
        self.add_constraint('max_cruise_power', upper=options['max_cruise_power'], scaler=1E-6)
        self.add_constraint('max_lift_power', upper=options['max_lift_power'], scaler=1E-6)

        # final altitude constraint
        final_h = h[-1]
        self.register_output('final_h', final_h)
        self.add_constraint('final_h', equals=options['h_f'], scaler=0.01)

        # min altitude constraint
        min_h = csdl.min(h)
        self.register_output('min_h', min_h)
        self.add_constraint('min_h', lower=options['h_0'] - 0.01)

        # final velocity constraint
        final_v = v[-1]
        self.register_output('final_v',final_v)
        self.add_constraint('final_v',lower=options['v_f'],scaler=0.01) #0.1
        

        # flight path angle constraints
        theta = gamma + alpha
        self.register_output('theta',theta)
        self.register_output('min_theta',csdl.min(theta))
        self.register_output('max_theta',csdl.max(theta))
        #self.add_constraint('min_theta',lower=-np.deg2rad(15))
        #self.add_constraint('max_theta',upper=np.deg2rad(15))
        
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
        
        self.add_design_variable('control_alpha',lower=-np.pi/2,upper=np.pi/2,scaler=1/options['control_alpha_i'])
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
options['max_spl'] = 100 # (db)
# initial control inputs
"""
options['control_x_i'] = np.ones(30)*2300
options['control_z_i'] = np.linspace(800, 100, 30)
options['control_alpha_i'] = np.linspace(0.7, 0, 30)
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
options['dt'] = 0.9270615 #1.21333051 #1.27790049 #2.70794719 # 0.9270615 # 3.5
num = 30
ODEProblem = ODEProblemTest('RK4', 'time-marching', num_times=num, display='default', visualization='end')
sim = python_csdl_backend.Simulator(RunModel(options=options), analytics=0)
#sim.run()
#sim.check_partials(compact_print=True)

prob = CSDLProblem(problem_name='Trajectory Optimization', simulator=sim)
optimizer = SLSQP(prob, maxiter=2000, ftol=1E-4)
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



