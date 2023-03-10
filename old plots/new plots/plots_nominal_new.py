import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 12})
# plt.box(False)
"""
print(np.array2string(sim['x'],separator=','))
print(np.array2string(sim['h'],separator=','))
print(np.array2string(sim['v'],separator=','))
print(np.array2string(sim['control_alpha'],separator=','))
print(np.array2string(sim['gamma'],separator=','))
print(np.array2string(sim['control_x'],separator=','))
print(np.array2string(sim['control_z'],separator=','))
print(np.array2string(sim['max_spl_gl'],separator=','))
"""
# num steps
num = 30
# timestep
dte = 2.67211946
dtt = 0.9270615
# x-axis time vectors
te = np.linspace(0,num*dte,num)
tt = np.linspace(0,num*dtt,num)
# total energy
ee = 13292179.14548814
et = 16348893.14520152

#region mine
# minimum energy objective
xe = np.array([   0.        ,  40.65701204, 112.17081845, 200.02583844, 296.73214727,
  400.33691799, 510.5331433 , 627.26871187, 750.81680282, 880.34086364,
 1012.87399015,1145.32527725,1276.28054124,1405.8413601 ,1534.76383172,
 1663.86013553,1793.56481446,1923.82930224,2054.26904982,2184.38994968,
 2313.93174397,2443.12328429,2572.72358064,2703.77642848,2836.90098202,
 2971.28051056,3104.01698785,3230.96096484,3349.9887158 ,3464.63791329])
he = np.array([0.00000000e+00,1.06399831e-01,2.07337489e-01,1.46265664e-01,
 2.08870325e-01,2.42177317e-01,2.72598832e-01,2.74610633e-01,
 3.29438490e-01,4.27201101e+00,1.46574533e+01,2.99764583e+01,
 4.68225499e+01,6.27406575e+01,7.69014174e+01,8.95988567e+01,
 1.01836402e+02,1.14492128e+02,1.28025486e+02,1.42372059e+02,
 1.56832730e+02,1.70415360e+02,1.82309841e+02,1.92527388e+02,
 2.02718907e+02,2.16084895e+02,2.35583751e+02,2.60968583e+02,
 2.86036159e+02,2.99999990e+02])
ve = np.array([ 5.        ,22.6008652 ,30.41540877,34.82212713,37.50658898,40.01319966,
 42.45725491,44.93924145,47.48879462,49.33508327,49.98979424,49.71162582,
 49.10719429,48.6387519 ,48.49073989,48.63248586,48.87898542,49.05769053,
 49.06545639,48.89560486,48.67226964,48.59947286,48.87842245,49.55836158,
 50.34307394,50.590355  ,49.5962305 ,47.09887762,44.06340252,42.99997987])
ae = np.array([0.88706619,0.46892978,0.19391763,0.13946598,0.10133364,0.07306852,
 0.05395443,0.03283381,0.0274812 ,0.02175095,0.01499966,0.01007989,
 0.00899336,0.01027347,0.01171162,0.01325794,0.0136892 ,0.01372033,
 0.01381559,0.01352123,0.01299059,0.01195269,0.01042739,0.01002401,
 0.01207339,0.01654903,0.02283205,0.02733581,0.01954736,0.00727297])
ge = np.array([ 0.        , 0.00809789,-0.00492557, 0.0004712 , 0.00049718, 0.00026574,
  0.00081522,-0.00247423, 0.00981007, 0.05368093, 0.10025662, 0.12561179,
  0.12730624, 0.11626409, 0.10282803, 0.09467891, 0.09452231, 0.09973868,
  0.1070401 , 0.111697  , 0.10936391, 0.09901342, 0.08381535, 0.07375678,
  0.08307227, 0.11923175, 0.17379695, 0.21528137, 0.18224534, 0.04747402])
cxe = np.array([1430.57121892,1731.39209194,1789.34065168,1410.45262232,1392.30793142,
 1380.83473316,1398.60689464,1431.34774773,1487.57487474,1531.837694  ,
 1548.7620248 ,1545.40981001,1533.29480501,1522.6305252 ,1519.31079971,
 1522.80557931,1529.02559808,1533.88052007,1533.6277055 ,1528.25865203,
 1520.247691  ,1516.74344998,1526.47489723,1551.15761809,1582.04799454,
 1597.75667045,1568.12559624,1476.64226222,1355.4989248 ,1289.17004856])
