

# RUN_MODEL

# system evaluation block

# op _005a_power_combination_eval
# REP:  v01_v --> v036__005b
# LANG: v --> _005b
# full namespace: 
v036__005b = (v01_v**1)
v036__005b = (v036__005b*_005a_coeff).reshape((1,))

# op _005i_power_combination_eval
# REP:  v01_v --> v040__005j
# LANG: v --> _005j
# full namespace: 
v040__005j = (v01_v**1)
v040__005j = (v040__005j*_005i_coeff).reshape((1,))

# op _005s_power_combination_eval
# REP:  v01_v --> v045__005t
# LANG: v --> _005t
# full namespace: 
v045__005t = (v01_v**1)
v045__005t = (v045__005t*_005s_coeff).reshape((1,))

# op _0066_power_combination_eval
# REP:  v01_v --> v064__0067
# LANG: v --> _0067
# full namespace: aero
v064__0067 = (v01_v**2)
v064__0067 = (v064__0067*_0066_coeff).reshape((1,))

# op _0054_sin_eval
# REP:  v02_gamma --> v033__0055
# LANG: gamma --> _0055
# full namespace: 
v033__0055 = np.sin(v02_gamma)

# op _005y_cos_eval
# REP:  v02_gamma --> v048__005z
# LANG: gamma --> _005z
# full namespace: 
v048__005z = np.cos(v02_gamma)

# op _005G_sin_eval
# REP:  v02_gamma --> v052__005H
# LANG: gamma --> _005H
# full namespace: 
v052__005H = np.sin(v02_gamma)

# op _005K_cos_eval
# REP:  v02_gamma --> v054__005L
# LANG: gamma --> _005L
# full namespace: 
v054__005L = np.cos(v02_gamma)

# op _006n_custom_explicit_eval
# REP:  v03_h --> v071_pressure, v072_density
# LANG: h --> pressure, density
# full namespace: aero.atmosphere
temp = _006n_custom_explicit_func_pressure.solve(v03_h)
v071_pressure = temp[0].copy()
v072_density = temp[1].copy()

# op _0047_cos_eval
# REP:  v06_control_alpha --> v07__0048
# LANG: control_alpha --> _0048
# full namespace: 
v07__0048 = np.cos(v06_control_alpha)

# op _004b_sin_eval
# REP:  v06_control_alpha --> v09__004c
# LANG: control_alpha --> _004c
# full namespace: 
v09__004c = np.sin(v06_control_alpha)

# op _004q_sin_eval
# REP:  v06_control_alpha --> v015__004r
# LANG: control_alpha --> _004r
# full namespace: 
v015__004r = np.sin(v06_control_alpha)

# op _004u_cos_eval
# REP:  v06_control_alpha --> v017__004v
# LANG: control_alpha --> _004v
# full namespace: 
v017__004v = np.cos(v06_control_alpha)

# op _004P_cos_eval
# REP:  v06_control_alpha --> v024__004Q
# LANG: control_alpha --> _004Q
# full namespace: 
v024__004Q = np.cos(v06_control_alpha)

# op _004V_sin_eval
# REP:  v06_control_alpha --> v028__004W
# LANG: control_alpha --> _004W
# full namespace: 
v028__004W = np.sin(v06_control_alpha)

# op _005e_sin_eval
# REP:  v06_control_alpha --> v038__005f
# LANG: control_alpha --> _005f
# full namespace: 
v038__005f = np.sin(v06_control_alpha)

# op _005m_cos_eval
# REP:  v06_control_alpha --> v042__005n
# LANG: control_alpha --> _005n
# full namespace: 
v042__005n = np.cos(v06_control_alpha)

# op _005X_power_combination_eval
# REP:  v06_control_alpha --> v061_alpha_w
# LANG: control_alpha --> alpha_w
# full namespace: aero
v061_alpha_w = (v06_control_alpha**1)
v061_alpha_w = (v061_alpha_w*_005X_coeff).reshape((1,))

# op _004f_power_combination_eval
# REP:  v011_control_x --> v012__004g
# LANG: control_x --> _004g
# full namespace: 
v012__004g = (v011_control_x**1)
v012__004g = (v012__004g*_004f_coeff).reshape((1,))

