import csdl
import numpy as np
import matplotlib.pyplot as plt
import python_csdl_backend
from odeproblemtest import ODEProblemTest
from timestep import timestep
from modopt.scipy_library import SLSQP
#from modopt.snopt_library import SNOPT
from modopt.csdl_library import CSDLProblem
from skmd import tonal
from parameters_time import options
from post_process import post

"""
run file for min time trajectories
"""

class RunModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('options')

    def define(self):
        options = self.parameters['options']
        self.create_input('dt',options['dt'])
        self.add(timestep(num=num), name='timestep') # add the time vector to the model
        
        # add dynamic inputs to the csdl model
        self.create_input('control_x',options['control_x_i'])
        self.create_input('control_z',options['control_z_i'])
        self.create_input('control_alpha',options['control_alpha_i'])
        # initial conditions for states
        self.create_input('v_0', options['v_0'])
        self.create_input('gamma_0', options['gamma_0'])
        self.create_input('h_0', options['h_0'])
        self.create_input('x_0', options['x_0'])
        self.create_input('e_0', 0)

        # create model containing the integrator
        optionsdict = {'options': options}
        self.add(ODEProblem.create_solver_model(ODE_parameters=optionsdict, profile_parameters=optionsdict), 'subgroup')

        # declare variables from integrator
        v = self.declare_variable('v', shape=(num,))
        x = self.declare_variable('x', shape=(num,))
        gamma = self.declare_variable('gamma', shape=(num,))
        h = self.declare_variable('h', shape=(num,))
        e = self.declare_variable('e', shape=(num,))
        alpha = self.declare_variable('control_alpha', shape=(num,))
        cruisepower = self.declare_variable('cruisepower', shape=(num,))
        liftpower = self.declare_variable('liftpower', shape=(num,))
        control_x = self.declare_variable('control_x',shape=(num,))
        control_z = self.declare_variable('control_z',shape=(num,))
        control_alpha = self.declare_variable('control_alpha',shape=(num,))
        dv = self.declare_variable('dv',shape=(num,))
        dt = self.declare_variable('dt')
        dgamma = self.declare_variable('dgamma',shape=(num,))

        # max power constraints
        self.register_output('max_cruise_power', csdl.max(cruisepower))
        self.register_output('max_lift_power', csdl.max(liftpower))
        self.add_constraint('max_cruise_power', upper=options['max_cruise_power'], scaler=1E-6)
        self.add_constraint('max_lift_power', upper=options['max_lift_power'], scaler=1E-6)

        # final altitude constraint
        self.register_output('final_h', h[-1])
        self.add_constraint('final_h', equals=options['h_f'], scaler=1E-2)

        # min altitude constraint
        self.register_output('min_h', csdl.min(h))
        self.add_constraint('min_h', lower=options['min_h'])

        # final velocity constraint
        self.register_output('final_v',v[-1])
        self.add_constraint('final_v',equals=options['v_f'],scaler=1E-2)
        
        # pitch angle constraints
        theta = gamma + alpha
        dtheta = self.create_output('dtheta',shape=(num-1,), val=0)
        for i in range(1,num):
            dtheta[i-1] = (((theta[i] - theta[i-1])/dt)**2)**0.5
        self.register_output('max_dtheta',csdl.max(dtheta))
        self.register_output('theta',theta)
        self.register_output('max_theta',csdl.max((theta**2)**0.5))
        self.add_constraint('max_theta',upper=np.deg2rad(20))
        #self.register_output('initial_theta',theta[0])
        #self.add_constraint('initial_theta',equals=options['theta_0'])
        self.add_constraint('max_dtheta',upper=np.deg2rad(15))
        
        # flight path angle constraints
        self.register_output('final_gamma',gamma[-1])
        self.register_output('final_dgamma',dgamma[-1])
        self.add_constraint('final_gamma',equals=options['gamma_f'])
        self.add_constraint('final_dgamma',equals=0.0)
        
        # acceleration constraints
        self.register_output('max_g',csdl.max(((dv**2)**0.5)/options['gravity']))
        self.register_output('final_dv',dv[-1])
        self.add_constraint('max_g',upper=options['max_g'])
        self.add_constraint('final_dv',equals=0.0)
        
        # acoustic constraints
        self.add(tonal(options=options,num=num), name='tonal')
        # self.add_constraint('max_spl_gl',upper=np.linspace(120,60,num),scaler=1E-2)
        # self.add_constraint('seg_ospl',upper=70,scaler=1E-2)
        
        # compute total energy
        energy = e[-1]
        self.register_output('energy',energy)
        self.print_var(dt)
        
        # for the minimum time objective
        self.add_design_variable('control_alpha',lower=-np.pi/2,upper=np.pi/2,scaler=4)
        self.add_design_variable('control_x',lower=0, scaler=1E-3)
        self.add_design_variable('control_z',lower=0, scaler=1E-3)
        self.add_design_variable('dt',lower=1.0,scaler=1E-1)
        self.add_objective('dt')
        




# ode problem instance
num = 40
ODEProblem = ODEProblemTest('RK4', 'time-marching', num_times=num, display='default', visualization='end')
sim = python_csdl_backend.Simulator(RunModel(options=options), analytics=0)
#sim.run()
#sim.check_partials(compact_print=False)
#sim.check_totals(step=1E-6)

prob = CSDLProblem(problem_name='Trajectory Optimization', simulator=sim)
optimizer = SLSQP(prob, maxiter=1000, ftol=1E-3)
#optimizer = SNOPT(prob,Major_iterations=2000,
#                    Major_optimality=1e-3,
#                    Major_feasibility=1E-2,
#                    append2file=True,
#                    Linesearch_tolerance=0.99,
#                    Hessian_frequency=10,
#                    Major_step_limit=0.02
#                    )

optimizer.solve()
optimizer.print_results()
# plot states from integrator
plt.show()

# post-process results and generate plots
post(sim=sim, options=options)

print(np.array2string(sim['control_x'],separator=','))
print(np.array2string(sim['control_z'],separator=','))
print(np.array2string(sim['control_alpha'],separator=','))


