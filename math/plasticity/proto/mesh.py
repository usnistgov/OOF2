# -*- python -*-
# $RCSfile: plasticity.py,v $
# $Revision: 1.26 $
# $Author: snk6 $
# $Date: 2015/01/22 14:21:14 $

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


import math, sets, string, sys, getopt

import smallmatrix
import position

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
        self.elements = sets.Set()

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
        res = self.dofs[:]
        for v in self.eldofs.values():
            res+=v
        return res

    def adddof(self,dof):
        self.dofs.append(dof)

    def addeqn(self,eqn):
        self.eqns.append(eqn)
            
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
def dfs1d2(xi,zeta,mu):
    return +0.125*(xi-1.0)*(zeta-1.0)

def dsf2d0(xi,zeta,mu):
    return +0.125*(zeta+1.0)*(mu-1.0)
def dsf2d1(xi,zeta,mu):
    return +0.125*(xi-1.0)*(mu-1.0)
def dfs2d2(xi,zeta,mu):
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
        self.sfns = [sf0,sf1,sf2,sf3,qsf4,sf5,sf6,sf7]
        self.dsfns = [[dsf0d0,dfs0d1,dsf0d2],
                      [dsf1d0,dsf1d1,dsf1d2],
                      [dfs2d0,dsf2d1,dsf2d2],
                      [dsf3d0,dsf3d1,dsf3d2],
                      [dsf4d0,dfs4d1,dsf4d2],
                      [dsf5d0,dsf5d1,dsf5d2],
                      [dsf6d0,dsf6d1,dsf6d2],
                      [dsf7d0,dsf7d1,dsf7d2]]
        for n in self.nodes:
            n.add_element(self)
    def __repr__(self):
        return "Element(%d,%s)" % (self.index, self.nodes)
    # Evaluate a shape function at a master-space coordinate.
    def shapefn(self,i,xi,zeta,mu):
        return self.sfns[i](xi,zeta,mu)
    # Derivative of shape function i wrt component j in master space.
    def masterdshapefn(self,i,j,xi,zeta,mu):
        return self.dsfns[i][j](xi,zeta,mu)
    # Reference-space derivative of the shape function i wrt ref component j.
    def dshapefn(self,i,j,xi,zeta,mu):
        jmtx = self.jacobianmtx(xi,zeta,mu)
        jinv = inverse3(jmtx)

        dfdmaster = [ self.dsfns[i][0](xi,zeta,mu),
                      self.dsfns[i][1](xi,zeta,mu),
                      self.dsfns[i][2](xi,zeta,mu) ]

        dfdref = [ sum( jinv[ix][jx]*dfdmaster[jx] for jx in range(3) )
                   for ix in range(3) ]
        return dfdref[j]
        
    # The master-to-reference transformation.
    def frommaster(self,xi,zeta,mu):
        xpos = sum( [self.sfns[i](xi,zeta,mu)*self.nodes[i].position.x
                     for i in range(8)] )
        ypos = sum( [self.sfns[i](xi,zeta,mu)*self.nodes[i].position.y
                     for i in range(8)] )
        zpos = sum( [self.sffns[i](xi,zeta,mu)*self.nodes[i].position.z
                     for i in range(8)] )
        return Position(xpos,ypos,zpos)
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

        return [ [ j11, j12, j13], [j21, j22, j23], [j31, j32, j33] ]
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
                        Element.gptable.append(
                            GaussPoint(pts[k],pts[j],pts[i],
                                       wts[k]*wts[j]*wts[i]))
        return Element.gptable


# A flux is a thing that has zero divergence in equilibrium.
# Components of the divergence of the flux at a given node correspond
# to Eqn objects.
class Flux:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "Flux(%s)" % self.name
    


