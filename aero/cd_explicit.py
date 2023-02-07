import csdl
import python_csdl_backend
from aero.viscous_surrogate import sm_cd
import numpy as np

class cd_aero(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes')
    def define(self):
        n = self.parameters['num_nodes']

        alpha_w = self.declare_variable('alpha_w', shape=n)
        mach = self.declare_variable('mach', shape=n)

        # custom operation insertion
        cd = csdl.custom(alpha_w, mach, op=AeroExplicit(num_nodes=n))
        self.register_output('cd', cd)

class AeroExplicit(csdl.CustomExplicitOperation):
    def initialize(self):
        self.parameters.declare('num_nodes')
    def define(self):
        n = self.parameters['num_nodes']

        # input: alpha and mach number
        self.add_input('alpha_w', shape=n)
        self.add_input('mach', shape=n)

        # output: cd
        self.add_output('cd', shape=n)

        self.declare_derivatives('cd', 'alpha_w')
        self.declare_derivatives('cd', 'mach')

    def compute(self, inputs, outputs):
        n = self.parameters['num_nodes']

        # surrogate model
        # cd = sm_cd.predict_values(inputs['alpha_w'])
        cd = np.zeros((n))
        for i in range(n):
            a = np.array([inputs['alpha_w'][i]])
            mach = np.array([inputs['mach'][i]])
            point = np.array([[a,mach]]).reshape(1,2)
            cd[i] = sm_cd.predict_values(point)

        outputs['cd'] = 1*cd

    def compute_derivatives(self, inputs, derivatives):
        n = self.parameters['num_nodes']

        # dcd_dalpha = sm_cd.predict_derivatives(inputs['alpha_w'], 0)
        dcd_dalpha = np.zeros((n))
        dcd_dmach = np.zeros((n))
        for i in range(n):
            a = np.array([inputs['alpha_w'][i]])
            mach = np.array([inputs['mach'][i]])
            point = np.array([[a,mach]]).reshape(1,2)
            dcd_dalpha[i] = sm_cd.predict_derivatives(point, 0)
            dcd_dmach[i] = sm_cd.predict_derivatives(point, 1)

        derivatives['cd', 'alpha_w'] = np.diag(dcd_dalpha)
        derivatives['cd', 'mach'] = np.diag(dcd_dmach)





if __name__ == '__main__':
    # run model
    sim = python_csdl_backend.Simulator(cd_aero(num_nodes=10))
    sim.run()

    print(sim['cd'])

    # print partials
    sim.check_partials(step=1E-2,compact_print=True)