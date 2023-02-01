import numpy as np
from smt.surrogate_models import RMTB
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 12})

ctarr = np.array([[ 0.51538655, 0.50138509, 0.50234612, 0.50657741, 0.4968842 , 0.50657741,
   0.50234612, 0.50138509, 0.51538655],
 [ 0.42698462, 0.38653019, 0.3649351 , 0.35437556, 0.34367894, 0.35437556,
   0.3649351 , 0.38653019, 0.42698462],
 [ 0.37458359, 0.31369744, 0.27426553, 0.24794468, 0.23621672, 0.24794468,
   0.27426553, 0.31369744, 0.37458359],
 [ 0.35413659, 0.28467044, 0.23477996, 0.20404997, 0.19082589, 0.20404997,
   0.23477996, 0.28467044, 0.35413659],
 [ 0.38370143, 0.31060777, 0.25874042, 0.23118026, 0.23408659, 0.23118026,
   0.25874042, 0.31060777, 0.38370143],
 [ 0.41751251, 0.33459946, 0.27392436, 0.23836484, 0.22605008, 0.23836484,
   0.27392436, 0.33459946, 0.41751251],
 [ 0.38210907, 0.26820932, 0.16030228, 0.06727833, 0.03599741, 0.06727833,
   0.16030228, 0.26820932, 0.38210907],
 [ 0.28412781, 0.12893167,-0.01146464,-0.11553627,-0.16364372,-0.11553627,
  -0.01146464, 0.12893167, 0.28412781],
 [ 0.12577403,-0.04527575,-0.17721413,-0.25530664,-0.24518606,-0.25530664,
  -0.17721413,-0.04527575, 0.12577403]])

cparr = np.array([[ 0.37985526, 0.38179326, 0.39116855, 0.39602796, 0.3947334 , 0.39602796,
   0.39116855, 0.38179326, 0.37985526],
 [ 0.29978527, 0.28472851, 0.28021738, 0.27900814, 0.27534046, 0.27900814,
   0.28021738, 0.28472851, 0.29978527],
 [ 0.2322751 , 0.20319437, 0.18625398, 0.17526944, 0.16774962, 0.17526944,
   0.18625398, 0.20319437, 0.2322751 ],
 [ 0.18097614, 0.14563774, 0.11967273, 0.09907742, 0.08999168, 0.09907742,
   0.11967273, 0.14563774, 0.18097614],
 [ 0.17891547, 0.14162302, 0.11593144, 0.10376086, 0.10338575, 0.10376086,
   0.11593144, 0.14162302, 0.17891547],
 [ 0.24376891, 0.20183719, 0.17696412, 0.17163354, 0.17569131, 0.17163354,
   0.17696412, 0.20183719, 0.24376891],
 [ 0.25705909, 0.18001026, 0.11014038, 0.05912626, 0.04716499, 0.05912626,
   0.11014038, 0.18001026, 0.25705909],
 [ 0.17159926, 0.04558263,-0.07475992,-0.18425995,-0.26078881,-0.18425995,
  -0.07475992, 0.04558263, 0.17159926],
 [-0.01976056,-0.18204503,-0.31996773,-0.41610793,-0.41301933,-0.41610793,
  -0.31996773,-0.18204503,-0.01976056]])


# construct training data in a form smt can use
N = 9
d = 2.5 # (m)
rpm = 1500
xta = np.linspace(-100,100,N)/((rpm/60)*d)
xtb = np.linspace(-100,100,N)/((rpm/60)*d)
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

xlimits = np.array([[-100.0, 100.0], [-100.0, 100.0]])/((rpm/60)*d)

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
    x = np.linspace(-100,100,num)/((rpm/60)*d)
    y = np.linspace(-100,100,num)/((rpm/60)*d)
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


    levelsct = np.arange(-0.25, 0.5, 0.01)
    levelscp = np.arange(0.0, 0.45, 0.01)
    fig, ((ax1), (ax2)) = plt.subplots(1, 2)

    

    plot_ct = ax1.contourf(X, Y, ZCT, cmap='plasma', levels=levelsct)
    plot_cp = ax2.contourf(X, Y, ZCP, cmap='rainbow', levels=levelscp)

    ax1.contour(X,Y,ZCT,levels=levelsct,colors='k',alpha=0.2,linewidths=0.5)
    ax2.contour(X,Y,ZCP,levels=levelscp,colors='k',alpha=0.2,linewidths=0.5)


    plt.colorbar(plot_ct, shrink=1, ax=ax1)
    plt.colorbar(plot_cp, shrink=1, ax=ax2)
    ax1.set_title('$cruise~C_T$')
    ax2.set_title('$cruise~C_P$')
    ax1.set_ylabel('axial advance ratio')
    ax2.set_ylabel('axial advance ratio')
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
    
    
    