# op _004j_power_combination_eval
# REP:  v011_control_x --> v014_cruisem
# LANG: control_x --> cruisem
# full namespace: 
v014_cruisem = (v011_control_x**1)
v014_cruisem = (v014_cruisem*_004j_coeff).reshape((1,))

# op _004y_power_combination_eval
# REP:  v019_control_z --> v020__004z
# LANG: control_z --> _004z
# full namespace: 
v020__004z = (v019_control_z**1)
v020__004z = (v020__004z*_004y_coeff).reshape((1,))

# op _004C_power_combination_eval
# REP:  v019_control_z --> v022_liftm
# LANG: control_z --> liftm
# full namespace: 
v022_liftm = (v019_control_z**1)
v022_liftm = (v022_liftm*_004C_coeff).reshape((1,))

# op _0056_power_combination_eval
# REP:  v033__0055 --> v034__0057
# LANG: _0055 --> _0057
# full namespace: 
v034__0057 = (v033__0055**1)
v034__0057 = (v034__0057*_0056_coeff).reshape((1,))

# op _005A_power_combination_eval
# REP:  v048__005z --> v049__005B
# LANG: _005z --> _005B
# full namespace: 
v049__005B = (v048__005z**1)
v049__005B = (v049__005B*_005A_coeff).reshape((1,))

# op _005I_power_combination_eval
# REP:  v01_v, v052__005H --> v053_dh
# LANG: v, _005H --> dh
# full namespace: 
v053_dh = (v01_v**1)*(v052__005H**1)
v053_dh = (v053_dh*_005I_coeff).reshape((1,))

# op _005M_power_combination_eval
# REP:  v01_v, v054__005L --> v055_dx
# LANG: v, _005L --> dx
# full namespace: 
v055_dx = (v01_v**1)*(v054__005L**1)
v055_dx = (v055_dx*_005M_coeff).reshape((1,))

# op _0064_power_combination_eval
# REP:  v072_density --> v062__0065
# LANG: density --> _0065
# full namespace: aero
v062__0065 = (v072_density**1)
v062__0065 = (v062__0065*_0064_coeff).reshape((1,))

# op _0049_power_combination_eval
# REP:  v01_v, v07__0048 --> v08_cruisevAxial
# LANG: v, _0048 --> cruisevAxial
# full namespace: 
v08_cruisevAxial = (v01_v**1)*(v07__0048**1)
v08_cruisevAxial = (v08_cruisevAxial*_0049_coeff).reshape((1,))

# op _004d_power_combination_eval
# REP:  v01_v, v09__004c --> v010_cruisevTan
# LANG: v, _004c --> cruisevTan
# full namespace: 
v010_cruisevTan = (v01_v**1)*(v09__004c**1)
v010_cruisevTan = (v010_cruisevTan*_004d_coeff).reshape((1,))

# op _004s_power_combination_eval
# REP:  v01_v, v015__004r --> v016_liftvAxial
# LANG: v, _004r --> liftvAxial
# full namespace: 
v016_liftvAxial = (v01_v**1)*(v015__004r**1)
v016_liftvAxial = (v016_liftvAxial*_004s_coeff).reshape((1,))

# op _004w_power_combination_eval
# REP:  v01_v, v017__004v --> v018_liftvTan
# LANG: v, _004v --> liftvTan
# full namespace: 
v018_liftvTan = (v01_v**1)*(v017__004v**1)
v018_liftvTan = (v018_liftvTan*_004w_coeff).reshape((1,))

# op _006j_custom_explicit_eval
# REP:  v061_alpha_w --> v069_cl, v070_cd
# LANG: alpha_w --> cl, cd
# full namespace: aero.airfoil
temp = _006j_custom_explicit_func_cl.solve(v061_alpha_w)
v069_cl = temp[0].copy()
v070_cd = temp[1].copy()

# op _004h_power_combination_eval
# REP:  v012__004g --> v013_cruisen
# LANG: _004g --> cruisen
# full namespace: 
v013_cruisen = (v012__004g**1)
v013_cruisen = (v013_cruisen*_004h_coeff).reshape((1,))

