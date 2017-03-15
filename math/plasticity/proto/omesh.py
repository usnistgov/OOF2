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

import smallmatrix
import position

import flux
from flux import CauchyStress
from flux import Orientation

import umat
from umat import umat

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
        self.fields = []
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

    def allfields(self):
        return self.fields[:]

    def nfields(self):
        return len(self.fields)

    def nfieldcomps(self):
        res = 0
        for f in self.fields:
            res += f.size
        return res
    
    def addfield(self,field):
        self.fields.append(field)

    def addeqn(self,eqn):
        self.eqns.append(eqn)

    # Returns the *mesh* index of this DOF.
    def fieldindex(self,fieldname):
        for d in self.fields:
            if d.name==fieldname:
                return d.index

    def field(self,fieldname):
        for d in self.fields:
            if d.name==fieldname:
                return d

    def eqn(self,eqnname):
        for e in self.eqns:
            if e.name==eqnname:
                return e

# This is a combination of the field and dof functionality in OOF.
# The index is the starting index for this field in the master stiffness
# matrix, and the size is the number of slots it uses.  There is
# one of these objects per node.
class Field:
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
        return "Field(%s,%d,%d)" % (self.name, self.index, self.size)

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
    def make_linear_system(self, mesh, element, ndx, gpt, flux_vector,
                           flux_dofderivs,fmap,flux_dofderivsg):
        jvec = [0,0,0,1,1,1,2,2,2]
        for fxcomp in range(self.flux.dim):
            row = self.index+flux.t_row[fxcomp]
            j = flux.t_col[fxcomp]
            
            res = element.dshapefn(ndx,j,gpt.xi,gpt.zeta,gpt.mu)
            
            res *= (-1.0)*element.jacobiandef(gpt.xi,gpt.zeta,gpt.mu)*gpt.weight


######### eqval is the equation value to calculate the residual stresses
            eqval = res*flux_vector[fxcomp]
            try:
                mesh.eqns[row] += eqval
                
            except KeyError:
                mesh.eqns[row] = eqval
            for fxcol in range(len(fmap)):
                col = fmap[fxcol]
                cres = res * flux_dofderivs[fxcomp][fxcol]

                try:
                    mesh.matrix[(row,col)] += cres
                    
                except KeyError:
                    mesh.matrix[(row,col)] = cres



        for fxcomp in range(self.flux.dim):
            
            rowg = self.index+flux.t_colg[fxcomp]
            jg = flux.t_rowg[fxcomp]


            resg = element.dshapefn(ndx,jg,gpt.xi,gpt.zeta,gpt.mu)
            

            resg *= (-1.0)*element.jacobiandef(gpt.xi,gpt.zeta,gpt.mu)*gpt.weight


            for fxcol in range(len(fmap)):
                col = fmap[fxcol]
                cresg = resg * flux_dofderivsg[fxcomp][fxcol]

                mesh.matrix[(rowg,col)] += cresg




        

# Hexahedral eight-node shape functions.  Coords are xi, zeta, mu..
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
        self.f_cache = {}
        self.fdx_cache = {}
        self.dshapefn_cache = {}
        self.material = None
    def __repr__(self):
        return "Element(%d,%s)" % (self.index, self.nodes)
    # Evaluate a shape function at a master-space coordinate
    def clear_caches(self):
        self.frommaster_cache = {}
        self.f_cache = {}
        self.fdx_cache = {}
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

