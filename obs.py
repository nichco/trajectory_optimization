from smt.surrogate_models import RBF, RMTB
import numpy as np


n = 500
x_lim = 10000.0 # (m)
be = 10
pi = 100 # (m)
pf = 10000.0 # (m)
o = 1 # (m)
x = np.linspace(0,x_lim,n)
obs = np.zeros((n))

for i in range(n):
    xi = x[i]
    if xi > pi and xi < pf:
        obs[i] = o
    elif xi > be and xi < pi:
        l = (pi-be)
        obs[i] = (np.sin((np.pi/(pi-be))*(xi-be)-(np.pi/2)) + 1)*(o/2)


sm = RBF(d0=20,print_global=False,print_solver=False,)
sm.set_training_values(x, obs)
sm.train()





if __name__ == '__main__':
    import matplotlib.pyplot as plt

    num = 10000
    x_p = np.linspace(0,x_lim,num)
    obs_p = sm.predict_values(x_p)

    plt.plot(x_p,obs_p)
    plt.scatter(x,obs)
    plt.xlim(0,10000)
    plt.show()