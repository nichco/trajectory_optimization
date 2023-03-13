from smt.surrogate_models import RBF
import numpy as np


n = 3500
x_lim = 12000.0 # (m)
be = 20
pi = 250
pf = 600
bf = pf + 250
obs_height = 100
x = np.linspace(0,x_lim,n)
obs = np.zeros((n))

for i in range(0,n):
    xi = x[i]
    if xi > pi and xi <= pf:
        obs[i] = obs_height
    elif xi > be and xi < pi:
        obs[i] = (np.sin((np.pi/(pi-be))*(xi-be)-(np.pi/2)) + 1)*(obs_height/2)
    elif xi > pf and xi < bf:
        obs[i] = (np.sin((np.pi/(bf-pf))*(xi-bf)-(np.pi/2)) + 1)*(obs_height/2)

sm = RBF(d0=50,print_global=False,print_solver=False,)
sm.set_training_values(x, obs)
sm.train()

num = 47
dte = 4.10321105
ee = 30501820.03526178
te = np.linspace(0,num*dte,num)

he = np.array([  0.        , 41.84190747, 87.76647961, 99.88657662,100.02731155,
  99.98427319,100.13041623,98.08782375,96.13259374,95.13143912,
 95.57738359,95.13935703,95.24298679,95.16565623,95.26694114,
 95.21533412,95.15874277,95.18396445,95.23833706,95.18876945,
 95.64149973,95.55508232,95.20757622,95.17008245,95.18349527,
 95.62575349,95.48161074,96.11841121,96.20608981,96.17472792,
 96.33797156,96.18988434,96.32520701,97.05141078,97.60072553,
 97.19957057,97.38040969,98.04641598,98.50577821,99.02809808,
 99.5219156 ,100.07884675,100.24054259,100.11677609,102.17746322,
 107.69209639,109.90300186])
xe = np.array([    0.        ,  52.87029151,   110.90784899,  181.78649909,
   294.54228262,  467.2288911 ,  657.70648684,  860.22298006,
  1072.20354999, 1292.37361963, 1519.13856698, 1751.81359145,
  1989.67976771, 2231.8950623 , 2478.03197702, 2727.61984461,
  2980.34750334, 3235.90423727, 3493.94047283, 3754.17883927,
  4016.08628903, 4279.55072662, 4544.74771312, 4811.26042923,
  5078.88374275, 5347.18992348, 5616.02058881, 5885.49327784,
  6155.3768578 , 6425.47843341, 6695.52854939, 6965.42294141,
  7234.92200701, 7503.97966918, 7772.29179042, 8040.02975193,
  8307.03504915, 8573.11698711, 8837.81036451, 9100.98028008,
  9362.48351154, 9621.82441343, 9878.92457649,10133.44203629,
 10385.71258034,10631.36870173,10870.50572183])
ve = np.array([ 0.625     ,20.78525629,23.83743471,30.90261678,38.93564099,44.61891999,
 48.03779004,50.57760981,52.70971006,54.52996329,55.98636755,57.39269371,
 58.51453191,59.5336888 ,60.41952786,61.22349643,61.95059333,62.59939645,
 63.16562952,63.65335557,64.00603453,64.4255786 ,64.81157863,65.09272226,
 65.33072945,65.44496645,65.59515468,65.74069537,65.8025223 ,65.83690403,
 65.79237418,65.74600161,65.61874873,65.50529609,65.29529261,65.19118551,
 64.95496116,64.71115704,64.31029818,63.95706567,63.48262015,62.93065271,
 62.35824465,61.75872154,60.97468894,58.84748588,57.9999052 ])
