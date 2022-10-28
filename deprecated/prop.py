import csdl
import python_csdl_backend

class prop(csdl.Model):
    def initialize(self):
        pass
    def define(self):
        
        velocity = self.declare_variable('velocity')
        pwr = self.declare_variable('pwr') # power setting (0-1)%

        max_power = 10000

        current_power = pwr*max_power

        thrust = current_power# /velocity

        self.register_output('thrust', thrust)