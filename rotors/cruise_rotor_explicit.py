from rotors.pitt_peters_rotor_surrogate_cruise import sm_ct, sm_cp
import csdl
import python_csdl_backend
import numpy as np

class cruiseRotorModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('name',types=str)
        self.parameters.declare('num_nodes')
    def define(self):
        n = self.parameters['num_nodes']
        name = self.parameters['name']

        vAxial = self.declare_variable(name+'vAxial', shape=n)
        vTan = self.declare_variable(name+'vTan', shape=n)

        # custom operation insertion
        cruise_ct, cruise_cp = csdl.custom(vAxial,vTan, op=cruiseRotorExplicit(name=name,num_nodes=n))

        self.register_output(name+'ct', cruise_ct)
        self.register_output(name+'cp', cruise_cp)

class cruiseRotorExplicit(csdl.CustomExplicitOperation):
    def initialize(self):
        self.parameters.declare('name',types=str)
        self.parameters.declare('num_nodes')
    def define(self):
        n = self.parameters['num_nodes']
        name = self.parameters['name']

        # input: axial and tangential freestream velocities
        self.add_input(name+'vAxial', shape=n)
        self.add_input(name+'vTan', shape=n)

        # output: thrust coefficient and power coefficient
        self.add_output(name+'ct', shape=n)
        self.add_output(name+'cp', shape=n)

        # declare derivatives
        self.declare_derivatives(name+'ct', name+'vAxial')
        self.declare_derivatives(name+'ct', name+'vTan')
        self.declare_derivatives(name+'cp', name+'vAxial')
        self.declare_derivatives(name+'cp', name+'vTan')

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
            point = np.array([[inputs[name+'vAxial'][i], inputs[name+'vTan'][i]]]).reshape(1,2)
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
        dct_dvaxial = np.zeros((n))
        dct_dvtan = np.zeros((n))
        dcp_dvaxial = np.zeros((n))
        dcp_dvtan = np.zeros((n))
        for i in range(n):
            point = np.array([[inputs[name+'vAxial'][i], inputs[name+'vTan'][i]]]).reshape(1,2)
            dct_dvaxial[i] = sm_ct.predict_derivatives(point, 0)
            dct_dvtan[i] = sm_ct.predict_derivatives(point, 1)
            dcp_dvaxial[i] = sm_cp.predict_derivatives(point, 0)
            dcp_dvtan[i] = sm_cp.predict_derivatives(point, 1)

        derivatives[name+'ct', name+'vAxial'] = np.diag(dct_dvaxial)
        derivatives[name+'ct', name+'vTan'] = np.diag(dct_dvtan)
        derivatives[name+'cp', name+'vAxial'] = np.diag(dcp_dvaxial)
        derivatives[name+'cp', name+'vTan'] = np.diag(dcp_dvtan)



if __name__ == '__main__':
    name = 'cruise'
    sim = python_csdl_backend.Simulator(liftRotorModel(name=name,num_nodes=10))
    sim.run()

    ct = sim[name+'ct']
    cp = sim[name+'cp']

    print('C_T: ',ct)
    print('C_P: ',cp)

    # print partials
    sim.check_partials(compact_print=True)