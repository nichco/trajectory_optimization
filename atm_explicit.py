import csdl
import python_csdl_backend
from atm_surrogate import sm_p, sm_d


class Atm(csdl.Model):
    def initialize(self):
        # self.parameters.declare('alt')
        pass
    def define(self):
        # alt = self.parameters['alt']
        # altitude = self.create_input('altitude', val=alt)
        altitude = self.declare_variable('altitude')

        # custom operation insertion
        p, d = csdl.custom(altitude, op=AtmExplicit())

        self.register_output('pressure', p)
        self.register_output('density', d)


class AtmExplicit(csdl.CustomExplicitOperation):
    def initialize(self):
        pass
    def define(self):

        # input: altitude
        self.add_input('altitude', shape=(1,))

        # output: pressure and density
        self.add_output('pressure', shape=(1,))
        self.add_output('density', shape=(1,))

        self.declare_derivatives('pressure', 'altitude')
        self.declare_derivatives('density', 'altitude')

    def compute(self, inputs, outputs):

        # surrogate model
        pressure = sm_p.predict_values(inputs['altitude'])
        density = sm_d.predict_values(inputs['altitude'])

        outputs['pressure'] = 1*pressure
        outputs['density'] = 1*density

    def compute_derivatives(self, inputs, derivatives):

        dp_da = sm_p.predict_derivatives(inputs['altitude'], 0)
        dd_da = sm_d.predict_derivatives(inputs['altitude'], 0)

        derivatives['pressure', 'altitude'] = 1*dp_da
        derivatives['density', 'altitude'] = 1*dd_da

"""
# run model
sim = python_csdl_backend.Simulator(Atm())
sim.run()

print(sim['pressure'])
print(sim['density'])

# print partials
# sim.check_partials(compact_print=True)
"""