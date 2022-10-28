from pitt_peters_rotor_surrogate import sm_ct, sm_cp
import csdl
import python_csdl_backend
import numpy as np

class rotorModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('name',types=str)
    def define(self):
        name = self.parameters['name']

        vAxial = self.declare_variable(name+'vAxial')
        vTan = self.declare_variable(name+'vTan')
        # custom operation insertion
        cruise_ct, cruise_cp = csdl.custom(vAxial,vTan, op=rotorExplicit(name=name))
        self.register_output(name+'ct', cruise_ct)
        self.register_output(name+'cp', cruise_cp)

class rotorExplicit(csdl.CustomExplicitOperation):
    def initialize(self):
        self.parameters.declare('name',types=str)
    def define(self):
        name = self.parameters['name']

        # input: axial and tangential freestream velocities
        self.add_input(name+'vAxial', shape=(1,))
        self.add_input(name+'vTan', shape=(1,))

        # output: thrust coefficient and power coefficient
        self.add_output(name+'ct', shape=(1,))
        self.add_output(name+'cp', shape=(1,))

        # declare derivatives
        self.declare_derivatives(name+'ct', name+'vAxial')
        self.declare_derivatives(name+'ct', name+'vTan')
        self.declare_derivatives(name+'cp', name+'vAxial')
        self.declare_derivatives(name+'cp', name+'vTan')

    def compute(self, inputs, outputs):
        name = self.parameters['name']

        # surrogate model interpolation
        point = np.array([[inputs[name+'vAxial'], inputs[name+'vTan']]]).reshape(1,2)
        ct = sm_ct.predict_values(point)
        cp = sm_cp.predict_values(point)

        # define outputs
        outputs[name+'ct'] = 1*ct
        outputs[name+'cp'] = 1*cp

    def compute_derivatives(self, inputs, derivatives):
        name = self.parameters['name']

        # compute derivatives
        point = np.array([[inputs[name+'vAxial'], inputs[name+'vTan']]]).reshape(1,2)
        dct_dvaxial = sm_ct.predict_derivatives(point, 0)
        dct_dvtan = sm_ct.predict_derivatives(point, 0)
        dcp_dvaxial = sm_cp.predict_derivatives(point, 0)
        dcp_dvtan = sm_cp.predict_derivatives(point, 0)

        # assign derivatives
        derivatives[name+'ct', name+'vAxial'] = dct_dvaxial
        derivatives[name+'ct', name+'vTan'] = dct_dvtan
        derivatives[name+'cp', name+'vAxial'] = dcp_dvaxial
        derivatives[name+'cp', name+'vTan'] = dcp_dvtan



if __name__ == '__main__':
    name = 'cruise'
    sim = python_csdl_backend.Simulator(rotorModel(name=name))
    sim.run()

    ct = sim[name+'ct']
    cp = sim[name+'cp']

    print('C_T: ',ct)
    print('C_P: ',cp)

    # print partials
    sim.check_partials(compact_print=True)