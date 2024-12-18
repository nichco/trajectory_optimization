import numpy as np
from smt.surrogate_models import RMTB, RBF
import matplotlib.pyplot as plt

ctarr = np.array([[-0.00564201,  0.04190931,  0.31698614,  0.32625857,  0.20641409,  0.22660314, 0.34538624,  0.41009487,  0.53787701],
 [ 0.03679444,  0.079847,    0.18217462,  0.12895866,  0.17887687,  0.24725859, 0.32516338,  0.44185799,  0.57691904],
 [ 0.02890808,  0.03978804,  0.06522085,  0.11603378,  0.1697704,   0.24684351, 0.35266153,  0.47996701,  0.6242619 ],
 [ 0.02354366,  0.03122142,  0.06645637,  0.11617544,  0.18063375,  0.27206168, 0.38619259,  0.52694194,  0.67972499],
 [ 0.01420187,  0.02877443,  0.06398953,  0.1211803,   0.19975897,  0.29978717, 0.42213329,  0.57384097,  0.73311478],
 [-0.00631034,  0.0160385,   0.0670078,   0.1219933,   0.2083068,   0.31621328, 0.44635502,  0.60752161,  0.774881  ],
 [-0.01296341,  0.01147101, -0.01073402,  0.06100016,  0.19067773,  0.31164401, 0.45195189,  0.62030597,  0.79533495],
 [-0.01649178,  0.05747629, -0.08870613, -0.04304159,  0.0781499,   0.25694485, 0.42647442,  0.599534,    0.78689746],
 [-0.02016227,  0.35207976, -0.12459508, -0.12745927, -0.05237745,  0.10369238, 0.31777454,  0.53319674,  0.74539571]])

cparr = np.array([[-0.03990252, -0.04585387, -0.05804596, -0.03112995,  0.02408786,  0.07593604, 0.11681512,  0.19428081,  0.27392719],
 [ 0.00433417, -0.01766337, -0.01808524,  0.01670184,  0.05038186,  0.09493786, 0.16240778,  0.23841032,  0.33107771],
 [ 0.03190453,  0.00989249,  0.0138012,   0.03548539,  0.07610819,  0.13183474, 0.2048049,   0.29952289,  0.408021  ],
 [ 0.02455147,  0.01749612,  0.02722224,  0.05769091,  0.10786049,  0.1765811, 0.26619475,  0.38434193,  0.50874656],
 [ 0.01634217,  0.01952956,  0.04331201,  0.08789691,  0.15303855,  0.23892469, 0.34536543,  0.48237421,  0.62183756],
 [-0.00829634,  0.00498838,  0.05705983,  0.12573215,  0.20183442,  0.30093029, 0.42087596,  0.57337482,  0.72768594],
 [-0.03019199, -0.07514297, -0.03597061,  0.10545675,  0.2564434,   0.36691264, 0.49950503,  0.66432954,  0.83110801],
 [-0.08054339, -0.14919094, -0.20546618, -0.04760945,  0.1634497,   0.39650004, 0.56531752,  0.73767813,  0.92407962],
 [-0.14098017, -0.29677521, -0.30120213, -0.24177517, -0.0400949,   0.23273437, 0.52461651,  0.76592235,  0.98982662]])

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
            order=4,
            num_ctrl_pts=4,
            energy_weight=1e-10,
            regularization_weight=0.0,
            print_global=False,
            print_solver=False,)

sm_cp = RMTB(
            xlimits=xlimits,
            order=4,
            num_ctrl_pts=4,
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

    levelsct = np.arange(-0.1, 0.85, 0.02)
    levelscp = np.arange(0, 1, 0.02)
    fig, ((ax1), (ax2)) = plt.subplots(1, 2)

    plot_ct = ax1.contourf(X, Y, ZCT, cmap='plasma', levels=levelsct)
    plot_cp = ax2.contourf(X, Y, ZCP, cmap='rainbow', levels=levelscp)
    plt.colorbar(plot_ct, shrink=1, ax=ax1)
    plt.colorbar(plot_cp, shrink=1, ax=ax2)
    ax1.set_title('$C_t$')
    ax2.set_title('$C_p$')
    ax1.set_ylabel('Axial Inflow Velocity (m/s)')
    ax2.set_ylabel('Axial Inflow Velocity (m/s)')
    ax1.set_xlabel('Edgewise Inflow Velocity (m/s)')
    ax2.set_xlabel('Edgewise Inflow Velocity (m/s)')
    # plt.show()


    # test predict vals
    tt = np.array([[100,0]])
    val = sm_ct.predict_values(tt)
    print(val)

    plt.show()