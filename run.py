import csdl
import numpy as np
import python_csdl_backend
from odeproblemtest import ODEProblemTest
from timestep import timestep
from modopt.scipy_library import SLSQP
from modopt.snopt_library import SNOPT
from modopt.csdl_library import CSDLProblem
import matplotlib.pyplot as plt
from slope import slope
from curvature import curve
from inputs import inputs
from skm import tonal
import time
from spline_explicit import spline


class RunModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('options')

    def define(self):
        options = self.parameters['options']
        self.create_input('dt',options['dt'])
        self.add(inputs(num=num,options=options), name = 'inputs')
        self.add(timestep(num=num), name = 'timestep') # add the time vector to the model
        
        # add dynamic inputs to the csdl model
        # control_x = np.ones(num)*options['control_x_i'] # cruise rotor speed input control
        control_z = np.ones(num)*options['control_z_i'] # lift rotor speed input control
        control_theta = np.ones(num)*np.deg2rad(options['control_theta_i']) # pitch angle input control
        # self.create_input('control_x',control_x)
        self.create_input('control_z',control_z)
        self.create_input('control_theta',control_theta)



        N = 5
        control_x = np.ones((N))*options['control_x_i']
        self.create_input('control_x',control_x)
        self.add(spline(name='x',N=N,num_nodes=num,dt=options['dt']))



        # initial conditions for states
        self.create_input('u_0', options['u_0'])
        self.create_input('w_0', options['w_0'])
        self.create_input('x_0', options['x_0'])
        self.create_input('z_0', options['z_0'])
        self.create_input('e_0', 0)

        # create model containing the integrator
        optionsdict = {'options': options}
        self.add(ODEProblem.create_solver_model(ODE_parameters=optionsdict, profile_parameters=optionsdict), 'subgroup')

        # declare variables from integrator
        u = self.declare_variable('u', shape=(num,))
        w = self.declare_variable('w', shape=(num,))
        x = self.declare_variable('x', shape=(num,))
        z = self.declare_variable('z', shape=(num,))
        e = self.declare_variable('e', shape=(num,))
        theta = self.declare_variable('control_theta', shape=(num,))
        cruisepower = self.declare_variable('cruisepower', shape=(num,))
        liftpower = self.declare_variable('liftpower', shape=(num,))

        # add final altitude constraint
        final_z = z[-1]
        self.register_output('final_z', final_z)
        self.add_constraint('final_z', equals=options['z_f'], scaler=0.01)
        # self.add_constraint('final_z', lower=options['z_f'], scaler=0.01)

        # horizontal velocity constraint
        # final_dx = u[-1]*csdl.cos(theta[-1]) + w[-1]*csdl.sin(theta[-1])
        # final_dx = u[-1]
        # self.register_output('final_dx',final_dx)
        # self.add_constraint('final_dx',equals=options['dx_f'],scaler=0.1)

        # vertical velocity constraint
        """
        final_dz = u[-1]*csdl.sin(theta[-1]) - w[-1]*csdl.cos(theta[-1])
        self.register_output('final_dz',final_dz)
        self.add_constraint('final_dz',equals=options['dz_f'],scaler=0.1)
        """

        # theta constraints
        initial_theta = theta[0]
        self.register_output('initial_theta', initial_theta)
        #self.add_constraint('initial_theta', equals=options['theta_0'])

        # power constraints
        max_cruise_pwr = csdl.max(cruisepower)
        max_lift_pwr = csdl.max(liftpower)
        self.register_output('max_cruise_pwr', max_cruise_pwr)
        self.register_output('max_lift_pwr', max_lift_pwr)
        #self.add_constraint('max_cruise_pwr', upper=options['max_cruise_power'], scaler=0.00001)
        #self.add_constraint('max_lift_pwr', upper=options['max_lift_power'], scaler=0.00001)
        # final_lift_pwr = liftpower[-1]
        # self.register_output('final_lift_pwr', final_lift_pwr)
        # self.add_constraint('final_lift_pwr', equals=0, scaler=0.00001)

        # control slope constraint
        self.add(slope(num=num), name = 'slope')
        #self.add_constraint('dtheta', lower=-2, upper=2)
        #self.add_constraint('dcx', lower=-2, upper=2)
        #self.add_constraint('dcz', lower=-2, upper=2)

        # control curvature constraint
        self.add(curve(num=num), name = 'curve')
        #self.add_constraint('d_dtheta', lower=-0.02, upper=0.02)
        #self.add_constraint('d_dpwr', lower=-0.02, upper=0.02)

        # acoustics constraints
        self.add(tonal(options=options,num=num), name = 'tonal')
        # self.add_constraint('spl', upper=85, scaler=0.01)

        # add design variables
        # self.add_design_variable('control_theta',lower=-1*np.pi/5,upper=np.pi/5)
        self.add_design_variable('control_x',lower=0, scaler=0.001)
        # self.add_design_variable('control_z',lower=0, upper=6000, scaler=0.001)
        # self.add_design_variable('dt',lower=0.1)

        # add objective
        energy = e[-1]
        self.register_output('energy',energy)
        self.add_objective('energy', scaler=0.001)
        # self.add_objective('dt', scaler=0.1)





