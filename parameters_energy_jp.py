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
options['max_dgamma'] = 1.8 # (rad/s)

# set the initial integrator timestep
options['dt'] = 1.7698738


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
options['control_x_i'] = np.array([2.82189530e+01,6.94923103e-16,1.31263032e+03,1.22082433e+03,
 1.59037811e+03,1.61162349e+03,1.38770080e+03,1.28814161e+03,
 1.20208709e+03,1.14830468e+03,1.10752001e+03,1.07446623e+03,
 1.04631502e+03,1.02121956e+03,9.98063760e+02,9.76284813e+02,
 9.55539344e+02,9.35865953e+02,9.17392735e+02,9.00054699e+02,
 8.83726744e+02,8.68220161e+02,8.53561852e+02,8.39819278e+02,
 8.26591942e+02,8.13838055e+02,8.01508468e+02,7.89558165e+02,
 7.77979087e+02,7.66762914e+02,7.55789995e+02,7.45061232e+02,
 7.34547341e+02,7.24231191e+02,7.14099227e+02,7.04122144e+02,
 6.94425039e+02,6.84844576e+02,6.75382389e+02,6.65941958e+02,
 6.56777916e+02,6.47424710e+02,6.38466727e+02,6.29136927e+02,
 6.21441221e+02])
options['control_z_i'] = np.array([1.02871427e+03,6.48839250e-15,1.02696529e+03,1.04087569e+03,
 9.35943599e+02,6.25555079e+02,4.77945555e+02,3.72398066e+02,
 3.08485046e+02,2.63823472e+02,2.19627710e+02,1.98300132e+02,
 1.79443510e+02,1.57289862e+02,1.31308586e+02,9.61605384e+01,
 5.60230304e+01,2.60807175e+01,7.15896651e+00,2.97658151e-03,
 4.24853429e-03,3.60342709e-03,2.23976678e-03,2.05672531e-03,
 1.67027785e-03,1.44584507e-03,1.31413876e-03,1.17313342e-03,
 1.07306347e-03,9.97215773e-04,9.23284728e-04,8.68710517e-04,
 8.19606731e-04,7.77894807e-04,7.40846498e-04,7.08611953e-04,
 6.80466017e-04,6.55698891e-04,6.33484992e-04,6.13346915e-04,
 5.96524987e-04,5.81463665e-04,5.69813433e-04,5.27716877e-04,
 5.91041701e-04])
options['control_alpha_i'] = np.array([-1.70000482e-21, 3.80049293e-01, 4.72000694e-01, 5.28852772e-01,
  2.25771014e-01, 1.73680164e-01, 1.52695542e-01, 1.37380247e-01,
  1.23263426e-01, 1.11386038e-01, 1.02581324e-01, 9.40551554e-02,
  8.69820623e-02, 8.10848682e-02, 7.62108087e-02, 7.20775072e-02,
  6.83780933e-02, 6.48078697e-02, 6.13902487e-02, 5.83140480e-02,
  5.55589046e-02, 5.30826752e-02, 5.08517220e-02, 4.88403855e-02,
  4.70148971e-02, 4.53904086e-02, 4.39273044e-02, 4.25937291e-02,
  4.14287016e-02, 4.03825281e-02, 3.94586427e-02, 3.86560181e-02,
  3.79581838e-02, 3.73458962e-02, 3.68531792e-02, 3.64754373e-02,
  3.61592146e-02, 3.59056749e-02, 3.57891615e-02, 3.57428044e-02,
  3.57671384e-02, 3.58995648e-02, 3.62295486e-02, 3.47375047e-02,
  3.93612238e-02])