cze = np.array([1637.69389579,1106.86059276, 684.28097985, 359.56687426, 205.50180373,
  173.56314396, 107.54286486, 100.1799865 ,  99.98944342,  99.9906537 ,
   99.9914637 ,  99.99236676,  99.99344101,  99.99449805,  99.99538591,
   99.9960759 ,  99.99658993,  99.99699099,  99.99731968,  99.99758667,
   99.99779641,  99.9979596 ,  99.99810123,  99.99825832,  99.99845972,
   99.99869883,  99.99892479,  99.9990439 ,  99.99897799,  99.99946101])
sple = np.array([121.66351372,113.44532375,110.11840687,103.61953258,103.23388204,
 103.00530211,103.32899538,103.92878906,104.92170598,103.93045572,
  97.40896202, 90.31150239, 85.31704283, 81.89681266, 79.5495364 ,
  77.87003624, 76.51938499, 75.27776851, 74.01722182, 72.7301695 ,
  71.49663508, 70.47244681, 69.82313777, 69.60506538, 69.53378182,
  69.13339111, 67.68277267, 65.00031419, 61.83893784, 59.97557756])
#endregion


# region mindt
# minimum time objective
xt = np.array([   0.        ,   8.25551682,  23.53072112,  44.51629938,  69.63212422,
   97.64866276, 127.68354605, 159.14075592, 192.1333374 , 227.19184136,
  264.6879085 , 304.81227989, 347.60253217, 392.91372284, 440.44218384,
  489.79171824, 540.48439098, 591.9562347 , 643.60916639, 694.87795119,
  745.22916422, 794.20537274, 841.43675611, 886.71491298, 929.94186223,
  971.00431992,1010.05309921,1047.30265656,1083.04725885,1117.53771003])
ht = np.array([ 0.00000000e+00, 6.31497213e-02,-2.48464296e-02,-7.53045277e-02,
  1.28295978e+00, 4.15754980e+00, 8.62443087e+00, 1.46354416e+01,
  2.02493591e+01, 2.40183198e+01, 2.59393114e+01, 2.68913403e+01,
  2.77142843e+01, 2.92917187e+01, 3.22190782e+01, 3.67999960e+01,
  4.34241321e+01, 5.26652456e+01, 6.45834437e+01, 7.91714178e+01,
  9.63160931e+01, 1.15739029e+02, 1.37037815e+02, 1.59756630e+02,
  1.83409651e+02, 2.07669927e+02, 2.31923633e+02, 2.55670893e+02,
  2.78460928e+02, 3.00015371e+02])
vt = np.array([ 5.        ,12.81755001,19.90963245,25.08389909,28.9460382 ,31.6803055 ,
 33.73844128,35.3013924 ,36.98110581,39.1926921 ,41.86690118,44.73419471,
 47.5739677 ,50.19239613,52.48131633,54.37369126,55.86238361,56.88044911,
 57.41957628,57.51419024,57.1797669 ,56.42415801,55.31460832,53.93811869,
 52.33506796,50.53452648,48.62387363,46.68094308,44.78213291,43.00011465])
at = np.array([6.14377795e-01,8.60604153e-01,9.85703418e-01,4.43511814e-01,
 3.53745726e-01,2.49629804e-01,1.67155793e-01,4.33161417e-02,
 8.75236776e-03,5.54205951e-03,1.73237101e-02,1.65553491e-02,
 1.65612931e-02,1.04217025e-02,3.32734549e-03,2.31559127e-05,
 3.83681218e-03,3.88737050e-06,1.67743048e-06,5.77316785e-05,
 4.79544581e-06,4.84186801e-06,6.75598944e-04,1.21478833e-05,
 5.90373745e-03,3.13436882e-03,5.28815936e-03,3.92249315e-03,
 1.28720498e-02,7.33241619e-20])
