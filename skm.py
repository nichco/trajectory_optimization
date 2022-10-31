import csdl
import numpy as np
import python_csdl_backend

class tonal(csdl.Model):
    def initialize(self):
        pass
    def define(self):
        
        cruise_sigma = self.declare_variable('cruise_sigma',val=0.1) # rotor solidity
        lift_sigma = self.declare_variable('liftsigma',val=0.1) # rotor solidity
        cruise_ct = self.declare_variable('cruisect')
        lift_ct = self.declare_variable('liftct')
        num_lift_rotors = self.declare_variable('num_lift_rotors')
        cruise_rotor_diameter = self.declare_variable('cruise_rotor_diameter')
        lift_rotor_diameter = self.declare_variable('lift_rotor_diameter')

        ab = self.declare_variable('blade_area')

        control_x = self.declare_variable('control_x')
        control_z = self.declare_variable('control_z')

        omega_x = 2*np.pi*control_x/60 # (rad/s)
        omega_z = 2*np.pi*control_z/60 # (rad/s)

        cruise_rotor_radius = cruise_rotor_diameter/2
        lift_rotor_radius = lift_rotor_diameter/2

        cruise_rotor_speed = omega_x*cruise_rotor_radius
        lift_rotor_speed = omega_z*lift_rotor_radius


        # schlegel king and mull broadband noise model
        cruise_spl_150 = 10*csdl.log(((cruise_rotor_speed)**6)*ab*((cruise_ct/cruise_sigma)**2)) - 42.9
        lift_spl_150 = 10*csdl.log(((lift_rotor_speed)**6)*ab*((lift_ct/lift_sigma)**2)) - 42.9


        # propogate to ground level
        #

