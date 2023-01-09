

# DERIVATIVESdv,dgamma,dh,dx,de-->v,gamma,h,x,e,control_alpha,control_x,control_z

# REV:v035_dv,v051_dgamma,v053_dh,v055_dx,v060_de,-->v01_v,v02_gamma,v03_h,v04_x,v05_e,v06_control_alpha,v011_control_x,v019_control_z,

# :::::::v035_dv-->v01_v,v02_gamma,v03_h,v04_x,v05_e,v06_control_alpha,v011_control_x,v019_control_z,:::::::

# op _001m_linear_combination_eval
# REP:  v032__001h, v034__001l --> v035_dv
# LANG: _001h, _001l --> dv
# full namespace: 

# _001m_linear_combination_eval_pv035_dv_pv034__001l
path_to_v032__001h = np.diagflat(pv035_dv_pv032__001h)
path_to_v034__001l = np.diagflat(pv035_dv_pv034__001l)

# op _001g_linear_combination_eval
# REP:  v030__001d, v031__001f --> v032__001h
# LANG: _001d, _001f --> _001h
# full namespace: 

# _001g_linear_combination_eval_pv032__001h_pv031__001f
path_to_v030__001d = DIAG_MULT(path_to_v032__001h,pv032__001h_pv030__001d)
path_to_v031__001f = DIAG_MULT(path_to_v032__001h,pv032__001h_pv031__001f)

# op _001k_power_combination_eval
# REP:  v033__001j --> v034__001l
# LANG: _001j --> _001l
# full namespace: 

# _001k_power_combination_eval_pv034__001l_pv033__001j
temp_power = _001k_coeff_temp*1
pv034__001l_pv033__001j = temp_power.flatten()
path_to_v033__001j = DIAG_MULT(path_to_v034__001l,pv034__001l_pv033__001j)

# op _001c_linear_combination_eval
# REP:  v025__0015, v029__001b --> v030__001d
# LANG: _0015, _001b --> _001d
# full namespace: 

# _001c_linear_combination_eval_pv030__001d_pv029__001b
path_to_v025__0015 = DIAG_MULT(path_to_v030__001d,pv030__001d_pv025__0015)
path_to_v029__001b = DIAG_MULT(path_to_v030__001d,pv030__001d_pv029__001b)

# op _001e_power_combination_eval
# REP:  v068_drag --> v031__001f
# LANG: drag --> _001f
# full namespace: 

# _001e_power_combination_eval_pv031__001f_pv068_drag
temp_power = _001e_coeff_temp*1
pv031__001f_pv068_drag = temp_power.flatten()
path_to_v068_drag = DIAG_MULT(path_to_v031__001f,pv031__001f_pv068_drag)

# op _001i_sin_eval
# REP:  v02_gamma --> v033__001j
# LANG: gamma --> _001j
# full namespace: 

# _001i_sin_eval_pv033__001j_pv02_gamma
pv033__001j_pv02_gamma = np.cos(v02_gamma).flatten()
path_to_v02_gamma = DIAG_MULT(path_to_v033__001j,pv033__001j_pv02_gamma)

# op _0014_power_combination_eval
# REP:  v023__0011, v024__0013 --> v025__0015
# LANG: _0011, _0013 --> _0015
# full namespace: 

# _0014_power_combination_eval_pv025__0015_pv024__0013
temp_power = _0014_coeff_temp*1*(v024__0013)
pv025__0015_pv023__0011 = temp_power.flatten()
temp_power = _0014_coeff_temp*(v023__0011)*1
pv025__0015_pv024__0013 = temp_power.flatten()
path_to_v023__0011 = DIAG_MULT(path_to_v025__0015,pv025__0015_pv023__0011)
path_to_v024__0013 = DIAG_MULT(path_to_v025__0015,pv025__0015_pv024__0013)

# op _001a_power_combination_eval
# REP:  v027__0017, v028__0019 --> v029__001b
# LANG: _0017, _0019 --> _001b
# full namespace: 

# _001a_power_combination_eval_pv029__001b_pv028__0019
temp_power = _001a_coeff_temp*1*(v028__0019)
pv029__001b_pv027__0017 = temp_power.flatten()
temp_power = _001a_coeff_temp*(v027__0017)*1
pv029__001b_pv028__0019 = temp_power.flatten()
path_to_v027__0017 = DIAG_MULT(path_to_v029__001b,pv029__001b_pv027__0017)
path_to_v028__0019 = DIAG_MULT(path_to_v029__001b,pv029__001b_pv028__0019)

# op _002w_power_combination_eval
# REP:  v067__002v, v069__002p --> v068_drag
# LANG: _002v, _002p --> drag
# full namespace: aero

# _002w_power_combination_eval_pv068_drag_pv069__002p
temp_power = _002w_coeff_temp*1*(v069__002p)
pv068_drag_pv067__002v = temp_power.flatten()
temp_power = _002w_coeff_temp*(v067__002v)*1
pv068_drag_pv069__002p = temp_power.flatten()
path_to_v067__002v = DIAG_MULT(path_to_v068_drag,pv068_drag_pv067__002v)
path_to_v069__002p = DIAG_MULT(path_to_v068_drag,pv068_drag_pv069__002p)

# op _0010_power_combination_eval
# REP:  v077_cruisethrust --> v023__0011
# LANG: cruisethrust --> _0011
# full namespace: 

# _0010_power_combination_eval_pv023__0011_pv077_cruisethrust
temp_power = _0010_coeff_temp*1
pv023__0011_pv077_cruisethrust = temp_power.flatten()
path_to_v077_cruisethrust = DIAG_MULT(path_to_v023__0011,pv023__0011_pv077_cruisethrust)

# op _0012_cos_eval
# REP:  v06_control_alpha --> v024__0013
# LANG: control_alpha --> _0013
# full namespace: 

# _0012_cos_eval_pv024__0013_pv06_control_alpha
pv024__0013_pv06_control_alpha = -np.sin(v06_control_alpha).flatten()
path_to_v06_control_alpha = DIAG_MULT(path_to_v024__0013,pv024__0013_pv06_control_alpha)

# op _0016_power_combination_eval
# REP:  v026__000X --> v027__0017
# LANG: _000X --> _0017
# full namespace: 

# _0016_power_combination_eval_pv027__0017_pv026__000X
temp_power = _0016_coeff_temp*1
pv027__0017_pv026__000X = temp_power.flatten()
path_to_v026__000X = DIAG_MULT(path_to_v027__0017,pv027__0017_pv026__000X)

# op _0018_sin_eval
# REP:  v06_control_alpha --> v028__0019
# LANG: control_alpha --> _0019
# full namespace: 

# _0018_sin_eval_pv028__0019_pv06_control_alpha
pv028__0019_pv06_control_alpha = np.cos(v06_control_alpha).flatten()
path_to_v06_control_alpha += DIAG_MULT(path_to_v028__0019,pv028__0019_pv06_control_alpha)

# op _002u_power_combination_eval
# REP:  v063__002n --> v067__002v
# LANG: _002n --> _002v
# full namespace: aero

# _002u_power_combination_eval_pv067__002v_pv063__002n
temp_power = _002u_coeff_temp*1
pv067__002v_pv063__002n = temp_power.flatten()
path_to_v063__002n = DIAG_MULT(path_to_v067__002v,pv067__002v_pv063__002n)

# op _002o_linear_combination_eval
# REP:  v071_cd --> v069__002p
# LANG: cd --> _002p
# full namespace: aero

# _002o_linear_combination_eval_pv069__002p_pv071_cd
path_to_v071_cd = DIAG_MULT(path_to_v069__002p,pv069__002p_pv071_cd)

