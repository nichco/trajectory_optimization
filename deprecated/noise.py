import numpy as np 
import csdl
import python_csdl_backend
from acoustics.core.barry_magliozzi_model import BarryMagliozziModel
from parameters import options



t_c_ratio      = np.array([0.3495,0.3161,0.2916,0.2727,0.2561,0.2406,0.2267,0.2142,0.2031,0.1933,0.1849,0.1775,0.1705,0.1638,0.1576,0.1520,0.1466,0.1415,0.1367,0.1324,0.1283,0.1246,
                            0.1210,0.1175,0.1140,0.1108,0.1077,0.1050,0.1024,0.0999,0.0975,0.0951,0.0929,0.0907,0.0885,0.0863,0.0839,0.0811,0.0777,0.0734,])
num_radial= len(t_c_ratio)
num_azimuthal = 1


acoustics_dict = {}
acoustics_dict['num_blades'] = 2
acoustics_dict['directivity'] = 0
acoustics_dict['mode'] = 3
acoustics_dict['hub_radius'] = 17.7 # (% of rotor radius)

x_pos = 45
y_pos = 0
z_pos = 45


class rotor_noise(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes')
        self.parameters.declare('options')
    def define(self):
        n = self.parameters['num_nodes']
        options = self.parameters['options']

        cruise_rotor_radius = options['cruise_rotor_diameter']/2
        lift_rotor_radius = options['lift_rotor_diameter']/2
        self.create_input('propeller_radius',val=cruise_rotor_radius)
        #velocity = self.declare_variable('v', shape=n)
        #a = self.declare_variable('speed_of_sound', shape=n)
        #self.register_output('M_inf',velocity/a)


        control_x = self.declare_variable('control_x', shape=(n))
        #control_z = self.declare_variable('control_z', shape=(n))

        self.register_output('omega',1*control_x)
        shape = (num_nodes,num_radial, num_azimuthal)

        # core inputs
        x = self.declare_variable('x_position',shape=(n))
        y = self.declare_variable('y_position',shape=(n))
        z = self.declare_variable('z_position',shape=(n))
        self.register_output('_x_position', csdl.expand(x, shape,'i->ijk'))
        self.register_output('_y_position', csdl.expand(y, shape,'i->ijk'))
        self.register_output('_z_position', csdl.expand(z, shape,'i->ijk'))

        # preprocess computations
        
        self.add(BarryMagliozziModel(
            acoustics_dict = acoustics_dict,
            shape=shape,
        ), name = 'barry_magliozzi_model')


if __name__ == '__main__':
    num_nodes=30
    sim = python_csdl_backend.Simulator(rotor_noise(num_nodes=num_nodes,options=options))

    sim['density'] = np.ones((num_nodes))*1.225
    sim['speed_of_sound'] = np.ones((num_nodes))*336
    sim['control_x'] = np.ones((num_nodes))*1200
    sim['x_position'] = np.ones((num_nodes))*45
    sim['y_position'] = np.ones((num_nodes))*0
    sim['z_position'] = np.ones((num_nodes))*45

    sim.run()

    BM_tonal_noise = sim['SPL_tonal_Barry_Magliozzi']
    total_tonal_noise = sim['total_tonal_noise']
    total_noise = sim['tonal_plus_broadband_noise']

    #print(BM_tonal_noise)
    #print(total_tonal_noise)
    print(total_noise)