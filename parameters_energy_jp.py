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
options['dt'] = 1.78045488 #1.78123594


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


# min dt seed (dtheta)
options['control_x_i'] = np.array([  59.81468989,   0.        ,1270.45466324, 576.04668946, 718.55015595,
  906.01631796, 887.9990607 , 889.42633488, 917.92412502, 954.22352812,
  985.03125472,1007.1943143 ,1023.35664195,1030.87530915,1033.97679859,
 1033.55996113,1029.94045782,1024.61407476,1018.53977015,1013.19888084,
 1008.45649107,1005.1053121 ,1003.76289165,1002.16487413,1000.46802223,
  998.24473893, 994.52490539, 988.03063625, 981.35226658, 971.32502164,
  958.15533341, 942.28406901, 923.81639262, 903.50386333, 881.38710858,
  857.33769252, 832.0355857 , 804.41625478, 773.34104449, 739.77905693,
  702.17543416, 663.47983646, 611.94947897, 589.6626939 , 647.75485573])
options['control_z_i'] = np.array([1.03049959e+03,0.00000000e+00,9.55689806e+02,9.56921234e+02,
 8.17595159e+02,7.10469360e+02,4.04602084e+02,2.35305046e+02,
 9.28010041e+01,2.90115545e+01,1.21610707e-01,4.13973459e-02,
 8.65984116e-02,0.00000000e+00,1.56835375e-01,6.89436775e-18,
 0.00000000e+00,2.89305219e-03,4.30813507e-04,9.78715172e-05,
 7.71034596e-04,2.76865792e-04,8.40022651e-05,7.12228689e-05,
 5.17681071e-04,1.52972744e-05,1.44945379e-03,2.02406636e-05,
 5.62974387e-04,1.22270694e-04,7.85488441e-04,1.60391056e-04,
 1.19536152e-03,8.90887105e-05,1.67238151e-03,1.63322783e-04,
 1.13944472e-03,3.03890374e-04,7.60454783e-05,4.78541065e-03,
 5.87436158e-05,1.75662210e-17,2.66683321e-02,1.62279361e-05,
 2.61547694e-04])
options['control_alpha_i'] = np.array([ 1.05762460e-20, 7.20728801e-02, 1.27847963e-01, 2.77701841e-01,
  3.02254521e-01, 2.72558966e-01, 2.10698321e-01, 1.44970913e-01,
  1.00648255e-01, 7.77217720e-02, 6.03787071e-02, 4.62568056e-02,
  3.52152221e-02, 2.71616460e-02, 2.02737469e-02, 1.45943142e-02,
  1.00189810e-02, 6.40826843e-03, 3.69410101e-03, 1.71244324e-03,
  4.01531822e-04,-3.58835370e-04,-6.75851006e-04,-5.79843935e-04,
 -2.25784697e-04, 2.17008279e-04, 7.47550571e-04, 1.37190835e-03,
  2.84004429e-03, 4.34324909e-03, 5.86306984e-03, 7.40666074e-03,
  9.01581065e-03, 1.07068659e-02, 1.24959341e-02, 1.43942876e-02,
  1.64193991e-02, 1.85762223e-02, 2.08901506e-02, 2.33810941e-02,
  2.60697921e-02, 2.89846385e-02, 3.04219670e-02, 2.09272924e-02,
  3.75264597e-02])


"""
# min e seed (no dtheta)
options['control_x_i'] = np.array([2.41527817e+01,5.73991623e-03,1.34056542e+03,1.21318705e+03,
 1.59087671e+03,1.60700745e+03,1.38417831e+03,1.28411808e+03,
 1.19985926e+03,1.14577927e+03,1.10599203e+03,1.07262836e+03,
 1.04469091e+03,1.01917498e+03,9.97074973e+02,9.74978972e+02,
 9.53876431e+02,9.34552602e+02,9.15782149e+02,8.97836928e+02,
 8.81722315e+02,8.67014631e+02,8.52595204e+02,8.37309061e+02,
 8.24484962e+02,8.12562913e+02,7.99631437e+02,7.86761994e+02,
 7.76690222e+02,7.64772705e+02,7.53573412e+02,7.43566742e+02,
 7.32981475e+02,7.23001065e+02,7.12053490e+02,7.01700849e+02,
 6.92719306e+02,6.82970328e+02,6.73254870e+02,6.63259694e+02,
 6.53150261e+02,6.46371671e+02,6.36155061e+02,6.26134931e+02,
 6.19762644e+02])
options['control_z_i'] = np.array([1.03003895e+03,2.78803253e-04,1.00957095e+03,1.04743052e+03,
 9.30593879e+02,6.21422254e+02,4.74124316e+02,3.68826965e+02,
 3.06379014e+02,2.61215415e+02,2.18302741e+02,1.96795675e+02,
 1.78621135e+02,1.54049024e+02,1.28540887e+02,9.08392878e+01,
 5.06116440e+01,2.21547685e+01,6.32219393e+00,4.87649650e-01,
 1.19115317e+00,3.39182164e-01,7.88473292e-01,8.59452594e-01,
 2.97337341e-01,4.47088959e-01,3.24674759e-01,7.99912706e-02,
 5.76083374e-01,2.75458137e-02,1.36030322e+00,9.34471057e-02,
 8.22004315e-01,2.70924626e-01,1.07509701e+00,1.42988094e+00,
 1.09450552e+00,2.41451663e-02,4.01833232e-02,5.53728044e-01,
 3.74024945e-11,2.25679126e-01,1.40677518e+00,9.64359103e-06,
 1.09522165e-01])
options['control_alpha_i'] = np.array([2.73353881e-23,3.80654849e-01,4.72370213e-01,5.22531494e-01,
 2.24353581e-01,1.72919089e-01,1.52159935e-01,1.36787180e-01,
 1.22707894e-01,1.10820852e-01,1.02001656e-01,9.35018400e-02,
 8.64929541e-02,8.06707844e-02,7.57771271e-02,7.17585594e-02,
 6.79462320e-02,6.43681660e-02,6.09912261e-02,5.78636244e-02,
 5.52367338e-02,5.27152288e-02,5.04327434e-02,4.85202533e-02,
 4.66818057e-02,4.50045202e-02,4.37083535e-02,4.23558098e-02,
 4.11095523e-02,4.01344749e-02,3.92069065e-02,3.84260408e-02,
 3.76966939e-02,3.72402858e-02,3.66141049e-02,3.62389816e-02,
 3.61305770e-02,3.56504883e-02,3.57175817e-02,3.56303337e-02,
 3.57089557e-02,3.58030444e-02,3.62195277e-02,3.45905814e-02,
 3.96176672e-02])
"""