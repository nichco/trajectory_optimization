import csdl
from aero_explicit import airfoil
from atm_explicit import Atm
import numpy as np

class aero(csdl.Model):
    def initialize(self):
        pass
    def define(self):

        wing_set_angle = self.declare_variable('wing_set_angle')
        alpha = self.declare_variable('alpha')
        self.register_output('alpha_w',alpha + wing_set_angle*2*np.pi/360) # add wing set angle to aoa as an input to the aero model
        
        self.add(airfoil())
        self.add(Atm())
        
        s = self.declare_variable('ref_area')
        cl = self.declare_variable('cl')
        cd_i = self.declare_variable('cd')
        pressure = self.declare_variable('pressure')
        density = self.declare_variable('density')
        velocity = self.declare_variable('velocity')

        q = 0.5*density*velocity**2 # compute dynamic pressure

        cd_0 = 0.02 # zero lift drag coefficient
        cd_total = cd_0 + cd_i # total drag coefficient

        self.register_output('lift',q*s*cl)
        self.register_output('drag',q*s*cd_total)
        

