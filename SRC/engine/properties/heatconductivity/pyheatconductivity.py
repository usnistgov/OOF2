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
# calculation, since would be much slower than the C++ code in
# heatconductivity.C, even if it didn't go out of its way to be more
# complicated than necessary.  It's used in the regression tests,
# though.

from ooflib.common import debug
from ooflib.SWIG.engine import fieldindex
from ooflib.SWIG.engine import planarity
from ooflib.SWIG.engine import pypropertywrapper
from ooflib.SWIG.engine import symmmatrix
from ooflib.engine import problem
from ooflib.engine import propertyregistration
import sys

class PyHeatConductivity(pypropertywrapper.PyFluxProperty):

    # To test precompute(), set_mesh_data(), get_mesh_data(), and
    # cross_reference() in Python Properties, PyHeatConductivity gets
    # its conductivity tensor from a separate Property.  It finds that
    # Property with cross_reference().  Precompute stores the tensor as
    # mesh data, and flux_matrix retrieves the tensor from the mesh.
    def precompute(self, mesh):
        self.set_mesh_data(mesh, self.heatcondvalue.value)
    def cross_reference(self, material):
        self.heatcondvalue = material.fetchProperty("TESTING")
        ## Checking that a C++ Property can be cross referenced by a
        ## Python Property.
        # orientation = material.fetchProperty("Orientation")
        # debug.fmsg(f"orientation={orientation.orientation()}")

    def flux_matrix(self, mesh, element, nodeiterator, flux, point, time,
                    fluxdata):
        sf = nodeiterator.shapefunction(point)
        dsf0 = nodeiterator.dshapefunction(0, point)
        dsf1 = nodeiterator.dshapefunction(1, point)

        # This demo Property uses a hard coded conductivity tensor.  A
        # real Property would set it from a Parameter.
        cond = self.get_mesh_data(mesh)
        
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

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class ProfessorButts(pypropertywrapper.PyAuxProperty):
    def __init__(self, name, registration):
        super(ProfessorButts, self).__init__(name, registration)
        self.value = symmmatrix.SymmMatrix3(1., 1., 1., 0., 0., 0.)
    
reg = propertyregistration.PropertyRegistration(
    "HeatCondValue",
    ProfessorButts,
    ordering=12345678,
    propertyType="TESTING",
    secret=True
)