gamma = np.array([ 0.00000000e+00, 1.25067971e+00, 2.09527504e-01, 3.67376015e-02,
 -1.68595799e-02, 5.35340843e-03,-1.31667574e-03, 4.72717073e-04,
 -5.69903414e-04, 1.68548291e-03,-1.06606701e-04,-1.24584215e-03,
  4.50766251e-04,-1.53066349e-04, 2.88489236e-04,-3.87771476e-04,
 -1.04540294e-04, 3.54365884e-04,-3.68482877e-04, 9.66332338e-04,
  1.20993327e-03,-1.43993905e-03,-6.54433402e-04,-2.20152870e-04,
  1.10041849e-03, 9.87366364e-04,-1.60590429e-03,-3.97302431e-04,
  1.45467091e-04, 3.71731417e-04,-1.08329338e-04, 1.18705429e-04,
 -4.19657282e-04, 9.34169059e-04, 1.29505784e-06,-5.76266080e-04,
 -1.34025891e-04, 3.08720272e-04, 4.43207790e-04,-1.20332945e-03,
  9.03388219e-04,-4.86647255e-04, 9.53532960e-04,-5.68542635e-03,
  1.83565402e-02, 2.59366841e-02,-8.63265479e-06])
control_x = np.array([1478.46379833,1510.02037267,1561.94847762,1590.6489358 ,1621.71172334,
 1243.35974109,1099.69694331,1031.27870549, 991.1806726 , 944.42023216,
  903.26768447, 881.4370414 , 844.73817016, 833.40374921, 809.44932288,
  793.24405787, 781.77511719, 768.46966513, 749.36256201, 733.13764883,
  723.47419142, 721.72140372, 696.89494668, 695.25713863, 681.97203952,
  664.99301556, 652.68484875, 653.23815621, 643.21559017, 629.97292629,
  616.53027834, 606.37350894, 595.06070562, 593.2460838 , 589.81310451,
  582.94813928, 568.60885032, 545.45258004, 532.49469643, 516.22322739,
  497.67036797, 482.75436735, 470.60134145, 456.86876721, 459.19444579,
  460.32351102, 654.2108247 ])
control_z = np.array([1.13820857e+03,1.09435148e+03,1.12697438e+03,8.35014374e+02,
 3.52746023e+02,8.96552542e+01,0.00000000e+00,6.02262278e-02,
 1.83121275e-15,1.08536404e-05,8.73901903e-05,1.49904625e-05,
 2.69059073e-04,2.15494203e-04,1.47925450e-04,5.68361051e-05,
 9.82455208e-05,2.53778031e-04,2.45312423e-04,2.31868048e-04,
 2.53059849e-04,1.36319391e-04,1.64070883e-05,5.22428381e-05,
 2.11610430e-04,2.49873036e-04,2.53232551e-04,1.56195383e-04,
 7.65107664e-05,5.98168345e-05,1.31277449e-04,1.95866186e-04,
 1.83690499e-04,1.87411707e-04,1.88697128e-04,2.00048217e-04,
 2.39352135e-04,2.13281934e-04,1.64528629e-04,1.47696175e-04,
 1.66148145e-04,1.67669870e-04,1.54944974e-04,1.63013147e-04,
 1.03522948e-04,1.78021373e-04,3.50947822e-05])
control_alpha = np.array([ 0.1827107 ,-1.57079633,-0.25566536, 0.105031  , 0.18192665, 0.11129706,
  0.08917585, 0.07208382, 0.0591251 , 0.05116414, 0.04129842, 0.03775774,
  0.0310528 , 0.02792097, 0.02365496, 0.02093741, 0.01819767, 0.01593144,
  0.01346824, 0.01289533, 0.01031189, 0.00935141, 0.00868521, 0.00713751,
  0.00723902, 0.0055953 , 0.00559518, 0.00588481, 0.00474047, 0.00544703,
  0.00458403, 0.00592391, 0.00493236, 0.00724121, 0.00531469, 0.00825768,
  0.00680948, 0.00972324, 0.00893118, 0.01159534, 0.01298021, 0.01403884,
  0.01783882, 0.01576063, 0.03268677, 0.02229917, 0.03420006])
