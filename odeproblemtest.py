from ozone.api import ODEProblem
from ode import ODESystemModel

# ODE problem CLASS
class ODEProblemTest(ODEProblem):
    def setup(self):
        # If dynamic == True, The parameter must have shape = (self.num_times, ... shape of parameter @ every timestep ...)
        # The ODE function will use the parameter value at timestep 't': parameter@ODEfunction[shape_p] = fullparameter[t, shape_p]
        self.add_parameter('power', dynamic=True, shape=(self.num_times))
        self.add_parameter('theta', dynamic=True, shape=(self.num_times))
        # If dynamic != True, it is a static parameter. i.e, the parameter used in the ODE is constant through time.
        # Therefore, the shape does not depend on the number of timesteps
        self.add_parameter('mass')
        self.add_parameter('wing_area')
        self.add_parameter('wing_set_angle')

        # inputs names correspond to respective upstream CSDL variables
        self.add_state('u', 'du', initial_condition_name='u_0', output='u')
        self.add_state('w', 'dw', initial_condition_name='w_0', output='w')
        self.add_state('x', 'dx', initial_condition_name='x_0', output='x')
        self.add_state('z', 'dz', initial_condition_name='z_0', output='z')
        self.add_state('e', 'de', initial_condition_name='e_0', output='e')

        self.add_times(step_vector='h')

        # define ODE
        self.set_ode_system(ODESystemModel)

        # export variables of interest from ode for troubleshooting
        self.set_profile_system(ODESystemModel)
        self.add_profile_output('lift')
        self.add_profile_output('drag')
        self.add_profile_output('alpha')
        self.add_profile_output('cl')
        self.add_profile_output('cd')
        self.add_profile_output('load_factor')
