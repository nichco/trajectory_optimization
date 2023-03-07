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
options['v_0'] = 0.625 # (m/s)
options['gamma_0'] = 0.0 # (rad)
options['h_0'] = 0 # (m)
options['min_h'] = -0.1 # (m)
options['x_0'] = 0 # (m)
options['alpha_0'] = 0 # (rad)
options['h_f'] = 110 # (m)
options['v_f'] = 58 # (m/s)
options['vne'] = 65 # (m/s)
options['x_lim'] = 5000 # (m)
options['theta_0'] = 0.0 # (rad)
options['gamma_f'] = 0.0 # (rad)
options['max_g'] = 0.5 # (g)

# obstacle
options['be'] = 10 # (m) start of sinusoidal ramp
options['p_i'] = 100 # (m) start of obstacle
options['p_f'] = 12000 # (m) end of obstacle
options['obs_height'] = 100 # (m)


"""
print(np.array2string(sim['control_x'],separator=','))
print(np.array2string(sim['control_z'],separator=','))
print(np.array2string(sim['control_alpha'],separator=','))
"""


# min e seed TRANS!
options['dt'] = 4.1069021
options['control_x_i'] = np.array([1478.46331616,1470.04003199,1561.95678174,1590.13030421,1621.0095176 ,
 1250.29432465,1102.93036944,1036.43524683, 997.21928729, 948.13394868,
  904.30245445, 881.37197083, 843.44564009, 834.14837251, 809.85065744,
  794.57438162, 784.53703254, 771.77529443, 751.19645144, 734.78910554,
  727.07959789, 725.56897988, 698.31147625, 695.49862479, 681.8005176 ,
  663.83505892, 651.43201163, 653.2528374 , 643.57773346, 629.24583363,
  614.70966087, 603.95691648, 592.81087864, 592.31074534, 590.54340723,
  584.14132097, 568.58547444, 542.95110032, 529.11100482, 511.72848575,
  491.79673304, 476.29240249, 464.03091536, 450.90512428, 452.61196247,
  356.69919201, 654.21086105])
options['control_z_i'] = np.array([1.13821186e+03,1.09436930e+03,1.12702247e+03,8.21783816e+02,
 3.72466943e+02,6.87460561e+01,0.00000000e+00,7.00246471e-02,
 2.04330639e-03,3.89339026e-05,8.45451924e-05,1.25382656e-05,
 2.71655704e-04,2.20245277e-04,1.44754476e-04,5.16260818e-05,
 9.38104732e-05,2.56613830e-04,2.51963533e-04,2.33900102e-04,
 2.56164564e-04,1.34492715e-04,1.28428858e-05,4.74905915e-05,
 2.11360736e-04,2.53474064e-04,2.58864568e-04,1.54135998e-04,
 7.10513831e-05,5.49848737e-05,1.27512628e-04,1.96420749e-04,
 1.83981216e-04,1.89815740e-04,1.90366168e-04,2.05403083e-04,
 2.48144939e-04,2.21202068e-04,1.66417638e-04,1.49524370e-04,
 1.68951658e-04,1.71961628e-04,1.58774631e-04,1.67162787e-04,
 1.06394259e-04,1.83138648e-04,3.54277494e-05])
options['control_alpha_i'] = np.array([ 0.18407412,-1.57079633,-0.10501119, 0.10296334, 0.18022523, 0.11420956,
  0.08918024, 0.07257138, 0.05914744, 0.05075966, 0.04054623, 0.04010431,
  0.02765393, 0.02989227, 0.02315637, 0.02051665, 0.01842413, 0.01467587,
  0.01481291, 0.01037397, 0.01057799, 0.01204142, 0.00326705, 0.0098959 ,
  0.00726069, 0.00317455, 0.00652965, 0.00632655, 0.00279735, 0.00571124,
  0.00441906, 0.00610958, 0.00331255, 0.00824341, 0.00397246, 0.00856209,
  0.00594999, 0.01033307, 0.00738644, 0.01218818, 0.01214599, 0.01426574,
  0.01724017, 0.01579413, 0.03243339, 0.02231348, 0.03420007])
