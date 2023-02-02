import numpy as np


# aircraft and mission parameter definitions
options = {} # aircraft and mission parameter dictionary

# aircraft data
options['mass'] = 2400 # (kg)
options['wing_area'] = 19.6 # 19.6(m^2)
options['max_cruise_power'] = 468300 # (w)
options['max_lift_power'] = 103652 # (w)
options['cruise_rotor_diameter'] = 2.6 # 2.6(m)
options['lift_rotor_diameter'] = 2.3 # 2.4(m)
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
options['v_0'] = 5.0 # 5 (m/s)
options['gamma_0'] = 0 # (rad)
options['h_0'] = 0 # (m)
options['min_h'] = -0.1 # (m)
options['x_0'] = 0 # (m)
options['alpha_0'] = 0 # (rad)
options['h_f'] = 300 # (m)
options['v_f'] = 58 # 43 (m/s)
options['vne'] = 65 # (m/s)
options['x_lim'] = 5000 # (m)
options['theta_0'] = 0 # (rad)
options['gamma_f'] = 0 # (rad)

# set the initial integrator timestep
options['dt'] = 0.96327856


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


# min dt seed (nominal) (converges from here)
options['control_x_i'] = np.array([1491.25970586,1508.1514948 ,1504.96711113,1528.00678016,1568.15994051,
 1583.73443633,1594.66708841,1613.37100997,1634.49442679,1652.74147081,
 1663.21868257,1668.76048096,1685.07707392,1707.61444838,1736.04168586,
 1755.23773379,1758.40945528,1746.58997789,1746.74810105,1751.36944399,
 1761.00919815,1783.49855856,1789.11078189,1779.77495368,1758.23629797,
 1744.43851518,1734.8270452 ,1729.03388491,1727.81642331,1732.33621659])
options['control_z_i'] = np.array([1.18329900e+03,1.18879303e+03,1.21685651e+03,1.21840368e+03,
 1.19040020e+03,5.44898056e+02,2.90911031e+02,5.49863972e+02,
 1.16364227e+03,1.15919707e+03,7.35172367e+02,0.00000000e+00,
 1.95436342e-14,1.59441060e+01,1.13568521e+03,1.12959956e+03,
 1.12798511e+03,2.98409707e-15,5.29394121e+00,4.68535150e-14,
 2.96969751e-15,1.12421725e+03,1.12536179e+03,1.12885066e+03,
 9.92780682e+01,0.00000000e+00,1.63498240e-01,5.92054243e-01,
 4.53647477e-01,1.98904750e-01])
options['control_alpha_i'] = np.array([ 0.34132507, 0.464158  , 0.96116162, 0.76330166, 0.32258762,-0.04471297,
 -0.01638625,-0.0016748 , 0.113615  , 0.11086172,-0.00605989,-0.09398812,
 -0.07042687,-0.09124747, 0.08558684, 0.07563141, 0.06058521,-0.1097711 ,
 -0.08271594,-0.08561243,-0.11576332, 0.05177854, 0.06927741, 0.06557895,
 -0.09125542,-0.07369413,-0.06137401,-0.06173992,-0.07179243,-0.08868225])


"""
# min e seed (nominal)
options['control_x_i'] = np.array([2.83750361e-16,2.50327847e+02,1.56048322e+03,1.54607247e+03,
 1.18247178e+03,1.15145795e+03,1.08224617e+03,1.06062299e+03,
 1.04238537e+03,1.03496031e+03,1.03164408e+03,1.03129258e+03,
 1.03243549e+03,1.03550668e+03,1.03599478e+03,1.04546735e+03,
 1.04303554e+03,1.04540663e+03,1.04596552e+03,1.04695216e+03,
 1.04768643e+03,1.04861572e+03,1.04941861e+03,1.05018888e+03,
 1.05113153e+03,1.05196055e+03,1.05280133e+03,1.05370428e+03,
 1.05438216e+03,1.05550744e+03,1.05597111e+03,1.05720842e+03,
 1.05795141e+03,1.05836949e+03,1.06021851e+03,1.06041882e+03,
 1.05876918e+03,1.05178939e+03,9.97802773e+02,9.43131047e+02])
options['control_z_i'] = np.array([9.32216388e+02,7.68226146e+02,1.02776440e+03,6.32717730e+02,
 2.88035042e+02,2.35376227e+02,1.62230518e+02,7.09247055e+01,
 3.21672446e-15,1.95592623e-03,1.45293587e-03,8.33800687e-04,
 7.32344474e-04,5.97153782e-04,4.56609163e-04,7.21651139e-04,
 4.28149836e-04,4.37072814e-04,4.34941956e-04,4.40542343e-04,
 4.40395972e-04,4.44839290e-04,4.45492587e-04,4.48511739e-04,
 4.51173621e-04,4.52394470e-04,4.55562685e-04,4.58513270e-04,
 4.58119413e-04,4.66208463e-04,4.60607251e-04,4.72288171e-04,
 4.68481265e-04,4.64363882e-04,5.01126882e-04,4.65021534e-04,
 6.96339124e-04,1.31352852e-03,3.94257166e-04,3.08148061e-05])
options['control_alpha_i'] = np.array([-1.29796006e-22, 1.57079633e+00, 2.84516303e-01, 1.64010065e-01,
  1.19775673e-01, 1.04617838e-01, 8.67996203e-02, 7.45257723e-02,
  6.25805514e-02, 5.17567908e-02, 4.23671535e-02, 3.41410759e-02,
  2.62563034e-02, 2.08119227e-02, 1.05309167e-02, 2.48736092e-02,
  7.42655953e-03, 8.61526461e-03, 8.13428697e-03, 8.52283142e-03,
  8.53719357e-03, 8.60316899e-03, 8.81405915e-03, 8.88790052e-03,
  8.92749251e-03, 9.14630950e-03, 9.19713212e-03, 9.34812655e-03,
  9.32949234e-03, 9.63554829e-03, 9.66987515e-03, 9.67168028e-03,
  9.92557367e-03, 1.00538037e-02, 9.81358774e-03, 1.11607873e-02,
  2.25393786e-02, 3.88740783e-02, 1.84726982e-02,-4.19699591e-02])
"""


