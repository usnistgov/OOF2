# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@ctcms.nist.gov. 

# File which isolates and tests the 1PK stress class.


import position,smallmatrix

class Oops:
    def __init__(self, message):
        self.message = message
    def __repr__(self):
        return "Oops(%s)" % self.message

Position = position.Position
SmallMatrix = smallmatrix.SmallMatrix




# A flux is a thing that has zero divergence in equilibrium.
# Components of the divergence of the flux at a given node correspond
# to Eqn objects.  Fluxes know what fields they depend on.
class Flux:
    def __init__(self, name, fieldname):
        self.name = name
        self.fieldname = fieldname
    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.name)
    

class Pk1Stress(Flux):
    def __init__(self,name,lmbda=1.0,mu=0.5):
        Flux.__init__(self,name,"Displacement")
        self.cijkl = Cijkl(lmbda,mu)
        self.dukl_cache = {}
    # For the Cauchy stress, derivative is very simple.
    def dukl(self,k,l,position,dofval,dofderivs):
        cache_index = (position,)+tuple(dofval)+tuple([tuple(x) for x in dofderivs])
        try:
            N = self.dukl_cache[cache_index]
            TMP = [[0.0 for ii in range(3)] for jj in range(3) ]
            for i in range(3):
                for j in range(3):
                    TMP[i][j] = N[i][j][k][l]
            return TMP
        except KeyError:
            FG = self.calc_F(dofderivs)            # F at gausspoint
            E_lag = self.calc_E_lag(FG)            # Euler-Lagrange strain
            S = self.SPK_stress(E_lag)             # 2nd PK stress
            dS_ddu = self.dS2PK_du_ij(dofderivs)      # 2nd PK derivatives.
            delta_4 = self.delta_kron4()
            N = self.dSP1PK_du_ij(delta_4,FG,S,dS_ddu) # 1st PK derviatives -- actual flux!
            self.dukl_cache[cache_index] = N
            TMP = [[0.0 for ii in range(3)] for jj in range(3)]
            for i in range(3):
                for j in range(3):
                    TMP[i][j] = N[i][j][k][l]
        
            return TMP
                
#        return [ [  0.5*(self.cijkl[i][j][k][l]+self.cijkl[i][j][l][k])
#                    for j in range(3) ] for i in range(3) ]
#################### Calculate deformation gradient #############@###########
    def calc_F(self,du_ij):
    
        delta_ij = [[0.0 for i in range(3)] for j in range(3)]
        delta_ij[0][0] = delta_ij[1][1] = delta_ij[2][2] = 1.0

        FG = [[0. for ii in range(3)] for jj in range(3)]
    
### Fij = dxi/dXj = &ij + dui/dXj ###
        for i in range(3):
            for j in range(3):
                FG[i][j] = delta_ij[i][j] + du_ij[i][j]

        return FG
#################### End of calculation of deformation gradient #############

###################### calculation of Lagrangian strain #####################
    def calc_E_lag(self,Fe):
        
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
    def SPK_stress(self,E_lag):
        
        S = [[0. for ii in range(3)] for jj in range(3)]
                    
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        S[i][j] += self.cijkl[i][j][k][l]*E_lag[k][l]

        return S
################### End of Calculation the 2PK stress #########################

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




    # Value is pretty simple too.    
    def value(self,i,j,pos,dofval,dofderivs):

        FG = self.calc_F(dofderivs)            # F at gausspoint
        E_lag = self.calc_E_lag(FG)            # Euler-Lagrange strain
        S = self.SPK_stress(E_lag)             # 2nd PK stress
        P = self.FPK_stress(FG,S)             # 1st PK stress

        return P[j][i]
                
#        return sum( sum( 0.5*self.cijkl[i][j][k][l]*
#                         (dofderivs[k][l]+dofderivs[l][k])
#                             for l in range(3)) for k in range(3))

####################### Calculate the 1PK stress  ############################
    def FPK_stress(self,FG,S):
        
        P = [[0. for ii in range(3)] for jj in range(3)]
                    
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    P[i][j] += FG[i][k]*S[k][j]

        return P
################### End of Calculation the 1PK stress #########################

                 
# Elastic constitutive bookkeeppiinngg.


voigt = [[0,5,4],
         [5,1,3],
         [4,3,2]]


def Cij(lmbda,mu):
    # Canonical: lmbda=0.5, mu=0.25, gives c11=1.0,c12=0.5.
    c11 = lmbda + 2.0*mu
    c12 = lmbda
    c44 = 0.5*(c11-c12)
    return [[c11, c12, c12, 0.0, 0.0, 0.0],
            [c12, c11, c12, 0.0, 0.0, 0.0],
            [c12, c12, c11, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, c44, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, c44, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, c44]]


def Cijkl(lmbda,mu):
    cij = Cij(lmbda,mu)
    return [ [ [ [ cij[voigt[i][j]][voigt[k][l]] for l in range(3) ]
                  for k in range(3) ] for j in range(3) ] for i in range(3) ]



if __name__=="__main__":
    # DOFs are displacements, everything is 3D.
    # Dofderivs are [ [du1/dx1,du1/dx2,du1/dx3],[du2/dx1,...] ], basically F.

    # Model strain -- simple shear in x-y plane.
    dofderivs = [ [ 0.0, 0.1, 0.0 ],
                  [ 0.1, 0.0, 0.0 ],
                  [ 0.0, 0.0, 0.0 ] ]
    
    pk1 = Pk1Stress("test")

    print pk1.value(0,0,None,None,dofderivs)

    print pk1.dukl(0,0,None,[None],dofderivs)