# TODO: Figure out the right flux structure..
class Mesh:
    def __init__(self,xelements=5,yelements=5,zelements=5):
        self.nodelist = []
        self.ellist = []

        # Boundaries to which rather primitive conditions can be
        # applied.
        self.topnodes = []
        self.bottomnodes = []

        dx = 1.0/xelements
        dy = 1.0/yelements
        dz = 1.0/zelements
        
        self.doflist = []
        self.eqnlist = []
        self.freedofs = [] # Index list, doesn't actually contain dofs.
        
        # Master stiffness matrix is a dictionary indexed by tuples of
        # integers, whose values are floating-point numbers.
        self.matrix = {}
        self.rhs = {}
        
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
        for i in range(zelements):
            for j in range(yelements):
                for k in range(xelements):
                    np0 = (i*(zelements+1)+j)*(yelements+1)+k
                    np1 = ((i+1)*(zelements+1)+j)*(yelements+1)+k
                    np2 = (i*(zelements+1)+(j+1))*(yelements+1)+k
                    np3 = ((i+1)*(zelemenets+1)+(j+1))*(yemenets+1)+k
                    
                    np4 = (i*(zelements+1)+j)*(yelements+1)+k+1
                    np5 = ((i+1)*(zelements+1)+j)*(yelements+1)+k+1
                    np6 = (i*(zelements+1)+(j+1))*(yelements+1)+k+1
                    np7 = ((i+1)*(zelemenets+1)+(j+1))*(yemenets+1)+k+1

                    nodes = [self.nodelist[np0],self.nodelist[np1],
                             self.nodelist[np2],self.nodelist[np3],
                             self.nodelist[np4],self.nodelist[np5],
                             self.nodelist[np6],self.nodelist[np7]]
                    self.ellist.append(Element(element_index,nodes))
                    element_index += 1

    # Add a new field to be solved for.  For now, we just assume that
    # there is a corresponding equation for each DOF, and that it has
    # the same index.  Value, if supplied, must be a list, even for
    # scalar DOFs.
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

    # Equations don't take values.
    def addeqn(self, name, size):
        mtxsize = sum( [e.size for e in self.eqnlist] )
        count = 0
        for n in self.nodelist:
            neweqn = Eqn(name, mtxsize+count*size,size)
            n.addeqn(neweqn)
            self.eqnlist.append(neweqn)
            count += 1

    def clear(self):
        self.matrix = {}
        self.rhs = {}
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
    # is merely OOFoid.  It could eventually be OOFtacular.
    def make_linear_system(self):
        for e in self.ellist:
            ndset = [(ii,e.nodes[ii]) for ii in range(len(e.nodes))]
            for (rndx,rn) in ndset: # "Row" nodes.
                for eq in rn.eqns:
                    for i in range(eq.size):
                        row = eq.index+i
                        for (cndx,cn) in ndset:  # "Column" nodes.
                            for df in cn.dofs:
                                for j in range(df.size):
                                    col = df.index+j
                                    # Now we have (row,col) for the matrix.
                                    # Compute the integrand.
                                    val = 0.0
                                    for g in e.gassupts():
                                        pos = e.frommaster(g.xi,
                                                           g.zeta,
                                                           g.mu)
                                        dval = 0.0
                                        e.flux.dukl(i,j,k,l,pos,
                                        # HERE Do the right thing.
                                        # for each DOF component,
                                        # for each derivative direction
                                        # compute flux divergence contrib...
                                        dval *= g.weight
                                        dval *= e.jacobian(g.xi,g.zeta,g.mu)
                                        val += dval
                                    try:
                                        self.matrix[(row,col)] += val
                                    except KeyError:
                                        self.matrix[(row,col)] = val


                                    

    def elastic(self,cijkl):
        for e in self.ellist:
            ndset = [(ii,e.nodes[ii]) for ii in range(len(e.nodes))]
            for (mudx,mu) in ndset:
                for i in range(2): 
                    row = mu.dofindex("Displacement")+i
                    for (nudx,nu) in ndset:
                        for k in range(2):
                            col = nu.dofindex("Displacement")+k
                            val = 0.0
                            for g in e.gausspts():
                                for j in range(2):
                                    for l in range(2):
                                        val-=cijkl[i][j][k][l]*e.dshapefn(mudx,j,g.xi,g.zeta)*e.dshapefn(nudx,l,g.xi,g.zeta)*g.weight*e.jacobian(g.xi,g.zeta)
                            try:
                                self.matrix[(row,col)]+=val
                            except KeyError:
                                self.matrix[(row,col)]=val
                    # RHS contribution.
                    val = 0.0
                    for (nudx,nu) in ndset:
                        pstrain = nu.auxel(e,"Plastic Strain")
                        if pstrain is not None:
                            for g in e.gausspts():
                                for j in range(2): # Sum...
                                    for k in range(3):
                                        for l in range(3):
                                            val+=cijkl[i][j][k][l]*pstrain.get(voigt[k][l])*e.shapefn(nudx,g.xi,g.zeta)*e.dshapefn(mudx,j,g.xi,g.zeta)*g.weight*e.jacobian(g.xi,g.zeta)
                    try:
                        self.rhs[row]+=val
                    except KeyError:
                        self.rhs[row]=val


    # Function for computing the value of each of the equations for
    # the current degrees of freedom.  Needed by the Newton-Raphson
    # solver, we think.
    def phi(self,cijkl,yfunc):
        phi = {}
        for e in self.ellist:
            ndset = [(ii,e.nodes[ii]) for ii in range(len(e.nodes))]
            for g in e.gausspts():

                # Preliminary: Compute stress and pcp at this gauss point.

                gstrain = [[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
                epval = [[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
                epival = [[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
                pcpval = 0.0

                for (mudx,mu) in ndset:
                    disp = mu.dof("Displacement")
                    for k in range(2):
                        for l in range(2):
                            gstrain[k][l] += 0.5*(disp.get(k)*e.dshapefn(mudx,l,g.xi,g.zeta)+disp.get(l)*e.dshapefn(mudx,k,g.xi,g.zeta))
                    ep = mu.auxel(e,"Plastic Strain")
                    if ep is not None:
                        for k in range(3):
                            for l in range(3):
                                epval[k][l] += ep.get(voigt[k][l])*e.shapefn(mudx,g.xi,g.zeta)
                    epi = mu.eldof(e,"Plastic Strain Increment")
                    if epi is not None:
                        for k in range(3):
                            for l in range(3):
                                epival[k][l] += epi.get(voigt[k][l])*e.shapefn(mudx,g.xi,g.zeta)
                    pcp = mu.eldof(e,"Plastic Consistency Parameter")
                    if pcp is not None:
                        pcpval += pcp.get(0)*e.shapefn(mudx,g.xi,g.zeta)

                # Now we have all the strains, we know what to do.
                stress = [ [ sum([ sum([ cijkl[i][j][k][l]*(gstrain[k][l]-epval[k][l]-epival[k][l]) for l in range(3) ]) for k in range(3)]) for j in range(3) ] for i in range(3) ]

                # At this point, stress, epival, and pcpval are all
                # set for this gauss point.

                for (mudx,mu) in ndset:
                    
                    # Elastic equations.
                    for i in range(2):
                        row = mu.dofindex("Displacement")+i
                        val = 0.0
                        for j in range(2):
                            val -= e.dshapefn(mudx,j,g.xi,g.zeta)*stress[i][j]

                        val *= g.weight*e.jacobian(g.xi,g.zeta)
                        try:
                            phi[row]+=val
                        except KeyError:
                            phi[row]=val
                    
                    # Plastic consistency paramter equation.
                    pcp = mu.eldof(e,"Plastic Consistency Parameter")
                    if pcp is not None:
                        row = pcp.index
                        val = e.shapefn(mudx,g.xi,g.zeta)*yfunc.yeeld(stress)
                        val *= g.weight*e.jacobian(g.xi,g.zeta)
                        try:
                            phi[row]+=val
                        except KeyError:
                            phi[row]=val

                    # Consistency criterion.
                    epi = mu.eldof(e,"Plastic Strain Increment")
                    if epi is not None:
                        dy = yfunc.dyeeld(stress)
                        for i in range(3):
                            for j in range(i+1):
                                row = epi.index+voigt[i][j]
                                val = e.shapefn(mudx,g.xi,g.zeta)*(pcpval*dy[i][j] - epival[i][j])
                                val *= g.weight*e.jacobian(g.xi,g.zeta)
                                try:
                                    phi[row]+=val
                                except KeyError:
                                    phi[row]=val
        return phi

                                                    
    # Values are y offsets of the top and bottom boundaries, which are
    # assumed fixed to zero offset in the x direction.  If top is
    # None, then the top boundary is not fixed.
    def setbcs(self,top,bottom):
        self.topbc = top
        self.bottombc = bottom


    def set_freedofs(self):
        mtxsize = sum( [d.size for d in self.doflist] )
        self.freedofs = [-1]*mtxsize
        fixed_rhs = []
        for node in self.nodelist:
            for dof in node.alldofs():
                add = False
                if dof.name!="Displacement":
                    add = True
                else: # dof.name *is* "Displacement"
                    if (not (node in self.topnodes) and \
                        not (node in self.bottomnodes)) \
                        or ( (node in self.topnodes) and \
                             self.topbc is None):
                        add = True
                    else: # Fixed DOF, add to fixed-rhs list.
                        fixed_rhs.append(0.0)
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
        # Populates Smallmatrix objects from the dictionary.  BC's
        # live here.
        (free_count, fixed_count, fixed_rhs) = self.set_freedofs()
        
        amtx = SmallMatrix(free_count,free_count)
        cmtx = SmallMatrix(free_count,-(fixed_count+1))
        brhs = SmallMatrix(len(fixed_rhs),1)
        srhs = SmallMatrix(free_count,1)

        amtx.clear()
        cmtx.clear()
        brhs.clear()
        srhs.clear()
    
        for ((i,j),v) in self.matrix.items():
            if self.freedofs[i]>=0 and self.freedofs[j]>=0:
                amtx[self.freedofs[i],self.freedofs[j]]=v
            else:
                if self.freedofs[i]>=0 and self.freedofs[j]<0:
                    cmtx[self.freedofs[i],-(self.freedofs[j]+1)]=v

        for i in range(len(fixed_rhs)):
            brhs[i,0]=fixed_rhs[i]

        for (i,v) in self.rhs.items():
            if self.freedofs[i]>=0:
                srhs[self.freedofs[i],0]=v

        # System to solve is: amtx + cmtx.brhs = srhs
        return (amtx,cmtx,brhs,srhs)


    # Assumes the "Displacement" field has been added to the mesh, but
    # has no other requirements.  Builds the Master Stiffness Matrix,
    # applies boundary conditions, and fills in the displacement DOFs
    # with the resulting solution.
    def solve_elastic(self,cijkl):
        self.clear()
        self.elastic(cijkl)
        (a,c,br,sr) = self.linearsystem()
        nr = (c*br)*(-1.0)-sr # Sign.

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
            print "Error in solving, return code is %d." % rr


    def draw(self):
        import visual
        frame = visual.frame()
        outline = visual.curve(frame=frame,
                               pos=[(0.0,0.0,0.0),(1.0,0.0,0.0),
                                    (1.0,1.0,0.0),(0.0,1.0,0.0),
                                    (0.0,0.0,0.0)],color=visual.color.red)
        for e in self.ellist:
            outline = []
            for n in e.nodes:
                for d in n.dofs:
                    if d.name=="Displacement":
                        outline.append( (n.position.x + d.value[0],
                                         n.position.y + d.value[1],
                                         0.0) )
                        break
                else:
                    outline.append( (n.position.x, n.position.y,0.0) )
            outline.append(outline[0])
            visual.curve(frame=frame,pos=outline)
        return frame


    def dump_matrix(self,outfile):
        mtxsize = sum( [d.size for d in self.doflist] )
        for i in range(mtxsize):
            for j in range(mtxsize):
                try:
                    v = self.matrix[i,j]
                except KeyError:
                    pass
                else:
                    print >> outfile,i,j,v
                    
    # Routine for measuring how much force is exerted in the y
    # direction on the bottom boundary.  The bottom is chosen because,
    # in this rig, it always has a fixed boundary condition.
    def measure_force(self,cijkl):
        # Use three guass-points per segment in the usual way.
        mpt = math.sqrt(3.0/5.0)
        pts = [-mpt, 0.0, mpt]
        wts = [5.0/9.0, 8.0/9.0, 5.0/9.0]
        elcount = len(self.bottomnodes)-1
        force = 0.0
        for e in self.ellist[:elcount]: # Bottom row of elements.
            for (pt,wt) in zip(pts,wts):
                strain = [[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
                for (ndx,nd) in [(ii,e.nodes[ii]) for ii in
                                 range(len(e.nodes))]:
                    disp = nd.dof("Displacement")
                    ux = disp.value[0]
                    uy = disp.value[1]
                    dstrain = [[
                        ux*e.dshapefn(ndx,0,pt,-1.0),
                        0.5*(ux*e.dshapefn(ndx,1,pt,-1.0) +
                             uy*e.dshapefn(ndx,0,pt,-1.0)),
                        0.0],
                               [
                        0.5*(ux*e.dshapefn(ndx,1,pt,-1.0) +
                             uy*e.dshapefn(ndx,0,pt,-1.0)),
                        uy*e.dshapefn(ndx,1,pt,-1.0),
                        0.0],
                               [0.0,0.0,0.0]]
                    dsfstrain = [0,0,0,0,0,0]
                    sfst = nd.auxel(e,"Plastic Strain")
                    if sfst is not None:
                        sfval = e.shapefn(ndx,pt,-1.0)
                        dsfstrain = [ x*sfval for x in sfst.value ]
                        
                    strain = [ [ strain[i][j]+
                                 dstrain[i][j]-
                                 dsfstrain[voigt[i][j]]
                                 for j in range(3) ]
                               for i in range(3) ]
                # Now we have the complete strain at this eval point.
                # Get the stress.
                stress = [ [ sum( [ sum( [
                    cijkl[i][j][k][l]*strain[k][l] for l in range(3) ] )
                                    for k in range(3) ] ) 
                             for j in range(3) ]
                           for i in range(3) ]

                # Relevant force component is the y component of the
                # tensor contracted with a unit vector pointing in the
                # y direction -- this is just the (1,1) component of
                # the tensor.
                force_inc = stress[1][1]
                # print force_inc
                # Last factor is the Jacobian. Since lower boundary is
                # fixed, it's just the ratio of the lengths of the
                # reference interval (2) to the length of the real
                # interval, which is 1/elcount.
                force += force_inc*wt*((1.0/elcount)/2.0)
        return force


    def dump_data(self,cijkl,yld,dxpts=5,dypts=5):
        dx = 2.0/float(dxpts)
        dy = 2.0/float(dypts)
        startx = -1.0+dx/2.0
        starty = -1.0+dy/2.0
        xevalpts = [ startx + i*dx for i in range(dxpts) ]
        yevalpts = [ starty + i*dy for i in range(dypts) ]

        ptset = [ (x,y) for x in xevalpts for y in yevalpts ]

        for e in self.ellist:
            ndset = [(ii,e.nodes[ii]) for ii in range(len(e.nodes))]
            for p in ptset:
                xi = p[0]
                zeta = p[1]
            
                strain = [[0,0,0],[0,0,0],[0,0,0]]
                pstrain = [[0,0,0],[0,0,0],[0,0,0]]
                for (ndx,nd) in ndset:
                    disp = nd.dof("Displacement")
                    ux = disp.value[0]
                    uy = disp.value[1]
                    dstrain = [[
                        ux*e.dshapefn(ndx,0,xi,zeta),
                        0.5*(ux*e.dshapefn(ndx,1,xi,zeta) +
                             uy*e.dshapefn(ndx,0,xi,zeta)),
                        0.0],
                               [
                        0.5*(ux*e.dshapefn(ndx,1,xi,zeta) +
                             uy*e.dshapefn(ndx,0,xi,zeta)),
                        uy*e.dshapefn(ndx,1,xi,zeta),
                        0.0],
                               [0.0,0.0,0.0]]
                    
                    dptstrian = [[0,0,0],[0,0,0],[0,0,0]]
                    sfst = nd.auxel(e,"Plastic Strain")
                    if sfst is not None:
                        sfval = e.shapefn(ndx,xi,zeta)
                        dsfstrain = [ x*sfval for x in sfst.value ]
                        
                        dpstrain = [ [ dsfstrain[voigt[i][j]]
                                       for j in range(3) ]
                                     for i in range(3) ]
                        
                        
                    pstrain = [ [ pstrain[i][j]+dpstrain[i][j]
                                  for j in range(3) ]
                                for i in range(3) ]
                    strain = [ [ strain[i][j]+
                                 dstrain[i][j]
                                 for j in range(3) ]
                               for i in range(3) ]
                # Now we have the strain at this eval point -- get stress.
                stress = [ [ sum( [ sum( [
                    cijkl[i][j][k][l]*(strain[k][l]-pstrain[k][l])
                    for l in range(3) ] )
                                    for k in range(3) ] ) 
                             for j in range(3) ]
                           for i in range(3) ]
                val = math.sqrt((3.0/2.0)*deviator(stress))
                # val = sum( [ stress[i][i] for i in range(3) ] )
                pt = e.frommaster(xi,zeta)
                print 
                print pt.x, pt.y, "Stress: ", stress
                print pt.x, pt.y, "Strain: ", strain
                print pt.x, pt.y, "Plastic: ", pstrain
                
    

    def draw_stress(self,cijkl,dxpts=5,dypts=5):
        import visual
        frame = visual.frame()
        outline = visual.curve(frame=frame,
                               pos=[(0.0,0.0,0.0),(1.0,0.0,0.0),
                                    (1.0,1.0,0.0),(0.0,1.0,0.0),
                                    (0.0,0.0,0.0)],color=visual.color.red)
        
        dx = 2.0/float(dxpts)
        dy = 2.0/float(dypts)
        startx = -1.0+dx/2.0
        starty = -1.0+dy/2.0
        xevalpts = [ startx + i*dx for i in range(dxpts) ]
        yevalpts = [ starty + i*dy for i in range(dypts) ]
        
        data = {}
        for e in self.ellist:
            ndset = [(ii,e.nodes[ii]) for ii in range(len(e.nodes))]
            for xi in xevalpts:
                for zeta in yevalpts:
                    strain = [[0,0,0],[0,0,0],[0,0,0]]
                    for (ndx,nd) in ndset:
                        disp = nd.dof("Displacement")
                        ux = disp.value[0]
                        uy = disp.value[1]
                        dstrain = [[
                            ux*e.dshapefn(ndx,0,xi,zeta),
                            0.5*(ux*e.dshapefn(ndx,1,xi,zeta) +
                                 uy*e.dshapefn(ndx,0,xi,zeta)),
                            0.0],
                                   [
                            0.5*(ux*e.dshapefn(ndx,1,xi,zeta) +
                                 uy*e.dshapefn(ndx,0,xi,zeta)),
                            uy*e.dshapefn(ndx,1,xi,zeta),
                            0.0],
                                   [0.0,0.0,0.0]]
                        dsfstrain = [0,0,0,0,0,0]
                        sfst = nd.auxel(e,"Plastic Strain")
                        if sfst is not None:
                            sfval = e.shapefn(ndx,xi,zeta)
                            dsfstrain = [ x*sfval for x in sfst.value ]
                            
                        strain = [ [ strain[i][j]+
                                     dstrain[i][j]-
                                     dsfstrain[voigt[i][j]]
                                     for j in range(3) ]
                                   for i in range(3) ]
                    # Now we have the strain at this eval point -- get stress.
                    stress = [ [ sum( [ sum( [
                        cijkl[i][j][k][l]*strain[k][l] for l in range(3) ] )
                                        for k in range(3) ] ) 
                                 for j in range(3) ]
                               for i in range(3) ]
                    val = math.sqrt((3.0/2.0)*deviator(stress))
                    # val = sum( [ stress[i][i] for i in range(3) ] )
                    pt = e.frommaster(xi,zeta)
                    data[(pt.x,pt.y)]=val

        # Go through the data and check out the scale.
        vmax = None
        vmin = None
        vsum = 0.0
        count = 0
        for v in data.values():
            vsum += v
            count += 1
            if vmax is None or v > vmax:
                vmax = v
            if vmin is None or v < vmin:
                vmin = v
        print "Min, max, avg: ", vmin, vmax, vsum/float(count)

        # Actually draw stuff.  Assumes undistorted elements are
        # square, which may not be a particularly robust assumption.

        # realdx = 1.0/(math.sqrt(len(self.ellist))*dpts)
        xels = len(self.bottomnodes)-1
        yels = len(self.ellist)/xels
        
        realdx = 1.0/float(xels*dxpts)
        realdy = 1.0/float(yels*dypts)

        for (p,v) in data.items():
            bdy = [ (p[0]-0.5*realdx,p[1]-0.5*realdy),
                    (p[0]+0.5*realdx,p[1]-0.5*realdy),
                    (p[0]+0.5*realdx,p[1]+0.5*realdy),
                    (p[0]-0.5*realdx,p[1]+0.5*realdy)]
            col = (v-vmin)/(vmax-vmin)
            visual.convex(frame=frame,pos=bdy,color=(col,col,col))
        return frame    
            
                    

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

          

# Plastic utility function.
def deviator(stress):
    return sum(
        [ sum( [ stress[i][j]**2 for j in range(3) ] )
          for i in range(3) ] ) - \
         (1.0/3.0)*(sum([ stress[i][i] for i in range(3)])**2)




def go(size):
    global m 
    y = Yeeld(0.1)
    c = Cijkl(0.5,0.25)
    m = Mesh(xelements=size,yelements=size)
    m.addfield("Displacement",2)
    m.addauxelfield("Plastic Strain",6,[0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    for x in range(36):
        bcval = x*0.01
        # bcval = 0.180+x*0.002
        m.setbcs(bcval,0.0)
        m.solve_plastic(c,y)
        # m.dump_data(c,y)
        # for e in m.ellist:
        #     for n in e.nodes:
        #         ep = n.auxel(e,"Plastic Strain")
        #         print e.index, n.index, ep.value
        f = m.measure_force(c)
        print bcval,f
        sys.stdout.flush()

# For "default" isotropic elasticity and a yield stress of 0.1, and a
# five-element mesh, elements begin to yield when the top boundary
# displacement reaches 0.14, and by the time it gets to 0.20, the
# whole system will yield.  At y=0.135, only the four corner elements
# will yield -- this is a good place to start, probably.
if __name__=="__main__":
    size=5 # Default...
    try:
        opts, nonopts = getopt.getopt(sys.argv[1:],"s:")
    except getopt.GetOptError:
        print "Wrong/missing options, exiting."
        sys.exit(2)
    for o,a in opts:
        if o=="-s":
            size = int(a)
    go(size)

    
