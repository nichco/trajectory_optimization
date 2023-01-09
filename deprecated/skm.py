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
        
        # declare variables
        cruise_ct = self.declare_variable('cruisect', shape=(num,),val=0.3)
        lift_ct = self.declare_variable('liftct', shape=(num,),val=0.3)
        h = self.declare_variable('h', shape=(num,),val=300)
        theta = self.declare_variable('theta', shape=(num,),val=0)
        alpha = self.declare_variable('control_alpha', shape=(num,),val=0)
        v = self.declare_variable('v', shape=(num,),val=10)
        control_x = self.declare_variable('control_x', shape=(num,),val=1000)
        control_z = self.declare_variable('control_z', shape=(num,),val=1000)

        # declare rotor options from dictionary
        num_lift_rotors = options['num_lift_rotors']
        cruise_rotor_diameter = options['cruise_rotor_diameter']
        lift_rotor_diameter = options['lift_rotor_diameter']
        num_lift_blades = options['num_lift_blades']
        num_cruise_blades = options['num_cruise_blades']
        epsilon = 1
        
        # compute Davidson and Hargest corrections
        #j_cruise = v/((control_x/60)*cruise_rotor_diameter)
        #j_lift = v/((control_z/60)*lift_rotor_diameter)
        #f_cruise = 8.33*j_cruise
        #f_lift = 8.33*j_lift
        #self.register_output('f_cruise',f_cruise)
        #self.register_output('f_lift',f_lift)
        
        # mean aerodynamic chord
        cruise_mac = 0.15 # (m)
        lift_mac = 0.15 # (m)

        # compute rotor area and disk area
        cruise_ab = cruise_mac*(cruise_rotor_diameter/2)*num_cruise_blades # rotor area
        lift_ab = lift_mac*(lift_rotor_diameter/2)*num_lift_blades # rotor area
        cruise_ad = np.pi*((cruise_rotor_diameter/2)**2)
        lift_ad = np.pi*((lift_rotor_diameter/2)**2)

        # compute blade solidity
        cruise_sigma = cruise_ab/cruise_ad
        lift_sigma = lift_ab/lift_ad

        # compute rotor speed
        omega_x = 2*np.pi*control_x/60 # (rad/s)
        omega_z = 2*np.pi*control_z/60 # (rad/s)
        cruise_rotor_speed = omega_x*cruise_rotor_diameter/2
        lift_rotor_speed = omega_z*lift_rotor_diameter/2


        # schlegel king and mull broadband noise model
        cruise_spl_150 = self.create_output('cruise_spl_150',shape=(num,))
        lift_spl_150 = self.create_output('lift_spl_150',shape=(num,))
        for i in range(num):
            cval = (cruise_rotor_speed[i]**6)*cruise_ab*((cruise_ct[i]/cruise_sigma)**2)
            lval = (lift_rotor_speed[i]**6)*lift_ab*((lift_ct[i]/lift_sigma)**2)
            cruise_spl_150[i] = 10*csdl.log10(cval + epsilon) - 36.7 #+ f_cruise[i]
            lift_spl_150[i] = 10*csdl.log10(lval + epsilon) - 36.7 #+ f_lift[i]
        
        max_cruise_spl_150 = csdl.max(cruise_spl_150)
        max_lift_spl_150 = csdl.max(lift_spl_150)
        self.register_output('max_cruise_spl_150', max_cruise_spl_150)
        self.register_output('max_lift_spl_150', max_lift_spl_150)
        
        
        
        # propogate to ground level
        ref_angle = self.declare_variable('ref_angle',val=np.pi/2,shape=(num,))
        lang = ref_angle - theta # rotor angles to observer
        cang = 1*theta
        
        val = (h + 1)/150
        cruise_spl = cruise_spl_150 - 20*csdl.log10(val)
        lift_spl = lift_spl_150 - 20*csdl.log10(val)
        self.register_output('cruise_spl', cruise_spl)
        self.register_output('lift_spl', lift_spl)
        
        sc = csdl.exp(np.log(10)*cruise_spl/10)
        sl = csdl.exp(np.log(10)*lift_spl/10)
        sum_spl = 10*csdl.log10(sc + num_lift_rotors*sl)
        self.register_output('sum_spl', sum_spl)
        
        max_spl = csdl.max(sum_spl)
        self.register_output('max_spl',max_spl)
        


if __name__ == '__main__':
    
    options = {}
    options['cruise_rotor_diameter'] = 2
    options['lift_rotor_diameter'] = 2
    options['num_lift_rotors'] = 8
    options['num_lift_blades'] = 2
    options['num_cruise_blades'] = 4
    options['epsilon'] = 1 # scaler for log10 operations
    
    num=4
    sim = python_csdl_backend.Simulator(tonal(options=options,num=num))
    sim.run()
    

    #print('f cruise: ', sim['f_cruise'])
    #print('f lift: ', sim['f_lift'])
    print('cruise spl150: ', sim['cruise_spl_150'])
    print('lift spl150: ', sim['lift_spl_150'])
    print('cruise spl: ', sim['cruise_spl'])
    print('lift spl: ', sim['lift_spl'])
    print('sum spl: ', sim['sum_spl'])
    print('max spl: ', sim['max_spl'])







