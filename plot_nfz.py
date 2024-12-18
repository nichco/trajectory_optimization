import numpy as np
import matplotlib.pyplot as plt
from smt.surrogate_models import RBF
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 12})

n = 3000
x_lim = 12000.0
be = 10
pi = 120
pf = 12000
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
dte = 4.11975845
#dtt = 
te = np.linspace(0,num*dte,num)
#tt = np.linspace(0,num*dtt,num)

# region energy

he = np.array([  0.        , 42.28155705, 88.16584767, 99.87484325,100.0169814 ,
  99.99328009,100.12973573,100.09777405,100.13358621,100.13923952,
 100.15518655,100.16671775,100.17653949,100.18768022,100.19396397,
 100.19883488,100.21056598,100.21870754,100.22829137,100.24644146,
 100.26301942,100.29719305,100.2632508 ,100.74951096,105.82091874,
 110.78937695,115.25205608,119.90341595,124.82692721,129.94864379,
 135.20566483,140.46597026,145.63557032,150.872734  ,156.23723284,
 161.61712727,167.12972553,172.57321487,177.45266215,181.22105002,
 183.52887289,185.94563218,192.86498192,211.679331  ,247.18020354,
 285.33748348,300.00011917])
xe = np.array([    0.        ,  0.85814615,   41.08824677,  153.03519442,
   297.11204083,  471.20902569,  662.92844808,  867.57521712,
  1082.77846726, 1307.09452596, 1539.38874839, 1778.76889153,
  2024.51374307, 2276.00342566, 2532.73843836, 2794.30129245,
  3060.27978791, 3330.37889895, 3604.36070114, 3881.92979844,
  4162.94036452, 4447.20713894, 4734.59239012, 5024.99272227,
  5316.43494772, 5607.7766367 , 5899.45536201, 6191.45275332,
  6483.63000737, 6775.86398993, 7068.06745694, 7360.21845169,
  7652.36598274, 7944.520072  , 8236.61859424, 8528.64510521,
  8820.55826758, 9112.34253327, 9404.21266946, 9696.67143598,
  9990.50468411,10286.07788867,10582.00496453,10872.81035059,
 11148.70942909,11398.54205844,11638.22474854])
ve = np.array([ 0.625     ,20.73637247,23.87388433,31.10259945,39.13684664,44.7381626 ,
 48.21814203,51.02995883,53.39243509,55.45896816,57.27757776,58.90533617,
 60.37061257,61.69947884,62.92123196,64.04083239,65.07136849,66.04501657,
 66.94856254,67.79939369,68.61176164,69.38494696,70.13765613,70.74697204,
 70.7231777 ,70.75889933,70.85323431,70.91441319,70.94276043,70.94497255,
 70.93187434,70.92274079,70.9273702 ,70.92305108,70.90460374,70.88616907,
 70.85143733,70.83269043,70.89919638,71.12526891,71.5425998 ,71.90922309,
 71.59232011,69.57816006,64.91507596,58.97080888,58.00000513])
ge = np.array([ 0.00000000e+00, 1.25311190e+00, 2.05315317e-01, 3.44693779e-02,
 -1.62191668e-02, 5.12671450e-03,-1.18421451e-03, 2.71423607e-04,
 -4.89885106e-07, 1.66653956e-05, 4.62059591e-05, 1.77705834e-05,
  3.25202288e-05, 3.10267023e-05,-2.66989758e-06, 3.10596094e-05,
  4.33446655e-05, 3.25587799e-06, 6.59255474e-05, 6.23484686e-05,
  9.40859297e-06, 4.24228801e-04,-1.59392870e-03, 9.79347382e-03,
  1.96656950e-02, 1.54382798e-02, 1.54481713e-02, 1.64125082e-02,
  1.72250131e-02, 1.78082485e-02, 1.80934722e-02, 1.78225547e-02,
  1.76996945e-02, 1.81997869e-02, 1.83781730e-02, 1.86274015e-02,
  1.90145067e-02, 1.80003015e-02, 1.52137237e-02, 1.01284670e-02,
  6.46747507e-03, 1.16287976e-02, 4.02613210e-02, 8.99326753e-02,
  1.75482517e-01, 1.14667878e-01, 3.74060543e-07])
cxe = np.array([1478.46115449,1470.10925412,1562.10905279,1591.39211652,1620.71694832,
 1222.52344219,1130.18735388,1058.99541098,1016.82168465, 978.55505587,
  948.98588448, 924.1583309 , 901.78114123, 883.89836611, 869.80140038,
  853.06603777, 843.0659189 , 837.01471622, 822.09687294, 822.60588068,
  812.67618177, 814.75534446, 803.33252653, 810.96531208, 805.13246131,
  810.43167314, 807.38603351, 809.76566938, 810.16772161, 810.6499241 ,
  811.77893695, 812.30724735, 813.12877112, 814.01286968, 814.71286412,
  815.56664069, 816.27369657, 816.75306621, 817.57147671, 817.6235195 ,
  818.59952304, 819.24051539, 825.72287246, 827.46491127, 822.04011844,
  750.94244555, 665.06721531])