# op _002R_power_combination_eval
# REP:  v075__002Q --> v077_cruisethrust
# LANG: _002Q --> cruisethrust
# full namespace: cruiserotor

# _002R_power_combination_eval_pv077_cruisethrust_pv075__002Q
temp_power = _002R_coeff_temp*1
pv077_cruisethrust_pv075__002Q = temp_power.flatten()
path_to_v075__002Q = DIAG_MULT(path_to_v077_cruisethrust,pv077_cruisethrust_pv075__002Q)

# op _000W_power_combination_eval
# REP:  v092_liftthrust --> v026__000X
# LANG: liftthrust --> _000X
# full namespace: 

# _000W_power_combination_eval_pv026__000X_pv092_liftthrust
temp_power = _000W_coeff_temp*1
pv026__000X_pv092_liftthrust = temp_power.flatten()
path_to_v092_liftthrust = DIAG_MULT(path_to_v026__000X,pv026__000X_pv092_liftthrust)

# op _002m_power_combination_eval
# REP:  v062__002j, v064__002l --> v063__002n
# LANG: _002j, _002l --> _002n
# full namespace: aero

# _002m_power_combination_eval_pv063__002n_pv064__002l
temp_power = _002m_coeff_temp*1*(v064__002l)
pv063__002n_pv062__002j = temp_power.flatten()
temp_power = _002m_coeff_temp*(v062__002j)*1
pv063__002n_pv064__002l = temp_power.flatten()
path_to_v062__002j = DIAG_MULT(path_to_v063__002n,pv063__002n_pv062__002j)
path_to_v064__002l = DIAG_MULT(path_to_v063__002n,pv063__002n_pv064__002l)

# op _002z_custom_explicit_eval
# REP:  v061_alpha_w --> v070_cl, v071_cd
# LANG: alpha_w --> cl, cd
# full namespace: aero.airfoil

# _002z_custom_explicit_eval_pv071_cd_pv061_alpha_w
pv070_cl_pv061_alpha_w = _002z_custom_explicit_func_cl.get_partials('cl', 'alpha_w')
pv071_cd_pv061_alpha_w = _002z_custom_explicit_func_cl.get_partials('cd', 'alpha_w')
path_to_v061_alpha_w = path_to_v071_cd@pv071_cd_pv061_alpha_w

# op _002P_power_combination_eval
# REP:  v074__002M, v076__002O --> v075__002Q
# LANG: _002M, _002O --> _002Q
# full namespace: cruiserotor

# _002P_power_combination_eval_pv075__002Q_pv076__002O
temp_power = _002P_coeff_temp*1*(v076__002O)
pv075__002Q_pv074__002M = temp_power.flatten()
temp_power = _002P_coeff_temp*(v074__002M)*1
pv075__002Q_pv076__002O = temp_power.flatten()
path_to_v074__002M = DIAG_MULT(path_to_v075__002Q,pv075__002Q_pv074__002M)
path_to_v076__002O = DIAG_MULT(path_to_v075__002Q,pv075__002Q_pv076__002O)

# op _003s_power_combination_eval
# REP:  v090__003r --> v092_liftthrust
# LANG: _003r --> liftthrust
# full namespace: liftrotor

# _003s_power_combination_eval_pv092_liftthrust_pv090__003r
temp_power = _003s_coeff_temp*1
pv092_liftthrust_pv090__003r = temp_power.flatten()
path_to_v090__003r = DIAG_MULT(path_to_v092_liftthrust,pv092_liftthrust_pv090__003r)

# op _002i_power_combination_eval
# REP:  v073_density --> v062__002j
# LANG: density --> _002j
# full namespace: aero

# _002i_power_combination_eval_pv062__002j_pv073_density
temp_power = _002i_coeff_temp*1
pv062__002j_pv073_density = temp_power.flatten()
path_to_v073_density = DIAG_MULT(path_to_v062__002j,pv062__002j_pv073_density)

# op _002k_power_combination_eval
# REP:  v01_v --> v064__002l
# LANG: v --> _002l
# full namespace: aero

# _002k_power_combination_eval_pv064__002l_pv01_v
temp_power = _002k_coeff_temp*2*(v01_v)
pv064__002l_pv01_v = temp_power.flatten()
path_to_v01_v = DIAG_MULT(path_to_v064__002l,pv064__002l_pv01_v)

# op _002a_linear_combination_eval
# REP:  v06_control_alpha --> v061_alpha_w
# LANG: control_alpha --> alpha_w
# full namespace: aero

# _002a_linear_combination_eval_pv061_alpha_w_pv06_control_alpha
path_to_v06_control_alpha += DIAG_MULT(path_to_v061_alpha_w,pv061_alpha_w_pv06_control_alpha)

# op _002L_power_combination_eval
# REP:  v073_density, v086_cruisect --> v074__002M
# LANG: density, cruisect --> _002M
# full namespace: cruiserotor

# _002L_power_combination_eval_pv074__002M_pv086_cruisect
temp_power = _002L_coeff_temp*(v086_cruisect)*1
pv074__002M_pv073_density = temp_power.flatten()
temp_power = _002L_coeff_temp*1*(v073_density)
pv074__002M_pv086_cruisect = temp_power.flatten()
path_to_v073_density += DIAG_MULT(path_to_v074__002M,pv074__002M_pv073_density)
path_to_v086_cruisect = DIAG_MULT(path_to_v074__002M,pv074__002M_pv086_cruisect)

# op _002N_power_combination_eval
# REP:  v013_cruisen --> v076__002O
# LANG: cruisen --> _002O
# full namespace: cruiserotor

# _002N_power_combination_eval_pv076__002O_pv013_cruisen
temp_power = _002N_coeff_temp*2*(v013_cruisen)
pv076__002O_pv013_cruisen = temp_power.flatten()
path_to_v013_cruisen = DIAG_MULT(path_to_v076__002O,pv076__002O_pv013_cruisen)

# op _003q_power_combination_eval
# REP:  v089__003n, v091__003p --> v090__003r
# LANG: _003n, _003p --> _003r
# full namespace: liftrotor

# _003q_power_combination_eval_pv090__003r_pv091__003p
temp_power = _003q_coeff_temp*1*(v091__003p)
pv090__003r_pv089__003n = temp_power.flatten()
temp_power = _003q_coeff_temp*(v089__003n)*1
pv090__003r_pv091__003p = temp_power.flatten()
path_to_v089__003n = DIAG_MULT(path_to_v090__003r,pv090__003r_pv089__003n)
path_to_v091__003p = DIAG_MULT(path_to_v090__003r,pv090__003r_pv091__003p)

# op _003a_custom_explicit_eval
# REP:  v08_cruisevAxial, v010_cruisevTan --> v086_cruisect, v087_cruisecp
# LANG: cruisevAxial, cruisevTan --> cruisect, cruisecp
# full namespace: cruiserotor.rotorModel

# _003a_custom_explicit_eval_pv087_cruisecp_pv010_cruisevTan
pv086_cruisect_pv08_cruisevAxial = _003a_custom_explicit_func_cruisect.get_partials('cruisect', 'cruisevAxial')
pv086_cruisect_pv010_cruisevTan = _003a_custom_explicit_func_cruisect.get_partials('cruisect', 'cruisevTan')
pv087_cruisecp_pv08_cruisevAxial = _003a_custom_explicit_func_cruisect.get_partials('cruisecp', 'cruisevAxial')
pv087_cruisecp_pv010_cruisevTan = _003a_custom_explicit_func_cruisect.get_partials('cruisecp', 'cruisevTan')
path_to_v08_cruisevAxial = path_to_v086_cruisect@pv086_cruisect_pv08_cruisevAxial
path_to_v010_cruisevTan = path_to_v086_cruisect@pv086_cruisect_pv010_cruisevTan