# op _004A_power_combination_eval
# REP:  v020__004z --> v021_liftn
# LANG: _004z --> liftn
# full namespace: 
v021_liftn = (v020__004z**1)
v021_liftn = (v021_liftn*_004A_coeff).reshape((1,))

# op _005C_power_combination_eval
# REP:  v01_v, v049__005B --> v050__005D
# LANG: v, _005B --> _005D
# full namespace: 
v050__005D = (v049__005B**1)*(v01_v**-1)
v050__005D = (v050__005D*_005C_coeff).reshape((1,))

# op _0068_power_combination_eval
# REP:  v062__0065, v064__0067 --> v063__0069
# LANG: _0065, _0067 --> _0069
# full namespace: aero
v063__0069 = (v062__0065**1)*(v064__0067**1)
v063__0069 = (v063__0069*_0068_coeff).reshape((1,))

# op _006V_custom_explicit_eval
# REP:  v08_cruisevAxial, v010_cruisevTan --> v085_cruisect, v086_cruisecp
# LANG: cruisevAxial, cruisevTan --> cruisect, cruisecp
# full namespace: cruiserotor.rotorModel
temp = _006V_custom_explicit_func_cruisect.solve(v08_cruisevAxial, v010_cruisevTan)
v085_cruisect = temp[0].copy()
v086_cruisecp = temp[1].copy()

# op _007w_custom_explicit_eval
# REP:  v016_liftvAxial, v018_liftvTan --> v0100_liftct, v0101_liftcp
# LANG: liftvAxial, liftvTan --> liftct, liftcp
# full namespace: liftrotor.rotorModel
temp = _007w_custom_explicit_func_liftct.solve(v016_liftvAxial, v018_liftvTan)
v0100_liftct = temp[0].copy()
v0101_liftcp = temp[1].copy()

# op _006x_power_combination_eval
# REP:  v013_cruisen --> v075__006y
# LANG: cruisen --> _006y
# full namespace: cruiserotor
v075__006y = (v013_cruisen**2)
v075__006y = (v075__006y*_006x_coeff).reshape((1,))

# op _006F_power_combination_eval
# REP:  v013_cruisen --> v079__006G
# LANG: cruisen --> _006G
# full namespace: cruiserotor
v079__006G = (v013_cruisen**3)
v079__006G = (v079__006G*_006F_coeff).reshape((1,))

# op _006N_power_combination_eval
# REP:  v013_cruisen --> v083__006O
# LANG: cruisen --> _006O
# full namespace: cruiserotor
v083__006O = (v013_cruisen**2)
v083__006O = (v083__006O*_006N_coeff).reshape((1,))

# op _0078_power_combination_eval
# REP:  v021_liftn --> v090__0079
# LANG: liftn --> _0079
# full namespace: liftrotor
v090__0079 = (v021_liftn**2)
v090__0079 = (v090__0079*_0078_coeff).reshape((1,))

# op _007g_power_combination_eval
# REP:  v021_liftn --> v094__007h
# LANG: liftn --> _007h
# full namespace: liftrotor
v094__007h = (v021_liftn**3)
v094__007h = (v094__007h*_007g_coeff).reshape((1,))

# op _007o_power_combination_eval
# REP:  v021_liftn --> v098__007p
# LANG: liftn --> _007p
# full namespace: liftrotor
v098__007p = (v021_liftn**2)
v098__007p = (v098__007p*_007o_coeff).reshape((1,))

# op _006a_power_combination_eval
# REP:  v063__0069 --> v065__006b
# LANG: _0069 --> _006b
# full namespace: aero
v065__006b = (v063__0069**1)
v065__006b = (v065__006b*_006a_coeff).reshape((1,))

# op _006e_power_combination_eval
# REP:  v063__0069 --> v067__006f
# LANG: _0069 --> _006f
# full namespace: aero
v067__006f = (v063__0069**1)
v067__006f = (v067__006f*_006e_coeff).reshape((1,))

# op _006v_power_combination_eval
# REP:  v072_density, v085_cruisect --> v073__006w
# LANG: density, cruisect --> _006w
# full namespace: cruiserotor
v073__006w = (v085_cruisect**1)*(v072_density**1)
v073__006w = (v073__006w*_006v_coeff).reshape((1,))

