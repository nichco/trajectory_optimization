import csdl

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

        control_x = self.declare_variable('control_x',shape=(num,))
        dcx = self.create_output('dcx',shape=(num,), val=0)
        for i in range(1,num):
            dcx[i] = (control_x[i] - control_x[i-1])/dt
        