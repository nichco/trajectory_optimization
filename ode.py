import csdl
from aero import aero
from rotor import rotor


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
        power = self.declare_variable('interp', shape=(n)) # thrust (0-1)
        theta = self.declare_variable('theta', shape=(n)) # pitch angle
        m = self.declare_variable('mass')
        wing_area = self.declare_variable('wing_area')
        max_power = self.declare_variable('max_power')
        max_rpm = self.declare_variable('max_rpm')
        propeller_efficiency = self.declare_variable('propeller_efficiency')
        g = self.declare_variable('gravity')
        
        # compute angle of attack
        alpha = csdl.arctan(w/u)

        # compute velocity
        velocity = (u**2 + w**2)**0.5

        # add aerodynamic model
        self.register_output('alpha',alpha)
        self.register_output('velocity',velocity)
        self.register_output('altitude',1*z)
        self.register_output('ref_area',1*wing_area)
        self.add(aero())
        # define outputs from aero model
        lift = self.declare_variable('lift')
        drag = self.declare_variable('drag')
        
        # transform aerodynamic forces to body axis system
        fax = -drag*csdl.cos(alpha) + lift*csdl.sin(alpha)
        faz = -drag*csdl.sin(alpha) - lift*csdl.cos(alpha)

        # compute thrust
        rpm = power*max_rpm
        self.register_output('omega',rpm)

        fpx = propeller_efficiency*power*max_power
        fpz = 0
        
        # system of ODE's
        du = -g*csdl.sin(theta) + (fax + fpx)/m
        dw = g*csdl.cos(theta) + (faz + fpz)/m
        dx = u*csdl.cos(theta) + w*csdl.sin(theta)
        dz = u*csdl.sin(theta) - w*csdl.cos(theta)
        de = 1*power
        
        # register outputs
        self.register_output('du', du)
        self.register_output('dw', dw)
        self.register_output('dx', dx)
        self.register_output('dz', dz)
        self.register_output('de', de)
        
        
        
        
        
        
        