# op _006D_power_combination_eval
# REP:  v072_density, v086_cruisecp --> v077__006E
# LANG: density, cruisecp --> _006E
# full namespace: cruiserotor
v077__006E = (v086_cruisecp**1)*(v072_density**1)
v077__006E = (v077__006E*_006D_coeff).reshape((1,))

# op _006L_power_combination_eval
# REP:  v086_cruisecp --> v081__006M
# LANG: cruisecp --> _006M
# full namespace: cruiserotor
v081__006M = (v086_cruisecp**1)
v081__006M = (v081__006M*_006L_coeff).reshape((1,))

# op _0076_power_combination_eval
# REP:  v072_density, v0100_liftct --> v088__0077
# LANG: density, liftct --> _0077
# full namespace: liftrotor
v088__0077 = (v0100_liftct**1)*(v072_density**1)
v088__0077 = (v088__0077*_0076_coeff).reshape((1,))

# op _007e_power_combination_eval
# REP:  v072_density, v0101_liftcp --> v092__007f
# LANG: density, liftcp --> _007f
# full namespace: liftrotor
v092__007f = (v0101_liftcp**1)*(v072_density**1)
v092__007f = (v092__007f*_007e_coeff).reshape((1,))

# op _007m_power_combination_eval
# REP:  v0101_liftcp --> v096__007n
# LANG: liftcp --> _007n
# full namespace: liftrotor
v096__007n = (v0101_liftcp**1)
v096__007n = (v096__007n*_007m_coeff).reshape((1,))

# op _006c_power_combination_eval
# REP:  v065__006b, v069_cl --> v066_lift
# LANG: _006b, cl --> lift
# full namespace: aero
v066_lift = (v065__006b**1)*(v069_cl**1)
v066_lift = (v066_lift*_006c_coeff).reshape((1,))

# op _006g_power_combination_eval
# REP:  v067__006f, v070_cd --> v068_drag
# LANG: _006f, cd --> drag
# full namespace: aero
v068_drag = (v067__006f**1)*(v070_cd**1)
v068_drag = (v068_drag*_006g_coeff).reshape((1,))

# op _006z_power_combination_eval
# REP:  v073__006w, v075__006y --> v074__006A
# LANG: _006w, _006y --> _006A
# full namespace: cruiserotor
v074__006A = (v073__006w**1)*(v075__006y**1)
v074__006A = (v074__006A*_006z_coeff).reshape((1,))

# op _006H_power_combination_eval
# REP:  v077__006E, v079__006G --> v078__006I
# LANG: _006E, _006G --> _006I
# full namespace: cruiserotor
v078__006I = (v077__006E**1)*(v079__006G**1)
v078__006I = (v078__006I*_006H_coeff).reshape((1,))

# op _006P_power_combination_eval
# REP:  v081__006M, v083__006O --> v082__006Q
# LANG: _006M, _006O --> _006Q
# full namespace: cruiserotor
v082__006Q = (v081__006M**1)*(v083__006O**1)
v082__006Q = (v082__006Q*_006P_coeff).reshape((1,))

# op _007a_power_combination_eval
# REP:  v088__0077, v090__0079 --> v089__007b
# LANG: _0077, _0079 --> _007b
# full namespace: liftrotor
v089__007b = (v088__0077**1)*(v090__0079**1)
v089__007b = (v089__007b*_007a_coeff).reshape((1,))

# op _007i_power_combination_eval
# REP:  v092__007f, v094__007h --> v093__007j
# LANG: _007f, _007h --> _007j
# full namespace: liftrotor
v093__007j = (v092__007f**1)*(v094__007h**1)
v093__007j = (v093__007j*_007i_coeff).reshape((1,))

# op _007q_power_combination_eval
# REP:  v096__007n, v098__007p --> v097__007r
# LANG: _007n, _007p --> _007r
# full namespace: liftrotor
v097__007r = (v096__007n**1)*(v098__007p**1)
v097__007r = (v097__007r*_007q_coeff).reshape((1,))

# op _005u_power_combination_eval
# REP:  v045__005t, v066_lift --> v046__005v
# LANG: _005t, lift --> _005v
# full namespace: 
v046__005v = (v066_lift**1)*(v045__005t**-1)
v046__005v = (v046__005v*_005u_coeff).reshape((1,))

