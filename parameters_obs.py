import numpy as np


# aircraft and mission parameter definitions
options = {} # aircraft and mission parameter dictionary

# aircraft data
options['mass'] = 3000 # 2000 # (kg)
options['wing_area'] = 19.6 # (m^2)
options['max_cruise_power'] = 468300 # (w)
options['max_lift_power'] = 153652 # # 153652 103652 (w)
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
options['p_f'] = 10000 # (m) end of obstacle
options['obs_height'] = 50 # (m)


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
options['dt'] = 3.5
options['control_x_i'] = np.array([ 943.84504103,1522.82023028,1090.13984014,1603.48428355,1217.10932801,
 1203.68412228,1141.70676267,1103.59181713,1069.45580492,1048.36088668,
 1024.84402643,1012.62534401, 999.08455569, 992.52738473, 985.03475481,
  984.62627471, 982.17890855, 982.21328671, 983.3463579 , 984.50705356,
  985.31488428, 986.26849339, 986.7205268 , 987.83186358, 989.02478117,
  990.2825595 , 991.24895045, 992.14205293, 993.18442942, 994.54812018,
  995.58556823, 995.94815575, 994.87196674, 993.15999175, 983.89928604,
  971.70212494, 928.29350263, 892.62350456, 801.082526  , 665.06725471])
options['control_z_i'] = np.array([1.16363004e+03,2.81044297e+02,1.17781449e+03,4.37408087e+02,
 2.50391433e+02,1.16470798e+02,1.56327506e+02,4.00923118e+01,
 6.79340344e+00,2.46895997e-01,6.59383303e-16,1.88162510e-04,
 9.94244462e-05,9.41742387e-04,3.33368563e-06,6.37835254e-04,
 2.99455251e-05,3.77145763e-04,2.97873615e-04,2.94119862e-04,
 2.98681335e-04,3.04843089e-04,3.04295910e-04,2.99419419e-04,
 3.11248394e-04,3.07321644e-04,3.15484557e-04,3.14668544e-04,
 3.21221087e-04,3.34833713e-04,3.37441523e-04,3.71077855e-04,
 3.78386216e-04,5.00021340e-04,3.91230642e-04,9.92899987e-04,
 0.00000000e+00,4.31422211e-03,4.98640220e-04,0.00000000e+00])
options['control_alpha_i'] = np.array([-5.00000000e-02,-3.20250549e-02, 3.69706081e-01, 9.07986189e-02,
  1.17752041e-01, 8.27624058e-02, 6.50604468e-02, 5.13925029e-02,
  4.11392483e-02, 3.13904210e-02, 2.17044275e-02, 1.68866903e-02,
  9.33632209e-03, 5.07229837e-03, 2.87980191e-04,-1.66141270e-03,
 -3.52142336e-03,-5.54646448e-03,-6.96387774e-03,-6.99926638e-03,
 -6.95851356e-03,-6.88384049e-03,-6.87389454e-03,-6.58964809e-03,
 -6.49652027e-03,-6.89831759e-03,-6.94787836e-03,-6.26055318e-03,
 -6.11833243e-03,-6.46173432e-03,-6.05137861e-03,-4.93405027e-03,
 -4.02132571e-03,-1.27169098e-03, 1.71423888e-03, 9.42926170e-03,
  9.39944377e-03, 3.17255319e-02, 1.27994763e-03, 3.65392507e-02])
"""