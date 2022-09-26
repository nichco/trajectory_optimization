import csdl
from aero_explicit import airfoil
from performance import dynamic_pressure

class aero(csdl.Model):
    def initialize(self):
        pass
    def define(self):
        
        self.add(airfoil())
        
        s = self.declare_variable('wing_area')

        cl = self.declare_variable('cl')
        cd = self.declare_variable('cd')

        self.add(dynamic_pressure())
        q = self.declare_variable('dynamic_pressure')

        self.register_output('lift',q*s*cl)
        self.register_output('drag',q*s*cd)
        

