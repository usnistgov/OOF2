# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# The GhostGfxWindow is the underlying non-GUI representation of a
# graphics window.  The actual graphics window, GfxWindow, is derived
# from GhostGfxWindow and overrides some of its functions.

## TODO: If the window is empty, write "This window intentionally left
## blank" w/ instructions on what to do.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import lock
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.common import timestamp
from ooflib.common import color
from ooflib.common import debug
from ooflib.common import enum
from ooflib.common import labeltree
from ooflib.common import mainthread
from ooflib.common import primitives
from ooflib.common import quit
from ooflib.common import subthread
from ooflib.common import toolbox
from ooflib.common.IO import animationstyle
from ooflib.common.IO import animationtimes
from ooflib.common.IO import display
from ooflib.common.IO import filenameparam
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import placeholder
from ooflib.common.IO import whoville
from ooflib.common.IO import xmlmenudump
import copy
import os.path
import sys
import traceback
import types

import oofcanvas

# TODO: These are used inconsistently.  Don't define the local variables. 
FloatParameter = parameter.FloatParameter
IntParameter = parameter.IntParameter

OOF = mainmenu.OOF
OOFMenuItem = oofmenu.OOFMenuItem
CheckOOFMenuItem = oofmenu.CheckOOFMenuItem

# Since debugging the locking code here is a fairly common
# requirement, and commenting out the debugging lines is a pain, they
# can all be turned on and off by setting _debuglocks.
_debuglocks = False

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class NewLayerPolicy(enum.EnumClass(
        ("Never", "Don't automatically create any display layers."),
        ("Single", "Automatically add new graphics layers for Images, Skeletons, and Meshes if the graphics window doesn't contain any similar layers for other objects.  New graphics windows will automatically add layers for pre-existing objects if they are unique."),
        ("Always", "Automatically add display layers for all newly created Images, Skeletons, and Meshes."))):
    tip = "How the graphics window reacts when new Images, Skeletons, or Meshes are created."
    discussion='<para>See <xref linkend="Section-Graphics-New-Layer-Policy"/>.</para>'

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class OutputImageFormat(enum.EnumClass(
        ("pdf", "Save image as a pdf file."),
        ("png", "Save image as a png file."))):
    tip="File format for the image."
    discussion="""<para>Images can be saved as either pdf or png files.</para>"""

if debug.debug():
    enum.addEnumName(OutputImageFormat, "datadump",
                     help="For debugging only.")

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

default_settings = dict(
    bgcolor = color.white.opaque(),
    zoomfactor = 1.5,
    margin = 0.05,
    longlayernames = False,     # Use long form of layer reprs.
    listall = False,            # are all layers to be listed?
    antialias = True,
    aspectratio = 5,            # Aspect ratio of the contourmap.
    contourmap_markersize = 2,  # Size in pixels of contourmap marker.
    contourmap_markercolor = color.gray50, # Contourmap position marker color.
    newlayerpolicy = NewLayerPolicy("Never")
)    

class GfxSettings:
    # Stores all the settable parameters for a graphics
    # window. Assigning to a variable sets *both* the instance and
    # default values so that a new window will always use the latest
    # settings.

    ## TODO? Use Python properties, instead of __setattr__.  Can that
    ## be done without writing separate setter and getter routines for
    ## each setting?  That would make it difficult to add new
    ## settings.

    def __init__(self):
        self.__dict__['timestamps'] = {} # don't use setattr for this!
        # Initialize to the default values
        for key, val in default_settings.items():
            self.__dict__[key] = val
            self.timestamps[key] = timestamp.TimeStamp()
    def __setattr__(self, attr, val):
        self.__dict__[attr] = val 
        default_settings[attr] = val
        if attr in self.timestamps:
            self.timestamps[attr].increment()
        else:
            self.timestamps[attr] = timestamp.TimeStamp()
    def getTimeStamp(self, attr):
        return self.timestamps[attr]

    def clone(self):
        copy = GfxSettings()
        for attr in default_settings.keys():
            setattr(copy, attr, getattr(self, attr))
        return copy


# Modules (eg, image or engine) can add graphics window settings by
# calling defineGfxSetting().  They should do this at initialization
# time, before any graphics windows are created.  defineGfxSetting
# does *not* create a menu item or callback for the setting.  That
# must be done by catching the "open graphics window" switchboard
# signal.

def defineGfxSetting(name, val):
    default_settings[name] = val

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# ContourMapData class just aggregates data related to the ContourMap
# display, to keep the code (relatively) tidy.

