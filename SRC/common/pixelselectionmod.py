# -*- python -*-
# $RCSfile: pixelselectionmod.py,v $
# $Revision: 1.31 $
# $Author: langer $
# $Date: 2014/09/27 21:40:27 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Pixel selection modification tools that *don't* depend on the image,
# and hence aren't in the image module.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import pixelselectioncourier
from ooflib.SWIG.common import switchboard
from ooflib.common import color
from ooflib.common import debug
from ooflib.common import registeredclass
from ooflib.common.IO import colordiffparameter
from ooflib.common.IO import parameter
from ooflib.common.IO import pixelgroupparam
from ooflib.common.IO import reporter
from ooflib.common.IO import whoville
from ooflib.common.IO import xmlmenudump
import ooflib.common.microstructure

# First, some basic methods: Clear, Undo, Redo
# These are no longer called from the generic toolbox, but they are
# still set as menu callbacks in the selectionmodmenu, in common/IO.

def clear(menuitem, microstructure):
    ms = ooflib.common.microstructure.microStructures[microstructure]
    selection = ms.getSelectionContext()
    selection.begin_writing()
    try:
        selection.start()
        selection.clear()
    finally:
        selection.end_writing()
    switchboard.notify('pixel selection changed')
    switchboard.notify('redraw')

def undo(menuitem, microstructure):
    ms = ooflib.common.microstructure.microStructures[microstructure]
    selection = ms.getSelectionContext()
    selection.begin_writing()
    try:
        selection.undo()
    finally:
        selection.end_writing()
    switchboard.notify('pixel selection changed')
    switchboard.notify('redraw')

def redo(menuitem, microstructure):
    ms = ooflib.common.microstructure.microStructures[microstructure]
    selection = ms.getSelectionContext()
    selection.begin_writing()
    try:
        selection.redo()
    finally:
        selection.end_writing()
    switchboard.notify('pixel selection changed')
    switchboard.notify('redraw')


############################################

# Selection methods derived from SelectionModifier are automatically
# put into the PixelSelection menu, via a switchboard call in their
# Registration's __init__.

class SelectionModifier(registeredclass.RegisteredClass):
    registry = []
    def __call__(self):
        pass

#############################################

# OOFMenu callback, installed automatically for each SelectionModifier
# class by the switchboard callback invoked when the class is
# registered.

def doSelectionMod(menuitem, microstructure, **params):
    registration = menuitem.data
    # create the SelectionModifier
    selectionModifier = registration(**params)
    # apply the SelectionModifier
    ms = ooflib.common.microstructure.microStructures[microstructure].getObject()
    selection = ms.pixelselection
    selection.begin_writing()
    try:
        selectionModifier(ms, selection)
    finally:
        selection.end_writing()
    switchboard.notify('pixel selection changed')
    switchboard.notify('modified pixel selection', selectionModifier)
    switchboard.notify('new pixel selection', None, None)
    switchboard.notify('redraw')

#############################

class Invert(SelectionModifier):
    def __call__(self, ms, selection):
        selection.start()
        selection.invert()

registeredclass.Registration(
    'Invert',
    SelectionModifier,
    Invert,
    ordering=0.0,
    tip="Select all unselected pixels and unselect all selected pixels.",
    discussion="""<para>
    Selected pixels will be unselected and unselelcted ones will be
    selected.</para>""")

##############################################

# Selection modifiers that take a pixel group as an argument.

class GSelectionModifier(SelectionModifier):
    def __init__(self, group):
        self.group = group

GroupSelection = pixelselectioncourier.GroupSelection
class GroupSelectionModifier(GSelectionModifier):
    def __call__(self, ms, selection):
        group = ms.findGroup(self.group)
        if group is not None:
            selection.start()
            selection.clearAndSelect(GroupSelection(ms, group))

class GroupTooSelectionModifier(GSelectionModifier):
    def __call__(self, ms, selection):
        group = ms.findGroup(self.group)
        if group is not None:
            selection.start()
            selection.select(GroupSelection(ms, group))

class UnselectGroupSelectionModifier(GSelectionModifier):
    def __call__(self, ms, selection):
        group = ms.findGroup(self.group)
        if group is not None:
            selection.start()
            selection.unselect(GroupSelection(ms, group))

IntersectSelection = pixelselectioncourier.IntersectSelection
class IntersectGroupSelectionModifier(GSelectionModifier):
    def __call__(self, ms, selection):
        group = ms.findGroup(self.group)
        if group is not None:
            selection.start()
            # The selection needs to be cloned before calling
            # clearAndSelect, or else it will be empty by the time the
            # intersection is actually computed.  The clone has to be
            # stored in a variable here, so that it won't be garbage
            # collected until the calculation is complete.
            selgrp = selection.getSelectionAsGroup().clone()
            selection.clearAndSelect(IntersectSelection(ms, selgrp, group))
            
registeredclass.Registration(
    'Select Group', SelectionModifier,
    GroupSelectionModifier,
    ordering=1.0,
    params=[pixelgroupparam.PixelGroupParameter('group',
                                         tip='Select pixels in this group.'),
            ],
    tip='Select all pixels in the given group.',
    discussion="""<para>

    Deselect all pixels, and then select the pixels in the given
    group.  Compare to <xref
    linkend='MenuItem-OOF.PixelSelection.Add_Group'/>.

    </para>""")
            
