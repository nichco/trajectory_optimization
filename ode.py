import csdl
from atm_explicit import Atm


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
        # inputs
        thrust = self.create_input('thrust', shape=(n)) # thrust (0-1)
        theta = self.create_input('theta', shape=(n)) # pitch angle

        # add atmospheric model
        self.register_output('altitude', 1*z)
        self.add(Atm(alt=-1*z))
        rho = self.declare_variable('density')
        p = self.declare_variable('pressure')
        
        # constants
        g = 9.81 # (m/s^2)
        
        # angle of attack
        alpha = csdl.arctan(w/u)

        # add aerodynamic model
        
        fax = -drag*csdl.cos(alpha) + lift*csdl.sin(alpha)
        faz = -drag*csdl.sin(alpha) - lift*csdl.cos(alpha)
        
        # system of ODE's
        du = -g*csdl.sin(theta) + (fax + fpx)/m
        dw = g*csdl.cos(theta) + (faz + fpz)/m
        dx = u*csdl.cos(theta) + w*csdl.sin(theta)
        dz = u*csdl.sin(theta) - w*csdl.cos(theta)
        
        # register outputs
        self.register_output('du', du)
        self.register_output('dw', dw)
        self.register_output('dx', dx)
        self.register_output('dz', dz)
        
        
        
        
        
        
        