gt = np.array([ 0.        , 0.00473449,-0.0144688 , 0.02300315, 0.07974545, 0.12365172,
  0.17219107, 0.19138746, 0.14041563, 0.07573959, 0.03292886, 0.01794092,
  0.02416865, 0.04695873, 0.07629098, 0.10951104, 0.15262425, 0.20215148,
  0.25171031, 0.30280333, 0.35333328, 0.40130356, 0.44543691, 0.48348439,
  0.51831899, 0.54669053, 0.56365831, 0.5689589 , 0.56597743, 0.54536037])
cxt = np.array([2104.7695022 ,2115.4134416 ,2153.00470178,2213.72873331,2243.58835329,
 2265.31092023,2280.0773581 ,2277.0607596 ,2305.60716744,2322.78056034,
 2335.96183508,2360.01621271,2378.15612254,2399.29355443,2413.2400634 ,
 2406.85330201,2441.97650291,2438.0228724 ,2452.43674488,2456.94948004,
 2459.63063656,2432.70304404,2441.10719955,2433.44848836,2423.97212453,
 2413.07552057,2401.03752593,2389.37685222,2373.43758947,2368.63876932])
czt = np.array([1385.9572475 ,1378.98939011,1352.12694977,1153.93501213, 936.79757382,
  763.80069359, 664.8801888 , 596.09227073, 538.42229699, 493.78067537,
  470.99409501, 444.99857618, 449.23781374, 458.06379036, 443.96877129,
  428.0284761 , 402.17005138, 366.89480855, 331.66057602, 297.94748818,
  261.1913302 , 229.43816243, 197.82240036, 168.18468783, 138.34289863,
  112.30607352, 100.03654335, 100.04349879, 100.05216305, 100.01703125])
splt = np.array([119.02899923,118.97299265,118.80830178,117.27373904,116.05749309,
 114.42658082,111.22480171,107.07854671,104.51824726,103.06942414,
 102.42175391,102.29596736,102.17310417,101.81660425,100.94886091,
  99.44175571, 97.97745051, 95.74821128, 93.52007544, 91.28679806,
  89.19495024, 86.69077724, 84.79721519, 82.8428133 , 81.0594126 ,
  79.43389936, 77.9656808 , 76.70374336, 75.52778977, 74.73702941])
#endregion


# region hx

# h vs x
plt.rcParams['figure.figsize'] = [11, 2.5]

eSpline = make_interp_spline(xe,he)
ixe = np.linspace(xe.min(), xe.max(), 500)
ihe = eSpline(ixe)

tSpline = make_interp_spline(xt,ht)
ixt = np.linspace(xt.min(), xt.max(), 500)
iht = tSpline(ixt)

target_altitude = np.ones(num)*300
plt.plot(xe,target_altitude,color='k',linestyle='dashed',linewidth=1)

plt.scatter(xe,he,color='blue',marker='^')
plt.scatter(xt,ht,color='red',marker='o')
plt.legend(['target altitude', 'minimum energy', 'minimum time'], frameon=False)

plt.plot(ixe,ihe,color='blue',linestyle='solid',linewidth=2)
plt.plot(ixt,iht,color='red',linestyle='solid',linewidth=2)
plt.xlabel('horizontal displacement (m)')
plt.ylabel('altitude (m)')

plt.savefig('new_h_vs_x.png', dpi=1200, bbox_inches='tight')
plt.show()

#endregion


#region ht
# h vs t
plt.rcParams['figure.figsize'] = [5, 2]
eSpline = make_interp_spline(te,he)
ite = np.linspace(te.min(), te.max(), 500)
ihe = eSpline(ite)

tSpline = make_interp_spline(tt,ht)
itt = np.linspace(tt.min(), tt.max(), 500)
iht = tSpline(itt)

target_altitude = np.ones(num)*300
ite = np.linspace(te.min(), te.max(), 500)
itt = np.linspace(tt.min(), tt.max(), 500)
plt.plot(te,target_altitude,color='k',linestyle='dashed',linewidth=1)

