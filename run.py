import csdl
import numpy as np
import python_csdl_backend
from odeproblemtest import ODEProblemTest
from timestep import timestep
from modopt.scipy_library import SLSQP
from modopt.csdl_library import CSDLProblem
import matplotlib.pyplot as plt


# The CSDL Model containing the ODE integrator
class RunModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('dt')
        self.parameters.declare('mass')
        self.parameters.declare('wing_area')

    def define(self):
        mass = self.parameters['mass']
        wing_area = self.parameters['wing_area']
        dt = self.parameters['dt']
        
        # add the time vector to the csdl model
        self.create_input('dt', dt)
        self.add(timestep(num=num))

        # add constant inputs to the csdl model
        self.create_input('mass',mass)
        self.create_input('wing_area',wing_area)
        # add dynamic inputs to the csdl model
        power = np.ones(num)*0 # power percent (0-1)
        self.create_input('power',power)
        
        theta = np.ones(num)*np.deg2rad(0)
        self.create_input('theta',theta)

        # initial conditions for states
        self.create_input('u_0', 1)
        self.create_input('w_0', 0)
        self.create_input('x_0', 0)
        self.create_input('z_0', 0)

        # create model containing the integrator
        self.add(ODEProblem.create_solver_model(), 'subgroup')

        # declare variables from integrator
        u = self.declare_variable('u', shape=(num,))
        w = self.declare_variable('w', shape=(num,))
        x = self.declare_variable('x', shape=(num,))
        z = self.declare_variable('z', shape=(num,))

        lift = self.declare_variable('lift', shape=(num,))
        drag = self.declare_variable('drag', shape=(num,))
        alpha = self.declare_variable('alpha', shape=(num,))

        # add constraints
        final_altitude = z[-1]
        self.register_output('final_altitude', final_altitude)
        self.add_constraint('final_altitude', lower=100)

        # add design variables
        # self.add_design_variable('theta',lower=-np.pi/6,upper=np.pi/6)
        self.add_design_variable('power',lower=0, upper=1)
        self.add_design_variable('dt',lower=0.5,upper=3)

        # add objective
        self.add_objective('dt')


# aircraft data
mass = 2000 # mass (kg)
wing_area = 40 # wing area (m^2)

# ode problem instance
dt = 0.5
num = 80
ODEProblem = ODEProblemTest('RK4', 'time-marching', num_times=num, display='default', visualization='end')
sim = python_csdl_backend.Simulator(RunModel(dt=dt,mass=mass,wing_area=wing_area))
sim.run()
"""
prob = CSDLProblem(problem_name='Trajectory Optimization', simulator=sim)
optimizer = SLSQP(prob, maxiter=50, ftol=1e-12)
optimizer.solve()
optimizer.print_results()
"""
# plot states from integrator
plt.show()

# assign variables for post-processing
u = sim['u']
w = sim['w']
x = sim['x']
z = sim['z']
dt = sim['dt']
thrust = sim['thrust']
theta = sim['theta']
alpha = sim['alpha']
cl = sim['cl']
cd = sim['cd']
lift = sim['lift']
drag = sim['drag']
power = sim['power']

plt.plot(u)
plt.plot(w)
plt.plot(x)
plt.plot(z)
plt.legend(['u','w','x','z'])
plt.show()

plt.plot(lift)
plt.plot(drag)
plt.legend(['lift','drag'])
plt.show()

plt.plot(cl)
plt.plot(cd)
plt.legend(['cl','cd'])
plt.show()

plt.plot(thrust)
plt.legend(['thrust'])
plt.show()