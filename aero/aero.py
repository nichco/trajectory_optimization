import csdl
#from aero.aero_explicit import airfoil
from aero.cl_explicit import cl_aero
from aero.cd_explicit import cd_aero
#from atmosphere.new_atm import Atm
import python_csdl_backend

class aero(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes')
        self.parameters.declare('options')
    def define(self):
        n = self.parameters['num_nodes']
        options = self.parameters['options']

        s = options['wing_area']

        alpha = self.declare_variable('alpha', shape=n)
        self.register_output('alpha_w', 1*alpha)

        #self.add(Atm(num_nodes=n), name='atmosphere')
        density = self.declare_variable('density', shape=n)
        velocity = self.declare_variable('v', shape=n)
        #a = self.declare_variable('speed_of_sound', shape=n)
        #self.register_output('mach',velocity/a)
        
        self.add(cl_aero(num_nodes=n),name='cl_aero')
        self.add(cd_aero(num_nodes=n),name='cd_aero')
        cl = self.declare_variable('cl', shape=n)
        cd = self.declare_variable('cd', shape=n)
        
        q = 0.5*density*(velocity**2)

        self.register_output('lift', q*s*cl)
        self.register_output('drag', q*s*cd)





if __name__ == '__main__':

    options = {}
    options['wing_area'] = 16.2 # wing area (m^2)


    # run model
    sim = python_csdl_backend.Simulator(aero(num_nodes=10,options=options))
    sim.run()

    print(sim['cl'])
    print(sim['cd'])
    print(sim['alpha_w'])

    # print partials
    sim.check_partials(compact_print=True)
