import csdl
import numpy as np

class slope(csdl.Model):
    def initialize(self):
        self.parameters.declare('dt')
        self.parameters.declare('num')

    def define(self):
        dt = self.parameters['dt']
        num = self.parameters['num']


        theta = self.declare_variable('theta',shape=(num,))
        dtheta = self.create_output('dtheta',shape=(num,), val=0)
        for i in range(1,num):
            dtheta[i] = (theta[i] - theta[i-1])/dt

        pwr = self.declare_variable('interp',shape=(num,))
        dpwr = self.create_output('dpwr',shape=(num,), val=0)
        for i in range(1,num):
            dpwr[i] = (pwr[i] - pwr[i-1])/dt
        