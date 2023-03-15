import numpy as np


# aircraft and mission parameter definitions
options = {} # aircraft and mission parameter dictionary

# aircraft data
options['mass'] = 3000 # 2000 # (kg)
options['wing_area'] = 19.6 # (m^2)
options['max_cruise_power'] = 468300 # (w)
options['max_lift_power'] = 145652 # 103652 (w)
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
options['p_i'] = 80 # (m) start of obstacle
options['p_f'] = 12000 # (m) end of obstacle
options['obs_height'] = 88 # (m) 75


"""
print(np.array2string(sim['control_x'],separator=','))
print(np.array2string(sim['control_z'],separator=','))
print(np.array2string(sim['control_alpha'],separator=','))
"""

# min e seed OBS!
options['dt'] = 2.002
options['control_x_i'] = np.array([1471.97102472,1467.79568523, 833.2229204 ,1304.67097586,1425.62668576,
 1462.89397377,1468.70269233,1476.53649816,1490.86030611,1475.90720767,
 1506.69317579,1544.08323009,1555.32099682,1560.64191914,1562.58158307,
 1504.3791399 ,1452.48625397,1449.89953668,1464.22948958,1430.05887626,
 1491.13099161,1480.54138779,1508.84692348,1518.52428729,1511.18100488,
 1524.06066031,1529.72670986,1521.17165643,1516.43709637,1518.21616041,
 1504.46814509,1489.40710515,1256.11322028,1022.94110079, 804.81742613,
  606.59681175, 438.16151038, 280.19957041, 151.323949  , 665.02978613])
options['control_z_i'] = np.array([1.13033399e+03,1.11426377e+03,1.12797873e+03,1.13366887e+03,
 1.13799704e+03,1.14174155e+03,1.14468683e+03,1.14529144e+03,
 1.14190277e+03,1.14370419e+03,1.13846486e+03,1.13332862e+03,
 1.10620474e+03,4.85696323e+02,1.33275588e+02,1.67215101e+01,
 8.55476926e-01,5.50500905e-02,7.13875884e-02,6.86264094e-02,
 8.40317021e-02,4.37614346e-02,1.35494622e-03,1.45158142e-03,
 1.47723262e-03,1.50799322e-03,1.53942202e-03,1.56397998e-03,
 1.57062310e-03,1.56200505e-03,1.54474765e-03,1.52582840e-03,
 1.50619316e-03,1.49811015e-03,1.49462946e-03,1.50712186e-03,
 1.53788410e-03,1.78454234e-02,1.86847642e-02,1.24863419e-03])
options['control_alpha_i'] = np.array([-8.19730986e-02,-1.56725329e+00,-7.17781908e-01,-6.92735390e-01,
 -5.53579286e-01,-3.38501959e-01,-1.76985014e-01,-9.67838087e-02,
 -7.35572742e-02,-3.05011251e-02,-3.70574341e-02,-3.75518105e-02,
  3.12788439e-02, 1.18574842e-01, 1.88371011e-01, 1.99391174e-01,
  1.60779281e-01, 9.22913243e-02, 6.98664438e-02, 5.57302623e-02,
  4.48357566e-02, 3.46119222e-02, 2.17369627e-02, 1.22578252e-02,
  5.71156740e-03,-1.35246930e-03,-6.55897243e-03,-8.80617123e-03,
 -1.14929392e-02,-1.09595816e-02,-1.09639534e-02,-1.00134060e-02,
 -1.47623138e-02,-1.45161181e-02,-1.10588455e-02,-3.32009314e-03,
  9.16909511e-03, 2.35932091e-02,-2.32121537e-02, 3.65365791e-02])


"""
# min dt seed new
options['dt'] = 1.499
options['control_x_i'] = np.array([1477.47014741,1417.81292867,1496.15121491,1498.4017867 ,1501.96477912,
 1505.01684938,1508.04043741,1505.39443368,1517.06254609,1541.50892715,
 1546.04454129,1562.05218713,1596.83906202,1586.93702028,1613.63332575,
 1618.39641925,1629.97405975,1653.7895603 ,1671.18000229,1636.33817534,
 1703.51902971,1695.38550771,1726.5473376 ,1735.77830766,1726.48846772,
 1739.44582402,1745.4484975 ,1735.84431128,1731.99784165,1738.76655698,
 1731.27955297,1718.75689868,1466.15385812,1205.69916543, 958.87020639,
  731.40657185, 533.98410776, 346.98317952, 213.73090777, 665.1318676 ])
options['control_z_i'] = np.array([1.09242549e+03,1.11206040e+03,1.12337663e+03,1.12694905e+03,
 1.13045674e+03,1.13435815e+03,1.13434086e+03,1.13296986e+03,
 1.13224078e+03,1.11141073e+03,1.12506322e+03,1.12292828e+03,
 1.06301685e+03,4.25046412e+02,9.53015441e+01,9.62694409e+00,
 3.82438482e-01,4.45160775e-03,1.26540906e-03,1.25317995e-03,
 1.33932405e-03,1.39384327e-03,1.44913855e-03,1.49092784e-03,
 1.51789975e-03,1.53311088e-03,1.54917055e-03,1.56213538e-03,
 1.56153884e-03,1.54923522e-03,1.53477194e-03,1.52012297e-03,
 1.50495617e-03,1.49859039e-03,1.49644905e-03,1.50944004e-03,
 1.47524591e-03,1.44344145e-03,5.53756322e-04,2.34764862e-07])
options['control_alpha_i'] = np.array([ 4.93198149e-02,-1.55914529e+00,-8.11249319e-01,-6.66829642e-01,
 -4.65060683e-01,-2.37813803e-01,-1.65990355e-01,-1.41637845e-01,
 -9.07975263e-02,-3.27030334e-02,-5.19591097e-02,-3.65760338e-02,
  5.21942560e-02, 1.52639188e-01, 1.86847364e-01, 1.75046892e-01,
  1.29389412e-01, 8.67243201e-02, 7.77459667e-02, 6.12642261e-02,
  4.99914466e-02, 4.16662600e-02, 3.05206504e-02, 2.29070194e-02,
  1.71685356e-02, 9.89241754e-03, 5.96229093e-03, 3.76509868e-03,
  6.55877990e-04,-1.42797356e-04,-1.69700860e-03, 9.20555172e-04,
 -3.39778131e-03,-2.55643601e-03, 2.42057992e-04, 4.78653602e-03,
  9.29526923e-03, 1.62377906e-02,-2.58977111e-02, 3.65392037e-02])
"""