cruise_power = np.array([468300.00000075,468272.54495848,468284.64606901,468292.37169398,
 468281.86789177,200108.03140211,134130.28021972,107971.26551117,
  93896.56669519, 79790.20274523, 68789.76190593, 63032.36374955,
  54846.9172644 , 52121.64568618, 47316.55561771, 44159.08074916,
  41948.94828182, 39570.22505434, 36470.0293845 , 33974.90410481,
  32523.22282531, 32141.96055027, 28818.15584022, 28527.95608802,
  26854.08777058, 24865.42347957, 23471.98062136, 23495.21856186,
  22414.69858935, 21050.83213717, 19740.9774622 , 18791.32867556,
  17783.41634022, 17643.74270495, 17377.83654049, 16798.25859974,
  15628.37171791, 13832.98209408, 12925.51934244, 11822.01349125,
  10646.75811615,  9775.07772216,  9111.05869697,  8388.78564737,
   8591.99956657,  4238.06692659, 25587.9510701 ])
lift_power = np.array([1.43651998e+05,1.43651594e+05,1.43648673e+05,5.73593117e+04,
 4.30917378e+03,7.30551251e+01,0.00000000e+00,2.28088643e-08,
 6.48408114e-49,1.36235280e-19,7.17181487e-17,3.64389332e-19,
 2.12082827e-15,1.09522090e-15,3.56034598e-16,2.02804084e-17,
 1.05162830e-16,1.81889280e-15,1.64818750e-15,1.39501144e-15,
 1.81775583e-15,2.84761150e-16,4.97455500e-19,1.60879665e-17,
 1.07023818e-15,1.76384304e-15,1.83721427e-15,4.31385433e-16,
 5.07347171e-17,2.42425482e-17,2.56273866e-16,8.50631105e-16,
 7.01465120e-16,7.44047686e-16,7.59181524e-16,9.03357369e-16,
 1.54632923e-15,1.09190911e-15,5.00461240e-16,3.61177030e-16,
 5.12865620e-16,5.25635597e-16,4.13297003e-16,4.80361938e-16,
 1.21971203e-16,6.16343039e-16,4.68775945e-18])
e = np.array([       0.        , 6947497.89843614,14151738.3868391 ,19620173.61648452,
 22537453.15384275,24011000.05861694,24744125.51122932,25276176.05581416,
 25719851.9667379 ,26100757.47571076,26426272.07963911,26714912.83594656,
 26972529.71186942,27206311.10718188,27423366.02136827,27622937.51355255,
 27810706.8219411 ,27988362.49922059,28153954.73422294,28307271.51345518,
 28451983.15311545,28592695.07948389,28725174.27892479,28849855.87661248,
 28970202.10287349,29082551.97320288,29187545.61047069,29289559.72719535,
 29389258.82107948,29483618.53016387,29572168.07299289,29655808.94041381,
 29735206.92436266,29812118.27718891,29888168.05204856,29962368.33043922,
 30032769.73803484,30096706.08386001,30154842.21240279,30208616.86967976,
 30257456.17516316,30301895.42660952,30343024.39100958,30381182.478695  ,
 30418180.9904597 ,30445589.21271402,30501820.03526178])
spl = np.array([143.32203164,111.85659157,107.08322652, 98.41672904, 95.66730598,
  88.3486535 , 84.89167978, 83.08874817, 81.92625015, 80.62004701,
  79.31735652, 78.67561841, 77.51690547, 77.13754794, 76.33648995,
  75.78412645, 75.38784993, 74.92350405, 74.23588597, 73.68031691,
  73.27586922, 73.18682676, 72.31053429, 72.24303239, 71.75461146,
  71.04872769, 70.55756566, 70.62093191, 70.20848136, 69.6793491 ,
  69.09683208, 68.69084594, 68.18007993, 68.14536058, 67.93309189,
  67.68330672, 67.01421816, 65.98697424, 65.32764509, 64.55670913,
  63.64202563, 62.8373165 , 62.2384165 , 61.39941076, 61.91070561,
  54.98869896, 70.13990668])
