import csdl
from aero import aero
from prop import prop


class ODESystemModel(csdl.Model):
    def initialize(self):
        # Required every time for ODE systems or Profile Output systems
        self.parameters.declare('num_nodes')

    def define(self):
        # Required every time for ODE systems or Profile Output systems
        n = self.parameters['num_nodes']
        # states
        u = self.create_input('u', shape=n)
        w = self.create_input('w', shape=n)
        x = self.create_input('x', shape=n)
        z = self.create_input('z', shape=n)
        e = self.create_input('e', shape=n)
        # parameters are inputs
        power = self.create_input('power', shape=(n)) # thrust (0-1)
        theta = self.create_input('theta', shape=(n)) # pitch angle
        m = self.create_input('mass')
        wing_area = self.create_input('wing_area')
        # wing_set_angle = self.declare_variable('wing_set_angle')
        
        # constants
        g = 9.81 # (m/s^2)
        
        # angle of attack
        alpha = csdl.arctan(w/u)

        # velocity
        velocity = (u**2 + w**2)**0.5

        # add aerodynamic model
        self.register_output('alpha',alpha)
        self.register_output('velocity',velocity)
        self.register_output('altitude',1*z)
        self.register_output('ref_area',1*wing_area)
        self.add(aero())

        lift = self.declare_variable('lift')
        drag = self.declare_variable('drag')

        # compute load factor    
        load_factor = lift/(1000*g)
        self.register_output('load_factor',load_factor)
        
        # transform aerodynamic forces to body axis system
        fax = -drag*csdl.cos(alpha) + lift*csdl.sin(alpha)
        faz = -drag*csdl.sin(alpha) - lift*csdl.cos(alpha)

        # add propulsion model
        fpx = 1*power*10000
        fpz = 0
        
        # system of ODE's
        # du = -g*csdl.sin(theta) + (fax + fpx)/m
        # dw = g*csdl.cos(theta) + (faz + fpz)/m
        du = (fax + fpx)/m
        dw = (faz + fpz)/m
        dx = u*csdl.cos(theta) + w*csdl.sin(theta)
        dz = u*csdl.sin(theta) - w*csdl.cos(theta)
        de = 1*power
        
        # register outputs
        self.register_output('du', du)
        self.register_output('dw', dw)
        self.register_output('dx', dx)
        self.register_output('dz', dz)
        self.register_output('de', de)
        
        
        
        
        
        
        