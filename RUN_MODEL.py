

# RUN_MODEL

# system evaluation block

# op _005c_power_combination_eval
# REP:  v01_v --> v036__005d
# LANG: v --> _005d
# full namespace: 
v036__005d = (v01_v**1)
v036__005d = (v036__005d*_005c_coeff).reshape((1,))

# op _005k_power_combination_eval
# REP:  v01_v --> v040__005l
# LANG: v --> _005l
# full namespace: 
v040__005l = (v01_v**1)
v040__005l = (v040__005l*_005k_coeff).reshape((1,))

# op _005u_power_combination_eval
# REP:  v01_v --> v045__005v
# LANG: v --> _005v
# full namespace: 
v045__005v = (v01_v**1)
v045__005v = (v045__005v*_005u_coeff).reshape((1,))

# op _0068_power_combination_eval
# REP:  v01_v --> v064__0069
# LANG: v --> _0069
# full namespace: aero
v064__0069 = (v01_v**2)
v064__0069 = (v064__0069*_0068_coeff).reshape((1,))

# op _0056_sin_eval
# REP:  v02_gamma --> v033__0057
# LANG: gamma --> _0057
# full namespace: 
v033__0057 = np.sin(v02_gamma)

# op _005A_cos_eval
# REP:  v02_gamma --> v048__005B
# LANG: gamma --> _005B
# full namespace: 
v048__005B = np.cos(v02_gamma)

# op _005I_sin_eval
# REP:  v02_gamma --> v052__005J
# LANG: gamma --> _005J
# full namespace: 
v052__005J = np.sin(v02_gamma)

# op _005M_cos_eval
# REP:  v02_gamma --> v054__005N
# LANG: gamma --> _005N
# full namespace: 
v054__005N = np.cos(v02_gamma)

# op _006r_custom_explicit_eval
# REP:  v03_h --> v072_pressure, v073_density
# LANG: h --> pressure, density
# full namespace: aero.atmosphere
temp = _006r_custom_explicit_func_pressure.solve(v03_h)
v072_pressure = temp[0].copy()
v073_density = temp[1].copy()

# op _0049_cos_eval
# REP:  v06_control_alpha --> v07__004a
# LANG: control_alpha --> _004a
# full namespace: 
v07__004a = np.cos(v06_control_alpha)

# op _004d_sin_eval
# REP:  v06_control_alpha --> v09__004e
# LANG: control_alpha --> _004e
# full namespace: 
v09__004e = np.sin(v06_control_alpha)

# op _004s_sin_eval
# REP:  v06_control_alpha --> v015__004t
# LANG: control_alpha --> _004t
# full namespace: 
v015__004t = np.sin(v06_control_alpha)

# op _004w_cos_eval
# REP:  v06_control_alpha --> v017__004x
# LANG: control_alpha --> _004x
# full namespace: 
v017__004x = np.cos(v06_control_alpha)

# op _004R_cos_eval
# REP:  v06_control_alpha --> v024__004S
# LANG: control_alpha --> _004S
# full namespace: 
v024__004S = np.cos(v06_control_alpha)

# op _004X_sin_eval
# REP:  v06_control_alpha --> v028__004Y
# LANG: control_alpha --> _004Y
# full namespace: 
v028__004Y = np.sin(v06_control_alpha)

# op _005g_sin_eval
# REP:  v06_control_alpha --> v038__005h
# LANG: control_alpha --> _005h
# full namespace: 
v038__005h = np.sin(v06_control_alpha)

# op _005o_cos_eval
# REP:  v06_control_alpha --> v042__005p
# LANG: control_alpha --> _005p
# full namespace: 
v042__005p = np.cos(v06_control_alpha)

# op _005Z_linear_combination_eval
# REP:  v06_control_alpha --> v061_alpha_w
# LANG: control_alpha --> alpha_w
# full namespace: aero
v061_alpha_w = _005Z_constant+1*v06_control_alpha

# op _004h_power_combination_eval
# REP:  v011_control_x --> v012__004i
# LANG: control_x --> _004i
# full namespace: 
v012__004i = (v011_control_x**1)
v012__004i = (v012__004i*_004h_coeff).reshape((1,))