class ContourMapData:
    def __init__(self):
        self.canvas = None      # an OOFCanvas.Canvas
        self.mouse_down = None
        self.mark_value = None
        self.canvas_mainlayer = None
        self.canvas_ticklayer = None

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class GhostGfxWindow:
    initial_height = 400
    initial_width = 800
    def __init__(self, name, gfxmanager, settings=None, clone=False):
        if not hasattr(self, 'settings'):
            self.settings = settings or GfxSettings()
        self.name = name
        self.gfxmanager = gfxmanager
        if not hasattr(self, 'gfxlock'):
            self.gfxlock = lock.Lock()
        self.layers = []        # DisplayMethod instances
        self.current_contourmap_method = None
        self.selectedLayer = None
        self.layerChangeTime = timestamp.TimeStamp()
        # displayTime is the simulation time of the displayed
        # mesh. displayTimeChanged is the timestamp indicated when the
        # simulation time was modified.  They are completely different
        # sorts of time.
        self.displayTime = 0.0
        self.displayTimeChanged = timestamp.TimeStamp()

        self.oofcanvas = mainthread.runBlock(self.newCanvas)
        self.oofcanvas.setAntialias(self.settings.antialias)
        self.oofcanvas.setBackgroundColor(
            color.canvasColor(self.settings.bgcolor))
        self.oofcanvas.setMargin(self.settings.margin)

        # Although the contour map, which displays the contour color
        # scheme, is only used in GUI mode, the command that saves it
        # to a file can be invoked in text mode, so the data has to
        # exist here in GhostGfxWindow.
        self.contourmapdata = ContourMapData()

        self.menu = OOF.addItem(OOFMenuItem(
            self.name,
            secret=True,
            help = "Commands dependent on a particular Graphics window.",
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/graphics.xml')
        ))

        # Put this window into the Windows/Graphics menu, so that it
        # can be raised in graphics mode.  Since this isn't meaningful
        # in text mode, there's no callback defined here.
        OOF.Windows.Graphics.addItem(OOFMenuItem(
            self.name,
            help="Raise the window named %s." % name, 
            gui_only=1,
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/graphicsraise.xml')
            ))
        filemenu = self.menu.addItem(OOFMenuItem(
            'File',
            help='General graphics window operations.'))
        filemenu.addItem(OOFMenuItem(
            'Clone',
            callback=self.cloneWindow,
            ellipsis=1,
            help='Make a copy of this window.',
            discussion="""<para>
            Duplicate this <link linkend='Chapter-Graphics'>Graphics
            window</link>.  The <link
            linkend='Section-Graphics-Layer'>layers</link> and most of the
            <link linkend="MenuItem-OOF.Graphics_n.Settings">settings</link>
            will be duplicated as well.
            </para>"""
            ))
        filemenu.addItem(OOFMenuItem(
            'Save_Canvas',
            callback=self.saveCanvas,
            ellipsis=1,
            params=[
                filenameparam.WriteFileNameParameter(
                    'filename', ident='gfxwindow',
                    tip="Name for the image file."),
                enum.EnumParameter(
                    "format", OutputImageFormat,
                    value="pdf", tip="Format for the image file"),
                filenameparam.OverwriteParameter(
                    'overwrite',
                    tip="Overwrite an existing file?"),
                parameter.IntParameter(
                    "pixels", 100,
                    tip="Size in pixels of the largest dimension of the image."),
                parameter.BooleanParameter(
                    "background", True,
                    tip="Fill the background?")                       
            ],
            help="Save the contents of the graphics window as an image file.",
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/graphicssave.xml')
            ))
        filemenu.addItem(OOFMenuItem(
            'Save_Canvas_Region',
            callback=self.saveCanvasRegion,
            ellipsis=1,
            params=[
                filenameparam.WriteFileNameParameter(
                    'filename', ident='gfxwindow',
                    tip='Name for the pdf image file.'),
                enum.EnumParameter(
                    "format", OutputImageFormat,
                    value="pdf", tip="Format for the image file"),
                filenameparam.OverwriteParameter(
                    'overwrite',
                    tip="Overwrite an existing file?"),
                parameter.IntParameter(
                    "pixels", 100,
                    tip="Size of the largest dimension of the image in pixels"),
                parameter.BooleanParameter(
                    "background", True,
                    tip="Fill the background?"),
                primitives.PointParameter(
                    "lowerleft",
                    tip="Lower left corner of the saved region,"
                    " in physical coordinates."),
                primitives.PointParameter(
                    "upperright",
                    tip="Upper right corner of the saved region,"
                    " in physical coordinates.")
                ],
            help="Save a region of the graphics window as an image file.",
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/graphicssaveregion.xml')))
            
        filemenu.addItem(OOFMenuItem(
            'Save_Contourmap',
            callback=self.saveContourmap,
            ellipsis=1,
            params=[
                filenameparam.WriteFileNameParameter(
                    'filename', ident='gfxwindow',
                    tip="Name for the image file."),
                enum.EnumParameter(
                    "format", OutputImageFormat,
                    value="pdf", tip="Format for the image file"),
                filenameparam.OverwriteParameter(
                    'overwrite', tip="Overwrite an existing file?"),
                parameter.IntParameter(
                    'pixels', 100,
                    tip='Size of the largest dimension of the image in pixels')
            ],
            help="Save a pdf image of the contour map.",
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/graphicssavecontour.xml')))
        filemenu.addItem(OOFMenuItem(
            'Clear',
            callback=self.clear,
            help="Remove all user-defined graphics layers.",
            discussion = xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/graphicsclear.xml')
            ))
        filemenu.addItem(OOFMenuItem(
            'Animate',
            callback=self.animate,
            accel='a',
            params=[
                placeholder.GfxTimeParameter(
                    'start',
                    value=placeholder.earliest,
                    tip="Start the animation at this time."),
                placeholder.GfxTimeParameter(
                    'finish', value=placeholder.latest,
                    tip="End the animation at this time."),
                parameter.RegisteredParameter(
                    'times',
                    animationtimes.AnimationTimes,
                    tip="How to select times between 'start' and 'finish'."),
                parameter.FloatParameter(
                    'frame_rate', 5.0,
                    tip='Update the display this many times per second.'),
                parameter.RegisteredParameter(
                    "style",
                    animationstyle.AnimationStyle,
                    tip="How to play the animation.")],
            help="Animate the Mesh displayed in the graphics window.",
            discussion=xmlmenudump.loadFile(
                    'DISCUSSIONS/common/menu/animate.xml')
            ))

        filemenu.addItem(OOFMenuItem(
            'Redraw',
            callback=self.redraw,
            help="Force all graphics layers to be redrawn.",
            discussion="""<para>
            Redraw all graphics layers, whether they need it or not.
            This should never be necessary.
            </para>"""
            ))
        if debug.debug():
            filemenu.addItem(OOFMenuItem(
                'DumpLayers',
                callback=self.dumpLayers,
                params=[parameter.StringParameter('filename',
                                                  tip="File name prefix.")],
                help="Save each graphics layer as a separate png file.",
                discussion="""<para> Save each individual graphics
                layer in a png file, named
                <userinput>filename</userinput>XX.png, where XX is an
                integer. Only available if the window was opened in
                debug mode. </para>"""
                ))

        filemenu.addItem(OOFMenuItem(
            'Close',
            callback=self.close,
            accel='w',
            help="Close the graphics window.",
            discussion="<para>Close the graphics window.</para>"))
        filemenu.addItem(OOFMenuItem(
            'Quit',
            callback=quit.quit,
            accel='q',
            threadable = oofmenu.UNTHREADABLE,
            help= "TTFN",
            discussion="""<para>
            See <xref linkend='MenuItem-OOF.File.Quit'/>.
            </para>"""))
        
        self.toolboxmenu = self.menu.addItem(OOFMenuItem(
            'Toolbox',
            cli_only=1,
            help='Commands for the graphics toolboxes.',
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/toolbox.xml')
            ))
        layermenu = self.menu.addItem(OOFMenuItem(
            'Layer',
            help='Commands for manipulating graphics layers.',
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/layer.xml')
            ))

        layermenu.addItem(OOFMenuItem(
            'New',
            callback=self.newLayerCB,
            accel='n',
            ellipsis=True,
            gui_title="New Graphics Layer", # used in the dialog box
            params=[
                whoville.WhoClassParameter(
                    "category", tip="The kind of object to display."),
                whoville.AnyWhoParameter(
                    "what", tip="The object to display."),
                display.DisplayMethodParameter(
                    "how", tip="How to display the object.")],
            help="Add a new graphics layer.",
            discussion=xmlmenudump.loadFile(
                # TODO GTK3: Fix this manual page.
                'DISCUSSIONS/common/menu/newlayer.xml')
            ))
        layermenu.addItem(OOFMenuItem(
            'Edit',
            callback=self.editLayerCB,
            params=[IntParameter('n', 0, tip="Layer to edit."),
                    whoville.WhoClassParameter(
                        "category", tip="The kind of object to display"),
                    whoville.AnyWhoParameter(
                        "what", tip="The object to display"),
                    display.DisplayMethodParameter(
                        "how", tip="How to display the object")],
            accel='e',
            ellipsis=True,
            help= "Edit the currently selected layer.",
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/editlayer.xml')
                                      ))
        layermenu.addItem(OOFMenuItem(
            'Delete',
            callback=self.deleteLayerNumber,
            params=[IntParameter('n', 0, tip="Layer index.")],
            help="Delete the selected graphics layer.",
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/deletelayer.xml')
            ))
        layermenu.addItem(OOFMenuItem(
            'Select',
            callback=self.selectLayerCB,
            cli_only=1,
            # Running this command on the mainthread avoids a race
            # condition arising from double clicks on the layer list.
            # See the comment in GfxWindowBase.layerDoubleClickCB in
            # SRC/common/IO/GUI/gfxwindowbase.py.
            threadable=oofmenu.UNTHREADABLE,
            params=[IntParameter('n', 0, tip="Layer index.")],
            help="Select the given graphics layer.",
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/selectlayer.xml')
            ))
        layermenu.addItem(OOFMenuItem(
            'Deselect',
            callback=self.deselectLayerCB,
            cli_only=1,
            params=[IntParameter('n', 0, tip="Layer index.")],
            help="Deselect the given graphics layer.",
            discussion="""<para>
            See <xref linkend='MenuItem-OOF.Graphics_n.Layer.Select'/>.
            </para>"""))
        layermenu.addItem(OOFMenuItem(
            'Hide',
            callback=self.hideLayer,
            accel='h',
            params=[IntParameter('n', 0, tip="Layer index.")],
            help="Hide the selected graphics layer.",
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/hidelayer.xml')
            ))
        layermenu.addItem(OOFMenuItem(
            'Show',
            callback=self.showLayer,
            accel='s',
            params=[IntParameter('n', 0, tip="Layer index.")],
            help="Show the selected and previously hidden graphics layer.",
            discussion=xmlmenudump.loadFile(
                    'DISCUSSIONS/common/menu/showlayer.xml')
            ))
        layermenu.addItem(OOFMenuItem(
            'Freeze',
            callback=self.freezeLayer,
            params=[IntParameter('n', 0, tip="Layer index.")],
            help="Prevent the selected layer from being redrawn.",
            discussion=xmlmenudump.loadFile(
                    'DISCUSSIONS/common/menu/freezelayer.xml')
            ))
        layermenu.addItem(OOFMenuItem(
            'Unfreeze',
            callback=self.unfreezeLayer,
            params=[IntParameter('n', 0, tip="Layer index.")],
            help="Allow the selected layer to be redrawn.",
            discussion="""
<para>Undo the effect of <xref
linkend="MenuItem-OOF.Graphics_n.Layer.Freeze"/>.</para>
"""
            ))

        raisemenu = layermenu.addItem(OOFMenuItem(
            'Raise',
            help='Make a layer more visible.',
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/raiselayer.xml')
            ))
        raisemenu.addItem(OOFMenuItem(
            'One_Level',
            callback=self.raiseLayer,
            accel='r',
            params=[IntParameter('n', 0, tip="Layer index.")],
            help="Raise the selected graphics layer.",
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/raiseone.xml')
            ))
        raisemenu.addItem(OOFMenuItem(
            'To_Top',
            callback=self.raiseToTop,
            accel='t',
            params=[IntParameter('n', 0, tip="Layer index.")],
            help=\
            "Draw the selected graphics layer on top of all other layers.",
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/raisetop.xml')
            ))
        raisemenu.addItem(OOFMenuItem(
            'By',
            callback=self.raiseBy,
            #cli_only = 1,
            params=[
                IntParameter('n', 0, tip="Layer index."),
                IntParameter('howfar', 1, tip="How far to raise the layer.")
            ],
            help="Raise the selected graphics layer over a given number"
            " of other layers.",
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/raiseby.xml')
            ))
        lowermenu = layermenu.addItem(OOFMenuItem(
            'Lower',
            help='Make a layer less visible.',
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/lowerlayer.xml')
            ))
        lowermenu.addItem(OOFMenuItem(
            'One_Level',
            callback=self.lowerLayer,
            accel='l',
            params=[IntParameter('n', 0, tip="Layer index.")],
            help="Lower the selected graphics layer.",
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/lowerone.xml')
            ))
        lowermenu.addItem(OOFMenuItem(
            'To_Bottom',
            callback=self.lowerToBottom,
            accel='b',
            params=[IntParameter('n', 0, tip="Layer index.")],
            help="Draw the selected graphics layer below all other layers.",
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/lowerbtm.xml')
            ))
        lowermenu.addItem(OOFMenuItem(
            'By',
            callback=self.lowerBy,
            params=[
                IntParameter('n', 0, tip="Layer index."),
                IntParameter('howfar', 1, tip="How far to lower the layer.")
                    ],
            help="Lower the selected graphics layer under"
            " a given number of other layers.",
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/lowerby.xml')
            ))
        layermenu.addItem(OOFMenuItem(
            'Reorder_All',
            callback=self.reorderLayers,
            help="Put the graphics layers in their default order.",
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/reorderlayers.xml')
        ))
        settingmenu = self.menu.addItem(OOFMenuItem(
            'Settings',
            help='Control Graphics window behavior.',
            discussion="""<para>
            The <command>Settings</command> menu contains commands
            that set parameters that control the behavior of the
            Graphics window.
            </para>"""
        ))
        settingmenu.addItem(CheckOOFMenuItem(
            'Antialias',
            callback=self.toggleAntialias,
            value=self.settings.antialias,
            threadable=oofmenu.THREADABLE,
            help="Use antialiased rendering.",
            discussion=xmlmenudump.loadFile(
                    'DISCUSSIONS/common/menu/antialias.xml')
        ))
        settingmenu.addItem(OOFMenuItem(
            'New_Layer_Policy',
            callback=self.setNewLayerPolicy,
            params=[enum.EnumParameter('policy', NewLayerPolicy,
                                       value=self.settings.newlayerpolicy,
                                       tip=parameter.emptyTipString)],
            help="When to create new graphics layers.",
            discussion=xmlmenudump.loadFile(
                "DISCUSSIONS/common/menu/newlayerpolicy.xml")
        ))
        settingmenu.addItem(CheckOOFMenuItem(
            'List_All_Layers',
            callback=self.toggleListAll,
            value=self.settings.listall,
            help="List all graphics layers, even predefined ones.",
            discussion=xmlmenudump.loadFile(
                    'DISCUSSIONS/common/menu/listall.xml')
        ))
        settingmenu.addItem(CheckOOFMenuItem(
            'Long_Layer_Names',
            callback=self.toggleLongLayerNames,
            value=self.settings.longlayernames,
            help= "Use the long form of layer names in the layer list.",
            discussion=xmlmenudump.loadFile(
                    'DISCUSSIONS/common/menu/longlayers.xml')
        ))
        settingmenu.addItem(OOFMenuItem(
            'Time',
            callback=self.setTimeCB,
            params=[FloatParameter(
                'time', 0.0,
                tip='The time to use when displaying time-dependent layers.')
                    ],
            help='Set the time for display layers.',
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/settime.xml')
        ))
        settingmenu.addItem(OOFMenuItem(
            'Aspect_Ratio',
            callback=self.aspectRatio,
            params=[FloatParameter('ratio', 5.0,
                                   tip="Aspect ratio of the contour map.")],
            help="Set the aspect ratio of the contour map.",
            discussion="""<para>
            Set the aspect ratio (height/width) of the <link
            linkend='Section-Graphics-ContourMap'>contour map</link>
            display.
            </para>"""))

        settingmenu.addItem(OOFMenuItem(
            'Contourmap_Marker_Size',
            callback=self.contourmapMarkSize,
            ellipsis=1,
            params=[IntParameter('width',2,
                                 tip="Contour map marker line width.")],
            help="Width in pixels of the markers on the contour map.",
            discussion="""<para>
            Set the line <varname>width</varname>, in pixels, of the
            rectangle used to mark a region of the <link
            linkend='Section-Graphics-ContourMap'>contour map</link>.
            </para>"""))

        zoommenu = settingmenu.addItem(OOFMenuItem('Zoom',
                                    help="Change the scale in the display."))
        zoommenu.addItem(OOFMenuItem(
            'In',
            callback=self.zoomIn,
            accel='.',
            help='Magnify the image.',
            discussion="""<para>
            Magnify the graphics display by the current <link
            linkend='MenuItem-OOF.Graphics_n.Settings.Zoom.Zoom_Factor'>zoom
            factor</link>, keeping the center of the display fixed.
            </para>"""))
        zoommenu.addItem(OOFMenuItem(
            'InFocussed',
            callback=self.zoomInFocussed,
            secret=1,
            params=[primitives.PointParameter('focus',
                                              tip='Point to magnify about.')],
            help='Magnify the image about a mouse click.',
            discussion="""<para>
            Magnify the graphics display by the current <link
            linkend='MenuItem-OOF.Graphics_n.Settings.Zoom.Zoom_Factor'>zoom
            factor</link>, keeping the mouse click position fixed.
            </para>"""))
        zoommenu.addItem(OOFMenuItem(
            'Out',
            callback=self.zoomOut,
            accel=',',
            help='Demagnify by the current zoom factor.',
            discussion="""<para> 
            Demagnify the graphics display by the current <link
            linkend='MenuItem-OOF.Graphics_n.Settings.Zoom.Zoom_Factor'>zoom
            factor</link>, keeping the center of the display fixed.
            </para>"""))
        zoommenu.addItem(OOFMenuItem(
            'OutFocussed',
            callback=self.zoomOutFocussed,
            secret=1,
            params=[primitives.PointParameter('focus',
                                              tip='Point to demagnify about.')],
            help='Magnify the image about a mouse click.',
            discussion="""<para>
            Demagnify the graphics display by the current <link
            linkend='MenuItem-OOF.Graphics_n.Settings.Zoom.Zoom_Factor'>zoom
            factor</link>, keeping the mouse click position fixed.
            </para>"""))
        zoommenu.addItem(OOFMenuItem(
            'Fill_Window',
            callback=self.zoomFillWindow,
            accel='=',
            help='Fit the image to the window.',
            discussion="""<para>
            Zoom the display so that it fills the window.
            </para>"""))
        zoommenu.addItem(OOFMenuItem(
            'Zoom_Factor',
            callback = self.zoomfactorCB,
            params=[
            FloatParameter('factor', self.settings.zoomfactor,
                           tip="Zoom factor.")],
            ellipsis=1,
            help='Set the zoom magnification.',
            discussion="""<para>
            The scale of the display changes by
            <varname>factor</varname> or 1./<varname>factor</varname>
            when zooming in or out.
            </para>"""))
        colormenu = settingmenu.addItem(OOFMenuItem(
            'Color',
            help='Set the color of various parts of the display.'
            ))
        colormenu.addItem(OOFMenuItem(
            'Background',
            callback=self.bgColor,
            params=[color.OpaqueColorParameter(
                'color', self.settings.bgcolor,
                tip="Color for the background.")],
            ellipsis=1,
            help='Change the background color.',
            discussion="""<para>

            Set the background color for the main display and the
            contour map display.
            
            </para>"""))

        colormenu.addItem(OOFMenuItem(
            'Contourmap_Marker', 
            callback=self.contourmapMarkColor,
            params=[color.TranslucentColorParameter(
                'color', self.settings.contourmap_markercolor,
                tip="Color for the contour map marker.")],
            ellipsis=1,
            help="Change the contour map marker color.",
            discussion="""<para>
            Change the color of the position marker on the contourmap pane.
            </para>"""))

        settingmenu.addItem(OOFMenuItem(
            'Margin',
            callback=self.marginCB,
            params=[FloatParameter(
                'fraction', self.settings.margin,
                tip="Margin as a fraction of the image size.")],
            ellipsis=1,
            help= 'Set the margin (as a fraction of the image size)'
            ' when zooming to full size.',
            discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/common/menu/margin.xml')
        ))
        
        # Create toolboxes.
        self.toolboxes = []
        for tbc in toolbox.toolboxClasses:
            self.newToolboxClass(tbc)

        self.sensitize_menus()

        # If this is a clone, the cloning process will copy the
        # predefined layers from the original, and we don't have to
        # create them here.
        if not clone:
            self.createPredefinedLayers()

        # Switchboard callbacks.  Keep a list of them so that they can
        # all be removed when the window is closed.
        self.switchboardCallbacks = [
            switchboard.requestCallback('new who', self.newWho), # generic who
            switchboard.requestCallback('preremove who', self.removeWho),
            switchboard.requestCallback('new toolbox class',
                                        self.newToolboxClass),
            switchboard.requestCallback('deselect all gfxlayers',
                                        self.deselectAll),
            switchboard.requestCallback('redraw', self.draw),
            switchboard.requestCallback('draw at time', self.drawAtTime)
            ]

    def newCanvas(self):
        # Create the actual OOFCanvas object.  This method is
        # overridden in GfxWindow.  If this version is called, the
        # program is running in text mode. The canvas might be used to
        # generate image files, but isn't going to be displayed.
        return oofcanvas.OffScreenCanvas(100) # arg is ppu

    def newContourmapCanvas(self):
        # Redefined in GfxWindow, where it returns an on-screen canvas.
        return oofcanvas.OffScreenCanvas(100) # arg is ppu

    def new_contourmap_canvas(self):
        # Called by saveContourmap and, in GUI mode, by
        # makeContourMapWidgets.  In GUI mode this method is extended
        # in the derived class.
        if self.contourmapdata.canvas:
            self.contourmapdata.canvas.destroy()
        self.contourmapdata.canvas = self.newContourmapCanvas()
        self.contourmapdata.canvas.setBackgroundColor(
            color.canvasColor(self.settings.bgcolor))
        # Create two layers, one for the "main" drawing, and
        # one for the ticks.
        self.contourmapdata.canvas_mainlayer = \
            self.contourmapdata.canvas.newLayer("main")
        self.contourmapdata.canvas_ticklayer = \
            self.contourmapdata.canvas.newLayer("tick")

    def drawable(self):
        # Can any layer be drawn?  Used when testing the gui.
        ## TODO: Does this need a lock?  I haven't seen any gui
        ## testing errors that might be due to a missing lock.  The
        ## gtk2 version had a separate SLock that controlled access to
        ## the list of layers, and it was acquired here.  This is
        ## called from the main thread during gui tests, and can't use
        ## self.gfxlock, because that's not an SLock.
        for layer in self.layers:
            if not layer.incomputable(self):
                return True
        return False
        
    def __repr__(self):
        return 'GhostGfxWindow("%s")' % self.name

    def nLayers(self):
        return len(self.layers)

    def acquireGfxLock(self):
        if _debuglocks:
            debug.dumpCaller()
            debug.fmsg('------------------------ acquiring gfxlock', self.name)
        self.gfxlock.acquire()
        if _debuglocks:
            debug.fmsg('------------------------ acquired', self.name)
    def releaseGfxLock(self):
        if _debuglocks:
            debug.dumpCaller()
            debug.fmsg("------------------------ releasing gfxlock", self.name)
        self.gfxlock.release()

    def createPredefinedLayers(self):
        # Create pre-defined layers.  These are in all graphics
        # windows, regardless of whether or not they are drawable at
        # the moment.
        for predeflayer in PredefinedLayer.allPredefinedLayers:
            layer, who = predeflayer.createLayer()
            self.incorporateLayer(layer, who, autoselect=False, lock=False)
            
        # Create default layers if possible.  One layer is created for
        # each WhoClass the first time that an instance of that class
        # is created.
        self.createDefaultLayers()

    def createDefaultLayers(self, whoclassname=None, newwhopath=None):
        # If whoclassname and newwhopath are given, a new Who object
        # has just been created.  If they're not given, then this
        # window has just been created.

        # Do different things depending on newlayerpolicy:

        # newlayerpolicy == "Never":
        #   Don't do anything.
        
        # newlayerpolicy == "Always"

        #   If a new Who object has been created, add all
        #   DefaultLayers that apply to it.  "Always" only applies
        #   when a new Who object is created, not when a new gfx
        #   window is opened.

        # newlayerpolicy == "Single"

        #   If a new Who object has been created, add the relevant
        #   default layers if no non-proxy layer exists for any other
        #   Who object in the same class.
        
        #   If the window is new, create new layers if there's only
        #   one member of the relevant WhoClass.

        
        if self.settings.newlayerpolicy == "Never":
            return

        # Unselect all layers first, so that new layers don't
        # overwrite existing ones.
        selectedLayer = self.selectedLayer
        self.deselectAll()

        # Are we adding layers for a new Who object, or is this a new
        # graphics window?  If it's a new window, create default
        # layers for all existing who objects, consistent with the
        # current policy.
        if whoclassname is not None:
            # A new Who object may need to be displayed.
            whoclass = whoville.getClass(whoclassname)
            newwho = whoclass[newwhopath]
            assert newwho is not None
            # Add only the default layers that can display newwho.
            for defaultlayer in DefaultLayer.allDefaultLayers:
                # createLayer returns None if the given Who is the
                # wrong kind of Who (of Whom?).
                layer, who = defaultlayer.createLayer(newwho)
                if layer is not None:
                    if self.settings.newlayerpolicy == "Always":
                        self.incorporateLayer(layer, who, autoselect=False,
                                              lock=False)
                    elif self.settings.newlayerpolicy == "Single":
                        # See if there's already a layer displaying a
                        # non-proxy Who object of this type.
                        for oldlayer in self.layers:
                            if not isinstance(oldlayer.who, whoville.WhoProxy):
                                if oldlayer.who.getClassName() == whoclassname:
                                    break
                        else:
                            # No existing layer for this WhoClass
                            self.incorporateLayer(layer, who, autoselect=False,
                                                  lock=False)
        else:
            # whoclassname is None, so this is a new graphics window.
            if self.settings.newlayerpolicy == "Single":
                for defaultlayer in DefaultLayer.allDefaultLayers:
                    if defaultlayer.whoclass.nActual() == 1:
                        layer, who = defaultlayer.createLayer(
                            defaultlayer.whoclass.actualMembers()[0])
                        if layer is not None:
                            self.incorporateLayer(layer, who, autoselect=False,
                                                  lock=False)

        # Restore the previous selection state.
        if selectedLayer:
            self.selectLayer(self.layerID(selectedLayer))
                
    def sensitize_menus(self):
        ## TODO?: There appears to be a problem with the timing of
        ## double clicks in the LayerList --- can one thread be inside
        ## sensitize_menus() while another thread is setting
        ## self.selectedLayer to None?  Does there need to be a lock
        ## on self.selectedLayer? (Not sure if this is still a problem...)
        if self.selectedLayer is not None and \
               (self.selectedLayer.listed or self.settings.listall):
            self.menu.Layer.Delete.enable()
            self.menu.Layer.Edit.enable()
            if self.selectedLayer.hidden:
                self.menu.Layer.Show.enable()
                self.menu.Layer.Hide.disable()
            else:
                self.menu.Layer.Show.disable()
                self.menu.Layer.Hide.enable()
            if self.layerID(self.selectedLayer) == 0:
                self.menu.Layer.Lower.disable()
            else:
                self.menu.Layer.Lower.enable()
            if self.layerID(self.selectedLayer) == self.nLayers()-1:
                self.menu.Layer.Raise.disable()
            else:
                self.menu.Layer.Raise.enable()

            if self.selectedLayer.frozen:
                self.menu.Layer.Unfreeze.enable()
                self.menu.Layer.Freeze.disable()
            else:
                self.menu.Layer.Freeze.enable()
                self.menu.Layer.Unfreeze.disable()
        else:
            self.menu.Layer.Delete.disable()
            self.menu.Layer.Raise.disable()
            self.menu.Layer.Lower.disable()
            self.menu.Layer.Show.disable()
            self.menu.Layer.Hide.disable()
            self.menu.Layer.Freeze.disable()
            self.menu.Layer.Unfreeze.disable()
            self.menu.Layer.Edit.disable()
        if self.nLayers() == 0:
            self.menu.Settings.Zoom.disable()
        else:
            self.menu.Settings.Zoom.enable()

        if self.sortedLayers():
            self.menu.Layer.Reorder_All.disable()
        else:
            self.menu.Layer.Reorder_All.enable()

        if self.current_contourmap_method is not None:
            self.menu.File.Save_Contourmap.enable()
        else:
            self.menu.File.Save_Contourmap.disable()

        if self.oofcanvas.empty():
            self.menu.File.Save_Canvas.disable()
            self.menu.File.Save_Canvas_Region.disable()
        else:
            self.menu.File.Save_Canvas.enable()
            self.menu.File.Save_Canvas_Region.enable()

    def getLayerChangeTimeStamp(self):
        return self.layerChangeTime
        
    ##############################

    # Menu callbacks.

    def newLayerCB(self, menuitem, category, what, how):
        whoclass = whoville.getClass(category)
        who = whoclass[what]
        self.selectedLayer = None
        self.incorporateLayer(how, who)

    def editLayerCB(self, menuitem, n, category, what, how):
        whoclass = whoville.getClass(category)
        who = whoclass[what]
        # If the edit command is run from a script, self.selectedLayer
        # might not be the nth layer, which is the one being edited.
        # So make sure it's selected, then call incorporateLayer,
        # which will replace it.
        self.selectedLayer = self.layers[n]
        self.incorporateLayer(how, who)

    ## TODO PYTHON3: Add GUI test for cloning a graphics window
    def cloneWindow(self, *args):
        self.acquireGfxLock()
        try:
            clone = self.gfxmanager.openWindow(clone=True,
                                               settings=self.settings.clone())
            # clone.settings = self.settings.clone()
            # ## TODO PYTHON3: Copying the cloned settings here doesn't
            # ## actually change anything in the window -- it doesn't
            # ## call the relevant oofcanvas routines, for example.  The
            # ## settings need to be passed in as arguments to the
            # ## constructor.
            for layer in self.layers:
                clone.incorporateLayer(layer.clone(), layer.who)
                clone.deselectLayer(clone.selectedLayerNumber())
            if self.selectedLayer is not None:
                clone.selectLayer(self.layerID(self.selectedLayer))
            return clone
        finally:
            self.releaseGfxLock()

    def close(self, menuitem, *args):
        self.acquireGfxLock()
        try:
            self.gfxmanager.closeWindow(self)

            # Things can be shut down via several pathways (ie, from
            # scripts or gtk events), so at each step we have to make sure
            # that the step won't be repeated.  This function has been
            # called from the menus, so here we turn off the menu
            # callback.
            menuitem.callback = None

            for callback in self.switchboardCallbacks:
                switchboard.removeCallback(callback)
            self.switchboardCallbacks = []

            for toolbox in self.toolboxes:
                toolbox.close()

            self.layers = []

            # cleanup to prevent possible circular references
            ## del self.display
            del self.gfxmanager
            self.menu.clearMenu()
            OOF.Windows.Graphics.removeItem(self.name)
            OOF.removeItem(self.name)
            self.menu = None
            del self.selectedLayer
            del self.toolboxes
        finally:
            self.releaseGfxLock()

    def clear(self, *args, **kwargs):
        # Remove all user specified layers from the display.
        self.acquireGfxLock()
        try:
            keptlayers = []
            for layer in self.layers:
                if layer.listed:
                    if layer is self.selectedLayer:
                        self.selectedLayer = None
                    layer.destroy()
                else:
                    keptlayers.append(layer)
            self.layers = keptlayers
        finally:
            self.releaseGfxLock()
        self.layersHaveChanged()

    def draw(self, *args, **kwargs):
        pass

    def drawAtTime(self, *args, **kwargs):
        pass

    def animate(self, *args, **kwargs):
        pass

    # def backdate(self):
    #     # Backdate timestamps on the local display.
    #     self.acquireGfxLock()
    #     try:
    #         self.display.clear()  
    #     finally:
    #         self.releaseGfxLock()
        
    def redraw(self, menuitem):
        self.acquireGfxLock()
        try:
            mainthread.runBlock(self.redraw_mainthread)
        finally:
            self.releaseGfxLock()
        self.draw()

    def redraw_mainthread(self):
        for layer in self.layers:
            ## TODO: This redraws the Cairo layers without
            ## reconstructing them.  Do we want to reconstruct them,
            ## ie. have the DisplayLayers recompute themselves?
            layer.canvaslayer.markDirty();
            layer.canvaslayer.render()

    def setTimeCB(self, menuitem, time):
        self.setDisplayTime(time)

    def setDisplayTime(self, time):
        if time != self.displayTime:
            self.displayTime = time
            self.displayTimeChanged.increment()
            switchboard.notify((self, "time changed"))

    def toggleAntialias(self, menuitem, antialias):
        self.settings.antialias = antialias
        # Swigged functions like setAntialias require their boolean
        # args to be actual bools, but gtk3 sets antialias to either 0
        # or 1.
        self.oofcanvas.setAntialias(bool(antialias))

    def toggleContourpane(self, menuitem, contourpane):
        self.settings.showcontourpane = contourpane

    def toggleListAll(self, menuitem, listall):
        self.acquireGfxLock()
        try:
            self.settings.listall = listall
            self.sensitize_menus()
            self.fillLayerList()
        finally:
            self.releaseGfxLock()

    def setNewLayerPolicy(self, menuitem, policy):
        self.settings.newlayerpolicy = policy

    def fillLayerList(self):
        # Redefined in GfxWindowBase class.
        pass

    def toggleLongLayerNames(self, menuitem, longlayernames):
        self.settings.longlayernames = longlayernames
        
    def aspectRatio(self, menuitem, ratio):
        self.settings.aspectratio = ratio
        
    def contourmapMarkSize(self, menuitem, width):
        self.settings.contourmap_markersize = width

    def contourmapMarkColor(self, menuitem, color):
        self.settings.contourmap_markercolor = color

    def contourmapBGColor(self, menuitem, color):
        self.settings.contourmap_bgcolor = color

    def contourmapTextColor(self, menuitem, color):
        self.settings.contourmap_textcolor = color
        
    def zoomIn(self, *args, **kwargs):
        pass
    def zoomOut(self, *args, **kwargs):
        pass
    def zoomInFocussed(self, *args, **kwargs):
        pass
    def zoomOutFocussed(self, *args, **kwargs):
        pass
    def zoomFillWindow(self, *args, **kwargs):
        pass

    def bgColor(self, menuitem, color):
        self.settings.bgcolor = color

    def marginCB(self, menuitem, fraction):
        self.settings.margin = fraction
        self.draw()

    def contourpanewidthCB(self, menuitem, fraction):
        self.settings.contourpanewidth = fraction

    def zoomfactorCB(self, menuitem, factor):
        self.settings.zoomfactor = factor
        switchboard.notify("zoom factor changed")

    def drawLayers(self):
        self.acquireGfxLock()
        try:
            for layer in self.layers:
                reason = layer.incomputable(self)
                if reason:
                    layer.clear()
                else:
                    try:
                        # Tell the DisplayLayer to (re)create its
                        # OOFCanvas::CanvasLayer.
                        layer.drawIfNecessary(self)
                    except subthread.StopThread:
                        return
                    except Exception as exc:
                        debug.fmsg('Exception while drawing!', exc)
                        if debug.debug():
                            traceback.print_exc()
                        raise
        finally:
            self.releaseGfxLock()

    def saveCanvas(self, menuitem, filename, format, overwrite,
                   pixels, background):
        if overwrite or not os.path.exists(filename):
            self.drawLayers()
            assert not self.oofcanvas.empty()
            if format == "pdf":
                if not self.oofcanvas.saveAsPDF(filename, pixels, background):
                    raise ooferror.PyErrUserError("Cannot save canvas!")
            elif format == "png":
                if not self.oofcanvas.saveAsPNG(filename, pixels, background):
                    raise ooferror.PyErrUserError("Cannot save canvas!")
            elif format == "datadump":
                self.oofcanvas.datadump(filename)

    def saveCanvasRegion(self, menuitem, filename, format, overwrite,
                         pixels, background, lowerleft, upperright):
        if overwrite or not os.path.exists(filename):
            self.drawLayers()
            assert not self.oofcanvas.empty()
            if format == "pdf":
                if not self.oofcanvas.saveRegionAsPDF(
                        filename, pixels, background, lowerleft, upperright):
                    raise ooferror.PyErrUserError("Cannot save canvas region!")
            elif format == "png":
                if not self.oofcanvas.saveRegionAsPNG(
                        filename, pixels, background, lowerleft, upperright):
                    raise ooferror.PyErrUserError("Cannot save canvas region!")

    def saveContourmap(self, menuitem, filename, format, overwrite, pixels):
        assert self.current_contourmap_method is not None
        if overwrite or not os.path.exists(filename):
            # In text mode, the contourmap canvas might not exist
            if self.contourmapdata.canvas is None:
                mainthread.runBlock(self.new_contourmap_canvas)
                # Can't draw the contourmap until the contour plot has
                # been drawn, because the limits aren't known.
                self.drawLayers() # draws contour plot
                self.current_contourmap_method.draw_contourmap(
                    self, self.contourmapdata.canvas_mainlayer)
            if format == "pdf":
                if not self.contourmapdata.canvas.saveAsPDF(
                        filename, pixels, False):
                    raise ooferror.PyErrUserError(
                        "Cannot save canvas contour map!")
            elif format == "png":
                if not self.contourmapdata.canvas.saveAsPNG(
                    filename, pixels, False):
                    raise ooferror.PyErrUserError(
                        "Cannot save canvas contour map!")

    ###############################

    # Returns the index of the layer in the list.
    def layerID(self, layer):
        try:
            return self.layers.index(layer)
        except ValueError:
            debug.fmsg("Can't find layer", layer)
            raise

    def getLayer(self, layerNumber):
        return self.layers[layerNumber]

    def topwho(self, *whoclasses):
        for layer in reversed(self.layers):
            if layer.who is not None:
                classname = layer.who.getClassName()
                if ((not isinstance(layer.who, whoville.WhoProxy)) and
                    not layer.hidden and
                    classname in whoclasses):
                    return layer.who

    # Advanced function, returns a reference to the *layer* object
    # which draws the who object referred to.
    def topwholayer(self, *whoclasses):
        for layer in reversed(self.layers):
            if layer.who is not None:
                classname = layer.who.getClassName()
                if ((not isinstance(layer.who, whoville.WhoProxy)) and
                    not layer.hidden and
                    classname in whoclasses):
                    return layer

    def topmost(self, *whoclasses):
        # Find the topmost layer whose 'who' belongs to the given
        # whoclass.  Eg, topmost('Image') returns the topmost image.
        who = self.topwho(*whoclasses)
        if who is not None:
            return who.getObject(self)

    def topMethod(self, *displaymethods):
        # Is this used?
        for layer in reversed(self.layers):
            if isinstance(layer, displaymethods):
                return layer

    #################################

    # Function for doing book-keeping whenever the list of layers has
    # changed.  Overridden in gfxwindow to update the layer list and
    # the time controls as well.
    def layersHaveChanged(self):
        self.layerChangeTime.increment()
        switchboard.notify((self, 'layers changed'))
        new_contourmap_method = self.topcontourable()
        if new_contourmap_method != self.current_contourmap_method:
            self.current_contourmap_method = new_contourmap_method
            switchboard.notify((self, "new contourmap layer"))

        # Sync layer order in the canvas the the order in self.layers
        self.oofcanvas.reorderLayers(
            [l.canvaslayer for l in self.layers])
        
        self.draw()
        self.sensitize_menus()  # must be called last

    def incorporateLayer(self, layer, who, autoselect=True, lock=True):
        if lock:
            self.acquireGfxLock()
        try:
            if self.selectedLayer:
                if (self.selectedLayer.equivalent(layer) and
                    who is self.selectedLayer.who):
                    return
                # Replace the selected layer with the new layer.
                which = self.layerID(self.selectedLayer)
                layer.frozen = self.selectedLayer.frozen
                oldlayer = self.selectedLayer
                self.layers[which] = layer
                # Do not call self.selectLayer here.  It'll try to
                # call deselectLayer() on the previous selection,
                # which is no longer in the list.  It also does
                # too much in the way of switchboard and gui
                # callbacks.
                self.selectedLayer = layer
                layer.build(self) # creates OOFCanvas::CanvasLayer
                layer.setWho(who)
                oldlayer.destroy()
            else:
                # There's no selected layer. Add the new layer.  Add
                # the new layer at the lowest position such that its
                # sorting order is below all the layers above it.
                # That is, the layer won't be hidden by the layers
                # above it, and if possible it won't hide layers
                # below.
                if not self.layers:
                    self.layers.append(layer)
                else:
                    for i in reversed(range(len(self.layers))):
                        if (layer.layerordering() >=
                            self.layers[i].layerordering()):
                            # The new layer belongs above layer i.
                            self.layers[i+1:i+1] = [layer]
                            break
                    else:
                        self.layers[0:0] = [layer]
                            
                layer.build(self)
                layer.setWho(who)
                if autoselect:
                    self.selectLayer(self.layerID(layer))
        finally:
            if lock:
                self.releaseGfxLock()
        self.layersHaveChanged()

    def sortedLayers(self):
        # Are the layers in a canonical order?
        for i in range(1, len(self.layers)):
            if (self.layers[i-1].layerordering() >
                self.layers[i].layerordering()):
                return False
        return True
            
    def deleteLayerNumber(self, menuitem, n):
        self.acquireGfxLock()
        try:
            layer = self.layers[n]
            if layer is self.selectedLayer:
                self.selectedLayer = None
            layer.destroy()
            del self.layers[n]
        finally:
            self.releaseGfxLock()
        self.layersHaveChanged()

    def newLayer(self, displaylayer):
        pass

    def hideLayer(self, menuitem, n):
        self.layers[n].hide()
        self.layersHaveChanged()

    def showLayer(self, menuitem, n):
        self.layers[n].show()
        self.layersHaveChanged()

    def freezeLayer(self, menuitem, n):
        self.layers[n].freeze(self)
        self.sensitize_menus()
    def unfreezeLayer(self, menuitem, n):
        self.layers[n].unfreeze(self)
        self.sensitize_menus()
        self.draw()

    # Topmost layer on which contours can be drawn -- such a layer
    # must have a mesh as its "who".
    def topcontourable(self):
        for layer in reversed(self.layers):
            if layer.contour_capable(self) and not layer.hidden:
                return layer
            
    def selectLayer(self, n):
        if n is not None:
            self.selectedLayer = self.layers[n]
            self.sensitize_menus()
    def deselectLayer(self, n):
        if (self.selectedLayer is not None and 
            self.layerID(self.selectedLayer) == n):
            self.selectedLayer = None
            self.sensitize_menus()
    def deselectAll(self):
        if self.selectedLayer is not None:
            self.selectedLayer = None
            self.sensitize_menus()
    def selectedLayerNumber(self):
        if self.selectedLayer is not None:
            return self.layerID(self.selectedLayer)

    def selectLayerCB(self, menuitem, n):
        self.selectLayer(n)
    def deselectLayerCB(self, menuitem, n):
        self.deselectLayer(n)

    def raiseLayerBy(self, n, howfar):
        # n is the layer number
        self.acquireGfxLock()
        try:
            if howfar > 0 and 0 <= n < self.nLayers()-howfar:
                thislayer = self.layers[n]
                for i in range(howfar):
                    self.layers[n+i] = self.layers[n+i+1]
                self.layers[n+howfar] = thislayer
                thislayer.raise_layer(howfar)
            else:
                return
        finally:
            self.releaseGfxLock()
        self.layersHaveChanged()

    def raiseLayer(self, menuitem, n):
        self.raiseLayerBy(n, 1)
        
    def raiseToTop(self, menuitem, n):
        self.raiseLayerBy(n, self.nLayers()-n-1)

    def raiseBy(self, menuitem, n, howfar):
        self.raiseLayerBy(n, howfar)

    def lowerLayerBy(self, n, howfar):
        # n is the layer number
        self.acquireGfxLock()
        try:
            if howfar > 0 and howfar <= n < self.nLayers():
                thislayer = self.layers[n]
                for i in range(howfar):
                    self.layers[n-i] = self.layers[n-i-1]
                self.layers[n-howfar] = thislayer
                thislayer.lower_layer(howfar)
            else:
                return
        finally:
            self.releaseGfxLock()
        self.layersHaveChanged()

    def lowerLayer(self, menuitem, n):
        self.lowerLayerBy(n, 1)
        
    def lowerToBottom(self, menuitem, n):
        self.lowerLayerBy(n, n)

    def lowerBy(self, menuitem, n, howfar):
        self.lowerLayerBy(n, howfar)

    def reorderLayers(self, menuitem):
        self.layers.sort(key=lambda x: x.layerordering())
        self.layersHaveChanged()

    def listedLayers(self):             # for testing
        result = []
        for layer in self.layers:
            if layer.listed:
                result.append(layer)
        return result
                
    def findAnimationTimes(self):
        # Return a list of all possible times that can appear in an
        # animation, by asking the unfrozen AnimationLayers for their
        # times.
        times = set()
        for layer in self.layers:
            if (isinstance(layer, display.AnimationLayer) 
                and layer.animatable(self)):
                when = layer.getParamValue('when')
                if when is placeholder.latest:
                    times.update(layer.animationTimes(self))
        times = sorted(times)
        return times

    def latestTime(self):
        times = self.findAnimationTimes()
        if times:
            return max(times)
        return None

    def dumpLayers(self, menuitem, filename):
        for i, layer in enumerate(self.layers):
            if not layer.empty():
                fname = filename + '%02d' % i + ".png"
                print("Saving layer", layer.short_name(), "as", fname)
                layer.canvaslayer.writeToPNG(fname)
            

    #####################################

    # switchboard callbacks

    def newWho(self, classname, whopath):
        # A new Who (layer context) has been created.  Display it
        # automatically, if nothing else is displayed.
        self.createDefaultLayers(classname, whopath)
        ## Don't call self.draw() here!  It should only be called when
        ## a menu item issues the "redraw" switchboard signal.
        ## Otherwise it can be called too often (such as when one menu
        ## item creates more than one new Who object).
        
    def removeWho(self, whoclassname, whoname):
        path = labeltree.makePath(whoname)
        defunctLayers = []
        for layer in self.layers:
            layerpath = labeltree.makePath(layer.who.path())
            if (layer.who.getClass().name() == whoclassname and
                layerpath == path):
                if layer is self.selectedLayer:
                    self.selectedLayer = None
                layer.setWho(None)
                defunctLayers.append(layer)
        # Don't use layer.getWho() here, because that tries to resolve
        # proxies in the graphics window.  We are just checking to see
        # if who was set to None in the loop above.
        self.layers = [layer for layer in self.layers
                       if layer.who is not None]
        for layer in defunctLayers:
            layer.destroy()

        self.layersHaveChanged()

        
    def newToolboxClass(self, tbclass):
        tb = tbclass(self)              # constructs toolbox
        self.toolboxes.append(tb)
        menu = self.toolboxmenu.addItem(OOFMenuItem(tb.name(),
                                                    help=tb.tip,
                                                    discussion=tb.discussion))
        menu.data = tb
        tb.makeMenu(menu)

    def getToolboxByName(self, name):
        for toolbox in self.toolboxes:
            if toolbox.name() == name:
                return toolbox

#########################################

# An imported module can define a default layer for a graphics window
# by instantiating the DefaultLayer class.  Default layers are drawn
# in a new grraphics window if there is exactly one instance of the
# WhoClass which they display, or if an object of the appropriate
# WhoClass is passed in to the createLayer method.

class DefaultLayer:
    allDefaultLayers = []
    def __init__(self, whoclass, displaymethodfn):
        DefaultLayer.allDefaultLayers.append(self)
        self.whoclass = whoclass
        self.displaymethodfn = displaymethodfn

    def createLayer(self, who):
        assert who is not None # used to be allowed
        if who.getClass() is self.whoclass:
            return (self.displaymethodfn(), who)
        return (None, None)

# Predefined layers are created whenever a graphics window is opened
# by GhostGfxWindow.createPredefinedLayers(), without checking for the
# existence of an object in the WhoClass.  They are automatically
# unlisted.

class PredefinedLayer:
    allPredefinedLayers = []
    def __init__(self, whoclassname, path, displaymethodfn):
        PredefinedLayer.allPredefinedLayers.append(self)
        self.whoclass = whoville.getClass(whoclassname)
        self.path = path
        self.displaymethodfn = displaymethodfn
    def createLayer(self):
        displaymethod = self.displaymethodfn()
        displaymethod.listed = 0
        return displaymethod, self.whoclass[self.path]

################################################

## Set default values for the gfx window size.  This isn't handled by
## GfxSettings, because the window size isn't set in the window's own
## settings menu.

def _setDefaultGfxSize(menuitem, width, height):
    GhostGfxWindow.initial_width = width
    GhostGfxWindow.initial_height = height

mainmenu.gfxdefaultsmenu.addItem(oofmenu.OOFMenuItem(
    'Window_Size',
    callback=_setDefaultGfxSize,
    ordering=0,
    params=[parameter.IntParameter('width',
                                   GhostGfxWindow.initial_width,
                                   tip="Window width in pixels."),
            parameter.IntParameter('height',
                                   GhostGfxWindow.initial_height,
                                   tip="Window height in pixels.")],
    help="Set the initial size of graphics windows.",
    discussion="<para> Set the initial size of graphics windows. </para>"
    ))

##########

# Global default setting for the new layer policy.  This applies to
# all new windows, not existing ones.

def _setDefaultNewLayerPolicy(menuitem, policy):
    default_settings["newlayerpolicy"] = policy

mainmenu.gfxdefaultsmenu.addItem(oofmenu.OOFMenuItem(
    'New_Layer_Policy',
    callback=_setDefaultNewLayerPolicy,
    params=[enum.EnumParameter(
        'policy', NewLayerPolicy,
        value=default_settings["newlayerpolicy"],
        tip='New layer policy for newly created windows.')],
    help = "When to create new graphics layers in new windows.",
    discussion=xmlmenudump.loadFile(
        "DISCUSSIONS/common/menu/defaultnewlayerpolicy.xml")
))
