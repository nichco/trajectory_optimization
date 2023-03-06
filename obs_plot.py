from smt.surrogate_models import RBF
import numpy as np


n = 3500
x_lim = 10000.0 # (m)
be = 10
pi = 50
pf = 1000
o = 100
x = np.linspace(0,x_lim,n)
obs = np.zeros((n))

for i in range(0,n):
    xi = x[i]
    if xi > pi and xi <= pf:
        obs[i] = o
    elif xi > be and xi < pi:
        l = (pi-be)
        obs[i] = (np.sin((np.pi/(pi-be))*(xi-be)-(np.pi/2)) + 1)*(o/2)

sm = RBF(d0=50,print_global=False,print_solver=False,)
sm.set_training_values(x, obs)
sm.train()





if __name__ == '__main__':
    import matplotlib.pyplot as plt
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams.update({'font.size': 12})
    plt.rcParams['figure.figsize'] = [5, 2.0]

    num = 10000
    x_p = np.linspace(0,x_lim,num)
    obs_p = sm.predict_values(x_p)

    plt.plot(x_p,obs_p,'k',linewidth=0.5)
    #plt.scatter(x,obs)
    plt.fill_between(x_p,obs_p.flatten(),alpha=0.8,color='mistyrose',hatch='///',edgecolor='indianred')
    plt.xlim(0,500)
    plt.ylim(0,300)
    plt.xlabel('horizontal position (m)')
    plt.ylabel('altitude (m)')

    plt.text(200, 45, 'No Fly Zone', color='red', fontsize=12,bbox={'facecolor': 'white', 'alpha': 0.8, 'pad': 3})

    plt.savefig('nfz', dpi=1200, bbox_inches='tight')
    plt.show()