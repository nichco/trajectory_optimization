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


    def compute_derivatives(self, inputs, derivatives):
        # compute derivatives with SMT






"""
# run model
sim = python_csdl_backend.Simulator(throttle())
sim.run()

print(sim['in_throttle'])
# print partials
# sim.check_partials(compact_print=True)
"""