"""
print(np.array2string(sim['cruisepower'].flatten(),separator=','))
print(np.array2string(sim['v'],separator=','))
"""


import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 12})

"""
plt.rcParams['figure.figsize'] = [11, 2.5]

num = 10000
x_p = np.linspace(0,x_lim,num)
obs_p = sm.predict_values(x_p)
# plt.text(5000, 50, 'No Fly Zone', color='red', fontsize=12,bbox={'facecolor': 'white', 'alpha': 0.8, 'pad': 3})

plt.scatter(xe,he,color='blue',marker='^')
plt.fill_between(x_p,obs_p.flatten(),alpha=0.8,color='mistyrose',hatch='///',edgecolor='indianred')
plt.legend(['minimum energy', 'obstacle'], frameon=False)

plt.plot(x_p,obs_p,'k',linewidth=0.5)
plt.xlabel('horizontal position (m)')
plt.ylabel('altitude (m)')

eSpline = make_interp_spline(xe,he)
ixe = np.linspace(xe.min(), xe.max(), 500)
ihe = eSpline(ixe)
plt.plot(ixe,ihe,color='blue')

plt.xlim(0,xe.max())
plt.ylim(0,200)

plt.savefig('hx_trans_2', dpi=1200, bbox_inches='tight')
plt.show()
"""
"""
# region v
plt.rcParams['figure.figsize'] = [5, 2]

target_velocity = np.ones(47)*58
plt.plot(te,target_velocity,color='k',linestyle='dashed',linewidth=1)

plt.scatter(te,ve,color='blue',marker='^')

plt.legend(['target velocity', 'minimum energy'], frameon=False)

eSpline = make_interp_spline(te,ve)
ixe = np.linspace(te.min(), te.max(), 500)
ihe = eSpline(ixe)
plt.plot(ixe,ihe,color='blue')

plt.xlabel('time (s)')
plt.ylabel('velocity (m/s)')
plt.savefig('v_trans_2', dpi=1200, bbox_inches='tight')
plt.show()
# endregion
"""
"""
# region gamma
plt.rcParams['figure.figsize'] = [5, 2]

plt.scatter(te,np.rad2deg(gamma),color='blue',marker='^')
plt.legend(['minimum energy'], frameon=False)

eSpline = make_interp_spline(te,np.rad2deg(gamma))
ixe = np.linspace(te.min(), te.max(), 500)
ihe = eSpline(ixe)
plt.plot(ixe,ihe,color='blue')

plt.xlabel('time (s)')
plt.ylabel('flight path angle ' r'($^{\circ}$)')
plt.savefig('g_trans_2', dpi=1200, bbox_inches='tight')
plt.show()
# endregion
"""
"""
# region alpha
plt.rcParams['figure.figsize'] = [5, 2]

plt.scatter(te,np.rad2deg(control_alpha),color='blue',marker='^')
plt.legend(['minimum energy'], frameon=False)

eSpline = make_interp_spline(te,np.rad2deg(control_alpha))
ixe = np.linspace(te.min(), te.max(), 500)
ihe = eSpline(ixe)
plt.plot(ixe,ihe,color='blue')

plt.xlabel('time (s)')
plt.ylabel('angle of attack ' r'($^{\circ}$)')
plt.savefig('a_trans_2', dpi=1200, bbox_inches='tight')
plt.show()
# endregion
"""
"""
# region theta
plt.rcParams['figure.figsize'] = [5, 2]

plt.scatter(te,np.rad2deg(control_alpha + gamma),color='blue',marker='^')
plt.legend(['minimum energy'], frameon=False)

eSpline = make_interp_spline(te,np.rad2deg(control_alpha + gamma))
ixe = np.linspace(te.min(), te.max(), 500)
ihe = eSpline(ixe)
plt.plot(ixe,ihe,color='blue')

plt.xlabel('time (s)')
plt.ylabel('pitch angle ' r'($^{\circ}$)')
plt.savefig('t_trans_2', dpi=1200, bbox_inches='tight')
plt.show()
# endregion
"""
"""
# region cxt
plt.rcParams['figure.figsize'] = [5, 2]

plt.scatter(te,control_x,color='blue',marker='^')
plt.legend(['minimum energy'], frameon=False)

eSpline = make_interp_spline(te,control_x)
ixe = np.linspace(te.min(), te.max(), 500)
ihe = eSpline(ixe)
plt.plot(ixe,ihe,color='blue')

plt.xlabel('time (s)')
plt.ylabel('cruise rotor speed (rpm)')
plt.savefig('cx_trans_2', dpi=1200, bbox_inches='tight')
plt.show()
# endregion
"""
"""
# region czt
plt.rcParams['figure.figsize'] = [5, 2]

plt.scatter(te,control_z,color='blue',marker='^')
plt.legend(['minimum energy'], frameon=False)

eSpline = make_interp_spline(te,control_z)
ixe = np.linspace(te.min(), te.max(), 500)
ihe = eSpline(ixe)
plt.plot(ixe,ihe,color='blue')

plt.xlabel('time (s)')
plt.ylabel('lift rotor speed (rpm)')
plt.savefig('cz_trans_2', dpi=1200, bbox_inches='tight')
plt.show()
# endregion
"""
"""
# region cruisepower
plt.rcParams['figure.figsize'] = [5, 2]

max_cruise_power = np.ones(47)*468300
plt.plot(te,max_cruise_power,color='k',linestyle='dashed',linewidth=1)

plt.scatter(te,cruise_power,color='blue',marker='^')

plt.legend(['maximum available cruise rotor power', 'cruise rotor power'], frameon=False)

eSpline = make_interp_spline(te,cruise_power)
ixe = np.linspace(te.min(), te.max(), 500)
ihe = eSpline(ixe)
plt.plot(ixe,ihe,color='blue')

plt.xlabel('time (s)')
plt.ylabel('power (W)')
#plt.savefig('cpwr_trans_2', dpi=1200, bbox_inches='tight')
plt.show()
# endregion
"""

