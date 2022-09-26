import csdl
import numpy as np
import python_csdl_backend
from odeproblemtest import ODEProblemTest
from timestep import timestep
import time
from modopt.scipy_library import SLSQP
from modopt.csdl_library import CSDLProblem

# The CSDL Model containing the ODE integrator
class RunModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('dt')
        self.parameters.declare('mass')

    def define(self):
        mass = self.parameters['mass']
        dt = self.parameters['dt']

        # add the time vector to the csdl model
        self.create_input('dt', dt)
        self.add(timestep(num=num))

        # add constant inputs to the csdl model
        self.create_input('mass',mass)
        # add dynamic inputs to the csdl model


        # create model containing the integrator
        self.add(ODEProblem.create_solver_model(), 'subgroup', ['*'])

        # declare variables from integrator
        # states
        u = self.declare_variable('u', shape=(num+1,))
        w = self.declare_variable('w', shape=(num+1,))
        z = self.declare_variable('z', shape=(num+1,))
        # inputs
        thrust = self.declare_variable('thrust', shape=(num,))
        theta = self.declare_variable('theta', shape=(num,))

        # recalculate aerodynamic data

        # compute load factor

        # add constraints

        # add design variables

        # add objective


# aircraft data
mass = 3724 # kg

t1 = time.perf_counter()
# ode problem instance
dt = 1
num = 10
ODEProblem = ODEProblemTest('ExplicitMidpoint', 'time-marching', num_times=num, display='default', visualization='end')
sim = python_csdl_backend.Simulator(RunModel(dt=dt,mass=mass))
sim.run()


t2 = time.perf_counter()
delta_t = (t2 - t1)
print('elapsed time: ', delta_t)
