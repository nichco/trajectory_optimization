import csdl
import numpy as np
import matplotlib.pyplot as plt
import python_csdl_backend
from odeproblemtest import ODEProblemTest
from modopt.scipy_library import SLSQP
#from modopt.snopt_library import SNOPT
from modopt.csdl_library import CSDLProblem
from post_process import post
import matplotlib.pyplot as plt
plt.rcParams.update(plt.rcParamsDefault)

"""
run file for min energy trajectories
"""

class RunModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('options')

    def define(self):
        options = self.parameters['options']
        dt = self.create_input('dt',options['dt'])
        h_vec = csdl.expand(dt, num-1)
        self.register_output('hvec', h_vec)
        
        # add dynamic inputs to the csdl model
        self.create_input('control_x',options['control_x_i'])
        self.create_input('control_z',options['control_z_i'])
        self.create_input('control_alpha',options['control_alpha_i'])
        # initial conditions for states
        self.create_input('v_0', 0.1)
        self.create_input('gamma_0', 0)
        self.create_input('h_0', 0)
        self.create_input('x_0', 0)
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
        self.register_output('max_cruise_power', csdl.max(10*cruisepower)/10)
        self.register_output('max_lift_power', csdl.max(10*liftpower)/10)
        self.add_constraint('max_cruise_power', upper=options['max_cruise_power'], scaler=1E-6)
        self.add_constraint('cruisepower', upper=options['max_cruise_power'], scaler=1E-6)
        self.add_constraint('max_lift_power', upper=options['max_lift_power'], scaler=1E-6)
        self.add_constraint('liftpower', upper=options['max_lift_power'], scaler=1E-6)

        # final altitude constraint
        self.register_output('final_h', h[-1])
        self.add_constraint('final_h', equals=options['h_f'], scaler=1E-3)

        # min altitude constraint
        self.register_output('min_h', csdl.min(100*h)/100)
        self.add_constraint('min_h', lower=options['min_h'])

        # final velocity constraint
        self.register_output('final_v',v[-1])
        self.add_constraint('final_v',equals=options['v_f'],scaler=1E-2)
        
        # pitch angle constraints
        #theta = gamma + alpha
        #dtheta = self.create_output('dtheta',shape=(num-1,), val=0)
        #for i in range(1,num):
        #    dtheta[i-1] = (((theta[i] - theta[i-1])/dt)**2)**0.5
        #self.register_output('max_dtheta',csdl.max(dtheta))
        #self.register_output('theta',theta)
        #self.register_output('max_theta',csdl.max((theta**2)**0.5))
        #self.add_constraint('max_theta',upper=np.deg2rad(20))
        #self.register_output('initial_theta',theta[0])
        #self.add_constraint('initial_theta',equals=options['theta_0'])
        #self.add_constraint('max_dtheta',upper=np.deg2rad(15))
        
        # flight path angle constraints
        #self.register_output('final_gamma',gamma[-1])
        #self.register_output('final_dgamma',dgamma[-1])
        #self.add_constraint('final_gamma',equals=options['gamma_f'])
        #self.add_constraint('final_dgamma',equals=0.0)
        
        # acceleration constraints
        #self.register_output('max_g',csdl.max(((dv**2)**0.5)/options['gravity']))
        #self.register_output('final_dv',dv[-1])
        #self.add_constraint('max_g',upper=options['max_g'])
        #self.add_constraint('final_dv',equals=0.0)
        
        # compute total energy
        energy = e[-1]
        self.register_output('energy',energy)
        self.print_var(energy)
       
        
        
        # for the minimum energy objective
        self.add_design_variable('control_alpha',lower=-np.pi/2,upper=np.pi/2,scaler=4)
        self.add_design_variable('control_x',lower=0, scaler=1E-3)
        self.add_design_variable('control_z',lower=0, scaler=1E-3)
        self.add_design_variable('dt',lower=2.0,scaler=1E-1)
        self.add_objective('energy', scaler=1E-4)




options = {}
# aircraft data
options['mass'] = 3000 # (kg)
options['wing_area'] = 19.6 # (m^2)
options['max_cruise_power'] = 468300 # (w)
options['max_lift_power'] = 133652 # 103652 (w)
options['cruise_rotor_diameter'] = 2.6 # (m)
options['lift_rotor_diameter'] = 2.4 # (m)
options['num_lift_rotors'] = 8
options['num_cruise_blades'] = 3
options['num_lift_blades'] = 2
options['energy_scale'] = 0.0001 # scale energy for plotting

