# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@ctcms.nist.gov. 

# Flux properties for the Mesh prototype code.


import math
import smallmatrix
import position

class FluxException:
    def __init__(self, message):
        self.message = message
    def __repr__(self):
        return "FluxException(%s)" % self.message

SmallMatrix = smallmatrix.SmallMatrix


class Orientation:
    def __init__(self, phi, theta, omega):
        self.rotation = self._euler_rot(phi,theta,omega)
    def _euler_rot(self,phi,theta,omega):
        # Cut and paste from where it is now...
        const_pi = math.acos(-1.0)
      
        phi = phi*const_pi/180.0
        theta = theta*const_pi/180.0
        omega = omega*const_pi/180.0
            
        sp = math.sin(phi)                      
        cp = math.cos(phi)                     
        st = math.sin(theta)                     
        ct = math.cos(theta)                    
        so = math.sin(omega)                    
        co = math.cos(omega)

        qrot = [[0.0 for i in range(3)] for j in range(3)]

        qrot[0][0] = co*cp-so*sp*ct
        qrot[1][0] = co*sp+so*ct*cp   
        qrot[2][0] = so*st   
        qrot[0][1] = -so*cp-sp*co*ct 
        qrot[1][1] = -so*sp+ct*co*cp
        qrot[2][1] = co*st
        qrot[0][2] = sp*st       
        qrot[1][2] = -st*cp       
        qrot[2][2] = ct

        return qrot

# A flux is a thing that has zero divergence in equilibrium.
# Components of the divergence of the flux at a given node correspond
# to Eqn objects.  Fluxes know what fields they depend on.
class Flux:
    def __init__(self, name, fieldname, dim):
        self.name = name
        self.fieldname = fieldname
        self.dim = dim
    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.name)
    

