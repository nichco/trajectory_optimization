from smt.surrogate_models import RBF
import numpy as np
import matplotlib.pyplot as plt

def standard_atmosphere(z):

    # constants for standard atmosphere model
    g = 9.806 # m/(s^2)
    Ts = 288.16 # deg K @ sea level
    Ps = 1.01325E5 # Pascals at sea level
    rhoS = 1.225 # kg/m^3 at sea level
    R = 287 # J/(Kg-K) gas constant
    P11 = 2.2629E04 # pressure @ 11km
    P25 = 2.4879E03 # pressure @ 25km
    rho11 = 0.3639 # density @ 11km
    rho25 = 0.0400 # density @ 25km

    # standard atmosphere model
    # through 47000 m / 154000 ft
    if z <= 11000:
        a = -6.5E-3 # K/m
        temperature = Ts + a*z
        pressure = Ps*((temperature/Ts)**((-g)/(a*R)))
        density = rhoS*((temperature/Ts)**(-((g/(a*R)) + 1)))
    elif z > 11000 and z <= 25000:
        temperature = 216.6 # isothermal region
        pressure = P11*(np.exp(-(g/(R*temperature))*(z - 11000)))
        density = rho11*(np.exp(-(g/(R*216.66))*(z - 11000)))
    elif z > 25000 and z <= 47000:
        a = 3E-3
        temperature = 216.66 + a*(z - 25000)
        pressure = P25*((temperature/216.66)**((-g)/(a*R)))
        density = rho25*((temperature/216.66)**(-((g/(a*R)) + 1)))

    return pressure, density


def training():
    # generate (x, y) training data pairs for the standard atmosphere model
    max = 47000 # max altitude for atmospheric model
    step = 1000 # training data step size
    size = int(max/step)

    xt_pressure = np.zeros(size)
    xt_density = np.zeros(size)

    yt_pressure = np.zeros(size)
    yt_density = np.zeros(size)

    index = 0
    for z in range(0,max,step):
        xt_pressure[index] = 1*z
        xt_density[index] = 1*z

        p,d = standard_atmosphere(z)
        yt_pressure[index] = 1*p
        yt_density[index] = 1*d

        index += 1

    return xt_pressure, xt_density, yt_pressure, yt_density


def create_surrogate():
    # get training data
    xt_p,xt_d,yt_p,yt_d = training()

    # train RBF pressure surrogate
    sm_p = RBF(d0=10000,print_global=False,print_solver=False,)
    sm_p.set_training_values(xt_p, yt_p)
    sm_p.train()

    # train RBF density surrogate
    sm_d = RBF(d0=10000,print_global=False,print_solver=False,)
    sm_d.set_training_values(xt_d, yt_d)
    sm_d.train()

    return sm_p, sm_d


# create surrogate models for pressure and density upon initial import
sm_p,sm_d = create_surrogate()

"""
num = 1000
x = np.linspace(0.0, 47000.0, num)
yp = sm_p.predict_values(x)
yd = sm_d.predict_values(x)
plt.plot(x, yp)
plt.xlabel("altitude (m)")
plt.ylabel("pressure (Pa)")
plt.show()
plt.plot(x, yd)
plt.xlabel("altitude (m)")
plt.ylabel("density (kg/m^3)")
plt.show()
"""