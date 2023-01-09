

# DERIVATIVESlift,drag,cl,cd,cruisepower,liftpower-->v,gamma,h,x,e,control_alpha,control_x,control_z

# REV:v066_lift,v068_drag,v070_cl,v071_cd,v081_cruisepower,v096_liftpower,-->v01_v,v02_gamma,v03_h,v04_x,v05_e,v06_control_alpha,v011_control_x,v019_control_z,

# :::::::v066_lift-->v01_v,v02_gamma,v03_h,v04_x,v05_e,v06_control_alpha,v011_control_x,v019_control_z,:::::::

# op _006g_power_combination_eval
# REP:  v065__006f, v070_cl --> v066_lift
# LANG: _006f, cl --> lift
# full namespace: aero

# _006g_power_combination_eval_pv066_lift_pv070_cl
temp_power = _006g_coeff_temp*1*(v070_cl)
pv066_lift_pv065__006f = temp_power.flatten()
temp_power = _006g_coeff_temp*(v065__006f)*1
pv066_lift_pv070_cl = temp_power.flatten()
path_to_v065__006f = np.diagflat(pv066_lift_pv065__006f)
path_to_v070_cl = np.diagflat(pv066_lift_pv070_cl)

# op _006e_power_combination_eval
# REP:  v063__006b --> v065__006f
# LANG: _006b --> _006f
# full namespace: aero

# _006e_power_combination_eval_pv065__006f_pv063__006b
temp_power = _006e_coeff_temp*1
pv065__006f_pv063__006b = temp_power.flatten()
path_to_v063__006b = DIAG_MULT(path_to_v065__006f,pv065__006f_pv063__006b)

# op _006n_custom_explicit_eval
# REP:  v061_alpha_w --> v070_cl, v071_cd
# LANG: alpha_w --> cl, cd
# full namespace: aero.airfoil

# _006n_custom_explicit_eval_pv071_cd_pv061_alpha_w
pv070_cl_pv061_alpha_w = _006n_custom_explicit_func_cl.get_partials('cl', 'alpha_w')
pv071_cd_pv061_alpha_w = _006n_custom_explicit_func_cl.get_partials('cd', 'alpha_w')
path_to_v061_alpha_w = path_to_v070_cl@pv070_cl_pv061_alpha_w

# op _006a_power_combination_eval
# REP:  v062__0067, v064__0069 --> v063__006b
# LANG: _0067, _0069 --> _006b
# full namespace: aero

# _006a_power_combination_eval_pv063__006b_pv064__0069
temp_power = _006a_coeff_temp*1*(v064__0069)
pv063__006b_pv062__0067 = temp_power.flatten()
temp_power = _006a_coeff_temp*(v062__0067)*1
pv063__006b_pv064__0069 = temp_power.flatten()
path_to_v062__0067 = DIAG_MULT(path_to_v063__006b,pv063__006b_pv062__0067)
path_to_v064__0069 = DIAG_MULT(path_to_v063__006b,pv063__006b_pv064__0069)

# op _005Z_linear_combination_eval
# REP:  v06_control_alpha --> v061_alpha_w
# LANG: control_alpha --> alpha_w
# full namespace: aero

# _005Z_linear_combination_eval_pv061_alpha_w_pv06_control_alpha
path_to_v06_control_alpha = DIAG_MULT(path_to_v061_alpha_w,pv061_alpha_w_pv06_control_alpha)

# op _0066_power_combination_eval
# REP:  v073_density --> v062__0067
# LANG: density --> _0067
# full namespace: aero

# _0066_power_combination_eval_pv062__0067_pv073_density
temp_power = _0066_coeff_temp*1
pv062__0067_pv073_density = temp_power.flatten()
path_to_v073_density = DIAG_MULT(path_to_v062__0067,pv062__0067_pv073_density)

# op _0068_power_combination_eval
# REP:  v01_v --> v064__0069
# LANG: v --> _0069
# full namespace: aero

# _0068_power_combination_eval_pv064__0069_pv01_v
temp_power = _0068_coeff_temp*2*(v01_v)
pv064__0069_pv01_v = temp_power.flatten()
path_to_v01_v = DIAG_MULT(path_to_v064__0069,pv064__0069_pv01_v)

