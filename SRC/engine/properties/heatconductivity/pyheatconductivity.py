# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# A simple heat conductivity property written in Python, as a test of
# the Python Property API.  This shouldn't ever be used in a real
# calculation, since it is much slower than the C++ code in
# heatconductivity.C.  It's used in the regression tests, though.

from ooflib.common import debug
from ooflib.SWIG.engine import fieldindex
from ooflib.SWIG.engine import planarity
from ooflib.SWIG.engine import pypropertywrapper
from ooflib.SWIG.engine import symmmatrix
from ooflib.engine import problem
from ooflib.engine import propertyregistration

class PyHeatConductivity(pypropertywrapper.PyFluxProperty):
    def flux_matrix(self, mesh, element, nodeiterator, flux, point, time,
                    fluxdata):
        sf = nodeiterator.shapefunction(point)
        dsf0 = nodeiterator.dshapefunction(0, point)
        dsf1 = nodeiterator.dshapefunction(1, point)

        # This demo Property uses a hard coded conductivity tensor.  A
        # real Property would set it from a Parameter.
        cond = symmmatrix.SymmMatrix3(1., 1., 1., 0., 0., 0.)
        
        for fluxindex in problem.Heat_Flux.components(planarity.ALL_INDICES):
            ij0 = fieldindex.SymTensorIndex(fluxindex, 0)
            ij1 = fieldindex.SymTensorIndex(fluxindex, 1)
            fluxdata.add_stiffness_matrix_element(
                fluxindex,
                problem.Temperature,
                problem.Temperature.getIndex(""), # scalar field dummy 'index'
                nodeiterator,
                -(cond[ij0]*dsf0 + cond[ij1]*dsf1)
            )
            if not problem.Temperature.in_plane(mesh):
                ij2 = fieldindex.SymTensorIndex(fluxindex, 2)
                fluxdata.add_stiffness_matrix_element(
                    fluxindex,
                    problem.Temperature.out_of_plane(), # also a scalar
                    problem.Temperature.getIndex(""),   # also a dummy
                    nodeiterator,
                    cond[ij2]*sf
                )
    def integration_order(self, subproblem, element):
        if problem.Temperature.in_plane(subproblem.get_mesh()):
            return element.dshapefun_degree()
        return element.shapefun_degree()

reg = propertyregistration.PropertyRegistration(
    'Thermal:Conductivity:PyIsotropic',
    PyHeatConductivity,
    ordering=10000,
    propertyType="ThermalConductivity",
    secret=True
    )

reg.fluxInfo(fluxes=[problem.Heat_Flux], fields=[problem.Temperature],
             time_derivs=[0])
