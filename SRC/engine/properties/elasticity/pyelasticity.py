# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# A simple elasticity property written in Python, as a test of the
# Python Property API.

## TODO: A C++ Property that gets a reference to this Property via
## cross_reference and expects to be able to call this Property's
## cijkl() method will be sorely disappointed, because from C++ this
## just looks like a PyFluxProperty, which doesn't have a cijkl
## method.  Fix this somehow.

## TODO? the loop in flux_matrix(), below, would be neater if it could
## be written like this:
# for ij in problem.Stress.components(planarity.ALL_INDICES):
#     for ell in problem.Displacement.components(planarity.ALL_INDICES):
#         for k in (0, 1):
#             fluxdata.stiffness_matrix_element(
#                 ij, problem.Displacement, ell, node) -= cijkl[ij, k, l]*dsf[k]

## The trouble with that is that it would require
## SmallSystem.stiffness_matrix_element to return some sort of proxy
## object to be the lhs operand of -=, and that's a SyntaxError:
## 'function call' is an illegal expression for augmented assignment
## Also, cijkl[ij, k, l] could be done, but it's still ugly.

## What works is 
# for ij in problem.Stress.components(planarity.ALL_INDICES):
#     for ell in problem.Displacement.components(planarity.ALL_INDICES):
#         for k in (0, 1):
#             fluxdata.stiffness_matrix_element(
#                 ij, problem.Displacement, ell, node).value -= cijkl[ij, k, l]*dsf[k]
## Where value is a property (in the python sense) of the proxy class
## that has a setter method that updates the fluxdata object.

from ooflib.SWIG.engine import cstrain
from ooflib.SWIG.engine import fieldindex
from ooflib.SWIG.engine import outputval
from ooflib.SWIG.engine import planarity
from ooflib.SWIG.engine import pypropertywrapper
from ooflib.SWIG.engine import symmmatrix
from ooflib.common import debug
from ooflib.engine import problem
from ooflib.engine import propertyregistration
from ooflib.engine.IO import isocijkl

class PyElasticity(pypropertywrapper.PyFluxProperty):
    def modulus(self):
        return isocijkl.IsotropicRank4TensorCij(c11=1.0, c12=0.5).tensorForm()

    def flux_matrix(self, mesh, element, nodeiterator, flux, point, time,
                    fluxdata):
        sf = nodeiterator.shapefunction(point)
        dsf0 = nodeiterator.dshapefunction(0, point)
        dsf1 = nodeiterator.dshapefunction(1, point)
        cijkl = self.modulus()
        for ij in problem.Stress.components(planarity.ALL_INDICES):
            for ell in problem.Displacement.components(planarity.ALL_INDICES):
                ell0 = fieldindex.SymTensorIndex(0, ell)
                ell1 = fieldindex.SymTensorIndex(1, ell)
                fluxdata.add_stiffness_matrix_element(
                    ij,
                    problem.Displacement,
                    ell,
                    nodeiterator,
                    -(cijkl[ij, ell0]*dsf0 + cijkl[ij, ell1]*dsf1))
            if not problem.Displacement.in_plane(mesh):
                oop = problem.Displacement.out_of_plane()
                for k in oop.components(planarity.ALL_INDICES):
                    kl = fieldindex.SymTensorIndex(2, ell)
                    fluxdata.add_stiffness_matrix_element(
                        ij, oop, kay, nodeiterator,
                        -cijkl[ij, kl]*sf)

    def integration_order(self, subproblem, element):
        if problem.Displacement.in_plane(subproblem.get_mesh()):
            return element.dshapefun_degree()
        return element.shapefun_degree()

    def output(self, mesh, element, output, pos):
        if output.name() == "Energy":
            etype = output.getEnumParam("etype")
            if etype in ("Total", "Elastic"):
                mod = self.modulus()
                # strain is a SymmMatrix3.  modulus is a cijkl.Cijkl
                strain = cstrain.getGeometricStrain(mesh, element, pos, False)
                stress = mod*strain # another SymmMatrix3.
                return outputval.ScalarOutputVal(0.5*stress.contract(strain))
                # TODO? Replace that with this:
                ## e = 0
                ## for ij in stress.components(planarity.ALL_INDICES):
                ##     if ij.diagonal():
                ##         e += stress[ij]*strain[ij]
                ##     else:
                ##         e += 2*stress[ij]*strain[ij]
                ## return ScalarOutputVal(0.5*e)
                # Although it would be slower than the calling
                # SymmMatrix3.contract(), it would be more easily
                # modifiable and applicable to specialized Python
                # Properties.                     

reg = propertyregistration.PropertyRegistration(
    'Mechanical:Elasticity:PyIsotropic',
    PyElasticity,
    ordering=10000,
    outputs=["Energy"],
    propertyType="Elasticity",
    secret=True,
    tip="Isotropic linear elasticity implemented in Python.")

reg.fluxInfo(fluxes=[problem.Stress], fields=[problem.Displacement],
             time_derivs=[0])