cze = np.array([1.13821917e+03,1.09446509e+03,1.12690496e+03,8.29571025e+02,
 3.37995298e+02,5.66047377e+01,4.39210431e-13,0.00000000e+00,
 2.79260465e-01,1.00518278e+00,7.76069533e-16,7.52788523e-03,
 9.53369801e-17,1.41179823e-02,1.22805115e-01,6.41379886e-01,
 4.52593028e-01,0.00000000e+00,1.39887898e-03,2.21744461e-03,
 2.86787025e-01,0.00000000e+00,6.33448075e-02,1.13759122e-02,
 0.00000000e+00,8.18492369e-02,0.00000000e+00,9.55876546e-04,
 5.80739234e-04,1.88527630e-04,5.16411321e-04,3.82985648e-04,
 3.66161572e-04,2.55238998e-04,3.75824665e-04,3.36522094e-04,
 3.51610526e-04,3.38129408e-04,3.95904537e-04,2.92982470e-04,
 3.97784093e-04,4.23260401e-04,2.54015112e-04,3.25710174e-04,
 2.08532422e-04,1.09107619e-04,3.27797101e-04])
control_alpha_e = np.array([ 0.00002106e-01,-1.57079633e+00,-1.06808973e-01, 9.95546301e-02,
  1.80328919e-01, 1.11537230e-01, 8.77137289e-02, 6.90088090e-02,
  5.57646803e-02, 4.53953358e-02, 3.69577038e-02, 2.99735312e-02,
  2.40801226e-02, 1.90318764e-02, 1.46264206e-02, 1.07969402e-02,
  7.41091238e-03, 4.33644710e-03, 1.61460261e-03,-8.72971619e-04,
 -3.20470446e-03,-5.11682965e-03,-8.05478906e-03,-4.71948298e-03,
 -9.86174493e-03,-8.93474880e-03,-8.84661732e-03,-8.95377788e-03,
 -9.04065615e-03,-9.01492466e-03,-9.01147869e-03,-9.03448037e-03,
 -8.86732783e-03,-8.75828845e-03,-8.81252198e-03,-8.55438294e-03,
 -8.53887935e-03,-8.74007720e-03,-9.09723190e-03,-1.00852592e-02,
 -1.02435221e-02,-9.37937393e-03,-3.40340583e-03, 2.91180094e-03,
  2.60424904e-02,-9.29974886e-03, 3.65392422e-02])
cruisepower_e = np.array([468299.97954046,468299.94374243,468299.6743397 ,468296.85219908,
 466600.97276716,190022.86231498,145348.96180435,116402.10381956,
 100700.25066723, 87936.85191469, 78750.0518526 , 71531.2478179 ,
  65459.96989561, 60789.91104559, 57181.85131644, 53300.60917359,
  50876.73122311, 49261.38366362, 46210.59946574, 45859.49106352,
  43816.7383175 , 43768.43701823, 41594.64253212, 42487.73297587,
  41571.74787242, 42359.48079425, 41819.86902668, 42141.97822849,
  42170.95473893, 42224.36453496, 42386.01758046, 42451.8369297 ,
  42557.15596882, 42676.64625177, 42773.93248355, 42895.3026171 ,
  43001.44462809, 43064.16806645, 43140.3943287 , 43020.53027165,
  42955.55241232, 42861.07685068, 44017.28257988, 45258.68271917,
  46602.30833229, 37636.31991024, 26397.17256168])
liftpower_e = np.array([1.43651997e+05,1.43651860e+05,1.43651793e+05,5.62171788e+04,
 3.79392217e+03,1.83907594e+01,8.73873221e-42,0.00000000e+00,
 2.30763695e-06,1.08787027e-04,5.05509678e-50,4.65392447e-11,
 9.52807512e-53,3.11645455e-10,2.06480222e-07,2.95958015e-05,
 1.04583548e-05,0.00000000e+00,3.12015204e-13,1.24865190e-12,
 2.71348519e-06,0.00000000e+00,2.94975282e-08,1.71149467e-10,
 0.00000000e+00,6.37772212e-08,0.00000000e+00,1.01571414e-13,
 2.27706244e-14,7.78651668e-16,1.59940296e-14,6.52052253e-15,
 5.69538113e-15,1.92797772e-15,6.15122610e-15,4.41312777e-15,
 5.03021269e-15,4.47106938e-15,7.17659656e-15,2.91155270e-15,
 7.30025925e-15,8.80565590e-15,1.89543734e-15,3.94256252e-15,
 1.00184520e-15,1.40824890e-16,3.74781441e-15])
