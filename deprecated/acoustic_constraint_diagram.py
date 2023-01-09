import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
plt.rcParams['font.family'] = 'Century'
plt.rcParams.update({'font.size': 12})
plt.rcParams['figure.figsize'] = [5, 2.5]

n=30

spl = np.array([101.87667103,102.21056089,102.07265058,100.46292652, 99.37854002,
  98.03199616, 96.58880886, 95.18044238, 93.72922598, 92.67400365,
  92.1910186 , 91.94515566, 91.91063947, 91.84047928, 91.51048578,
  91.05705144, 90.43062603, 89.61644002, 88.7799018 , 88.01858393,
  87.30328939, 86.67676379, 86.13038854, 85.65373936, 85.2521069 ,
  84.89597058, 84.60245531, 84.34130633, 84.10942531, 83.86027327])

lin = np.linspace(105,85,n)
const = np.ones((n-10))*93
cx = np.linspace(10,n,n-10)

plt.plot(spl,color='k',linestyle='solid',linewidth=2)
plt.plot(lin,color='k',linestyle='dashed',linewidth=2)
plt.xlabel('time (s)')
plt.ylabel('sound pressure level (db)')

x = np.arange(0,30,1)
plt.fill_between(x,lin,color='gray',alpha=0.3)
plt.ylim(83, 110)
plt.show()



plt.plot(spl,color='k',linestyle='solid',linewidth=2)
plt.plot(cx,const,color='k',linestyle='dashed',linewidth=2)
plt.xlabel('time (s)')
plt.ylabel('sound pressure level (db)')
plt.fill_between(cx,const,color='gray',alpha=0.3)
plt.ylim(83, 110)
plt.show()