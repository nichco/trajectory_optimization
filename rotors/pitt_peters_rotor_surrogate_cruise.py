import numpy as np
from smt.surrogate_models import RMTB
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 12})

ctarr = np.array([[0.34109014, 0.32022758, 0.30803051, 0.30432654, 0.30803051, 0.32022758, 0.34109014],
 [0.27498589, 0.24261474, 0.2208496,  0.20759395, 0.2208496,  0.24261474, 0.27498589],
 [0.24059899, 0.20353147, 0.1788035,  0.1675615,  0.1788035,  0.20353147, 0.24059899],
 [0.24281987, 0.20633708, 0.18710435, 0.18013922, 0.18710435, 0.20633708, 0.24281987],
 [0.29894334, 0.26915449, 0.25724091, 0.25620867, 0.25724091, 0.26915449, 0.29894334],
 [0.34276908, 0.29244788, 0.26638418, 0.25411163, 0.26638418, 0.29244788, 0.34276908],
 [0.326719,   0.22106911, 0.12208725, 0.08928657, 0.12208725, 0.22106911, 0.326719  ]])



cparr = np.array([[0.42547426, 0.40049258, 0.38455166, 0.38547294, 0.38455166, 0.40049258, 0.42547426],
 [0.33536457, 0.30202057, 0.2801524,  0.26876275, 0.2801524,  0.30202057, 0.33536457],
 [0.26096398, 0.22332012, 0.19279575, 0.17012914, 0.19279575, 0.22332012, 0.26096398],
 [0.2207449,  0.184324,   0.16313566, 0.15262927, 0.16313566, 0.184324, 0.2207449 ],
 [0.25483283, 0.23020163, 0.22366887, 0.22286158, 0.22366887, 0.23020163, 0.25483283],
 [0.31285753, 0.29199657, 0.3031886,  0.31375242, 0.3031886,  0.29199657, 0.31285753],
 [0.30371861, 0.2223365,  0.16403792, 0.15348461, 0.16403792, 0.2223365, 0.30371861]])


# construct training data in a form smt can use
N = 7
xta = np.linspace(-75,75,N)
xtb = np.linspace(-75,75,N)
xt = np.zeros((N*N,2))
index = 0
for i in range(N):
    for j in range(N):
        xt[index,:] = [xta[i],xtb[j]]
        index += 1

yt_ct = np.zeros((N*N,1))
index = 0
for i in range(N):
    for j in range(N):
        yt_ct[index,:] = ctarr[i,j]
        index += 1

yt_cp = np.zeros((N*N,1))
index = 0
for i in range(N):
    for j in range(N):
        yt_cp[index,:] = cparr[i,j]
        index += 1

xlimits = np.array([[-75.0, 75.0], [-75.0, 75.0]])

# construct surrogate model
sm_ct = RMTB(
            xlimits=xlimits,
            order=3,
            num_ctrl_pts=4,
            energy_weight=1e-10,
            regularization_weight=0.0,
            print_global=False,
            print_solver=False,)

sm_cp = RMTB(
            xlimits=xlimits,
            order=3,
            num_ctrl_pts=4, # 4 cp's and order 4 introduces local minimum
            energy_weight=1e-10,
            regularization_weight=0.0,
            print_global=False,
            print_solver=False,)

# train model
sm_ct.set_training_values(xt, yt_ct)
sm_ct.train()

sm_cp.set_training_values(xt, yt_cp)
sm_cp.train()


if __name__ == '__main__':
    # interpolate surrogate model and plot it
    num = 100
    x = np.linspace(-75,75,num)
    y = np.linspace(-75,75,num)
    X, Y = np.meshgrid(x, y)

    xint = np.zeros((num*num,2))
    index = 0
    for i in range(num):
        for j in range(num):
            xint[index,:] = [x[i],y[j]]
            index += 1

    zint_ct = sm_ct.predict_values(xint)
    ZCT = np.zeros((num,num))
    index = 0
    for i in range(num):
        for j in range(num):
            ZCT[i,j] = zint_ct[index]
            index += 1

    zint_cp = sm_cp.predict_values(xint)
    ZCP = np.zeros((num,num))
    index = 0
    for i in range(num):
        for j in range(num):
            ZCP[i,j] = zint_cp[index]
            index += 1



    plt.rcParams['figure.figsize'] = [12, 4]


    levelsct = np.arange(0.1, 0.4, 0.01)
    levelscp = np.arange(0.15, 0.45, 0.01)
    fig, ((ax1), (ax2)) = plt.subplots(1, 2)

    

    plot_ct = ax1.contourf(X, Y, ZCT, cmap='plasma', levels=levelsct)
    plot_cp = ax2.contourf(X, Y, ZCP, cmap='rainbow', levels=levelscp)

    ax1.contour(X,Y,ZCT,levels=levelsct,colors='k',alpha=0.2,linewidths=0.5)
    ax2.contour(X,Y,ZCP,levels=levelscp,colors='k',alpha=0.2,linewidths=0.5)


    plt.colorbar(plot_ct, shrink=1, ax=ax1)
    plt.colorbar(plot_cp, shrink=1, ax=ax2)
    ax1.set_title('$cruise~C_T$')
    ax2.set_title('$cruise~C_P$')
    ax1.set_ylabel('axial inflow velocity (m/s)')
    ax2.set_ylabel('axial inflow velocity (m/s)')
    ax1.set_xlabel('edgewise inflow velocity (m/s)')
    ax2.set_xlabel('edgewise inflow velocity (m/s)')
    
    
    #ax1.set_xlim(0,60)
    #ax1.set_ylim(0,60)
    #ax2.set_xlim(0,60)
    #ax2.set_ylim(0,60)


    #plt.savefig('rotor_model.png', dpi=1200, bbox_inches='tight')

    # test predict vals
    tt = np.array([[10,0]])
    val = sm_ct.predict_values(tt)
    print(val)

    plt.show()
    #plot = plt.contourf(xta, xtb, cparr,cmap='plasma',levels=levelsct)
    
    
    