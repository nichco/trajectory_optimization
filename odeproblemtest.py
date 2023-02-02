from ozone.api import ODEProblem
from ode import ODESystemModel

# ODE problem CLASS
class ODEProblemTest(ODEProblem):
    def setup(self):
        # If dynamic == True, The parameter must have shape = (self.num_times, ... shape of parameter @ every timestep ...)
        # The ODE function will use the parameter value at timestep 't': parameter@ODEfunction[shape_p] = fullparameter[t, shape_p]
        self.add_parameter('control_alpha', dynamic=True, shape=(self.num_times))
        self.add_parameter('control_x', dynamic=True, shape=(self.num_times))
        self.add_parameter('control_z', dynamic=True, shape=(self.num_times))
        # If dynamic != True, it is a static parameter. i.e, the parameter used in the ODE is constant through time.
        # Therefore, the shape does not depend on the number of timesteps

        # inputs names correspond to respective upstream CSDL variables
        self.add_state('v', 'dv', initial_condition_name='v_0', output='v', interp_guess=[4, 60])
        self.add_state('gamma', 'dgamma', initial_condition_name='gamma_0', output='gamma', interp_guess=[0.001,0.02])
        self.add_state('h', 'dh', initial_condition_name='h_0', output='h', interp_guess=[1, 300])
        self.add_state('x', 'dx', initial_condition_name='x_0', output='x', interp_guess=[0, 4000])
        self.add_state('e', 'de', initial_condition_name='e_0', output='e', interp_guess=[0, 2103])

        self.add_times(step_vector='hvec')

        # define ODE
        self.set_ode_system(ODESystemModel)

        # export variables of interest from ode for troubleshooting
        self.set_profile_system(ODESystemModel)
        self.add_profile_output('lift')
        self.add_profile_output('drag')
        self.add_profile_output('cl')
        self.add_profile_output('cd')
        self.add_profile_output('cruisepower')
        self.add_profile_output('liftpower')