registeredclass.Registration(
    'Add Group', SelectionModifier,
    GroupTooSelectionModifier,
    ordering=1.01,
    params=[pixelgroupparam.PixelGroupParameter('group',
                                        tip='Select pixels in this group too.'),
    ],
    tip='Select all pixels in the given group, while retaining all currently selected pixels.',
    discussion="""<para>

    Select all the pixels in the given &pixelgroup;
    <emphasis>without</emphasis> first deselecting the currently selected
    pixels.  Compare to <xref
    linkend='MenuItem-OOF.PixelSelection.Select_Group'/>.

    </para>"""

    )

registeredclass.Registration(
    'Unselect Group', SelectionModifier,
    UnselectGroupSelectionModifier,
    ordering=1.02,
    params=[pixelgroupparam.PixelGroupParameter('group',
                               tip='Unselect pixels that are in this group.'),
    ],
    tip='Unselect all pixels that are in the given group, while retaining other currently selected pixels.',
    discussion="<para>Remove pixels that belong to the chosen &pixelgroup; from the current pixel selection.</para>")

registeredclass.Registration(
    'Intersect Group', SelectionModifier,
    IntersectGroupSelectionModifier,
    ordering=1.03,
    params=[
    pixelgroupparam.PixelGroupParameter('group',
                                        tip='Unselect pixels that are not in this group'),
    ],
    tip='Select only the intersection of the current selection and the given group.',
    discussion="""<para>

    Select only the pixels that belong to both the chosen &pixelgroup;
    and the current selection.

    </para>""")
            
#########################################

class Despeckle(SelectionModifier):
    def __init__(self, neighbors):
        self.neighbors = neighbors
    def __call__(self, ms, selection):
        selection.start()
        selection.select(pixelselectioncourier.DespeckleSelection(
            ms, selection.getSelectionAsGroup(), self.neighbors))
        
class Elkcepsed(SelectionModifier):
    def __init__(self, neighbors):
        self.neighbors = neighbors
    def __call__(self, ms, selection):
        selection.start()
        selection.unselect(pixelselectioncourier.ElkcepsedSelection(
            ms, selection.getSelectionAsGroup(), self.neighbors))

if config.dimension() == 2:
    registeredclass.Registration(
        'Despeckle',
        SelectionModifier,
        Despeckle,
        ordering=2.0,
        params=[parameter.IntRangeParameter('neighbors', (4,8), 8,
                tip="Select pixels with at least this many selected neighbors")
        ],
        tip="Recursively select all pixels with a minimum number of selected neighbors. This fills in small holes in the selection.",
        discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/despeckle.xml')
        )

    registeredclass.Registration(
        'Elkcepsed',
        SelectionModifier,
        Elkcepsed,
        ordering=2.1,
        params=[parameter.IntRangeParameter('neighbors', (1,4), 3,
           tip="Deselect pixels with fewer than this many selected neighbors.")
        ],
        tip="Recursively deselect all pixels with fewer than a minimum number of selected neighbors.  This has the effect of removing small islands and peninsulas, and is the opposite of 'Despeckle'.",
        discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/elkcepsed.xml')
        )


#########################################

class Expand(SelectionModifier):
    def __init__(self, radius):
        self.radius = radius
    def __call__(self, ms, selection):
        selection.start()
        selection.select(pixelselectioncourier.ExpandSelection(
            ms, selection.getSelectionAsGroup(), self.radius))

class Shrink(SelectionModifier):
    def __init__(self, radius):
        self.radius = radius
    def __call__(self, ms, selection):
        selection.start()
        selection.unselect(pixelselectioncourier.ShrinkSelection(
            ms, selection.getSelectionAsGroup(), self.radius))

if config.dimension() == 2:
    registeredclass.Registration(
        'Expand',
        SelectionModifier,
        Expand,
        ordering=3.0,
        params=[
        parameter.FloatParameter('radius', 1.0,
                                 tip='Select pixels within this distance of other selected pixels.')
        ],
        tip="Select all pixels within a given distance of the current selection.",
        discussion=xmlmenudump.loadFile("DISCUSSIONS/common/menu/expand_pixsel.xml")
        )

    registeredclass.Registration(
        'Shrink',
        SelectionModifier,
        Shrink,
        ordering=3.1,
        params=[
        parameter.FloatParameter('radius', 1.0,
                                 tip='Deselect pixels within this distance of other deselected pixels.')
        ],
        tip="Deselect all pixels within a given distance of the boundaries of the current selection.",
        discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/shrink_pixsel.xml')
        )
#############################

class CopyPixelSelection(SelectionModifier):
    def __init__(self, source):
        self.source = source
    def __call__(self, ms, selection):
        selection.start()
        sourceMS = ooflib.common.microstructure.microStructures[self.source]
        selection.selectFromGroup(
            sourceMS.getObject().pixelselection.getSelectionAsGroup())

registeredclass.Registration(
    'Copy',
    SelectionModifier,
    CopyPixelSelection,
    ordering=4.0,
    params=[
    whoville.WhoParameter('source', ooflib.common.microstructure.microStructures,
                          tip="Copy the current selection from this Microstructure.")],
    tip="Copy the current selection from another Microstructure.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/copy_pixsel.xml')
    )
