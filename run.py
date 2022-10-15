import csdl
import numpy as np
import python_csdl_backend
from odeproblemtest import ODEProblemTest
from timestep import timestep
from modopt.scipy_library import SLSQP
# from modopt.snopt_library import SNOPT
from modopt.csdl_library import CSDLProblem
import matplotlib.pyplot as plt
from slope import slope
from curvature import curve


class RunModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('dt')
        self.parameters.declare('options')
    def define(self):
        options = self.parameters['options']
        dt = self.parameters['dt']

        mass = options['mass']
        wing_area = options['wing_area']
        wing_set_angle = options['wing_set_angle']
        max_power = options['max_power']
        max_rpm = options['max_rpm']
        propeller_efficiency = options['propeller_efficiency']
        oswald = options['oswald']
        cd_0 = options['cd_0']
        gravity = options['gravity']
        u_0 = options['u_0']
        w_0 = options['w_0']
        x_0 = options['x_0']
        z_0 = options['z_0']
        theta_0 = options['theta_0']
        theta_f = options['theta_f']
        z_f = options['z_f']
        dx_f = options['dx_f']

        # add the time vector to the csdl model
        self.create_input('dt', dt)
        self.add(timestep(num=num))

        # add constant inputs to the csdl model
        self.create_input('mass',mass)
        self.create_input('wing_area',wing_area)
        self.create_input('wing_set_angle',wing_set_angle)
        self.create_input('max_power',max_power)
        self.create_input('max_rpm',max_rpm)
        self.create_input('propeller_efficiency',propeller_efficiency)
        self.create_input('oswald',oswald)
        self.create_input('cd_0',cd_0)
        self.create_input('gravity',gravity)

        # add dynamic inputs to the csdl model
        power = np.ones(num)*0.1 # power fraction (0-1)
        self.create_input('interp',power)
        # N = 5
        # control = np.ones(N)*0.1
        # self.create_input('control',control)
        # self.add(spline(N=N,num_nodes=num,dt=dt))
        
        theta_control = np.ones(num)*np.deg2rad(0)
        self.create_input('theta',theta_control)

        # initial conditions for states
        self.create_input('u_0', u_0)
        self.create_input('w_0', w_0)
        self.create_input('x_0', x_0)
        self.create_input('z_0', z_0)
        self.create_input('e_0', 0)

        # create model containing the integrator
        self.add(ODEProblem.create_solver_model(), 'subgroup')

        # declare variables from integrator
        u = self.declare_variable('u', shape=(num,))
        w = self.declare_variable('w', shape=(num,))
        x = self.declare_variable('x', shape=(num,))
        z = self.declare_variable('z', shape=(num,))
        e = self.declare_variable('e', shape=(num,))
        theta = self.declare_variable('theta', shape=(num,))

        # add final altitude constraint
        final_z = z[-1]
        self.register_output('final_z', final_z)
        self.add_constraint('final_z', equals=z_f, scaler=0.01)

        # horizontal velocity constraint
        final_dx = u[-1]*csdl.cos(theta[-1]) + w[-1]*csdl.sin(theta[-1])
        self.register_output('final_dx',final_dx)
        self.add_constraint('final_dx',equals=dx_f,scaler=0.1)

        # theta constraints
        initial_theta = theta[0]
        self.register_output('initial_theta', initial_theta)
        self.add_constraint('initial_theta', equals=theta_0)

        # control slope constraint
        self.add(slope(dt=dt,num=num))
        self.add_constraint('dtheta', lower=-0.05, upper=0.05)
        self.add_constraint('dpwr', lower=-0.05, upper=0.05)

        # control curvature constraint
        self.add(curve(dt=dt,num=num))
        #self.add_constraint('d_dtheta', lower=-0.02, upper=0.02)
        #self.add_constraint('d_dpwr', lower=-0.02, upper=0.02)

        # add design variables
        self.add_design_variable('theta',lower=-1*np.pi/6,upper=np.pi/6)
        # self.add_design_variable('control',lower=0, upper=1.0)
        self.add_design_variable('interp',lower=0, upper=1.0)
        self.add_design_variable('dt',lower=0, upper=1.0)

        # add objective
        energy = e[-1]
        self.register_output('energy',energy)
        self.add_objective('energy', scaler=0.01)





options = {} # aircraft and mission parameter dictionary
# aircraft data
options['mass'] = 1111 # (kg)
options['wing_area'] = 16.2 # wing area (m^2)
options['wing_set_angle'] = 3 # (deg)
options['max_power'] = 120000 # maximum engine power (w)
options['max_rpm'] = 6000 # maximum rotor speed (rpm)
options['propeller_efficiency'] = 0.8 # propeller efficiency factor
options['oswald'] = 0.8 # finite wing correction
options['cd_0'] = 0.025 # zero-lift drag coefficient
# mission parameters
options['gravity'] = 9.81 # acceleration due to gravity (m/s^2)
options['u_0'] = 63 # (m/s)
options['w_0'] = 0 # (m/s)
options['x_0'] = 0 # (m)
options['z_0'] = 2000 # (m)
options['theta_0'] = 0 # (rad)
options['theta_f'] = 0 # (rad)
options['z_f'] = 2200 # (m)
options['dx_f'] = 63 # (m/s)

# ode problem instance
dt = 0.3
num = 100
ODEProblem = ODEProblemTest('RK4', 'time-marching', num_times=num, display='default', visualization='end')
sim = python_csdl_backend.Simulator(RunModel(dt=dt,options=options))
# sim.run()

prob = CSDLProblem(problem_name='Trajectory Optimization', simulator=sim)
optimizer = SLSQP(prob, maxiter=800, ftol=1e-9)
# optimizer = SNOPT(prob, Optimality_tolerance=1e-10)
optimizer.solve()
# optimizer.print_results()

# plot states from integrator
plt.show()

# assign variables for post-processing
u = sim['u']
w = sim['w']
x = sim['x']
z = sim['z']
dt = sim['dt']
theta = sim['theta']
alpha = sim['alpha']
cl = sim['cl']
cd = sim['cd']
lift = sim['lift']
drag = sim['drag']
power = sim['interp']
dtheta = sim['dtheta']
dpwr = sim['dpwr']
d_dtheta = sim['d_dtheta']
d_dpwr = sim['d_dpwr']

print(sim['dt'])

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

ax6.plot(cl)
ax6.plot(cd)
ax6.legend(['cl','cd'])

ax7.plot(alpha,color='k')
ax7.set_title('alpha')
ax7.set_ylabel('rad')

ax8.plot(power,color='k')
ax8.set_title('power')

ax9.plot(theta,color='c')
ax9.set_title('theta')

ax10.plot(dtheta,color='k')
ax10.plot(dpwr,color='m')
ax10.legend(['dtheta','dpwr'])
ax10.set_title('slope')

ax11.plot(d_dtheta,color='k')
ax11.plot(d_dpwr,color='c')
ax11.legend(['d_dtheta','d_dpwr'])
ax11.set_title('curvature')
plt.show()