# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@ctcms.nist.gov. 


# Prototype code for playing with plastic constitutive rules.  Has a
# local, custom-constructed mesh of fixed geometry, and various other
# cheats which bypass the full generality of OOF, with the idea of
# focussing on the plasticity part.


import math, sys, getopt
import matplotlib.pyplot as plt
#from pylab import *
import smallmatrix
import position

import flux
from flux import CauchyStress

class Oops:
    def __init__(self, message):
        self.message = message
    def __repr__(self):
        return "Oops(%s)" % self.message

Position = position.Position
SmallMatrix = smallmatrix.SmallMatrix

class Node:
    def __init__(self,idx,pos):
        self.index = idx
        self.position = pos
        self.dofs = []
        self.eqns = []
        self.elements = set()

    def __repr__(self):
        return "Node(%d,%f,%f,%f)" % (self.index,
                                      self.position.x,
                                      self.position.y,
                                      self.position.z)
    def add_element(self, el):
        self.elements.add(el)

    def get_elements(self):
        return self.elements

    def alldofs(self):
        return self.dofs[:]

    def adddof(self,dof):
        self.dofs.append(dof)

    def addeqn(self,eqn):
        self.eqns.append(eqn)

    # Returns the *mesh* index of this DOF.
    def dofindex(self,dofname):
        for d in self.dofs:
            if d.name==dofname:
                return d.index

    def dof(self,dofname):
        for d in self.dofs:
            if d.name==dofname:
                return d

    def eqn(self,eqnname):
        for e in self.eqns:
            if e.name==eqnname:
                return e

# This is a combination of the field and dof functionality in OOF.
# The index is the starting index for this DOF in the master stiffness
# matrix, and the size is the number of slots it uses.
class Dof:
    def __init__(self, name, index, size):
        self.name = name
        self.index = index
        self.size = size
        self.value = [0.0]*size
    def set(self,idx,v):
        self.value[idx] = v
    def add(self,idx,v):
        self.value[idx] += v

    def get(self,idx):
        return self.value[idx]
    def __repr__(self):
        return "Dof(%s,%d,%d)" % (self.name, self.index, self.size)

# Equation object.  Indexing as for Dofs.  Indexing is really all it
# does.
class Eqn:
    def __init__(self, name, index, size, flux):
        self.name = name
        self.index = index
        self.size = size
        self.flux = flux
    def __repr__(self):
        return "Eqn(%s,%d,%d,%s)" % (self.name, self.index, 
                                     self.size, self.flux.name)
        

# Hexahedral eight-node shape functions.  Coords are xi, eta, mu..
# Master space is (-1 -> 1) in these axes.  Normalization is so
# that the nodal value is 1.


def sf0(xi,zeta,mu):
    return -0.125*(xi-1.0)*(zeta-1.0)*(mu-1.0)
def sf1(xi,zeta,mu):
    return +0.125*(xi-1.0)*(zeta-1.0)*(mu+1.0)
def sf2(xi,zeta,mu):
    return +0.125*(xi-1.0)*(zeta+1.0)*(mu-1.0)
def sf3(xi,zeta,mu):
    return -0.125*(xi-1.0)*(zeta+1.0)*(mu+1.0)
def sf4(xi,zeta,mu):
    return +0.125*(xi+1.0)*(zeta-1.0)*(mu-1.0)
def sf5(xi,zeta,mu):
    return -0.125*(xi+1.0)*(zeta-1.0)*(mu+1.0)
def sf6(xi,zeta,mu):
    return -0.125*(xi+1.0)*(zeta+1.0)*(mu-1.0)
def sf7(xi,zeta,mu):
    return +0.125*(xi+1.0)*(zeta+1.0)*(mu+1.0)

# With this shape function ordering, the locations of the
# corresponding nodes are, in order:
# (0,0,0), (0,0,dz), (0,dy,0), (0,dy,dz),
# (dx,0,0), (dx,0,dz), (dx,dy,0), (dx,dy,dz).

# Quad shape function derivatives, wrt master coords,.  Derivatives
# are in order, xi, zeta, mu.
def dsf0d0(xi,zeta,mu):
    return -0.125*(zeta-1.0)*(mu-1.0)
def dsf0d1(xi,zeta,mu):
    return -0.125*(xi-1.0)*(mu-1.0)
def dsf0d2(xi,zeta,mu):
    return -0.125*(xi-1.0)*(zeta-1.0)

def dsf1d0(xi,zeta,mu):
    return +0.125*(zeta-1.0)*(mu+1.0)
def dsf1d1(xi,zeta,mu):
    return +0.125*(xi-1.0)*(mu+1.0)
def dsf1d2(xi,zeta,mu):
    return +0.125*(xi-1.0)*(zeta-1.0)

def dsf2d0(xi,zeta,mu):
    return +0.125*(zeta+1.0)*(mu-1.0)
def dsf2d1(xi,zeta,mu):
    return +0.125*(xi-1.0)*(mu-1.0)
def dsf2d2(xi,zeta,mu):
    return +0.125*(xi-1.0)*(zeta+1.0) 

def dsf3d0(xi,zeta,mu):
    return -0.125*(zeta+1.0)*(mu+1.0)
def dsf3d1(xi,zeta,mu):
    return -0.125*(xi-1.0)*(mu+1.0)
def dsf3d2(xi,zeta,mu):
    return -0.125*(xi-1.0)*(zeta+1.0)

def dsf4d0(xi,zeta,mu):
    return +0.125*(zeta-1.0)*(mu-1.0)
def dsf4d1(xi,zeta,mu):
    return +0.125*(xi+1.0)*(mu-1.0)
def dsf4d2(xi,zeta,mu):
    return +0.125*(xi+1.0)*(zeta-1.0)

def dsf5d0(xi,zeta,mu):
    return -0.125*(zeta-1.0)*(mu+1.0)
def dsf5d1(xi,zeta,mu):
    return -0.125*(xi+1.0)*(mu+1.0)
def dsf5d2(xi,zeta,mu):
    return -0.125*(xi+1.0)*(zeta-1.0)

def dsf6d0(xi,zeta,mu):
    return -0.125*(zeta+1.0)*(mu-1.0)
def dsf6d1(xi,zeta,mu):
    return -0.125*(xi+1.0)*(mu-1.0)
def dsf6d2(xi,zeta,mu):
    return -0.125*(xi+1.0)*(zeta+1.0)

def dsf7d0(xi,zeta,mu):
    return +0.125*(zeta+1.0)*(mu+1.0)
def dsf7d1(xi,zeta,mu):
    return +0.125*(xi+1.0)*(mu+1.0)
def dsf7d2(xi,zeta,mu):
    return +0.125*(xi+1.0)*(zeta+1.0)


# Shape functions for faces.  Clockwise around the face.

def fsf0(xi,zeta):
    return  0.25*(xi-1.0)*(zeta-1.0)
def fsf1(xi,zeta):
    return -0.25*(xi-1.0)*(zeta+1.0)
def fsf2(xi,zeta):
    return  0.25*(xi+1.0)*(zeta+1.0)
def fsf3(xi,zeta):
    return -0.25*(xi+1.0)*(zeta-1.0)

# Master-space derivatives, in-plane only of course.

def dfsf0d0(xi,zeta):
    return 0.25*(zeta-1.0)
def dfsf0d1(xi,zeta):
    return 0.25*(xi-1.0)

def dfsf1d0(xi,zeta):
    return -0.25*(zeta+1.0)
def dfsf1d1(xi,zeta):
    return -0.25*(xi-1.0)

def dfsf2d0(xi,zeta):
    return 0.25*(zeta+1.0)
def dfsf2d1(xi,zeta):
    return 0.25*(xi+1.0)

def dfsf3d0(xi,zeta):
    return -0.25*(zeta-1.0)
def dfsf3d1(xi,zeta):
    return -0.25*(xi+1.0)


class GaussPoint:
    def __init__(self,xi,zeta,mu,weight):
        self.xi = xi
        self.zeta = zeta
        self.mu = mu
        self.weight = weight
    def __repr__(self):
        return "GaussPoint(%g,%g,%g,%g)" % (self.xi, self.zeta,
                                            self.mu, self.weight)

# Utility function, closed form of the determinant of a 3x3 matrix.
def det3(lst):
    [[m11,m12,m13],[m21,m22,m23],[m31,m32,m33]] = lst
    return m11*(m22*m33-m23*m32)-m21*(m33*m12-m32*m13)+m31*(m23*m12-m22*m13)

