import csdl
import python_csdl_backend
from viscous_surrogate import sm_cl, sm_cd
import numpy as np

class AeroCoef(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes')
    def define(self):
        n = self.parameters['num_nodes']

        alpha_w = self.declare_variable('alpha_w', shape=n)
        mach = self.declare_variable('mach', shape=n)

        # custom operation insertion
        cl, cd = csdl.custom(alpha_w, mach, op=AeroExplicit(num_nodes=n))

        self.register_output('cl', cl)
        self.register_output('cd', cd)

class AeroExplicit(csdl.CustomExplicitOperation):
    def initialize(self):
        self.parameters.declare('num_nodes')
    def define(self):
        n = self.parameters['num_nodes']

        # input: alpha and mach number
        self.add_input('alpha_w', shape=n)
        self.add_input('mach', shape=n)

        # output: cl and cd
        self.add_output('cl', shape=n)
        self.add_output('cd', shape=n)

        self.declare_derivatives('cl', 'alpha_w')
        self.declare_derivatives('cd', 'alpha_w')
        self.declare_derivatives('cd', 'mach')

    def compute(self, inputs, outputs):
        n = self.parameters['num_nodes']

        # surrogate model
        # cl = sm_cl.predict_values(inputs['alpha_w'])
        # cd = sm_cd.predict_values(inputs['alpha_w'])
        cl = np.zeros((n))
        cd = np.zeros((n))
        for i in range(n):
            a = np.array([inputs['alpha_w'][i]])
            mach = np.array([inputs['mach'][i]])
            point = np.array([[a,mach]]).reshape(1,2)
            cl[i] = sm_cl.predict_values(a)
            cd[i] = sm_cd.predict_values(point)

        outputs['cl'] = 1*cl
        outputs['cd'] = 1*cd

    def compute_derivatives(self, inputs, derivatives):
        n = self.parameters['num_nodes']

        # dcl_dalpha = sm_cl.predict_derivatives(inputs['alpha_w'], 0)
        # dcd_dalpha = sm_cd.predict_derivatives(inputs['alpha_w'], 0)
        dcl_dalpha = np.zeros((n))
        dcd_dalpha = np.zeros((n))
        dcd_dmach = np.zeros((n))
        for i in range(n):
            a = np.array([inputs['alpha_w'][i]])
            mach = np.array([inputs['mach'][i]])
            point = np.array([[a,mach]]).reshape(1,2)
            dcl_dalpha[i] = sm_cl.predict_derivatives(a, 0)
            dcd_dalpha[i] = sm_cd.predict_derivatives(point, 0)
            dcd_dmach[i] = sm_cd.predict_derivatives(point, 1)

        derivatives['cl', 'alpha_w'] = np.diag(dcl_dalpha)
        derivatives['cd', 'alpha_w'] = np.diag(dcd_dalpha)
        derivatives['cd', 'mach'] = np.diag(dcd_dmach)





if __name__ == '__main__':
    # run model
    sim = python_csdl_backend.Simulator(AeroCoef(num_nodes=10))
    sim.run()

    print(sim['cl'])
    print(sim['cd'])

    # print partials
    sim.check_partials(step=1E-6,compact_print=True)