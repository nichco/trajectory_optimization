import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 12})
# plt.box(False)

# print(np.array2string(sim['x'],separator=','))

# num steps
num = 30
# timestep
dte = 2.66245201
dtt = 0.92450286
# x-axis time vectors
te = np.linspace(0,num*dte,num)
tt = np.linspace(0,num*dtt,num)
# total energy
ee = 12647649.77219404
et = 15531639.33530839

#region mine
# minimum energy objective
xe = np.array([   0.        ,  40.67036172, 112.11577654, 199.61122378, 296.05812808,
  399.50570306, 509.57992249, 626.19494   , 749.54628687, 878.9755276 ,
 1011.804107  ,1144.97142233,1276.8793721 ,1407.42794057,1537.28362987,
 1667.1695525 ,1797.50723869,1928.29216995,2059.20239389,2189.85828097,
 2320.09382987,2450.17544144,2580.8490989 ,2713.03724519,2847.16333708,
 2982.28783538,3115.47155009,3242.6225933 ,3361.59970126,3475.91855105])

he = np.array([ 0.00000000e+00,-6.28525524e-02, 2.75165914e-02,-1.87058392e-02,
  3.96533860e-02, 7.09659802e-02, 1.07459849e-01, 1.07946240e-01,
  1.51303738e-01, 3.44172530e+00, 1.29502808e+01, 2.75119482e+01,
  4.40608705e+01, 6.00352028e+01, 7.43821973e+01, 8.73923705e+01,
  9.98688057e+01, 1.12654030e+02, 1.26178762e+02, 1.40317573e+02,
  1.54473357e+02, 1.67740415e+02, 1.79409801e+02, 1.89708045e+02,
  2.00316915e+02, 2.14229956e+02, 2.34294203e+02, 2.60112774e+02,
  2.85652365e+02, 2.99991684e+02])

ve = np.array([ 5.        ,22.68382994,30.43496736,34.81487619,37.57102248,40.10932407,
 42.56806139,45.0479003 ,47.57870601,49.52769274,50.33241086,50.19389992,
 49.65258923,49.18354313,49.00463198,49.08311055,49.27566711,49.41837236,
 49.41861933,49.28714277,49.13066328,49.13512296,49.47775695,50.15837578,
 50.8730185 ,51.023168  ,49.92446614,47.33799953,44.18369662,42.99981117])

ae = np.array([0.89347   ,0.46590265,0.19463583,0.13910781,0.10018586,0.07219567,
 0.05281446,0.03266187,0.02510722,0.0207182 ,0.01340617,0.00874563,
 0.00701051,0.00767112,0.00951521,0.01073071,0.01152712,0.0117201 ,
 0.01162453,0.01141245,0.01065769,0.00934977,0.00808049,0.00781443,
 0.00966483,0.0145878 ,0.02072564,0.02620118,0.01879815,0.00521476])

ge = np.array([ 0.        , 0.0059949 ,-0.00423621, 0.00033767, 0.00050203, 0.00032443,
  0.00067741,-0.00190897, 0.00753902, 0.04711826, 0.0933818 , 0.12066237,
  0.12579744, 0.11641284, 0.10416555, 0.09648135, 0.09549591, 0.09993748,
  0.10581042, 0.10908488, 0.10626231, 0.09597036, 0.08230732, 0.0751856 ,
  0.0862875 , 0.12299197, 0.17704782, 0.2184582 , 0.18673146, 0.04879375])

cxe = np.array([1432.48275042,1745.0820869 ,1767.54533382,1431.38232297,1401.68360326,
 1387.6139432 ,1402.81942907,1431.95000698,1483.57434494,1529.8226077 ,
 1549.90212914,1549.20905727,1539.17835208,1528.72480251,1524.26390479,
 1526.52299135,1531.30264769,1535.41599635,1535.49475704,1531.88417805,
 1526.03007201,1524.91044307,1536.87085117,1561.40881915,1590.34289648,
 1603.16670197,1569.24343729,1474.4722664 ,1349.54218827,1281.66483142])

cze = np.array([1638.31947407,1106.6317184 , 683.9153001 , 359.57062733, 205.53383824,
  173.58328742, 107.55535577, 100.19005751,  99.99759615,  99.99753622,
   99.99742825,  99.99747533,  99.997748  ,  99.99811163,  99.99844396,
   99.99871013,  99.99889625,  99.99903272,  99.99913864,  99.99921668,
   99.9992719 ,  99.99931174,  99.99935007,  99.99940783,  99.99949852,
   99.99961388,  99.99972422,  99.99976711,  99.99968998,  99.99981136])

