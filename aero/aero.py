import csdl
from aero.aero_explicit import airfoil
from atmosphere.atm_explicit import Atm
import numpy as np
import python_csdl_backend

class aero(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes')
        self.parameters.declare('options')
    def define(self):
        n = self.parameters['num_nodes']
        options = self.parameters['options']

        alpha = self.declare_variable('control_alpha', shape=n)
        self.register_output('alpha_w', alpha + np.deg2rad(options['wing_set_angle']))
        
        self.add(airfoil(num_nodes=n), name='airfoil')
        self.add(Atm(num_nodes=n), name='atmosphere')
        
        s = options['wing_area']
        cd_0 = options['cd_0']
        e = options['span_efficiency']
        #aspect_ratio = options['aspect_ratio']

        cl = self.declare_variable('cl', shape=n)
        cdi = self.declare_variable('cd', shape=n)
        density = self.declare_variable('density', shape=n)
        velocity = self.declare_variable('v', shape=n)
        
        q = 0.5*density*(velocity**2)
        # cd_total = cd_0 + (cl**2)/(np.pi*e*aspect_ratio) # total drag coefficient (this isn't right, need cd from airfoil() surrogate)
        cd = cd_0 + cdi

        self.register_output('lift', q*s*cl)
        self.register_output('drag', q*s*cd)





if __name__ == '__main__':

    options = {}
    options['wing_area'] = 16.2 # wing area (m^2)
    options['aspect_ratio'] = 7.5
    options['wing_set_angle'] = 3 # (deg)
    options['oswald'] = 0.8 # finite wing correction
    options['cd_0'] = 0.025 # zero-lift drag coefficient


    # run model
    sim = python_csdl_backend.Simulator(aero(num_nodes=10,options=options))
    sim.run()

    print(sim['cl'])
    print(sim['cd'])
    print(sim['alpha_w'])

    # print partials
    sim.check_partials(compact_print=True)
