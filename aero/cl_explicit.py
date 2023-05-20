import csdl
import python_csdl_backend
from aero.viscous_surrogate import sm_cl
import numpy as np

class cl_aero(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes')
    def define(self):
        n = self.parameters['num_nodes']

        alpha_w = self.declare_variable('alpha_w', shape=n)

        # custom operation insertion
        cl = csdl.custom(alpha_w, op=CLAeroExplicit(num_nodes=n))

        self.register_output('cl', cl)

class CLAeroExplicit(csdl.CustomExplicitOperation):
    def initialize(self):
        self.parameters.declare('num_nodes')
    def define(self):
        n = self.parameters['num_nodes']

        # input: alpha
        self.add_input('alpha_w', shape=n)

        # output: cl
        self.add_output('cl', shape=n)

        self.declare_derivatives('cl', 'alpha_w')

    def compute(self, inputs, outputs):
        n = self.parameters['num_nodes']

        # surrogate model
        # cl = sm_cl.predict_values(inputs['alpha_w'])
        cl = np.zeros((n))
        for i in range(n):
            a = np.array([inputs['alpha_w'][i]])
            cl[i] = sm_cl.predict_values(a)

        outputs['cl'] = 1*cl

    def compute_derivatives(self, inputs, derivatives):
        n = self.parameters['num_nodes']

        # dcl_dalpha = sm_cl.predict_derivatives(inputs['alpha_w'], 0)
        dcl_dalpha = np.zeros((n))
        for i in range(n):
            a = np.array([inputs['alpha_w'][i]])
            dcl_dalpha[i] = sm_cl.predict_derivatives(a, 0)

        derivatives['cl', 'alpha_w'] = np.diag(dcl_dalpha)





if __name__ == '__main__':
    # run model
    sim = python_csdl_backend.Simulator(cl_aero(num_nodes=10))
    sim.run()

    print(sim['cl'])

    # print partials
    sim.check_partials(step=1E-6,compact_print=True)