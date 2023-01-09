from efficiency import efficiency
import numpy as np


ht120_60 = np.array([0.00000000e+00,2.96883223e-01,1.42393373e+00,3.95403883e+00,
 7.61539178e+00,1.04415828e+01,1.73684880e+01,2.20872665e+01,
 2.35759008e+01,2.85530052e+01,3.50197761e+01,4.25496504e+01,
 5.23070654e+01,6.49214645e+01,8.06751866e+01,9.87516404e+01,
 1.18589159e+02,1.40395258e+02,1.63544940e+02,1.87945932e+02,
 2.13123712e+02,2.39309733e+02,2.65125734e+02,2.88432889e+02,
 3.05465414e+02,3.09881923e+02,3.02754644e+02,2.96186341e+02,
 2.94915451e+02,2.99938450e+02])
vt120_60 = np.array([ 5.        ,13.8413514 ,20.2529454 ,24.78449932,28.00249724,31.59252878,
 33.92253456,36.56860588,40.13333831,42.80761867,45.19990819,47.33807293,
 49.01179169,49.99396729,50.31643386,50.31224248,50.04663897,49.37594239,
 48.287264  ,46.6415203 ,44.76804736,42.62869971,40.12296602,37.62700841,
 35.99327332,37.15549216,40.84839191,43.53128298,44.41477237,43.00647746])

et120_60 = 17349703.34377608

g = 9.81
m = 2000

eta_e = efficiency(et120_60,ht120_60,vt120_60,m,g)

print(eta_e)