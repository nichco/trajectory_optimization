import csdl
from aero_explicit import airfoil
from atm_explicit import Atm
import numpy as np

class aero(csdl.Model):
    def initialize(self):
        self.parameters.declare('options')
    def define(self):
        options = self.parameters['options']

        wing_set_angle = options['wing_set_angle']

        alpha = self.declare_variable('alpha')
        self.register_output('alpha_w',alpha + wing_set_angle*2*np.pi/360) # add wing set angle to aoa as an input to the aero model
        
        self.add(airfoil())
        self.add(Atm())
        
        s = options['wing_area']
        cl = self.declare_variable('cl')
        cd_0 = options['cd_0']
        density = self.declare_variable('density')
        velocity = self.declare_variable('velocity')
        oswald = options['oswald']
        AR = self.declare_variable('aspect_ratio',val=7.52)

        q = 0.5*density*(velocity**2) # compute dynamic pressure

        cd_total = cd_0 + (cl**2)/(np.pi*oswald*AR) # total drag coefficient

        self.register_output('lift',q*s*oswald*cl)
        self.register_output('drag',q*s*cd_total)
        