# op _006r_custom_explicit_eval
# REP:  v03_h --> v072_pressure, v073_density
# LANG: h --> pressure, density
# full namespace: aero.atmosphere

# _006r_custom_explicit_eval_pv073_density_pv03_h
pv072_pressure_pv03_h = _006r_custom_explicit_func_pressure.get_partials('pressure', 'h')
pv073_density_pv03_h = _006r_custom_explicit_func_pressure.get_partials('density', 'h')
path_to_v03_h = path_to_v073_density@pv073_density_pv03_h
dv066_lift_dv01_v = path_to_v01_v.copy()
# dv066_lift_dv02_gamma = zero
dv066_lift_dv03_h = path_to_v03_h.copy()
# dv066_lift_dv04_x = zero
# dv066_lift_dv05_e = zero
dv066_lift_dv06_control_alpha = path_to_v06_control_alpha.copy()
# dv066_lift_dv011_control_x = zero
# dv066_lift_dv019_control_z = zero

# :::::::v068_drag-->v01_v,v02_gamma,v03_h,v04_x,v05_e,v06_control_alpha,v011_control_x,v019_control_z,:::::::

# op _006k_power_combination_eval
# REP:  v067__006j, v069__006d --> v068_drag
# LANG: _006j, _006d --> drag
# full namespace: aero

# _006k_power_combination_eval_pv068_drag_pv069__006d
temp_power = _006k_coeff_temp*1*(v069__006d)
pv068_drag_pv067__006j = temp_power.flatten()
temp_power = _006k_coeff_temp*(v067__006j)*1
pv068_drag_pv069__006d = temp_power.flatten()
path_to_v067__006j = np.diagflat(pv068_drag_pv067__006j)
path_to_v069__006d = np.diagflat(pv068_drag_pv069__006d)

# op _006i_power_combination_eval
# REP:  v063__006b --> v067__006j
# LANG: _006b --> _006j
# full namespace: aero

# _006i_power_combination_eval_pv067__006j_pv063__006b
temp_power = _006i_coeff_temp*1
pv067__006j_pv063__006b = temp_power.flatten()
path_to_v063__006b = DIAG_MULT(path_to_v067__006j,pv067__006j_pv063__006b)

# op _006c_linear_combination_eval
# REP:  v071_cd --> v069__006d
# LANG: cd --> _006d
# full namespace: aero

# _006c_linear_combination_eval_pv069__006d_pv071_cd
path_to_v071_cd = DIAG_MULT(path_to_v069__006d,pv069__006d_pv071_cd)
path_to_v062__0067 = DIAG_MULT(path_to_v063__006b,pv063__006b_pv062__0067)
path_to_v064__0069 = DIAG_MULT(path_to_v063__006b,pv063__006b_pv064__0069)
path_to_v061_alpha_w = path_to_v071_cd@pv071_cd_pv061_alpha_w
path_to_v073_density = DIAG_MULT(path_to_v062__0067,pv062__0067_pv073_density)
path_to_v01_v = DIAG_MULT(path_to_v064__0069,pv064__0069_pv01_v)
path_to_v06_control_alpha = DIAG_MULT(path_to_v061_alpha_w,pv061_alpha_w_pv06_control_alpha)
path_to_v03_h = path_to_v073_density@pv073_density_pv03_h
dv068_drag_dv01_v = path_to_v01_v.copy()
# dv068_drag_dv02_gamma = zero
dv068_drag_dv03_h = path_to_v03_h.copy()
# dv068_drag_dv04_x = zero
# dv068_drag_dv05_e = zero
dv068_drag_dv06_control_alpha = path_to_v06_control_alpha.copy()
# dv068_drag_dv011_control_x = zero
# dv068_drag_dv019_control_z = zero

