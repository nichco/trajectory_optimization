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
from parameters import options


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
        self.register_output('max_theta',csdl.max(((gamma + alpha)**2)**0.5))
        #self.add_constraint('max_theta',upper=np.deg2rad(15))
        
        # flight path angle constraints
        self.register_output('final_gamma',gamma[-1])
        self.add_constraint('final_gamma',equals=0)
        
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
        self.add_design_variable('control_alpha',scaler=np.linspace(1,10,num))
        self.add_design_variable('control_x',lower=0, scaler=1E-2)
        self.add_design_variable('control_z',lower=0, scaler=np.linspace(1E-3,1E-2,num))
        self.add_design_variable('dt')
        
        #self.add_design_variable('control_alpha',scaler=1)
        #self.add_design_variable('control_x',lower=0, scaler=1/options['control_x_i'])
        #self.add_design_variable('control_z',lower=0, scaler=1/options['control_z_i'])
        #self.add_design_variable('dt',lower=0.5)

        self.add_objective('dt')
        




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
options['h_0'] = 0 # (m)
options['x_0'] = 0 # (m)
options['alpha_0'] = 0 # (rad)
options['h_f'] = 300 # (m)
options['v_f'] = 43 # (m/s)
# initial control inputs

#options['control_x_i'] = np.ones(30)*2300
#options['control_z_i'] = np.linspace(800, 100, 30)
#options['control_alpha_i'] = np.linspace(0.7, 0, 30)


# min dt seed (nominal)
options['control_x_i'] = np.array([2124.99713301,2147.24162348,2115.99307639,2214.36883994,2235.05443852,
 2251.16923596,2262.83541486,2251.50139516,2280.69407357,2318.61481819,
 2372.73930726,2396.17291084,2402.23339706,2410.49323496,2416.40173985,
 2422.22593009,2427.72441213,2432.44080978,2435.91621419,2438.89892645,
 2445.35503282,2447.08162961,2442.22806877,2441.27106436,2434.52204514,
 2395.05870964,2383.57262964,2339.14905017,2326.76477643,2322.1561648 ])
options['control_z_i'] = np.array([1.39186114e+03,1.40588527e+03,1.44174575e+03,1.40516985e+03,
 1.40707281e+03,1.40503301e+03,0.00000000e+00,0.00000000e+00,
 5.61818907e-11,1.39204212e+03,1.36908634e+03,1.36221795e+03,
 3.33518864e+01,9.49141118e-11,8.51545310e+01,1.79199693e+01,
 8.46641499e+01,3.23762380e+01,7.03650851e+01,1.92946223e-10,
 2.62559450e+01,1.77522523e+01,1.36160992e+03,1.36296269e+03,
 1.77442966e+02,7.71765306e+00,8.00610237e+00,2.92696133e+01,
 7.80277801e+00,1.79312794e-10])
options['control_alpha_i'] = np.array([ 0.67217549, 0.73394818, 1.35204692, 0.44813604, 0.44881455, 0.4199771 ,
 -0.2944446 ,-0.1687615 ,-0.37530761, 0.34098485, 0.22135739, 0.19954471,
 -0.14085656, 0.0091387 ,-0.01820163,-0.00819797,-0.00176691,-0.00863974,
 -0.01958483,-0.02096045,-0.01700367,-0.10227899, 0.20966134, 0.20845703,
 -0.06247892,-0.01924573,-0.04494589,-0.18205321,-0.16431064,-0.17932383])
"""

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
#options['dt'] = 0.85585751 #1.21333051 #2.70794719 # 3.5
num = 30
ODEProblem = ODEProblemTest('RK4', 'time-marching', num_times=num, display='default', visualization='end')
sim = python_csdl_backend.Simulator(RunModel(options=options), analytics=0)
#sim.run()
#sim.check_partials(compact_print=True)

prob = CSDLProblem(problem_name='Trajectory Optimization', simulator=sim)
optimizer = SLSQP(prob, maxiter=2000, ftol=1E-6)
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



