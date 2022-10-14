import csdl

class curve(csdl.Model):
    def initialize(self):
        self.parameters.declare('dt')
        self.parameters.declare('num')

    def define(self):
        dt = self.parameters['dt']
        num = self.parameters['num']


        dtheta = self.declare_variable('dtheta',shape=(num,))
        d_dtheta = self.create_output('d_dtheta',shape=(num,), val=0)
        for i in range(1,num):
            d_dtheta[i] = (dtheta[i] - dtheta[i-1])/dt

        dpwr = self.declare_variable('dpwr',shape=(num,))
        d_dpwr = self.create_output('d_dpwr',shape=(num,), val=0)
        for i in range(1,num):
            d_dpwr[i] = (dpwr[i] - dpwr[i-1])/dt