# :::::::v070_cl-->v01_v,v02_gamma,v03_h,v04_x,v05_e,v06_control_alpha,v011_control_x,v019_control_z,:::::::
path_to_v061_alpha_w = pv070_cl_pv061_alpha_w.copy()
path_to_v06_control_alpha = DIAG_MULT(path_to_v061_alpha_w,pv061_alpha_w_pv06_control_alpha)
# dv070_cl_dv01_v = zero
# dv070_cl_dv02_gamma = zero
# dv070_cl_dv03_h = zero
# dv070_cl_dv04_x = zero
# dv070_cl_dv05_e = zero
dv070_cl_dv06_control_alpha = path_to_v06_control_alpha.copy()
# dv070_cl_dv011_control_x = zero
# dv070_cl_dv019_control_z = zero

# :::::::v071_cd-->v01_v,v02_gamma,v03_h,v04_x,v05_e,v06_control_alpha,v011_control_x,v019_control_z,:::::::
path_to_v061_alpha_w = pv071_cd_pv061_alpha_w.copy()
path_to_v06_control_alpha = DIAG_MULT(path_to_v061_alpha_w,pv061_alpha_w_pv06_control_alpha)
# dv071_cd_dv01_v = zero
# dv071_cd_dv02_gamma = zero
# dv071_cd_dv03_h = zero
# dv071_cd_dv04_x = zero
# dv071_cd_dv05_e = zero
dv071_cd_dv06_control_alpha = path_to_v06_control_alpha.copy()
# dv071_cd_dv011_control_x = zero
# dv071_cd_dv019_control_z = zero

# :::::::v081_cruisepower-->v01_v,v02_gamma,v03_h,v04_x,v05_e,v06_control_alpha,v011_control_x,v019_control_z,:::::::

# op _006N_power_combination_eval
# REP:  v079__006M --> v081_cruisepower
# LANG: _006M --> cruisepower
# full namespace: cruiserotor

# _006N_power_combination_eval_pv081_cruisepower_pv079__006M
temp_power = _006N_coeff_temp*1
pv081_cruisepower_pv079__006M = temp_power.flatten()
path_to_v079__006M = np.diagflat(pv081_cruisepower_pv079__006M)

# op _006L_power_combination_eval
# REP:  v078__006I, v080__006K --> v079__006M
# LANG: _006I, _006K --> _006M
# full namespace: cruiserotor

# _006L_power_combination_eval_pv079__006M_pv080__006K
temp_power = _006L_coeff_temp*1*(v080__006K)
pv079__006M_pv078__006I = temp_power.flatten()
temp_power = _006L_coeff_temp*(v078__006I)*1
pv079__006M_pv080__006K = temp_power.flatten()
path_to_v078__006I = DIAG_MULT(path_to_v079__006M,pv079__006M_pv078__006I)
path_to_v080__006K = DIAG_MULT(path_to_v079__006M,pv079__006M_pv080__006K)

# op _006H_power_combination_eval
# REP:  v073_density, v087_cruisecp --> v078__006I
# LANG: density, cruisecp --> _006I
# full namespace: cruiserotor

# _006H_power_combination_eval_pv078__006I_pv087_cruisecp
temp_power = _006H_coeff_temp*(v087_cruisecp)*1
pv078__006I_pv073_density = temp_power.flatten()
temp_power = _006H_coeff_temp*1*(v073_density)
pv078__006I_pv087_cruisecp = temp_power.flatten()
path_to_v073_density = DIAG_MULT(path_to_v078__006I,pv078__006I_pv073_density)
path_to_v087_cruisecp = DIAG_MULT(path_to_v078__006I,pv078__006I_pv087_cruisecp)

# op _006J_power_combination_eval
# REP:  v013_cruisen --> v080__006K
# LANG: cruisen --> _006K
# full namespace: cruiserotor

# _006J_power_combination_eval_pv080__006K_pv013_cruisen
temp_power = _006J_coeff_temp*3*(v013_cruisen**2.0)
pv080__006K_pv013_cruisen = temp_power.flatten()
path_to_v013_cruisen = DIAG_MULT(path_to_v080__006K,pv080__006K_pv013_cruisen)
path_to_v03_h = path_to_v073_density@pv073_density_pv03_h

# op _006Z_custom_explicit_eval
# REP:  v08_cruisevAxial, v010_cruisevTan --> v086_cruisect, v087_cruisecp
# LANG: cruisevAxial, cruisevTan --> cruisect, cruisecp
# full namespace: cruiserotor.rotorModel