# mission parameters
options['gravity'] = 9.81 # (m/s^2)
options['v_0'] = 0.625 # 4 (m/s)
options['min_h'] = -0.1 # (m)
options['alpha_0'] = 0 # (rad)
options['h_f'] = 300 # (m)
options['v_f'] = 58 # 43 (m/s)
options['vne'] = 65 # (m/s)
options['x_lim'] = 5000 # (m)
options['theta_0'] = 0.0 # (rad)
options['gamma_f'] = 0.0 # (rad)
options['max_g'] = 0.5 # (g)

options['dt'] = 2.15999432

options['control_x_i'] = np.array([1478.49611216,1480.98178811,1529.61277261,1573.22831274,1605.33023483,
 1630.98581331,1325.68386461,1287.46910033,1339.86743696,1263.6562584 ,
 1251.32535487,1241.39490916,1212.17821459,1204.65166484,1199.24128993,
 1186.5037763 ,1190.63105459,1193.85537146,1195.69973551,1196.65021426,
 1199.04350553,1200.86596124,1201.85349357,1202.13528782,1202.52075349,
 1203.72357223,1205.51812862,1207.28826333,1208.69326616,1209.64616944,
 1209.92608225,1208.74462395,1204.64875896,1195.3825217 ,1178.85084849,
 1149.08723753,1106.09261556,1024.90212253,1037.64371144, 665.06722568])
options['control_z_i'] = np.array([1.12996275e+03,1.03291990e+03,1.10774032e+03,7.87463530e+02,
 7.38730531e+02,4.98149648e+02,9.42650213e+01,9.09921098e-14,
 1.03100208e+01,5.81990551e-01,1.00975439e-03,1.82794555e-03,
 1.99846882e-04,4.84163052e-04,4.99547738e-04,4.22227666e-04,
 5.72542284e-04,5.28382585e-04,6.57981121e-04,6.30165102e-04,
 6.65704540e-04,6.72547897e-04,6.78140703e-04,6.78543610e-04,
 6.77427651e-04,6.73575235e-04,6.72091758e-04,6.70816729e-04,
 6.61888690e-04,6.42643649e-04,6.17300104e-04,5.90248487e-04,
 5.63600334e-04,5.37170528e-04,5.04523290e-04,4.80961544e-04,
 4.22227264e-04,4.69403469e-04,5.58653981e-04,0.00000000e+00])
options['control_alpha_i'] = np.array([ 2.00489587e-19,-1.38948540e+00,-4.92507868e-01, 1.21928731e-01,
  1.60088633e-01, 1.67457851e-01, 1.06928339e-01, 8.45766132e-02,
  6.63405209e-02, 6.24369994e-02, 2.96994876e-02, 4.77539534e-02,
  1.58138088e-02, 1.69457624e-02, 1.57000891e-02, 7.65332356e-03,
  3.86478765e-03, 4.24245210e-04, 4.71990672e-03,-1.54203055e-03,
 -6.05797343e-03,-4.02878599e-03,-3.63357340e-03,-3.68309723e-03,
 -4.50940955e-03,-5.88538858e-03,-5.57637775e-03,-3.51755127e-03,
 -1.69293155e-03,-9.49276183e-04,-3.49339094e-04, 1.36294799e-03,
  4.75339048e-03, 8.62854176e-03, 1.13839880e-02, 1.61076942e-02,
  2.12016572e-02, 3.06008921e-02,-2.59336189e-02, 3.65392444e-02])



# ode problem instance
num = 40
ODEProblem = ODEProblemTest('RK4', 'time-marching', num_times=num, display='default', visualization='end')
sim = python_csdl_backend.Simulator(RunModel(options=options), analytics=0)
#sim.run()
#sim.check_partials(compact_print=False)
#sim.check_totals(step=1E-6)

prob = CSDLProblem(problem_name='Trajectory Optimization', simulator=sim)
optimizer = SLSQP(prob, maxiter=1000, ftol=1E-4)
#optimizer = SNOPT(prob,Major_iterations=1000,Major_optimality=1e-7,Major_feasibility=1E-7,append2file=True,Linesearch_tolerance=0.99,Hessian_frequency=10,Major_step_limit=0.1)
optimizer.solve()
optimizer.print_results()
# plot states from integrator
plt.show()

# post-process results and generate plots
post(sim=sim, options=options)


print(np.array2string(sim['e']/options['energy_scale'],separator=','))
print(np.array2string(sim['max_spl_gl'].flatten(),separator=','))