# op _004l_power_combination_eval
# REP:  v011_control_x --> v014_cruisem
# LANG: control_x --> cruisem
# full namespace: 
v014_cruisem = (v011_control_x**1)
v014_cruisem = (v014_cruisem*_004l_coeff).reshape((1,))

# op _004A_power_combination_eval
# REP:  v019_control_z --> v020__004B
# LANG: control_z --> _004B
# full namespace: 
v020__004B = (v019_control_z**1)
v020__004B = (v020__004B*_004A_coeff).reshape((1,))

# op _004E_power_combination_eval
# REP:  v019_control_z --> v022_liftm
# LANG: control_z --> liftm
# full namespace: 
v022_liftm = (v019_control_z**1)
v022_liftm = (v022_liftm*_004E_coeff).reshape((1,))

# op _0058_power_combination_eval
# REP:  v033__0057 --> v034__0059
# LANG: _0057 --> _0059
# full namespace: 
v034__0059 = (v033__0057**1)
v034__0059 = (v034__0059*_0058_coeff).reshape((1,))

# op _005C_power_combination_eval
# REP:  v048__005B --> v049__005D
# LANG: _005B --> _005D
# full namespace: 
v049__005D = (v048__005B**1)
v049__005D = (v049__005D*_005C_coeff).reshape((1,))

# op _005K_power_combination_eval
# REP:  v01_v, v052__005J --> v053_dh
# LANG: v, _005J --> dh
# full namespace: 
v053_dh = (v01_v**1)*(v052__005J**1)
v053_dh = (v053_dh*_005K_coeff).reshape((1,))

# op _005O_power_combination_eval
# REP:  v01_v, v054__005N --> v055_dx
# LANG: v, _005N --> dx
# full namespace: 
v055_dx = (v01_v**1)*(v054__005N**1)
v055_dx = (v055_dx*_005O_coeff).reshape((1,))

# op _0066_power_combination_eval
# REP:  v073_density --> v062__0067
# LANG: density --> _0067
# full namespace: aero
v062__0067 = (v073_density**1)
v062__0067 = (v062__0067*_0066_coeff).reshape((1,))

# op _004b_power_combination_eval
# REP:  v01_v, v07__004a --> v08_cruisevAxial
# LANG: v, _004a --> cruisevAxial
# full namespace: 
v08_cruisevAxial = (v01_v**1)*(v07__004a**1)
v08_cruisevAxial = (v08_cruisevAxial*_004b_coeff).reshape((1,))

# op _004f_power_combination_eval
# REP:  v01_v, v09__004e --> v010_cruisevTan
# LANG: v, _004e --> cruisevTan
# full namespace: 
v010_cruisevTan = (v01_v**1)*(v09__004e**1)
v010_cruisevTan = (v010_cruisevTan*_004f_coeff).reshape((1,))

# op _004u_power_combination_eval
# REP:  v01_v, v015__004t --> v016_liftvAxial
# LANG: v, _004t --> liftvAxial
# full namespace: 
v016_liftvAxial = (v01_v**1)*(v015__004t**1)
v016_liftvAxial = (v016_liftvAxial*_004u_coeff).reshape((1,))

# op _004y_power_combination_eval
# REP:  v01_v, v017__004x --> v018_liftvTan
# LANG: v, _004x --> liftvTan
# full namespace: 
v018_liftvTan = (v01_v**1)*(v017__004x**1)
v018_liftvTan = (v018_liftvTan*_004y_coeff).reshape((1,))

# op _006n_custom_explicit_eval
# REP:  v061_alpha_w --> v070_cl, v071_cd
# LANG: alpha_w --> cl, cd
# full namespace: aero.airfoil
temp = _006n_custom_explicit_func_cl.solve(v061_alpha_w)
v070_cl = temp[0].copy()
v071_cd = temp[1].copy()

# op _004j_power_combination_eval
# REP:  v012__004i --> v013_cruisen
# LANG: _004i --> cruisen
# full namespace: 
v013_cruisen = (v012__004i**1)
v013_cruisen = (v013_cruisen*_004j_coeff).reshape((1,))

# op _004C_power_combination_eval
# REP:  v020__004B --> v021_liftn
# LANG: _004B --> liftn
# full namespace: 
v021_liftn = (v020__004B**1)
v021_liftn = (v021_liftn*_004C_coeff).reshape((1,))