# Utility function to invert a 3x3 matrix.  We need this for 
# our Jacobians.
def inverse3(lst):
    det = det3(lst)
    if det != 0.0:
        [[m11,m12,m13],[m21,m22,m23],[m31,m32,m33]] = lst
        return [ [ (m22*m33-m23*m32)/det, (m13*m32-m12*m33)/det, 
                   (m12*m23-m13*m22)/det ],
                 [ (m23*m31-m21*m33)/det, (m11*m33-m13*m31)/det,
                   (m13*m21-m11*m23)/det ],
                 [ (m21*m32-m22*m31)/det, (m12*m31-m11*m32)/det,
                   (m11*m22-m12*m21)/det ] ]
    raise Oops("Singular matrix in inverse3.")


class Element:
    gptable = []
    def __init__(self,idx,nodelist=[]):
        self.index = idx
        self.nodes = nodelist[:]
        self.sfns = [sf0,sf1,sf2,sf3,sf4,sf5,sf6,sf7]
        self.dsfns = [[dsf0d0,dsf0d1,dsf0d2],
                      [dsf1d0,dsf1d1,dsf1d2],
                      [dsf2d0,dsf2d1,dsf2d2],
                      [dsf3d0,dsf3d1,dsf3d2],
                      [dsf4d0,dsf4d1,dsf4d2],
                      [dsf5d0,dsf5d1,dsf5d2],
                      [dsf6d0,dsf6d1,dsf6d2],
                      [dsf7d0,dsf7d1,dsf7d2]]
        for n in self.nodes:
            n.add_element(self)
        self.frommaster_cache = {}
        self.dof_cache = {}
        self.dofdx_cache = {}
        self.dshapefn_cache = {}
    def __repr__(self):
        return "Element(%d,%s)" % (self.index, self.nodes)
    # Evaluate a shape function at a master-space coordinate
    def clear_caches(self):
        self.frommaster_cache = {}
        self.dof_cache = {}
        self.dofdx_cache = {}
        self.dshapefn_cache = {}
    def shapefn(self,i,xi,zeta,mu):
        return self.sfns[i](xi,zeta,mu)
    # Derivative of shape function i wrt component j in master space.
    def masterdshapefn(self,i,j,xi,zeta,mu):
        return self.dsfns[i][j](xi,zeta,mu)
    # Reference-space derivative of the shape function i wrt ref
    # component j.  It's a scalar, so cache-safe copying is not required.
    def dshapefn(self,i,j,xi,zeta,mu):
        try:
            return self.dshapefn_cache[(i,j,xi,zeta,mu)]
        except KeyError:


#####            jmtx = self.jacobianmtx(xi,zeta,mu)
    ################### added by shahriyar ####################
            jmtx = self.jacobianmtxdef(xi,zeta,mu)
    ################### added by shahriyar ####################
            jinv = inverse3(jmtx)

            dfdmaster = [ self.dsfns[i][0](xi,zeta,mu),
                          self.dsfns[i][1](xi,zeta,mu),
                          self.dsfns[i][2](xi,zeta,mu) ]
            

            dfdref = [ sum( jinv[ix][jx]*dfdmaster[jx] for jx in range(3) )
                       for ix in range(3) ]



            self.dshapefn_cache[(i,0,xi,zeta,mu)] = dfdref[0]
            self.dshapefn_cache[(i,1,xi,zeta,mu)] = dfdref[1]
            self.dshapefn_cache[(i,2,xi,zeta,mu)] = dfdref[2]



            
            return dfdref[j]


#****************************************************************************
    def dshapefnRef(self,xi,zeta,mu):
        jmtx = self.jacobianmtx(xi,zeta,mu)
        jinv = inverse3(jmtx)

        dfdreft = []
        
        for i in range(8):
            dfdmaster = [ self.dsfns[i][0](xi,zeta,mu),
                          self.dsfns[i][1](xi,zeta,mu),
                          self.dsfns[i][2](xi,zeta,mu) ]
            

            dfdref = [ sum( jinv[ix][jx]*dfdmaster[jx] for jx in range(3) )
                       for ix in range(3) ]

            dfdreft.append(dfdref)

        
        return dfdreft
#**************************************************************************






    # Evaluate an arbitrary DOF at a given master-space position.
    # Always returns a list, even for scalar DOFs.
    def dof(self,dofname,xi,zeta,mu):
        try:
            return self.dof_cache[(dofname,xi,zeta,mu)][:]
        except KeyError:
            res = None
            for (ni,n) in enumerate(self.nodes):
                sfval = self.shapefn(ni,xi,zeta,mu)
                for dof in n.dofs:
                    if dof.name == dofname:
                        term = [sfval*x for x in dof.value]
                        if res==None:
                            res = term
                        else:
                            res = [sum(x) for x in zip(res,term)]
            self.dof_cache[(dofname,xi,zeta,mu)]=res
            return res[:]

    # Return the reference-state derivatives jacobianmtxof a DOF at a given
    # master-space position.  Always returns a list of lists, with the
    # componentn of the derivative being the fastest-varying thing.
    def dofdx(self,dofname,xi,zeta,mu):

        try:
            return [x[:] for x in self.dofdx_cache[(dofname,xi,zeta,mu)]]
        except KeyError:
            res = None
            for (ni,n) in enumerate(self.nodes):
                dsf = [ self.dshapefn(ni,0,xi,zeta,mu),
                        self.dshapefn(ni,1,xi,zeta,mu),
                        self.dshapefn(ni,2,xi,zeta,mu) ]
                for dof in n.dofs:
                    if dof.name == dofname:
                        term = [[ df*x for x in dof.value ] for df in dsf ]
                        if res == None:
                            res = term
                        else:
                            res = [[sum(y) for y in zip(x[0],x[1])]
                                   for x in zip(res,term)]
            self.dofdx_cache[(dofname,xi,zeta,mu)]=res
            return [x[:] for x in res]
                        
    # The master-to-reference transformation.
    def frommaster(self,xi,zeta,mu):
##        try:
##            return self.frommaster_cache[(xi,zeta,mu)].clone()
##        except KeyError:
            
        xpos = sum( [self.sfns[i](xi,zeta,mu)*self.nodes[i].position.x
                     for i in range(8)] )
        ypos = sum( [self.sfns[i](xi,zeta,mu)*self.nodes[i].position.y
                     for i in range(8)] )
        zpos = sum( [self.sfns[i](xi,zeta,mu)*self.nodes[i].position.z
                     for i in range(8)] )
        res = Position(xpos,ypos,zpos)
        self.frommaster_cache[(xi,zeta,mu)] = res
        return res.clone()
        
    # Jacobian of the master-to-reference transformation.
    def jacobianmtx(self,xi,zeta,mu):

        j11 = sum( [ self.dsfns[i][0](xi,zeta,mu)*self.nodes[i].position.x
                     for i in range(8)] )
        j12 = sum( [ self.dsfns[i][1](xi,zeta,mu)*self.nodes[i].position.x
                     for i in range(8)] )
        j13 = sum( [ self.dsfns[i][2](xi,zeta,mu)*self.nodes[i].position.x
                     for i in range(8)] )

        j21 = sum( [ self.dsfns[i][0](xi,zeta,mu)*self.nodes[i].position.y
                     for i in range(8)] )
        j22 = sum( [ self.dsfns[i][1](xi,zeta,mu)*self.nodes[i].position.y
                     for i in range(8)] )
        j23 = sum( [ self.dsfns[i][2](xi,zeta,mu)*self.nodes[i].position.y
                     for i in range(8)] )

        j31 = sum( [ self.dsfns[i][0](xi,zeta,mu)*self.nodes[i].position.z
                     for i in range(8)] )
        j32 = sum( [ self.dsfns[i][1](xi,zeta,mu)*self.nodes[i].position.z
                     for i in range(8)] )
        j33 = sum( [ self.dsfns[i][2](xi,zeta,mu)*self.nodes[i].position.z
                     for i in range(8)] )
        
        return [ [ j11, j21, j31], [j12, j22, j32], [j13, j23, j33] ]
