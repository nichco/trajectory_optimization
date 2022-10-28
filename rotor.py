import csdl
import python_csdl_backend
import numpy as np
from rotor_explicit import rotorModel

class rotor(csdl.Model):
    def initialize(self):
        self.parameters.declare('name',types=str)
    def define(self):
        name = self.parameters['name']

        # add the explicit operation containing the surrogate model
        self.add(rotorModel(name=name))

        # declare variables from rotorModel
        ct = self.declare_variable(name+'ct')
        cp = self.declare_variable(name+'cp')

        # declare necessary variables
        n = self.declare_variable(name+'n') # revolutions per SECOND
        d = self.declare_variable(name+'d')
        rho = self.declare_variable('density')

        # compute thrust and power
        thrust = ct*rho*(n**2)*(d**4)
        power = cp*rho*(n**3)*(d**5)

        self.register_output(name+'thrust',thrust)
        self.register_output(name+'power',power)



if __name__ == '__main__':
    name = 'cruise'
    sim = python_csdl_backend.Simulator(rotor(name=name))
    sim.run()

    thrust = sim[name+'thrust']
    power = sim[name+'power']

    print('thrust: ',thrust)
    print('power: ',power)