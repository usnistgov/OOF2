# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# This file has the big block of imports which gets all the built-in
# property classes.  These imports run the initialization code in the
# property classes themselves, creating a PropertyRegistration entry,
# which then adds itself to the main OOF2 namespace.

from ooflib.SWIG.common import config

# Properties not in this list can be imported by the user at
# other points, so this list of properties is not guaranteed to
# be exhaustive.
import ooflib.SWIG.engine.properties

import ooflib.SWIG.engine.properties.color.color
import ooflib.SWIG.engine.properties.damping.damping
import ooflib.SWIG.engine.properties.elasticity.aniso.aniso
import ooflib.SWIG.engine.properties.elasticity.elasticity
import ooflib.SWIG.engine.properties.elasticity.iso.iso
import ooflib.SWIG.engine.properties.elasticity.largestrain.largestrain
import ooflib.SWIG.engine.properties.elasticity.thermo.thermo
import ooflib.SWIG.engine.properties.elasticity.visco.visco
import ooflib.SWIG.engine.properties.elasticity.nonlinear.general_nonlinear_elasticity
import ooflib.SWIG.engine.properties.forcedensity.forcedensity
import ooflib.SWIG.engine.properties.forcedensity.nonconstant.nonconstant_force_density
import ooflib.SWIG.engine.properties.forcedensity.nonlinear.nonlinear_force_density
import ooflib.SWIG.engine.properties.heatcapacity.heatcapacity
import ooflib.SWIG.engine.properties.heatconductivity.heatconductivity
import ooflib.SWIG.engine.properties.heatconductivity.nonlinear.nonlinear_heat_conductivity
import ooflib.SWIG.engine.properties.heatsource.heatsource
import ooflib.SWIG.engine.properties.heatsource.nonconstant.nonconstant_heat_source
import ooflib.SWIG.engine.properties.heatsource.nonlinear.nonlinear_heat_source
import ooflib.SWIG.engine.properties.massdensity.massdensity
import ooflib.SWIG.engine.properties.orientation.orientation
import ooflib.SWIG.engine.properties.permittivity.permittivity
import ooflib.SWIG.engine.properties.piezoelectricity.piezoelectricity
import ooflib.SWIG.engine.properties.pyroelectricity.pyroelectricity
import ooflib.SWIG.engine.properties.stressfreestrain.stressfreestrain
import ooflib.SWIG.engine.properties.thermalexpansion.thermalexpansion
import ooflib.engine.properties.plasticity.plasticity

# Planar strain only makes sense in 2D.
if config.dimension() == 2:
    import ooflib.SWIG.engine.properties.planestrain.planestrain

#Interface branch
if config.dimension() == 2:
    import ooflib.SWIG.engine.properties.interfaces.surfacetension.simpletension.simpletension
    import ooflib.SWIG.engine.properties.interfaces.surfacetest.surfacetest
#     import ooflib.SWIG.engine.properties.interfaces.surfacetension.simpletension2.simpletension2


import ooflib.engine.properties.heatconductivity.pyheatconductivity
import ooflib.engine.properties.elasticity.pyelasticity
import ooflib.engine.properties.stressfreestrain.pystressfreestrain