#        return [ [ j11, j12, j13], [j21, j22, j23], [j31, j32, j33] ]

    # Scalar Jacobian, aka determinant.
    def jacobian(self,xi,zeta,mu):
        return det3(self.jacobianmtx(xi,zeta,mu))
    
    
    # Return the relevant gausspoints, once they're computed.
    def gausspts(self):
        if not Element.gptable:
            # mpt = math.sqrt(3.0/5.0)
            # pts = [-mpt,0.0,mpt]
            # wts = [5.0/9.0, 8.0/9.0, 5.0/9.0]
            mpt = math.sqrt(1.0/3.0)
            pts = [-mpt,mpt]
            wts = [1.0,1.0]
            n = len(pts)
            for i in range(n):
                for j in range(n):
                    for k in range(n):
##                        Element.gptable.append(
##                            GaussPoint(pts[k],pts[j],pts[i],
##                                       wts[k]*wts[j]*wts[i]))

                        Element.gptable.append(
                            GaussPoint(pts[i],pts[j],pts[k],
                                       wts[k]*wts[j]*wts[i]))
        return Element.gptable

################################ added by Shahriyar #################
    # Jacobian of the master-to-reference transformation.
    def jacobianmtxdef(self,xi,zeta,mu):

        j11 = j12 = j13 = j21 = j22 = j23= j31 = j32 = j33 = 0.0

        j11 = sum( [ self.dsfns[i][0](xi,zeta,mu)*(self.nodes[i].position.x
                     + self.nodes[i].dofs[0].value[0]) for i in range(8)] )
        j12 = sum( [ self.dsfns[i][1](xi,zeta,mu)*(self.nodes[i].position.x
                     + self.nodes[i].dofs[0].value[0]) for i in range(8)] )
        j13 = sum( [ self.dsfns[i][2](xi,zeta,mu)*(self.nodes[i].position.x
                     + self.nodes[i].dofs[0].value[0]) for i in range(8)] )

        j21 = sum( [ self.dsfns[i][0](xi,zeta,mu)*(self.nodes[i].position.y
                     + self.nodes[i].dofs[0].value[1]) for i in range(8)] )
        j22 = sum( [ self.dsfns[i][1](xi,zeta,mu)*(self.nodes[i].position.y
                     + self.nodes[i].dofs[0].value[1]) for i in range(8)] )
        j23 = sum( [ self.dsfns[i][2](xi,zeta,mu)*(self.nodes[i].position.y
                     + self.nodes[i].dofs[0].value[1]) for i in range(8)] )

        j31 = sum( [ self.dsfns[i][0](xi,zeta,mu)*(self.nodes[i].position.z
                     + self.nodes[i].dofs[0].value[2]) for i in range(8)] )
        j32 = sum( [ self.dsfns[i][1](xi,zeta,mu)*(self.nodes[i].position.z
                     + self.nodes[i].dofs[0].value[2]) for i in range(8)] )
        j33 = sum( [ self.dsfns[i][2](xi,zeta,mu)*(self.nodes[i].position.z
                     + self.nodes[i].dofs[0].value[2]) for i in range(8)] )

#        return [ [ j11, j12, j13], [j21, j22, j23], [j31, j32, j33] ]
        return [ [ j11, j21, j31], [j12, j22, j32], [j13, j23, j33] ]

    # Scalar Jacobian, aka determinant.
    def jacobiandef(self,xi,zeta,mu):
        return det3(self.jacobianmtxdef(xi,zeta,mu))

#####################################################################



class Face:
    gptable = []
    def __init__(self,idx,element,nodelist=[]):
        self.index = idx
        self.element = element
        self.nodes = nodelist[:]
        self.sfns = [fsf0,fsf1,fsf2,fsf3]
        self.dsfns = [[dfsf0d0,dfsf0d1],[dfsf1d0,dfsf1d1],
                      [dfsf2d0,dfsf2d1],[dfsf3d0,dfsf3d1]]
        # Nodes probably don't need to know their faces.
    def __repr__(self):
        return "Face(%d,%s)" % (self.index,self.nodes)
    def shapefn(self,i,xi,zeta,mu):  # Discard mu.
        return self.sfns[i](xi,zeta)
    def masterdshapefn(self,i,j,xi,zeta,mu): # Discard mu
        return self.dsfns[i][j](xi,zeta)
    # As with elements, the reference-space derivative at the
    # master-space coordinate.  Discard mu.
    def dshapefn(self,i,j,xi,zeta,mu):
        pass
    def frommaster(self,xi,zeta,mu):
        xpos = sum( [self.sfns[i](xi,zeta)*self.nodes[i].position.x
                     for i in range(4)] )
        ypos = sum( [self.sfns[i](xi,zeta)*self.nodes[i].position.y
                     for i in range(4)] )
        zpos = sum( [self.sfns[i](xi,zeta)*self.nodes[i].position.z
                     for i in range(4)] )
        res = Position(xpos,ypos,zpos)
        return res

    def jacobian(self,xi,zeta,mu):
        [[m11,m12],[m21,m22],[m31,m32]] = self.jacobianmtx(xi,zeta,mu)
        cross = [m21*m32-m31*m22,m31*m12-m11*m32,m11*m22-m21*m12]
        return math.sqrt(cross[0]*cross[0]+
                         cross[1]*cross[1]+
                         cross[2]*cross[2])

    def jacobianmtx(self,xi,zeta,mu):
        j11 = sum( [self.dsfns[i][0](xi,zeta)*self.nodes[i].position.x
                    for i in range(4)])
        j12 = sum( [self.dsfns[i][1](xi,zeta)*self.nodes[i].position.x
                    for i in range(4)])

        j21 = sum( [self.dsfns[i][0](xi,zeta)*self.nodes[i].position.y
                    for i in range(4)])
        j22 = sum( [self.dsfns[i][1](xi,zeta)*self.nodes[i].position.y
                    for i in range(4)])

        j31 = sum( [self.dsfns[i][0](xi,zeta)*self.nodes[i].position.z
                    for i in range(4)])
        j32 = sum( [self.dsfns[i][1](xi,zeta)*self.nodes[i].position.z
                    for i in range(4)])
        return [[j11,j12],[j21,j22],[j31,j32]]
           
    def gausspts(self):
        if not Face.gptable:
            mpt = math.sqrt(1.0/3.0)
            pts = [-mpt,mpt]
            wts = [1.0,1.0]
            n = len(pts)
            for i in range(n):
                for j in range(n):
                    Face.gptable.append(GaussPoint(pts[i],pts[j],0.0,
                                                   wts[i]*wts[j]))
        return Face.gptable
        
    
    
# The general scheme is, we have a set of equations we want to solve,
# which are of the form E_i(c_j)+b_i = 0, where E_i is FE discretized
# equation and component, and b_i is the externally-applied body
# force, aka Neumann boundary condition, and the c_j variables are the
# coefficients of the shape function expansion of the degree of
# freedom field.  There is no a priori guarantee that E_i(c_j) does
# not have a constant term in its expansion, but if it does, then it
# is not reflected in b_i, which is only the externally-applied
# forces.

# There are a couple of solvers.  For the linear solver, we assume
# that E_i(c_j) is purely linear, i.e. has no constant term, and no
# higher-than-first order term.  In this case, the solution is to just
# construct the matrix dE_i/dc_j, apply the boundary conditions, and
# solve the resulting linear algebra problem for the unknowns.

# There is also a nonlinear solver.  For this solver, we use a
# Newton-Raphson technique.  Given an initial set of c_j, we
# numerically compute all the E_i, as well as M_ij = dE_i/dc_j, then
# compute an increment from M_ij.delta_c_j = -E_i, update the c_js,
# and iterate until the residual is small enough.


