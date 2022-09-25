import csdl
import python_csdl_backend

class load_factor(csdl.Model):
    def initialize(self):
        pass
    def define(self):
        
        lift = self.declare_variable('lift')
        weight = self.declare_variable('weight')

        n = lift/weight

        self.register_output('load_factor',n)

class dynamic_pressure(csdl.Model):
    def initialize(self):
        pass
    def define(self):
        
        density = self.declare_variable('density')
        velocity = self.declare_variable('velocity')

        self.register_output('dynamic_pressure',0.5*density*velocity**2)