# op _005E_power_combination_eval
# REP:  v01_v, v049__005D --> v050__005F
# LANG: v, _005D --> _005F
# full namespace: 
v050__005F = (v049__005D**1)*(v01_v**-1)
v050__005F = (v050__005F*_005E_coeff).reshape((1,))

# op _006a_power_combination_eval
# REP:  v062__0067, v064__0069 --> v063__006b
# LANG: _0067, _0069 --> _006b
# full namespace: aero
v063__006b = (v062__0067**1)*(v064__0069**1)
v063__006b = (v063__006b*_006a_coeff).reshape((1,))

# op _006Z_custom_explicit_eval
# REP:  v08_cruisevAxial, v010_cruisevTan --> v086_cruisect, v087_cruisecp
# LANG: cruisevAxial, cruisevTan --> cruisect, cruisecp
# full namespace: cruiserotor.rotorModel
temp = _006Z_custom_explicit_func_cruisect.solve(v08_cruisevAxial, v010_cruisevTan)
v086_cruisect = temp[0].copy()
v087_cruisecp = temp[1].copy()

# op _007A_custom_explicit_eval
# REP:  v016_liftvAxial, v018_liftvTan --> v0101_liftct, v0102_liftcp
# LANG: liftvAxial, liftvTan --> liftct, liftcp
# full namespace: liftrotor.rotorModel
temp = _007A_custom_explicit_func_liftct.solve(v016_liftvAxial, v018_liftvTan)
v0101_liftct = temp[0].copy()
v0102_liftcp = temp[1].copy()

# op _006c_linear_combination_eval
# REP:  v071_cd --> v069__006d
# LANG: cd --> _006d
# full namespace: aero
v069__006d = _006c_constant+1*v071_cd

# op _006B_power_combination_eval
# REP:  v013_cruisen --> v076__006C
# LANG: cruisen --> _006C
# full namespace: cruiserotor
v076__006C = (v013_cruisen**2)
v076__006C = (v076__006C*_006B_coeff).reshape((1,))

# op _006J_power_combination_eval
# REP:  v013_cruisen --> v080__006K
# LANG: cruisen --> _006K
# full namespace: cruiserotor
v080__006K = (v013_cruisen**3)
v080__006K = (v080__006K*_006J_coeff).reshape((1,))

# op _006R_power_combination_eval
# REP:  v013_cruisen --> v084__006S
# LANG: cruisen --> _006S
# full namespace: cruiserotor
v084__006S = (v013_cruisen**2)
v084__006S = (v084__006S*_006R_coeff).reshape((1,))

# op _007c_power_combination_eval
# REP:  v021_liftn --> v091__007d
# LANG: liftn --> _007d
# full namespace: liftrotor
v091__007d = (v021_liftn**2)
v091__007d = (v091__007d*_007c_coeff).reshape((1,))

# op _007k_power_combination_eval
# REP:  v021_liftn --> v095__007l
# LANG: liftn --> _007l
# full namespace: liftrotor
v095__007l = (v021_liftn**3)
v095__007l = (v095__007l*_007k_coeff).reshape((1,))

# op _007s_power_combination_eval
# REP:  v021_liftn --> v099__007t
# LANG: liftn --> _007t
# full namespace: liftrotor
v099__007t = (v021_liftn**2)
v099__007t = (v099__007t*_007s_coeff).reshape((1,))

# op _006e_power_combination_eval
# REP:  v063__006b --> v065__006f
# LANG: _006b --> _006f
# full namespace: aero
v065__006f = (v063__006b**1)
v065__006f = (v065__006f*_006e_coeff).reshape((1,))

# op _006i_power_combination_eval
# REP:  v063__006b --> v067__006j
# LANG: _006b --> _006j
# full namespace: aero
v067__006j = (v063__006b**1)
v067__006j = (v067__006j*_006i_coeff).reshape((1,))

# op _006z_power_combination_eval
# REP:  v073_density, v086_cruisect --> v074__006A
# LANG: density, cruisect --> _006A
# full namespace: cruiserotor
v074__006A = (v086_cruisect**1)*(v073_density**1)
v074__006A = (v074__006A*_006z_coeff).reshape((1,))

