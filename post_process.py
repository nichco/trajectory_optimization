import matplotlib.pyplot as plt

# post processing and plotting


def post(sim, options):
    
    # print total energy
    print('dt: ', sim['dt'])
    print('total energy: ', sim['energy']/options['energy_scale'])
    
    # assign variables for post-processing
    v = sim['v']
    gamma = sim['gamma']
    h = sim['h']
    x = sim['x']
    e = sim['e']
    dt = sim['dt']
    alpha = sim['control_alpha']
    dv = sim['dv']
    dgamma = sim['dgamma']
    lift = sim['lift']
    drag = sim['drag']
    control_x = sim['control_x']
    control_z = sim['control_z']
    cruisepower = sim['cruisepower']
    liftpower = sim['liftpower']
    #cruise_spl_gl = sim['max_cruise_spl_gl']
    #lift_spl_gl = sim['max_lift_spl_gl']
    ospl = sim['max_spl_gl']
    theta = sim['theta']
    
    
    # post-processing
    fig, ((ax1, ax2, ax3, ax4, ax5, ax6), (ax7, ax8, ax9, ax10, ax11, ax12)) = plt.subplots(2, 6)
    fig.suptitle('trajectory optimization')
    ax1.plot(v,color='b')
    ax1.legend(['v'])
    
    ax2.plot(gamma,color='g')
    ax2.plot(theta,color='r')
    ax2.legend(['gamma','theta'])
    
    ax3.plot(h,color='r')
    ax3.legend(['h'])
    
    ax4.plot(x,color='c')
    ax4.legend(['x'])
    
    ax5.plot(e,color='m')
    ax5.legend(['e'])
    
    ax6.plot(dv)
    ax6.plot(dgamma)
    ax6.legend(['dv','dgamma'])
    
    ax7.plot(alpha,color='k')
    ax7.set_title('alpha')
    ax7.set_ylabel('rad')
    
    ax8.plot(control_x,color='k')
    ax8.set_title('cruise rotor speed')
    ax8.set_ylabel('rotor speed (rpm)')
    
    ax9.plot(control_z,color='k')
    ax9.set_title('lift rotor speed')
    ax9.set_ylabel('rotor speed (rpm)')
    
    ax10.plot(cruisepower,color='k')
    ax10.plot(liftpower,color='r')
    ax10.set_title('power')
    ax10.set_ylabel('power (w)')
    
    #ax11.plot(cruise_spl_gl,color='k')
    #ax11.plot(lift_spl_gl,color='r')
    ax11.plot(ospl,color='c')
    ax11.set_title('spl')
    ax11.set_ylabel('spl (db)')
    
    ax12.plot(lift,color='k')
    ax12.plot(drag,color='r')
    ax12.legend(['lift','drag'])
    
    plt.show()
    
    
    
    
    
    
    
    
    
    