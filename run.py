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
        #self.add_constraint('cruisepower', upper=options['max_cruise_power'], scaler=1E-6)
        self.add_constraint('max_lift_power', upper=options['max_lift_power'], scaler=1E-6)
        #self.add_constraint('liftpower', upper=options['max_lift_power'], scaler=1E-6)

        # final altitude constraint
        self.register_output('final_h', h[-1])
        self.add_constraint('final_h', equals=options['h_f'], scaler=1E-3)

        # min altitude constraint
        self.register_output('min_h', csdl.min(100*h)/100)
        self.add_constraint('min_h', lower=-0.01)

        # final velocity constraint
        self.register_output('final_v',v[-1])
        self.add_constraint('final_v',equals=options['v_f'],scaler=1E-2)
        
        # pitch angle constraints
        theta = self.register_output('theta', gamma + alpha)
        #dtheta = self.create_output('dtheta',shape=(num-1,), val=0)
        #for i in range(1,num):
        #    dtheta[i-1] = (((theta[i] - theta[i-1])/dt)**2)**0.5
        #self.register_output('max_dtheta',csdl.max(dtheta))
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
options['alpha_0'] = 0 # (rad)
options['h_f'] = 300 # (m)
options['v_f'] = 58 # 43 (m/s)
options['vne'] = 65 # (m/s)
options['x_lim'] = 5000 # (m)
options['theta_0'] = 0.0 # (rad)
options['gamma_f'] = 0.0 # (rad)

options['dt'] = 2.86300868

options['control_x_i'] = np.array([1102.12682829, 184.44061268, 343.09978951,1292.05537858,1297.44949729,
 1279.56875063,1211.42475592,1196.85597471,1176.63991584,1165.62468441,
 1156.8184399 ,1154.0785229 ,1155.63754313,1160.89215887,1165.75787773,
 1170.53528197,1172.14318389,1174.12242365,1175.67388567,1177.03212989,
 1178.71475611,1179.86952604,1182.80048761,1189.71184813,1192.76210608,
 1189.90506546,1171.84874995,1102.97130014, 994.89702246, 968.36637858])
options['control_z_i'] = np.array([1.09350496e+03,9.19060570e+02,1.40145995e+03,4.93983466e+02,
 2.89541639e-15,3.33779732e+01,1.40258207e+01,8.71515916e+01,
 9.99821607e+01,1.04791175e+02,9.30850071e+01,8.39650259e+01,
 3.26498850e+01,3.96773343e+00,1.57741787e+00,1.96382486e+00,
 2.12730338e+00,2.00659518e+00,1.88375993e+00,1.94179131e+00,
 2.10977038e+00,2.30250834e+00,2.09756585e+00,1.25871708e+00,
 3.46627780e-01,8.64863323e-03,2.72078697e-05,0.00000000e+00,
 6.72295197e-02,2.34358307e-01])
options['control_alpha_i'] = np.array([ 1.45076942e-01,-1.57079633e+00,-1.06766898e+00, 1.20888520e-01,
  1.39386888e-01, 1.12237265e-01, 3.20175095e-02, 3.32461297e-02,
  2.14253566e-02, 1.22345742e-02, 4.46800127e-03, 2.15306907e-03,
  4.18990757e-03,-8.48910377e-04,-3.17620705e-03,-5.53209765e-03,
 -4.55569694e-03,-4.48500450e-03,-4.66600432e-03,-4.14648147e-03,
 -5.27258261e-03,-4.97267092e-03,-3.77550455e-03,-1.57033635e-03,
  4.11636770e-03, 1.26055595e-02, 2.33319283e-02, 2.53408338e-02,
 -1.05117193e-02,-7.15975001e-02])



# ode problem instance
num = 30
ODEProblem = ODEProblemTest('RK4', 'time-marching', num_times=num, display='default', visualization='end')
sim = python_csdl_backend.Simulator(RunModel(options=options), analytics=0)
#sim.run()
#sim.check_partials(compact_print=False)
#sim.check_totals(step=1E-6)

prob = CSDLProblem(problem_name='Trajectory Optimization', simulator=sim)
optimizer = SLSQP(prob, maxiter=1000, ftol=1E-6)
#optimizer = SNOPT(prob,Major_iterations=1000,Major_optimality=1e-7,Major_feasibility=1E-7,append2file=True,Linesearch_tolerance=0.99,Hessian_frequency=10,Major_step_limit=0.1)
optimizer.solve()
optimizer.print_results()
# plot states from integrator
plt.show()

# post-process results and generate plots
post(sim=sim, options=options)


print(np.array2string(sim['control_x'],separator=','))
print(np.array2string(sim['control_z'],separator=','))
print(np.array2string(sim['control_alpha'],separator=','))