# op _006H_power_combination_eval
# REP:  v073_density, v087_cruisecp --> v078__006I
# LANG: density, cruisecp --> _006I
# full namespace: cruiserotor
v078__006I = (v087_cruisecp**1)*(v073_density**1)
v078__006I = (v078__006I*_006H_coeff).reshape((1,))

# op _006P_power_combination_eval
# REP:  v087_cruisecp --> v082__006Q
# LANG: cruisecp --> _006Q
# full namespace: cruiserotor
v082__006Q = (v087_cruisecp**1)
v082__006Q = (v082__006Q*_006P_coeff).reshape((1,))

# op _007a_power_combination_eval
# REP:  v073_density, v0101_liftct --> v089__007b
# LANG: density, liftct --> _007b
# full namespace: liftrotor
v089__007b = (v0101_liftct**1)*(v073_density**1)
v089__007b = (v089__007b*_007a_coeff).reshape((1,))

# op _007i_power_combination_eval
# REP:  v073_density, v0102_liftcp --> v093__007j
# LANG: density, liftcp --> _007j
# full namespace: liftrotor
v093__007j = (v0102_liftcp**1)*(v073_density**1)
v093__007j = (v093__007j*_007i_coeff).reshape((1,))

# op _007q_power_combination_eval
# REP:  v0102_liftcp --> v097__007r
# LANG: liftcp --> _007r
# full namespace: liftrotor
v097__007r = (v0102_liftcp**1)
v097__007r = (v097__007r*_007q_coeff).reshape((1,))

# op _006g_power_combination_eval
# REP:  v065__006f, v070_cl --> v066_lift
# LANG: _006f, cl --> lift
# full namespace: aero
v066_lift = (v065__006f**1)*(v070_cl**1)
v066_lift = (v066_lift*_006g_coeff).reshape((1,))

# op _006k_power_combination_eval
# REP:  v067__006j, v069__006d --> v068_drag
# LANG: _006j, _006d --> drag
# full namespace: aero
v068_drag = (v067__006j**1)*(v069__006d**1)
v068_drag = (v068_drag*_006k_coeff).reshape((1,))

# op _006D_power_combination_eval
# REP:  v074__006A, v076__006C --> v075__006E
# LANG: _006A, _006C --> _006E
# full namespace: cruiserotor
v075__006E = (v074__006A**1)*(v076__006C**1)
v075__006E = (v075__006E*_006D_coeff).reshape((1,))

# op _006L_power_combination_eval
# REP:  v078__006I, v080__006K --> v079__006M
# LANG: _006I, _006K --> _006M
# full namespace: cruiserotor
v079__006M = (v078__006I**1)*(v080__006K**1)
v079__006M = (v079__006M*_006L_coeff).reshape((1,))

# op _006T_power_combination_eval
# REP:  v082__006Q, v084__006S --> v083__006U
# LANG: _006Q, _006S --> _006U
# full namespace: cruiserotor
v083__006U = (v082__006Q**1)*(v084__006S**1)
v083__006U = (v083__006U*_006T_coeff).reshape((1,))

# op _007e_power_combination_eval
# REP:  v089__007b, v091__007d --> v090__007f
# LANG: _007b, _007d --> _007f
# full namespace: liftrotor
v090__007f = (v089__007b**1)*(v091__007d**1)
v090__007f = (v090__007f*_007e_coeff).reshape((1,))

# op _007m_power_combination_eval
# REP:  v093__007j, v095__007l --> v094__007n
# LANG: _007j, _007l --> _007n
# full namespace: liftrotor
v094__007n = (v093__007j**1)*(v095__007l**1)
v094__007n = (v094__007n*_007m_coeff).reshape((1,))

# op _007u_power_combination_eval
# REP:  v097__007r, v099__007t --> v098__007v
# LANG: _007r, _007t --> _007v
# full namespace: liftrotor
v098__007v = (v097__007r**1)*(v099__007t**1)
v098__007v = (v098__007v*_007u_coeff).reshape((1,))

# op _005w_power_combination_eval
# REP:  v045__005v, v066_lift --> v046__005x
# LANG: _005v, lift --> _005x
# full namespace: 
v046__005x = (v066_lift**1)*(v045__005v**-1)
v046__005x = (v046__005x*_005w_coeff).reshape((1,))