# op _000v_power_combination_eval
# REP:  v012__000u --> v013_cruisen
# LANG: _000u --> cruisen
# full namespace: 

# _000v_power_combination_eval_pv013_cruisen_pv012__000u
temp_power = _000v_coeff_temp*1
pv013_cruisen_pv012__000u = temp_power.flatten()
path_to_v012__000u = DIAG_MULT(path_to_v013_cruisen,pv013_cruisen_pv012__000u)

# op _003m_power_combination_eval
# REP:  v073_density, v0101_liftct --> v089__003n
# LANG: density, liftct --> _003n
# full namespace: liftrotor

# _003m_power_combination_eval_pv089__003n_pv0101_liftct
temp_power = _003m_coeff_temp*(v0101_liftct)*1
pv089__003n_pv073_density = temp_power.flatten()
temp_power = _003m_coeff_temp*1*(v073_density)
pv089__003n_pv0101_liftct = temp_power.flatten()
path_to_v073_density += DIAG_MULT(path_to_v089__003n,pv089__003n_pv073_density)
path_to_v0101_liftct = DIAG_MULT(path_to_v089__003n,pv089__003n_pv0101_liftct)

# op _003o_power_combination_eval
# REP:  v021_liftn --> v091__003p
# LANG: liftn --> _003p
# full namespace: liftrotor

# _003o_power_combination_eval_pv091__003p_pv021_liftn
temp_power = _003o_coeff_temp*2*(v021_liftn)
pv091__003p_pv021_liftn = temp_power.flatten()
path_to_v021_liftn = DIAG_MULT(path_to_v091__003p,pv091__003p_pv021_liftn)

# op _000n_power_combination_eval
# REP:  v01_v, v07__000m --> v08_cruisevAxial
# LANG: v, _000m --> cruisevAxial
# full namespace: 

# _000n_power_combination_eval_pv08_cruisevAxial_pv07__000m
temp_power = _000n_coeff_temp*1*(v07__000m)
pv08_cruisevAxial_pv01_v = temp_power.flatten()
temp_power = _000n_coeff_temp*(v01_v)*1
pv08_cruisevAxial_pv07__000m = temp_power.flatten()
path_to_v01_v += DIAG_MULT(path_to_v08_cruisevAxial,pv08_cruisevAxial_pv01_v)
path_to_v07__000m = DIAG_MULT(path_to_v08_cruisevAxial,pv08_cruisevAxial_pv07__000m)

# op _000r_power_combination_eval
# REP:  v01_v, v09__000q --> v010_cruisevTan
# LANG: v, _000q --> cruisevTan
# full namespace: 

# _000r_power_combination_eval_pv010_cruisevTan_pv09__000q
temp_power = _000r_coeff_temp*1*(v09__000q)
pv010_cruisevTan_pv01_v = temp_power.flatten()
temp_power = _000r_coeff_temp*(v01_v)*1
pv010_cruisevTan_pv09__000q = temp_power.flatten()
path_to_v01_v += DIAG_MULT(path_to_v010_cruisevTan,pv010_cruisevTan_pv01_v)
path_to_v09__000q = DIAG_MULT(path_to_v010_cruisevTan,pv010_cruisevTan_pv09__000q)

# op _000t_power_combination_eval
# REP:  v011_control_x --> v012__000u
# LANG: control_x --> _000u
# full namespace: 

# _000t_power_combination_eval_pv012__000u_pv011_control_x
temp_power = _000t_coeff_temp*1
pv012__000u_pv011_control_x = temp_power.flatten()
path_to_v011_control_x = DIAG_MULT(path_to_v012__000u,pv012__000u_pv011_control_x)

# op _002D_custom_explicit_eval
# REP:  v03_h --> v072_pressure, v073_density
# LANG: h --> pressure, density
# full namespace: aero.atmosphere

# _002D_custom_explicit_eval_pv073_density_pv03_h
pv072_pressure_pv03_h = _002D_custom_explicit_func_pressure.get_partials('pressure', 'h')
pv073_density_pv03_h = _002D_custom_explicit_func_pressure.get_partials('density', 'h')
path_to_v03_h = path_to_v073_density@pv073_density_pv03_h

# op _003M_custom_explicit_eval
# REP:  v016_liftvAxial, v018_liftvTan --> v0101_liftct, v0102_liftcp
# LANG: liftvAxial, liftvTan --> liftct, liftcp
# full namespace: liftrotor.rotorModel

# _003M_custom_explicit_eval_pv0102_liftcp_pv018_liftvTan
pv0101_liftct_pv016_liftvAxial = _003M_custom_explicit_func_liftct.get_partials('liftct', 'liftvAxial')
pv0101_liftct_pv018_liftvTan = _003M_custom_explicit_func_liftct.get_partials('liftct', 'liftvTan')
pv0102_liftcp_pv016_liftvAxial = _003M_custom_explicit_func_liftct.get_partials('liftcp', 'liftvAxial')
pv0102_liftcp_pv018_liftvTan = _003M_custom_explicit_func_liftct.get_partials('liftcp', 'liftvTan')
path_to_v016_liftvAxial = path_to_v0101_liftct@pv0101_liftct_pv016_liftvAxial
path_to_v018_liftvTan = path_to_v0101_liftct@pv0101_liftct_pv018_liftvTan

# op _000O_power_combination_eval
# REP:  v020__000N --> v021_liftn
# LANG: _000N --> liftn
# full namespace: 

# _000O_power_combination_eval_pv021_liftn_pv020__000N
temp_power = _000O_coeff_temp*1
pv021_liftn_pv020__000N = temp_power.flatten()
path_to_v020__000N = DIAG_MULT(path_to_v021_liftn,pv021_liftn_pv020__000N)

# op _000l_cos_eval
# REP:  v06_control_alpha --> v07__000m
# LANG: control_alpha --> _000m
# full namespace: 

# _000l_cos_eval_pv07__000m_pv06_control_alpha
pv07__000m_pv06_control_alpha = -np.sin(v06_control_alpha).flatten()
path_to_v06_control_alpha += DIAG_MULT(path_to_v07__000m,pv07__000m_pv06_control_alpha)

# op _000p_sin_eval
# REP:  v06_control_alpha --> v09__000q
# LANG: control_alpha --> _000q
# full namespace: 

# _000p_sin_eval_pv09__000q_pv06_control_alpha
pv09__000q_pv06_control_alpha = np.cos(v06_control_alpha).flatten()
path_to_v06_control_alpha += DIAG_MULT(path_to_v09__000q,pv09__000q_pv06_control_alpha)

# op _000G_power_combination_eval
# REP:  v01_v, v015__000F --> v016_liftvAxial
# LANG: v, _000F --> liftvAxial
# full namespace: 

# _000G_power_combination_eval_pv016_liftvAxial_pv015__000F
temp_power = _000G_coeff_temp*1*(v015__000F)
pv016_liftvAxial_pv01_v = temp_power.flatten()
temp_power = _000G_coeff_temp*(v01_v)*1
pv016_liftvAxial_pv015__000F = temp_power.flatten()
path_to_v01_v += DIAG_MULT(path_to_v016_liftvAxial,pv016_liftvAxial_pv01_v)
path_to_v015__000F = DIAG_MULT(path_to_v016_liftvAxial,pv016_liftvAxial_pv015__000F)

# op _000K_power_combination_eval
# REP:  v01_v, v017__000J --> v018_liftvTan
# LANG: v, _000J --> liftvTan
# full namespace: 

