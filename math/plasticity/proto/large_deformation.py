#################### Calculate deformation gradient #############@###########
def calc_F(du_ij):
    
    delta_ij = [[0.0 for i in range(3)] for j in range(3)]
    delta_ij[0][0] = delta_ij[1][1] = delta_ij[2][2]

    FG = [[0. for ii in range(3)] for jj in range(3)]
    
### Fij = dxi/dXj = &ij + dui/dXj ###
    for i in range(3):
        for j in range(3):
            FG[i][j] = delta_ij[i][j] + du_ij[i][j]

    return FG
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
def dE_du_ij(delta_4,du_ij):

    dE_ddu = [[[[0. for i in range(3)] for j in range(3)] for k in range(3)] for l in range(3)] 

    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    dE_ddu[i][j][k][l] = 0.5*(delta_4[i][k][j][l] + delta_4[j][k][i][l])
                    for m in range(3):
                        dE_ddu[i][j][k][l] += 0.5*(delta_4[m][k][i][l]*du_ij[m][j] + du_ij[m][i]*delta_4[m][k][j][l])
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
def dS2PK_du_ij(cijkl,du_ij):
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
                            dS_ddu[i][j][k][l] += 0.5*cijkl[i][j][l][n]*delta_kron[p][k]*du_ij[p][n]
                    for m in range(3):
                        for p in range(3):
                            dS_ddu[i][j][k][l] += 0.5*cijkl[i][j][m][l]*delta_kron[p][k]*du_ij[p][m]

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




du_ij = [[0.0 for i in range(3)] for j in range(3)]

lamda1 = 1.2 ; lamda2 = 1.05
du_ij[0][0] = lamda1 - 1.0 ; du_ij[1][1] = lamda2 - 1.0 ; du_ij[2][2] = lamda2 - 1.0

delta_4 = delta_kron4()
FG = calc_F(du_ij)   # F at gausspoint.
E_lag = calc_E_lag(FG) # Euler-Lagrange strain
cijkl = cmat(1.0,0.5)  # Constitutive parameters
S = SPK_stress(cijkl,E_lag) # 2nd PK stress.
dS_ddu = dS2PK_du_ij(cijkl,du_ij) # 2nd PK derivatives.

N = dSP1PK_du_ij(delta_4,FG,S,dS_ddu) # 1st PK derviatives -- actual flux!

print N