# op _0052_power_combination_eval
# REP:  v068_drag --> v031__0053
# LANG: drag --> _0053
# full namespace: 
v031__0053 = (v068_drag**1)
v031__0053 = (v031__0053*_0052_coeff).reshape((1,))

# op _006F_power_combination_eval
# REP:  v075__006E --> v077_cruisethrust
# LANG: _006E --> cruisethrust
# full namespace: cruiserotor
v077_cruisethrust = (v075__006E**1)
v077_cruisethrust = (v077_cruisethrust*_006F_coeff).reshape((1,))

# op _006N_power_combination_eval
# REP:  v079__006M --> v081_cruisepower
# LANG: _006M --> cruisepower
# full namespace: cruiserotor
v081_cruisepower = (v079__006M**1)
v081_cruisepower = (v081_cruisepower*_006N_coeff).reshape((1,))

# op _006V_power_combination_eval
# REP:  v083__006U --> v085_cruisetorque
# LANG: _006U --> cruisetorque
# full namespace: cruiserotor
v085_cruisetorque = (v083__006U**1)
v085_cruisetorque = (v085_cruisetorque*_006V_coeff).reshape((1,))

# op _007g_power_combination_eval
# REP:  v090__007f --> v092_liftthrust
# LANG: _007f --> liftthrust
# full namespace: liftrotor
v092_liftthrust = (v090__007f**1)
v092_liftthrust = (v092_liftthrust*_007g_coeff).reshape((1,))

# op _007o_power_combination_eval
# REP:  v094__007n --> v096_liftpower
# LANG: _007n --> liftpower
# full namespace: liftrotor
v096_liftpower = (v094__007n**1)
v096_liftpower = (v096_liftpower*_007o_coeff).reshape((1,))

# op _007w_power_combination_eval
# REP:  v098__007v --> v0100_lifttorque
# LANG: _007v --> lifttorque
# full namespace: liftrotor
v0100_lifttorque = (v098__007v**1)
v0100_lifttorque = (v0100_lifttorque*_007w_coeff).reshape((1,))

# op _004P_power_combination_eval
# REP:  v077_cruisethrust --> v023__004Q
# LANG: cruisethrust --> _004Q
# full namespace: 
v023__004Q = (v077_cruisethrust**1)
v023__004Q = (v023__004Q*_004P_coeff).reshape((1,))

# op _005e_power_combination_eval
# REP:  v036__005d, v077_cruisethrust --> v037__005f
# LANG: _005d, cruisethrust --> _005f
# full namespace: 
v037__005f = (v077_cruisethrust**1)*(v036__005d**-1)
v037__005f = (v037__005f*_005e_coeff).reshape((1,))

# op _0073_custom_explicit_eval
# REP:  v014_cruisem, v085_cruisetorque --> v088_cruiseeta
# LANG: cruisem, cruisetorque --> cruiseeta
# full namespace: cruisemotor
temp = _0073_custom_explicit_func_cruiseeta.solve(v085_cruisetorque, v014_cruisem)
v088_cruiseeta = temp[0].copy()

# op _004K_power_combination_eval
# REP:  v092_liftthrust --> v026__004L
# LANG: liftthrust --> _004L
# full namespace: 
v026__004L = (v092_liftthrust**1)
v026__004L = (v026__004L*_004K_coeff).reshape((1,))

# op _004N_power_combination_eval
# REP:  v096_liftpower --> v057__004O
# LANG: liftpower --> _004O
# full namespace: 
v057__004O = (v096_liftpower**1)
v057__004O = (v057__004O*_004N_coeff).reshape((1,))

# op _007F_custom_explicit_eval
# REP:  v022_liftm, v0100_lifttorque --> v0103_lifteta
# LANG: liftm, lifttorque --> lifteta
# full namespace: liftmotor
temp = _007F_custom_explicit_func_lifteta.solve(v0100_lifttorque, v022_liftm)
v0103_lifteta = temp[0].copy()

# op _004T_power_combination_eval
# REP:  v023__004Q, v024__004S --> v025__004U
# LANG: _004Q, _004S --> _004U
# full namespace: 
v025__004U = (v023__004Q**1)*(v024__004S**1)
v025__004U = (v025__004U*_004T_coeff).reshape((1,))

