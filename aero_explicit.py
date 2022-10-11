import csdl
import python_csdl_backend
from aero_surrogate import sm_cl, sm_cd

class airfoil(csdl.Model):
    def initialize(self):
        pass
    def define(self):

        alpha_w = self.declare_variable('alpha_w')

        # custom operation insertion
        cl, cd = csdl.custom(alpha_w, op=AeroExplicit())

        self.register_output('cl', cl)
        self.register_output('cd', cd)

class AeroExplicit(csdl.CustomExplicitOperation):
    def initialize(self):
        pass
    def define(self):

        # input: alpha
        self.add_input('alpha_w', shape=(1,))

        # output: pressure and density
        self.add_output('cl', shape=(1,))
        self.add_output('cd', shape=(1,))

        self.declare_derivatives('cl', 'alpha_w')
        self.declare_derivatives('cd', 'alpha_w')

    def compute(self, inputs, outputs):

        # surrogate model
        cl = sm_cl.predict_values(inputs['alpha_w'])
        cd = sm_cd.predict_values(inputs['alpha_w'])

        outputs['cl'] = 1*cl
        outputs['cd'] = 1*cd

    def compute_derivatives(self, inputs, derivatives):

        dcl_dalpha = sm_cl.predict_derivatives(inputs['alpha_w'], 0)
        dcd_dalpha = sm_cd.predict_derivatives(inputs['alpha_w'], 0)

        derivatives['cl', 'alpha_w'] = dcl_dalpha
        derivatives['cd', 'alpha_w'] = dcd_dalpha

"""
# run model
sim = python_csdl_backend.Simulator(airfoil())
sim.run()

print(sim['cl'])
print(sim['cd'])

# print partials
# sim.check_partials(compact_print=True)
"""