# _000K_power_combination_eval_pv018_liftvTan_pv017__000J
temp_power = _000K_coeff_temp*1*(v017__000J)
pv018_liftvTan_pv01_v = temp_power.flatten()
temp_power = _000K_coeff_temp*(v01_v)*1
pv018_liftvTan_pv017__000J = temp_power.flatten()
path_to_v01_v += DIAG_MULT(path_to_v018_liftvTan,pv018_liftvTan_pv01_v)
path_to_v017__000J = DIAG_MULT(path_to_v018_liftvTan,pv018_liftvTan_pv017__000J)

# op _000M_power_combination_eval
# REP:  v019_control_z --> v020__000N
# LANG: control_z --> _000N
# full namespace: 

# _000M_power_combination_eval_pv020__000N_pv019_control_z
temp_power = _000M_coeff_temp*1
pv020__000N_pv019_control_z = temp_power.flatten()
path_to_v019_control_z = DIAG_MULT(path_to_v020__000N,pv020__000N_pv019_control_z)

# op _000E_sin_eval
# REP:  v06_control_alpha --> v015__000F
# LANG: control_alpha --> _000F
# full namespace: 

# _000E_sin_eval_pv015__000F_pv06_control_alpha
pv015__000F_pv06_control_alpha = np.cos(v06_control_alpha).flatten()
path_to_v06_control_alpha += DIAG_MULT(path_to_v015__000F,pv015__000F_pv06_control_alpha)

# op _000I_cos_eval
# REP:  v06_control_alpha --> v017__000J
# LANG: control_alpha --> _000J
# full namespace: 

# _000I_cos_eval_pv017__000J_pv06_control_alpha
pv017__000J_pv06_control_alpha = -np.sin(v06_control_alpha).flatten()
path_to_v06_control_alpha += DIAG_MULT(path_to_v017__000J,pv017__000J_pv06_control_alpha)
dv035_dv_dv01_v = path_to_v01_v.copy()
dv035_dv_dv02_gamma = path_to_v02_gamma.copy()
dv035_dv_dv03_h = path_to_v03_h.copy()
# dv035_dv_dv04_x = zero
# dv035_dv_dv05_e = zero
dv035_dv_dv06_control_alpha = path_to_v06_control_alpha.copy()
dv035_dv_dv011_control_x = path_to_v011_control_x.copy()
dv035_dv_dv019_control_z = path_to_v019_control_z.copy()

# :::::::v051_dgamma-->v01_v,v02_gamma,v03_h,v04_x,v05_e,v06_control_alpha,v011_control_x,v019_control_z,:::::::

# op _001S_linear_combination_eval
# REP:  v047__001L, v050__001R --> v051_dgamma
# LANG: _001L, _001R --> dgamma
# full namespace: 

# _001S_linear_combination_eval_pv051_dgamma_pv050__001R
path_to_v047__001L = np.diagflat(pv051_dgamma_pv047__001L)
path_to_v050__001R = np.diagflat(pv051_dgamma_pv050__001R)

# op _001K_linear_combination_eval
# REP:  v044__001F, v046__001J --> v047__001L
# LANG: _001F, _001J --> _001L
# full namespace: 

# _001K_linear_combination_eval_pv047__001L_pv046__001J
path_to_v044__001F = DIAG_MULT(path_to_v047__001L,pv047__001L_pv044__001F)
path_to_v046__001J = DIAG_MULT(path_to_v047__001L,pv047__001L_pv046__001J)

# op _001Q_power_combination_eval
# REP:  v01_v, v049__001P --> v050__001R
# LANG: v, _001P --> _001R
# full namespace: 

# _001Q_power_combination_eval_pv050__001R_pv049__001P
temp_power = _001Q_coeff_temp*(v049__001P)*-1*(v01_v**-2.0)
pv050__001R_pv01_v = temp_power.flatten()
temp_power = _001Q_coeff_temp*1*(v01_v**-1)
pv050__001R_pv049__001P = temp_power.flatten()
path_to_v01_v = DIAG_MULT(path_to_v050__001R,pv050__001R_pv01_v)
path_to_v049__001P = DIAG_MULT(path_to_v050__001R,pv050__001R_pv049__001P)

# op _001E_linear_combination_eval
# REP:  v039__001v, v043__001D --> v044__001F
# LANG: _001v, _001D --> _001F
# full namespace: 

# _001E_linear_combination_eval_pv044__001F_pv043__001D
path_to_v039__001v = DIAG_MULT(path_to_v044__001F,pv044__001F_pv039__001v)
path_to_v043__001D = DIAG_MULT(path_to_v044__001F,pv044__001F_pv043__001D)

# op _001I_power_combination_eval
# REP:  v045__001H, v066_lift --> v046__001J
# LANG: _001H, lift --> _001J
# full namespace: 

# _001I_power_combination_eval_pv046__001J_pv066_lift
temp_power = _001I_coeff_temp*(v066_lift)*-1*(v045__001H**-2.0)
pv046__001J_pv045__001H = temp_power.flatten()
temp_power = _001I_coeff_temp*1*(v045__001H**-1)
pv046__001J_pv066_lift = temp_power.flatten()
path_to_v045__001H = DIAG_MULT(path_to_v046__001J,pv046__001J_pv045__001H)
path_to_v066_lift = DIAG_MULT(path_to_v046__001J,pv046__001J_pv066_lift)

# op _001O_power_combination_eval
# REP:  v048__001N --> v049__001P
# LANG: _001N --> _001P
# full namespace: 

# _001O_power_combination_eval_pv049__001P_pv048__001N
temp_power = _001O_coeff_temp*1
pv049__001P_pv048__001N = temp_power.flatten()
path_to_v048__001N = DIAG_MULT(path_to_v049__001P,pv049__001P_pv048__001N)

# op _001u_power_combination_eval
# REP:  v037__001r, v038__001t --> v039__001v
# LANG: _001r, _001t --> _001v
# full namespace: 

# _001u_power_combination_eval_pv039__001v_pv038__001t
temp_power = _001u_coeff_temp*1*(v038__001t)
pv039__001v_pv037__001r = temp_power.flatten()
temp_power = _001u_coeff_temp*(v037__001r)*1
pv039__001v_pv038__001t = temp_power.flatten()
path_to_v037__001r = DIAG_MULT(path_to_v039__001v,pv039__001v_pv037__001r)
path_to_v038__001t = DIAG_MULT(path_to_v039__001v,pv039__001v_pv038__001t)

# op _001C_power_combination_eval
# REP:  v041__001z, v042__001B --> v043__001D
# LANG: _001z, _001B --> _001D
# full namespace: 

# _001C_power_combination_eval_pv043__001D_pv042__001B
temp_power = _001C_coeff_temp*1*(v042__001B)
pv043__001D_pv041__001z = temp_power.flatten()
temp_power = _001C_coeff_temp*(v041__001z)*1
pv043__001D_pv042__001B = temp_power.flatten()
path_to_v041__001z = DIAG_MULT(path_to_v043__001D,pv043__001D_pv041__001z)
path_to_v042__001B = DIAG_MULT(path_to_v043__001D,pv043__001D_pv042__001B)

# op _001G_power_combination_eval
# REP:  v01_v --> v045__001H
# LANG: v --> _001H
# full namespace: 

# _001G_power_combination_eval_pv045__001H_pv01_v
temp_power = _001G_coeff_temp*1
pv045__001H_pv01_v = temp_power.flatten()
path_to_v01_v += DIAG_MULT(path_to_v045__001H,pv045__001H_pv01_v)

# op _002s_power_combination_eval
# REP:  v065__002r, v070_cl --> v066_lift
# LANG: _002r, cl --> lift
# full namespace: aero

