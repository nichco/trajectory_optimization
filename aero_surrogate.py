from smt.surrogate_models import RBF, RMTB
import numpy as np
import matplotlib.pyplot as plt

xt = np.linspace(-30, 30, 61)
yt_cl = np.array([0,0,0,0,0,0,0,0,0,0,
                -0,-0,-0.01,-0.02,-0.04,-0.07,-0.1,-0.17,-0.25,-0.37,
                -0.5314,-0.61,-0.6353,-0.568,-0.4854,-0.3957,-0.3076,-0.1436,0.0914,0.2692,
                0.401,0.5091,0.6101,0.7044,0.8008,0.8925,0.9747,1.0335,1.0833,1.1539,
                1.2206,1.2586,1.2148,1.1052,0.8,0.5,0.3,0.14,0.05,0.01,0,
                0,0,0,0,0,0,0,0,0,0])

yt_cd = np.array([0.37536,0.34,0.3,0.23,0.20285,0.18013,0.16549,0.15658,0.13657,0.12271,
                0.11641,0.09726,0.08653,0.07473,0.06647,0.05788,0.05091,0.04659,0.04296,0.03895,
                0.03576,0.035,0.03,0.03,0.02778,0.02332,0.02039,0.01869,0.01702,0.01732,0.01669,
                0.01596,0.01561,0.01587,0.01666,0.01746,0.01837,0.01947,0.02223,0.02742,0.03392,
                0.04141,0.05186,0.06233,0.07,0.073,0.075,0.08,0.088,0.09923,0.10924,
                0.12493,0.14493,0.15622,0.17977,0.19094,0.20944,0.22779,0.2466,0.27293,0.29])

sm_cl = RBF(d0=8,print_global=False,print_solver=False,)
sm_cl.set_training_values(xt, yt_cl)
sm_cl.train()

sm_cd = RBF(d0=30,print_global=False,print_solver=False,)
sm_cd.set_training_values(xt, yt_cd)
sm_cd.train()

"""
num = 1000
x = np.linspace(-30, 30, num)

ycl = sm_cl.predict_values(x)

plt.plot(xt, yt_cl, "o")
plt.plot(x, ycl)
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["Training data", "Prediction"])
plt.show()

ycd = sm_cd.predict_values(x)

plt.plot(xt, yt_cd, "o")
plt.plot(x, ycd)
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["Training data", "Prediction"])
plt.show()
"""