import numpy as np


# aircraft and mission parameter definitions
options = {} # aircraft and mission parameter dictionary

# aircraft data
options['mass'] = 3000 # 2000 # (kg)
options['wing_area'] = 19.6 # (m^2)
options['max_cruise_power'] = 468300 # (w)
options['max_lift_power'] = 138652 # 103652 (w)
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
options['vne'] = 67 # (m/s)
options['x_lim'] = 5000 # (m)
options['theta_0'] = 0.0 # (rad)
options['gamma_f'] = 0.0 # (rad)
options['max_g'] = 0.5 # (g)

# obstacle
options['be'] = 10 # (m) start of sinusoidal ramp
options['p_i'] = 130 # (m) start of obstacle
options['p_f'] = 12000 # (m) end of obstacle
options['obs_height'] = 100 # (m) 75


"""
print(np.array2string(sim['control_x'],separator=','))
print(np.array2string(sim['control_z'],separator=','))
print(np.array2string(sim['control_alpha'],separator=','))
"""

# min dt seed
options['dt'] = 1.9849
options['control_x_i'] = np.array([1372.82014894,1472.80232258,1498.86135573,1491.20270863,1487.11320601,
 1490.46870826,1516.15738813,1517.85453959,1539.83894125,1557.88107054,
 1582.36240238,1591.24318923,1582.77139934,1606.41641442,1620.12138517,
 1646.66816629,1673.71048718,1698.55597106,1039.65843129,1306.86293092,
 1161.68135956,1213.93228743,1183.46543814,1198.82161886,1148.54118476,
 1115.74266521,1124.06110462,1143.05592708,1131.14116598,1146.95567062,
 1171.65474959,1183.18989671,1210.51298292,1204.95707933,1188.83384462,
 1202.89313989,1157.56416974,1113.21079052,1133.20204853, 777.34603529])
options['control_z_i'] = np.array([1.12705171e+03,1.09690645e+03,1.10988723e+03,1.11312144e+03,
 1.11833221e+03,1.11937229e+03,1.13018806e+03,1.13201947e+03,
 1.12744859e+03,1.11749478e+03,1.12560621e+03,4.00338526e+02,
 6.75096876e+02,4.40819389e+02,3.47899559e+02,2.27502382e+02,
 1.38686313e+02,1.39850130e+02,2.46463198e+02,1.99825449e+02,
 1.41622492e+02,1.08455804e+02,1.30806951e+02,1.93398594e+02,
 1.68920400e+02,2.27666101e+02,1.95796488e+02,9.95350103e+01,
 5.11114588e-12,3.81267216e+01,3.72435992e-02,7.35508095e-01,
 2.91636918e+00,5.70699237e-01,5.16298624e-01,8.48455628e-02,
 1.42599777e-02,0.00000000e+00,1.46058753e+00,2.92358334e-01])
options['control_alpha_i'] = np.array([-1.04226004e-02,-1.56349446e+00,-8.83086753e-01,-1.08802707e+00,
 -8.51147663e-01,-5.07492851e-01,-5.44551414e-03, 7.31195555e-02,
 -3.01338652e-02,-1.54125609e-01, 7.65027546e-02, 1.95452829e-01,
  1.70627723e-01, 1.30023131e-01, 1.56822992e-01, 4.89490067e-02,
  6.66040204e-02, 3.77783661e-02, 2.98082722e-02, 2.18640474e-02,
  1.49825169e-02, 5.24916669e-03, 1.18559626e-02,-5.16595161e-03,
 -1.87885213e-03,-1.48435637e-02,-9.20842741e-03,-1.68361322e-02,
 -1.74645875e-02, 1.41829256e-02,-7.14030664e-03,-3.80603476e-03,
 -1.01583446e-02, 1.22858966e-03, 1.38187018e-03, 1.32717972e-02,
  1.47665077e-02, 1.67985349e-02,-4.57360011e-03,-1.64431643e-02])


