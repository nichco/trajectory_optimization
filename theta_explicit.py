import csdl
import python_csdl_backend
import numpy as np
from smt.surrogate_models import RMTB, RBF
import matplotlib.pyplot as plt

class theta_exp(csdl.Model):
    def initialize(self):
        self.parameters.declare('N') # number of spline control points
        self.parameters.declare('num_nodes') # number of ode timesteps
        self.parameters.declare('dt') # timestep

    def define(self):
        N = self.parameters['N']
        num_nodes = self.parameters['num_nodes']
        dt = self.parameters['dt']

        # input sparse control point vector
        theta_control = self.declare_variable('theta_control', shape=(N,))

        # custom operation insertion
        interp = csdl.custom(theta_control, op=ThetaExplicit(N=N,num_nodes=num_nodes,dt=dt))

        # output interpolated spline vector
        self.register_output('theta_interp', interp)

class ThetaExplicit(csdl.CustomExplicitOperation):
    def initialize(self):
        self.parameters.declare('N') # number of spline control points
        self.parameters.declare('num_nodes') # number of ode timesteps
        self.parameters.declare('dt') # timestep

    def define(self):
        N = self.parameters['N']
        num_nodes = self.parameters['num_nodes']
        dt = self.parameters['dt']

        # input sparse control point vector
        self.add_input('theta_control', shape=(N,))

        # output interpolated spline vector
        self.add_output('theta_interp', shape=(num_nodes,))

        # declare derivatives
        self.declare_derivatives('theta_interp', 'theta_control')

    def compute(self, inputs, outputs):
        N = self.parameters['N']
        num_nodes = self.parameters['num_nodes']
        dt = self.parameters['dt']

        # create spline surrogate model
        xt = np.linspace(0,num_nodes*dt,N)
        yt = inputs['theta_control']

        xlimits = np.array([[0.0, num_nodes*dt]])

        # sm = RBF(d0=100,print_global=False,print_solver=False,)
        
        sm = RMTB(
            xlimits=xlimits,
            order=3,
            num_ctrl_pts=N,
            energy_weight=1e-15,
            regularization_weight=0.0,
            print_global=False,
            print_solver=False,)
        
        sm.set_training_values(xt, yt)
        sm.train()
        
        self.sm = sm

        # vector for spline interpolation
        xnew = np.arange(0, num_nodes*dt, dt)

        # interpolate spline
        ynew = sm.predict_values(xnew)

        # assign interpolated output vector
        outputs['theta_interp'] = ynew

    def compute_derivatives(self, inputs, derivatives):
        N = self.parameters['N']
        num_nodes = self.parameters['num_nodes']
        dt = self.parameters['dt']


        xnew = np.arange(0, num_nodes*dt, dt)
        yder_dict = self.sm.predict_output_derivatives(xnew)

        array = np.array(yder_dict[None])

        derivatives['theta_interp', 'theta_control'] = array


"""
sim = python_csdl_backend.Simulator(theta_exp(N=10,num_nodes=100,dt=0.1))
sim.run()

theta_interp = sim['theta_interp']
print(sim['theta_interp'])
plt.plot(theta_interp)
plt.show()
# print partials
sim.check_partials(compact_print=True)
"""
"""
# test code
N=5
num_nodes=10
dt=0.1
xt = np.linspace(0,num_nodes*dt,N)
yt = np.ones(N)
yt = np.linspace(0,num_nodes*dt,N)
xlimits = np.array([[0.0, num_nodes*dt]])

sm = RBF(d0=0.1,print_global=False,print_solver=False,)
sm.set_training_values(xt, yt)
sm.train()

sm = RMTB(
            xlimits=xlimits,
            order=4,
            num_ctrl_pts=20,
            energy_weight=1e-15,
            regularization_weight=0.0,
            print_global=False,
            print_solver=False,)
sm.set_training_values(xt, yt)
sm.train()

xnew = np.arange(0, num_nodes*dt, dt)
ynew = sm.predict_values(xnew)
dict = sm.predict_output_derivatives(xnew)
array = np.array(dict[None])
print(array)

print(ynew)
"""