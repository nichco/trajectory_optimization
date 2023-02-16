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
options['v_0'] = 1.5 # 4 (m/s)
options['gamma_0'] = 0 # (rad)
options['h_0'] = 300 # (m)
options['min_h'] = 299.9 # (m)
options['x_0'] = 0 # (m)
options['alpha_0'] = 0 # (rad)
options['h_f'] = 300 # (m)
options['v_f'] = 58 # 43 (m/s)
options['vne'] = 70 # (m/s)
options['x_lim'] = 5000 # (m)
options['theta_0'] = 0 # (rad)
options['gamma_f'] = 0 # (rad)
options['max_g'] = 0.5 # (g)
options['max_dgamma'] = 0.5 # (rad/s)

# set the initial integrator timestep
options['dt'] = 1.78119483


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
# min dt seed (nominal) (converges from here)
options['control_x_i'] = np.array([2125.10451257,2128.22740825,2138.98203216,2153.99947746,2237.70658894,
 2245.6320373 ,2276.13933419,2279.80089705,2306.00549874,2323.1525011 ,
 2356.03764486,2375.65396978,2383.02309681,2404.55599069,2412.13836763,
 2417.1654391 ,2390.66092551,2431.4544577 ,2419.68558804,2411.35247524,
 2442.15742165,2348.80131579,2340.58372021,2434.73306808,2431.81460948,
 2403.85867832,2380.2409502 ,2317.98436098,2341.90075405,2344.85593879])
options['control_z_i'] = np.array([1.38419639e+03,1.41089046e+03,1.43011595e+03,1.44370813e+03,
 1.40020468e+03,1.40967237e+03,2.36324651e+02,0.00000000e+00,
 6.14692924e+01,1.35732341e+03,1.38201991e+03,1.37738355e+03,
 2.01414482e-13,0.00000000e+00,6.06725875e+01,5.18081169e+00,
 7.51542249e+01,2.57096218e+01,6.01631576e+01,0.00000000e+00,
 3.77703389e+00,8.24626537e+01,1.36995661e+03,1.36443527e+03,
 2.63253977e+02,0.00000000e+00,1.42508854e+00,7.51179569e+00,
 4.95918066e-01,0.00000000e+00])
options['control_alpha_i'] = np.array([ 1.26036173e-18, 1.04719755e+00, 1.04719755e+00, 9.94746980e-01,
  3.76819906e-01, 4.58801240e-01,-1.37896318e-01,-1.75723772e-01,
 -1.74893629e-01, 3.43015702e-01, 3.18934912e-01, 2.99079711e-01,
 -2.39721024e-01,-1.71224779e-03,-3.61508449e-03,-4.20819752e-03,
 -3.73232577e-03, 1.59761105e-03,-3.92617848e-03,-1.46307079e-02,
  6.52879430e-03,-1.64853013e-01, 2.53109259e-01, 2.19020757e-01,
 -3.73958992e-02,-3.25720775e-02,-7.34992469e-02,-1.05259183e-01,
 -2.00428763e-01,-1.67777799e-01])
"""


# min e seed (no dgamma)
options['control_x_i'] = np.array([2.43209089e+01,7.47367962e-14,1.33712622e+03,1.21176390e+03,
 1.59086245e+03,1.60752999e+03,1.38396312e+03,1.28468793e+03,
 1.19929599e+03,1.14596381e+03,1.10550707e+03,1.07275411e+03,
 1.04464066e+03,1.01952002e+03,9.96467657e+02,9.74756602e+02,
 9.53992602e+02,9.34260826e+02,9.15751968e+02,8.98382194e+02,
 8.82045778e+02,8.66555229e+02,8.51920953e+02,8.38111866e+02,
 8.24840072e+02,8.12054414e+02,7.99719323e+02,7.87765959e+02,
 7.76192858e+02,7.65000668e+02,7.54031278e+02,7.43264821e+02,
 7.32709409e+02,7.22343245e+02,7.12153792e+02,7.02180870e+02,
 6.92522050e+02,6.82928715e+02,6.73370254e+02,6.63671124e+02,
 6.54614483e+02,6.45283754e+02,6.36248797e+02,6.27118648e+02,
 6.18990135e+02])
options['control_z_i'] = np.array([1.03003651e+03,4.74248851e-15,1.01000621e+03,1.04759592e+03,
 9.31375716e+02,6.20909785e+02,4.74475762e+02,3.69113114e+02,
 3.06188350e+02,2.61526735e+02,2.17285278e+02,1.97697767e+02,
 1.78055007e+02,1.55525758e+02,1.28814727e+02,9.20615331e+01,
 5.10918711e+01,2.32732408e+01,5.09573869e+00,1.09323117e+00,
 4.01424538e-01,3.15271400e-02,9.45806509e-03,1.59785872e-03,
 8.41982307e-03,1.88815790e-02,2.54970538e-02,1.54686392e-02,
 2.81996785e-03,9.99330690e-04,9.25977370e-04,8.56230914e-04,
 8.11096398e-04,7.69387888e-04,7.32146893e-04,6.99848155e-04,
 6.71705844e-04,6.27907015e-04,6.22582479e-04,6.07262874e-04,
 5.55057009e-04,5.70859871e-04,5.53423762e-04,5.21706763e-04,
 5.83825243e-04])
options['control_alpha_i'] = np.array([-7.30768585e-22, 3.80342478e-01, 4.72244778e-01, 5.23168285e-01,
  2.24610892e-01, 1.72824740e-01, 1.52164006e-01, 1.36800245e-01,
  1.22761511e-01, 1.10857898e-01, 1.01905090e-01, 9.36105756e-02,
  8.66268055e-02, 8.05794295e-02, 7.57445426e-02, 7.17796892e-02,
  6.80113085e-02, 6.43744970e-02, 6.09758357e-02, 5.79601704e-02,
  5.52246767e-02, 5.27483970e-02, 5.06252067e-02, 4.84704923e-02,
  4.65602270e-02, 4.51179912e-02, 4.37296306e-02, 4.23770942e-02,
  4.11548426e-02, 4.01450365e-02, 3.92185250e-02, 3.84309467e-02,
  3.77403614e-02, 3.71552557e-02, 3.67076918e-02, 3.62449619e-02,
  3.59812790e-02, 3.57801248e-02, 3.56799240e-02, 3.56919235e-02,
  3.56194446e-02, 3.58942166e-02, 3.61532937e-02, 3.46399776e-02,
  3.94670144e-02])
