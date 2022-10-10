import csdl
from aero_explicit import airfoil
from atm_explicit import Atm

class aero(csdl.Model):
    def initialize(self):
        pass
    def define(self):
        
        self.add(airfoil())
        self.add(Atm())
        
        s = self.declare_variable('ref_area')
        cl = self.declare_variable('cl')
        cd_i = self.declare_variable('cd')
        pressure = self.declare_variable('pressure')
        density = self.declare_variable('density')
        velocity = self.declare_variable('velocity')

        q = 0.5*density*velocity**2

        cd_0 = 0.02
        cd_total = cd_0 + cd_i

        self.register_output('lift',q*s*cl)
        self.register_output('drag',q*s*cd_total)
        