# _002s_power_combination_eval_pv066_lift_pv070_cl
temp_power = _002s_coeff_temp*1*(v070_cl)
pv066_lift_pv065__002r = temp_power.flatten()
temp_power = _002s_coeff_temp*(v065__002r)*1
pv066_lift_pv070_cl = temp_power.flatten()
path_to_v065__002r = DIAG_MULT(path_to_v066_lift,pv066_lift_pv065__002r)
path_to_v070_cl = DIAG_MULT(path_to_v066_lift,pv066_lift_pv070_cl)

# op _001M_cos_eval
# REP:  v02_gamma --> v048__001N
# LANG: gamma --> _001N
# full namespace: 

# _001M_cos_eval_pv048__001N_pv02_gamma
pv048__001N_pv02_gamma = -np.sin(v02_gamma).flatten()
path_to_v02_gamma = DIAG_MULT(path_to_v048__001N,pv048__001N_pv02_gamma)

# op _001q_power_combination_eval
# REP:  v036__001p, v077_cruisethrust --> v037__001r
# LANG: _001p, cruisethrust --> _001r
# full namespace: 

# _001q_power_combination_eval_pv037__001r_pv077_cruisethrust
temp_power = _001q_coeff_temp*(v077_cruisethrust)*-1*(v036__001p**-2.0)
pv037__001r_pv036__001p = temp_power.flatten()
temp_power = _001q_coeff_temp*1*(v036__001p**-1)
pv037__001r_pv077_cruisethrust = temp_power.flatten()
path_to_v036__001p = DIAG_MULT(path_to_v037__001r,pv037__001r_pv036__001p)
path_to_v077_cruisethrust = DIAG_MULT(path_to_v037__001r,pv037__001r_pv077_cruisethrust)

# op _001s_sin_eval
# REP:  v06_control_alpha --> v038__001t
# LANG: control_alpha --> _001t
# full namespace: 

# _001s_sin_eval_pv038__001t_pv06_control_alpha
pv038__001t_pv06_control_alpha = np.cos(v06_control_alpha).flatten()
path_to_v06_control_alpha = DIAG_MULT(path_to_v038__001t,pv038__001t_pv06_control_alpha)

# op _001y_power_combination_eval
# REP:  v026__000X, v040__001x --> v041__001z
# LANG: _000X, _001x --> _001z
# full namespace: 

# _001y_power_combination_eval_pv041__001z_pv040__001x
temp_power = _001y_coeff_temp*1*(v040__001x**-1)
pv041__001z_pv026__000X = temp_power.flatten()
temp_power = _001y_coeff_temp*(v026__000X)*-1*(v040__001x**-2.0)
pv041__001z_pv040__001x = temp_power.flatten()
path_to_v026__000X = DIAG_MULT(path_to_v041__001z,pv041__001z_pv026__000X)
path_to_v040__001x = DIAG_MULT(path_to_v041__001z,pv041__001z_pv040__001x)

# op _001A_cos_eval
# REP:  v06_control_alpha --> v042__001B
# LANG: control_alpha --> _001B
# full namespace: 

# _001A_cos_eval_pv042__001B_pv06_control_alpha
pv042__001B_pv06_control_alpha = -np.sin(v06_control_alpha).flatten()
path_to_v06_control_alpha += DIAG_MULT(path_to_v042__001B,pv042__001B_pv06_control_alpha)

# op _002q_power_combination_eval
# REP:  v063__002n --> v065__002r
# LANG: _002n --> _002r
# full namespace: aero

# _002q_power_combination_eval_pv065__002r_pv063__002n
temp_power = _002q_coeff_temp*1
pv065__002r_pv063__002n = temp_power.flatten()
path_to_v063__002n = DIAG_MULT(path_to_v065__002r,pv065__002r_pv063__002n)
path_to_v061_alpha_w = path_to_v070_cl@pv070_cl_pv061_alpha_w

# op _001o_power_combination_eval
# REP:  v01_v --> v036__001p
# LANG: v --> _001p
# full namespace: 

# _001o_power_combination_eval_pv036__001p_pv01_v
temp_power = _001o_coeff_temp*1
pv036__001p_pv01_v = temp_power.flatten()
path_to_v01_v += DIAG_MULT(path_to_v036__001p,pv036__001p_pv01_v)
path_to_v075__002Q = DIAG_MULT(path_to_v077_cruisethrust,pv077_cruisethrust_pv075__002Q)
path_to_v092_liftthrust = DIAG_MULT(path_to_v026__000X,pv026__000X_pv092_liftthrust)

# op _001w_power_combination_eval
# REP:  v01_v --> v040__001x
# LANG: v --> _001x
# full namespace: 

# _001w_power_combination_eval_pv040__001x_pv01_v
temp_power = _001w_coeff_temp*1
pv040__001x_pv01_v = temp_power.flatten()
path_to_v01_v += DIAG_MULT(path_to_v040__001x,pv040__001x_pv01_v)
path_to_v062__002j = DIAG_MULT(path_to_v063__002n,pv063__002n_pv062__002j)
path_to_v064__002l = DIAG_MULT(path_to_v063__002n,pv063__002n_pv064__002l)
path_to_v06_control_alpha += DIAG_MULT(path_to_v061_alpha_w,pv061_alpha_w_pv06_control_alpha)
path_to_v074__002M = DIAG_MULT(path_to_v075__002Q,pv075__002Q_pv074__002M)
path_to_v076__002O = DIAG_MULT(path_to_v075__002Q,pv075__002Q_pv076__002O)
path_to_v090__003r = DIAG_MULT(path_to_v092_liftthrust,pv092_liftthrust_pv090__003r)
path_to_v073_density = DIAG_MULT(path_to_v062__002j,pv062__002j_pv073_density)
path_to_v01_v += DIAG_MULT(path_to_v064__002l,pv064__002l_pv01_v)
path_to_v073_density += DIAG_MULT(path_to_v074__002M,pv074__002M_pv073_density)
path_to_v086_cruisect = DIAG_MULT(path_to_v074__002M,pv074__002M_pv086_cruisect)
path_to_v013_cruisen = DIAG_MULT(path_to_v076__002O,pv076__002O_pv013_cruisen)
path_to_v089__003n = DIAG_MULT(path_to_v090__003r,pv090__003r_pv089__003n)
path_to_v091__003p = DIAG_MULT(path_to_v090__003r,pv090__003r_pv091__003p)
path_to_v08_cruisevAxial = path_to_v086_cruisect@pv086_cruisect_pv08_cruisevAxial
path_to_v010_cruisevTan = path_to_v086_cruisect@pv086_cruisect_pv010_cruisevTan
path_to_v012__000u = DIAG_MULT(path_to_v013_cruisen,pv013_cruisen_pv012__000u)
path_to_v073_density += DIAG_MULT(path_to_v089__003n,pv089__003n_pv073_density)
path_to_v0101_liftct = DIAG_MULT(path_to_v089__003n,pv089__003n_pv0101_liftct)
path_to_v021_liftn = DIAG_MULT(path_to_v091__003p,pv091__003p_pv021_liftn)
path_to_v01_v += DIAG_MULT(path_to_v08_cruisevAxial,pv08_cruisevAxial_pv01_v)
path_to_v07__000m = DIAG_MULT(path_to_v08_cruisevAxial,pv08_cruisevAxial_pv07__000m)
path_to_v01_v += DIAG_MULT(path_to_v010_cruisevTan,pv010_cruisevTan_pv01_v)
path_to_v09__000q = DIAG_MULT(path_to_v010_cruisevTan,pv010_cruisevTan_pv09__000q)
path_to_v011_control_x = DIAG_MULT(path_to_v012__000u,pv012__000u_pv011_control_x)
path_to_v03_h = path_to_v073_density@pv073_density_pv03_h
path_to_v016_liftvAxial = path_to_v0101_liftct@pv0101_liftct_pv016_liftvAxial
path_to_v018_liftvTan = path_to_v0101_liftct@pv0101_liftct_pv018_liftvTan
path_to_v020__000N = DIAG_MULT(path_to_v021_liftn,pv021_liftn_pv020__000N)
path_to_v06_control_alpha += DIAG_MULT(path_to_v07__000m,pv07__000m_pv06_control_alpha)
path_to_v06_control_alpha += DIAG_MULT(path_to_v09__000q,pv09__000q_pv06_control_alpha)
path_to_v01_v += DIAG_MULT(path_to_v016_liftvAxial,pv016_liftvAxial_pv01_v)
path_to_v015__000F = DIAG_MULT(path_to_v016_liftvAxial,pv016_liftvAxial_pv015__000F)
path_to_v01_v += DIAG_MULT(path_to_v018_liftvTan,pv018_liftvTan_pv01_v)
path_to_v017__000J = DIAG_MULT(path_to_v018_liftvTan,pv018_liftvTan_pv017__000J)
path_to_v019_control_z = DIAG_MULT(path_to_v020__000N,pv020__000N_pv019_control_z)
path_to_v06_control_alpha += DIAG_MULT(path_to_v015__000F,pv015__000F_pv06_control_alpha)
path_to_v06_control_alpha += DIAG_MULT(path_to_v017__000J,pv017__000J_pv06_control_alpha)
dv051_dgamma_dv01_v = path_to_v01_v.copy()
dv051_dgamma_dv02_gamma = path_to_v02_gamma.copy()
dv051_dgamma_dv03_h = path_to_v03_h.copy()
# dv051_dgamma_dv04_x = zero
# dv051_dgamma_dv05_e = zero
dv051_dgamma_dv06_control_alpha = path_to_v06_control_alpha.copy()
dv051_dgamma_dv011_control_x = path_to_v011_control_x.copy()
dv051_dgamma_dv019_control_z = path_to_v019_control_z.copy()

