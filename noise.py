import csdl
import numpy as np
import python_csdl_backend
import matplotlib.pyplot as plt

class noise(csdl.Model):
    def initialize(self):
        self.parameters.declare('options')
        self.parameters.declare('num')
    def define(self):
        options = self.parameters['options']
        num = self.parameters['num']

        # declare variables
        cruise_ct = self.declare_variable('cruisect', shape=(num,),val=0.2)
        lift_ct = self.declare_variable('liftct', shape=(num,),val=0.2)
        theta = self.declare_variable('theta', shape=(num,),val=0)
        control_x = self.declare_variable('control_x', shape=(num,),val=1200)
        control_z = self.declare_variable('control_z', shape=(num,),val=1000)

        # declare rotor options from dictionary
        num_lift_rotors = options['num_lift_rotors']
        cruise_rotor_diameter = options['cruise_rotor_diameter']
        lift_rotor_diameter = options['lift_rotor_diameter']
        num_lift_blades = options['num_lift_blades']
        num_cruise_blades = options['num_cruise_blades']
        cruise_mac, lift_mac = options['cruise_mac'], options['lift_mac']
        cruise_sigma = options['c_sigma']
        lift_sigma = options['l_sigma']

        # compute blade area
        cab = cruise_mac*(cruise_rotor_diameter/2)*num_cruise_blades*0.8
        lab = lift_mac*(lift_rotor_diameter/2)*num_lift_blades*0.8

        # compute rotor tip speed
        cvt = (control_x/60)*2*np.pi*(cruise_rotor_diameter/2)
        lvt = (control_z/60)*2*np.pi*(lift_rotor_diameter/2)

        # absolute value of thrust coefficients
        cct = (cruise_ct**2)**0.5
        lct = (lift_ct**2)**0.5

        # SKM model
        cruise_spl_150 = 10*csdl.log10((cvt**6)*cab*((cct/cruise_sigma)**2) + 0.01) - 42.9
        lift_spl_150 = 10*csdl.log10((lvt**6)*lab*((lct/lift_sigma)**2) + 0.01) - 42.9
        self.register_output('cruise_spl_150',cruise_spl_150)
        self.register_output('lift_spl_150',lift_spl_150)

        # transformed to observer location
        theta = np.pi/2 # (rad)
        s0 = 76.2 # (m)

        cruise_spl = cruise_spl_150 + 20*np.log10(np.sin(theta)/(s0/150))
        lift_spl = lift_spl_150 + 20*np.log10(np.sin(theta)/(s0/150))
        self.register_output('cruise_spl_s',cruise_spl)
        self.register_output('lift_spl_s',lift_spl)

        # sum rotor noise
        sum_spl = 10*csdl.log10(csdl.exp_a(10,0.1*cruise_spl) + num_lift_rotors*csdl.exp_a(10,0.1*lift_spl))
        self.register_output('sum_spl',sum_spl)
        


if __name__ == '__main__':
    
    options = {}
    options['cruise_rotor_diameter'] = 2
    options['lift_rotor_diameter'] = 2
    options['num_lift_rotors'] = 8
    options['num_lift_blades'] = 2
    options['num_cruise_blades'] = 4
    options['cruise_mac'] = 0.15
    options['lift_mac'] = 0.15

    options['c_sigma'] = 0.19
    options['l_sigma'] = 0.095

    num=20
    sim = python_csdl_backend.Simulator(noise(options=options,num=num))
    sim.run()

    print('cruise spl 150: ', sim['cruise_spl_150'])
    print('lift spl 150: ', sim['lift_spl_150'])
    print('cruise spl s: ', sim['cruise_spl_s'])
    print('lift spl s: ', sim['lift_spl_s'])
    print('sum spl: ', sim['sum_spl'])
