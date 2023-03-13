import numpy as np


# aircraft and mission parameter definitions
options = {} # aircraft and mission parameter dictionary

# aircraft data
options['mass'] = 3000 # 2000 # (kg)
options['wing_area'] = 19.6 # (m^2)
options['max_cruise_power'] = 468300.0 # (w)
options['max_lift_power'] = 103652.0 # (w)
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
options['v_0'] = 1.45 # 1.45 (m/s)
options['gamma_0'] = 0 # (rad)
options['h_0'] = 300 # (m)
options['min_h'] = 0.0 # 299.9(m)
options['x_0'] = 0 # (m)
options['alpha_0'] = 0 # (rad)
options['h_f'] = 300 # (m)
options['v_f'] = 58 # 43 (m/s)
options['vne'] = 70 # (m/s)
#options['x_lim'] = 5000 # (m)
options['theta_0'] = 0.0 # (rad)
options['gamma_f'] = 0.0 # (rad)
options['max_g'] = 0.5 # (g)

# set the initial integrator timestep
options['dt'] = 1.73855297


"""
print(np.array2string(sim['control_x'],separator=','))
print(np.array2string(sim['control_z'],separator=','))
print(np.array2string(sim['control_alpha'],separator=','))
"""

# min e seed (no dtheta)
options['control_x_i'] = np.array([   4.84957043, 549.77233204,1520.78051239,1551.26557337,1574.58227571,
 1597.56172793,1334.10071667, 851.93398385, 947.50217037,1069.02319858,
 1096.64476191,1106.8895996 ,1113.20691323,1117.9215256 ,1120.04901544,
 1119.72714903,1116.31300859,1111.25679359,1104.86067758,1097.61529023,
 1088.13537261,1074.10460569,1058.73892452,1041.53684946,1025.12408642,
 1007.36597365, 991.97896617, 976.90576232, 963.44621212, 949.81698386,
  929.53380644, 906.56741053, 883.76883155, 856.86269518, 825.73871278,
  787.36378772, 744.6504969 , 700.68810867, 652.89451629, 601.32613833,
  545.5187396 , 473.97352424, 438.20373243, 247.89913008, 665.06720824])
options['control_z_i'] = np.array([1.03002830e+03,4.56059130e-01,6.13702708e+02,1.03828403e+03,
 9.77813693e+02,6.24273770e+02,3.42650675e+02,4.37631059e+01,
 4.96144639e+00,7.42897560e-16,1.68444993e-02,1.22815433e-02,
 6.38517492e-02,2.61253972e-01,9.86470971e-04,1.35002677e+00,
 1.17893175e+00,1.77147768e+00,9.67970323e-01,9.85795918e-02,
 1.58463651e-15,3.12527028e-16,4.32974699e-02,1.22540959e-01,
 1.46350083e-01,1.13236073e-01,4.07058807e-02,6.64671693e-17,
 3.99799533e-01,5.56400518e-02,1.82536777e-01,1.05319629e-01,
 6.24943000e-02,7.14065905e-02,2.38014262e-01,1.66061435e-02,
 5.28656211e-05,2.18266919e-05,1.90366296e-01,8.60489248e-01,
 3.03622896e-03,0.00000000e+00,1.49389385e-01,2.37614107e-03,
 4.33392128e-16])
options['control_alpha_i'] = np.array([ 9.67263366e-19,-6.53109650e-02,-6.27348351e-02, 3.04760257e-01,
  2.32646394e-01, 2.16463993e-01, 2.29865185e-01, 2.05859254e-01,
  1.45959766e-01, 9.49513322e-02, 7.00113617e-02, 5.38190905e-02,
  4.18130367e-02, 3.26675046e-02, 2.51402263e-02, 1.94711636e-02,
  1.49479486e-02, 1.04372162e-02, 1.14214126e-02, 6.04463139e-03,
  2.61362719e-03, 3.91104719e-03, 2.35248231e-03, 3.04284475e-03,
  1.46250423e-03, 2.20817718e-03, 3.15145998e-03, 3.37996666e-03,
  4.27525719e-03, 4.90261667e-03, 5.75260738e-03, 6.59770285e-03,
  7.73605418e-03, 9.47766780e-03, 1.06949259e-02, 1.18834703e-02,
  1.37014737e-02, 1.60553857e-02, 1.83447840e-02, 2.10265823e-02,
  2.36380664e-02, 2.69370146e-02, 2.87282820e-02, 2.51714803e-02,
  3.65392420e-02])