class Mesh:
    def __init__(self,xelements=1,yelements=1,zelements=1):
        self.nodelist = []
        self.elementlist = []

        # Boundaries to which rather primitive conditions can be
        # applied.
        self.topnodes = []
        self.bottomnodes = []
        self.bottomfaces = [] 

        dx = 1.0/xelements
        dy = 1.0/yelements
        dz = 1.0/zelements
        
        self.doflist = []
        self.eqnlist = []
        self.freedofs = [] # Index list, doesn't actually contain dofs.
        
        # Master stiffness matrix is a dictionary indexed by tuples of
        # integers, whose values are floating-point numbers.
        self.matrix = {}
        self.fbody = {}  # In principle, has Neumann BCs.
        self.eqns = {} # Values of the equations, for nonlinear solver.
        
        node_index = 0
        for i in range(zelements+1):
            for j in range(yelements+1):
                for k in range(xelements+1):
                    node = Node(node_index,Position(k*dx,j*dy,i*dz))
                    self.nodelist.append(node)
                    if i==0:
                        self.bottomnodes.append(node)
                    if i==zelements:
                        self.topnodes.append(node)
                    node_index += 1
                    
        # The node indexing is such that the node with position
        # x = a*dx, y = b*dy, z = c*dz is in the node list at
        # list position (c*(zelements+1)+b)*(yelements+1)+a
                    
        

        element_index = 0
        face_index = 0
        for i in range(zelements):
            for j in range(yelements):
                for k in range(xelements):
                    np0 = (i*(zelements+1)+j)*(yelements+1)+k
                    np1 = ((i+1)*(zelements+1)+j)*(yelements+1)+k
                    np2 = (i*(zelements+1)+(j+1))*(yelements+1)+k
                    np3 = ((i+1)*(zelements+1)+(j+1))*(yelements+1)+k
                    
                    np4 = (i*(zelements+1)+j)*(yelements+1)+k+1
                    np5 = ((i+1)*(zelements+1)+j)*(yelements+1)+k+1
                    np6 = (i*(zelements+1)+(j+1))*(yelements+1)+k+1
                    np7 = ((i+1)*(zelements+1)+(j+1))*(yelements+1)+k+1

                    nodes = [self.nodelist[np0],self.nodelist[np1],
                             self.nodelist[np2],self.nodelist[np3],
                             self.nodelist[np4],self.nodelist[np5],
                             self.nodelist[np6],self.nodelist[np7]]
                    el = Element(element_index,nodes)
                    self.elementlist.append(el)
                    element_index += 1

                    if i==0: # Element is on the bottom face.
                        fc = Face(face_index,el,[nodes[0],nodes[2],
                                                 nodes[6],nodes[4]])
                        self.bottomfaces.append(fc)
                        face_index += 1
                        
    def clear_caches(self):
        for e in self.elementlist:
            e.clear_caches()

    def addmaterial(self,material):
        self.material = material
            
    # Add a new field to be solved for. 
    def addfield(self, name, size, value=None):
        mtxsize = sum( [d.size for d in self.doflist] )
        count = 0
        for n in self.nodelist:
            newdof = Dof(name, mtxsize+count*size, size)
            if value is not None:
                for i in range(len(value)):
                    newdof.set(i,value[i])
            n.adddof(newdof)
            self.doflist.append(newdof)
            count += 1


    # Equations don't take values. Yet.
    def addeqn(self, name, size, flux):
        mtxsize = sum( [e.size for e in self.eqnlist] )
        count = 0
        for n in self.nodelist:
            neweqn = Eqn(name, mtxsize+count*size, size, flux)
            n.addeqn(neweqn)
            self.eqnlist.append(neweqn)

            count += 1

    def clear(self):
        self.matrix = {}
        self.fbody = {}
        self.eqns = {}
        self.freedofs = []


    # Reset is like clear, but also removes all the fields and
    # equations.  There is no facility for selectively removing
    # fields.
    def reset(self):
        self.clear()
        self.doflist = []
        self.eqnlist = []
        for n in self.nodelist:
            n.dofs = []


        
    # Build the flux-divergence contributions to the stiffness matrix.
    # In OOF, individual properties do this, but this is not OOF, it
    # is merely OOFoid.  It could eventually be OOFtacular.  What it
    # actually does is populate a dictionary indexed by (row,col)
    # tuples.
    
    def make_stiffness(self):
#        Cijkl_rot = self.material.precompute()
#        print "stuff",self.material.flux.cijkl
#        raw_input()
        
        for e in self.elementlist:
            print "Element...."

            Dep_gpt = []
            Cauchy_gpt = []

            XYZ = [[0.0 for i in range(3)] for j in range(8)]
            xyz = [[0.0 for i in range(3)] for j in range(8)]

            for (rrndx,rrn) in enumerate(e.nodes):
                XYZ[rrndx][0] = rrn.position.x
                XYZ[rrndx][1] = rrn.position.y
                XYZ[rrndx][2] = rrn.position.z

                xyz[rrndx][0] = rrn.position.x + rrn.dofs[0].value[0]
                xyz[rrndx][1] = rrn.position.y + rrn.dofs[0].value[1]
                xyz[rrndx][2] = rrn.position.z + rrn.dofs[0].value[2]

            
                
                
            
            for g in e.gausspts():
                SHP = e.dshapefnRef(g.xi,g.zeta,g.mu)
                
                DepC = self.material.flux.umat(xyz,SHP,self.material.flux.cijkl)

                Dep = DepC[0]
                CS = DepC[1]
                Dep_gpt.append(Dep)
                Cauchy_gpt.append(CS)
            
            for (rndx,rn) in enumerate(e.nodes): # "Row" nodes.
                igeo = 0
                for eq in rn.eqns:
                    
                    
                    for i in range(eq.size):
                        row = eq.index+i
                        for (cndx,cn) in enumerate(e.nodes):  # "Column" nodes.
                            for df in cn.dofs:                                
                                for j in range(df.size):
                                    # this is for the geometric part
                                    igeo = j - i
                                    col = df.index+j
                                    # Now we have (row,col) for the matrix.
                                    # Compute the integrand.
                                    val = 0.0
                                    vals = 0.0
                                    for (gdx,g) in enumerate(e.gausspts()):
                                        Dep_gp = Dep_gpt[gdx]
                                        Cauchy_gp = Cauchy_gpt[gdx]
                                        dval = self._flux_deriv(
                                             e, rndx, cndx, i,
                                             j, g,Dep_gp,Cauchy_gp,igeo)
                                        dval *= g.weight
                                        dval *= e.jacobiandef(g.xi,g.zeta,g.mu)
                                        val += dval
                                    try:
                                        self.matrix[(row,col)] += val
                                    except KeyError:
                                        self.matrix[(row,col)] = val

#    def _flux_deriv(self, element, rndx, cndx, eqn, eqcomp,
#                    dof, dofcomp, gpt):
    def _flux_deriv(self, element, rndx, cndx, eqcomp,
                     dofcomp, gpt,Dep_gp,Cauchy_gp,igeo):

        # We are inside most of the matrix loops, including the
        # gausspoint loop. Take the derivative.
        # Rndx is the element's index of the shapefunction for the row.
        # Cndx is the element's index of the shapefunction for the column.
        # Eqn is the equation object, eqncomp the component.
        # Dof is the ODF object, dofcomp the component.
        # Gpt is the gausspoint, pos the reference-state position of it.


#        pos = element.frommaster(gpt.xi,gpt.zeta,gpt.mu)
#        dofval = element.dof(dof.name, gpt.xi,gpt.zeta,gpt.mu)
#        dofderivs = element.dofdx(dof.name, gpt.xi,gpt.zeta,gpt.mu)

        # In principle, we could check metadata here, to make sure
        # that the flux we are calling contributes to the equation
        # we're working on, and understands teh DOF we're passing in.
        # However, for this prototype, all DOFs are displacement, and
        # all equations are force-balance.
#        print igeo
#        raw_input()
        # Pre-compute the flux derivatives.
        k = dofcomp
        fluxdvs = []
        for l in range(3):
            TMP = [[0.0 for ii in range(3)] for jj in range(3)]
            for i in range(3):
                for j in range(3):
                    TMP[i][j] = Dep_gp[i][j][k][l]
            fluxdvs.append(TMP)
                        
        TMP = [[0.0 for ii in range(3)] for jj in range(3)]
        if igeo == 0:
            gstress = Cauchy_gp
        else:
            gstress = TMP
        
#        fluxdvs = [ eqn.flux.dukl(dofcomp,l,
#                                  pos,dofval,dofderivs) for l in range(3) ]
#        fluxdvs = [ Dep_gp[i][j][k][l] for l in range(3) ]

        res = 0.0
        ress = 0.0