plt.scatter(te,he,color='blue',marker='^')
plt.scatter(tt,ht,color='red',marker='o')
plt.legend(['target altitude', 'minimum energy', 'minimum time'], frameon=False)

plt.plot(ite,ihe,color='blue',linestyle='solid',linewidth=2)
plt.plot(itt,iht,color='red',linestyle='solid',linewidth=2)
plt.xlabel('time (s)')
plt.ylabel('altitude (m)')
plt.savefig('new_h_vs_t.png', dpi=1200, bbox_inches='tight')
plt.show()
#endregion


#region xt
# x vs t
plt.rcParams['figure.figsize'] = [5, 2]
eSpline = make_interp_spline(te,xe)
ite = np.linspace(te.min(), te.max(), 500)
ixe = eSpline(ite)

tSpline = make_interp_spline(tt,xt)
itt = np.linspace(tt.min(), tt.max(), 500)
ixt = tSpline(itt)

plt.scatter(te,xe,color='blue',marker='^')
plt.scatter(tt,xt,color='red',marker='o')
plt.legend(['minimum energy', 'minimum time'], frameon=False)

plt.plot(ite,ixe,color='blue',linestyle='solid',linewidth=2)
plt.plot(itt,ixt,color='red',linestyle='solid',linewidth=2)
plt.xlabel('time (s)')
plt.ylabel('horizontal displacement (m)')
plt.savefig('new_x_vs_t.png', dpi=1200, bbox_inches='tight')
plt.show()
#endregion


#region pt
"""
# power vs t
plt.rcParams['figure.figsize'] = [5, 2.5]
eSpline = make_interp_spline(te,cxe)
ite = np.linspace(te.min(), te.max(), 500)
icxe = eSpline(ite)

tSpline = make_interp_spline(tt,cxt)
itt = np.linspace(tt.min(), tt.max(), 500)
icxt = tSpline(itt)

plt.plot(ite,icxe,color='k',linestyle='solid',linewidth=2)
plt.plot(itt,icxt,color='indianred',linestyle='solid',linewidth=2)
plt.xlabel('time (s)')
plt.ylabel('cruise rotor speed (RPM)')
plt.legend(['minimum energy', 'minimum time'], frameon=False)
plt.savefig('cx_vs_t.png', dpi=1200, bbox_inches='tight')
plt.show()
"""
#endregion


#region vt
# v vs t
plt.rcParams['figure.figsize'] = [5, 2]

eSpline = make_interp_spline(te,ve)
ite = np.linspace(te.min(), te.max(), 500)
ive = eSpline(ite)

eSpline = make_interp_spline(tt,vt)
itt = np.linspace(tt.min(), tt.max(), 500)
ivt = eSpline(itt)

target_velocity = np.ones(num)*43
plt.plot(te,target_velocity,color='k',linestyle='dashed',linewidth=1)
plt.scatter(te,ve,color='blue',marker='^')
plt.scatter(tt,vt,color='red',marker='o')
plt.legend(['target velocity', 'minimum energy', 'minimum time'], frameon=False)

plt.plot(ite,ive,color='blue',linestyle='solid',linewidth=2)
plt.plot(itt,ivt,color='red',linestyle='solid',linewidth=2)
plt.xlabel('time (s)')
plt.ylabel('velocity (m/s)')
plt.savefig('new_v_vs_t.png', dpi=1200, bbox_inches='tight')
plt.show()
#endregion


#region at
# a vs t
plt.rcParams['figure.figsize'] = [5, 2]

eSpline = make_interp_spline(te,np.rad2deg(ae))
ite = np.linspace(te.min(), te.max(), 500)
iae = eSpline(ite)

eSpline = make_interp_spline(tt,np.rad2deg(at))
itt = np.linspace(tt.min(), tt.max(), 500)
iat = eSpline(itt)

plt.scatter(te,np.rad2deg(ae),color='blue',marker='^')
plt.scatter(tt,np.rad2deg(at),color='red',marker='o')
plt.legend(['minimum energy', 'minimum time'], frameon=False)

