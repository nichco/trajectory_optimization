import csdl
from aero import aero
from rotor import rotor


class ODESystemModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes')
        self.parameters.declare('options')

    def define(self):
        # Required every time for ODE systems or Profile Output systems
        n = self.parameters['num_nodes']
        options = self.parameters['options']
        
        # states
        u = self.create_input('u', shape=n)
        w = self.create_input('w', shape=n)
        x = self.create_input('x', shape=n)
        z = self.create_input('z', shape=n)
        e = self.create_input('e', shape=n)
        # parameters are inputs
        # control_x = self.declare_variable('control_x', shape=(n))
        control_x = self.declare_variable('control_x', shape=(n))
        control_z = self.declare_variable('control_z', shape=(n))
        theta = self.declare_variable('control_theta', shape=(n))
        m = options['mass']
        num_lift_rotors = options['num_lift_rotors']
        g = options['gravity']
        
        # compute angle of attack
        alpha = csdl.arctan(w/u)
        self.register_output('alpha',alpha)

        # compute velocity
        velocity = (u**2 + w**2)**0.5
        self.register_output('velocity',velocity)

        # add aerodynamic model
        self.register_output('altitude',1*z)
        # self.register_output('ref_area',1*wing_area)
        self.add(aero(options=options), name='aero')
        # define outputs from aerodynamic model
        lift = self.declare_variable('lift')
        drag = self.declare_variable('drag')
        
        # transform aerodynamic forces to body axis system
        fax = -drag*csdl.cos(alpha) + lift*csdl.sin(alpha)
        faz = -drag*csdl.sin(alpha) - lift*csdl.cos(alpha)

        #region rotor models
        # cruise rotor model
        cname = 'cruise'
        self.register_output(cname+'vAxial',1*u)
        self.register_output(cname+'vTan',1*w)
        self.register_output(cname+'n',1*control_x/60) # rotations per second
        self.add(rotor(name=cname,options=options), name=cname+'rotor')
        cruisethrust = self.declare_variable(cname+'thrust')
        cruisepower = self.declare_variable(cname+'power')
        # lift rotor model
        lname = 'lift'
        self.register_output(lname+'vAxial',-1*w)
        self.register_output(lname+'vTan',1*u)
        self.register_output(lname+'n',1*control_z/60) # rotations per second
        self.add(rotor(name=lname,options=options), name=lname+'rotor')
        liftthrust = self.declare_variable(lname+'thrust')
        liftpower = self.declare_variable(lname+'power')
        #endregion


        # summations
        # fpx = propeller_efficiency*power*max_power
        # fpz = 0
        fpx = 1*cruisethrust
        fpz = -1*liftthrust*num_lift_rotors
        power = cruisepower + num_lift_rotors*liftpower
        
        # system of ODE's
        du = -g*csdl.sin(theta) + (fax + fpx)/m
        dw = g*csdl.cos(theta) + (faz + fpz)/m
        dx = u*csdl.cos(theta) + w*csdl.sin(theta)
        dz = u*csdl.sin(theta) - w*csdl.cos(theta)
        de = 0.0001*power
        
        # register outputs
        self.register_output('du', du)
        self.register_output('dw', dw)
        self.register_output('dx', dx)
        self.register_output('dz', dz)
        self.register_output('de', de)

        
        
        
        
        
        
        