ee = np.array([       0.        , 6974232.82212877,14207481.19978415,19672141.98915203,
 22563847.41839676,24001147.11934444,24742479.13994263,25320120.75355702,
 25799253.01960568,26214989.34442957,26581987.16563668,26912520.62097293,
 27213511.73412088,27490667.52308528,27749454.44398853,27991589.71365783,
 28219782.92300061,28439022.32093351,28647871.62138601,28849244.46729308,
 29045266.36149713,29236676.56445886,29423140.78199486,29606674.81417298,
 29790202.06796923,29973514.06071341,30157338.90624485,30340683.36560937,
 30524797.54267183,30709093.79128472,30893866.07209251,31079142.63809045,
 31264793.62998377,31450935.39923488,31637557.89083212,31824660.085993  ,
 32012264.94540451,32200253.25436245,32388557.70907582,32576774.30745666,
 32764550.16579141,32951888.51067276,33141372.30165102,33336076.01031683,
 33536380.64366516,33721200.48250993,33860621.07473098])
sple = np.array([143.3296713 ,111.78299126,107.04958931, 98.25898247, 95.64277167,
  87.90966915, 85.58868945, 83.74502875, 82.56195509, 81.46927743,
  80.59256703, 79.83730921, 79.1446318 , 78.57581001, 78.11569169,
  77.57544661, 77.23783874, 77.02570829, 76.54538171, 76.55782574,
  76.25047004, 76.32327634, 76.00269464, 76.16701797, 75.60382195,
  75.35406953, 74.92187797, 74.66969851, 74.34758954, 74.02748569,
  73.72985775, 73.42014879, 73.14028313, 72.87487376, 72.60225131,
  72.34756541, 72.08984557, 71.82102143, 71.57973179, 71.36843934,
  71.30532618, 71.20389767, 71.44087685, 71.25972233, 70.77612705,
  65.77058658, 61.37412251])

# endregion


# region time
"""
ht = np.array()
xt = np.array()
vt = np.array()
gt = np.array()
cxt = np.array()
czt = np.array()
control_alpha_t = np.array()
cruisepower_t = np.array()
liftpower_t = np.array()
et = np.array()
splt = np.array()
"""
# endregion


num_obs = 5000
x_p = np.linspace(0,x_lim,num_obs)
obs_p = sm.predict_values(x_p)

"""
plt.rcParams['figure.figsize'] = [11, 2.5]
plt.figure(layout='constrained')

plt.plot(xe,np.ones(num)*300,color='k',linestyle='dashed',linewidth=1)
plt.scatter(xe,he,color='blue',marker='^',alpha=0.3,linewidth=0.3, edgecolor='k',s=50)
#plt.scatter(xt,ht,color='red',marker='o',alpha=0.3,linewidth=0.3, edgecolor='k',s=50)
plt.fill_between(x_p,obs_p.flatten(),alpha=0.8,color='mistyrose',hatch='///',edgecolor='indianred')
plt.legend(['target altitude', 'minimum energy takeoff', 'no-fly zone'], frameon=False)

plt.plot(xe,he,color='blue',linewidth=2)
#plt.plot(xt,ht,color='red',linewidth=2)
plt.ylim(0, 400)
plt.xlim(-50,xe.max())
plt.xlabel('horizontal position (m)')
plt.ylabel('altitude (m)')

plt.savefig('hx_nfz.png', dpi=1200, bbox_inches='tight')
plt.show()
"""

