from ozone.api import ODEProblem
from ode import ODESystemModel

# ODE problem CLASS
class ODEProblemTest(ODEProblem):
    def setup(self):
        # If dynamic == True, The parameter must have shape = (self.num_times, ... shape of parameter @ every timestep ...)
        # The ODE function will use the parameter value at timestep 't': parameter@ODEfunction[shape_p] = fullparameter[t, shape_p]
        self.add_parameter('thrust', dynamic=True, shape=(self.num_times))
        self.add_parameter('theta', dynamic=True, shape=(self.num_times))
        # If dynamic != True, it is a static parameter. i.e, the parameter used in the ODE is constant through time.
        # Therefore, the shape does not depend on the number of timesteps
        self.add_parameter('mass')

        # Inputs names correspond to respective upstream CSDL variables
        self.add_state('u', 'du', initial_condition_name='u_0', output='u')
        self.add_state('w', 'dw', initial_condition_name='w_0', output='w')
        self.add_state('x', 'dx', initial_condition_name='x_0', output='x')
        self.add_state('z', 'dz', initial_condition_name='z_0', output='z')

        self.add_times(step_vector='h')

        # Define ODE
        self.set_ode_system(ODESystemModel)