import numpy as np
from smt.surrogate_models import RMTB
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 12})

ctarr = np.array([[ 0.27527234 , 0.2570891  , 0.24206007,  0.23532886,  0.24206007,  0.2570891, 0.27527234],
 [ 0.2413152 ,  0.21910207,  0.20816377, -0.069667689,  0.20816377,  0.21910207, 0.2413152 ],
 [ 0.23573032,  0.21456918,  0.20992625,  0.20323507,  0.20992625 , 0.21456918, 0.23573032],
 [ 0.26029668,  0.23957331,  0.23167374,  0.23293493,  0.23167374,  0.23957331, 0.26029668],
 [ 0.28634104,  0.26554729,  0.25908844,  0.26219313,  0.25908844,  0.26554729, 0.28634104],
 [ 0.24710911,  0.21028245,  0.18178604,  0.16737932,  0.18178604,  0.21028245, 0.24710911],
 [ 0.16224415,  0.09408995,  0.05157397,  0.03749109,  0.05157397,  0.09408995, 0.16224415]])

cparr = np.array([[ 0.18575809,  0.1768958,   0.16898413,  0.16484272,  0.16898413,  0.1768958, 0.18575809],
 [ 0.13667546,  0.12396843,  0.10216338, 0.0185871,   0.10216338,  0.12396843, 0.13667546],
 [ 0.10767016, 0.09504349,  0.09523202, 0.07930297, 0.09523202,  0.09504349, 0.10767016],
 [ 0.11561739,  0.10595176,  0.10296542, 0.10183471, 0.10296542 , 0.10595176, 0.11561739],
 [ 0.16253955,  0.15742636,  0.16193041,  0.16808673,  0.16193041,  0.15742636,0.16253955],
 [ 0.17317604,  0.16295867,  0.15793526,  0.15475181,  0.15793526 , 0.16295867, 0.17317604],
 [ 0.11152926, 0.0727886,  0.05398328,  0.04957107 , 0.05398328 , 0.0727886, 0.11152926]])


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


    levelsct = np.arange(-0.05, 0.35, 0.01)
    levelscp = np.arange(0.05, 0.22, 0.01)
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
    
    
    