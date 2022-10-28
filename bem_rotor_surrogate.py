import numpy as np
from smt.surrogate_models import RMTB, RBF
import matplotlib.pyplot as plt

ctarr = np.array()

cparr = np.array()

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

yt = np.zeros((N*N,1))
index = 0
for i in range(N):
    for j in range(N):
        yt[index,:] = ctarr[i,j]
        index += 1

xlimits = np.array([[-100.0, 100.0], [-100.0, 100.0]])

# construct surrogate model
sm = RMTB(
            xlimits=xlimits,
            order=4,
            num_ctrl_pts=4,
            energy_weight=1e-10,
            regularization_weight=0.0,
            print_global=False,
            print_solver=False,)

# train model
sm.set_training_values(xt, yt)
sm.train()


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

zint = sm.predict_values(xint)
Z = np.zeros((num,num))
index = 0
for i in range(num):
    for j in range(num):
        Z[i,j] = zint[index]
        index += 1

plot = plt.contourf(X, Y, Z, cmap='plasma')
plt.colorbar(plot, shrink=1)
plt.title('Thrust Coefficient')
plt.ylabel('Axial Inflow Velocity (m/s)')
plt.xlabel('Edgewise Inflow Velocity (m/s)')
plt.show()

"""
sm = RBF(d0=0.1,print_global=False,print_solver=False,)
sm.set_training_values(xt, ctarr)
sm.train()
"""