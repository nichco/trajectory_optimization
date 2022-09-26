import csdl
import numpy as np
import python_csdl_backend
from odeproblemtest import ODEProblemTest
from timestep import timestep
import time
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
        thrust = np.ones(num)*0
        self.create_input('thrust',thrust)
        theta = np.ones(num)*np.deg2rad(3)
        self.create_input('theta',theta)

        # initial conditions for states
        self.create_input('u_0', 0.1)
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

        # recalculate aerodynamic data

        # compute load factor

        # add constraints

        # add design variables

        # add objective


# aircraft data
mass = 3724 # mass (kg)
wing_area = 30 # wing area (m^2)

t1 = time.perf_counter()
# ode problem instance
dt = 1
num = 10
ODEProblem = ODEProblemTest('RK4', 'time-marching', num_times=num, display='default', visualization='end')
sim = python_csdl_backend.Simulator(RunModel(dt=dt,mass=mass,wing_area=wing_area))
sim.run()


t2 = time.perf_counter()
delta_t = (t2 - t1)
print('elapsed time: ', delta_t)

# plot states from integrator
plt.show()

# assign variables for post-processing
u = sim['u']
w = sim['w']
x = sim['x']
z = sim['z']

plt.plot(u)
plt.plot(w)
plt.plot(x)
plt.plot(z)
plt.legend(['u','w','x','z'])
plt.show()


