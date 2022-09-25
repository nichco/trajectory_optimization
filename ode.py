import csdl
import numpy as np


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
        theta = self.create_input('theta', shape=n)
        q = self.create_input('q', shape=n)
        x = self.create_input('x', shape=n)
        z = self.create_input('z', shape=n)
        # inputs
        t = self.create_input('t', shape=(n))
        n = self.create_input('n', shape=(n))
        
        # constants
        g = 9.81 # (m/s^2)
        
        # forces and moments
        alpha = csdl.arctan(w/u)
            
        fax = -drag*csdl.cos(alpha) + lift*csdl.sin(alpha)
        faz = -drag*csdl.sin(alpha) - lift*csdl.cos(alpha)
        
        # system of ODE's
        du = -q*w - g*csdl.sin(theta) + (fax + fpx)/m
        dw = q*u + g*csdl.cos(theta) + (faz + fpz)/m
        dtheta = 1*q
        dq = (ma + mp)/Iyy
        dx = u*csdl.cos(theta) + w*csdl.sin(theta)
        dz = u*csdl.sin(theta) - w*csdl.cos(theta)
        
        # register outputs
        self.register_output('du', du)
        self.register_output('dw', dw)
        self.register_output('dtheta', dtheta)
        self.register_output('dq', dq)
        self.register_output('dx', dx)
        self.register_output('dz', dz)
        
        
        
        
        
        
        