# op _005i_power_combination_eval
# REP:  v037__005f, v038__005h --> v039__005j
# LANG: _005f, _005h --> _005j
# full namespace: 
v039__005j = (v037__005f**1)*(v038__005h**1)
v039__005j = (v039__005j*_005i_coeff).reshape((1,))

# op _005Q_power_combination_eval
# REP:  v081_cruisepower, v088_cruiseeta --> v056__005R
# LANG: cruisepower, cruiseeta --> _005R
# full namespace: 
v056__005R = (v081_cruisepower**1)*(v088_cruiseeta**-1)
v056__005R = (v056__005R*_005Q_coeff).reshape((1,))

# op _004V_power_combination_eval
# REP:  v026__004L --> v027__004W
# LANG: _004L --> _004W
# full namespace: 
v027__004W = (v026__004L**1)
v027__004W = (v027__004W*_004V_coeff).reshape((1,))

# op _005m_power_combination_eval
# REP:  v026__004L, v040__005l --> v041__005n
# LANG: _004L, _005l --> _005n
# full namespace: 
v041__005n = (v026__004L**1)*(v040__005l**-1)
v041__005n = (v041__005n*_005m_coeff).reshape((1,))

# op _005S_power_combination_eval
# REP:  v057__004O, v0103_lifteta --> v058__005T
# LANG: _004O, lifteta --> _005T
# full namespace: 
v058__005T = (v057__004O**1)*(v0103_lifteta**-1)
v058__005T = (v058__005T*_005S_coeff).reshape((1,))

# op _004Z_power_combination_eval
# REP:  v027__004W, v028__004Y --> v029__004_
# LANG: _004W, _004Y --> _004_
# full namespace: 
v029__004_ = (v027__004W**1)*(v028__004Y**1)
v029__004_ = (v029__004_*_004Z_coeff).reshape((1,))

# op _005q_power_combination_eval
# REP:  v041__005n, v042__005p --> v043__005r
# LANG: _005n, _005p --> _005r
# full namespace: 
v043__005r = (v041__005n**1)*(v042__005p**1)
v043__005r = (v043__005r*_005q_coeff).reshape((1,))

# op _005U_linear_combination_eval
# REP:  v056__005R, v058__005T --> v059__005V
# LANG: _005R, _005T --> _005V
# full namespace: 
v059__005V = _005U_constant+1*v056__005R+1*v058__005T

# op _0050_linear_combination_eval
# REP:  v025__004U, v029__004_ --> v030__0051
# LANG: _004U, _004_ --> _0051
# full namespace: 
v030__0051 = _0050_constant+1*v025__004U+1*v029__004_

# op _005s_linear_combination_eval
# REP:  v039__005j, v043__005r --> v044__005t
# LANG: _005j, _005r --> _005t
# full namespace: 
v044__005t = _005s_constant+1*v039__005j+1*v043__005r

# op _005W_power_combination_eval
# REP:  v059__005V --> v060_de
# LANG: _005V --> de
# full namespace: 
v060_de = (v059__005V**1)
v060_de = (v060_de*_005W_coeff).reshape((1,))

# op _0054_linear_combination_eval
# REP:  v030__0051, v031__0053 --> v032__0055
# LANG: _0051, _0053 --> _0055
# full namespace: 
v032__0055 = _0054_constant+1*v030__0051+-1*v031__0053

# op _005y_linear_combination_eval
# REP:  v044__005t, v046__005x --> v047__005z
# LANG: _005t, _005x --> _005z
# full namespace: 
v047__005z = _005y_constant+1*v044__005t+1*v046__005x

# op _005a_linear_combination_eval
# REP:  v032__0055, v034__0059 --> v035_dv
# LANG: _0055, _0059 --> dv
# full namespace: 
v035_dv = _005a_constant+1*v032__0055+-1*v034__0059

# op _005G_linear_combination_eval
# REP:  v047__005z, v050__005F --> v051_dgamma
# LANG: _005z, _005F --> dgamma
# full namespace: 
v051_dgamma = _005G_constant+1*v047__005z+-1*v050__005F