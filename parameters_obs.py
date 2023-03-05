import numpy as np


# aircraft and mission parameter definitions
options = {} # aircraft and mission parameter dictionary

# aircraft data
options['mass'] = 3000 # 2000 # (kg)
options['wing_area'] = 19.6 # (m^2)
options['max_cruise_power'] = 468300 # (w)
options['max_lift_power'] = 143652 # # 153652 103652 (w)
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

"""
# min e seed new
options['dt'] = 3.27828625
options['control_x_i'] = np.array([1455.47114882,1481.50940364,1568.32831534,1649.56902759,1164.23241727,
 1023.14879517,1138.02440408,1029.36649619,1053.70196076,1022.62121658,
 1022.33430367,1014.41106476, 957.66687475,1008.629677  , 960.86096389,
  974.18273788, 972.33973326, 978.82100686, 979.83239284, 984.4227158 ,
  986.0700484 , 987.14202874, 988.027184  , 987.31477684, 989.18512231,
  991.61224896, 993.37904941, 993.76802555, 993.38771325, 993.53469214,
  995.55009605, 998.63047437, 998.99034351,1011.06175232,1013.66380348,
 1043.97000071,1035.52382631,1017.48057351, 965.84869369, 665.06721873])
options['control_z_i'] = np.array([1.16366111e+03,1.06992634e+03,7.29029956e+02,1.72828031e+02,
 1.33897771e+02,3.08623869e+02,1.88195257e+00,3.50154942e-01,
 0.00000000e+00,3.83813821e-01,1.47004264e-16,4.74897770e-03,
 2.27874877e-02,4.50940337e-01,5.20015789e-01,1.66742049e-01,
 6.47422839e-01,0.00000000e+00,5.71428162e-04,4.62084165e-04,
 7.09036129e-04,3.72598036e-04,3.74174691e-04,6.29246750e-04,
 5.33898701e-04,4.29546162e-04,4.77425069e-04,3.61335002e-04,
 2.75303908e-04,4.34238809e-04,5.82816838e-04,5.10037982e-04,
 5.05312171e-04,6.40710114e-04,2.94049127e-04,8.16790708e-05,
 3.85242581e-04,4.48142364e-04,2.78526873e-04,1.95779344e-04])
options['control_alpha_i'] = np.array([-6.22608504e-02,-1.03415819e+00, 1.53748352e-01, 1.71827656e-01,
  9.41864240e-02,-1.16764787e-03, 8.55299121e-02, 2.74027989e-02,
  4.19837748e-02, 1.01431937e-02, 2.33097295e-02, 2.65461621e-02,
 -2.55682836e-02, 2.67972214e-02,-1.21573865e-02, 1.35633867e-03,
 -1.12505445e-02,-3.07333010e-03,-3.38593654e-03,-1.31881663e-02,
 -7.41653665e-03,-6.47829262e-03,-5.98360921e-03,-4.22186533e-03,
 -7.16748791e-03,-9.91575923e-03,-7.56403434e-03,-4.65321176e-03,
 -4.91751084e-03,-7.45393434e-03,-1.14285075e-02,-9.30573991e-03,
 -6.65074968e-03,-7.92602832e-03, 8.14200596e-04, 5.08570873e-03,
  9.71905663e-03, 2.80925794e-02,-1.78327554e-02, 3.65392466e-02])
"""


# min e seed OBS!
options['dt'] = 3.91994631
options['control_x_i'] = np.array([1478.47520795,1470.97039742,1563.66819359,1600.74129178,1588.03418327,
 1170.8564189 ,1111.84844094,1038.92205935,1021.63705118, 990.93771119,
  964.59928187, 935.22210475, 908.79685998, 890.83540709, 892.86361101,
  865.2173124 , 870.47215129, 857.27489236, 847.26249263, 844.6908183 ,
  838.11131043, 839.46613771, 838.46984546, 840.00944521, 841.0774477 ,
  842.22808878, 843.11598511, 843.98436501, 844.61818923, 845.31314071,
  846.11216288, 846.85948098, 847.7149867 , 848.27897421, 848.96051001,
  850.34135723, 849.48293741, 853.21693923, 850.35017088, 855.83340431,
  861.12406521, 851.14422556, 837.01778698, 762.55190795, 665.0672268, 762.55190795, 665.0672268 ])
options['control_z_i'] = np.array([1.13815629e+03,1.09433251e+03,1.12318843e+03,7.41069951e+02,
 2.44116777e+02,3.68822759e+01,3.71020683e+00,4.39875508e-16,
 5.12587985e-01,0.00000000e+00,6.75591124e-04,1.93087332e-04,
 8.78689149e-17,1.99050613e-03,1.14455333e-02,1.09366668e-04,
 1.06057972e-03,2.25459094e-04,7.83021232e-05,4.02786038e-04,
 3.52469807e-04,3.52412748e-04,3.67777997e-04,3.66897438e-04,
 3.68422404e-04,3.74897812e-04,3.70988257e-04,3.71168082e-04,
 3.74225957e-04,3.73211708e-04,3.75651239e-04,3.71657262e-04,
 3.75285903e-04,3.75283999e-04,3.74373529e-04,3.80416867e-04,
 3.61361578e-04,3.95225635e-04,3.28905163e-04,3.95138377e-04,
 2.71133612e-04,2.67000996e-04,2.98651869e-04,7.46326637e-05,
 2.54411306e-05,7.46326637e-05,
 2.54411306e-05])
options['control_alpha_i'] = np.array([ 1.46881770e-01,-1.55365575e+00,-1.49300066e-01, 1.62306193e-01,
  1.41588079e-01, 9.89678120e-02, 7.90541610e-02, 6.27843894e-02,
  5.14557138e-02, 4.18746390e-02, 3.28378079e-02, 2.66443064e-02,
  2.09149329e-02, 1.61091219e-02, 1.30591203e-02, 7.12189394e-03,
  5.23955500e-03, 1.85279278e-03,-3.09811588e-04,-5.28034007e-03,
 -5.21527407e-03,-6.11889260e-03,-7.95228376e-03,-8.62290778e-03,
 -9.09505596e-03,-8.66144663e-03,-8.39383050e-03,-8.36956127e-03,
 -8.24839122e-03,-8.12126652e-03,-7.99998025e-03,-7.95744370e-03,
 -7.89380139e-03,-8.01985506e-03,-8.05089904e-03,-8.42508467e-03,
 -8.96289267e-03,-8.83457858e-03,-8.76354193e-03,-6.67979781e-03,
  4.84353509e-04, 4.23834121e-03, 2.78188186e-02,-6.39861394e-03,
  3.65392446e-02,-6.39861394e-03,
  3.65392446e-02])
