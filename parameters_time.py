import numpy as np


# aircraft and mission parameter definitions
options = {} # aircraft and mission parameter dictionary

# aircraft data
options['mass'] = 3000 # 2000 # (kg)
options['wing_area'] = 19.6 # (m^2)
options['max_cruise_power'] = 468300 # (w)
options['max_lift_power'] = 103652 # (w)
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
options['v_0'] = 4.0 # 5 (m/s)
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
options['dt'] = 1.28312198 #2.90903366 # 3.5


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


# min dt seed new
options['control_x_i'] = np.array([   0.        ,1307.40168411,1516.5430552 ,1538.61342446,1328.27031651,
 1331.25744652,1426.13716745,1540.23347467,1530.90769513,1565.61532661,
 1576.1612199 ,1620.30084214,1424.22175625,1638.08594085,1610.2070298 ,
 1657.74514554,1679.04396771,1664.5371417 ,1653.50300319,1649.68051638,
 1642.90411412,1634.13128874,1629.50830199,1627.3771433 ,1624.13765115,
 1619.76697162,1613.01294316,1605.67614925,1600.10654387,1597.57913434,
 1597.42309172,1598.05001782,1597.40306727,1593.67213517,1585.23165085,
 1570.18154091,1532.37929416,1438.24092753,1369.89609188, 665.13189557])
options['control_z_i'] = np.array([2.07518593e+02,1.02207493e+03,1.02770255e+03,1.02404243e+03,
 1.02736320e+03,8.65153358e+02,9.78904004e+02,5.87026193e+02,
 4.20919455e+02,1.23019351e+02,2.73149982e+01,5.02327182e+00,
 7.22015045e-01,7.47069515e-02,6.79159825e-03,1.58559818e-03,
 1.04027986e-03,7.90576702e-04,6.62548482e-04,5.66072896e-04,
 5.27008889e-04,5.02530034e-04,5.04221903e-04,5.11118448e-04,
 5.17303863e-04,5.21126540e-04,5.21636801e-04,5.19226870e-04,
 5.15363338e-04,5.10550682e-04,5.09672387e-04,5.18744359e-04,
 5.56856481e-04,6.51600581e-04,8.44117423e-04,1.20123390e-03,
 1.63758774e-03,1.49098735e-03,1.62849149e-04,6.15865984e-05])
options['control_alpha_i'] = np.array([-0.13658575, 0.13230763, 0.34215405, 0.20446883, 0.2824265 , 0.27523741,
  0.17719204, 0.10780268, 0.1549011 , 0.20669165, 0.23031927, 0.21383677,
  0.17101114, 0.12549587, 0.09973586, 0.08086334, 0.07092027, 0.06136904,
  0.0521369 , 0.04879677, 0.04541533, 0.03589271, 0.0335665 , 0.03290263,
  0.03308108, 0.03282447, 0.03231455, 0.03123888, 0.03055516, 0.02974734,
  0.03013394, 0.03095795, 0.03106198, 0.0328061 , 0.03313079, 0.03265378,
  0.02735088, 0.00619636,-0.0322839 , 0.03653921])


