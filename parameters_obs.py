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
options['obs_height'] = 5 # (m)


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
options['dt'] = 3.5
options['control_x_i'] = np.array([1333.24873126,1526.23528821,1602.08971599,1566.14236028,1111.6369479 ,
 1188.51681746,1103.28462658,1055.30066479, 993.74429015, 985.12137927,
  978.53841347, 981.82176596, 983.40232811, 986.28034813, 981.01448742,
  981.74678422, 979.23591143, 980.26659446, 980.64688186, 982.26318698,
  982.52683415, 982.63243483, 984.46669228, 985.2596369 , 985.64353844,
  986.38319117, 986.57590452, 987.16830244, 988.12770248, 989.07132884,
  988.75325513, 987.77618327, 985.48808167, 979.34116115, 961.80433145,
  943.21223465, 897.62423116, 844.50986769, 780.94831418, 665.06720786])
options['control_z_i'] = np.array([1.15987535e+03,1.04557807e+03,8.00602250e+02,6.87492404e+01,
 1.90634305e-01,1.25979859e+00,2.69568560e-01,3.94381481e+00,
 5.67041294e-01,0.00000000e+00,1.28127943e-03,3.65673044e-04,
 4.33816482e-03,2.04707321e-01,2.42526131e-01,2.85442659e-01,
 4.13368573e-01,9.59182436e-03,6.11653556e-04,5.70273621e-04,
 7.33105465e-04,5.19508849e-04,5.49104938e-04,7.55172514e-04,
 6.68604769e-04,5.19991114e-04,4.71874828e-04,3.76182167e-04,
 4.06199615e-04,4.89080254e-04,7.50715702e-04,7.62097983e-04,
 7.21647816e-04,6.68846142e-04,4.11663231e-04,2.03598671e-04,
 4.62933513e-04,6.12876559e-04,1.12116341e-06,4.30040141e-04])
options['control_alpha_i'] = np.array([-1.54418068e-01,-7.39780880e-01, 1.74531220e-01, 1.70128914e-01,
  6.18137812e-02, 5.37154322e-02, 4.67732622e-02, 3.08427315e-02,
  2.41252823e-02, 1.98235512e-02, 9.15753916e-03, 9.69532516e-03,
  2.68349890e-05, 2.09267584e-04,-2.20003029e-03,-6.20211616e-03,
 -4.40247546e-03,-1.00412381e-02,-8.34396255e-03,-5.36276248e-03,
 -7.77382075e-03,-9.18117719e-03,-7.61275831e-03,-6.45375103e-03,
 -6.72650973e-03,-7.44576779e-03,-7.22107786e-03,-6.58742450e-03,
 -5.94042399e-03,-5.79814342e-03,-5.95432726e-03,-5.04171716e-03,
 -2.97356149e-03, 6.44548410e-04, 1.54752588e-03, 1.03656349e-02,
  9.56869052e-03, 3.27145605e-02, 4.72518390e-03, 3.65392406e-02])


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