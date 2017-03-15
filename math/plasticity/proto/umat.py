import math
    
#--------------------------------------------------------------------
def umat(element,gausspt,Dep,CaStress,cijkl,Fe):
    
##    XYZ = [[0.0 for i in range(3)] for j in range(8)]
##    xyz = [[0.0 for i in range(3)] for j in range(8)]
##
##    for (rrndx,rrn) in enumerate(element.nodes):
##        XYZ[rrndx][0] = rrn.position.x
##        XYZ[rrndx][1] = rrn.position.y
##        XYZ[rrndx][2] = rrn.position.z
##
##        xyz[rrndx][0] = rrn.position.x + rrn.fields[0].value[0]
##        xyz[rrndx][1] = rrn.position.y + rrn.fields[0].value[1]
##        xyz[rrndx][2] = rrn.position.z + rrn.fields[0].value[2]
##
##    SHP = element.dshapefnRef(gausspt.xi,gausspt.zeta,gausspt.mu)
##    
##    FG = calc_F(xyz,SHP)            # F at gausspoint
    FG = Fe
    E_lag = calc_E_lag(FG)            # Euler-Lagrange strain
    S = SPK_stress(E_lag,cijkl)             # 2nd PK stress
    
    Cauchy = Chuchy_stress(S,FG)      # Cauchy stress
    N = cijkl 

    for i in range(3):
        for j in range(3):
            CaStress[i][j] = Cauchy[i][j]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    Dep[i][j][k][l] = cijkl[i][j][k][l]

##def calc_F(cord,SHP):
##
##    dxt_dx0 = 0.0 ; dxt_dy0 = 0.0 ; dxt_dz0 = 0.0
##    dyt_dx0 = 0.0 ; dyt_dy0 = 0.0 ; dyt_dz0 = 0.0
##    dzt_dx0 = 0.0 ; dzt_dy0 = 0.0 ; dzt_dz0 = 0.0
##    for i in range(8):
##        dxt_dx0 += SHP[i][0]*cord[i][0]
##        dxt_dy0 += SHP[i][1]*cord[i][0]
##        dxt_dz0 += SHP[i][2]*cord[i][0]
##        
##        dyt_dx0 += SHP[i][0]*cord[i][1]
##        dyt_dy0 += SHP[i][1]*cord[i][1]
##        dyt_dz0 += SHP[i][2]*cord[i][1]
##
##        dzt_dx0 += SHP[i][0]*cord[i][2]
##        dzt_dy0 += SHP[i][1]*cord[i][2]
##        dzt_dz0 += SHP[i][2]*cord[i][2]
## 
##    FG = [[0. for ii in range(3)] for jj in range(3)]
##    FG[0][0] = dxt_dx0 ; FG[0][1] = dxt_dy0 ; FG[0][2] = dxt_dz0
##    FG[1][0] = dyt_dx0 ; FG[1][1] = dyt_dy0 ; FG[1][2] = dyt_dz0
##    FG[2][0] = dzt_dx0 ; FG[2][1] = dzt_dy0 ; FG[2][2] = dzt_dz0
##
##    return FG
#################### End of calculation of deformation gradient #############

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
def SPK_stress(E_lag,cijkl):
    
    S = [[0. for ii in range(3)] for jj in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
#                       S[i][j] += Cijkl_rot[i][j][k][l]*E_lag[k][l]
                    S[i][j] += cijkl[i][j][k][l]*E_lag[k][l]

    return S
################### End of Calculation the 2PK stress #########################

####################### Calculate the Chuchy stress  ############################

def Chuchy_stress(S_2PK,Fe):

    TPMc = [[0.0 for i in range(3)] for j in range(3)]                

    FeT = zip(*Fe)

    for i in range(3):
        for j in range(3):
            for k in range(3):
                TPMc[i][j] += S_2PK[i][k]*FeT[k][j]
                                                 
    Cauchy = [[0.0 for i in range(3)] for j in range(3)]
                                        
    for i in range(3):
        for j in range(3):
            for k in range(3):
                Cauchy[i][j] += Fe[i][k]*TPMc[k][j]

    det_F_e=(Fe[0][0]*Fe[1][1]*Fe[2][2]\
            -Fe[0][0]*Fe[1][2]*Fe[2][1]-Fe[1][0]*Fe[0][1]*Fe[2][2]\
             +Fe[1][0]*Fe[0][2]*Fe[2][1]+Fe[2][0]*Fe[0][1]*Fe[1][2]\
             -Fe[2][0]*Fe[0][2]*Fe[1][1])
                                                 
    for i in range(3):
        for j in range(3):
            Cauchy[i][j] = Cauchy[i][j]/det_F_e

    return Cauchy
    
    
################### End of Calculation the Chuchy stress #########################

###### drivative of 2PK stress to gradient of displacement #########
def dS2PK_du_ij(self,du_ij):
    delta_kron = [[0. for ii in range(3)] for jj in range(3)]
    delta_kron[0][0] = delta_kron[1][1]= delta_kron[2][2] = 1.0

    dS_ddu = [[[[0. for i in range(3)] for j in range(3)] for k in range(3)] for l in range(3)] 


    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    dS_ddu[i][j][k][l] = 0.5*(self.cijkl[i][j][k][l] + self.cijkl[i][j][l][k])
                    for n in range(3):
                        dS_ddu[i][j][k][l] += 0.5*self.cijkl[i][j][l][n]*du_ij[k][n]
                    for m in range(3):
                        dS_ddu[i][j][k][l] += 0.5*self.cijkl[i][j][m][l]*du_ij[k][m]


    return dS_ddu

######################### Forth order Kronecker Delta ##########################
def delta_kron4(self):
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

###### drivative of 1PK stress to gradient of displacement #########
def dSP1PK_du_ij(self,delta_4,FG,S,dS_ddu):
    delta_kron = [[0. for ii in range(3)] for jj in range(3)]
    delta_kron[0][0] = delta_kron[1][1]= delta_kron[2][2] = 1.0

    dP_ddu = [[[[0. for i in range(3)] for j in range(3)] for k in range(3)] for l in range(3)] 
    TMP = [[[[0. for i in range(3)] for j in range(3)] for k in range(3)] for l in range(3)] 


    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    dP_ddu[i][j][k][l] = delta_kron[i][k]*S[l][j]

                    
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    for m in range(3):
                        dP_ddu[i][j][k][l] += FG[i][m]*dS_ddu[m][j][k][l]
                    
                        

    return dP_ddu


#### End of drivative of 1PK stress to gradient of displacement ######




            

####################### Calculate the 1PK stress  ############################
def FPK_stress(FG,S):
    
    P = [[0. for ii in range(3)] for jj in range(3)]
                
    for i in range(3):
        for j in range(3):
            for k in range(3):
                P[i][j] += FG[i][k]*S[k][j]

    return P
################### End of Calculation the 1PK stress #########################