# :::::::v053_dh-->v01_v,v02_gamma,v03_h,v04_x,v05_e,v06_control_alpha,v011_control_x,v019_control_z,:::::::

# op _001W_power_combination_eval
# REP:  v01_v, v052__001V --> v053_dh
# LANG: v, _001V --> dh
# full namespace: 

# _001W_power_combination_eval_pv053_dh_pv052__001V
temp_power = _001W_coeff_temp*1*(v052__001V)
pv053_dh_pv01_v = temp_power.flatten()
temp_power = _001W_coeff_temp*(v01_v)*1
pv053_dh_pv052__001V = temp_power.flatten()
path_to_v01_v = np.diagflat(pv053_dh_pv01_v)
path_to_v052__001V = np.diagflat(pv053_dh_pv052__001V)

# op _001U_sin_eval
# REP:  v02_gamma --> v052__001V
# LANG: gamma --> _001V
# full namespace: 

# _001U_sin_eval_pv052__001V_pv02_gamma
pv052__001V_pv02_gamma = np.cos(v02_gamma).flatten()
path_to_v02_gamma = DIAG_MULT(path_to_v052__001V,pv052__001V_pv02_gamma)
dv053_dh_dv01_v = path_to_v01_v.copy()
dv053_dh_dv02_gamma = path_to_v02_gamma.copy()
# dv053_dh_dv03_h = zero
# dv053_dh_dv04_x = zero
# dv053_dh_dv05_e = zero
# dv053_dh_dv06_control_alpha = zero
# dv053_dh_dv011_control_x = zero
# dv053_dh_dv019_control_z = zero

# :::::::v055_dx-->v01_v,v02_gamma,v03_h,v04_x,v05_e,v06_control_alpha,v011_control_x,v019_control_z,:::::::

# op _001__power_combination_eval
# REP:  v01_v, v054__001Z --> v055_dx
# LANG: v, _001Z --> dx
# full namespace: 

# _001__power_combination_eval_pv055_dx_pv054__001Z
temp_power = _001__coeff_temp*1*(v054__001Z)
pv055_dx_pv01_v = temp_power.flatten()
temp_power = _001__coeff_temp*(v01_v)*1
pv055_dx_pv054__001Z = temp_power.flatten()
path_to_v01_v = np.diagflat(pv055_dx_pv01_v)
path_to_v054__001Z = np.diagflat(pv055_dx_pv054__001Z)

# op _001Y_cos_eval
# REP:  v02_gamma --> v054__001Z
# LANG: gamma --> _001Z
# full namespace: 

# _001Y_cos_eval_pv054__001Z_pv02_gamma
pv054__001Z_pv02_gamma = -np.sin(v02_gamma).flatten()
path_to_v02_gamma = DIAG_MULT(path_to_v054__001Z,pv054__001Z_pv02_gamma)
dv055_dx_dv01_v = path_to_v01_v.copy()
dv055_dx_dv02_gamma = path_to_v02_gamma.copy()
# dv055_dx_dv03_h = zero
# dv055_dx_dv04_x = zero
# dv055_dx_dv05_e = zero
# dv055_dx_dv06_control_alpha = zero
# dv055_dx_dv011_control_x = zero
# dv055_dx_dv019_control_z = zero

# :::::::v060_de-->v01_v,v02_gamma,v03_h,v04_x,v05_e,v06_control_alpha,v011_control_x,v019_control_z,:::::::

# op _0027_power_combination_eval
# REP:  v059__0026 --> v060_de
# LANG: _0026 --> de
# full namespace: 

# _0027_power_combination_eval_pv060_de_pv059__0026
temp_power = _0027_coeff_temp*1
pv060_de_pv059__0026 = temp_power.flatten()
path_to_v059__0026 = np.diagflat(pv060_de_pv059__0026)

# op _0025_linear_combination_eval
# REP:  v056__0022, v058__0024 --> v059__0026
# LANG: _0022, _0024 --> _0026
# full namespace: 

# _0025_linear_combination_eval_pv059__0026_pv058__0024
path_to_v056__0022 = DIAG_MULT(path_to_v059__0026,pv059__0026_pv056__0022)
path_to_v058__0024 = DIAG_MULT(path_to_v059__0026,pv059__0026_pv058__0024)

# op _0021_power_combination_eval
# REP:  v081_cruisepower, v088_cruiseeta --> v056__0022
# LANG: cruisepower, cruiseeta --> _0022
# full namespace: 

# _0021_power_combination_eval_pv056__0022_pv088_cruiseeta
temp_power = _0021_coeff_temp*1*(v088_cruiseeta**-1)
pv056__0022_pv081_cruisepower = temp_power.flatten()
temp_power = _0021_coeff_temp*(v081_cruisepower)*-1*(v088_cruiseeta**-2.0)
pv056__0022_pv088_cruiseeta = temp_power.flatten()
path_to_v081_cruisepower = DIAG_MULT(path_to_v056__0022,pv056__0022_pv081_cruisepower)
path_to_v088_cruiseeta = DIAG_MULT(path_to_v056__0022,pv056__0022_pv088_cruiseeta)

# op _0023_power_combination_eval
# REP:  v057__000_, v0103_lifteta --> v058__0024
# LANG: _000_, lifteta --> _0024
# full namespace: 

# _0023_power_combination_eval_pv058__0024_pv0103_lifteta
temp_power = _0023_coeff_temp*1*(v0103_lifteta**-1)
pv058__0024_pv057__000_ = temp_power.flatten()
temp_power = _0023_coeff_temp*(v057__000_)*-1*(v0103_lifteta**-2.0)
pv058__0024_pv0103_lifteta = temp_power.flatten()
path_to_v057__000_ = DIAG_MULT(path_to_v058__0024,pv058__0024_pv057__000_)
path_to_v0103_lifteta = DIAG_MULT(path_to_v058__0024,pv058__0024_pv0103_lifteta)