#******************************shahriyar**********************************************
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



    # Get number of field components.
    def nfieldcomps(self):
        ftotal = 0
        for n in self.nodes:
            ftotal += n.nfieldcomps()
        return ftotal
            
    # Evaluate an arbitrary field at a given master-space position.
    # Always returns a list, even for scalar fields.
    def field(self,fname,xi,zeta,mu):
        try:
            return self.f_cache[(fname,xi,zeta,mu)][:]
        except KeyError:
            res = None
            for (ni,n) in enumerate(self.nodes):
                sfval = self.shapefn(ni,xi,zeta,mu)
                for f in n.fields:
                    if f.name == fname:
                        term = [sfval*x for x in f.value]
                        if res==None:
                            res = term
                        else:
                            res = [sum(x) for x in zip(res,term)]
            self.f_cache[(fname,xi,zeta,mu)]=res
            return res[:]

    # Return the reference-state derivatives of a field at a given
    # master-space position.  Always returns a list of lists, with the
    # component of the derivative being the fastest-varying thing.
    def fielddx(self,dofname,xi,zeta,mu):
        try:
            return [x[:] for x in self.fdx_cache[(dofname,xi,zeta,mu)]]
        except KeyError:
            res = None
            for (ni,n) in enumerate(self.nodes):
                
                dsf = [ self.dshapefn(ni,0,xi,zeta,mu),
                        self.dshapefn(ni,1,xi,zeta,mu),
                        self.dshapefn(ni,2,xi,zeta,mu) ]
                
                for f in n.fields:
                    if f.name == dofname:
                        term = [[ df*x for x in f.value ] for df in dsf ]
                        if res == None:
                            res = term
                        else:
                            res = [[sum(y) for y in zip(x[0],x[1])]
                                   for x in zip(res,term)]
            self.fdx_cache[(dofname,xi,zeta,mu)]=res
             
            return [x[:] for x in res]
                        
    # The master-to-reference transformation.
    def frommaster(self,xi,zeta,mu):
        try:
            return self.frommaster_cache[(xi,zeta,mu)].clone()
        except KeyError:
            
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

################################ added by Shahriyar #################
    # Jacobian of the master-to-reference transformation.
    def jacobianmtxdef(self,xi,zeta,mu):

        j11 = j12 = j13 = j21 = j22 = j23= j31 = j32 = j33 = 0.0

        j11 = sum( [ self.dsfns[i][0](xi,zeta,mu)*(self.nodes[i].position.x
                     + self.nodes[i].fields[0].value[0]) for i in range(8)] )
        j12 = sum( [ self.dsfns[i][1](xi,zeta,mu)*(self.nodes[i].position.x
                     + self.nodes[i].fields[0].value[0]) for i in range(8)] )
        j13 = sum( [ self.dsfns[i][2](xi,zeta,mu)*(self.nodes[i].position.x
                     + self.nodes[i].fields[0].value[0]) for i in range(8)] )

        j21 = sum( [ self.dsfns[i][0](xi,zeta,mu)*(self.nodes[i].position.y
                     + self.nodes[i].fields[0].value[1]) for i in range(8)] )
        j22 = sum( [ self.dsfns[i][1](xi,zeta,mu)*(self.nodes[i].position.y
                     + self.nodes[i].fields[0].value[1]) for i in range(8)] )
        j23 = sum( [ self.dsfns[i][2](xi,zeta,mu)*(self.nodes[i].position.y
                     + self.nodes[i].fields[0].value[1]) for i in range(8)] )

        j31 = sum( [ self.dsfns[i][0](xi,zeta,mu)*(self.nodes[i].position.z
                     + self.nodes[i].fields[0].value[2]) for i in range(8)] )
        j32 = sum( [ self.dsfns[i][1](xi,zeta,mu)*(self.nodes[i].position.z
                     + self.nodes[i].fields[0].value[2]) for i in range(8)] )
        j33 = sum( [ self.dsfns[i][2](xi,zeta,mu)*(self.nodes[i].position.z
                     + self.nodes[i].fields[0].value[2]) for i in range(8)] )

#        return [ [ j11, j12, j13], [j21, j22, j23], [j31, j32, j33] ]
        return [ [ j11, j21, j31], [j12, j22, j32], [j13, j23, j33] ]

#------------------ added by shahriyar -----------------
    def jacobiandef(self,xi,zeta,mu):
        return det3(self.jacobianmtxdef(xi,zeta,mu))
#------------------ added by shahriyar -----------------

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

    def addmaterial(self,mtl):
        self.material = mtl
    def make_linear_system(self, mesh):
        print "Element...."
        self.material.begin_element(self)
        for g in self.gausspts():
            self.material.make_linear_system(mesh, self, g) 
        self.material.end_element(self)

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
# and iterate until either the increment is small enough, the
# residual is small enough, or the allowed iteration count is
# exceeded.