#        element.dshapefn = [dNi/dX,dNi/dY,dNi/dZ]
        for j in range(3):
            for l in range(3):
                res -= element.dshapefn(rndx,j,gpt.xi,gpt.zeta,gpt.mu)*\
                       fluxdvs[l][eqcomp][j]*\
                       element.dshapefn(cndx,l,gpt.xi,gpt.zeta,gpt.mu)

        for j in range(3):
            for l in range(3):
                res -= element.dshapefn(rndx,j,gpt.xi,gpt.zeta,gpt.mu)*\
                       gstress[l][j]*\
                       element.dshapefn(cndx,l,gpt.xi,gpt.zeta,gpt.mu)
        
        return res 
            
    
    # Function for computing the value of each of the equations for
    # the current degrees of freedom.  Needed by the Newton-Raphson
    # solver.  Just does a straightforward integral.  Note that the
    # value of the equation and the value of the flux are not the same
    # thing.  Populates the self.eqns attribute.
    def evaluate_eqns(self):
#        Cijkl_rot = self.material.precompute()
        for e in self.elementlist:
#*************************************
            
            XYZ = [[0.0 for i in range(3)] for j in range(8)]
            xyz = [[0.0 for i in range(3)] for j in range(8)]

            for (rrndx,rrn) in enumerate(e.nodes):
                XYZ[rrndx][0] = rrn.position.x
                XYZ[rrndx][1] = rrn.position.y
                XYZ[rrndx][2] = rrn.position.z

                xyz[rrndx][0] = rrn.position.x + rrn.dofs[0].value[0]
                xyz[rrndx][1] = rrn.position.y + rrn.dofs[0].value[1]
                xyz[rrndx][2] = rrn.position.z + rrn.dofs[0].value[2]

#**********************************
            for (mudx,mu) in enumerate(e.nodes):

                

                for eq in mu.eqns:
                    for i in range(eq.size):
                        row = eq.index+i
                        val = 0.0
                        for g in e.gausspts():
#*******
                            SHP = e.dshapefnRef(g.xi,g.zeta,g.mu)
#********
                            dval = self._flux_contrib(
                                e, mudx, eq, i, g,xyz,SHP)#Cijkl_rot)
                            dval *= g.weight
                            dval *= e.jacobiandef(g.xi,g.zeta,g.mu)
                            val += dval
                        try:
                            self.eqns[row]+=val

                        except KeyError:
                            self.eqns[row]=val

    def _flux_contrib(self, element, rndx, eqn, eqndx, gpt,xyz,SHP):#Cijkl_rot):
        # This is essentially the integrand function for the equation
        # values. It assumes a divergence flux, and includes
        # contributions from the derivative of the row shape function,
        # and the negative sign from the integration by parts.
        pos = element.frommaster(gpt.xi,gpt.zeta,gpt.mu)

        dofname = eqn.flux.fieldname # Assume there's only one, for now.
        dofval = element.dof(dofname,gpt.xi,gpt.zeta,gpt.mu)
        dofderivs = element.dofdx(dofname,gpt.xi,gpt.zeta,gpt.mu)
        res = 0.0
#        for j in range(3):
#            res -= element.dshapefn(rndx,j,gpt.xi,gpt.zeta,gpt.mu)*\
#                   eqn.flux.value(eqndx,j,pos,dofval,dofderivs,xyz,SHP,self.material.flux.cijkl)#Cijkl_rot)
        for j in range(3):
            res -= element.dshapefn(rndx,j,gpt.xi,gpt.zeta,gpt.mu)*\
                   eqn.flux.umat(xyz,SHP,self.material.flux.cijkl)[1][j][eqndx]

        return res
                                                    
    # Values are z offsets of the top and bottom boundaries, which are
    # assumed fixed to zero offset in the x and y direction.  BCs can
    # be set to None, in which case they are not fixed, but why woold
    # you do that?
    def setbcs(self,top,bottom):
        self.topbc = top
        self.bottombc = bottom


    def set_freedofs(self):
        # Builds the self.freedofs vector, and returns some counts and
        # lists. After this is done, the self.freedofs vector has, for
        # each entry, an integer -- if the integer is positive or
        # zero, then this DOF is free and the integer is the index.
        # If the integer is negative, then this DOF is fixed, and the
        # absolute value of the integer is one more than the index, so
        # that -1 is the fixed DOF with index 0, for instance.  The
        # fixed_rhs vector has the actual numerical values of the
        # fixed DOFs, using the self.freedofs indexing scheme.
        mtxsize = sum( [d.size for d in self.doflist] )
        self.freedofs = [-1]*mtxsize
        fixed_rhs = []
        for node in self.nodelist:
            for dof in node.alldofs():
                add = False # Add to free DOF list?
                if dof.name!="Displacement":
                    add = True # All non-displacement DOFs are free.
                else: # dof.name *is* "Displacement"
                    if (not (node in self.topnodes) and \
                        not (node in self.bottomnodes)) \
                        or ( (node in self.topnodes) and \
                             self.topbc is None):
                        add = True
                    else: # Fixed DOF, add to fixed-rhs list.
                        fixed_rhs.append(0.0)  # X component.
                        fixed_rhs.append(0.0)  # Y component.
                        if node in self.topnodes:
                            fixed_rhs.append(self.topbc)
                        else:
                            fixed_rhs.append(self.bottombc)
                if add:
                    for k in range(dof.index, dof.index+dof.size):
                        self.freedofs[k]=k
        # So now we have the list, compress it.
        free_count = 0
        fixed_count = -1
        for idx in range(len(self.freedofs)):
            if self.freedofs[idx]!=-1:
                self.freedofs[idx]=free_count
                free_count+=1
            else:
                self.freedofs[idx]=fixed_count
                fixed_count-=1

        return (free_count, fixed_count, fixed_rhs)


    def linearsystem(self):
        # Populates Smallmatrix objects from the self.matrix and
        # self.fbody and self.eqns dictionaries.  BC's are implemented
        # here. Note that it's OK for the self.eqns dictionary to be
        # empty, it just means that the eqvs vector will be all zeros.

        (free_count, fixed_count, fixed_rhs) = self.set_freedofs()

        amtx = SmallMatrix(free_count,free_count)
        cmtx = SmallMatrix(free_count,-(fixed_count+1))
        brhs = SmallMatrix(len(fixed_rhs),1)  # Boundary RHS.
        frhs = SmallMatrix(free_count,1)      # Body forces.
        eqvs = SmallMatrix(free_count,1)  # Equation values.

        
        amtx.clear()
        cmtx.clear()
        brhs.clear()
        frhs.clear()
        eqvs.clear()


        for ((i,j),v) in self.matrix.items():
            if self.freedofs[i]>=0 and self.freedofs[j]>=0:
                amtx[self.freedofs[i],self.freedofs[j]]=v
            
            else:
                if self.freedofs[i]>=0 and self.freedofs[j]<0:
                    cmtx[self.freedofs[i],-(self.freedofs[j]+1)]=v

        for i in range(len(fixed_rhs)):
            brhs[i,0]=fixed_rhs[i]

        for (i,v) in self.fbody.items():
            if self.freedofs[i]>=0:
                frhs[self.freedofs[i],0]=v

        # TODO: We're assuming conjugacy here, which may not be wise.
        for (i,v) in self.eqns.items():
            if self.freedofs[i]>=0:
                eqvs[self.freedofs[i],0]=-v  #shahriyar has put minus
                
        return (amtx,cmtx,brhs,frhs,eqvs)

    
    # Assumes the "Displacement" field has been added to the mesh, and
    # the appropriate equations and the bcs are set. Builds the big
    # master stiffness matrix.
    def solve_linear(self):
        self.make_stiffness()
       
        (a,c,br,fr,eq) = self.linearsystem()
        # We don't use eq in the linear case.

        # Sign.  Solver solves Ax=b, not Ax+b=0.
        nr = (c*br)*(-1.0)-fr # Fr is zero if no Neumann BCs.


        if a.rows()!=0:
            rr = a.solve(nr)
        else:
            rr = 0 # Degenerate case, set to "solved".

        
        if rr==0:
            for n in self.nodelist:
                for d in n.alldofs():
                    for k in range(d.size):
                        ref = self.freedofs[d.index+k]
                        if ref >= 0:
                            d.set(k,nr[ref,0])
                        else:
                            d.set(k,br[-(ref+1),0])
                            
        else:
            Oops("Error in linear solver, return code is %d." % rr)


    # Assumes the "Displacement" field has been added to the system,
    # and that the big master matrix of derivatives of equations with
    # respect to the coefficients has been built, and that self.eqns
    # equation values have been set.
    def solve_nonlinear(self):
        (a,c,br,fr,eq) = self.linearsystem()


        nr = (c*br)*(-1.0)-fr+eq



        if a.rows()!=0:
            rr = a.solve(nr)
        else:
            Oops("Zero rows in the A matrix, very odd...")

        if rr==0:
            mag = 0.0
            for n in self.nodelist:
                for d in n.alldofs():
                    for k in range(d.size):
                        ref = self.freedofs[d.index+k]
                        if ref >= 0:
                            v = nr[ref,0]
                            mag += v*v
                            d.add(k,v)
                        else:
###                            d.set(k,br[-(ref+1),0]) # Should be redundant.
                            d.add(k,br[-(ref+1),0]) # added by shahriyar

        else:
            Oops("Error in nonlinear solver, return code is %d." % rr)
            

#--------- start convergence loop -----------------------

        iconv = 0
        nconv = 2
        ratio_norm = 1.0e10
        magiter = [0.0 for i in range(nconv)]
        while (iconv <= nconv-1 and abs(ratio_norm) >= 1.0e-9):
            if iconv > 0:

                (a,c,br,fr,eq) = self.linearsystem()

                nr = eq

                if a.rows()!=0:
                    rr = a.solve(nr)
                else:
                    Oops("Zero rows in the A matrix, very odd...")

                if rr==0:
                    for n in self.nodelist:
                        for d in n.alldofs():
                            for k in range(d.size):
                                ref = self.freedofs[d.index+k]
                                if ref >= 0:
                                    v = nr[ref,0]
                                    magiter[iconv] += v*v
                                    d.add(k,v)


                else:
                    Oops("Error in nonlinear solver, return code is %d." % rr)

            self.clear_caches()
            self.eqns = {}
            self.evaluate_eqns()

            self.matrix = {}
            self.clear_caches()
            self.make_stiffness()            
            

            ratio_norm = 0.0

            gf_nod = unb_nod = 0.0


            for (i,v) in self.eqns.items():
                gf_nod += v*v


            for (i,v) in self.eqns.items():
                if self.freedofs[i]>=0:
                    unb_nod += v*v

             
            norm_gs = math.sqrt(gf_nod)
            norm_us = math.sqrt(unb_nod)


            ratio_norm = norm_us/norm_gs

            print iconv,norm_us,ratio_norm

            iconv += 1

            
#--------- end convergence loop -----------------------

        
        return math.sqrt(mag) # Size of the increment. *Not* the residual.


###################### post-proccesing ###########################
    def evaluate_ss(self):
#        Cijkl_rot = self.material.precompute()



        valstrain = 0.0 ; valstress = 0.0 ; vol = 0.0
        for e in m.elementlist:
            
            XYZ = [[0.0 for i in range(3)] for j in range(8)]
            xyz = [[0.0 for i in range(3)] for j in range(8)]

            for (rrndx,rrn) in enumerate(e.nodes):
                XYZ[rrndx][0] = rrn.position.x
                XYZ[rrndx][1] = rrn.position.y
                XYZ[rrndx][2] = rrn.position.z

                xyz[rrndx][0] = rrn.position.x + rrn.dofs[0].value[0]
                xyz[rrndx][1] = rrn.position.y + rrn.dofs[0].value[1]
                xyz[rrndx][2] = rrn.position.z + rrn.dofs[0].value[2]

            
            for g in e.gausspts():
                SHP = e.dshapefnRef(g.xi,g.zeta,g.mu)

                
                dvalstrain = self.CastressTstrain(e,g,xyz,SHP)[0]#Cijkl_rot)[0]
                dvalstress = self.CastressTstrain(e,g,xyz,SHP)[1]#Cijkl_rot)[1]


                dvalstrain *= e.jacobiandef(g.xi,g.zeta,g.mu)
                dvalstress *= e.jacobiandef(g.xi,g.zeta,g.mu)

                vol += e.jacobiandef(g.xi,g.zeta,g.mu)

                valstrain += dvalstrain
                valstress += dvalstress

        vol_T_strain = valstrain/vol
        vol_C_stress = valstress/vol

        return vol_T_strain,vol_C_stress


    def CastressTstrain(self, element,gpt,xyz,SHP):#Cijkl_rot):

        pos = element.frommaster(gpt.xi,gpt.zeta,gpt.mu)
        dofderivs = element.dofdx("Displacement", gpt.xi,gpt.zeta,gpt.mu)
        CaT = self.Cavalue(xyz,SHP)#Cijkl_rot)

        T_Strain = CaT[0] ; C_Stress = CaT[1]


        return T_Strain,C_Stress

    
    def Cavalue(self,xyz,SHP):#ijkl_rot):

#        cijkl = Cijkl(c11=2.0,c12=1.3,c44=1.0)#(lmbda = 1.0,mu = 0.5)
        FG = self.calc_F(xyz,SHP)            # F at gausspoint
        E_lag = self.calc_E_lag(FG)[0]            # Euler-Lagrange strain
        RCGDT = self.true_strain(self.calc_E_lag(FG)[1])
        S = self.SPK_stress(E_lag)#Cijkl_rot)#cijkl)             # 2nd PK stress
        Ca = self.Ca_stress(FG,S)             # Cauchy Stress stress

        return RCGDT[2][2],Ca[2][2]

#################### Calculate deformation gradient #############@###########
#    def calc_F(self,du_ij):
    def calc_F(self,cord,SHP):
    
        dxt_dx0 = 0.0 ; dxt_dy0 = 0.0 ; dxt_dz0 = 0.0
        dyt_dx0 = 0.0 ; dyt_dy0 = 0.0 ; dyt_dz0 = 0.0
        dzt_dx0 = 0.0 ; dzt_dy0 = 0.0 ; dzt_dz0 = 0.0

        for i in range(8):
            dxt_dx0 += SHP[i][0]*cord[i][0]
            dxt_dy0 += SHP[i][1]*cord[i][0]
            dxt_dz0 += SHP[i][2]*cord[i][0]
            
            dyt_dx0 += SHP[i][0]*cord[i][1]
            dyt_dy0 += SHP[i][1]*cord[i][1]
            dyt_dz0 += SHP[i][2]*cord[i][1]

            dzt_dx0 += SHP[i][0]*cord[i][2]
            dzt_dy0 += SHP[i][1]*cord[i][2]
            dzt_dz0 += SHP[i][2]*cord[i][2]
     
        FG = [[0. for ii in range(3)] for jj in range(3)]
        FG[0][0] = dxt_dx0 ; FG[0][1] = dxt_dy0 ; FG[0][2] = dxt_dz0
        FG[1][0] = dyt_dx0 ; FG[1][1] = dyt_dy0 ; FG[1][2] = dyt_dz0
        FG[2][0] = dzt_dx0 ; FG[2][1] = dzt_dy0 ; FG[2][2] = dzt_dz0


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

        return E_lag,C
#################### End of calculation of Lagrangian strain #################

