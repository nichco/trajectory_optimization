import csdl
from aero.aero import aero
from rotors.rotor import rotor
#from rotors.liftRotor import liftRotor
#from rotors.cruiseRotor import cruiseRotor
from motors.motor_explicit import motor
import numpy as np
import python_csdl_backend


class ODESystemModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes')
        self.parameters.declare('options')

    def define(self):
        # Required every time for ODE systems or Profile Output systems
        n = self.parameters['num_nodes']
        options = self.parameters['options']
        
        # states
        v = self.create_input('v', shape=n)
        gamma = self.create_input('gamma', shape=n)
        h = self.create_input('h', shape=n)
        x = self.create_input('x', shape=n)
        e = self.create_input('e', shape=n)
        # parameters are inputs
        control_x = self.declare_variable('control_x', shape=(n))
        control_z = self.declare_variable('control_z', shape=(n))
        alpha = self.declare_variable('control_alpha', shape=(n))
        m = options['mass']
        g = options['gravity']
        num_lift_rotors = options['num_lift_rotors']
        
        # add aerodynamic model
        self.add(aero(num_nodes=n, options=options), name='aero')
        # define outputs from aerodynamic model
        L = self.declare_variable('lift', shape=(n))
        D = self.declare_variable('drag', shape=(n))

        # rotor and motor models
        cname = 'cruise'
        self.register_output(cname+'vAxial',((v*csdl.cos(alpha))**2)**0.5)
        self.register_output(cname+'vTan',((v*csdl.sin(alpha))**2)**0.5)
        self.register_output(cname+'n',1*control_x/60) # rotations per second for rotor model
        self.register_output(cname+'m',1*control_x) # rotations per minute for motor model
        self.add(rotor(name=cname,options=options,num_nodes=n), name=cname+'rotor')
        self.add(motor(name=cname,num_nodes=n), name=cname+'motor')
        cruiseeta = self.declare_variable(cname+'eta',shape=(n))
        TC = self.declare_variable(cname+'thrust', shape=(n))
        cruisepower = self.declare_variable(cname+'power', shape=(n))

        lname = 'lift'
        self.register_output(lname+'vAxial',v*csdl.sin(alpha))
        self.register_output(lname+'vTan',v*csdl.cos(alpha))
        self.register_output(lname+'n',1*control_z/60) # rotations per second for rotor model
        self.register_output(lname+'m',1*control_z) # rotations per minute for motor model
        self.add(rotor(name=lname,options=options,num_nodes=n), name=lname+'rotor')
        self.add(motor(name=lname,num_nodes=n), name=lname+'motor')
        lifteta = self.declare_variable(lname+'eta',shape=(n))
        TL_s = self.declare_variable(lname+'thrust', shape=(n))
        TL = num_lift_rotors*TL_s
        liftpower_s = self.declare_variable(lname+'power', shape=(n))
        liftpower = num_lift_rotors*liftpower_s






        
        # system of ODE's
        dv = (TC/m)*csdl.cos(alpha) + (TL/m)*csdl.sin(alpha) - (D/m) - g*csdl.sin(gamma)
        dgamma = (TC/(m*v))*csdl.sin(alpha) + (TL/(m*v))*csdl.cos(alpha) + (L/(m*v)) - (g*csdl.cos(gamma)/v)
        dh = v*csdl.sin(gamma)
        dx = v*csdl.cos(gamma)
        de = options['energy_scale']*((cruisepower/cruiseeta) + (liftpower/lifteta))

        # register outputs
        self.register_output('dv', dv)
        self.register_output('dgamma', dgamma)
        self.register_output('dh', dh)
        self.register_output('dx', dx)
        self.register_output('de', de)

 




       
if __name__ == '__main__':

    from parameters import options


    # run model
    sim = python_csdl_backend.Simulator(ODESystemModel(num_nodes=30,options=options))
    sim.run()
    # print partials
    sim.check_partials(compact_print=True)     
        
        
        
        
        