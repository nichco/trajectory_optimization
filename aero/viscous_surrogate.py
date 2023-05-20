from smt.surrogate_models import RBF, RMTB
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 12})

#region data
alpha = np.deg2rad(np.array([-90.0,-86.0,-82.0,-78.0,-74.0,-70.0,-66.0,-62.0,-58.0,-54.0,-50.0,-46.0,-42.0,-38.0,-34.0,-30.0,-28.0,
                    -26.0,-24.0,-22.0,-20.0,-18.0,-16.0,-14.0,-12.0,-10.0,-9.0,-8.0,-7.0,-6.0,-5.0,-4.0,-3.0,-2.0,-1.0,
                    0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,12.0,14.0,16.0,18.0,20.0,22.0,24.0,26.0,28.0,30.0,34.0,
                    38.0,42.0,46.0,50.0,54.0,58.0,62.0,66.0,70.0,74.0,78.0,82.0,86.0,90.0,]))

mach = np.array([0,0.05,0.1,0.15,0.2,0.25])

yt_cl = np.array([0,-0.1,-0.2,-0.3,-0.4,-0.5,-0.6,-0.7,-0.8,-0.9,-1,-1.1,-1.2,-1.3,-1.4,-1.51,-1.57,-1.6,-1.588070455,-1.530320887,-1.435595552,-1.239615964,
-1.041723778,-0.845277566,-0.648485652,-0.450238406,-0.348259602,-0.248636703,-0.148952539,-0.0481308,0.050757594,0.150340236,0.250846236,0.349074757,
0.449352117,0.547829033,0.645443497,0.746708352,0.840086807,0.941883703,1.038413324,1.136352044,1.235221826,1.333400827,1.385795143,1.409719559,
1.44,1.42,1.38,1.34,1.3,1.26,1.22,1.18,1.14,1.1,1.03,0.96,0.89,0.82,0.75,0.68,0.61,0.54,0.47,0.4,0.33,0.26,0.19,0.12,0.05,])

yt_cdi = np.array([1.285,1.28,1.279793779,1.273160103,1.265681088,1.232972271,1.19040054,1.134941379,1.061688602,0.976249697,0.890448309,0.789433507,
0.681494704,0.567166135,0.449270459,0.325785086,0.265547002,0.203603892,0.144397407,0.094618849,0.053416623,0.036564225,0.022821768,
0.012353886,0.003485044,-0.002600189,-0.005194702,-0.006713881,-0.007742439,-0.00769314,-0.007594652,-0.006369865,-0.005088151,-0.002464788,
0.00011891,0.003609361,0.007805871,0.012475276,0.017667058,0.023755429,0.03005707,0.037105731,0.044793811,0.053018973,0.072896471,0.099600972,
0.157334225,0.218046899,0.278941601,0.339442619,0.400480584,0.460611005,0.520034671,0.579355032,0.640043686,0.699553734,0.805142894,
0.906641227,0.994160511,1.074643432,1.135182693,1.189257697,1.225111109,1.232,1.238888891,1.245777782,1.252666674,1.259555565,1.266444456,
1.273333347,1.280222239,])

#yt_cd0 = np.array([0.05645,0.03448,0.02044,0.01885,0.01779,0.01702,])
yt_cd0 = np.array([0.05745,0.03448,0.02444,0.02085,0.01979,0.01902,])
#endregion

# format data
n = len(yt_cdi)*len(mach)
xt_cd = np.zeros((n,2))
yt_cd = np.zeros((n))
i = 0
for a in enumerate(alpha):
    for m in enumerate(mach):
        xt_cd[i,0] = a[1]
        xt_cd[i,1] = m[1]
        yt_cd[i] = yt_cdi[a[0]] + yt_cd0[m[0]] # drag buildup: cd = cd0 + cdi
        i = i + 1

# train surrogate models
sm_cl = RBF(d0=0.3,print_global=False,print_solver=False,)
sm_cl.set_training_values(alpha, yt_cl)
sm_cl.train()

xlimits = np.array([[-np.pi/2, np.pi/2],[0,0.25]])
sm_cd = RMTB(
            xlimits=xlimits,
            order=3,
            num_ctrl_pts=17,
            energy_weight=1e-10,
            regularization_weight=0.0,
            print_global=False,
            print_solver=False,)
sm_cd.set_training_values(xt_cd, yt_cd)
sm_cd.train()






if __name__ == '__main__':


    fig = plt.figure(figsize=[12, 3])

    
    num = 1000
    xcl = np.deg2rad(np.linspace(-90, 90, num))
    ycl = sm_cl.predict_values(xcl)

    ax1 = fig.add_subplot(1, 2, 1)
    ax1.plot(np.rad2deg(alpha), yt_cl,'o',color='darkkhaki',markersize=6)
    ax1.plot(np.rad2deg(xcl), ycl,color='k',linewidth=1.0)

    plt.xticks(np.arange(-90, 95, 30))
    plt.yticks(np.arange(-1.5, 1.75, 0.5))

    plt.xlim([-90,90])
    
    ax1.set_ylabel('lift coefficient')
    ax1.set_xlabel('angle of attack '+r'($^{\circ}$)')
    ax1.legend(['VLM training points','RBF surrogate'], frameon=False)
    

    num=100
    x_alpha = np.deg2rad(np.linspace(-90, 90, num))
    x_mach = np.linspace(0,0.25,num)
    X, Y = np.meshgrid(x_alpha,x_mach)

    # interpolation vector for smt data
    xint = np.zeros((num*num,2))
    index = 0
    for i in range(num):
        for j in range(num):
            xint[index,0] = x_alpha[i]
            xint[index,1] = x_mach[j]
            index += 1

    # interpolate data:
    zint_cd = sm_cd.predict_values(xint)
    Z = np.zeros((num,num))
    index = 0
    for i in range(num):
        for j in range(num):
            Z[i,j] = zint_cd[index]
            index += 1

    """
    # Plot the surface.
    levels = np.arange(0.0, 1.4, 0.005)
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    #fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    surf = ax2.plot_surface(np.rad2deg(X), Y, Z.T, cmap=cm.coolwarm,
                       linewidth=1, antialiased=True,vmin=0,vmax=1.2,rcount=20,ccount=100)
    ax2.set_xlabel('angle of attack')
    ax2.set_ylabel('mach number')
    ax2.set_zlabel('$C_D$')
    ax2.set_box_aspect((1.5,1.5,1))
    """
    
    levels = np.arange(0.0, 1.5, 0.05)
    ax2 = fig.add_subplot(1, 2, 2)
    plot_cd = ax2.contourf(np.rad2deg(X), Y, Z.T, cmap='rainbow', levels=levels)
    ax2.contour(np.rad2deg(X), Y, Z.T,levels=levels,colors='k',alpha=0.2,linewidths=0.5)
    cbar = plt.colorbar(plot_cd, shrink=1, ax=ax2)
    cbar.set_label('drag coefficient')
    ax2.set_ylabel('mach number')
    ax2.set_xlabel('angle of attack '+r'($^{\circ}$)')
    plt.xticks(np.arange(-90, 95, 30))

    plt.savefig('viscous_aero_model.png', dpi=1200, bbox_inches='tight')
    
    plt.show()

    