# op _002Z_power_combination_eval
# REP:  v079__002Y --> v081_cruisepower
# LANG: _002Y --> cruisepower
# full namespace: cruiserotor

# _002Z_power_combination_eval_pv081_cruisepower_pv079__002Y
temp_power = _002Z_coeff_temp*1
pv081_cruisepower_pv079__002Y = temp_power.flatten()
path_to_v079__002Y = DIAG_MULT(path_to_v081_cruisepower,pv081_cruisepower_pv079__002Y)

# op _003f_custom_explicit_eval
# REP:  v014_cruisem, v085_cruisetorque --> v088_cruiseeta
# LANG: cruisem, cruisetorque --> cruiseeta
# full namespace: cruisemotor

# _003f_custom_explicit_eval_pv088_cruiseeta_pv085_cruisetorque
pv088_cruiseeta_pv014_cruisem = _003f_custom_explicit_func_cruiseeta.get_partials('cruiseeta', 'cruisem')
pv088_cruiseeta_pv085_cruisetorque = _003f_custom_explicit_func_cruiseeta.get_partials('cruiseeta', 'cruisetorque')
path_to_v014_cruisem = path_to_v088_cruiseeta@pv088_cruiseeta_pv014_cruisem
path_to_v085_cruisetorque = path_to_v088_cruiseeta@pv088_cruiseeta_pv085_cruisetorque

# op _000Z_power_combination_eval
# REP:  v096_liftpower --> v057__000_
# LANG: liftpower --> _000_
# full namespace: 

# _000Z_power_combination_eval_pv057__000__pv096_liftpower
temp_power = _000Z_coeff_temp*1
pv057__000__pv096_liftpower = temp_power.flatten()
path_to_v096_liftpower = DIAG_MULT(path_to_v057__000_,pv057__000__pv096_liftpower)

# op _003R_custom_explicit_eval
# REP:  v022_liftm, v0100_lifttorque --> v0103_lifteta
# LANG: liftm, lifttorque --> lifteta
# full namespace: liftmotor

# _003R_custom_explicit_eval_pv0103_lifteta_pv0100_lifttorque
pv0103_lifteta_pv022_liftm = _003R_custom_explicit_func_lifteta.get_partials('lifteta', 'liftm')
pv0103_lifteta_pv0100_lifttorque = _003R_custom_explicit_func_lifteta.get_partials('lifteta', 'lifttorque')
path_to_v022_liftm = path_to_v0103_lifteta@pv0103_lifteta_pv022_liftm
path_to_v0100_lifttorque = path_to_v0103_lifteta@pv0103_lifteta_pv0100_lifttorque

# op _002X_power_combination_eval
# REP:  v078__002U, v080__002W --> v079__002Y
# LANG: _002U, _002W --> _002Y
# full namespace: cruiserotor

# _002X_power_combination_eval_pv079__002Y_pv080__002W
temp_power = _002X_coeff_temp*1*(v080__002W)
pv079__002Y_pv078__002U = temp_power.flatten()
temp_power = _002X_coeff_temp*(v078__002U)*1
pv079__002Y_pv080__002W = temp_power.flatten()
path_to_v078__002U = DIAG_MULT(path_to_v079__002Y,pv079__002Y_pv078__002U)
path_to_v080__002W = DIAG_MULT(path_to_v079__002Y,pv079__002Y_pv080__002W)

# op _000x_power_combination_eval
# REP:  v011_control_x --> v014_cruisem
# LANG: control_x --> cruisem
# full namespace: 

# _000x_power_combination_eval_pv014_cruisem_pv011_control_x
temp_power = _000x_coeff_temp*1
pv014_cruisem_pv011_control_x = temp_power.flatten()
path_to_v011_control_x = DIAG_MULT(path_to_v014_cruisem,pv014_cruisem_pv011_control_x)

# op _0036_power_combination_eval
# REP:  v083__0035 --> v085_cruisetorque
# LANG: _0035 --> cruisetorque
# full namespace: cruiserotor

# _0036_power_combination_eval_pv085_cruisetorque_pv083__0035
temp_power = _0036_coeff_temp*1
pv085_cruisetorque_pv083__0035 = temp_power.flatten()
path_to_v083__0035 = DIAG_MULT(path_to_v085_cruisetorque,pv085_cruisetorque_pv083__0035)

# op _003A_power_combination_eval
# REP:  v094__003z --> v096_liftpower
# LANG: _003z --> liftpower
# full namespace: liftrotor

# _003A_power_combination_eval_pv096_liftpower_pv094__003z
temp_power = _003A_coeff_temp*1
pv096_liftpower_pv094__003z = temp_power.flatten()
path_to_v094__003z = DIAG_MULT(path_to_v096_liftpower,pv096_liftpower_pv094__003z)

# op _000Q_power_combination_eval
# REP:  v019_control_z --> v022_liftm
# LANG: control_z --> liftm
# full namespace: 

# _000Q_power_combination_eval_pv022_liftm_pv019_control_z
temp_power = _000Q_coeff_temp*1
pv022_liftm_pv019_control_z = temp_power.flatten()
path_to_v019_control_z = DIAG_MULT(path_to_v022_liftm,pv022_liftm_pv019_control_z)

# op _003I_power_combination_eval
# REP:  v098__003H --> v0100_lifttorque
# LANG: _003H --> lifttorque
# full namespace: liftrotor

# _003I_power_combination_eval_pv0100_lifttorque_pv098__003H
temp_power = _003I_coeff_temp*1
pv0100_lifttorque_pv098__003H = temp_power.flatten()
path_to_v098__003H = DIAG_MULT(path_to_v0100_lifttorque,pv0100_lifttorque_pv098__003H)

# op _002T_power_combination_eval
# REP:  v073_density, v087_cruisecp --> v078__002U
# LANG: density, cruisecp --> _002U
# full namespace: cruiserotor

# _002T_power_combination_eval_pv078__002U_pv087_cruisecp
temp_power = _002T_coeff_temp*(v087_cruisecp)*1
pv078__002U_pv073_density = temp_power.flatten()
temp_power = _002T_coeff_temp*1*(v073_density)
pv078__002U_pv087_cruisecp = temp_power.flatten()
path_to_v073_density = DIAG_MULT(path_to_v078__002U,pv078__002U_pv073_density)
path_to_v087_cruisecp = DIAG_MULT(path_to_v078__002U,pv078__002U_pv087_cruisecp)

# op _002V_power_combination_eval
# REP:  v013_cruisen --> v080__002W
# LANG: cruisen --> _002W
# full namespace: cruiserotor

# _002V_power_combination_eval_pv080__002W_pv013_cruisen
temp_power = _002V_coeff_temp*3*(v013_cruisen**2.0)
pv080__002W_pv013_cruisen = temp_power.flatten()
path_to_v013_cruisen = DIAG_MULT(path_to_v080__002W,pv080__002W_pv013_cruisen)

# op _0034_power_combination_eval
# REP:  v082__0031, v084__0033 --> v083__0035
# LANG: _0031, _0033 --> _0035
# full namespace: cruiserotor

# _0034_power_combination_eval_pv083__0035_pv084__0033
temp_power = _0034_coeff_temp*1*(v084__0033)
pv083__0035_pv082__0031 = temp_power.flatten()
temp_power = _0034_coeff_temp*(v082__0031)*1
pv083__0035_pv084__0033 = temp_power.flatten()
path_to_v082__0031 = DIAG_MULT(path_to_v083__0035,pv083__0035_pv082__0031)
path_to_v084__0033 = DIAG_MULT(path_to_v083__0035,pv083__0035_pv084__0033)