# op _0050_power_combination_eval
# REP:  v068_drag --> v031__0051
# LANG: drag --> _0051
# full namespace: 
v031__0051 = (v068_drag**1)
v031__0051 = (v031__0051*_0050_coeff).reshape((1,))

# op _006B_power_combination_eval
# REP:  v074__006A --> v076_cruisethrust
# LANG: _006A --> cruisethrust
# full namespace: cruiserotor
v076_cruisethrust = (v074__006A**1)
v076_cruisethrust = (v076_cruisethrust*_006B_coeff).reshape((1,))

# op _006J_power_combination_eval
# REP:  v078__006I --> v080_cruisepower
# LANG: _006I --> cruisepower
# full namespace: cruiserotor
v080_cruisepower = (v078__006I**1)
v080_cruisepower = (v080_cruisepower*_006J_coeff).reshape((1,))

# op _006R_power_combination_eval
# REP:  v082__006Q --> v084_cruisetorque
# LANG: _006Q --> cruisetorque
# full namespace: cruiserotor
v084_cruisetorque = (v082__006Q**1)
v084_cruisetorque = (v084_cruisetorque*_006R_coeff).reshape((1,))

# op _007c_power_combination_eval
# REP:  v089__007b --> v091_liftthrust
# LANG: _007b --> liftthrust
# full namespace: liftrotor
v091_liftthrust = (v089__007b**1)
v091_liftthrust = (v091_liftthrust*_007c_coeff).reshape((1,))

# op _007k_power_combination_eval
# REP:  v093__007j --> v095_liftpower
# LANG: _007j --> liftpower
# full namespace: liftrotor
v095_liftpower = (v093__007j**1)
v095_liftpower = (v095_liftpower*_007k_coeff).reshape((1,))

# op _007s_power_combination_eval
# REP:  v097__007r --> v099_lifttorque
# LANG: _007r --> lifttorque
# full namespace: liftrotor
v099_lifttorque = (v097__007r**1)
v099_lifttorque = (v099_lifttorque*_007s_coeff).reshape((1,))

# op _004N_power_combination_eval
# REP:  v076_cruisethrust --> v023__004O
# LANG: cruisethrust --> _004O
# full namespace: 
v023__004O = (v076_cruisethrust**1)
v023__004O = (v023__004O*_004N_coeff).reshape((1,))

# op _005c_power_combination_eval
# REP:  v036__005b, v076_cruisethrust --> v037__005d
# LANG: _005b, cruisethrust --> _005d
# full namespace: 
v037__005d = (v076_cruisethrust**1)*(v036__005b**-1)
v037__005d = (v037__005d*_005c_coeff).reshape((1,))

# op _006__custom_explicit_eval
# REP:  v014_cruisem, v084_cruisetorque --> v087_cruiseeta
# LANG: cruisem, cruisetorque --> cruiseeta
# full namespace: cruisemotor
temp = _006__custom_explicit_func_cruiseeta.solve(v084_cruisetorque, v014_cruisem)
v087_cruiseeta = temp[0].copy()

# op _004I_power_combination_eval
# REP:  v091_liftthrust --> v026__004J
# LANG: liftthrust --> _004J
# full namespace: 
v026__004J = (v091_liftthrust**1)
v026__004J = (v026__004J*_004I_coeff).reshape((1,))

# op _004L_power_combination_eval
# REP:  v095_liftpower --> v057__004M
# LANG: liftpower --> _004M
# full namespace: 
v057__004M = (v095_liftpower**1)
v057__004M = (v057__004M*_004L_coeff).reshape((1,))

# op _007B_custom_explicit_eval
# REP:  v022_liftm, v099_lifttorque --> v0102_lifteta
# LANG: liftm, lifttorque --> lifteta
# full namespace: liftmotor
temp = _007B_custom_explicit_func_lifteta.solve(v099_lifttorque, v022_liftm)
v0102_lifteta = temp[0].copy()

# op _004R_power_combination_eval
# REP:  v023__004O, v024__004Q --> v025__004S
# LANG: _004O, _004Q --> _004S
# full namespace: 
v025__004S = (v023__004O**1)*(v024__004Q**1)
v025__004S = (v025__004S*_004R_coeff).reshape((1,))