class CauchyStress(Flux):
    def __init__(self,name,lmbda=1.0,mu=0.5):
        Flux.__init__(self,name,"Displacement",9) # Dimensionality.
        self.cijkl = None
        self.global_cijkl = Cijkl(lmbda,mu)
    # For the Cauchy stress, derivative is very simple.
    def dukl(self,k,l,position,dofval,dofderivs):
        return [ [  0.5*(self.cijkl[i][j][k][l]+self.cijkl[i][j][l][k])
                    for j in range(3) ] for i in range(3) ]

    # Value is pretty simple too.
    def value(self,i,j,pos,dofval,dofderivs):
        return sum( sum( 0.5*self.cijkl[i][j][k][l]*
                         (dofderivs[k][l]+dofderivs[l][k])
                             for l in range(3)) for k in range(3))
    def rotate(self,qrot):
        C_mat = [[[[0.0 for i in range(3)] for j in range(3) ]
                  for k in range(3)] for l in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        # Whew...
                        for m in range(3):
                            for n in range(3):
                                for o in range(3):
                                    for p in range(3):
                                        C_mat[i][j][k][l] += qrot[i][m]*
                                        qrot[j][n]*qrot[k][o]*qrot[l][p]*
                                        self.global_cijkl[m][n][o][p]
        self.cijkl = C_mat
    



#######################################################################
# PK1 flux insertion here.
#######################################################################

class Pk1Stress(Flux):
    def __init__(self,name,lmbda=1.0,mu=0.5):
        Flux.__init__(self,name,"Displacement",9)
        self.cijkl = Cijkl(lmbda,mu)
        self.dukl_cache = {}
    # For the Cauchy stress, derivative is very simple.
    def dukl(self,k,l,position,dofval,dofderivs):
        cache_index = (position,)+tuple(dofval)+tuple([tuple(x) for
                                                       x in dofderivs])
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
            N = self.dSP1PK_du_ij(delta_4,FG,S,dS_ddu) # 1st PK derviatives
                                                       # -- actual flux!
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

        dS_ddu = [[[[0. for i in range(3)] for j in range(3)]
                   for k in range(3)] for l in range(3)] 


        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        dS_ddu[i][j][k][l] = 0.5*(self.cijkl[i][j][k][l]
                                                  + self.cijkl[i][j][l][k])
                        for n in range(3):
                            dS_ddu[i][j][k][l] += 0.5*\
                                                  self.cijkl[i][j][l][n]*\
                                                  du_ij[k][n]
                        for m in range(3):
                            dS_ddu[i][j][k][l] += 0.5*\
                                                  self.cijkl[i][j][m][l]*\
                                                  du_ij[k][m]

        return dS_ddu

######################### Forth order Kronecker Delta ##########################
    def delta_kron4(self):
        delta_kron = [[0. for ii in range(3)] for jj in range(3)]
        delta_kron[0][0] = delta_kron[1][1]= delta_kron[2][2] = 1.0

        delta_kron4d = [[[[0. for i in range(3)] for j in range(3)]
                         for k in range(3)] for l in range(3)] 

        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        delta_kron4d[i][j][k][l] = \
                                                   delta_kron[i][k]*\
                                                   delta_kron[j][l]


        return delta_kron4d
####################### End of Forth order Kronecker Delta #####################

###### drivative of 1PK stress to gradient of displacement #########
    def dSP1PK_du_ij(self,delta_4,FG,S,dS_ddu):
        delta_kron = [[0. for ii in range(3)] for jj in range(3)]
        delta_kron[0][0] = delta_kron[1][1]= delta_kron[2][2] = 1.0

        dP_ddu = [[[[0. for i in range(3)] for j in range(3)]
                   for k in range(3)] for l in range(3)] 
        TMP = [[[[0. for i in range(3)] for j in range(3)]
                for k in range(3)] for l in range(3)] 


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

                 


######################################################################
# PK1 insertion ends here.
######################################################################


class RambergOsgood(Flux):
    # Ramberg-Osgood defines the strain as an analytic function of the
    # stress, which is not in general invertible.
    def __init__(self,name,lmbda=1.0,mu=0.5,alpha=1.0,s0=0.1,n=7):
        Flux.__init__(self,name,"Displacement", 9) # Dimensionality.
        cij = Cij(lmbda,mu)
        c11 = cij[0][0]
        c12 = cij[0][1]
        self.A = 1.0/(c11-c12)
        self.B = c12/((c11-c12)*(c11+2.0*c12))
        self.alpha = alpha # Amplitude.
        self.s0 = s0       # Reference stress.
        self.n = n         # Exponent.
        self.tol = 1.0e-8  # Tolerance for the NR inversion.
        #
        self.clear_caches()
    def clear_caches(self):
        self.dukl_cache = {}
        self.stress_cache = {}
    def _residual(self,stress,strain):
        # Zero when stress and strain are on the RO curve.
        # Stress and strain are 3x3 Python arrays
        sijsij = sum( sum( stress[i][j]**2 for j in range(3) )
                      for i in range(3) )
        tr = sum( stress[i][i] for i in range(3) )
        q = math.sqrt((3.0/2.0)*(sijsij-tr*tr/3.0))
        ro = (3.0*self.alpha/2.0)*((q/self.s0)**(self.n-1))
        res = [ [ (self.A+ro)*stress[i][j]-strain[i][j]
                  for j in range(3) ] for i in range(3) ]
        for i in range(3):
            res[i][i] -= (self.B+(ro/3.0))*tr
        return res
    def _derivs_wrt_stress(self,stress,strain):
        # Matrix of derivatives of the residual wrt *stress*
        # components. Result is a four-index object.
        tr = sum(stress[i][i] for i in range(3))
        #
        dvtr = [ [ x for x in row ] for row in stress ]
        dvtr[0][0]-=tr/3.0
        dvtr[1][1]-=tr/3.0
        dvtr[2][2]-=tr/3.0
        #
        sijsij = sum(sum( x*x for x in row) for row in stress)
        v = (3.0/2.0)*(sijsij-tr*tr/3.0)
        q = math.sqrt(v)
        #
        dvds = [ [ 3.0*x for x in row ] for row in stress]
        dvds[0][0]-=tr
        dvds[1][1]-=tr
        dvds[2][2]-=tr
        #
        if v > 0.0:
            dqds = [[ (0.5/math.sqrt(v))*x for x in row] for row in dvds]
        else:
            dqds = [ [ 0.0 ]*3 ] *3 # Never written to, this is safe.
        #
        ro=(3.0*self.alpha/2.0)*((q/self.s0)**(self.n-1))
        #
        res = [ [ [ [ (3.0/2.0)*self.alpha*dvtr[i][j]*(self.n-1.0)*
                       (1.0/(self.s0**(self.n-1)))*(q**(self.n-2))*dqds[k][l]
                       for l in range(3) ] for k in range(3) ]
                    for j in range(3) ] for i in range(3) ]
        for i in range(3):
            for k in range(3):
                res[i][k][i][k] += self.A+ro
                res[i][i][k][k] -= self.B+ro/3.0
        return res
    def _stress(self,strain):
        cache_index = tuple( [ tuple(x) for x in strain ] )
        try:
            return self.stress_cache[cache_index]
        except KeyError:
            # Start with a copy of the strain. Be smarter later on.
            wrk = [ [ x for x in row ] for row in strain ]
            inc = 1.0
            count = 0 
            while inc > self.tol:
                resid = self._residual(wrk,strain)
                dfijdskl = self._derivs_wrt_stress(wrk,strain)
                rmtx = smallmatrix.SmallMatrix(9,1)
                dfmtx = smallmatrix.SmallMatrix(9,9)
                rmtx.clear()
                dfmtx.clear()
                for i in range(3):
                    for j in range(3):
                        rmtx[i+j*3,0] = -resid[i][j]
                        for k in range(3):
                            for l in range(3):
                                dfmtx[i*3+j,k*3+l]=dfijdskl[i][j][k][l]
                rr = dfmtx.solve(rmtx)
                if rr==0:
                    inc = 0.0
                    for i in range(3):
                        for j in range(3):
                            dlta = rmtx[i*3+j,0]
                            wrk[i][j]+=dlta
                            inc+=dlta*dlta
                else:
                    raise FluxException("Matrix failure in RO flux.")
                count += 1
                # print "Iteration %d, increment is %f." % (count,inc)
                if count>100:
                    raise FluxException("Debug overflow in RO stress.")
            self.stress_cache[cache_index] = wrk
            return wrk

    #
    # TODO: These are going to be slow. Use caches and cleverness to
    # fix them later on.
    def dukl(self,k,l,pos,dofval,dofderivs):
        cache_index = tuple( [ tuple(x) for x in dofderivs ] )
        try:
            dsijdukl = self.dukl_cache[cache_index]
        except KeyError:
            strain = [ [ 0.5*(dofderivs[i][j]+dofderivs[j][i])
                         for j in range(3) ]
                       for i in range(3) ] 
            stress = self._stress(strain)
            deijdskl = self._derivs_wrt_stress(stress,strain)
            deds = smallmatrix.SmallMatrix(9,9)
            deds.clear()
            for ix in range(3):
                for jx in range(3):
                    for kx in range(3):
                        for lx in range(3):
                            deds[ix*3+jx,kx*3+lx] = deijdskl[ix][jx][kx][lx]
            dsde = smallmatrix.SmallMatrix(9,9)
            dsde.clear()
            for i in range(9):
                dsde[i,i]=1.0
            rr = deds.solve(dsde) # Invert
            if rr==0:
                # Convert from strain to dofs here.
                dsijdukl = [ [ [ [ 0.5*(dsde[ix*3+jx,kx*3+lx]+
                                        dsde[ix*3+jx,lx*3+kx])
                                   for lx in range(3) ]
                                 for kx in range(3) ]
                               for jx in range(3) ]
                             for ix in range(3) ]
                self.dukl_cache[cache_index] = dsijdukl
            else:
                raise FluxException("Matrix exception in Ramberg-Osgood dukl.")
        # At this point, dsijdukl is a valid four-index object.
        return [ [ dsijdukl[ix][jx][k][l] for jx in range(3) ]
                 for ix in range(3) ]
            
    def value(self,i,j,pos,dofval,dofderivs):
        strain = [ [ 0.5*(dofderivs[ix][jx]+dofderivs[jx][ix])
                     for jx in range(3) ]
                   for ix in range(3) ]
        stress = self._stress(strain)
        return stress[i][j]
    
# Elastic constitutive bookkeeppiinngg, necessary for fluxes.


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

          
