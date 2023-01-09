"""
Created on Tue Nov 22 18:04:26 2022

@author: Nicholas Orndorff
"""

def efficiency(e,h,v,m,g):
    hi = h[0]
    hf = h[-1]
    
    vi = v[0]
    vf = v[-1]
    
    dv = vf - vi
    dh = hf - hi
    
    ke = 0.5*m*dv**2
    pe = 0.5*m*g*dh
    
    eta = (ke + pe)/e
    
    return eta
    