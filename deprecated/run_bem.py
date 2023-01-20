import numpy as np 
import csdl
from csdl import Model
from csdl_om import Simulator
from lsdo_rotor.core.BEM.BEM_model import BEMModel



num_nodes = 1
num_radial = 50
num_tangential = num_azimuthal = 1
# Thrust vector is the unit normal vector w.r.t the rotor disk
thrust_vector =  np.array([[0,0,-1]])
# Thrust origin is the point at which the thrust acts (usually the center of the rotor disk)
thrust_origin =  np.array([[8.5, 5, 5]])
# Reference point is the point about which the moments due to thrust will be computed
reference_point = np.array([8.5, 0, 5])
shape = (num_nodes,num_radial,num_tangential)

class RunModel(Model):
    def initialize(self):
        self.parameters.declare('u')
        self.parameters.declare('v')
        self.parameters.declare('n')
    def define(self):
        u = self.parameters['u']
        v = self.parameters['v']
        n = self.parameters['n']
        # Inputs not changing across conditions (segments)
        self.create_input(name='propeller_radius', shape=(1, ), units='m', val=1)
        self.create_input(name='chord_profile', shape=(num_radial,), units='m', val=np.linspace(0.2,0.1,num_radial))
        self.create_input(name='twist_profile', shape=(num_radial,), units='rad', val=np.linspace(80,10,num_radial)*np.pi/180)
        # pitch_cp = self.create_input(name='pitch_cp', shape=(4,), units='rad', val=np.linspace(80,10,4)*np.pi/180) #np.array([8.60773973e-01,6.18472835e-01,3.76150609e-01,1.88136239e-01]))#np.linspace(35,10,4)*np.pi/180)
        # chord_cp = self.create_input(name='chord_cp', shape=(2,), units='rad', val=np.array([0.35,0.14]))
        # self.add_design_variable('pitch_cp', lower=5*np.pi/180,upper=60*np.pi/180)
        
        # Inputs changing across conditions (segments), 
        #   - If the quantities are scalars, they will be expanded into shape (num_nodes,1)
        #   - If the quantities are vectors (numpy arrays), they must be specified s.t. they have shape (num_nodes,1)
        self.create_input('omega', shape=(num_nodes, 1), units='rpm', val=n)

        self.create_input(name='u', shape=(num_nodes, 1), units='m/s', val=0)
        self.create_input(name='v', shape=(num_nodes, 1), units='m/s', val=v)
        self.create_input(name='w', shape=(num_nodes, 1), units='m/s', val=u)

        self.create_input(name='p', shape=(num_nodes, 1), units='rad/s', val=0)
        self.create_input(name='q', shape=(num_nodes, 1), units='rad/s', val=0)
        self.create_input(name='r', shape=(num_nodes, 1), units='rad/s', val=0)

        self.create_input(name='Phi', shape=(num_nodes, 1), units='rad', val=0)
        self.create_input(name='Theta', shape=(num_nodes, 1), units='rad', val=0)
        self.create_input(name='Psi', shape=(num_nodes, 1), units='rad', val=0)

        self.create_input(name='x', shape=(num_nodes,  1), units='m', val=0)
        self.create_input(name='y', shape=(num_nodes,  1), units='m', val=0)
        self.create_input(name='z', shape=(num_nodes,  1), units='m', val=100)


        self.add(BEMModel(   
            name='BEM_instance_1',
            num_nodes=num_nodes,
            num_radial=num_radial,
            num_tangential=num_azimuthal,
            airfoil='NACA_4412',
            thrust_vector=thrust_vector,
            thrust_origin=thrust_origin,
            ref_pt=reference_point,
            num_blades=4,
            chord_b_spline=False,
            pitch_b_spline=False,
            normalized_hub_radius=0.2,
        ),name='BEM_model_1')


sim = Simulator(RunModel(u=50,v=0,n=1))
sim.run()

print('Thrust: ',sim['T'])
print('C_T: ',sim['C_T'])
print('C_P: ', sim['C_P'])
print('J', sim['J'])

"""
cparr = np.zeros((9,9))
ctarr = np.zeros((9,9))
ii = 0
for i in range(-100,101,25):
    jj = 0
    for j in range (-100,101,25):
        sim = Simulator(RunModel(u=i,v=j))
        sim.run()
        ctarr[ii,jj] = sim['C_T']
        cparr[ii,jj] = sim['C_P']
        jj +=1
    ii += 1

print(ctarr)
print(cparr)
"""