################ Calculation of logarithmic strain #############
    def true_strain(self,a):
        v = [[0.0 for i in range(3)] for j in range(3)]
        beta = [0.0 for i in range(3)]
        
        p1 = a[0][1]**2 + a[0][2]**2 + a[1][2]**2

        if p1 < 1.0e-10:
            for ivec in range(3):
                beta[ivec] = a[ivec][ivec]
                v[ivec][ivec] = 1.0
        elif p1 >= 1.0e-10:

            q = 0.0
            for i in range(3):
                q += a[i][i]
            q = q/3.0
            Iden = [[0.0 for i in range(3)] for j in range(3)]
            Iden[0][0] = Iden[1][1] = Iden[2][2] = 1.0
            tmp1 = [[0.0 for i in range(3)] for j in range(3)]
            tmp2 = [[0.0 for i in range(3)] for j in range(3)]

            for i in range(3):
                for j in range(3):
                    tmp1[i][j] = a[i][j]-q*Iden[i][j]

            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        tmp2[i][j] += tmp1[i][k]*tmp1[k][j]
                    tmp2[i][j] = tmp2[i][j]/6.0
            p = 0.0
            for i in range(3):
                p += tmp2[i][i]
            p = math.sqrt(p)

            b = [[0.0 for i in range(3)] for j in range(3)]
            for i in range(3):
                for j in range(3):
                    b[i][j] = tmp1[i][j]/p
           
            det_b = b[0][0]*b[1][1]*b[2][2]-b[0][0]*b[1][2]*b[2][1]-b[1][0]*b[0][1]\
                      *b[2][2]+b[1][0]*b[0][2]*b[2][1]+b[2][0]*b[0][1]*b[1][2]-b[2][0]\
                      *b[0][2]*b[1][1]
            r = det_b/2.0
            if r <= -1.0:
                phi = math.pi/3.0
            elif r >= 1.0:
                phi = 0.0
            elif r > -1.0 and r < 1.0:
               phi = math.acos(r)/3.0
           

            beta[0] = q + 2.0 * p * math.cos(phi)
            beta[1] = q + 2.0 * p * math.cos(phi + (2.0*math.pi/3.0))
            beta[2] = 3.0 * q - beta[0] - beta[1]

            tmp3 = [[0.0 for i in range(3)] for j in range(3)]

            for ivec in range(3):
                for i in range(3):
                    for j in range(3):
                        tmp3[i][j] = a[i][j]-beta[ivec]*Iden[i][j]

                if tmp3[2][2] != 0.0:
                    alpha1 = 1.0
                    alpha21 = -tmp3[1][0]+(tmp3[1][2]*tmp3[2][0]/tmp3[2][2])
                    alpha22 = tmp3[1][1]-(tmp3[1][2]*tmp3[2][1]/tmp3[2][2])
                    alpha2 = alpha21/alpha22
                    alpha3 = (-tmp3[2][0]/tmp3[2][2])-(tmp3[2][1]/tmp3[2][2])*alpha2
                if tmp3[2][2] == 0.0 and tmp3[2][1] != 0.0:
                    alpha1 = 1.0
                    alpha2 = -tmp3[2][0]/tmp3[2][1]
                    if tmp3[1][2] != 0.0:
                        alpha3 = (tmp3[1][0]-tmp3[1][1]*alpha2)/tmp3[1][2]
                    elif tmp3[1][2] == 0.0 and tmp3[0][2] != 0.0:
                        alpha3 = (tmp3[0][0]-tmp3[0][1]*alpha2)/tmp3[1][2]
                    elif tmp3[1][2] == 0.0 and tmp3[0][2] == 0.0:
                        alpha3 = 0.0

                if tmp3[2][2] == 0.0 and tmp3[2][1] == 0.0 and tmp3[2][1] != 0.0:
                    alpha1 = 0.0
                    if tmp3[1][2] != 0.0:
                        alpha2 = 1.0            
                        alpha3 = -tmp3[1][1]/tmp3[1][2]
                    elif tmp3[1][2] == 0.0 and tmp3[0][2] != 0.0:
                        alpha2 = 0.0            
                        alpha3 = 1.0

                alpha = math.sqrt(alpha1**2+alpha2**2+alpha3**2)
                alpha1 = alpha1/alpha ; alpha2 = alpha2/alpha ; alpha3 = alpha3/alpha
                v[ivec][0] = alpha1 ; v[ivec][1] = alpha2 ; v[ivec][2] = alpha3

        strain = [[0.0 for i in range(3)] for j in range(3)]

        tmpv1 = [[0.0 for i in range(3)] for j in range(3)]
        tmpv2 = [[0.0 for i in range(3)] for j in range(3)]
        tmpv3 = [[0.0 for i in range(3)] for j in range(3)]

        for i in range(3):
            for j in range(3):
                tmpv1[i][j] = v[0][i]*v[0][j]
                
        for i in range(3):
            for j in range(3):
                tmpv2[i][j] = v[1][i]*v[1][j]

        for i in range(3):
            for j in range(3):
                tmpv3[i][j] = v[2][i]*v[2][j]
        for i in range(3):
            for j in range(3):
                strain[i][j] = 0.0
                strain[i][j] = 0.5*math.log(beta[0])*tmpv1[i][j]+\
                               0.5*math.log(beta[1])*tmpv2[i][j]+\
                               0.5*math.log(beta[2])*tmpv3[i][j]

        return strain            

################ end of calculation of logarithmic strain ######


####################### Calculate the 2PK stress  ############################
    def SPK_stress(self,E_lag):
        
        S = [[0. for ii in range(3)] for jj in range(3)]
        cijkl = self.material.flux.cijkl
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        S[i][j] += cijkl[i][j][k][l]*E_lag[k][l]

        return S
################### End of Calculation the 2PK stress #########################
####################### Calculate the 1PK stress  ############################
    def Ca_stress(self,Fe,S):
        
        Cauchy = [[0. for ii in range(3)] for jj in range(3)]

        det_F_e=(Fe[0][0]*Fe[1][1]*Fe[2][2]\
                -Fe[0][0]*Fe[1][2]*Fe[2][1]-Fe[1][0]*Fe[0][1]*Fe[2][2]\
                 +Fe[1][0]*Fe[0][2]*Fe[2][1]+Fe[2][0]*Fe[0][1]*Fe[1][2]\
                 -Fe[2][0]*Fe[0][2]*Fe[1][1])

        FeT = zip(*Fe)

        TMP = [[0. for ii in range(3)] for jj in range(3)]

        for i in range(3):
            for j in range(3):
                for k in range(3):
                    TMP[i][j] += S[i][k]*FeT[k][j]
                    
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    Cauchy[i][j] += (Fe[i][k]*TMP[k][j])/det_F_e

        return Cauchy
################### End of Calculation the 1PK stress #########################

##################################################################
                 



        

    def measure_force(self,flux):
        # Scheme: Evaluate the fluxes on the bottom surface, doing an
        # integral elementwise.  This routine is kind of specialized,
        # and includes a hard-coded DOF name and hard-coded knowledge
        # of the relationship between face and element master
        # coordinates.  It also knows its on the bottom, and can just
        # pick out the z component of the stress.
        res = [0.0,0.0,0.0]
        for f in self.bottomfaces:
            for g in f.gausspts():
                jw = f.jacobian(g.xi,g.zeta,g.mu)*g.weight
                dofval = f.element.dof("Displacement",
                                       g.xi,g.zeta,-1.0)
                dofderivs = f.element.dofdx("Displacement",
                                            g.xi,g.zeta,-1.0)
                # Only want the z components.  The "None" argument is
                # for the position, we don't care for now.
                fvec = [ flux.value(i,2,None,dofval,dofderivs)
                         for i in range(3) ]
                res[0]+=fvec[0]*jw
                res[1]+=fvec[1]*jw
                res[2]+=fvec[2]*jw
        return res
                
        
    
    # TODO: Draw strains, draw stresses?
    def draw(self,displaced=False):
        import mayavi.mlab as mlab
        import numpy as np

        # mlab.options.offscreen = True
        fg = mlab.figure(bgcolor=(1,1,1))
        fg.scene.disable_render = True

        # Undisplaced.
        dotset = set()
        segset = set()

        # Displaced.
        ddotset = set()
        dsegset = set()
        
        segmap = [ [0,1],[1,3],[3,2],[2,0],[0,4],[1,5],[3,7],
                   [2,6],[4,5],[5,7],[7,6],[6,4] ]
        # The dotset is the set of all the dots.  The segset is the
        # set of all segments, where we use a canonical ordering
        # scheme in order to ensure uniqueness independent of node
        # order.
        for e in self.elementlist:
            for n in e.nodes:
                dotset.add(n.position)
                if displaced:
                    dpos = n.position
                    disp_idx = n.dof("Displacement")
                    disp_val = Position(disp_idx.value[0],
                                        disp_idx.value[1],
                                        disp_idx.value[2])
                    ddotset.add(n.position+disp_val)
            for seq in segmap:
                p1 = e.nodes[seq[0]].position
                p2 = e.nodes[seq[1]].position
                if p1 < p2:
                    segset.add( (p1,p2) )
                else:
                    segset.add( (p2,p1) )
                if displaced:
                    p1dx = e.nodes[seq[0]].dof("Displacement")
                    p2dx = e.nodes[seq[1]].dof("Displacement")
                    p1dv = Position(p1dx.value[0],p1dx.value[1],p1dx.value[2])
                    p2dv = Position(p2dx.value[0],p2dx.value[1],p2dx.value[2])
                    p1d = p1+p1dv
                    p2d = p2+p2dv
                    if p1d < p2d:
                        dsegset.add( (p1d,p2d) )
                    else:
                        dsegset.add( (p2d,p1d) )
                        
                    
        # Dots.
        xs = np.array([p.x for p in dotset])
        ys = np.array([p.y for p in dotset])
        zs = np.array([p.z for p in dotset])
        mlab.points3d(xs,ys,zs,figure=fg,color=(0.5,0.5,0.5),
                      scale_factor=0.04)

        if displaced:
            xs = np.array([p.x for p in ddotset])
            ys = np.array([p.y for p in ddotset])
            zs = np.array([p.z for p in ddotset])
            mlab.points3d(xs,ys,zs,figure=fg,color=(0,0,0),
                          scale_factor=0.04)
            
        # Segments. Drawing all these is very slow, there are
        # apparently too damn many objects in the scene, even though
        # there are only a few hundred.
        for s in segset:
            seqx = np.array( [s[0].x,s[1].x] )
            seqy = np.array( [s[0].y,s[1].y] )
            seqz = np.array( [s[0].z,s[1].z] )
            mlab.plot3d( seqx, seqy, seqz, color=(0.5,0.5,0.5),
                         figure=fg,tube_radius=None)

        if displaced:
            for s in dsegset:
                seqx = np.array( [s[0].x,s[1].x] )
                seqy = np.array( [s[0].y,s[1].y] )
                seqz = np.array( [s[0].z,s[1].z] )
                mlab.plot3d( seqx, seqy, seqz, color=(0,0,0),
                             figure=fg,tube_radius=None)

            
        fg.scene.disable_render = False
        mlab.show() # Blocking..
        

    def dump_matrix(self,outfile):
        # We sometimes want to diff matrices, which means we need to
        # control the order of the indices, which is why we iterate
        # over the possible index pairs, isntead of just dumping it
        # out in dictionary order.
        mtxsize = sum( [d.size for d in self.doflist] )
        for i in range(mtxsize):
            for j in range(mtxsize):
                try:
                    v = self.matrix[i,j]
                except KeyError:
                    pass
                else:
                    print >> outfile,i,j,v
                    