# op _003y_power_combination_eval
# REP:  v093__003v, v095__003x --> v094__003z
# LANG: _003v, _003x --> _003z
# full namespace: liftrotor

# _003y_power_combination_eval_pv094__003z_pv095__003x
temp_power = _003y_coeff_temp*1*(v095__003x)
pv094__003z_pv093__003v = temp_power.flatten()
temp_power = _003y_coeff_temp*(v093__003v)*1
pv094__003z_pv095__003x = temp_power.flatten()
path_to_v093__003v = DIAG_MULT(path_to_v094__003z,pv094__003z_pv093__003v)
path_to_v095__003x = DIAG_MULT(path_to_v094__003z,pv094__003z_pv095__003x)

# op _003G_power_combination_eval
# REP:  v097__003D, v099__003F --> v098__003H
# LANG: _003D, _003F --> _003H
# full namespace: liftrotor

# _003G_power_combination_eval_pv098__003H_pv099__003F
temp_power = _003G_coeff_temp*1*(v099__003F)
pv098__003H_pv097__003D = temp_power.flatten()
temp_power = _003G_coeff_temp*(v097__003D)*1
pv098__003H_pv099__003F = temp_power.flatten()
path_to_v097__003D = DIAG_MULT(path_to_v098__003H,pv098__003H_pv097__003D)
path_to_v099__003F = DIAG_MULT(path_to_v098__003H,pv098__003H_pv099__003F)

# op _0030_power_combination_eval
# REP:  v087_cruisecp --> v082__0031
# LANG: cruisecp --> _0031
# full namespace: cruiserotor

# _0030_power_combination_eval_pv082__0031_pv087_cruisecp
temp_power = _0030_coeff_temp*1
pv082__0031_pv087_cruisecp = temp_power.flatten()
path_to_v087_cruisecp += DIAG_MULT(path_to_v082__0031,pv082__0031_pv087_cruisecp)

# op _0032_power_combination_eval
# REP:  v013_cruisen --> v084__0033
# LANG: cruisen --> _0033
# full namespace: cruiserotor

# _0032_power_combination_eval_pv084__0033_pv013_cruisen
temp_power = _0032_coeff_temp*2*(v013_cruisen)
pv084__0033_pv013_cruisen = temp_power.flatten()
path_to_v013_cruisen += DIAG_MULT(path_to_v084__0033,pv084__0033_pv013_cruisen)

# op _003u_power_combination_eval
# REP:  v073_density, v0102_liftcp --> v093__003v
# LANG: density, liftcp --> _003v
# full namespace: liftrotor

# _003u_power_combination_eval_pv093__003v_pv0102_liftcp
temp_power = _003u_coeff_temp*(v0102_liftcp)*1
pv093__003v_pv073_density = temp_power.flatten()
temp_power = _003u_coeff_temp*1*(v073_density)
pv093__003v_pv0102_liftcp = temp_power.flatten()
path_to_v073_density += DIAG_MULT(path_to_v093__003v,pv093__003v_pv073_density)
path_to_v0102_liftcp = DIAG_MULT(path_to_v093__003v,pv093__003v_pv0102_liftcp)

# op _003w_power_combination_eval
# REP:  v021_liftn --> v095__003x
# LANG: liftn --> _003x
# full namespace: liftrotor

# _003w_power_combination_eval_pv095__003x_pv021_liftn
temp_power = _003w_coeff_temp*3*(v021_liftn**2.0)
pv095__003x_pv021_liftn = temp_power.flatten()
path_to_v021_liftn = DIAG_MULT(path_to_v095__003x,pv095__003x_pv021_liftn)

# op _003C_power_combination_eval
# REP:  v0102_liftcp --> v097__003D
# LANG: liftcp --> _003D
# full namespace: liftrotor

# _003C_power_combination_eval_pv097__003D_pv0102_liftcp
temp_power = _003C_coeff_temp*1
pv097__003D_pv0102_liftcp = temp_power.flatten()
path_to_v0102_liftcp += DIAG_MULT(path_to_v097__003D,pv097__003D_pv0102_liftcp)

# op _003E_power_combination_eval
# REP:  v021_liftn --> v099__003F
# LANG: liftn --> _003F
# full namespace: liftrotor

# _003E_power_combination_eval_pv099__003F_pv021_liftn
temp_power = _003E_coeff_temp*2*(v021_liftn)
pv099__003F_pv021_liftn = temp_power.flatten()
path_to_v021_liftn += DIAG_MULT(path_to_v099__003F,pv099__003F_pv021_liftn)
path_to_v08_cruisevAxial = path_to_v087_cruisecp@pv087_cruisecp_pv08_cruisevAxial
path_to_v010_cruisevTan = path_to_v087_cruisecp@pv087_cruisecp_pv010_cruisevTan
path_to_v012__000u = DIAG_MULT(path_to_v013_cruisen,pv013_cruisen_pv012__000u)
path_to_v03_h = path_to_v073_density@pv073_density_pv03_h
path_to_v016_liftvAxial = path_to_v0102_liftcp@pv0102_liftcp_pv016_liftvAxial
path_to_v018_liftvTan = path_to_v0102_liftcp@pv0102_liftcp_pv018_liftvTan
path_to_v020__000N = DIAG_MULT(path_to_v021_liftn,pv021_liftn_pv020__000N)
path_to_v01_v = DIAG_MULT(path_to_v08_cruisevAxial,pv08_cruisevAxial_pv01_v)
path_to_v07__000m = DIAG_MULT(path_to_v08_cruisevAxial,pv08_cruisevAxial_pv07__000m)
path_to_v01_v += DIAG_MULT(path_to_v010_cruisevTan,pv010_cruisevTan_pv01_v)
path_to_v09__000q = DIAG_MULT(path_to_v010_cruisevTan,pv010_cruisevTan_pv09__000q)
path_to_v011_control_x += DIAG_MULT(path_to_v012__000u,pv012__000u_pv011_control_x)
path_to_v01_v += DIAG_MULT(path_to_v016_liftvAxial,pv016_liftvAxial_pv01_v)
path_to_v015__000F = DIAG_MULT(path_to_v016_liftvAxial,pv016_liftvAxial_pv015__000F)
path_to_v01_v += DIAG_MULT(path_to_v018_liftvTan,pv018_liftvTan_pv01_v)
path_to_v017__000J = DIAG_MULT(path_to_v018_liftvTan,pv018_liftvTan_pv017__000J)
path_to_v019_control_z += DIAG_MULT(path_to_v020__000N,pv020__000N_pv019_control_z)
path_to_v06_control_alpha = DIAG_MULT(path_to_v07__000m,pv07__000m_pv06_control_alpha)
path_to_v06_control_alpha += DIAG_MULT(path_to_v09__000q,pv09__000q_pv06_control_alpha)
path_to_v06_control_alpha += DIAG_MULT(path_to_v015__000F,pv015__000F_pv06_control_alpha)
path_to_v06_control_alpha += DIAG_MULT(path_to_v017__000J,pv017__000J_pv06_control_alpha)
dv060_de_dv01_v = path_to_v01_v.copy()
# dv060_de_dv02_gamma = zero
dv060_de_dv03_h = path_to_v03_h.copy()
# dv060_de_dv04_x = zero
# dv060_de_dv05_e = zero
dv060_de_dv06_control_alpha = path_to_v06_control_alpha.copy()
dv060_de_dv011_control_x = path_to_v011_control_x.copy()
dv060_de_dv019_control_z = path_to_v019_control_z.copy()