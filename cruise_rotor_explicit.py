from pitt_peters_rotor_surrogate import sm_ct, sm_cp
import csdl
import python_csdl_backend

class rotor(csdl.Model):
    def initialize(self):
        self.parameters.declare('name',types=str)
    def define(self):
        name = self.parameters['name']

        vAxial = self.declare_variable('vAxial')
        vTan = self.declare_variable('vTan')
        # custom operation insertion
        cruise_ct, cruise_cp = csdl.custom(vAxial,vTan, op=rotorExplicit(name=name))
        self.register_output(name+'cruise_ct', cruise_ct)
        self.register_output(name+'cruise_cp', cruise_cp)

class rotorExplicit(csdl.CustomExplicitOperation):
    def initialize(self):
        self.parameters.declare('name',types=str)
    def define(self):
        name = self.parameters['name']