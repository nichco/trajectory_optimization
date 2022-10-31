import csdl
import numpy as np
import python_csdl_backend

class tonal(csdl.Model):
    def initialize(self):
        self.parameters.declare('options')
        self.parameters.declare('num')
    def define(self):
        options = self.parameters['options']
        num = self.parameters['num']
        
        cruise_ct = self.declare_variable('cruisect', shape=(num,))
        lift_ct = self.declare_variable('liftct', shape=(num,))
        z = self.declare_variable('z', shape=(num,))

        # declare rotor options from dictionary
        num_lift_rotors = options['num_lift_rotors']
        cruise_rotor_diameter = options['cruise_rotor_diameter']
        lift_rotor_diameter = options['lift_rotor_diameter']
        num_lift_blades = options['num_lift_blades']
        num_cruise_blades = options['num_cruise_blades']

        # compute rotor radii
        cruise_rotor_radius = cruise_rotor_diameter/2
        lift_rotor_radius = lift_rotor_diameter/2

        # mean aerodynamic chord
        cruise_mac = 0.15 # (m)
        lift_mac = 0.15 # (m)

        # compute rotor area and disk area
        cruise_ab = cruise_mac*cruise_rotor_radius*num_cruise_blades # rotor area
        lift_ab = lift_mac*lift_rotor_radius*num_lift_blades # rotor area
        cruise_ad = np.pi*(cruise_rotor_radius**2)
        lift_ad = np.pi*(lift_rotor_radius**2)

        # compute blade solidity
        cruise_sigma = cruise_ab/cruise_ad
        lift_sigma = lift_ab/lift_ad

        # compute rotor speed
        control_x = self.declare_variable('control_x', shape=(num,))
        control_z = self.declare_variable('control_z', shape=(num,))
        omega_x = 2*np.pi*control_x/60 # (rad/s)
        omega_z = 2*np.pi*control_z/60 # (rad/s)
        cruise_rotor_speed = omega_x*cruise_rotor_radius
        lift_rotor_speed = omega_z*lift_rotor_radius

        """
        # schlegel king and mull broadband noise model
        cruise_spl_150 = 10*csdl.log(((cruise_rotor_speed)**6)*cruise_ab*((cruise_ct/cruise_sigma)**2)) - 42.9
        lift_spl_150 = 10*csdl.log(((lift_rotor_speed)**6)*lift_ab*((lift_ct/lift_sigma)**2)) - 42.9
        self.register_output('cruise_spl_150',cruise_spl_150)
        self.register_output('lift_spl_150',lift_spl_150)

        # propogate to ground level
        cruise_elevation_angle = 0 # (rad)
        lift_elevation_angle = np.pi/2 # (rad)

        cruise_spl = cruise_spl_150 + 20*csdl.log(csdl.sin(cruise_elevation_angle)/(z/150))
        lift_spl = lift_spl_150 + 20*csdl.log(csdl.sin(lift_elevation_angle)/(z/150))
        self.register_output('cruise_spl',cruise_spl)
        self.register_output('lift_spl',lift_spl)
        """


        cruise_spl_150 = self.create_output('cruise_spl_150',shape=(num,))
        for i in range(num):
            cruise_spl_150[i,] = 10*csdl.log10(((cruise_rotor_speed[i])**6)*cruise_ab*((cruise_ct[i]/cruise_sigma)**2)) - 42.9


        # propogate to ground level
        cruise_spl = self.create_output('cruise_spl',shape=(num,))
        for i in range(num):
            # cruise_spl = cruise_spl_150[i] + 20*csdl.log(np.sin(cruise_elevation_angle)/(z[i]/150))
            cruise_spl[i,] = cruise_spl_150[i] + 20*csdl.log10(1/(z[i]/150))


        max_cruise_spl = csdl.max(cruise_spl)
        # max_lift_spl = csdl.max(lift_spl)

