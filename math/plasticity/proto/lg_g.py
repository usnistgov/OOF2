import math


##### Get global shape functions and their derivatives at a given gauss point#####
############################ N_i(X,t) and gradN_i(X,t) ###########################
def SHP3D(ss,tt,zz,XL=[[]]):
    si = [-1,1,1,-1,-1,1,1,-1]
    ti = [-1,-1,1,1,-1,-1,1,1]
    zi = [-1,-1,-1,-1,1,1,1,1]
    SHPL = [[0. for ii in range(8)] for jj in range(4)]
#----------- Local shape functions with derivatives with repect to si,ti and zi
    for i in range(8):
    	N1 = 1.0+ss*si[i]
        N2 = 1.0+tt*ti[i]
        N3 = 1.0+zz*zi[i]
        SHPL[3][i] = N1*N2*N3/8.0
        SHPL[0][i] = si[i]*N2*N3/8.0
        SHPL[1][i] = ti[i]*N1*N3/8.0
        SHPL[2][i] = zi[i]*N1*N2/8.0
#--------- Get global values in refrence configuration


    XS = [[0. for ii in range(3)] for jj in range(3)]
    SX = [[0. for ii in range(3)] for jj in range(3)]
 

    for i in range(3):
        for j in range(3):
            for k in range(8):
            	XS[i][j] += SHPL[i][k]*XL[k][j]

    SXD = matinv3(XS)
    SX = SXD[0] ; xsJ = SXD[1]
    
    SHPG = [[0. for ii in range(8)] for jj in range(3)]
    for i in range(8):
        T0 = SX[0][0]*SHPL[0][i]+SX[0][1]*SHPL[1][i]+SX[0][2]*SHPL[2][i]
        T1 = SX[1][0]*SHPL[0][i]+SX[1][1]*SHPL[1][i]+SX[1][2]*SHPL[2][i]
        T2 = SX[2][0]*SHPL[0][i]+SX[2][1]*SHPL[1][i]+SX[2][2]*SHPL[2][i]
        SHPG[0][i] = T0
        SHPG[1][i] = T1
        SHPG[2][i] = T2
                
    return SHPG
############### End of calculation of shape functions and drivatives ##################
################# inverse 3by3 matrix ######################
def matinv3(a):
    a_inv = [[0.0 for i in range(3)] for j in range(3)]
    
    det = a[0][0]*a[1][1]*a[2][2]-a[0][0]*a[1][2]*a[2][1]-a[1][0]*a[0][1]\
              *a[2][2]+a[1][0]*a[0][2]*a[2][1]+a[2][0]*a[0][1]*a[1][2]-a[2][0]\
              *a[0][2]*a[1][1]
    
    a_inv[0][0] =  ( a[1][1]*a[2][2]-a[1][2]*a[2][1])/det
    a_inv[0][1] = -( a[0][1]*a[2][2]-a[0][2]*a[2][1])/det
    a_inv[0][2] = -(-a[0][1]*a[1][2]+a[0][2]*a[1][1])/det
    a_inv[1][0] = -( a[1][0]*a[2][2]-a[1][2]*a[2][0])/det
    a_inv[1][1] =  ( a[0][0]*a[2][2]-a[0][2]*a[2][0])/det
    a_inv[1][2] = -( a[0][0]*a[1][2]-a[0][2]*a[1][0])/det
    a_inv[2][0] =  ( a[1][0]*a[2][1]-a[1][1]*a[2][0])/det
    a_inv[2][1] = -( a[0][0]*a[2][1]-a[0][1]*a[2][0])/det
    a_inv[2][2] =  ( a[0][0]*a[1][1]-a[0][1]*a[1][0])/det
      
    return a_inv,det

################# end of inverse 3by3 matrix ######################
########## Loading gauss points for 8 integration points per element ############
def pgauss():
    g = 1.0/math.sqrt(3.0)
    ls = [-1,1,1,-1,-1,1,1,-1]
    lt = [-1,-1,1,1,-1,-1,1,1]
    lz = [-1,-1,-1,-1,1,1,1,1]
    sg = [] ; tg = [] ; zg = [] ; wg = [] 
    for i in range(8):
        s = g*ls[i] ; sg.append(s)
        t = g*lt[i] ; tg.append(t)
        z = g*lz[i] ; zg.append(z)
        w = 1.0     ; wg.append(w)
    return sg,tg,zg,wg
##################### End of loading gauss points ################################