options = {} # aircraft and mission parameter dictionary
# aircraft data
options['mass'] = 1111 # (kg)
options['wing_area'] = 16.2 # wing area (m^2)
options['wing_set_angle'] = 3 # (deg)
options['max_cruise_power'] = 500000 # maximum cruise power (w)
options['max_lift_power'] = 220000 # maximum lift power (w)
options['oswald'] = 0.8 # finite wing correction
options['cd_0'] = 0.025 # zero-lift drag coefficient
options['cruise_rotor_diameter'] = 2.0 # (m)
options['lift_rotor_diameter'] = 1.2 # (m)
options['num_lift_rotors'] = 8
options['num_cruise_blades'] = 4
options['num_lift_blades'] = 2
# mission parameters
options['gravity'] = 9.81 # (m/s^2)
options['u_0'] = 1 # (m/s)
options['w_0'] = 0 # (m/s)
options['x_0'] = 0 # (m)
options['z_0'] = 1000 # (m)
options['theta_0'] = 0 # (rad)
options['theta_f'] = 0 # (rad)
options['z_f'] = 1000 # (m)
options['dx_f'] = 63 # (m/s)
options['dz_f'] = 0 # (m/s)
# initial control inputs
options['control_x_i'] = 5000 # (rpm)
options['control_z_i'] = 1 # (rpm)
options['control_theta_i'] = 0 # (deg)

# ode problem instance
options['dt'] = 0.2
num = 50
t1 = time.perf_counter()
ODEProblem = ODEProblemTest('ExplicitMidpoint', 'time-marching', num_times=num, display='default', visualization='end')
sim = python_csdl_backend.Simulator(RunModel(options=options), analytics=0)
# sim.run()

prob = CSDLProblem(problem_name='Trajectory Optimization', simulator=sim)
# optimizer = SLSQP(prob, maxiter=800, ftol=1e-8)
optimizer = SNOPT(prob, Major_optimality=1e-7)
optimizer.solve()
optimizer.print_results()
# plot states from integrator
plt.show()
t2 = time.perf_counter()
print('time: ', t2-t1)


# assign variables for post-processing
u = sim['u']
w = sim['w']
x = sim['x']
z = sim['z']
dt = sim['dt']
theta = sim['control_theta']
alpha = sim['alpha']
cl = sim['cl']
cd = sim['cd']
lift = sim['lift']
drag = sim['drag']
control_x = sim['interp_x']
control_z = sim['control_z']
dtheta = sim['dtheta']
dcx = sim['dcx']
dcz = sim['dcz']
d_dtheta = sim['d_dtheta']
d_dcx = sim['d_dcx']
d_dcz = sim['d_dcz']
cruisepower = sim['cruisepower']
liftpower = 8*sim['liftpower']
e = sim['e']
cruise_spl = sim['cruise_spl']
lift_spl = sim['lift_spl']
sum_spl = sim['sum_spl']
spl = sim['spl']

# post-processing
fig, ((ax1, ax2, ax3, ax4, ax5, ax6), (ax7, ax8, ax9, ax10, ax11, ax12)) = plt.subplots(2, 6)
fig.suptitle('trajectory optimization')
ax1.plot(u,color='b')
ax1.legend(['u'])

ax2.plot(w,color='g')
ax2.legend(['w'])

ax3.plot(x,color='r')
ax3.legend(['x'])

ax4.plot(z,color='c')
ax4.legend(['z'])

ax5.plot(lift,color='m')
ax5.plot(drag,color='y')
ax5.legend(['lift','drag'])

# ax6.plot(cl)
# ax6.plot(cd)
# ax6.legend(['cl','cd'])
# ax6.plot(e)
# ax6.set_title('energy')
ax6.plot(sum_spl)
ax6.set_title('spl')

ax7.plot(alpha,color='k')
ax7.set_title('alpha')
ax7.set_ylabel('rad')

ax8.plot(control_x,color='k')
ax8.plot(control_z,color='r')
ax8.set_title('rotor speed')
ax8.legend(['cruise rotor speed','lift rotor speed'])
ax8.set_ylabel('rotor speed (rpm)')

ax9.plot(theta,color='c')
ax9.set_title('theta')

ax10.plot(dtheta,color='k')
ax10.plot(dcx,color='m')
ax10.plot(dcz,color='c')
ax10.legend(['dtheta','dcx', 'dcz'])
ax10.set_title('slope')

ax11.plot(d_dtheta,color='k')
ax11.plot(d_dcx,color='c')
ax11.plot(d_dcz,color='r')
ax11.legend(['d_dtheta','d_dcx', 'd_dcz'])
ax11.set_title('curvature')

ax12.plot(cruisepower,color='k')
ax12.plot(liftpower,color='r')
ax12.legend(['cruise power','lift power'])
ax12.set_title('power')

plt.show()