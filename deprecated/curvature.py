import csdl

class curve(csdl.Model):
    def initialize(self):
        self.parameters.declare('num')

    def define(self):
        num = self.parameters['num']

        dt = self.declare_variable('dt')

        dtheta = self.declare_variable('dtheta',shape=(num,))
        d_dtheta = self.create_output('d_dtheta',shape=(num,), val=0)
        for i in range(1,num):
            d_dtheta[i] = (dtheta[i] - dtheta[i-1])/dt

        dcx = self.declare_variable('dcx',shape=(num,))
        d_dcx = self.create_output('d_dcx',shape=(num,), val=0)
        for i in range(1,num):
            d_dcx[i] = (dcx[i] - dcx[i-1])/dt

        dcz = self.declare_variable('dcz',shape=(num,))
        d_dcz = self.create_output('d_dcz',shape=(num,), val=0)
        for i in range(1,num):
            d_dcz[i] = (dcz[i] - dcz[i-1])/dt