# op _005g_power_combination_eval
# REP:  v037__005d, v038__005f --> v039__005h
# LANG: _005d, _005f --> _005h
# full namespace: 
v039__005h = (v037__005d**1)*(v038__005f**1)
v039__005h = (v039__005h*_005g_coeff).reshape((1,))

# op _005O_power_combination_eval
# REP:  v080_cruisepower, v087_cruiseeta --> v056__005P
# LANG: cruisepower, cruiseeta --> _005P
# full namespace: 
v056__005P = (v080_cruisepower**1)*(v087_cruiseeta**-1)
v056__005P = (v056__005P*_005O_coeff).reshape((1,))

# op _004T_power_combination_eval
# REP:  v026__004J --> v027__004U
# LANG: _004J --> _004U
# full namespace: 
v027__004U = (v026__004J**1)
v027__004U = (v027__004U*_004T_coeff).reshape((1,))

# op _005k_power_combination_eval
# REP:  v026__004J, v040__005j --> v041__005l
# LANG: _004J, _005j --> _005l
# full namespace: 
v041__005l = (v026__004J**1)*(v040__005j**-1)
v041__005l = (v041__005l*_005k_coeff).reshape((1,))

# op _005Q_power_combination_eval
# REP:  v057__004M, v0102_lifteta --> v058__005R
# LANG: _004M, lifteta --> _005R
# full namespace: 
v058__005R = (v057__004M**1)*(v0102_lifteta**-1)
v058__005R = (v058__005R*_005Q_coeff).reshape((1,))

# op _004X_power_combination_eval
# REP:  v027__004U, v028__004W --> v029__004Y
# LANG: _004U, _004W --> _004Y
# full namespace: 
v029__004Y = (v027__004U**1)*(v028__004W**1)
v029__004Y = (v029__004Y*_004X_coeff).reshape((1,))

# op _005o_power_combination_eval
# REP:  v041__005l, v042__005n --> v043__005p
# LANG: _005l, _005n --> _005p
# full namespace: 
v043__005p = (v041__005l**1)*(v042__005n**1)
v043__005p = (v043__005p*_005o_coeff).reshape((1,))

# op _005S_linear_combination_eval
# REP:  v056__005P, v058__005R --> v059__005T
# LANG: _005P, _005R --> _005T
# full namespace: 
v059__005T = _005S_constant+1*v056__005P+1*v058__005R

# op _004Z_linear_combination_eval
# REP:  v025__004S, v029__004Y --> v030__004_
# LANG: _004S, _004Y --> _004_
# full namespace: 
v030__004_ = _004Z_constant+1*v025__004S+1*v029__004Y

# op _005q_linear_combination_eval
# REP:  v039__005h, v043__005p --> v044__005r
# LANG: _005h, _005p --> _005r
# full namespace: 
v044__005r = _005q_constant+1*v039__005h+1*v043__005p

# op _005U_power_combination_eval
# REP:  v059__005T --> v060_de
# LANG: _005T --> de
# full namespace: 
v060_de = (v059__005T**1)
v060_de = (v060_de*_005U_coeff).reshape((1,))

# op _0052_linear_combination_eval
# REP:  v030__004_, v031__0051 --> v032__0053
# LANG: _004_, _0051 --> _0053
# full namespace: 
v032__0053 = _0052_constant+1*v030__004_+-1*v031__0051

# op _005w_linear_combination_eval
# REP:  v044__005r, v046__005v --> v047__005x
# LANG: _005r, _005v --> _005x
# full namespace: 
v047__005x = _005w_constant+1*v044__005r+1*v046__005v

# op _0058_linear_combination_eval
# REP:  v032__0053, v034__0057 --> v035_dv
# LANG: _0053, _0057 --> dv
# full namespace: 
v035_dv = _0058_constant+1*v032__0053+-1*v034__0057

# op _005E_linear_combination_eval
# REP:  v047__005x, v050__005D --> v051_dgamma
# LANG: _005x, _005D --> dgamma
# full namespace: 
v051_dgamma = _005E_constant+1*v047__005x+-1*v050__005D