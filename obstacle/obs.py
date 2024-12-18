from smt.surrogate_models import RBF
import numpy as np
from parameters_obs_time import options


n = 3500
x_lim = 12000.0 # (m)
be = options['be']
pi = options['p_i']
pf = options['p_f']
bf = options['p_f'] + 500
obs_height = options['obs_height']
x = np.linspace(0,x_lim,n)
obs = np.zeros((n))

for i in range(0,n):
    xi = x[i]
    if xi > pi and xi <= pf:
        obs[i] = obs_height
    elif xi > be and xi < pi:
        obs[i] = (np.sin((np.pi/(pi-be))*(xi-be)-(np.pi/2)) + 1)*(obs_height/2)
    elif xi > pf and xi < bf:
        obs[i] = (np.sin((np.pi/(bf-pf))*(xi-bf)-(np.pi/2)) + 1)*(obs_height/2)


sm_obs = RBF(d0=50,print_global=False,print_solver=False,)
sm_obs.set_training_values(x, obs)
sm_obs.train()





if __name__ == '__main__':
    import matplotlib.pyplot as plt

    num = 10000
    x_p = np.linspace(0,x_lim,num)
    obs_p = sm_obs.predict_values(x_p)

    plt.plot(x_p,obs_p)
    plt.scatter(x,obs)
    plt.xlim(0,6000)
    plt.show()