cpe = np.array([[144193.63027504],
 [233257.27337127],
 [224894.72709192],
 [115090.24535113],
 [105487.49097103],
 [100089.43558521],
 [101204.36037363],
 [105278.57470978],
 [114442.02242816],
 [123218.95904218],
 [127056.5489539 ],
 [126870.66654872],
 [124852.30484924],
 [122672.02788234],
 [121638.57494059],
 [121943.71996822],
 [122731.1995007 ],
 [123411.38720428],
 [123272.19639594],
 [122388.82300257],
 [121002.07633279],
 [120577.78006714],
 [122910.86789662],
 [127957.4874093 ],
 [134172.43220588],
 [137076.91146285],
 [129643.96814188],
 [109859.2479254 ],
 [ 86410.58146455],
 [ 74675.22872782]])

lpe = np.array([[1.68158897e+05],
 [5.06311594e+04],
 [1.25329978e+04],
 [1.85538869e+03],
 [3.51631732e+02],
 [2.14582575e+02],
 [5.16456942e+01],
 [4.22810362e+01],
 [4.24759752e+01],
 [4.28030323e+01],
 [4.29743568e+01],
 [4.29485982e+01],
 [4.28180307e+01],
 [4.26743982e+01],
 [4.25689319e+01],
 [4.25152002e+01],
 [4.24855962e+01],
 [4.24539982e+01],
 [4.24009896e+01],
 [4.23268131e+01],
 [4.22550040e+01],
 [4.22173349e+01],
 [4.22369465e+01],
 [4.23030652e+01],
 [4.23500403e+01],
 [4.22601972e+01],
 [4.19408701e+01],
 [4.14003872e+01],
 [4.09473289e+01],
 [4.08713748e+01]])

sple = np.array([103.33626292, 99.57464541, 96.18920581, 92.79270769, 91.79528984,
  91.51774483, 91.38507575, 91.46167072, 91.66688026, 91.31348434,
  88.72972147, 86.45385192, 84.97939193, 83.97732524, 83.25380432,
  82.74409157, 82.3400475 , 81.9867508 , 81.64168728, 81.29821597,
  80.96012959, 80.66708707, 80.47289452, 80.38476625, 80.36610701,
  80.30668832, 80.01373974, 79.34423079, 78.32613725, 77.44835434])
#endregion


# region mindt
# minimum time objective
xt = np.array([   0.        ,   8.23580089,  23.47055501,  44.38638487,  69.41619298,
   97.33860186, 127.28247944, 158.68106758, 191.69817324, 226.83827616,
  264.45627401, 304.74844785, 347.74383413, 393.29077701, 441.07591669,
  490.71167994, 541.7521186 , 593.61797684, 645.72689873, 697.50472778,
  748.39695341, 797.92527484, 845.71259261, 891.48734304, 935.09661552,
  976.38363818,1015.47094205,1052.5591669 ,1087.94291404,1121.88244314])

ht = np.array([ 0.00000000e+00, 6.93358566e-02,-1.00170667e-02,-7.61759172e-02,
  1.24386934e+00, 4.05388889e+00, 8.42957121e+00, 1.42938561e+01,
  1.96346978e+01, 2.30501155e+01, 2.45960026e+01, 2.51881573e+01,
  2.56900169e+01, 2.69926950e+01, 2.96840894e+01, 3.40421000e+01,
  4.04287599e+01, 4.94181687e+01, 6.10707142e+01, 7.54044332e+01,
  9.23418505e+01, 1.11642892e+02, 1.32949402e+02, 1.55836065e+02,
  1.79825649e+02, 2.04584092e+02, 2.29472070e+02, 2.53956198e+02,
  2.77547270e+02, 2.99927287e+02])

vt = np.array([ 5.        ,12.82271641,19.90517245,25.06536617,28.92348045,31.65561838,
 33.72290662,35.33661809,37.09935993,39.38247541,42.12812579,45.05626783,
 47.93888267,50.58650379,52.89599406,54.83767256,56.37489468,57.43081151,
 58.01715342,58.144849  ,57.8307285 ,57.11139355,56.03232099,54.64250607,
 52.99664967,51.12232661,49.10759415,47.03108015,44.97490081,43.00402133])

at = np.array([ 6.16271544e-01, 8.65463251e-01, 9.90107723e-01, 4.43738867e-01,
  3.54706372e-01, 2.49634588e-01, 1.64405687e-01, 3.83913477e-02,
  6.48541002e-03, 4.48538080e-03, 1.64942369e-02, 1.58302201e-02,
  1.56872561e-02, 9.39476129e-03, 2.02313060e-03,-1.84628075e-03,
  1.96555341e-03,-2.04516482e-03,-1.87169814e-03,-1.56045926e-03,
 -1.27024554e-03,-1.08156197e-03, 4.62369201e-05,-2.96683591e-04,
  5.79979839e-03, 3.20515396e-03, 5.41785473e-03, 4.04073863e-03,
  1.28898328e-02, 9.69354119e-06])

