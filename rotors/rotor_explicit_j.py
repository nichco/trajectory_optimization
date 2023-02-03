from rotors.pitt_peters_rotor_surrogate_j import sm_ct, sm_cp
import csdl
import python_csdl_backend
import numpy as np

class rotorModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('name',types=str)
        self.parameters.declare('num_nodes')
    def define(self):
        n = self.parameters['num_nodes']
        name = self.parameters['name']

        #vAxial = self.declare_variable(name+'vAxial', shape=n)
        #vTan = self.declare_variable(name+'vTan', shape=n)
        jAxial = self.declare_variable(name+'jAxial', shape=n)
        jTan = self.declare_variable(name+'jTan', shape=n)

        # custom operation insertion
        cruise_ct, cruise_cp = csdl.custom(jAxial,jTan, op=rotorExplicit(name=name,num_nodes=n))

        self.register_output(name+'ct', cruise_ct)
        self.register_output(name+'cp', cruise_cp)

class rotorExplicit(csdl.CustomExplicitOperation):
    def initialize(self):
        self.parameters.declare('name',types=str)
        self.parameters.declare('num_nodes')
    def define(self):
        n = self.parameters['num_nodes']
        name = self.parameters['name']

        # input: axial and tangential freestream velocities
        self.add_input(name+'jAxial', shape=n)
        self.add_input(name+'jTan', shape=n)

        # output: thrust coefficient and power coefficient
        self.add_output(name+'ct', shape=n)
        self.add_output(name+'cp', shape=n)

        # declare derivatives
        self.declare_derivatives(name+'ct', name+'jAxial')
        self.declare_derivatives(name+'ct', name+'jTan')
        self.declare_derivatives(name+'cp', name+'jAxial')
        self.declare_derivatives(name+'cp', name+'jTan')

    def compute(self, inputs, outputs):
        n = self.parameters['num_nodes']
        name = self.parameters['name']

        # surrogate model interpolation
        # point = np.array([[inputs[name+'vAxial'], inputs[name+'vTan']]]).reshape(1,2)
        # ct = sm_ct.predict_values(point)
        # cp = sm_cp.predict_values(point)
        ct = np.zeros((n))
        cp = np.zeros((n))
        for i in range(n):
            point = np.array([[inputs[name+'jAxial'][i], inputs[name+'jTan'][i]]]).reshape(1,2)
            ct[i] = sm_ct.predict_values(point)
            cp[i] = sm_cp.predict_values(point)

        # define outputs
        outputs[name+'ct'] = 1*ct
        outputs[name+'cp'] = 1*cp

    def compute_derivatives(self, inputs, derivatives):
        n = self.parameters['num_nodes']
        name = self.parameters['name']
        """
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
        """
        dct_djaxial = np.zeros((n))
        dct_djtan = np.zeros((n))
        dcp_djaxial = np.zeros((n))
        dcp_djtan = np.zeros((n))
        for i in range(n):
            point = np.array([[inputs[name+'jAxial'][i], inputs[name+'jTan'][i]]]).reshape(1,2)
            dct_djaxial[i] = sm_ct.predict_derivatives(point, 0)
            dct_djtan[i] = sm_ct.predict_derivatives(point, 1)
            dcp_djaxial[i] = sm_cp.predict_derivatives(point, 0)
            dcp_djtan[i] = sm_cp.predict_derivatives(point, 1)

        derivatives[name+'ct', name+'jAxial'] = np.diag(dct_djaxial)
        derivatives[name+'ct', name+'jTan'] = np.diag(dct_djtan)
        derivatives[name+'cp', name+'jAxial'] = np.diag(dcp_djaxial)
        derivatives[name+'cp', name+'jTan'] = np.diag(dcp_djtan)



if __name__ == '__main__':
    name = 'cruise'
    sim = python_csdl_backend.Simulator(rotorModel(name=name,num_nodes=10))
    sim.run()

    ct = sim[name+'ct']
    cp = sim[name+'cp']

    print('C_T: ',ct)
    print('C_P: ',cp)

    # print partials
    sim.check_partials(compact_print=True)