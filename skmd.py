import csdl
import numpy as np
import python_csdl_backend
import matplotlib.pyplot as plt

class tonal(csdl.Model):
    def initialize(self):
        self.parameters.declare('options')
        self.parameters.declare('num')
    def define(self):
        options = self.parameters['options']
        num = self.parameters['num']
        
        # declare variables
        cruise_ct = self.declare_variable('cruisect', shape=(num,),val=0.2)
        lift_ct = self.declare_variable('liftct', shape=(num,),val=0.3)
        h = self.declare_variable('h', shape=(num,),val=100)
        theta = self.declare_variable('theta', shape=(num,),val=0)
        control_x = self.declare_variable('control_x', shape=(num,),val=1000)
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
        
        # compute broadband spl_d
        """
        # untested equation
        cruise_spl_d = 10*csdl.log10((cvt**2.16)*(cab**0.6)*((cct/cruise_sigma)**1.2) + 0.01) + 49.909
        lift_spl_d = 10*csdl.log10((lvt**2.16)*(lab**0.6)*((lct/lift_sigma)**1.2) + 0.01) + 49.909
        self.register_output('cruise_spl_d', cruise_spl_d)
        self.register_output('lift_spl_d', lift_spl_d)
        """
        # SKM model transformed to SPL_D
        cruise_spl150 = 10*csdl.log10((cvt**6)*cab*((cct/cruise_sigma)**2) + 0.01) - 42.9
        cruise_spl_d = cruise_spl150 + 20*np.log10(150/(cruise_rotor_diameter))

        lift_spl150 = 10*csdl.log10((lvt**6)*lab*((lct/lift_sigma)**2) + 0.01) - 42.9
        lift_spl_d = lift_spl150 + 20*np.log10(150/(lift_rotor_diameter))

        self.register_output('cruise_spl_d',cruise_spl_d)
        self.register_output('lift_spl_d',lift_spl_d)


        

        """
        # fallback option
        b1, b2, b3 = 0.031, 6.2429, 0.7267
        s = ((h+1)**2)**0.5 # absolute value of altitude
        cruise_angle = 1*theta
        lift_angle = theta + np.pi/2
        
        ct2 = b2 + b3 - b3*((csdl.sin(cruise_angle)**2)**0.5)
        cruise_spl_gl = (((csdl.sin(cruise_angle)**2)**0.5)**b1)*cruise_spl_d - ct2*csdl.log10(s/cruise_rotor_diameter)
        self.register_output('cruise_spl_gl',cruise_spl_gl)
        
        lt2 = b2 + b3 - b3*((csdl.sin(lift_angle)**2)**0.5)
        lift_spl_gl = (((csdl.sin(lift_angle)**2)**0.5)**b1)*lift_spl_d - lt2*csdl.log10(s/lift_rotor_diameter)
        self.register_output('lift_spl_gl',lift_spl_gl)
        
        max_cspl = csdl.max(cruise_spl_gl)
        self.register_output('max_cspl',max_cspl)
        max_lspl = csdl.max(lift_spl_gl)
        self.register_output('max_lspl',max_lspl)
        """
 
        # new values
        # b1, b2, b3 = 0.031, 6.2429, 0.7267
        # old values
        b1, b2, b3 = 0.0209, 18.2429, 6.7267
        r = self.create_input('range',val=np.linspace(-200,200,num),shape=(num,))
        hc = h + 1 # add a correction factor so equations aren't undefined
        
        max_spl_gl = self.create_output('max_spl_gl',shape=(num,))
        max_cruise_spl_gl = self.create_output('max_cruise_spl_gl',shape=(num,))
        max_lift_spl_gl = self.create_output('max_lift_spl_gl',shape=(num,))
        
        for i in range(num):
            ex_theta = csdl.expand(theta[i],shape=(num,))
            ex_hc = csdl.expand(hc[i],shape=(num,))
            ex_cspl_d = csdl.expand(cruise_spl_d[i],shape=(num,))
            ex_lspl_d = csdl.expand(lift_spl_d[i],shape=(num,))
            beta = csdl.arctan(r/ex_hc)
            s = (r**2 + ex_hc**2)**0.5
            
            cruise_angle = beta + ex_theta
            lift_angle = beta + ex_theta + np.pi/2
            
            ct2 = b2 + b3 - b3*((csdl.sin(cruise_angle)**2)**0.5)
            cruise_spl_gl = (((csdl.sin(cruise_angle)**2)**0.5)**b1)*ex_cspl_d - ct2*csdl.log10(s/cruise_rotor_diameter)
            
            lt2 = b2 + b3 - b3*((csdl.sin(lift_angle)**2)**0.5)
            lift_spl_gl = (((csdl.sin(lift_angle)**2)**0.5)**b1)*ex_lspl_d - lt2*csdl.log10(s/lift_rotor_diameter)

            # sum sources at ground level over the r vector
            sum_gl = 10*csdl.log10(csdl.exp_a(10,0.1*cruise_spl_gl) + num_lift_rotors*csdl.exp_a(10,0.1*lift_spl_gl))

            # spl at a given timestep is the maximum of the spl sum across the r vector
            max_spl_gl[i] = csdl.max(sum_gl)
            max_cruise_spl_gl[i] = csdl.max(cruise_spl_gl)
            max_lift_spl_gl[i] = csdl.max(lift_spl_gl)
        
        
        self.register_output('csplgl',cruise_spl_gl)
        self.register_output('lsplgl',lift_spl_gl)
        
        
        # maximum of the spl sum across the timestep vector
        mspl = csdl.max(max_spl_gl)
        self.register_output('mspl',mspl)

        
        # last 2/3 of trajectory
        seg_cspl = max_cruise_spl_gl[10:num]
        seg_lspl = max_lift_spl_gl[10:num]
        seg_ospl = max_spl_gl[10:num]
        self.register_output('seg_cspl',seg_cspl)
        self.register_output('seg_lspl',seg_lspl)
        self.register_output('seg_ospl',seg_ospl)
        

        
        
        

        
        


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

    options['epsilon'] = 1 # scaler for log10 operations
    
    num=20
    sim = python_csdl_backend.Simulator(tonal(options=options,num=num))
    sim.run()
    

    print('cruise spl d: ', sim['cruise_spl_d'])
    print('lift spl d: ', sim['lift_spl_d'])
    
    print('max spl gl: ', sim['max_spl_gl'])
    print('max lift spl gl: ', sim['max_lift_spl_gl'])
    """
    x = np.linspace(-500,500,num)
    plt.plot(x,sim['csplgl'],color='k',linestyle='solid')
    plt.plot(x,sim['lsplgl'],color='k',linestyle='dashed')
    plt.axis('off')
    # plt.box(False)
    # plt.legend(['in rotor plane', 'out of rotor plane'], frameon=False)
    plt.xlabel('observer distance at ground level (m)')
    plt.ylabel('sound pressure level (db)')
    plt.savefig('spl_diagram', dpi=1200, bbox_inches='tight')
    plt.show()
    """







