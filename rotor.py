import csdl
import numpy as np
from lsdo_rotor.core.BEM.BEM_model import BEMModel
import python_csdl_backend

num_nodes = 1
num_radial = 30
num_tangential = num_azimuthal = 1
thrust_vector = np.array([[1,0,0]])
thrust_origin=np.array([[8.5, 0, 5]])
reference_point = np.array([4.5, 0, 5])

class rotor(csdl.Model):
    def initialize(self):
        pass
    def define(self):
        # Inputs not changing across conditions (segments)
        self.create_input(name='propeller_radius', shape=(1, ), units='m', val=2.5)
        # self.create_input(name='chord_profile', shape=(num_radial,), units='m', val=np.linspace(0.2,0.1,num_radial))
        # self.create_input(name='twist_profile', shape=(num_radial,), units='rad', val=np.linspace(50,10,num_radial)*np.pi/180)
        pitch_cp = self.create_input(name='pitch_cp', shape=(4,), units='rad', val=np.array([8.60773973e-01,6.18472835e-01,3.76150609e-01,1.88136239e-01]))#np.linspace(35,10,4)*np.pi/180)
        chord_cp = self.create_input(name='chord_cp', shape=(2,), units='rad', val=np.array([0.3,0.1]))
        self.add_design_variable('pitch_cp', lower=5*np.pi/180,upper=60*np.pi/180)
        # Inputs changing across conditions (segments)
        # self.create_input('omega', shape=(num_nodes, 1), units='rpm/1000', val=3000)

        # self.create_input(name='u', shape=(num_nodes, 1), units='m/s', val=0)
        self.create_input(name='v', shape=(num_nodes, 1), units='m/s', val=0)
        # self.create_input(name='w', shape=(num_nodes, 1), units='m/s', val=0)
        self.create_input(name='p', shape=(num_nodes, 1), units='rad/s', val=0)
        self.create_input(name='q', shape=(num_nodes, 1), units='rad/s', val=0)
        self.create_input(name='r', shape=(num_nodes, 1), units='rad/s', val=0)
        self.create_input(name='Phi', shape=(num_nodes, 1), units='rad', val=0)
        self.create_input(name='Theta', shape=(num_nodes, 1), units='rad', val=0)
        self.create_input(name='Psi', shape=(num_nodes, 1), units='rad', val=0)
        # self.create_input(name='x', shape=(num_nodes,  1), units='m', val=0)
        self.create_input(name='y', shape=(num_nodes,  1), units='m', val=0)
        # self.create_input(name='z', shape=(num_nodes,  1), units='m', val=0)

        self.create_input(name='thrust_vector', shape=(num_nodes,3), val=np.tile(thrust_vector,(num_nodes,1)))
        self.create_input(name='thrust_origin', shape=(num_nodes,3), val=np.tile(thrust_origin,(num_nodes,1)))

        self.add(BEMModel(   
            name='propulsion',
            num_nodes=num_nodes,
            num_radial=num_radial,
            num_tangential=num_azimuthal,
            airfoil='NACA_4412',
            # thrust_vector=thrust_vector,
            # thrust_origin=thrust_origin,
            ref_pt=reference_point,
            num_blades=3,
        ),name='BEM_model')



"""
sim = python_csdl_backend.Simulator(rotor())
sim.run()

print(sim['T'])
"""