plt.plot(ite,iae,color='blue',linestyle='solid',linewidth=2)
plt.plot(itt,iat,color='red',linestyle='solid',linewidth=2)
plt.xlabel('time (s)')
plt.ylabel('angle of attack ' r'($^{\circ}$)')
plt.savefig('new_a_vs_t.png', dpi=1200, bbox_inches='tight')
plt.show()
#endregion


#region gt
# g vs t
plt.rcParams['figure.figsize'] = [5, 2]

eSpline = make_interp_spline(te,np.rad2deg(ge))
ite = np.linspace(te.min(), te.max(), 500)
ige = eSpline(ite)

eSpline = make_interp_spline(tt,np.rad2deg(gt))
itt = np.linspace(tt.min(), tt.max(), 500)
igt = eSpline(itt)

plt.scatter(te,np.rad2deg(ge),color='blue',marker='^')
plt.scatter(tt,np.rad2deg(gt),color='red',marker='o')
plt.legend(['minimum energy', 'minimum time'], frameon=False)

plt.plot(ite,ige,color='blue',linestyle='solid',linewidth=2)
plt.plot(itt,igt,color='red',linestyle='solid',linewidth=2)
plt.xlabel('time (s)')
plt.ylabel('flight path angle ' r'($^{\circ}$)')
plt.savefig('new_g_vs_t.png', dpi=1200, bbox_inches='tight')
plt.show()
#endregion


# region cxt
# cx vs t
plt.rcParams['figure.figsize'] = [5, 2]

eSpline = make_interp_spline(te,cxe)
ite = np.linspace(te.min(), te.max(), 500)
icxe = eSpline(ite)

eSpline = make_interp_spline(tt,cxt)
itt = np.linspace(tt.min(), tt.max(), 500)
icxt = eSpline(itt)

plt.scatter(te,cxe,color='blue',marker='^')
plt.scatter(tt,cxt,color='red',marker='o')
plt.legend(['minimum energy', 'minimum time'], frameon=False)

plt.plot(ite,icxe,color='blue',linestyle='solid',linewidth=2)
plt.plot(itt,icxt,color='red',linestyle='solid',linewidth=2)

plt.ylim(1000,3000)

plt.xlabel('time (s)')
plt.ylabel('cruise rotor speed (rpm)')
plt.savefig('new_cx_vs_t.png', dpi=1200, bbox_inches='tight')
plt.show()
#endregion


#region czt
# cz vs t
plt.rcParams['figure.figsize'] = [5, 2]

eSpline = make_interp_spline(te,cze)
ite = np.linspace(te.min(), te.max(), 500)
icze = eSpline(ite)

eSpline = make_interp_spline(tt,czt)
itt = np.linspace(tt.min(), tt.max(), 500)
iczt = eSpline(itt)

plt.scatter(te,cze,color='blue',marker='^')
plt.scatter(tt,czt,color='red',marker='o')
plt.legend(['minimum energy', 'minimum time'], frameon=False)

plt.plot(ite,icze,color='blue',linestyle='solid',linewidth=2)
plt.plot(itt,iczt,color='red',linestyle='solid',linewidth=2)
plt.xlabel('time (s)')
plt.ylabel('lift rotor speed (rpm)')
plt.savefig('new_cz_vs_t.png', dpi=1200, bbox_inches='tight')
plt.show()
#endregion


#region splt
# spl vs t
plt.rcParams['figure.figsize'] = [5, 2]

eSpline = make_interp_spline(te,sple)
ite = np.linspace(te.min(), te.max(), 500)
isple = eSpline(ite)

eSpline = make_interp_spline(tt,splt)
itt = np.linspace(tt.min(), tt.max(), 500)
isplt = eSpline(itt)

plt.scatter(te,sple,color='blue',marker='^')
plt.scatter(tt,splt,color='red',marker='o')
plt.legend(['minimum energy', 'minimum time'], frameon=False)

plt.plot(ite,isple,color='blue',linestyle='solid',linewidth=2)
plt.plot(itt,isplt,color='red',linestyle='solid',linewidth=2)
plt.xlabel('time (s)')
plt.ylabel('sound pressure level (db)')
plt.savefig('new_spl_vs_t.png', dpi=1200, bbox_inches='tight')
plt.show()
#endregion