class Mesh:
    def __init__(self,xelements=5,yelements=5,zelements=5):
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
        
        self.fieldlist = []
        self.eqnlist = []
        self.freedofs = [] # Index list, doesn't actually contain dofs.
        
        # Master stiffness matrix is a dictionary indexed by tuples of
        # integers, whose values are floating-point numbers.

        self.matrixg = {}

        
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
        # list position (c*(xelements+1)+b)*(yelements+1)+a
                    
        

        element_index = 0
        face_index = 0
        for i in range(zelements):
            for j in range(yelements):
                for k in range(xelements):
                    np0 = (i*(xelements+1)+j)*(yelements+1)+k
                    np1 = ((i+1)*(xelements+1)+j)*(yelements+1)+k
                    np2 = (i*(xelements+1)+(j+1))*(yelements+1)+k
                    np3 = ((i+1)*(xelements+1)+(j+1))*(yelements+1)+k
                    
                    np4 = (i*(xelements+1)+j)*(yelements+1)+k+1
                    np5 = ((i+1)*(xelements+1)+j)*(yelements+1)+k+1
                    np6 = (i*(xelements+1)+(j+1))*(yelements+1)+k+1
                    np7 = ((i+1)*(xelements+1)+(j+1))*(yelements+1)+k+1

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

    def addmaterial(self,mtl):
        # For the future, different elements can have different materials.
        for e in self.elementlist:
            e.addmaterial(mtl)
        
    # Add a new field to be solved for. 
    def addfield(self, name, size, value=None):
        mtxsize = sum( [d.size for d in self.fieldlist] )
        count = 0
        for n in self.nodelist:
            newf = Field(name, mtxsize+count*size, size)
            if value is not None:
                for i in range(len(value)):
                    newf.set(i,value[i])
            n.addfield(newf)
            self.fieldlist.append(newf)
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
        self.matrixg = {}
        
        self.matrix = {}
        self.fbody = {}
        self.eqns = {}
        self.freedofs = []


    # Reset is like clear, but also removes all the fields and
    # equations.  There is no facility for selectively removing
    # fields.
    def reset(self):
        self.clear()
        self.fieldlist = []
        self.eqnlist = []
        for n in self.nodelist:
            n.fields = []

    # Build the flux-divergence contributions to the stiffness matrix.
    # In OOF, individual properties do this, but this is not OOF, it
    # is merely OOFoid.  It could eventually be OOFtacular.  What it
    # actually does is populate a dictionary indexed by (row,col)
    # tuples.  Note that this process populates the mesh's .matrix and
    # .eqns objects with the appropriate data, suitable for
    # Newton-Raphson iteration.  You may still want to evaluate the
    # equations separately to check convergence, and having done so,
    # might not want this process to do it again, because it's
    # redundant. Optimize this later.
    def new_make_stiffness(self):
        for e in self.elementlist:
            e.make_linear_system(self)

        
        
    # Build the flux-divergence contributions to the stiffness matrix.
    # In OOF, individual properties do this, but this is not OOF, it
    # is merely OOFoid.  It could eventually be OOFtacular.  What it
    # actually does is populate a dictionary indexed by (row,col)
    # tuples.

    def make_stiffness(self):
        for e in self.elementlist:
            print "Element...."
            for (rndx,rn) in enumerate(e.nodes): # "Row" nodes.
                for eq in rn.eqns:
                    for i in range(eq.size):
                        row = eq.index+i
                        for (cndx,cn) in enumerate(e.nodes):  # "Column" nodes.
                            for df in cn.fields:
                                for j in range(df.size):
                                    col = df.index+j
                                    # Now we have (row,col) for the matrix.
                                    # Compute the integrand.
                                    val = 0.0
                                    for g in e.gausspts():
                                        dval = self._flux_deriv(
                                            e, rndx, cndx, eq, i,
                                            df, j, g)
                                        # 
                                        dval *= g.weight
                                        dval *= e.jacobian(g.xi,g.zeta,g.mu)
                                        val += dval
                                    try:
                                        self.matrix[(row,col)] += val
                                    except KeyError:
                                        self.matrix[(row,col)] = val


    def _flux_deriv(self, element, rndx, cndx, eqn, eqcomp,
                    field, fieldcomp, gpt):
        # We are inside most of the matrix loops, including the
        # gausspoint loop. Take the derivative.
        # Rndx is the element's index of the shapefunction for the row.
        # Cndx is the element's index of the shapefunction for the column.
        # Eqn is the equation object, eqncomp the component.
        # Field is the field object, fcomp the component.
        # Gpt is the gausspoint, pos the reference-state position of it.

        pos = element.frommaster(gpt.xi,gpt.zeta,gpt.mu)
        fval = element.field(field.name, gpt.xi,gpt.zeta,gpt.mu)
        fderivs = element.fielddx(field.name, gpt.xi,gpt.zeta,gpt.mu)

        # In principle, we could check metadata here, to make sure
        # that the flux we are calling contributes to the equation
        # we're working on, and understands teh DOF we're passing in.
        # However, for this prototype, all DOFs are displacement, and
        # all equations are force-balance.

        # Pre-compute the flux derivatives.
        fluxdvs = [ eqn.flux.dukl(fieldcomp,l,
                                  pos,fval,fderivs) for l in range(3) ]
        res = 0.0
        
        for j in range(3):
            for l in range(3):
                res -= element.dshapefn(rndx,j,gpt.xi,gpt.zeta,gpt.mu)*\
                       fluxdvs[l][eqcomp][j]*\
                       element.dshapefn(cndx,l,gpt.xi,gpt.zeta,gpt.mu)
        return res
            
    
    # Function for computing the value of each of the equations for
    # the current degrees of freedom.  Needed by the Newton-Raphson
    # solver.  Just does a straightforward integral.  Note that the
    # value of the equation and the value of the flux are not the same
    # thing.  Populates the self.eqns attribute.
    def evaluate_eqns(self):
        for e in self.elementlist:
            for (mudx,mu) in enumerate(e.nodes):
                for eq in mu.eqns:
                    for i in range(eq.size):
                        row = eq.index+i
                        val = 0.0
                        for g in e.gausspts():
                            dval = self._flux_contrib(
                                e, mudx, eq, i, g)
                            dval *= g.weight
                            dval *= e.jacobian(g.xi,g.zeta,g.mu)
                            val += dval
                        try:
                            self.eqns[row]+=val
                        except KeyError:
                            self.eqns[row]=val

        # Build the Smallmatrix version of it.  Assumes conjugacy.
        # Also, call to set_freedofs is duplicated in linearsystem.
        (free_count,fixed_count, fixed_rhs) = self.set_freedofs()
        eqvs = SmallMatrix(free_count,1)
        for (i,v) in self.eqns.items():
            if self.freedofs[i]>0:
                eqvs[self.freedofs[i],0]=v
        return eqvs
        
    def _flux_contrib(self, element, rndx, eqn, eqndx, gpt):
        # This is essentially the integrand function for the equation
        # values. It assumes a divergence flux, and includes
        # contributions from the derivative of the row shape function,
        # and the negative sign from the integration by parts.

        pos = element.frommaster(gpt.xi,gpt.zeta,gpt.mu)

        fname = eqn.flux.fieldname # Assume there's only one, for now.
        fval = element.field(fname,gpt.xi,gpt.zeta,gpt.mu)
        fderivs = element.fielddx(fname,gpt.xi,gpt.zeta,gpt.mu)
        res = 0.0
        for j in range(3):
            res -= element.dshapefn(rndx,j,gpt.xi,gpt.zeta,gpt.mu)*\
                   eqn.flux.value(eqndx,j,pos,fval,fderivs)
        return res
                                                    
    # Values are z offsets of the top and bottom boundaries, which are
    # assumed fixed to zero offset in the x and y direction.  BCs can
    # be set to None, in which case they are not fixed, but why woold
    # you do that?  The field must already be added before you do
    # this.
    def setbcs(self,top,bottom):
        self.topbc = top
        self.bottombc = bottom
        if self.topbc is not None:
            for n in self.topnodes:
                d = n.fields[0] # Assume only displacement exists.
                d.set(0,0)
                d.set(1,0)
                d.set(2,self.topbc)
        if self.bottombc is not None:
            for n in self.bottomnodes:
                d = n.fields[0] # Assume only displacement exists.
                d.set(0,0)
                d.set(1,0)
                d.set(2,self.bottombc)

    def new_setbcs(self,top,bottom):
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
        mtxsize = sum( [d.size for d in self.fieldlist] )
        self.freedofs = [-1]*mtxsize
        fixed_rhs = []
        for node in self.nodelist:
            for f in node.allfields():
                add = False # Add to free DOF list?
                if f.name!="Displacement":
                    add = True # All non-displacement DOFs are free.
                else: # f.name *is* "Displacement"
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
                    for k in range(f.index, f.index+f.size):
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
        
        amtx.clear()
        cmtx.clear()
        brhs.clear()
        frhs.clear()

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

        return (amtx,cmtx,brhs,frhs)

