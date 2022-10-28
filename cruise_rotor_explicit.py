from pitt_peters_rotor_surrogate import sm_ct, sm_cp
import csdl
import python_csdl_backend

class rotor(csdl.Model):
    def initialize(self):
        self.parameters.declare('name',types=str)
    def define(self):
        name = self.parameters['name']

        vAxial = self.declare_variable(name+'vAxial')
        vTan = self.declare_variable(name+'vTan')
        # custom operation insertion
        cruise_ct, cruise_cp = csdl.custom(vAxial,vTan, op=rotorExplicit(name=name))
        self.register_output(name+'cruise_ct', cruise_ct)
        self.register_output(name+'cruise_cp', cruise_cp)

class rotorExplicit(csdl.CustomExplicitOperation):
    def initialize(self):
        self.parameters.declare('name',types=str)
    def define(self):
        name = self.parameters['name']

        # input: axial and tangential freestream velocities
        self.add_input(name+'vAxial', shape=(1,))
        self.add_input(name+'vTan', shape=(1,))

        # output: thrust coefficient and power coefficient
        self.add_output(name+'ct', shape=(1,))
        self.add_output(name+'cp', shape=(1,))

        # declare derivatives
        self.declare_derivatives(name+'ct', name+'vAxial')
        self.declare_derivatives(name+'ct', name+'vTan')
        self.declare_derivatives(name+'cp', name+'vAxial')
        self.declare_derivatives(name+'cp', name+'vTan')