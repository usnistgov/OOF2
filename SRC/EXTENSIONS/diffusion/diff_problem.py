# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.engine import problem
from ooflib.SWIG.engine import flux
from ooflib.SWIG.engine import equation
from ooflib.SWIG.engine import field
from ooflib.SWIG.engine import fieldindex
from ooflib.SWIG.common import config
from ooflib.engine import conjugate

# Define a field.  This creates an object named 'Concentration' in the
# OOF namespace.
Concentration = field.ScalarField('Concentration')
# Define a flux
Atom_Flux = flux.VectorFlux('Atom_Flux')
Charge_Flux = flux.VectorFlux('Charge_Flux')

# And equations
AtomBalanceEquation = equation.DivergenceEquation(
    'Atom_Eqn', Atom_Flux, 1)

ChargeBalanceEquation = equation.DivergenceEquation(
    'Charge_Eqn', Charge_Flux, 1)


AtomOutOfPlane = equation.PlaneFluxEquation(
    'Plane_Atom_Flux', Atom_Flux, 1)
ChargeOutOfPlane = equation.PlaneFluxEquation(
            'Plane_Charge_Flux', Charge_Flux, 1)

##
## Atom flux equation
##
## In-plane components, C
##
# C = fieldindex.ScalarFieldIndex()
# DivJd = fieldindex.ScalarFieldIndex()
# $\nabla \cdot \vec{Jd}$ is conjugate to C

conjugate.conjugatePair("Diffusivity",
                        AtomBalanceEquation,
                        AtomBalanceEquation.components(),
                        Concentration,
                        Concentration.components())

conjugate.conjugatePair("Current",
                        ChargeBalanceEquation,
                        ChargeBalanceEquation.components(),
                        problem.Voltage,
                        problem.Voltage.components())

## out-of-plane components, $\frac{\partial C}{\partial z}$
# C_z = fieldindex.OutOfPlaneVectorFieldIndex(2)
# Jd_z = fieldindex.OutOfPlaneVectorFieldIndex(2)
##  $Jd_{z}$ is conjugate to $\frac{\partial C}{\partial z}$

conjugate.conjugatePair("Diffusivity", AtomOutOfPlane,
                        AtomOutOfPlane.components(),
                        Concentration.out_of_plane(),
                        Concentration.out_of_plane().components())
conjugate.conjugatePair("Current",
                        ChargeOutOfPlane,
                        ChargeOutOfPlane.components(),
                        problem.Voltage.out_of_plane(),
                        problem.Voltage.out_of_plane().components())