# A flux is a thing that has zero divergence in equilibrium.
# Components of the divergence of the flux at a given node correspond
# to Eqn objects.  Fluxes know what fields they depend on.


    
# Elastic constitutive bookkeeppiinngg.


##voigt = [[0,5,4],
##         [5,1,3],
##         [4,3,2]]
##
##
##def Cij(lmbda,mu):
##    # Canonical: lmbda=0.5, mu=0.25, gives c11=1.0,c12=0.5.
##    c11 = lmbda + 2.0*mu
##    c12 = lmbda
##    c44 = 0.5*(c11-c12)
##    return [[c11, c12, c12, 0.0, 0.0, 0.0],
##            [c12, c11, c12, 0.0, 0.0, 0.0],
##            [c12, c12, c11, 0.0, 0.0, 0.0],
##            [0.0, 0.0, 0.0, c44, 0.0, 0.0],
##            [0.0, 0.0, 0.0, 0.0, c44, 0.0],
##            [0.0, 0.0, 0.0, 0.0, 0.0, c44]]
##
##
##def Cijkl(lmbda,mu):
##    cij = Cij(lmbda,mu)
##    return [ [ [ [ cij[voigt[i][j]][voigt[k][l]] for l in range(3) ]
##                  for k in range(3) ] for j in range(3) ] for i in range(3) ]
##
                 

          
class Orientation:
    def __init__(self, phi, theta, omega):
        self.rotation = self._euler_rot(phi,theta,omega)
############## Rotation Matrix based on Euler angles #####################
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
###################### End of Rotation Matrix #####################

class Material:
    def __init__(self,name,flux=None,orientation=None):
        self.name = name
        self.flux = flux
        self.orientation = orientation
    def get_flux(self):
        return self.flux

    # For the future:
    def precompute(self):
        omtx = self.orientation.rotation
#        print omtx
#        raw_input()
#        Cijkl_rot = self.flux.rotate(omtx)
        self.flux.rotate(omtx)
#        print self.flux.cijkl

#        return Cijkl_rot



##voigt = [[0,5,4],
##         [5,1,3],
##         [4,3,2]]


##def Cij(c11,c12,c44):#lmbda,mu):
##    # Canonical: lmbda=0.5, mu=0.25, gives c11=1.0,c12=0.5.
###    c11 = lmbda + 2.0*mu
###    c12 = lmbda
###    c44 = 0.5*(c11-c12)
##    return [[c11, c12, c12, 0.0, 0.0, 0.0],
##            [c12, c11, c12, 0.0, 0.0, 0.0],
##            [c12, c12, c11, 0.0, 0.0, 0.0],
##            [0.0, 0.0, 0.0, c44, 0.0, 0.0],
##            [0.0, 0.0, 0.0, 0.0, c44, 0.0],
##            [0.0, 0.0, 0.0, 0.0, 0.0, c44]]
##
##
##def Cijkl(c11,c12,c44):#lmbda,mu):
##    cij = Cij(c11,c12,c44)#(lmbda,mu)
##    return [ [ [ [ cij[voigt[i][j]][voigt[k][l]] for l in range(3) ]
##                  for k in range(3) ] for j in range(3) ] for i in range(3) ]
##












def go(size):
    pass # Collect $200?

#
# The general scheme is, you create a mesh, add a field, maybe add
# some equations with associated fluxes, build the matrix and
# right-hand side, which calls out to the flux objects for their
# derivatives and values, and then solve.  You can write the solution
# back into the mesh (for iterating, of course) using the Dof "set"
# method.

def displaced_drawing_test():
    m = Mesh(xelements=1,yelements=1,zelements=1)
    m.addfield("Displacement",3)
    
    for n in m.nodelist:
        p = n.position
        dp = [0,0,p.z*0.1]
        df = n.dof("Displacement")
        for i in range(3):
            df.value[i]=dp[i]
            
    m.draw(displaced=True)


def face_integration_test():
    n1 = Node(0,Position(2.0,2.0,0.0))
    n2 = Node(1,Position(3.0,3.0,0.0))
    n3 = Node(2,Position(2.0,4.0,0.0))
    n4 = Node(3,Position(1.0,3.0,0.0))
    f = Face(0,None,[n1,n2,n3,n4])
    
    # See if we can get the right area.
    res = 0.0
    for g in f.gausspts():
        res += g.weight*f.jacobian(g.xi,g.zeta,g.mu)
    return res # Should be 2.0.
    

if __name__=="__main__":
    m = Mesh(xelements=2,yelements=2,zelements=2)
    
    f = CauchyStress("Stress")
    ore = Orientation(0.0,35.0,45.0)
    mtl = Material("Stuff",flux=f,orientation=ore)

    mtl.precompute()

#    print mtl.flux.cijkl
    
    m.addmaterial(mtl)

    m.addfield("Displacement",3)
    m.addeqn("Force",3,f) # Last argument is the flux.


##    for i in m.nodelist:
##        print i.eqns[0].flux.value
##        print i.dofs[0].value
##
    nstep = 10
    m.make_stiffness()#mtl.flux.cijkl)


    SS0 = m.evaluate_ss()
    x = [] ; y = []
    x.append(SS0[0]) ; y.append(SS0[1])


    ssy = open('py.22','w')

    ssy.write("%f   %f" % (SS0[0],SS0[1]))
    ssy.write('\n')

    for istep in range(nstep):

    
        m.setbcs(0.05,0.0)
        m.solve_nonlinear()

##        for n in m.nodelist:
##            print n.index,0,n.dofs[0].value[0]
##            print n.index,1,n.dofs[0].value[1]
##            print n.index,2,n.dofs[0].value[2]
##        raw_input()
        SS = m.evaluate_ss()
        print SS
        x.append(abs(SS[0])) ; y.append(SS[1])

        ssy.write("%f   %f" % (abs(SS[0]),SS[1]))
        ssy.write('\n')

    ssy.close()

    plt.plot(x,y)
    plt.ylabel('Stress(MPa)')
    plt.xlabel('Strain')

    plt.show()



##        for e in m.elementlist:
##            for g in e.gausspts():
##                print e.jacobiandef(g.xi,g.zeta,g.mu)

#    m.solve_linear()
#    force_val = m.measure_force(f)

#     # m.solve_nonlinear()
#    m.draw(displaced=True)
#    
        
##    for n in m.nodelist:
##        print n.index,0,n.position.x+n.dofs[0].value[0]
##        print n.index,1,n.position.y+n.dofs[0].value[1]
##        print n.index,2,n.position.z+n.dofs[0].value[2]






        
