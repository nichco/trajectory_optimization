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
options['dt'] = 4.11975845
options['control_x_i'] = np.array([1478.46115449,1470.10925412,1562.10905279,1591.39211652,1620.71694832,
 1222.52344219,1130.18735388,1058.99541098,1016.82168465, 978.55505587,
  948.98588448, 924.1583309 , 901.78114123, 883.89836611, 869.80140038,
  853.06603777, 843.0659189 , 837.01471622, 822.09687294, 822.60588068,
  812.67618177, 814.75534446, 803.33252653, 810.96531208, 805.13246131,
  810.43167314, 807.38603351, 809.76566938, 810.16772161, 810.6499241 ,
  811.77893695, 812.30724735, 813.12877112, 814.01286968, 814.71286412,
  815.56664069, 816.27369657, 816.75306621, 817.57147671, 817.6235195 ,
  818.59952304, 819.24051539, 825.72287246, 827.46491127, 822.04011844,
  750.94244555, 665.06721531])
options['control_z_i'] = np.array([1.13821917e+03,1.09446509e+03,1.12690496e+03,8.29571025e+02,
 3.37995298e+02,5.66047377e+01,4.39210431e-13,0.00000000e+00,
 2.79260465e-01,1.00518278e+00,7.76069533e-16,7.52788523e-03,
 9.53369801e-17,1.41179823e-02,1.22805115e-01,6.41379886e-01,
 4.52593028e-01,0.00000000e+00,1.39887898e-03,2.21744461e-03,
 2.86787025e-01,0.00000000e+00,6.33448075e-02,1.13759122e-02,
 0.00000000e+00,8.18492369e-02,0.00000000e+00,9.55876546e-04,
 5.80739234e-04,1.88527630e-04,5.16411321e-04,3.82985648e-04,
 3.66161572e-04,2.55238998e-04,3.75824665e-04,3.36522094e-04,
 3.51610526e-04,3.38129408e-04,3.95904537e-04,2.92982470e-04,
 3.97784093e-04,4.23260401e-04,2.54015112e-04,3.25710174e-04,
 2.08532422e-04,1.09107619e-04,3.27797101e-04])
options['control_alpha_i'] = np.array([ 1.90002106e-01,-1.57079633e+00,-1.06808973e-01, 9.95546301e-02,
  1.80328919e-01, 1.11537230e-01, 8.77137289e-02, 6.90088090e-02,
  5.57646803e-02, 4.53953358e-02, 3.69577038e-02, 2.99735312e-02,
  2.40801226e-02, 1.90318764e-02, 1.46264206e-02, 1.07969402e-02,
  7.41091238e-03, 4.33644710e-03, 1.61460261e-03,-8.72971619e-04,
 -3.20470446e-03,-5.11682965e-03,-8.05478906e-03,-4.71948298e-03,
 -9.86174493e-03,-8.93474880e-03,-8.84661732e-03,-8.95377788e-03,
 -9.04065615e-03,-9.01492466e-03,-9.01147869e-03,-9.03448037e-03,
 -8.86732783e-03,-8.75828845e-03,-8.81252198e-03,-8.55438294e-03,
 -8.53887935e-03,-8.74007720e-03,-9.09723190e-03,-1.00852592e-02,
 -1.02435221e-02,-9.37937393e-03,-3.40340583e-03, 2.91180094e-03,
  2.60424904e-02,-9.29974886e-03, 3.65392422e-02])