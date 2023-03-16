import numpy as np


# aircraft and mission parameter definitions
options = {} # aircraft and mission parameter dictionary

# aircraft data
options['mass'] = 3000 # 2000 # (kg)
options['wing_area'] = 19.6 # (m^2)
options['max_cruise_power'] = 468300 # (w)
options['max_lift_power'] = 143652 # 103652 (w)
options['cruise_rotor_diameter'] = 2.6 # (m)
options['lift_rotor_diameter'] = 2.4 # (m)
options['num_lift_rotors'] = 8
options['num_cruise_blades'] = 3
options['num_lift_blades'] = 2
options['cruise_mac'] = 0.15 # (m)
options['lift_mac'] = 0.15 # (m)
options['c_sigma'] = 0.19
options['l_sigma'] = 0.095
options['energy_scale'] = 0.0001 # scale energy for plotting

# mission parameters
options['gravity'] = 9.81 # (m/s^2)
options['v_0'] = 0.625 #spyder:0.625 (m/s)
options['gamma_0'] = 0.0 # (rad)
options['h_0'] = 0 # (m)
options['min_h'] = -0.1 # (m)
options['x_0'] = 0 # (m)
options['alpha_0'] = 0 # (rad)
options['h_f'] = 300 # (m)
options['v_f'] = 58 # 43 (m/s)
options['vne'] = 65 # (m/s)
options['x_lim'] = 5000 # (m)
options['theta_0'] = 0.0 # (rad)
options['gamma_f'] = 0.0 # (rad)
options['max_g'] = 0.5 # (g)

# obstacle
options['be'] = 10 # (m) start of sinusoidal ramp
options['p_i'] = 150 # (m) start of obstacle
options['p_f'] = 12000 # (m) end of obstacle
options['obs_height'] = 100 # (m) 75


"""
print(np.array2string(sim['control_x'],separator=','))
print(np.array2string(sim['control_z'],separator=','))
print(np.array2string(sim['control_alpha'],separator=','))
"""

# min dt seed
options['dt'] = 2.001
options['control_x_i'] = np.array([1478.12367982,1472.11156164, 761.28111538,1416.3147309 ,1500.05008518,
 1503.9069216 ,1510.88994445,1515.0570821 ,1522.06937277,1528.67776166,
 1539.42537204,1561.79700418,1586.24335311,1599.15178291,1615.43035922,
 1534.98013558,1450.58289857,1458.67501135,1473.24501163,1437.56226459,
 1501.06554706,1491.88438941,1518.3222514 ,1526.09420134,1517.10221576,
 1528.39313967,1532.31525289,1521.87043679,1515.12284836,1514.83544964,
 1498.91544969,1481.56613284,1246.4774836 ,1012.19105182, 793.91066065,
  596.67478333, 430.06286897, 274.13557108, 144.08443515, 662.48674773])
options['control_z_i'] = np.array([1.13006913e+03,1.11164246e+03,1.12561257e+03,1.13101230e+03,
 1.13500112e+03,1.13854473e+03,1.14150859e+03,1.14334904e+03,
 1.14252884e+03,1.14223456e+03,1.09184727e+03,1.13430345e+03,
 1.13401119e+03,6.95612481e+02,2.29572089e+02,3.14077568e+01,
 1.22644790e+00,5.66094720e-02,7.33526311e-02,6.87153379e-02,
 8.22615170e-02,4.42736296e-02,1.58741853e-03,1.48018991e-03,
 1.50193650e-03,1.53338587e-03,1.56721374e-03,1.59376965e-03,
 1.59999544e-03,1.58799258e-03,1.56768571e-03,1.55221087e-03,
 1.53939886e-03,1.53145165e-03,1.51707256e-03,1.50907231e-03,
 1.51300027e-03,1.85233195e-02,1.94078576e-02,1.26022506e-03])
options['control_alpha_i'] = np.array([-8.19743680e-02,-1.57078812e+00,-7.10847277e-01,-7.32225859e-01,
 -5.69034181e-01,-3.42295633e-01,-1.30654158e-01,-2.10361337e-02,
  5.53463947e-03,-1.06058307e-02,-6.03991689e-02,-7.17177172e-02,
  7.75450797e-03, 1.10900294e-01, 1.81230839e-01, 1.87638351e-01,
  1.33033473e-01, 7.84413334e-02, 6.79402655e-02, 5.01753207e-02,
  3.29254433e-02, 3.47262464e-02, 2.51295650e-02, 1.42801692e-02,
  6.55664645e-03,-4.04005270e-04,-4.92092139e-03,-6.99967384e-03,
 -9.96668102e-03,-1.08598856e-02,-1.23727233e-02,-1.13978141e-02,
 -1.28006237e-02,-1.05042603e-02,-8.67428608e-03,-6.44081903e-03,
 -6.89267651e-05, 1.74385343e-02,-9.84511575e-03, 3.11400551e-02])


