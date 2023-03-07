import csdl
import python_csdl_backend
from obs import sm_obs
import numpy as np

class obs(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes')
    def define(self):
        n = self.parameters['num_nodes']

        x = self.declare_variable('x', shape=n)

        # custom operation insertion
        obsi = csdl.custom(x, op=ObsExplicit(num_nodes=n))

        self.register_output('obsi', obsi)

class ObsExplicit(csdl.CustomExplicitOperation):
    def initialize(self):
        self.parameters.declare('num_nodes')
    def define(self):
        n = self.parameters['num_nodes']

        # input:
        self.add_input('x', shape=n)

        # output:
        self.add_output('obsi', shape=n)

        self.declare_derivatives('obsi', 'x')

    def compute(self, inputs, outputs):
        n = self.parameters['num_nodes']

        # surrogate model
        obsi = np.zeros((n))
        for i in range(n):
            xi = np.array([inputs['x'][i]])
            obsi[i] = sm_obs.predict_values(xi)

        outputs['obsi'] = 1*obsi

    def compute_derivatives(self, inputs, derivatives):
        n = self.parameters['num_nodes']

        dobsi_dxi = np.zeros((n))
        for i in range(n):
            xi = np.array([inputs['x'][i]])
            dobsi_dxi[i] = sm_obs.predict_derivatives(xi, 0)

        derivatives['obsi', 'x'] = np.diag(dobsi_dxi)


if __name__ == '__main__':
    # run model
    num = 100
    sim = python_csdl_backend.Simulator(obs(num_nodes=num))
    sim.run()
    print(sim['obsi'])

    # print partials
    sim.check_partials(step=1E-3,compact_print=True)