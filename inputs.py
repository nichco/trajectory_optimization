import csdl
import python_csdl_backend

class inputs(csdl.Model):
    def initialize(self):
        self.parameters.declare('options')
    def define(self):
        options = self.parameters['options']

        # declare external inputs from options dictionary
        mass = options['mass']
        wing_area = options['wing_area']
        wing_set_angle = options['wing_set_angle']
        oswald = options['oswald']
        cd_0 = options['cd_0']
        cruise_rotor_diameter = options['cruise_rotor_diameter']
        lift_rotor_diameter = options['lift_rotor_diameter']
        num_lift_rotors = options['num_lift_rotors']
        gravity = options['gravity']
        

        # add external inputs
        self.create_input('mass',mass)
        self.create_input('wing_area',wing_area)
        self.create_input('wing_set_angle',wing_set_angle)
        self.create_input('oswald',oswald)
        self.create_input('cd_0',cd_0)
        self.create_input('cruise_rotor_diameter',cruise_rotor_diameter)
        self.create_input('lift_rotor_diameter',lift_rotor_diameter)
        self.create_input('num_lift_rotors',num_lift_rotors)
        self.create_input('gravity',gravity)