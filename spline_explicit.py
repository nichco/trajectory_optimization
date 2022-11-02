import csdl
import python_csdl_backend
import numpy as np
from smt.surrogate_models import RMTB, RBF
import matplotlib.pyplot as plt
from modopt.scipy_library import SLSQP
from modopt.snopt_library import SNOPT
from modopt.csdl_library import CSDLProblem

class spline(csdl.Model):
    def initialize(self):
        self.parameters.declare('name',types=str)
        self.parameters.declare('N') # number of spline control points
        self.parameters.declare('num_nodes') # number of ode timesteps
        self.parameters.declare('dt') # timestep

    def define(self):
        name = self.parameters['name']
        N = self.parameters['N']
        num_nodes = self.parameters['num_nodes']
        dt = self.parameters['dt']

        # input sparse control point vector
        control = self.declare_variable('control_'+name, shape=(N,))

        # custom operation insertion
        interp = csdl.custom(control, op=SplineExplicit(name=name,N=N,num_nodes=num_nodes,dt=dt))

        # output interpolated spline vector
        self.register_output('interp_'+name, interp)

class SplineExplicit(csdl.CustomExplicitOperation):
    def initialize(self):
        self.parameters.declare('name',types=str)
        self.parameters.declare('N') # number of spline control points
        self.parameters.declare('num_nodes') # number of ode timesteps
        self.parameters.declare('dt') # timestep

    def define(self):
        name = self.parameters['name']
        N = self.parameters['N']
        num_nodes = self.parameters['num_nodes']
        dt = self.parameters['dt']

        # input sparse control point vector
        self.add_input('control_'+name, shape=(N,))

        # output interpolated spline vector
        self.add_output('interp_'+name, shape=(num_nodes,))

        # declare derivatives
        self.declare_derivatives('interp_'+name, 'control_'+name)

    def compute(self, inputs, outputs):
        name = self.parameters['name']
        N = self.parameters['N']
        num_nodes = self.parameters['num_nodes']
        dt = self.parameters['dt']

        # create spline surrogate model
        xt = np.linspace(0,num_nodes*dt,N)
        yt = inputs['control_'+name]

        xlimits = np.array([[0.0, num_nodes*dt]])

        sm = RBF(d0=70,print_global=False,print_solver=False,)
        """
        sm = RMTB(
            xlimits=xlimits,
            order=3,
            num_ctrl_pts=N,
            energy_weight=1e-15,
            regularization_weight=0.0,
            print_global=False,
            print_solver=False,
            derivative_solver='lu')
        """
        sm.set_training_values(xt, yt)
        sm.train()
        self.sm = sm

        # vector for spline interpolation
        xnew = np.arange(0, num_nodes*dt, dt)

        # interpolate spline
        ynew = sm.predict_values(xnew)

        # assign interpolated output vector
        outputs['interp_'+name] = ynew

    def compute_derivatives(self, inputs, derivatives):
        name = self.parameters['name']
        N = self.parameters['N']
        num_nodes = self.parameters['num_nodes']
        dt = self.parameters['dt']

        xnew = np.arange(0, num_nodes*dt, dt)
        yder_dict = self.sm.predict_output_derivatives(xnew)

        array = np.array(yder_dict[None])
        # self.print_var(array)

        derivatives['interp_'+name, 'control_'+name] = array


class test(csdl.Model):

    def define(self):
        dt = 0.5
        num=100
        N = 5
        control_x = np.ones((N))*100
        self.create_input('control_x',control_x)
        self.add(spline(name='x',N=N,num_nodes=num,dt=dt),name='spline')

        self.add_design_variable('control_x',lower=0, scaler=0.01)

        interp_x = self.declare_variable('interp_x',shape=(num))
        obj = interp_x[-1]
        self.register_output('obj',obj)
        self.add_objective('obj', scaler=1)



if __name__ == '__main__':
    # sim = python_csdl_backend.Simulator(spline(name='x',N=10,num_nodes=100,dt=0.1))
    sim = python_csdl_backend.Simulator(test())
    # sim.run()
    prob = CSDLProblem(problem_name='test', simulator=sim)
    optimizer = SNOPT(prob, Major_optimality=1e-14)
    optimizer.solve()
    
    interp = sim['interp_x']
    # print(sim['interp_x'])
    plt.plot(interp)
    plt.show()

    # print partials
    # sim.check_partials(compact_print=True)


"""
if __name__ == '__main__':
    # test code
    N=5
    num_nodes=10
    dt=0.1
    xt = np.linspace(0,num_nodes*dt,N)
    yt = np.ones(N)*100
    yt = np.linspace(0,num_nodes*dt,N)
    xlimits = np.array([[0.0, num_nodes*dt]])

    sm = RMTB(
                xlimits=xlimits,
                order=4,
                num_ctrl_pts=20,
                energy_weight=1e-15,
                regularization_weight=0.0,
                print_global=False,
                print_solver=False,
                derivative_solver='krylov')
    
    # sm = RBF(d0=100)
    sm.set_training_values(xt, yt)
    sm.train()
    xnew = np.arange(0, num_nodes*dt, dt)
    ynew = sm.predict_values(xnew)
    dict = sm.predict_output_derivatives(xnew)
    array = np.array(dict[None])
    print(array)
    print(ynew)
"""