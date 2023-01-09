import csdl
import python_csdl_backend
from atmosphere.atm_surrogate import sm_p, sm_d
import numpy as np

class Atm(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes')
    def define(self):
        n = self.parameters['num_nodes']
        
        h = self.declare_variable('h', shape=n)

        # custom operation insertion
        p, d = csdl.custom(h, op=AtmExplicit(num_nodes=n))

        self.register_output('pressure', p)
        self.register_output('density', d)


class AtmExplicit(csdl.CustomExplicitOperation):
    def initialize(self):
        self.parameters.declare('num_nodes')
    def define(self):
        n = self.parameters['num_nodes']

        # input: altitude
        self.add_input('h', shape=n)

        # output: pressure and density
        self.add_output('pressure', shape=n)
        self.add_output('density', shape=n)

        self.declare_derivatives('pressure', 'h')
        self.declare_derivatives('density', 'h')

    def compute(self, inputs, outputs):
        n = self.parameters['num_nodes']

        # surrogate model
        # pressure = sm_p.predict_values(inputs['altitude'])
        # density = sm_d.predict_values(inputs['altitude'])
        pressure = np.zeros((n))
        density = np.zeros((n))
        for i in range(n):
            a = np.array([inputs['h'][i]])
            pressure[i] = sm_p.predict_values(a)
            density[i] = sm_d.predict_values(a)

        outputs['pressure'] = 1*pressure
        outputs['density'] = 1*density

    def compute_derivatives(self, inputs, derivatives):
        n = self.parameters['num_nodes']

        #dp_da = sm_p.predict_derivatives(inputs['altitude'], 0)
        #dd_da = sm_d.predict_derivatives(inputs['altitude'], 0)
        #derivatives['pressure', 'altitude'] = 1*dp_da
        #derivatives['density', 'altitude'] = 1*dd_da
        dp_da = np.zeros((n))
        dd_da = np.zeros((n))
        for i in range(n):
            a = np.array([inputs['h'][i]])
            dp_da[i] = sm_p.predict_derivatives(a, 0)
            dd_da[i] = sm_d.predict_derivatives(a, 0)

        derivatives['pressure', 'h'] = np.diag(dp_da)
        derivatives['density', 'h'] = np.diag(dd_da)



if __name__ == '__main__':
    # run model
    sim = python_csdl_backend.Simulator(Atm(num_nodes=10))
    sim['h'] = 4000
    sim.run()

    print(sim['pressure'])
    print(sim['density'])

    # print partials
    sim.check_partials(step=1,compact_print=True)