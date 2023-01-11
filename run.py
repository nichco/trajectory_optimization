import csdl
import numpy as np
import matplotlib.pyplot as plt
import python_csdl_backend
from odeproblemtest import ODEProblemTest
from timestep import timestep
from modopt.scipy_library import SLSQP
# from modopt.snopt_library import SNOPT
from modopt.csdl_library import CSDLProblem
from skmd import tonal
from parameters import options
from post_process import post


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
        gamma = self.declare_variable('gamma', shape=(num,))
        h = self.declare_variable('h', shape=(num,))
        e = self.declare_variable('e', shape=(num,))
        alpha = self.declare_variable('control_alpha', shape=(num,))
        cruisepower = self.declare_variable('cruisepower', shape=(num,))
        liftpower = self.declare_variable('liftpower', shape=(num,))

        # max power constraints
        self.register_output('max_cruise_power', csdl.max(cruisepower))
        self.register_output('max_lift_power', csdl.max(liftpower))
        # only for min dt case
        self.add_constraint('max_cruise_power', upper=options['max_cruise_power'], scaler=1E-6)
        self.add_constraint('max_lift_power', upper=options['max_lift_power'], scaler=1E-6)

        # final altitude constraint
        self.register_output('final_h', h[-1])
        self.add_constraint('final_h', equals=options['h_f'], scaler=0.01)

        # min altitude constraint
        self.register_output('min_h', csdl.min(h))
        self.add_constraint('min_h', lower=options['h_0'] - 0.01)

        # final velocity constraint
        self.register_output('final_v',v[-1])
        self.add_constraint('final_v',lower=options['v_f'],scaler=0.01) #0.1
        
        # pitch angle constraint
        self.register_output('theta',gamma + alpha)
        self.register_output('max_theta',csdl.max(((gamma + alpha)**2)**0.5))
        #self.add_constraint('max_theta',upper=np.deg2rad(15))
        
        # flight path angle constraints
        self.register_output('final_gamma',gamma[-1])
        self.add_constraint('final_gamma',equals=0)
        
        # acoustic constraints
        self.add(tonal(options=options,num=num), name='tonal')
        # self.add_constraint('max_spl_gl',upper=np.linspace(120,60,num),scaler=1E-2)
        # self.add_constraint('seg_ospl',upper=70,scaler=1E-2)
        
        # compute total energy
        energy = e[-1]
        self.register_output('energy',energy)
        self.print_var(energy)
       
        
        """
        # for the minimum energy objective
        self.add_design_variable('control_alpha',lower=-np.pi/2,upper=np.pi/2,scaler=5)
        self.add_design_variable('control_x',lower=0, scaler=2E-3)
        self.add_design_variable('control_z',lower=0, scaler=np.linspace(1E-3,1,num))
        self.add_design_variable('dt',lower=2.0)
        self.add_objective('energy', scaler=5E-3)
        """
        
        # for the minimum time objective
        self.add_design_variable('control_alpha',scaler=np.linspace(1,10,num))
        self.add_design_variable('control_x',lower=0, scaler=1E-2)
        self.add_design_variable('control_z',lower=0, scaler=np.linspace(1E-3,1E-2,num))
        self.add_design_variable('dt')
        
        #self.add_design_variable('control_alpha',scaler=1)
        #self.add_design_variable('control_x',lower=0, scaler=1/options['control_x_i'])
        #self.add_design_variable('control_z',lower=0, scaler=1/options['control_z_i'])
        #self.add_design_variable('dt',lower=0.5)

        self.add_objective('dt')
        




# ode problem instance
num = 30
ODEProblem = ODEProblemTest('RK4', 'time-marching', num_times=num, display='default', visualization='end')
sim = python_csdl_backend.Simulator(RunModel(options=options), analytics=0)
#sim.run()
#sim.check_partials(compact_print=True)

prob = CSDLProblem(problem_name='Trajectory Optimization', simulator=sim)
optimizer = SLSQP(prob, maxiter=10000, ftol=1E-8)
#optimizer = SNOPT(prob,Major_iterations=100,Major_optimality=1e-3,Major_feasibility=1E-3,append2file=True)
optimizer.solve()
optimizer.print_results()
# plot states from integrator
plt.show()

# post-process results and generate plots
post(sim=sim, options=options)