# _006Z_custom_explicit_eval_pv087_cruisecp_pv010_cruisevTan
pv086_cruisect_pv08_cruisevAxial = _006Z_custom_explicit_func_cruisect.get_partials('cruisect', 'cruisevAxial')
pv086_cruisect_pv010_cruisevTan = _006Z_custom_explicit_func_cruisect.get_partials('cruisect', 'cruisevTan')
pv087_cruisecp_pv08_cruisevAxial = _006Z_custom_explicit_func_cruisect.get_partials('cruisecp', 'cruisevAxial')
pv087_cruisecp_pv010_cruisevTan = _006Z_custom_explicit_func_cruisect.get_partials('cruisecp', 'cruisevTan')
path_to_v08_cruisevAxial = path_to_v087_cruisecp@pv087_cruisecp_pv08_cruisevAxial
path_to_v010_cruisevTan = path_to_v087_cruisecp@pv087_cruisecp_pv010_cruisevTan

# op _004j_power_combination_eval
# REP:  v012__004i --> v013_cruisen
# LANG: _004i --> cruisen
# full namespace: 

# _004j_power_combination_eval_pv013_cruisen_pv012__004i
temp_power = _004j_coeff_temp*1
pv013_cruisen_pv012__004i = temp_power.flatten()
path_to_v012__004i = DIAG_MULT(path_to_v013_cruisen,pv013_cruisen_pv012__004i)

# op _004b_power_combination_eval
# REP:  v01_v, v07__004a --> v08_cruisevAxial
# LANG: v, _004a --> cruisevAxial
# full namespace: 

# _004b_power_combination_eval_pv08_cruisevAxial_pv07__004a
temp_power = _004b_coeff_temp*1*(v07__004a)
pv08_cruisevAxial_pv01_v = temp_power.flatten()
temp_power = _004b_coeff_temp*(v01_v)*1
pv08_cruisevAxial_pv07__004a = temp_power.flatten()
path_to_v01_v = DIAG_MULT(path_to_v08_cruisevAxial,pv08_cruisevAxial_pv01_v)
path_to_v07__004a = DIAG_MULT(path_to_v08_cruisevAxial,pv08_cruisevAxial_pv07__004a)

# op _004f_power_combination_eval
# REP:  v01_v, v09__004e --> v010_cruisevTan
# LANG: v, _004e --> cruisevTan
# full namespace: 

# _004f_power_combination_eval_pv010_cruisevTan_pv09__004e
temp_power = _004f_coeff_temp*1*(v09__004e)
pv010_cruisevTan_pv01_v = temp_power.flatten()
temp_power = _004f_coeff_temp*(v01_v)*1
pv010_cruisevTan_pv09__004e = temp_power.flatten()
path_to_v01_v += DIAG_MULT(path_to_v010_cruisevTan,pv010_cruisevTan_pv01_v)
path_to_v09__004e = DIAG_MULT(path_to_v010_cruisevTan,pv010_cruisevTan_pv09__004e)

# op _004h_power_combination_eval
# REP:  v011_control_x --> v012__004i
# LANG: control_x --> _004i
# full namespace: 

# _004h_power_combination_eval_pv012__004i_pv011_control_x
temp_power = _004h_coeff_temp*1
pv012__004i_pv011_control_x = temp_power.flatten()
path_to_v011_control_x = DIAG_MULT(path_to_v012__004i,pv012__004i_pv011_control_x)

# op _0049_cos_eval
# REP:  v06_control_alpha --> v07__004a
# LANG: control_alpha --> _004a
# full namespace: 

# _0049_cos_eval_pv07__004a_pv06_control_alpha
pv07__004a_pv06_control_alpha = -np.sin(v06_control_alpha).flatten()
path_to_v06_control_alpha = DIAG_MULT(path_to_v07__004a,pv07__004a_pv06_control_alpha)

# op _004d_sin_eval
# REP:  v06_control_alpha --> v09__004e
# LANG: control_alpha --> _004e
# full namespace: 