gt = np.array([ 0.        , 0.00572257,-0.01459251, 0.02191502, 0.07812616, 0.12139728,
  0.1692967 , 0.18528108, 0.13078334, 0.06533562, 0.02324528, 0.00962528,
  0.01732539, 0.0413155 , 0.07131656, 0.10434632, 0.14691078, 0.1957391 ,
  0.24466201, 0.29565867, 0.34678557, 0.39603557, 0.44244606, 0.4837827 ,
  0.52264046, 0.55553145, 0.57724748, 0.58723168, 0.58853005, 0.57147714])

cxt = np.array([2113.18275621,2126.0893834 ,2149.68675965,2213.94806941,2238.90327191,
 2260.92102643,2277.95252076,2291.66968097,2304.56438828,2318.86488845,
 2337.29880341,2358.14196734,2378.62802916,2398.49828784,2415.56162553,
 2431.62982299,2444.04217887,2452.91148091,2459.26561203,2460.03821619,
 2458.91724884,2454.67232855,2447.74202727,2437.95609254,2427.10505937,
 2414.69209788,2402.44951532,2389.71991703,2376.6559932 ,2363.17826856])

czt = np.array([1386.32366273,1379.01599481,1352.13263611,1153.93518207, 936.79744806,
  763.80065247, 664.88014458, 596.09219625, 538.42224714, 493.78065467,
  470.99409117, 444.99857691, 449.23781422, 458.06378796, 443.9687658 ,
  428.02846915, 402.17004487, 366.89480247, 331.66057105, 297.94748456,
  261.19132786, 229.43816113, 197.8223999 , 168.18468794, 138.34289912,
  112.30607405, 100.03654385, 100.04349922, 100.05216337, 100.01703131])

cpt = np.array([[459985.73588615],
 [457508.03346247],
 [468637.33733058],
 [468546.90336453],
 [468370.76477028],
 [468255.17544735],
 [468222.608811  ],
 [467902.37333229],
 [468650.98738568],
 [468289.10253284],
 [468437.42694409],
 [468912.04084124],
 [468936.93305538],
 [469121.80521325],
 [468741.91885929],
 [469103.66638545],
 [468916.15162146],
 [468695.21343937],
 [469064.60311507],
 [468271.24288737],
 [468361.26556351],
 [468447.69503535],
 [468536.33297047],
 [468257.74150478],
 [468354.64875842],
 [468349.31752255],
 [468861.94696999],
 [469154.66641394],
 [469018.13764531],
 [468086.04285297]])

lpt = np.array([[1.02570670e+05],
 [9.67756429e+04],
 [8.72736531e+04],
 [5.74506992e+04],
 [3.11783817e+04],
 [1.72809534e+04],
 [1.16340225e+04],
 [8.63597461e+03],
 [6.43424671e+03],
 [4.99631515e+03],
 [4.35959282e+03],
 [3.71186828e+03],
 [3.85643107e+03],
 [4.13359611e+03],
 [3.80317932e+03],
 [3.43629853e+03],
 [2.86305955e+03],
 [2.18390964e+03],
 [1.61525800e+03],
 [1.16999138e+03],
 [7.85860180e+02],
 [5.30113386e+02],
 [3.37506140e+02],
 [2.05832033e+02],
 [1.13372611e+02],
 [6.01261812e+01],
 [4.20568897e+01],
 [4.16756025e+01],
 [4.12106852e+01],
 [4.09445152e+01]])

splt = np.array([101.87667103,102.21056089,102.07265058,100.46292652, 99.37854002,
  98.03199616, 96.58880886, 95.18044238, 93.72922598, 92.67400365,
  92.1910186 , 91.94515566, 91.91063947, 91.84047928, 91.51048578,
  91.05705144, 90.43062603, 89.61644002, 88.7799018 , 88.01858393,
  87.30328939, 86.67676379, 86.13038854, 85.65373936, 85.2521069 ,
  84.89597058, 84.60245531, 84.34130633, 84.10942531, 83.86027327])
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

plt.savefig('h_vs_x.png', dpi=1200, bbox_inches='tight')
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
plt.savefig('h_vs_t.png', dpi=1200, bbox_inches='tight')
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
plt.savefig('x_vs_t.png', dpi=1200, bbox_inches='tight')
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
plt.savefig('v_vs_t.png', dpi=1200, bbox_inches='tight')
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
plt.savefig('a_vs_t.png', dpi=1200, bbox_inches='tight')
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
plt.savefig('g_vs_t.png', dpi=1200, bbox_inches='tight')
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
plt.savefig('cx_vs_t.png', dpi=1200, bbox_inches='tight')
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
plt.savefig('cz_vs_t.png', dpi=1200, bbox_inches='tight')
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
plt.savefig('spl_vs_t.png', dpi=1200, bbox_inches='tight')
plt.show()
