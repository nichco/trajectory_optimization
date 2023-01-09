import csdl
import numpy as np
import python_csdl_backend

class control(csdl.Model):
    def initialize(self):
        self.parameters.declare('name')
        self.parameters.declare('order')
        self.parameters.declare('num_nodes')
    def define(self):
        order = self.parameters['order']
        name = self.parameters['name']
        num_nodes = self.parameters['num_nodes']

        control = self.declare_variable('in_'+name,shape=1)

        # if order == 0:
        interpolated_control = csdl.expand(control,shape=num_nodes)


        self.register_output('control_'+name,interpolated_control)

