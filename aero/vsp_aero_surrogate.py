from smt.surrogate_models import RBF, RMTB
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 12})

#region data
# data from vspaero
xt = np.deg2rad(np.linspace(-90, 90, 37))
yt_cl = np.array([0,-0.13,-0.26,-0.39,-0.52,-0.65,-0.78,-0.91,-1.04,-1.16,-1.29,-1.43,-1.55,-1.6,-1.440866479,-0.952207817,-0.458042874,0.042272219,0.537553614,
1.030899101,1.4,1.45,1.4,1.31,1.21,1.11,1.01,0.91,0.81,0.71,0.61,0.51,0.41,0.31,0.21,0.11,0.01,])

yt_cd = np.array([1.191308205,1.188,1.186033965,1.179762265,1.158815985,1.113876301,1.047947196,0.965115078,0.866730629,0.750070161,0.620489728,0.481112557,
0.335140556,0.186836785,0.067410268,0.028389972,0.006013008,0.000950904,0.013505923,0.043538331,0.116663427,0.266083605,0.420373542,0.57145064,0.721261971,
0.861188551,0.985827271,1.094205044,1.177593611,1.240456117,1.282483901,1.296,1.299,1.302,1.305,1.308,1.311,])
#endregion

sm_cl = RBF(d0=0.15,print_global=False,print_solver=False,)
sm_cl.set_training_values(xt, yt_cl)
sm_cl.train()

sm_cd = RBF(d0=0.35,print_global=False,print_solver=False,)
sm_cd.set_training_values(xt, yt_cd)
sm_cd.train()






if __name__ == '__main__':
    num = 1000
    x = np.deg2rad(np.linspace(-90, 90, num))

    ycl = sm_cl.predict_values(x)
    ycd = sm_cd.predict_values(x)

    plt.rcParams['figure.figsize'] = [12, 3]

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(np.rad2deg(xt), yt_cl,'o',color='k')
    ax1.plot(np.rad2deg(x), ycl,color='k',linewidth=2)
    ax1.set_ylabel('lift coefficient')
    ax1.set_xlabel('angle of attack '+r'$(^{\circ}$)')
    ax1.legend(['VLM training points','RBF surrogate'], frameon=False)
    ax2.plot(np.rad2deg(xt), yt_cd,'o',color='k')
    ax2.plot(np.rad2deg(x), ycd,color='k',linewidth=2)
    ax2.set_ylabel('drag coefficient')
    ax2.set_xlabel('angle of attack '+r'$(^{\circ}$)')
    ax2.legend(['VLM training points','RBF surrogate'], frameon=False)
    plt.savefig('vsp_wing_model.png', dpi=1200, bbox_inches='tight')
    plt.show()