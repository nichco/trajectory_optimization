import csdl
import python_csdl_backend
import numpy as np
from rotors.rotor_explicit import rotorModel

class rotor(csdl.Model):
    def initialize(self):
        self.parameters.declare('name',types=str)
        self.parameters.declare('options')
        self.parameters.declare('num_nodes')
    def define(self):
        num = self.parameters['num_nodes']
        name = self.parameters['name']
        options = self.parameters['options']

        # declare necessary variables
        n = self.declare_variable(name+'n', shape=num) # revolutions per SECOND
        v_axial = self.declare_variable(name+'vAxial',shape=num)
        v_tan = self.declare_variable(name+'vTan',shape=num)
        d = options[name+'_rotor_diameter']
        rho = self.declare_variable('density', shape=num)

        # calculate advance ratio
        ja = v_axial/(n*d)
        jt = v_tan/(n*d)

        # add the explicit operation containing the surrogate model
        self.add(rotorModel(name=name,num_nodes=num), name='rotorModel')

        # declare variables
        ct = self.declare_variable(name+'ct', shape=num)
        cp = self.declare_variable(name+'cp', shape=num)

        # compute thrust and power
        thrust = ct*rho*(n**2)*(d**4)
        power = cp*rho*(n**3)*(d**5)
        torque = (cp/(2*np.pi))*(n**2)*(d**5)

        self.register_output(name+'thrust',thrust)
        self.register_output(name+'power',power)
        self.register_output(name+'torque',torque)



if __name__ == '__main__':

    options = {}
    options['cruise_rotor_diameter'] = 2 # (m)

    name = 'cruise'
    sim = python_csdl_backend.Simulator(rotor(options=options,name=name,num_nodes=10))
    sim.run()
    sim.check_partials(compact_print=True)

    thrust = sim[name+'thrust']
    power = sim[name+'power']
    torque = sim[name+'torque']

    print('thrust: ',thrust)
    print('power: ',power)
    print('torque: ',torque)