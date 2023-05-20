import csdl
from aero.aero import aero
from aero.aeromodel import Aero
from rotors.rotor import rotor
from motors.motor_explicit import motor
import numpy as np
import python_csdl_backend
from prop.propmodel import Prop
from atmosphere.new_atm import Atm


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
        ux = self.declare_variable('control_x', shape=(n))
        uz = self.declare_variable('control_z', shape=(n))
        ua = self.declare_variable('control_alpha', shape=(n))
        m = options['mass']
        g = 9.81
        alpha = 1*ua
        
        # add aerodynamic model
        self.add(Atm(num_nodes=n), name='atm')
        self.add(aero(num_nodes=n, options=options), name='aero')
        #self.add(Aero(num_nodes=n, wing_area=options['wing_area']), name='Aero')
        L = self.declare_variable('lift', shape=(n))
        D = self.declare_variable('drag', shape=(n))

        # rotor and motor models
        
        cname = 'cruise'
        self.register_output(cname+'vAxial', v*csdl.cos(alpha))
        self.register_output(cname+'vTan', ((v*csdl.sin(alpha))**2)**0.5)
        self.register_output(cname+'n',1*ux/60) # rotations per second for rotor model
        self.register_output(cname+'m',1*ux) # rotations per minute for motor model
        self.add(rotor(name=cname,options=options,num_nodes=n), name=cname+'rotor')
        self.add(motor(name=cname,num_nodes=n), name=cname+'motor')
        cruiseeta = self.declare_variable(cname+'eta',shape=(n))
        TC = self.declare_variable(cname+'thrust', shape=(n))
        cruisepower = self.declare_variable(cname+'power', shape=(n))
        
        """
        self.register_output('cruise_vaxial', ((v*csdl.cos(alpha))**2)**0.5)
        self.register_output('cruise_vtan',((v*csdl.sin(alpha))**2)**0.5)
        self.register_output('cruise_rpm', 1*control_x)
        self.add(Prop(name='cruise', num_nodes=n, d=options['cruise_rotor_diameter']), name='CruiseProp', 
                 promotes=['cruise_thrust', 'cruisepower', 'cruise_rpm', 'cruise_vaxial', 'cruise_vtan', 'density'])
        TC = self.declare_variable('cruise_thrust', shape=(n))
        cruisepower = self.declare_variable('cruisepower', shape=(n))

        self.register_output('cruisem', 1*control_x)
        self.add(motor(name='cruise', num_nodes=n), name='cruise_motor')
        cruiseeta = self.declare_variable('cruiseeta', shape=(n))
        """
        """
        lname = 'lift'
        self.register_output(lname+'vAxial',v*csdl.sin(alpha))
        self.register_output(lname+'vTan',v*csdl.cos(alpha))
        self.register_output(lname+'n',1*uz/60) # rotations per second for rotor model
        self.register_output(lname+'m',1*uz) # rotations per minute for motor model
        self.add(rotor(name=lname,options=options,num_nodes=n), name=lname+'rotor')
        self.add(motor(name=lname,num_nodes=n), name=lname+'motor')
        lifteta = self.declare_variable(lname+'eta',shape=(n))
        TL_s = self.declare_variable(lname+'thrust', shape=(n))
        TL = 8*TL_s
        liftpower_s = self.declare_variable(lname+'power', shape=(n))
        liftpower = 8*liftpower_s
        """

        
        self.register_output('lift_vaxial', v*csdl.sin(alpha))
        self.register_output('lift_vtan', ((v*csdl.cos(alpha))**2)**0.5)
        self.register_output('lift_rpm', 1*uz)
        self.add(Prop(name='lift', num_nodes=n, d=options['lift_rotor_diameter']), name='LiftProp', 
                 promotes=['lift_thrust', 'liftpower', 'lift_rpm', 'lift_vaxial', 'lift_vtan', 'density'])
        TL = 8*self.declare_variable('lift_thrust', shape=(n))
        liftpower = 8*self.declare_variable('liftpower', shape=(n))

        self.register_output('liftm',1*uz) # rotations per minute for motor model
        self.add(motor(name='lift',num_nodes=n), name='lift_motor')
        lifteta = self.declare_variable('lifteta',shape=(n))
        


        
        # system of ODE's
        dv = (TC/m)*csdl.cos(alpha) - (TL/m)*csdl.sin(alpha) - (D/m) - g*csdl.sin(gamma)
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

    options = {}

    # run model
    sim = python_csdl_backend.Simulator(ODESystemModel(num_nodes=30,options=options))
    sim.run()
    # print partials
    sim.check_partials(compact_print=True)     
        
        
        
        
        