#----------------- added by shahriyar ----------------------
    def new_linearsystem(self):
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

#----------------- added by shahriyar ----------------------


    
    # Assumes the "Displacement" field has been added to the mesh, and
    # the appropriate equations and the bcs are set. Builds the big
    # master stiffness matrix.
    def solve_linear(self):
        self.make_stiffness()
        
        (a,c,br,fr) = self.linearsystem()

        # Sign.  Solver solves Ax=b, not Ax+b=0.
        nr = (c*br)*(-1.0)-fr # Fr is zero if no Neumann BCs.

        if a.rows()!=0:
            rr = a.solve(nr)
        else:
            rr = 0 # Degenerate case, set to "solved". 

        if rr==0:
            for n in self.nodelist:
                for d in n.allfields():
                    for k in range(d.size):
                        ref = self.freedofs[d.index+k]
                        if ref >= 0:
                            d.set(k,nr[ref,0])
                        else:
                            d.set(k,br[-(ref+1),0])  # Should be redundant.
        else:
            raise Oops("Error in linear solver, return code is %d." % rr)


    # Arguments are the residual tolerance, the increment tolerance,
    # and the maximum number of iterations.  Setting any of these to
    # None means they'll be ignored.
    def solve_nonlinear(self, eps_r, eps_dx, max_count):

        icount = 0

        while 1:
            self.clear()
            self.clear_caches()
            # self.make_stiffness()
            eq = self.evaluate_eqns()

            # nr = (c*br)*(-1.0)-fr-eq
            nr = eq*(-1.0)

            rmag = math.sqrt(sum( nr[i,0]*nr[i,0] for i in range(nr.rows()) )) 
            print "Starting nonlinear iteration, rmag is %f." % rmag

            # If there's a residual criterion, and it's satsified, success.
            if eps_r is not None and math.fabs(rmag)<eps_r:
                return icount

            # If another iteration would exceed the count, fail.
            if icount is not None and icount >= max_count:
                raise Oops("Iteration count %d reached in nonlinear solver."
                           % max_count)

            # We are actually going to do this.  Build and extract the
            # matrix.
            self.make_stiffness()
            (a,c,br,fr) = self.linearsystem()
            
            xmag = self.iterate_nonlinear(a,nr,br)
            icount += 1

            print "Completing nonlinear iteration, xmag is %f." % xmag
            
            # If there's an increment criterion and it's met, success!
            if eps_dx is not None and math.fabs(xmag)<eps_dx:
                return icount
            

    # Performs a single Newton-Raphson iteration, updates the free
    # DOFs in the mesh, and returns the un-normalized L2 norm of the
    # increment vector.
    def iterate_nonlinear(self,a,nr,br):

        if a.rows()!=0:
            rr = a.solve(nr)
        else:
            raise Oops("Zero rows in the A matrix, very odd...")

        if rr==0:
            mag = 0.0
            for n in self.nodelist:
                for d in n.allfields():
                    for k in range(d.size):
                        ref = self.freedofs[d.index+k]
                        if ref >= 0:
                            v = nr[ref,0]
                            mag += v*v
                            d.add(k,v)
                        else:
                            d.set(k,br[-(ref+1),0]) # Should be redundant.
        else:
            raise Oops("Error in nonlinear solver, return code is %d." % rr)
        
        return math.sqrt(mag) # Size of the increment. *Not* the residual.
        


