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
options['dt'] = 4.05948281
options['control_x_i'] = np.array([1478.46839177,1469.88371172,1561.30193842,1590.6517131 ,1621.02725978,
 1258.00635731,1136.14748068,1069.42239768,1012.62285566, 983.78951168,
  951.22861856, 918.07893348, 902.02278023, 891.31667097, 867.77763391,
  868.57036563, 847.29577691, 842.83376122, 830.96112606, 825.9796067 ,
  820.83511672, 816.25525442, 814.94215875, 811.47833568, 810.09559839,
  809.72238888, 810.42534428, 811.21304233, 812.09912366, 812.79303528,
  813.62782248, 814.51022796, 815.23106405, 815.80475138, 816.58646707,
  817.62711267, 818.53716115, 818.91296902, 819.30955833, 819.66902176,
  820.75434756, 819.74803248, 826.98838551, 830.72992529, 823.80509854,
  750.97519027, 665.06727011])
options['control_z_i'] = np.array([1.13818888e+03,1.09422547e+03,1.12652998e+03,8.92621611e+02,
 3.37422206e+02,6.49171589e+01,1.20335936e-14,3.52522818e-02,
 5.17012824e-02,1.10644975e-02,5.57893602e-04,8.81099543e-05,
 3.49938024e-04,2.78368562e-04,2.66875333e-04,3.53108037e-04,
 2.23079466e-04,3.34797144e-04,3.00553857e-04,2.74932631e-04,
 3.31353169e-04,3.25468045e-04,3.25589043e-04,3.35547256e-04,
 3.41446722e-04,3.44010914e-04,3.48076410e-04,3.51170734e-04,
 3.51005211e-04,3.50833691e-04,3.50781244e-04,3.52671278e-04,
 3.52560491e-04,3.52339689e-04,3.52050152e-04,3.50385570e-04,
 3.53707240e-04,3.48914421e-04,3.61919944e-04,3.50901201e-04,
 3.74057325e-04,3.68301192e-04,3.25907660e-04,3.34079419e-04,
 2.39506953e-04,3.33523160e-04,5.65272230e-05])
options['control_alpha_i'] = np.array([ 1.69192075e-01,-1.57079633e+00,-1.05241623e-01, 5.61499156e-02,
  1.93740981e-01, 1.11155226e-01, 8.81666989e-02, 6.88369811e-02,
  5.58035669e-02, 4.55632870e-02, 3.72141792e-02, 3.01760063e-02,
  2.46608480e-02, 1.94122134e-02, 1.45622733e-02, 1.35338040e-02,
  5.26571915e-03, 6.21023668e-03, 1.82630652e-03,-1.25958062e-03,
 -1.41789290e-03,-7.01514745e-03,-5.91688260e-03,-8.25085717e-03,
 -8.22605453e-03,-9.95720380e-03,-9.35977947e-03,-8.61935302e-03,
 -9.10453188e-03,-9.29488703e-03,-9.10336869e-03,-8.52415871e-03,
 -8.17966508e-03,-8.58292686e-03,-9.14590698e-03,-9.18702958e-03,
 -8.60954917e-03,-8.45990546e-03,-9.74782551e-03,-1.07150042e-02,
 -1.10234640e-02,-9.03643285e-03,-3.10362739e-03, 2.94956754e-03,
  2.58116793e-02,-9.57654706e-03, 3.65392539e-02])
