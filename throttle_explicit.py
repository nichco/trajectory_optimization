from smt.surrogate_models import RMTB
import numpy as np
import matplotlib.pyplot as plt
import csdl
import python_csdl_backend

class throttle(csdl.Model):
    def initialize(self):
        pass
    def define(self):
        throttle = self.declare_variable('throttle')
        # custom operation insertion
        in_throttle = csdl.custom(throttle, op=ThrottleExplicit()) # interpolate sparse throttle vector with SMT RMTB
        self.register_output('in_throttle', in_throttle)

class ThrottleExplicit(csdl.CustomExplicitOperation):
    def initialize(self):
        pass
    def define(self):
        # input sparse throttle vector
        self.add_input('throttle', shape=(N,))
        # output interpolated throttle vector
        self.add_output('in_throttle', shape=(num_nodes,))
        # declare derivatives
        self.declare_derivatives('in_throttle', 'throttle')

    def compute(self, inputs, outputs):
        # add surrogate model

        xt = np.linspace(0,num_nodes*dt,N)
        yt = inputs['throttle']

        xlimits = np.array([[0.0, num_nodes*dt]])

        sm = RMTB(
            xlimits=xlimits,
            order=4,
            num_ctrl_pts=20,
            energy_weight=1e-15,
            regularization_weight=0.0,)
        sm.set_training_values(xt, yt)
        sm.train()

        t_vec = np.linspace(0,num_nodes*dt,num_nodes)
        in_throttle = sm.predict_values(t_vec)

        outputs['in_throttle'] = 1*in_throttle


    def compute_derivatives(self, inputs, derivatives):
        # compute derivatives with SMT
        dthrottle_dt = sm.predict_derivatives(inputs['alpha'], 0)

        derivatives['cl', 'alpha'] = dcl_dalpha






"""
# run model
sim = python_csdl_backend.Simulator(throttle())
sim.run()

print(sim['in_throttle'])
# print partials
# sim.check_partials(compact_print=True)
"""