"""
plt.rcParams['figure.figsize'] = [11, 5]
plt.figure(layout='constrained')

plt.subplot(2,2,1)
plt.plot(te,np.ones(num)*58,color='k',linestyle='dashed',linewidth=1)
plt.scatter(te,ve,color='blue',marker='^',alpha=0.3,linewidth=0.3, edgecolor='k',s=50)
#plt.scatter(tt,vt,color='red',marker='o',alpha=0.3,linewidth=0.3, edgecolor='k',s=50)
plt.legend(['target velocity', 'minimum energy takeoff', 'minimum time takeoff'], frameon=False)
plt.plot(te,ve,color='blue',linewidth=2)
#plt.plot(tt,vt,color='red',linewidth=2)
plt.xlabel('time (s)')
plt.ylabel('velocity (m/s)')
plt.xlim(0,te.max())


plt.subplot(2,2,2)
plt.scatter(te,np.rad2deg(ge),color='blue',marker='^',alpha=0.3,linewidth=0.3, edgecolor='k',s=50)
#plt.scatter(tt,np.rad2deg(gt),color='red',marker='o',alpha=0.3,linewidth=0.3, edgecolor='k',s=50)
plt.legend(['minimum energy takeoff', 'minimum time takeoff'], frameon=False)
plt.plot(te,np.rad2deg(ge),color='blue',linewidth=2)
#plt.plot(tt,np.rad2deg(gt),color='red',linewidth=2)
plt.xlabel('time (s)')
plt.ylabel('flight path angle ' r'($^{\circ}$)')
plt.xlim(0,te.max())


plt.subplot(2,2,3)
plt.scatter(te,np.rad2deg(control_alpha_e),color='blue',marker='^',alpha=0.3,linewidth=0.3, edgecolor='k',s=50)
#plt.scatter(tt,np.rad2deg(control_alpha_t),color='red',marker='o',alpha=0.3,linewidth=0.3, edgecolor='k',s=50)
plt.legend(['minimum energy takeoff', 'minimum time takeoff'], frameon=False)
plt.plot(te,np.rad2deg(control_alpha_e),color='blue',linewidth=2)
#plt.plot(tt,np.rad2deg(control_alpha_t),color='red',linewidth=2)
plt.xlabel('time (s)')
plt.ylabel('angle of attack ' r'($^{\circ}$)')
plt.xlim(0,te.max())


plt.subplot(2,2,4)
plt.scatter(te,np.rad2deg(control_alpha_e + ge),color='blue',marker='^',alpha=0.3,linewidth=0.3, edgecolor='k',s=50)
#plt.scatter(tt,np.rad2deg(control_alpha_t + gt),color='red',marker='o',alpha=0.3,linewidth=0.3, edgecolor='k',s=50)
plt.legend(['minimum energy takeoff', 'minimum time takeoff'], frameon=False)
plt.plot(te,np.rad2deg(control_alpha_e + ge),color='blue',linewidth=2)
#plt.plot(tt,np.rad2deg(control_alpha_t + gt),color='red',linewidth=2)
plt.xlabel('time (s)')
plt.ylabel('pitch angle ' r'($^{\circ}$)')
plt.xlim(0,te.max())

plt.savefig('s1_nfz.png', dpi=1200, bbox_inches='tight')
plt.show()
"""



plt.rcParams['figure.figsize'] = [11, 5]
plt.figure(layout='constrained')

plt.subplot(2,2,1)
plt.scatter(te,cxe,color='blue',marker='^',alpha=0.3,linewidth=0.3, edgecolor='k',s=50)
#plt.scatter(tt,cxt,color='red',marker='o',alpha=0.3,linewidth=0.3, edgecolor='k',s=50)
plt.legend(['minimum energy', 'minimum time'], frameon=False)
plt.plot(te,cxe,color='blue',linewidth=2)
#plt.plot(tt,cxt,color='red',linewidth=2)
plt.xlabel('time (s)')
plt.ylabel('cruise rotor speed (rpm)')

plt.subplot(2,2,2)
plt.scatter(te,cze,color='blue',marker='^',alpha=0.3,linewidth=0.3, edgecolor='k',s=50)
#plt.scatter(tt,czt,color='red',marker='o',alpha=0.3,linewidth=0.3, edgecolor='k',s=50)
plt.legend(['minimum energy', 'minimum time'], frameon=False)
plt.plot(te,cze,color='blue',linewidth=2)
#plt.plot(tt,czt,color='red',linewidth=2)
plt.xlabel('time (s)')
plt.ylabel('lift rotor speed (rpm)')

plt.subplot(2,2,3)
plt.scatter(te,ee/1E6,color='blue',marker='^',alpha=0.3,linewidth=0.3, edgecolor='k',s=50)
#plt.scatter(tt,et/1E6,color='red',marker='o',alpha=0.3,linewidth=0.3, edgecolor='k',s=50)
plt.legend(['minimum energy', 'minimum time'], frameon=False)
plt.plot(te,ee/1E6,color='blue',linewidth=2)
#plt.plot(tt,et/1E6,color='red',linewidth=2)
plt.xlabel('time (s)')
plt.ylabel('energy (MJ)')

plt.subplot(2,2,4)
plt.scatter(te,sple,color='blue',marker='^',alpha=0.3,linewidth=0.3, edgecolor='k',s=50)
#plt.scatter(tt,splt,color='red',marker='o',alpha=0.3,linewidth=0.3, edgecolor='k',s=50)
plt.legend(['minimum energy', 'minimum time'], frameon=False)
plt.plot(te,sple,color='blue',linewidth=2)
#plt.plot(tt,splt,color='red',linewidth=2)
plt.xlabel('time (s)')
plt.ylabel('sound pressure level (db)')

plt.savefig('s2_nfz.png', dpi=1200, bbox_inches='tight')
plt.show()
