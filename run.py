import csdl
import numpy as np
import python_csdl_backend
from odeproblemtest import ODEProblemTest
from timestep import timestep
from modopt.scipy_library import SLSQP
from modopt.snopt_library import SNOPT
from modopt.csdl_library import CSDLProblem
import matplotlib.pyplot as plt
from spline_explicit import spline
from theta_explicit import theta_exp


# The CSDL Model containing the ODE integrator
class RunModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('dt')
        self.parameters.declare('mass')
        self.parameters.declare('wing_area')
        self.parameters.declare('wing_set_angle')
        self.parameters.declare('max_power')
        self.parameters.declare('propeller_efficiency')
        self.parameters.declare('oswald')
        self.parameters.declare('gravity')
        self.parameters.declare('u_0')
        self.parameters.declare('w_0')
        self.parameters.declare('x_0')
        self.parameters.declare('z_0')

    def define(self):
        mass = self.parameters['mass']
        wing_area = self.parameters['wing_area']
        wing_set_angle = self.parameters['wing_set_angle']
        max_power = self.parameters['max_power']
        propeller_efficiency = self.parameters['propeller_efficiency']
        oswald = self.parameters['oswald']
        gravity = self.parameters['gravity']
        u_0 = self.parameters['u_0']
        w_0 = self.parameters['w_0']
        x_0 = self.parameters['x_0']
        z_0 = self.parameters['z_0']
        dt = self.parameters['dt']
        
        
        # add the time vector to the csdl model
        self.create_input('dt', dt)
        self.add(timestep(num=num))

        # add constant inputs to the csdl model
        self.create_input('mass',mass)
        self.create_input('wing_area',wing_area)
        self.create_input('wing_set_angle',wing_set_angle)
        self.create_input('max_power',max_power)
        self.create_input('propeller_efficiency',propeller_efficiency)
        self.create_input('oswald',oswald)
        self.create_input('gravity',gravity)

        # add dynamic inputs to the csdl model
        power = np.ones(num)*0.1 # power fraction (0-1)
        self.create_input('interp',power)
        # N = 5
        # control = np.ones(N)*0.1
        # self.create_input('control',control)
        # self.add(spline(N=N,num_nodes=num,dt=dt))
        
        theta = np.ones(num)*np.deg2rad(0)
        self.create_input('theta',theta)

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

        # add constraints
        final_z = z[-1]
        self.register_output('final_z', final_z)
        self.add_constraint('final_z', equals=z_0, scaler=0.01)

        final_u = u[-1]
        self.register_output('final_u', final_u)
        self.add_constraint('final_u', equals=u_0, scaler=0.01)

        theta_out = self.declare_variable('theta',shape=(num,))
        slope = self.create_output('slope',shape=(num,), val=0)
        for i in range(1,num):
            slope[i] = (theta_out[i] - theta_out[i-1])/dt
        self.add_constraint('slope', lower=-0.005, upper=0.005)

        pwr_out = self.declare_variable('interp',shape=(num,))
        slope_pwr = self.create_output('slope_pwr',shape=(num,), val=0)
        for i in range(1,num):
            slope_pwr[i] = (pwr_out[i] - pwr_out[i-1])/dt
        self.add_constraint('slope_pwr', lower=-0.005, upper=0.005)


        # add design variables
        self.add_design_variable('theta',lower=-1*np.pi/6,upper=np.pi/6)
        # self.add_design_variable('control',lower=0, upper=1.0)
        self.add_design_variable('interp',lower=0, upper=1.0)

        # add objective
        energy = e[-1]
        self.register_output('energy',energy)
        self.add_objective('energy', scaler=0.01)





# aircraft data
mass = 1111 # mass (kg)
wing_area = 16.2 # wing area (m^2)
wing_set_angle = 2 # (deg)
max_power = 120000 # maximum engine power (w)
propeller_efficiency = 0.7 # propeller efficiency factor
oswald = 0.8 # finite wing correction
# mission parameters
gravity = 9.81 # acceleration due to gravity (m/s^2)
u_0 = 53 # 63 (m/s)
w_0 = 0 # (m/s)
x_0 = 0 # (m)
z_0 = 2000 # (m)

# ode problem instance
dt = 0.2
num = 100
ODEProblem = ODEProblemTest('RK4', 'time-marching', num_times=num, display='default', visualization='end')
sim = python_csdl_backend.Simulator(RunModel(dt=dt,mass=mass,
                                                wing_area=wing_area,
                                                wing_set_angle=wing_set_angle,
                                                max_power=max_power,
                                                propeller_efficiency=propeller_efficiency,
                                                oswald=oswald,
                                                gravity=gravity,
                                                u_0=u_0,
                                                w_0=w_0,
                                                x_0=x_0,
                                                z_0=z_0))
# sim.run()

prob = CSDLProblem(problem_name='Trajectory Optimization', simulator=sim)
# optimizer = SLSQP(prob, maxiter=800, ftol=1e-8)
optimizer = SNOPT(prob, Optimality_tolerance=1e-10)
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
slope = sim['slope']

# post-processing
fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4)
fig.suptitle('trajectory optimization')
ax1.plot(u,color='b')
ax1.plot(w,color='g')
ax1.legend(['u','w'])

ax2.plot(x,color='r')
ax2.plot(z,color='c')
ax2.legend(['x','z'])

ax3.plot(lift,color='m')
ax3.plot(drag,color='y')
ax3.legend(['lift','drag'])

ax4.plot(cl)
ax4.plot(cd)
ax4.legend(['cl','cd'])

ax5.plot(alpha,color='k')
ax5.set_title('alpha')
ax5.set_ylabel('rad')

ax6.plot(power,color='k')
ax6.set_title('power')

ax7.plot(theta,color='c')
ax7.set_title('theta')

ax8.plot(slope,color='k')
ax8.set_title('slope')

plt.show()