"""
# region liftpower
plt.rcParams['figure.figsize'] = [5, 2]

max_lift_power = np.ones(47)*143652
plt.plot(te,max_lift_power,color='k',linestyle='dashed',linewidth=1)

plt.scatter(te,lift_power,color='blue',marker='^')

plt.legend(['maximum available lift rotor power', 'lift rotor power'], frameon=False)

eSpline = make_interp_spline(te,lift_power)
ixe = np.linspace(te.min(), te.max(), 500)
ihe = eSpline(ixe)
plt.plot(ixe,ihe,color='blue')

plt.xlabel('time (s)')
plt.ylabel('power (W)')
plt.savefig('lpwr_nfz', dpi=1200, bbox_inches='tight')
plt.show()
# endregion
"""

"""
# region energy
plt.rcParams['figure.figsize'] = [5, 2]

plt.scatter(te,e/1e6,color='blue',marker='^')
plt.legend(['energy'], frameon=False)

eSpline = make_interp_spline(te,e/1e6)
ixe = np.linspace(te.min(), te.max(), 500)
ihe = eSpline(ixe)
plt.plot(ixe,ihe,color='blue')

plt.xlabel('time (s)')
plt.ylabel('energy (MJ)')
plt.savefig('e_trans_2', dpi=1200, bbox_inches='tight')
plt.show()
# endregion
"""
"""
# region spl
plt.rcParams['figure.figsize'] = [5, 2]

plt.scatter(te,spl,color='blue',marker='^')
plt.legend(['maximum ground-level SPL'], frameon=False)

eSpline = make_interp_spline(te,spl)
ixe = np.linspace(te.min(), te.max(), 500)
ihe = eSpline(ixe)
plt.plot(ixe,ihe,color='blue')

plt.xlabel('time (s)')
plt.ylabel('SPL (db)')
plt.savefig('spl_trans_2', dpi=1200, bbox_inches='tight')
plt.show()
# endregion
"""