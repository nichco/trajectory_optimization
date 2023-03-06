from efficiency import efficiency
import numpy as np


h = np.array([300.        ,302.48571804,302.72640155,302.69623638,299.91068637,
 294.6970981 ,287.96958419,281.49887185,277.33444715,276.008333  ,
 275.58107749,272.58109541,268.08309801,263.51020506,259.38059378,
 256.07617008,253.7022344 ,252.19192568,251.46385893,251.45837253,
 252.12894944,253.4312149 ,255.30025118,257.6343972 ,260.31502625,
 263.23213865,266.29290727,269.41735008,272.54173742,275.61678829,
 278.57576463,281.37388823,283.99153128,286.41869684,288.6524437 ,
 290.69095402,292.53332341,294.18165174,295.63255837,296.89137041,
 297.97071279,298.87271846,299.5606859 ,299.91787623,299.98932862])
v = np.array([ 1.5       , 3.40821511, 8.02189779,10.97772336,15.8477505 ,20.70977649,
 25.29128228,28.97361433,31.7362305 ,34.3589013 ,36.9392613 ,39.64936672,
 42.28426664,44.83629517,47.34324807,49.79772326,52.19745142,54.53581304,
 56.80652326,59.01157704,61.13473971,63.08580645,64.72649867,65.9527888 ,
 66.78181854,67.29838876,67.53800499,67.52311506,67.27827348,66.82535271,
 66.24083196,65.59793964,64.9252029 ,64.24083284,63.55693495,62.88044213,
 62.22203666,61.58448982,60.96845665,60.37391442,59.79943236,59.24586809,
 58.7259064 ,58.26210338,58.00010424])

e = 15796063.6556642

g = 9.81
m = 3000

eta_e = efficiency(e,h,v,m,g)

print(eta_e)