########### Calculate deformation gradient (dx/dX=sum(x*gradN_i(X,t))) ################
def calc_F(cord,SHP):
    
    dxt_dx0 = 0.0 ; dxt_dy0 = 0.0 ; dxt_dz0 = 0.0
    dyt_dx0 = 0.0 ; dyt_dy0 = 0.0 ; dyt_dz0 = 0.0
    dzt_dx0 = 0.0 ; dzt_dy0 = 0.0 ; dzt_dz0 = 0.0

    for i in range(8):
	dxt_dx0 += SHP[0][i]*cord[i][0]
	dxt_dy0 += SHP[1][i]*cord[i][0]
	dxt_dz0 += SHP[2][i]*cord[i][0]
	
	dyt_dx0 += SHP[0][i]*cord[i][1]
	dyt_dy0 += SHP[1][i]*cord[i][1]
	dyt_dz0 += SHP[2][i]*cord[i][1]

	dzt_dx0 += SHP[0][i]*cord[i][2]
	dzt_dy0 += SHP[1][i]*cord[i][2]
	dzt_dz0 += SHP[2][i]*cord[i][2]
 
    FG = [[0. for ii in range(3)] for jj in range(3)]
    FG[0][0] = dxt_dx0 ; FG[0][1] = dxt_dy0 ; FG[0][2] = dxt_dz0
    FG[1][0] = dyt_dx0 ; FG[1][1] = dyt_dy0 ; FG[1][2] = dyt_dz0
    FG[2][0] = dzt_dx0 ; FG[2][1] = dzt_dy0 ; FG[2][2] = dzt_dz0


    return FG
#################### End of calculation of deformation gradient ###################


###################### calculation of Lagrangian strain #####################
def calc_E_lag(Fe):
    
    Iden = [[0. for i in range(3)] for j in range(3)]
    Iden[0][0] = Iden[1][1] = Iden[2][2] = 1.0

    C = [[0. for i in range(3)] for j in range(3)]
    E_lag = [[0. for i in range(3)] for j in range(3)]

    FeT = zip(*Fe)
## C: right Cauchy-Green deformation tensor ###########
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i][j] += FeT[i][k]*Fe[k][j]
#### Lagrangian strain tensor E=0.5(C-I)############               
    for i in range(3):
        for j in range(3):
            E_lag[i][j] = 0.5*(C[i][j]-Iden[i][j])

    return E_lag
#################### End of calculation of Lagrangian strain #################

####################### Calculate the 2PK stress  ############################
def SPK_stress(cijkl,E_lag):
    
    delta_kron = [[0. for ii in range(3)] for jj in range(3)]
    S = [[0. for ii in range(3)] for jj in range(3)]
    
    delta_kron[0][0] = delta_kron[1][1]= delta_kron[2][2] = 1.0
	
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    S[i][j] += cijkl[i][j][k][l]*E_lag[k][l]

    return S
################### End of Calculation the 2PK stress #########################


######################### Forth order Kronecker Delta ##########################
def delta_kron4():
    delta_kron = [[0. for ii in range(3)] for jj in range(3)]
    delta_kron[0][0] = delta_kron[1][1]= delta_kron[2][2] = 1.0

    delta_kron4d = [[[[0. for i in range(3)] for j in range(3)] for k in range(3)] for l in range(3)] 

    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    delta_kron4d[i][j][k][l] = delta_kron[i][k]*delta_kron[j][l]

    return delta_kron4d
####################### End of Forth order Kronecker Delta #####################


####### drivative of green-lagrange strain to gradient of displacement #########
def dE_du_ij(delta_4,UG):

    dE_ddu = [[[[0. for i in range(3)] for j in range(3)] for k in range(3)] for l in range(3)] 

    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    dE_ddu[i][j][k][l] = 0.5*(delta_4[i][k][j][l] + delta_4[j][k][i][l])
                    for m in range(3):
                        dE_ddu[i][j][k][l] += 0.5*(delta_4[m][k][i][l]*UG[m][j] + UG[m][i]*delta_4[m][k][j][l])
    return dE_ddu
#### End of drivative of green-lagrange strain to gradient of displacement ######
def cmat(c11,c12):

    cij = [[0. for i in range(6)] for j in range(6)] 

    c44 = 0.5*(c11-c12)
#---------------- cij for cubic materials 
    cij[0][0] = cij[1][1] = cij[2][2] = c11
    cij[0][1] = cij[0][2] = cij[1][0] = cij[1][2] = cij[2][0] = cij[2][1] = c12
    cij[3][3] = cij[4][4] = cij[5][5] = c44
        


    cijkl = [[[[0. for i in range(3)] for j in range(3)] for k in range(3)] for l in range(3)] 

