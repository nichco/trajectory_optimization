import csdl
import python_csdl_backend
import numpy as np
from smt.surrogate_models import RMTB

class spline(csdl.Model):
    def initialize(self):
        self.parameters.declare('N') # number of spline control points
        self.parameters.declare('num_nodes') # number of ode timesteps
        self.parameters.declare('dt') # timestep

    def define(self):
        N = self.parameters['N']
        num_nodes = self.parameters['num_nodes']
        dt = self.parameters['dt']

        # input sparse control point vector
        control = self.declare_variable('control', shape=(N,))

        # custom operation insertion
        interp = csdl.custom(control, op=SplineExplicit(N=N,num_nodes=num_nodes,dt=dt))

        # output interpolated spline vector
        self.register_output('interp', interp)

class SplineExplicit(csdl.CustomExplicitOperation):
    def initialize(self):
        self.parameters.declare('N') # number of spline control points
        self.parameters.declare('num_nodes') # number of ode timesteps
        self.parameters.declare('dt') # timestep

    def define(self):
        N = self.parameters['N']
        num_nodes = self.parameters['num_nodes']
        dt = self.parameters['dt']

        # input sparse control point vector
        self.add_input('control', shape=(N,))

        # output interpolated spline vector
        self.add_output('interp', shape=(num_nodes,))

        # declare derivatives
        self.declare_derivatives('interp', 'control')

    def compute(self, inputs, outputs):
        N = self.parameters['N']
        num_nodes = self.parameters['num_nodes']
        dt = self.parameters['dt']

        # create spline surrogate model
        xt = np.linspace(0,num_nodes*dt,N)
        yt = inputs['control']

        xlimits = np.array([[0.0, num_nodes*dt]])

        sm = RMTB(
            xlimits=xlimits,
            order=4,
            num_ctrl_pts=20,
            energy_weight=1e-15,
            regularization_weight=0.0,)
        sm.set_training_values(xt, yt)
        sm.train()

        # vector for spline interpolation
        xnew = np.arange(0, num_nodes*dt, dt)

        # interpolate spline
        ynew = sm.predict_values(xnew)

        # assign interpolated output vector
        outputs['interp'] = ynew

    def compute_derivatives(self, inputs, derivatives):
        N = self.parameters['N']
        num_nodes = self.parameters['num_nodes']
        dt = self.parameters['dt']

        # redo surrogate generation
        xt = np.linspace(0,num_nodes*dt,N)
        yt = inputs['control']
        xlimits = np.array([[0.0, num_nodes*dt]])
        sm = RMTB(
            xlimits=xlimits,
            order=4,
            num_ctrl_pts=20,
            energy_weight=1e-15,
            regularization_weight=0.0,)
        sm.set_training_values(xt, yt)
        sm.train()

        xnew = np.arange(0, num_nodes*dt, dt)
        yder = sm.predict_output_derivatives(xnew)

        derivatives['interp', 'control'] = yder

"""
# run model
sim = python_csdl_backend.Simulator(spline(N=10,num_nodes=100,dt=0.1))
sim.run()

print(sim['interp'])
# print partials
sim.check_partials(compact_print=True)

"""
# test code
N=5
num_nodes=10
dt=0.1
xt = np.linspace(0,num_nodes*dt,N)
yt = np.ones(N)
xlimits = np.array([[0.0, num_nodes*dt]])
sm = RMTB(
        xlimits=xlimits,
        order=4,
        num_ctrl_pts=20,
        energy_weight=1e-15,
        regularization_weight=0.0,)
sm.set_training_values(xt, yt)
sm.train()

xnew = np.arange(0, num_nodes*dt, dt)
dict = sm.predict_output_derivatives(xnew)
list = list(dict.items())
array = np.array(list)
"""
yder = np.zeros((num_nodes,N))
for i in range(0,num_nodes):
    for j in range(0,N):
        yder[i,j] = items[i,j]
"""


print(list[0])