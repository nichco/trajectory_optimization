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
options['dt'] = 2.003
options['control_x_i'] = np.array([1478.09518288,1472.03027224, 761.24808783,1416.3592413 ,1500.08669639,
 1503.91797669,1510.88793507,1515.04206506,1522.03136907,1528.61392321,
 1539.35696082,1561.73000491,1586.17603082,1599.0848711 ,1615.37136332,
 1534.90803181,1450.50655596,1458.5982106 ,1473.17678701,1437.50771015,
 1501.02259366,1491.8511784 ,1518.29594829,1526.07167678,1517.08016206,
 1528.36828582,1532.28516906,1521.83374945,1515.07908175,1514.78517608,
 1498.86053936,1481.51030377,1246.42893417,1012.15326425, 793.88419047,
  596.65858881, 430.0546185 , 274.13253471, 144.0837857 , 662.48664145])
options['control_z_i'] = np.array([1.13006049e+03,1.11163389e+03,1.12560041e+03,1.13095535e+03,
 1.13497007e+03,1.13844025e+03,1.14146554e+03,1.14354399e+03,
 1.14280268e+03,1.14248082e+03,1.09189019e+03,1.13427175e+03,
 1.13400070e+03,6.95625981e+02,2.29582177e+02,3.14109163e+01,
 1.22681409e+00,5.66100437e-02,7.33466557e-02,6.87075142e-02,
 8.22538302e-02,4.42697428e-02,1.58679258e-03,1.48015183e-03,
 1.50195408e-03,1.53345396e-03,1.56732009e-03,1.59389350e-03,
 1.60010917e-03,1.58806860e-03,1.56770077e-03,1.55214987e-03,
 1.53925549e-03,1.53123449e-03,1.51680312e-03,1.50878291e-03,
 1.51226725e-03,1.85211500e-02,1.94064609e-02,1.26009052e-03])
options['control_alpha_i'] = np.array([-8.19715026e-02,-1.57079176e+00,-7.10804194e-01,-7.32216477e-01,
 -5.69031432e-01,-3.42295247e-01,-1.30646904e-01,-2.10200156e-02,
  5.55597449e-03,-1.05843380e-02,-6.03869016e-02,-7.17087395e-02,
  7.76489537e-03, 1.10911077e-01, 1.81242766e-01, 1.87652718e-01,
  1.33044932e-01, 7.84362534e-02, 6.79201452e-02, 5.01468364e-02,
  3.28962510e-02, 3.47003740e-02, 2.51116769e-02, 1.42744650e-02,
  6.56481725e-03,-3.82731431e-04,-4.88915737e-03,-6.96187560e-03,
 -9.92906248e-03,-1.08293635e-02,-1.23562270e-02,-1.14009334e-02,
 -1.28264230e-02,-1.05509786e-02,-8.73572628e-03,-6.50751979e-03,
 -1.30224204e-04, 1.73921453e-02,-9.87018189e-03, 3.11370088e-02])