#----------------- Get cijkl  
    for i in range(3):
        for j in range(3):
            cijkl[i][i][j][j] = cij[i][j]

    for i in range(3):
        cijkl[i][i][0][1] = cij[i][3]
        cijkl[i][i][1][0] = cij[i][3]
        cijkl[i][i][1][2] = cij[i][4]
        cijkl[i][i][2][1] = cij[i][4]
        cijkl[i][i][0][2] = cij[i][5]
        cijkl[i][i][2][0] = cij[i][5]
        
        cijkl[0][1][i][i] = cijkl[1][0][i][i] = cij[3][i]
        cijkl[1][2][i][i] = cijkl[2][1][i][i] = cij[4][i]
        cijkl[0][2][i][i] = cijkl[2][0][i][i] = cij[5][i]
    
    cijkl[0][1][0][1] = cijkl[0][1][1][0] = cijkl[1][0][0][1] = cijkl[1][0][1][0] = cij[3][3]
    cijkl[0][1][1][2] = cijkl[0][1][2][1] = cijkl[1][0][1][2] = cijkl[1][0][2][1] = cij[3][4]
    cijkl[0][1][0][2] = cijkl[0][1][2][0] = cijkl[1][0][0][2] = cijkl[1][0][2][0] = cij[3][5]
    cijkl[1][2][0][1] = cijkl[1][2][1][0] = cijkl[2][1][0][1] = cijkl[2][1][1][0] = cij[4][3]
    cijkl[1][2][1][2] = cijkl[1][2][2][1] = cijkl[2][1][1][2] = cijkl[2][1][2][1] = cij[4][4]
    cijkl[1][2][0][2] = cijkl[1][2][2][0] = cijkl[2][1][0][2] = cijkl[2][1][2][0] = cij[4][5]
    cijkl[0][2][0][1] = cijkl[0][2][1][0] = cijkl[2][0][0][1] = cijkl[2][0][1][0] = cij[5][3]
    cijkl[0][2][1][2] = cijkl[0][2][2][1] = cijkl[2][0][1][2] = cijkl[2][0][2][1] = cij[5][4]
    cijkl[0][2][0][2] = cijkl[0][2][2][0] = cijkl[2][0][0][2] = cijkl[2][0][2][0] = cij[5][5]

    return cijkl


###### drivative of 2PK stress to gradient of displacement #########
def dS2PK_du_ij(cijkl,UG):
    delta_kron = [[0. for ii in range(3)] for jj in range(3)]
    delta_kron[0][0] = delta_kron[1][1]= delta_kron[2][2] = 1.0

    dS_ddu = [[[[0. for i in range(3)] for j in range(3)] for k in range(3)] for l in range(3)] 


    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    dS_ddu[i][j][k][l] = 0.5*(cijkl[i][j][k][l] + cijkl[i][j][l][k])
                    for n in range(3):
                        for p in range(3):
                            dS_ddu[i][j][k][l] += 0.5*cijkl[i][j][l][n]*delta_kron[p][k]*UG[p][n]
                    for m in range(3):
                        for p in range(3):
                            dS_ddu[i][j][k][l] += 0.5*cijkl[i][j][m][l]*delta_kron[p][k]*UG[p][m]

    return dS_ddu
    
#### End of drivative of 2PK stress to gradient of displacement ######


###### drivative of 1PK stress to gradient of displacement #########
def dSP1PK_du_ij(delta_4,FG,S,dS_ddu):

    dP_ddu = [[[[0. for i in range(3)] for j in range(3)] for k in range(3)] for l in range(3)] 

    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    for m in range(3):
                        dP_ddu[i][j][k][l] += delta_4[i][m][k][l]*S[m][j]

                    
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    for m in range(3):
                        dP_ddu[i][j][k][l] += FG[i][m]*dS_ddu[m][j][k][l]

    return dP_ddu
    

#### End of drivative of 1PK stress to gradient of displacement ######

XYZ = [[0.0 for i in range(3)] for j in range(8)]
xyz = [[0.0 for i in range(3)] for j in range(8)]
du_ij = [[0.0 for i in range(3)] for j in range(8)]

# unit cube coordinates
XYZ[1][0] = 1.0
XYZ[2][0] = 1.0 ; XYZ[2][1] = 1.0
XYZ[3][1] = 1.0
XYZ[4][2] = 1.0
XYZ[5][0] = 1.0 ; XYZ[5][2] = 1.0
XYZ[6][0] = 1.0 ; XYZ[6][1] = 1.0 ; XYZ[6][2] = 1.0
XYZ[7][1] = 1.0 ; XYZ[7][2] = 1.0

# tension in x-direction
du_ij[1][0] = du_ij[2][0] = du_ij[5][0] = du_ij[6][0] = 0.2

for i in range(8):
    for j in range(3):
        xyz[i][j] = XYZ[i][j] + du_ij[i][j]
gaussw = pgauss()


ngauss = 8

for ig in range(ngauss):
    
    SHP = SHP3D(gaussw[0][ig],gaussw[1][ig],gaussw[2][ig],XYZ)
    FG = calc_F(xyz,SHP)

    delta_4 = delta_kron4()

    E_lag = calc_E_lag(FG)
    cijkl = cmat(1.0,0.5)
    S = SPK_stress(cijkl,E_lag)
    
    UG = calc_F(du_ij,SHP)


    dS_ddu = dS2PK_du_ij(cijkl,UG)


    N = dSP1PK_du_ij(delta_4,FG,S,dS_ddu)

    print N
    raw_input()
