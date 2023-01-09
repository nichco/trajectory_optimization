import numpy as np
import matplotlib.pyplot as plt
from smt.surrogate_models import RMTB, RBF
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 12})

eta = np.loadtxt('Nick_surrogate_data_efficiency.txt').astype(np.double)
rpm = np.loadtxt('Nick_surrogate_data_speed.txt').astype(np.double)
q = np.loadtxt('Nick_surrogate_data_torque.txt').astype(np.double)

plt.rcParams['figure.figsize'] = [6, 3]
levels = np.arange(0.0, 1.0, 0.03)
plot = plt.contourf(rpm,q,eta,cmap='jet',levels=levels)
plt.contour(rpm,q,eta,colors='k',levels=levels,linewidths=1,alpha=0.3)
plt.colorbar(plot, shrink=1)
plt.xlabel('motor speed (rpm)')
plt.ylabel('load torque (N-m)')
#plt.savefig('motor_model.png', dpi=1200, bbox_inches='tight')
plt.show()

xta = np.zeros((80*120))
xtb = np.zeros((80*120))
yt = np.zeros((80*120))
index = 0
for i in range(80):
    for j in range(120):
        xta[index] = rpm[i,j]
        xtb[index] = q[i,j]
        yt[index] = eta[i,j]
        index += 1





xt = np.transpose(np.array([xta, xtb]))

xlimits = np.array([[xta.min(), xta.max()], [xtb.min(), xtb.max()]])
"""
sm_eta = RMTB(
            xlimits=xlimits,
            order=3,
            num_ctrl_pts=10,
            energy_weight=1e-10,
            regularization_weight=0.0,
            print_global=False,
            print_solver=False,)
"""
sm_eta = RBF(d0=6000,print_global=False,print_solver=False,)
# train model
sm_eta.set_training_values(xt[0:-1:4], yt[0:-1:4])
sm_eta.train()


if __name__ == '__main__':
    # interpolate surrogate model and plot it
    num = 100
    x = np.linspace(0,6000,num)
    y = np.linspace(0,1000,num)
    X, Y = np.meshgrid(x, y)

    xint = np.zeros((num*num,2))
    index = 0
    for i in range(num):
        for j in range(num):
            xint[index,:] = [x[i],y[j]]
            index += 1

    zint_eta = sm_eta.predict_values(xint)
    ZN = np.zeros((num,num))
    index = 0
    for i in range(num):
        for j in range(num):
            ZN[j,i] = zint_eta[index]
            index += 1
            
    plt.rcParams['figure.figsize'] = [6, 3]
    levels = np.arange(-0.1, 1.1, 0.03)
    plot = plt.contourf(X, Y, ZN, cmap='jet', levels=levels)
    plt.contour(X,Y,ZN,colors='k',levels=levels,linewidths=0.5,alpha=0.5)
    plt.colorbar(plot, shrink=1)
    plt.xlabel('motor speed (rpm)')
    plt.ylabel('load torque (N-m)')
    
    #plt.savefig('motor_model.png', dpi=1200, bbox_inches='tight')
    
    plt.show()


