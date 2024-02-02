# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# The MaterialType enum was introduced when we started to add
# interface properties, to distinguish between materials assigned to
# bulk and materials assigned to interfaces.  Since that 

from ooflib.SWIG.common import config
from ooflib.common import runtimeflags
from ooflib.common import enum
from ooflib.common import utils

class MaterialType(enum.EnumClass(
    ('bulk',
     'A bulk material. Normal bulk properties can be added only to this type of material.'))):
    tip = "Types of &oof2; materials."
    discussion = """<para>
    Types of &oof2; materials.
    Certain properties can only be assigned to certain types of materials.
    Bulk materials can be assigned to bulk elements.
    </para>
    <para>
    There used to be an Interface material type in &oof2;, but it
    wasn't fully implemented. It will be reintroduced sometime, we
    hope.
    </para>"""
    xrefs=["Section-Tasks-Materials"]

if runtimeflags.surface_mode:
    enum.addEnumName(
        MaterialType,
        "interface",
        "An interface material. Interface properties can be added only to this type of material.")
                     

utils.OOFdefine('MaterialType', MaterialType)

MATERIALTYPE_BULK = MaterialType("bulk")
if runtimeflags.surface_mode:
    MATERIALTYPE_INTERFACE = MaterialType("interface")