# _004d_sin_eval_pv09__004e_pv06_control_alpha
pv09__004e_pv06_control_alpha = np.cos(v06_control_alpha).flatten()
path_to_v06_control_alpha += DIAG_MULT(path_to_v09__004e,pv09__004e_pv06_control_alpha)
dv081_cruisepower_dv01_v = path_to_v01_v.copy()
# dv081_cruisepower_dv02_gamma = zero
dv081_cruisepower_dv03_h = path_to_v03_h.copy()
# dv081_cruisepower_dv04_x = zero
# dv081_cruisepower_dv05_e = zero
dv081_cruisepower_dv06_control_alpha = path_to_v06_control_alpha.copy()
dv081_cruisepower_dv011_control_x = path_to_v011_control_x.copy()
# dv081_cruisepower_dv019_control_z = zero

# :::::::v096_liftpower-->v01_v,v02_gamma,v03_h,v04_x,v05_e,v06_control_alpha,v011_control_x,v019_control_z,:::::::

# op _007o_power_combination_eval
# REP:  v094__007n --> v096_liftpower
# LANG: _007n --> liftpower
# full namespace: liftrotor

# _007o_power_combination_eval_pv096_liftpower_pv094__007n
temp_power = _007o_coeff_temp*1
pv096_liftpower_pv094__007n = temp_power.flatten()
path_to_v094__007n = np.diagflat(pv096_liftpower_pv094__007n)

# op _007m_power_combination_eval
# REP:  v093__007j, v095__007l --> v094__007n
# LANG: _007j, _007l --> _007n
# full namespace: liftrotor

# _007m_power_combination_eval_pv094__007n_pv095__007l
temp_power = _007m_coeff_temp*1*(v095__007l)
pv094__007n_pv093__007j = temp_power.flatten()
temp_power = _007m_coeff_temp*(v093__007j)*1
pv094__007n_pv095__007l = temp_power.flatten()
path_to_v093__007j = DIAG_MULT(path_to_v094__007n,pv094__007n_pv093__007j)
path_to_v095__007l = DIAG_MULT(path_to_v094__007n,pv094__007n_pv095__007l)

# op _007i_power_combination_eval
# REP:  v073_density, v0102_liftcp --> v093__007j
# LANG: density, liftcp --> _007j
# full namespace: liftrotor

# _007i_power_combination_eval_pv093__007j_pv0102_liftcp
temp_power = _007i_coeff_temp*(v0102_liftcp)*1
pv093__007j_pv073_density = temp_power.flatten()
temp_power = _007i_coeff_temp*1*(v073_density)
pv093__007j_pv0102_liftcp = temp_power.flatten()
path_to_v073_density = DIAG_MULT(path_to_v093__007j,pv093__007j_pv073_density)
path_to_v0102_liftcp = DIAG_MULT(path_to_v093__007j,pv093__007j_pv0102_liftcp)

# op _007k_power_combination_eval
# REP:  v021_liftn --> v095__007l
# LANG: liftn --> _007l
# full namespace: liftrotor

# _007k_power_combination_eval_pv095__007l_pv021_liftn
temp_power = _007k_coeff_temp*3*(v021_liftn**2.0)
pv095__007l_pv021_liftn = temp_power.flatten()
path_to_v021_liftn = DIAG_MULT(path_to_v095__007l,pv095__007l_pv021_liftn)
path_to_v03_h = path_to_v073_density@pv073_density_pv03_h

# op _007A_custom_explicit_eval
# REP:  v016_liftvAxial, v018_liftvTan --> v0101_liftct, v0102_liftcp
# LANG: liftvAxial, liftvTan --> liftct, liftcp
# full namespace: liftrotor.rotorModel

# _007A_custom_explicit_eval_pv0102_liftcp_pv018_liftvTan
pv0101_liftct_pv016_liftvAxial = _007A_custom_explicit_func_liftct.get_partials('liftct', 'liftvAxial')
pv0101_liftct_pv018_liftvTan = _007A_custom_explicit_func_liftct.get_partials('liftct', 'liftvTan')
pv0102_liftcp_pv016_liftvAxial = _007A_custom_explicit_func_liftct.get_partials('liftcp', 'liftvAxial')
pv0102_liftcp_pv018_liftvTan = _007A_custom_explicit_func_liftct.get_partials('liftcp', 'liftvTan')
path_to_v016_liftvAxial = path_to_v0102_liftcp@pv0102_liftcp_pv016_liftvAxial
path_to_v018_liftvTan = path_to_v0102_liftcp@pv0102_liftcp_pv018_liftvTan

