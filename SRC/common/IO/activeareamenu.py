# -*- python -*-


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Menu item for loading named active areas into a microstructure.

from ooflib.common.IO import microstructureIO
from ooflib.SWIG.common import activearea
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.common import pixelgroup
from ooflib.common.IO import oofmenu
from ooflib.common.IO import whoville
from ooflib.common.IO import parameter
import ooflib.common.microstructure as ms_module


def _namedactivearea(menuitem, microstructure, category, active_areas):
    # Get the pixels for this category, and add all the active areas
    # associated with this category to each pixel.
    ms_obj = ms_module.getMicrostructure(microstructure)
    pxls = microstructureIO.getCategoryPixels(microstructure, category)
    
    px_dict = {}
    
    for name in active_areas:
        px_dict[name]=[]

    for p in pxls:
        aal = activearea.areaListFromPixel(ms_obj, p)
        for name in active_areas:
            aal.add(name)
            px_dict[name].append(p)

    for name in active_areas:
        aa = ms_obj.getNamedActiveArea(name)
        aa.activearea.add_pixels(px_dict[name])
        

# The name of this menu item is set by the name passed in to the
# singleton instance of the ActiveAreasAttributeRegistration object.

# This item is a sub-item of OOF.LoadData.Microstructure.DefineCategory.
microstructureIO.categorymenu.addItem(
    oofmenu.OOFMenuItem(
        'NamedActiveArea',
        callback=_namedactivearea,
        params=[whoville.WhoParameter('microstructure',
                                      ms_module.microStructures,
                                      tip=parameter.emptyTipString),
                parameter.IntParameter('category',
                                       tip=parameter.emptyTipString),
                parameter.ListOfStringsParameter('active_areas',
                                                 tip=parameter.emptyTipString)],
        
        help="Create a named active area in a microstructure",
        discussion="""<para> Creates a named active area when
        loading a microstructure from
        a file.  This menu item is only used in data files.</para>""",
        xrefs=["Section-Concepts-FileFormats",
               "Section-Tasks-Active_Area",
               "MenuItem-OOF.LoadData.Microstructure"]
    ))                    


def _newactivearea(menuitem, microstructure, name):
    ms_obj = ms_module.getMicrostructure(microstructure)
    new_aa = activearea.ActiveArea(
        ms_obj.sizeInPixels(), ms_obj.size(), ms_obj)
    ms_obj.namedActiveAreas.append(
        activearea.NamedActiveArea(name, new_aa))
    switchboard.notify('stored active areas changed', name)
        

# Create a new (empty) named active area in a microstructure when
# loading it from a file.
microstructureIO.micromenu.addItem(
    oofmenu.OOFMenuItem(
        'NewActiveArea',
        callback=_newactivearea,
        params=[whoville.WhoParameter('microstructure',
                                      ms_module.microStructures,
                                      tip=parameter.emptyTipString),
                parameter.StringParameter('name',
                                          tip=parameter.emptyTipString)],
        help="Create a new empty active area in a microstructure.",
        discussion="""<para>Create a new empty active area in a
        microstructure when loading it from a data file.  This menu
        item is only used in data files.</para>""",
        xrefs=["Section-Concepts-FileFormats", "Section-Tasks-Active_Area"]
    ))
