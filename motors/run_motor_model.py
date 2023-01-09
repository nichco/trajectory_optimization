from TC1_motor_model.TC1_motor_analysis_model import TC1MotorAnalysisModel
from TC1_motor_model.TC1_motor_sizing_model import TC1MotorSizingModel
import numpy as np
import csdl
import python_csdl_backend
import matplotlib.pyplot as plt



class motor(csdl.Model):
    def initialize(self):
        self.parameters.declare('n')

        self.parameters.declare('q')
        self.parameters.declare('rpm')

    def define(self):
        n = self.parameters['n']

        self.create_input('load_torque_rotor',self.parameters['q'],shape=(n,))
        self.create_input('omega_rotor',self.parameters['rpm'],shape=(n,))


        D_i = 0.182
        L = 0.086
        
        
        #D_i = 0.4
        self.create_input('D_i',D_i)
        #L = 0.25
        self.create_input('L',L)
        
        self.add(TC1MotorSizingModel(
        pole_pairs = 6,
        phases=3,
        num_slots=36,
        rated_current=123
        ), name='sizing')


        self.add(TC1MotorAnalysisModel(
        pole_pairs = 6,
        phases=3,
        num_slots=36,
        V_lim=800,
        rated_current=123,
        fit_coeff_dep_H=np.array([0.00222, 10.36338, -3.13465]),
        fit_coeff_dep_B=np.array([1.12833, 1., 1., 1.]),
        num_nodes=n,
        num_active_nodes=n
        ), name='analysis')

        #output_power = self.declare_variable('output_power',shape=(n,))
        #input_power = self.declare_variable('input_power',shape=(n,))
        #self.register_output('eta',output_power/input_power)







if __name__ == '__main__':

    """
    q=800
    rpm=6000
    sim = python_csdl_backend.Simulator(motor(n=1,q=q,rpm=rpm))
    sim.run()
    print(sim['efficiency_active'])
    """
    
    d = 30
    qvec = np.zeros((d*d))
    rvec = np.zeros((d*d))

    rpm_space = np.linspace(500,6000,d)
    torque_space = np.linspace(10,2500,d)
    i = 0
    for rpm in rpm_space:
        for q in torque_space:
            rvec[i] = 1*rpm
            qvec[i] = 1*q
            i += 1

    sim = python_csdl_backend.Simulator(motor(n=d*d,q=qvec,rpm=rvec))
    sim.run()

    # print(np.array2string(sim['eta'],separator=','))
    print(np.array2string(sim['efficiency_active'],separator=','))
    
    
    X, Y = np.meshgrid(rpm_space,torque_space)
    Z = np.zeros((d,d))
    index = 0
    for i in range(d):
        for j in range(d):
            Z[j,i] = sim['efficiency_active'][index]
            index += 1
    
    levels = np.arange(0.0, 1.0, 0.01)
    
    contours = plt.contourf(X,Y,Z,cmap='jet',levels=levels)
    plt.clim(0,1)
    plt.show()
    
    