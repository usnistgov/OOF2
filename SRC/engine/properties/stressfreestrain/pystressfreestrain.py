# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.engine import fieldindex
from ooflib.SWIG.engine import planarity
from ooflib.SWIG.engine import pypropertywrapper
from ooflib.SWIG.engine import symmmatrix
from ooflib.common import debug
from ooflib.engine import problem
from ooflib.engine import propertyregistration

## TODO: See the TODO in pyelasticity.py about improving the Python
## Properties.

class PyStressFreeStrain(pypropertywrapper.PyFluxProperty):

    def cross_reference(self, material):
        self.elasticity = material.fetchProperty("Elasticity")

    def flux_offset(self, mesh, element, flux, point, time, fluxdata):
        cijkl = self.elasticity.cijkl(mesh, element, point)
        strain0 = symmmatrix.SymmMatrix3(0.1, 0.1, 0.1, 0, 0, 0)
        for ij in problem.Stress.components(planarity.ALL_INDICES):
            for kl in fieldindex.symTensorIJComponents:
                strain_kl = strain0.get(kl.row(), kl.col()) # TODO: too ugly
                if kl.diagonal(): 
                    fluxdata.add_offset_vector_element(
                        ij,
                        cijkl[ij.integer(), kl.integer()]*strain_kl)
                else:
                    fluxdata.add_offset_vector_element(
                        ij,
                        2.0*cijkl[ij.integer(), kl.integer()]*strain_kl)
        
        ## It would be nice if this could have been written like this:
        # for ij in problem.Stress.components(planarity.ALL_INDICES):
        #     for kl in fieldindex.symTensorIJComponents:
        #         if kl.diagonal():
        #             fluxdata(element, ij) -= cijkl[ij, kl]*strain0[kl]
        #         else:
        #             fluxdata(element, ij) -= 2*cijkl[ij, ik]*strain0[kl]

    def integration_order(self, subproblem, element):
        return element.shapefun_degree()

reg = propertyregistration.PropertyRegistration(
    'Mechanical:StressFreeStrain:PyIsotropic',
    PyStressFreeStrain,
    10000,
    propertyType="StressFreeStrain",
    tip = "Isotropic stress-free strain implemented in Python.",
    secret=True)

reg.fluxInfo(fluxes=[problem.Stress])
