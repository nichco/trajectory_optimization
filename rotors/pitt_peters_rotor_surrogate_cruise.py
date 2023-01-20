import numpy as np
from smt.surrogate_models import RMTB
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 12})

ctarr = np.array([[0.30466064, 0.29244744, 0.28230295, 0.27193481, 0.26792095, 0.27193481, 0.28230295, 0.29244744, 0.30466064],
 [0.26132066, 0.24154929, 0.22833687, 0.21605026, 0.21013064, 0.21605026, 0.22833687, 0.24154929, 0.26132066],
 [0.23475909, 0.2121092 , 0.19501965, 0.18216669, 0.18397825, 0.18216669, 0.19501965, 0.2121092 , 0.23475909],
 [0.2230508 , 0.20002176, 0.18365262, 0.18015868, 0.18228982, 0.18015868, 0.18365262, 0.20002176, 0.2230508 ],
 [0.23000979, 0.20801924, 0.19394784, 0.18751065, 0.18439698, 0.18751065, 0.19394784, 0.20801924, 0.23000979],
 [0.26265248, 0.24222789, 0.22997594, 0.22669962, 0.22539321, 0.22669962, 0.22997594, 0.24222789, 0.26265248],
 [0.30807096, 0.28968091, 0.28249675, 0.29015985, 0.298684  , 0.29015985, 0.28249675, 0.28968091, 0.30807096],
 [0.32719859, 0.29581935, 0.27595815, 0.26673718, 0.25651618, 0.26673718, 0.27595815, 0.29581935, 0.32719859],
 [0.31241688, 0.25593677, 0.2029379 , 0.15975728, 0.14542505, 0.15975728, 0.2029379 , 0.25593677, 0.31241688]])



cparr = np.array([[0.38065575, 0.36564349, 0.35350359, 0.34389175, 0.34014191, 0.34389175, 0.35350359, 0.36564349, 0.38065575],
 [0.32010061, 0.29933149, 0.28495068, 0.27153714, 0.26451247, 0.27153714, 0.28495068, 0.29933149, 0.32010061],
 [0.26735481, 0.24403667, 0.22557223, 0.17805779, 0.23819756, 0.17805779, 0.22557223, 0.24403667, 0.26735481],
 [0.22632239, 0.2023527 , 0.1830083 , 0.16804378, 0.1521415 , 0.16804378, 0.1830083 , 0.2023527 , 0.22632239],
 [0.20579774, 0.18304199, 0.16713229, 0.1576722 , 0.15276884, 0.1576722 ,0.16713229 ,0.18304199 ,0.20579774],
 [0.22000634, 0.20035655, 0.18895515, 0.18509266, 0.18316781, 0.18509266, 0.18895515, 0.20035655, 0.22000634],
 [0.26972494, 0.26081735, 0.26360652, 0.27803949, 0.28802175, 0.27803949, 0.26360652, 0.26081735, 0.26972494],
 [0.30561106, 0.29549815, 0.30101247, 0.31571088, 0.31691479, 0.31571088, 0.30101247, 0.29549815, 0.30561106],
 [0.29671857, 0.2640331 , 0.24275178, 0.22652735, 0.22401305, 0.22652735, 0.24275178, 0.2640331 , 0.29671857]])


# construct training data in a form smt can use
N = 9
xta = np.linspace(-100,100,N)
xtb = np.linspace(-100,100,N)
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

xlimits = np.array([[-100.0, 100.0], [-100.0, 100.0]])

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
    x = np.linspace(-100,100,num)
    y = np.linspace(-100,100,num)
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


    levelsct = np.arange(0.15, 0.4, 0.01)
    levelscp = np.arange(0.15, 0.4, 0.01)
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
    tt = np.array([[100,0]])
    val = sm_ct.predict_values(tt)
    print(val)

    plt.show()
    #plot = plt.contourf(xta, xtb, cparr,cmap='plasma',levels=levelsct)
    
    
    