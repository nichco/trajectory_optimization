import csdl
import python_csdl_backend
from aero_surrogate import sm_cl, sm_cd

class airfoil(csdl.Model):
    def initialize(self):
        self.parameters.declare('alpha')
    def define(self):
        aoa = self.parameters['alpha']

        alpha = self.create_input('alpha', val=aoa)

        # alpha = self.declare_variable('alpha')

        # custom operation insertion
        cl, cd = csdl.custom(alpha, op=AeroExplicit())

        self.register_output('cl', cl)
        self.register_output('cd', cd)

class AeroExplicit(csdl.CustomExplicitOperation):
    def initialize(self):
        pass
    def define(self):

        # input: altitude
        self.add_input('alpha', shape=(1,))

        # output: pressure and density
        self.add_output('cl', shape=(1,))
        self.add_output('cd', shape=(1,))

        self.declare_derivatives('cl', 'alpha')
        self.declare_derivatives('cd', 'alpha')

    def compute(self, inputs, outputs):

        # surrogate model
        cl = sm_cl.predict_values(inputs['alpha'])
        cd = sm_cd.predict_values(inputs['alpha'])

        outputs['cl'] = 1*cl
        outputs['cd'] = 1*cd

    def compute_derivatives(self, inputs, derivatives):

        dcl_dalpha = sm_cl.predict_derivatives(inputs['alpha'], 0)
        dcd_dalpha = sm_cd.predict_derivatives(inputs['alpha'], 0)

        derivatives['cl', 'alpha'] = dcl_dalpha
        derivatives['cd', 'alpha'] = dcd_dalpha


# run model
sim = python_csdl_backend.Simulator(airfoil(alpha=0))
sim.run()

print(sim['cl'])
print(sim['cd'])

# print partials
# sim.check_partials(compact_print=True)