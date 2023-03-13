import numpy as np


# aircraft and mission parameter definitions
options = {} # aircraft and mission parameter dictionary

# aircraft data
options['mass'] = 3000 # (kg)
options['wing_area'] = 19.6 # (m^2)
options['max_cruise_power'] = 468300 # (w)
options['max_lift_power'] = 133652 # 103652 (w)
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
options['v_0'] = 0.625 # 4 (m/s)
options['gamma_0'] = 0 # (rad)
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

# set the initial integrator timestep
# options['dt'] = 2.95548274 #2.90903366 # 3.5

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

# min e seed new ode
options['dt'] = 2.15999432
options['control_x_i'] = np.array([1478.49611216,1480.98178811,1529.61277261,1573.22831274,1605.33023483,
 1630.98581331,1325.68386461,1287.46910033,1339.86743696,1263.6562584 ,
 1251.32535487,1241.39490916,1212.17821459,1204.65166484,1199.24128993,
 1186.5037763 ,1190.63105459,1193.85537146,1195.69973551,1196.65021426,
 1199.04350553,1200.86596124,1201.85349357,1202.13528782,1202.52075349,
 1203.72357223,1205.51812862,1207.28826333,1208.69326616,1209.64616944,
 1209.92608225,1208.74462395,1204.64875896,1195.3825217 ,1178.85084849,
 1149.08723753,1106.09261556,1024.90212253,1037.64371144, 665.06722568])
options['control_z_i'] = np.array([1.12996275e+03,1.03291990e+03,1.10774032e+03,7.87463530e+02,
 7.38730531e+02,4.98149648e+02,9.42650213e+01,9.09921098e-14,
 1.03100208e+01,5.81990551e-01,1.00975439e-03,1.82794555e-03,
 1.99846882e-04,4.84163052e-04,4.99547738e-04,4.22227666e-04,
 5.72542284e-04,5.28382585e-04,6.57981121e-04,6.30165102e-04,
 6.65704540e-04,6.72547897e-04,6.78140703e-04,6.78543610e-04,
 6.77427651e-04,6.73575235e-04,6.72091758e-04,6.70816729e-04,
 6.61888690e-04,6.42643649e-04,6.17300104e-04,5.90248487e-04,
 5.63600334e-04,5.37170528e-04,5.04523290e-04,4.80961544e-04,
 4.22227264e-04,4.69403469e-04,5.58653981e-04,0.00000000e+00])
options['control_alpha_i'] = np.array([ 2.00489587e-19,-1.38948540e+00,-4.92507868e-01, 1.21928731e-01,
  1.60088633e-01, 1.67457851e-01, 1.06928339e-01, 8.45766132e-02,
  6.63405209e-02, 6.24369994e-02, 2.96994876e-02, 4.77539534e-02,
  1.58138088e-02, 1.69457624e-02, 1.57000891e-02, 7.65332356e-03,
  3.86478765e-03, 4.24245210e-04, 4.71990672e-03,-1.54203055e-03,
 -6.05797343e-03,-4.02878599e-03,-3.63357340e-03,-3.68309723e-03,
 -4.50940955e-03,-5.88538858e-03,-5.57637775e-03,-3.51755127e-03,
 -1.69293155e-03,-9.49276183e-04,-3.49339094e-04, 1.36294799e-03,
  4.75339048e-03, 8.62854176e-03, 1.13839880e-02, 1.61076942e-02,
  2.12016572e-02, 3.06008921e-02,-2.59336189e-02, 3.65392444e-02])

"""
# min e seed (nominal)
options['control_x_i'] = np.array([1.47855031e-15,2.50470577e+02,1.56047951e+03,1.54602870e+03,
 1.18254133e+03,1.15148779e+03,1.08226472e+03,1.06061702e+03,
 1.04237249e+03,1.03502324e+03,1.03164771e+03,1.03156371e+03,
 1.03218558e+03,1.03629692e+03,1.03481931e+03,1.04723080e+03,
 1.04216775e+03,1.04570747e+03,1.04613593e+03,1.04693095e+03,
 1.04785350e+03,1.04863823e+03,1.04950639e+03,1.05032760e+03,
 1.05118870e+03,1.05205102e+03,1.05291187e+03,1.05364504e+03,
 1.05465023e+03,1.05539487e+03,1.05624950e+03,1.05718247e+03,
 1.05794571e+03,1.05870443e+03,1.06002567e+03,1.06053371e+03,
 1.06017716e+03,1.04807614e+03,1.00207247e+03,9.36016407e+02])
options['control_z_i'] = np.array([9.32201132e+02,7.68225214e+02,1.02776660e+03,6.32744588e+02,
 2.88034635e+02,2.35413135e+02,1.62301078e+02,7.02325290e+01,
 0.00000000e+00,3.19059568e-03,5.70548583e-03,1.89369080e-04,
 1.39318668e-03,5.03293468e-04,4.35137170e-04,7.72917245e-04,
 3.92763945e-04,4.53820702e-04,4.27047731e-04,4.44222146e-04,
 4.39462749e-04,4.43954202e-04,4.46175223e-04,4.48897304e-04,
 4.50883895e-04,4.52379153e-04,4.54867841e-04,4.58387355e-04,
 4.60284546e-04,4.60813039e-04,4.66497505e-04,4.66642724e-04,
 4.69830355e-04,4.71493517e-04,4.77024341e-04,4.75439890e-04,
 7.33346115e-04,1.18332465e-03,4.43222087e-04,0.00000000e+00])
options['control_alpha_i'] = np.array([ 8.51785733e-23, 1.57079633e+00, 2.84553121e-01, 1.64025297e-01,
  1.19794358e-01, 1.04622789e-01, 8.68016900e-02, 7.45562613e-02,
  6.25764140e-02, 5.17703598e-02, 4.23677829e-02, 3.41640734e-02,
  2.61828862e-02, 2.10738133e-02, 9.59328805e-03, 2.62518607e-02,
  6.26458766e-03, 9.18137422e-03, 7.84918763e-03, 8.64875976e-03,
  8.46212714e-03, 8.66907695e-03, 8.78466708e-03, 8.84180799e-03,
  9.01439034e-03, 9.10643512e-03, 9.18418746e-03, 9.31414258e-03,
  9.47230412e-03, 9.49110087e-03, 9.68236549e-03, 9.75153971e-03,
  9.88842002e-03, 9.94810972e-03, 1.01557764e-02, 1.04353727e-02,
  2.35793211e-02, 3.76341876e-02, 1.95703798e-02,-4.29344164e-02])
"""