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
options['p_i'] = 50 # (m) start of obstacle
options['p_f'] = 12000 # (m) end of obstacle
options['obs_height'] = 100 # (m)


# initial control inputs
"""
options['control_x_i'] = np.ones(30)*2300
options['control_z_i'] = np.linspace(800, 100, 30)
options['control_alpha_i'] = np.linspace(0.7, 0, 30)
"""
"""
print(np.array2string(sim['control_x'],separator=','))
print(np.array2string(sim['control_z'],separator=','))
print(np.array2string(sim['control_alpha'],separator=','))
"""


# min e seed OBS!
options['dt'] = 4.02572608
options['control_x_i'] = np.array([1478.46291963,1469.89313482,1560.41535417,1590.53808922,1621.73873238,
 1244.0962006 ,1139.3047715 ,1080.90968068,1028.03294735, 963.21110765,
  926.68966409, 921.59410933, 897.03680267, 869.98739013, 869.92853194,
  862.97268909, 863.59632053, 849.46438729, 839.41328059, 828.43927638,
  823.59744976, 819.79094245, 816.722397  , 816.34322888, 815.85725569,
  816.21572374, 816.13853329, 816.49333084, 817.03434724, 817.87147409,
  818.7012501 , 819.38575553, 819.99193232, 820.77274311, 821.49949175,
  822.20552729, 823.01385586, 823.64935718, 824.46373525, 825.169119  ,
  825.97997084, 827.12805134, 827.26217788, 823.98450006, 813.65029409,
  750.85538109, 665.06724497])
options['control_z_i'] = np.array([1.13817675e+03,1.09420408e+03,1.12693520e+03,9.36103221e+02,
 3.41639942e+02,7.75889438e+01,4.10493391e-11,5.11586905e-01,
 4.12268108e-01,4.52295058e-03,5.69608324e-03,2.97886631e-14,
 1.30775692e-04,4.61522972e-05,2.84625705e-05,7.12929525e-05,
 3.48819372e-04,2.07655999e-04,2.90751657e-04,3.28542985e-04,
 2.83440131e-04,3.20977350e-04,3.34839949e-04,3.39636738e-04,
 3.47913471e-04,3.50960142e-04,3.54240729e-04,3.53744145e-04,
 3.53931573e-04,3.53849241e-04,3.54195154e-04,3.53198216e-04,
 3.54758257e-04,3.55260572e-04,3.53820820e-04,3.56441494e-04,
 3.50128472e-04,3.63027674e-04,3.48098234e-04,3.76590381e-04,
 3.63494597e-04,3.67215950e-04,3.67803563e-04,2.63563593e-04,
 1.68758147e-04,2.23296400e-04,5.53101824e-05])
options['control_alpha_i'] = np.array([ 1.60894540e-01,-1.57079624e+00,-1.09488801e-01, 2.77842948e-02,
  1.94671517e-01, 1.10169965e-01, 8.94495051e-02, 6.89790111e-02,
  5.51394578e-02, 4.70934917e-02, 3.62948126e-02, 3.23508932e-02,
  2.64056416e-02, 1.82755813e-02, 2.37945024e-02, 4.54838152e-03,
  1.46445850e-02, 4.41134821e-03, 3.97321196e-03,-4.23597470e-05,
 -2.98443014e-03,-3.63170771e-03,-6.10243917e-03,-7.54690549e-03,
 -7.69307416e-03,-9.01216302e-03,-9.13575577e-03,-9.26989676e-03,
 -8.99976665e-03,-8.71367140e-03,-8.91691071e-03,-8.94202907e-03,
 -8.53789725e-03,-8.37144459e-03,-8.44433332e-03,-8.69858009e-03,
 -8.57667823e-03,-8.32378644e-03,-9.35653480e-03,-1.03295555e-02,
 -1.00255504e-02,-9.47266859e-03,-1.56154471e-03, 1.83962214e-03,
  2.74345433e-02,-9.63513992e-03, 3.65392485e-02])