# op _004C_power_combination_eval
# REP:  v020__004B --> v021_liftn
# LANG: _004B --> liftn
# full namespace: 

# _004C_power_combination_eval_pv021_liftn_pv020__004B
temp_power = _004C_coeff_temp*1
pv021_liftn_pv020__004B = temp_power.flatten()
path_to_v020__004B = DIAG_MULT(path_to_v021_liftn,pv021_liftn_pv020__004B)

# op _004u_power_combination_eval
# REP:  v01_v, v015__004t --> v016_liftvAxial
# LANG: v, _004t --> liftvAxial
# full namespace: 

# _004u_power_combination_eval_pv016_liftvAxial_pv015__004t
temp_power = _004u_coeff_temp*1*(v015__004t)
pv016_liftvAxial_pv01_v = temp_power.flatten()
temp_power = _004u_coeff_temp*(v01_v)*1
pv016_liftvAxial_pv015__004t = temp_power.flatten()
path_to_v01_v = DIAG_MULT(path_to_v016_liftvAxial,pv016_liftvAxial_pv01_v)
path_to_v015__004t = DIAG_MULT(path_to_v016_liftvAxial,pv016_liftvAxial_pv015__004t)

# op _004y_power_combination_eval
# REP:  v01_v, v017__004x --> v018_liftvTan
# LANG: v, _004x --> liftvTan
# full namespace: 

# _004y_power_combination_eval_pv018_liftvTan_pv017__004x
temp_power = _004y_coeff_temp*1*(v017__004x)
pv018_liftvTan_pv01_v = temp_power.flatten()
temp_power = _004y_coeff_temp*(v01_v)*1
pv018_liftvTan_pv017__004x = temp_power.flatten()
path_to_v01_v += DIAG_MULT(path_to_v018_liftvTan,pv018_liftvTan_pv01_v)
path_to_v017__004x = DIAG_MULT(path_to_v018_liftvTan,pv018_liftvTan_pv017__004x)

# op _004A_power_combination_eval
# REP:  v019_control_z --> v020__004B
# LANG: control_z --> _004B
# full namespace: 

# _004A_power_combination_eval_pv020__004B_pv019_control_z
temp_power = _004A_coeff_temp*1
pv020__004B_pv019_control_z = temp_power.flatten()
path_to_v019_control_z = DIAG_MULT(path_to_v020__004B,pv020__004B_pv019_control_z)

# op _004s_sin_eval
# REP:  v06_control_alpha --> v015__004t
# LANG: control_alpha --> _004t
# full namespace: 

# _004s_sin_eval_pv015__004t_pv06_control_alpha
pv015__004t_pv06_control_alpha = np.cos(v06_control_alpha).flatten()
path_to_v06_control_alpha = DIAG_MULT(path_to_v015__004t,pv015__004t_pv06_control_alpha)

# op _004w_cos_eval
# REP:  v06_control_alpha --> v017__004x
# LANG: control_alpha --> _004x
# full namespace: 

# _004w_cos_eval_pv017__004x_pv06_control_alpha
pv017__004x_pv06_control_alpha = -np.sin(v06_control_alpha).flatten()
path_to_v06_control_alpha += DIAG_MULT(path_to_v017__004x,pv017__004x_pv06_control_alpha)
dv096_liftpower_dv01_v = path_to_v01_v.copy()
# dv096_liftpower_dv02_gamma = zero
dv096_liftpower_dv03_h = path_to_v03_h.copy()
# dv096_liftpower_dv04_x = zero
# dv096_liftpower_dv05_e = zero
dv096_liftpower_dv06_control_alpha = path_to_v06_control_alpha.copy()
# dv096_liftpower_dv011_control_x = zero
dv096_liftpower_dv019_control_z = path_to_v019_control_z.copy()