#------------ nol-linear solver added by Shahriyar -------------------
    def new_solve_nonlinear(self):
        (a,c,br,fr,eq) = self.new_linearsystem()


        nr = (c*br)*(-1.0)-fr+eq

        
        if a.rows()!=0:
            rr = a.solve(nr)
        else:
            Oops("Zero rows in the A matrix, very odd...")


        if rr==0:
            mag = 0.0
            for n in self.nodelist:
                for d in n.allfields():
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
##        for n in self.nodelist:
##            print n.index,0,n.fields[0].value[0]
##            print n.index,1,n.fields[0].value[1]
##            print n.index,2,n.fields[0].value[2]
##
##        raw_input()

 
#--------- start convergence loop -----------------------

        iconv = 0
        nconv = 2
        ratio_norm = 1.0e10
        magiter = [0.0 for i in range(nconv)]
        while (iconv <= nconv-1 and abs(ratio_norm) >= 1.0e-9):
            if iconv > 0:

                (a,c,br,fr,eq) = self.new_linearsystem()

                nr = eq

                if a.rows()!=0:
                    rr = a.solve(nr)
                else:
                    Oops("Zero rows in the A matrix, very odd...")

                if rr==0:
                    for n in self.nodelist:
                        for d in n.allfields():
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
#            self.evaluate_eqns()

            self.matrix = {}
            self.clear_caches()
            self.new_make_stiffness()            



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
#---------------------- added by sShahriyar ----------------------------













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
                fval = f.element.field("Displacement",
                                       g.xi,g.zeta,-1.0)
                fderivs = f.element.fielddx("Displacement",
                                            g.xi,g.zeta,-1.0)
                # Only want the z components.  The "None" argument is
                # for the position, we don't care for now.
                fvec = [ flux.value(i,2,None,fval,fderivs)
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
                    disp_idx = n.field("Displacement")
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
                    



# The general scheme is, you create a mesh, add a field, maybe add
# some equations with associated fluxes, build the matrix and
# right-hand side, which calls out to the flux objects for their
# derivatives and values, and then solve.  You can write the solution
# back into the mesh (for iterating, of course) using the Dof "set"
# method.

def displaced_drawing_test():
    m = Mesh(xelements=4,yelements=4,zelements=4)
    m.addfield("Displacement",3)
    
    for n in m.nodelist:
        p = n.position
        dp = [0,0,p.z*0.1]
        df = n.field("Displacement")
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


def rotest_iterate(ro,du,cpi,cpj):
    # Ro is the property, du is a starting displacement derivative
    # field, and component is a tuple of integers indicating which
    # "direction" to take the derivative.a
    delta = 0.0005
    #
    delta_du = [ [ 0.0 for j in range(3) ] for i in range(3) ]
    delta_du[cpi][cpj] += delta
    #
    du2 = [ [ du[i][j] +delta_du[i][j] for j in range(3) ] for i in range(3) ]
    #
    # The scheme is to compute stress(du), stress(du2), and
    # stress(du)+delta-du*dstress(du)/du, and compare.
    stss_1 = ro.value(cpi,cpj,None,None,du)
    stss_2 = ro.value(cpi,cpj,None,None,du2)
    
    # We want the derivative of stress[i][j], and we want all k,l
    # components of it.
    dukl = [ [ ro.dukl(cpk,cpl,None,None,du)[cpi][cpj]
               for cpl in range(3) ] for cpk in range(3)]
    stss_2a = stss_1+sum(sum(dukl[k][l]*delta_du[k][l]
                             for l in range(3)) for k in range(3))
    print stss_1,stss_2,stss_2a
    print (stss_2-stss_2a)/stss_2
    
def rotest():
    # It's safe to pass in None for the pos and dofval arguments to
    # the RO value and dukl routines, because those arguments are
    # ignored.
    ro = RambergOsgood("RO") # Use defaults.
    du1 = [[0.1, 0.3,0.5],[0.1,0.0,0.1],[0.0,0.0,0.5]]
    delta = 0.001
    for cpi in range(3):
        for cpj in range(3):
            rotest_iterate(ro,du1,cpi,cpj)
    


class Material:
    def __init__(self, name, flux=None, orientation=None):
        self.name = name
        self.flux = flux
        if orientation is not None:
            orientation = Orientation(0.0,0.0,0.0)#35.0,45.0)
        self.orientation = orientation      
    def get_flux(self):
        return self.flux
    def precompute(self):
        if self.orientation is not None:        
            omx = self.orientation.rotation
            self.flux.rotate(omx)

    def begin_element(self,element):
        pass
    def end_element(self,element):
        pass
    def make_linear_system(self, mesh, element, gausspt):
        #
        # This routine populates the self.matrix and self.eqn objects
        # in the mesh, so they'd better be cleared before you start.

#**************************** shahriyar **************************************
        # umat is called at this point to calculate and return elasto-plastic modulus
        # (Dep) and cauchy stresses (Castress) which are need to make stiffness matrix. The elasto-plastic
        # modulus is used to make the material part of stiffness matrix while the
        # Cauchy stresses mkae the geometric part of the stiffness matrix.
        
        Dep = [[[[0.0 for i in range(3)] for j in range(3) ]
                  for k in range(3)] for l in range(3)]
        CaStress = [[0.0 for i in range(3)] for j in range(3)]

        XYZ = [[0.0 for i in range(3)] for j in range(8)]
        xyz = [[0.0 for i in range(3)] for j in range(8)]

        for (rrndx,rrn) in enumerate(element.nodes):
            XYZ[rrndx][0] = rrn.position.x
            XYZ[rrndx][1] = rrn.position.y
            XYZ[rrndx][2] = rrn.position.z

            xyz[rrndx][0] = rrn.position.x + rrn.fields[0].value[0]
            xyz[rrndx][1] = rrn.position.y + rrn.fields[0].value[1]
            xyz[rrndx][2] = rrn.position.z + rrn.fields[0].value[2]

        SHP = element.dshapefnRef(gausspt.xi,gausspt.zeta,gausspt.mu)
        
        FG = calc_F(xyz,SHP)            # F at gausspoint

        umat(element,gausspt,Dep,CaStress,self.flux.cijkl,FG)
#*****************************************************************************        
        # Iterate over fluxes, but there's only one.
        cols = element.nfieldcomps()
        rows = self.flux.dim
        
        #
        # TODO: Look at the flux class, clear up "offset" vs "value".
        flux_vector = [0.0]*rows
        #
        flux_fderivs = [ [0.0]*cols for i in range(rows)]
        flux_fderivsg = [ [0.0]*cols for i in range(rows)]
        
        #
        fmap = [0]*cols # Map from local to global columns.
        # Fmap is the mapping from local flux matrix columns to the
        # global stiffness matrix columns, and gets populated by
        # the flux_matrix call.
        
        self.flux.flux_matrix(element, gausspt, flux_vector,
                              flux_fderivs, fmap,Dep,CaStress,flux_fderivsg)

        t_row = [0,1,2,1,0,0,1,2,2]
        t_col = [0,1,2,2,2,1,0,0,1]

        for flux_comp in range(len(flux_fderivs)):
            flux_vector[flux_comp] = CaStress[t_row[flux_comp]][t_col[flux_comp]]

#        self.flux.flux_vector(element, gausspt, flux_vector, flux_fderivs)
        #
        for (ndx,nd) in enumerate(element.nodes):
            for eqn in nd.eqns:
                eqn.make_linear_system(mesh, element, ndx, gausspt,
                                       flux_vector, flux_fderivs,fmap,flux_fderivsg)
############## shahriyar #################
def calc_F(cord,SHP):

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
############## shahriyar #################

                
if __name__=="__main__":
    m = Mesh(xelements=2,yelements=2,zelements=2)
#    f = flux.CauchyStress("Stress")
    f = CauchyStress("Stress") #Cachystress is imported here

#    f = flux.RambergOsgood("Nonlinear!",alpha=0.05)
#    mtl = Material("Stuff",f,None) # TODO: Add orientation.    

    mtl = Material("Stuff",f,0) # TODO: Add orientation.
    mtl.precompute() 

    m.addmaterial(mtl)
    
    m.addfield("Displacement",3)
    m.addeqn("Force",3,f) # Last argument is the flux.
##############    m.setbcs(0.1,0.0)

    # m.solve_linear()

    m.clear()
    m.clear_caches()

#    m.new_make_stiffness()

##    print m.matrix
##    raw_input()
##    
##    m.clear()
##    m.clear_caches()
##    m.make_stiffness()
##
##    print m.matrix
    # try:
    #     m.solve_nonlinear(None,None,5)
    # except Oops, o:
    #     print "Got exception, ", o
    # force_val = m.measure_force(f)
    # print force_val

    # m.draw(displaced=True)

    nstep = 2
    m.new_make_stiffness()



##    SS0 = m.evaluate_ss()
##    x = [] ; y = []
##    x.append(SS0[0]) ; y.append(SS0[1])


##    ssy = open('py.22','w')

##    ssy.write("%f   %f" % (SS0[0],SS0[1]))
##    ssy.write('\n')

    for istep in range(nstep):

    
        m.new_setbcs(0.05,0.0)
        m.new_solve_nonlinear()


##        for n in m.nodelist:
##            print n.index,0,n.dofs[0].value[0]
##            print n.index,1,n.dofs[0].value[1]
##            print n.index,2,n.dofs[0].value[2]
##        raw_input()




##        SS = m.evaluate_ss()
##        print SS
##        x.append(abs(SS[0])) ; y.append(SS[1])
##
##        ssy.write("%f   %f" % (abs(SS[0]),SS[1]))
##        ssy.write('\n')
##
##    ssy.close()
##    
