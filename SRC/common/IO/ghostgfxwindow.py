# -*- python -*-
# $RCSfile: ghostgfxwindow.py,v $
# $Revision: 1.188 $
# $Author: langer $
# $Date: 2011/04/11 21:45:18 $


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

from ooflib.SWIG.common import config
from ooflib.SWIG.common import lock
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
from ooflib.common.IO import outputdevice
from ooflib.common.IO import parameter
from ooflib.common.IO import pdfoutput
from ooflib.common.IO import placeholder
from ooflib.common.IO import whoville
from ooflib.common.IO import xmlmenudump
from types import *
import copy
import os.path
import string
import sys

FloatParameter = parameter.FloatParameter
IntParameter = parameter.IntParameter
StringParameter = parameter.StringParameter

OOF = mainmenu.OOF
OOFMenuItem = oofmenu.OOFMenuItem
CheckOOFMenuItem = oofmenu.CheckOOFMenuItem

# Since debugging the locking code here is a fairly common
# requirement, and commenting out the debugging lines is a pain, they
# can all be turned on and off by setting _debuglocks.
_debuglocks = False

# TODO 3D: in 3D and in oof 3.0, the division between ghostgfxwindow
# and the regular gfxwindow will probably not be necessary -- we still
# need a vtkRenderWindow to save images, even if we don't display it
# on the screen.  It will also be simplified by not using a pdf device
# and separate device for the contourmap.

#######################################

class GfxSettings:
    # Stores all the settable parameters for a graphics
    # window. Variables defined at the class level are the default
    # values. Assigning to a variable sets *both* the instance and
    # default values.  Therefore a new window will always use the
    # latest settings.

    ## TODO: Use Python properties, instead of __setattr__.

    bgcolor = color.white
    zoomfactor = 1.5
    margin = 0.05
    longlayernames = 0                   # Use long form of layer reprs.
    listall = 0                          # are all layers to be listed?
    autoreorder = 1                      # automatically reorder layers?
    antialias = 0
    if config.dimension() == 2:
        aspectratio = 5                      # Aspect ratio of the contourmap.
        contourmap_markersize = 2            # Size in pixels of contourmap marker.
        contourmap_markercolor = color.gray50 # Color of contourmap position marker.
    elif config.dimension() == 3:
        showcontourpane = 1
        contourmap_bgcolor = color.white
        contourmap_textcolor = color.black
        contourpanewidth = .1
    def __init__(self):
        # Copy all default (class) values into local (instance) variables.
        self.__dict__['timestamps'] = {}
        for key,val in GfxSettings.__dict__.items():
            # Exclude '__module__', etc, as well as all methods (such
            # as getTimeStamp).  Because (apparently) we're accessing
            # the methods via the dictionary, they're not recognized
            # as methods, and we have to check for FunctionType
            # instead of MethodType or UnboundMethodType.
            if key[0] != '_' and type(val) is not FunctionType:
                self.__dict__[key] = val
                self.timestamps[key] = timestamp.TimeStamp()
    def __setattr__(self, attr, val):
        self.__dict__[attr] = val       # local value
        GfxSettings.__dict__[attr] = val # default value
        self.timestamps[attr].increment()
    def getTimeStamp(self, attr):
        return self.timestamps[attr]


# Modules (eg, image or engine) can add graphics window settings by
# calling defineGfxSetting().  They should do this at initialization
# time, before any graphics windows are created.  defineGfxSetting
# does *not* create a menu item or callback for the setting.  That
# must be done by catching the "open graphics window" switchboard
# signal.

def defineGfxSetting(name, val):
    GfxSettings.__dict__[name] = val

#######################################

class GhostGfxWindow:
    initial_height = 400
    initial_width = 800
    def __init__(self, name, gfxmanager, clone=0):
        self.name = name
        self.gfxmanager = gfxmanager
        self.display = display.Display()
        if not hasattr(self, 'device'): # may have already been set by GfxWindow
            self.device = outputdevice.NullDevice()
        if not hasattr(self, 'gfxlock'): # ditto
            self.gfxlock = lock.Lock()
        self.layerSets = []
        self.current_contourmap_method = None
        self.selectedLayer = None
        self.displayTime = 0.0
        self.displayTimeChanged = timestamp.TimeStamp()
        if not hasattr(self, 'settings'):
            self.settings = GfxSettings()

        self.menu = OOF.addItem(OOFMenuItem(
            self.name,
            secret=1,
            help = "Commands dependent on a particular Graphics window.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/graphics.xml')
            ))

        # Put this window into the Windows/Graphics menu, so that it
        # can be raised in graphics mode.  Since this isn't meaningful
        # in text mode, there's no callback defined here.
        OOF.Windows.Graphics.addItem(OOFMenuItem(
            self.name,
            help="Raise the window named %s." % name, 
            gui_only=1,
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/graphicsraise.xml')
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
            window</link>.  All the settings and <link
            linkend='Section-Graphics-Layer'>layers</link> will be
            duplicated as well.
            </para>"""
            ))
        filemenu.addItem(OOFMenuItem(
            'Save_Image',
            callback=self.saveImage,
            ellipsis=1,
            params=[filenameparam.WriteFileNameParameter(
                        'filename', ident='gfxwindow',
                        tip="Name for the image file."),
                    filenameparam.OverwriteParameter(
                        'overwrite',
                        tip="Overwrite an existing file?")],
            help="Save the contents of the graphics window as a pdf file.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/graphicssave.xml')
            ))
        if config.dimension() == 2:
            filemenu.addItem(OOFMenuItem(
                'Save_Contourmap',
                callback=self.saveContourmap,
                ellipsis=1,
                params=[filenameparam.WriteFileNameParameter(
                            'filename', ident='gfxwindow',
                            tip="Name for the image file."),
                        filenameparam.OverwriteParameter(
                            'overwrite', tip="Overwrite an existing file?"
                            )],
                help="Save a pdf image of the contour map.",
                discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/graphicssavecontour.xml')))
        filemenu.addItem(OOFMenuItem(
            'Clear',
            callback=self.clear,
            help="Remove all user-defined graphics layers.",
            discussion = xmlmenudump.loadFile('DISCUSSIONS/common/menu/graphicsclear.xml')
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

        ## This had been marked UNTHREADABLE.  Why?  Making it
        ## unthreaded makes it hang when executed while drawing.
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
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/toolbox.xml')
            ))
        layermenu = self.menu.addItem(OOFMenuItem(
            'Layer',
            help='Commands for manipulating graphics layers.',
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/layer.xml')
            ))

        # Layer editing is invoked either through the GUI version of
        # this menu item, or by double clicking on a layer in the
        # GUI's layer list.  In either case, the scripted command is a
        # *LayerEditor* command, not a GhostGfxWindow command, so
        # there's nothing to do here.  This menu item is here just so
        # that the GfxWindow can hang a gui_callback on it.
        layermenu.addItem(OOFMenuItem(
            'New',
            gui_only=1,
            accel='n',
            ellipsis=1,
            help="Open the graphics layer editor.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/newlayer.xml')
            ))
        layermenu.addItem(OOFMenuItem(
            'Edit',
            gui_only=1,
            accel='e',
            ellipsis=1,
            help= "Open the graphics layer editor, loading the currently selected layer.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/editlayer.xml')
                                      ))
        layermenu.addItem(OOFMenuItem(
            'Delete',
            callback=self.deleteLayerNumber,
            params=[IntParameter('n', 0, tip="Layer index.")],
            help="Delete the selected graphics layer.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/deletelayer.xml')
            ))
        layermenu.addItem(OOFMenuItem(
            'Select',
            callback=self.selectLayerCB,
            cli_only=1,
            params=[IntParameter('n', 0, tip="Layer index.")],
            help="Select the given graphics layer.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/selectlayer.xml')
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
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/hidelayer.xml')
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

        if config.dimension() == 2:
            layermenu.addItem(OOFMenuItem(
                'Hide_Contour_Map',
                callback=self.hideLayerContourmap,
                params=[IntParameter('n',0,tip="Contour map index.")],
                help="Hide the selected layer's contour map.",
                discussion=xmlmenudump.loadFile(
                        'DISCUSSIONS/common/menu/hidecontour.xml')
                ))
            layermenu.addItem(OOFMenuItem(
                'Show_Contour_Map',
                callback=self.showLayerContourmap,
                params=[IntParameter('n',0, tip="Contour map index.")],
                help="Show the selected layer's contour map.",
                discussion="""<para>
                See <xref
                linkend='MenuItem-OOF.Graphics_n.Layer.Hide_Contour_Map'/>.
                </para>"""
                ))
        raisemenu = layermenu.addItem(OOFMenuItem(
            'Raise',
            help='Make a layer more visible.',
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/raiselayer.xml')
            ))
        raisemenu.addItem(OOFMenuItem(
            'One_Level',
            callback=self.raiseLayer,
            accel='r',
            params=[IntParameter('n', 0, tip="Layer index.")],
            help="Raise the selected graphics layer.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/raiseone.xml')
            ))
        raisemenu.addItem(OOFMenuItem(
            'To_Top',
            callback=self.raiseToTop,
            accel='t',
            params=[IntParameter('n', 0, tip="Layer index.")],
            help=\
            "Draw the selected graphics layer on top of all other layers.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/raisetop.xml')
            ))
        raisemenu.addItem(OOFMenuItem(
            'By',
            callback=self.raiseBy,
            cli_only = 1,
            params=[IntParameter('n', 0, tip="Layer index."),
                    IntParameter('howfar', 1, tip="How far to raise the layer.")
                    ],
            help="Raise the selected graphics layer over a given number of other layers.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/raiseby.xml')
            ))
        lowermenu = layermenu.addItem(OOFMenuItem(
            'Lower',
            help='Make a layer less visible.',
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/lowerlayer.xml')
            ))
        lowermenu.addItem(OOFMenuItem(
            'One_Level',
            callback=self.lowerLayer,
            accel='l',
            params=[IntParameter('n', 0, tip="Layer index.")],
            help="Lower the selected graphics layer.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/lowerone.xml')
            ))
        lowermenu.addItem(OOFMenuItem(
            'To_Bottom',
            callback=self.lowerToBottom,
            accel='b',
            params=[IntParameter('n', 0, tip="Layer index.")],
            help="Draw the selected graphics layer below all other layers.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/lowerbtm.xml')
            ))
        lowermenu.addItem(OOFMenuItem(
            'By',
            callback=self.lowerBy,
            cli_only = 1,
            params=[IntParameter('n', 0, tip="Layer index."),
                    IntParameter('howfar', 1, tip="How far to lower the layer.")
                    ],
            help="Lower the selected graphics layer under a given number of other layers.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/lowerby.xml')
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
            help=
            "Use antialiased rendering.",
            discussion=xmlmenudump.loadFile(
                    'DISCUSSIONS/common/menu/antialias.xml')
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
        settingmenu.addItem(CheckOOFMenuItem(
            'Auto_Reorder',
            callback=self.toggleAutoReorder,
            value=self.settings.autoreorder,
            help="Automatically reorder layers when new layers are created.",
            discussion=xmlmenudump.loadFile(
                    'DISCUSSIONS/common/menu/autoreorder.xml')
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
        if config.dimension() == 2:
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
            params=[color.ColorParameter('color', self.settings.bgcolor,
                                         tip="Color for the background.")],
            ellipsis=1,
            help='Change the background color.',
            discussion="""<para>

            Set the background color for the main display and the
            contour map display.
            
            </para>"""))
        if config.dimension() == 2:
            colormenu.addItem(OOFMenuItem(
                'Contourmap_Marker', 
                callback=self.contourmapMarkColor,
                params=[color.ColorParameter('color',
                                             self.settings.contourmap_markercolor,
                                             tip="Color for the contour map marker.")],
                ellipsis=1,
                help="Change the contour map marker color.",
                discussion="""<para>
                Change the color of the position marker on the contourmap pane.
                </para>"""))
        elif config.dimension() == 3:
            colormenu.addItem(OOFMenuItem(
                'Contourmap_Background', 
                callback=self.contourmapBGColor,
                params=[color.ColorParameter('color',
                                             self.settings.contourmap_bgcolor,
                                             tip="Color for the contour map background.")],
                ellipsis=1,
                help="Change the contour map background color.",
                discussion="""<para>
                Change the color of the background of the contourmap pane.
                </para>"""))
            colormenu.addItem(OOFMenuItem(
                'Contourmap_Text', 
                callback=self.contourmapTextColor,
                params=[color.ColorParameter('color',
                                             self.settings.contourmap_textcolor,
                                             tip="Color for the contour map text.")],
                ellipsis=1,
                help="Change the contour map text color.",
                discussion="""<para>
                Change the color of the text in the contourmap pane.
                </para>"""))

            settingmenu.addItem(CheckOOFMenuItem(
                'Show_Contourmap_Pane',
                callback=self.toggleContourpane,
                value=self.settings.showcontourpane,
                threadable=oofmenu.THREADABLE,
                help="Show/hide the contourmap pane.",
                discussion="""<para>Show or hide the contourmap pane.</para>"""
                ))
                

        settingmenu.addItem(OOFMenuItem(
            'Margin',
            callback=self.marginCB,
            params=[FloatParameter('fraction', self.settings.margin,
                                   tip="Margin as a fraction of the image size.")],
            ellipsis=1,
            help=
  'Set the margin (as a fraction of the image size) when zooming to full size.',
            discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/margin.xml')
            ))

        if config.dimension() == 3:
            settingmenu.addItem(OOFMenuItem(
                'Contour_Pane_Width',
                callback=self.contourpanewidthCB,
                params=[FloatParameter('fraction', self.settings.contourpanewidth,
                                       tip="Contour pane width as a fraction of the window size.")],
                ellipsis=1,
                help=
      'Set the contour pane width as a fraction of the window size.',
                # TODO 3D: will have to update the documentation
                discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/margin.xml')
                ))

        if config.dimension() == 2:
            scrollmenu = settingmenu.addItem(OOFMenuItem(
                'Scroll',
                cli_only=1,
                help='Scroll the main display.'))
            scrollmenu.addItem(OOFMenuItem(
                'Horizontal',
                callback=self.hScrollCB,
                params=[FloatParameter('position', 0.,
                                       tip="Horizontal scroll position.")],
                help="Scroll horizontally.",
                discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/scrollhoriz.xml')
                ))
            scrollmenu.addItem(OOFMenuItem(
                'Vertical',
                callback=self.vScrollCB,
                params=[FloatParameter('position', 0.,
                                       tip="Vertical scroll position.")],
                help="Scroll vertically.",
                discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/scrollvert.xml')
                ))

        # Create toolboxes.
        self.toolboxes = []
        map(self.newToolboxClass, toolbox.toolboxClasses)

        self.defaultLayerCreated = {}
        self.sensitize_menus()

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
        

    def createPredefinedLayers(self):
        # Create pre-defined layers.  These are in all graphics
        # windows, regardless of whether or not they are drawable at
        # the moment.
        for predeflayer in PredefinedLayer.allPredefinedLayers:
            self.incorporateLayerSet(predeflayer.createLayerSet(),
                                     force=1, autoselect=0)
        
##        for layerset in display.predefinedLayerSets:
##            self.incorporateLayerSet(layerset, force=1, autoselect=0)

        # Create default layers if possible.  One layer is created for
        # each WhoClass the first time that an instance of that class
        # is created.
        self.createDefaultLayers()

    def drawable(self):                 # used when testing the gui
        return self.display.drawable(self)
        
    def __repr__(self):
        return 'GhostGfxWindow("%s")' % self.name

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

    def createDefaultLayers(self):
        # Unselect all layers first, so that new layers don't
        # overwrite existing ones.
        selectedLayer = self.selectedLayer
        self.deselectAll()

        # Create a default layer for each WhoClass if this window
        # hasn't already created a default layer for that class and if
        # there's only a single member of the class.  (The single
        # member constraint is enforced in
        # DefaultLayer.createLayerSet().)
        for defaultlayer in DefaultLayer.allDefaultLayers:
            try:
                layercreated = self.defaultLayerCreated[defaultlayer]
            except KeyError:
                self.defaultLayerCreated[defaultlayer] = layercreated = 0
            if not layercreated:
                layerset = defaultlayer.createLayerSet()
                if layerset is not None:
                    self.incorporateLayerSet(layerset, autoselect=0)
                    self.defaultLayerCreated[defaultlayer] = 1

        # Restore the previous selection state.
        if selectedLayer:
            self.selectLayer(self.layerID(selectedLayer))
                
    def sensitize_menus(self):
        ## TODO?: There appears to be a problem with the timing of
        ## double clicks in the LayerList --- can one thread be inside
        ## sensitize_menus() while another thread is setting
        ## self.selectedLayer to None?  Does there need to be a lock
        ## on self.selectedLayer?
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
            if self.layerID(self.selectedLayer) == self.display.nlayers()-1:
                self.menu.Layer.Raise.disable()
            else:
                self.menu.Layer.Raise.enable()

            if self.selectedLayer.frozen:
                self.menu.Layer.Unfreeze.enable()
                self.menu.Layer.Freeze.disable()
            else:
                self.menu.Layer.Freeze.enable()
                self.menu.Layer.Unfreeze.disable()

            if config.dimension() == 2:
                self.menu.Layer.Show_Contour_Map.disable()
                self.menu.Layer.Hide_Contour_Map.disable()
                if self.selectedLayer.contour_capable(self):
                    if not self.selectedLayer.contourmaphidden:
                        self.menu.Layer.Hide_Contour_Map.enable()
                    else:
                        self.menu.Layer.Show_Contour_Map.enable()
        else:
            self.menu.Layer.Delete.disable()
            self.menu.Layer.Raise.disable()
            self.menu.Layer.Lower.disable()
            self.menu.Layer.Show.disable()
            self.menu.Layer.Hide.disable()
            self.menu.Layer.Freeze.disable()
            self.menu.Layer.Unfreeze.disable()
            self.menu.Layer.Edit.disable()
            if config.dimension() == 2:
                self.menu.Layer.Show_Contour_Map.disable()
                self.menu.Layer.Hide_Contour_Map.disable()
        if config.dimension() == 2:
            if len(self.display) == 0:
                self.menu.Settings.Zoom.disable()
            else:
                self.menu.Settings.Zoom.enable()
        if self.display.sorted:
            self.menu.Layer.Reorder_All.disable()
        else:
            self.menu.Layer.Reorder_All.enable()

    def getLayerChangeTimeStamp(self):
        return self.display.getLayerChangeTimeStamp()
        
    ##############################

    # Menu callbacks.

    # Runs on a subthread, even in GUI mode.
    def cloneWindow(self, *args):
        self.acquireGfxLock()
        try:
            clone = self.gfxmanager.openWindow(clone=1)
            clone.settings = copy.deepcopy(self.settings)
            for layerset in self.layerSets:
                clone.incorporateLayerSet(layerset)
                clone.deselectLayer(clone.selectedLayerNumber())
            if self.selectedLayer is not None:
                clone.selectLayer(self.layerID(self.selectedLayer))
            clone.draw()
            return clone
        finally:
            self.releaseGfxLock()

    def close(self, menuitem, *args):
        # Before acquiring the gfx lock, kill all subthreads, or
        # this may deadlock!
        self.device.destroy()

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

            for layerSet in self.layerSets:
                layerSet.removeAll()
            del self.layerSets

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
            # Although the window is closing, it's important to
            # release the lock so that any remaining drawing threads
            # can finish.  They won't actually try to draw anything,
            # because of the device.destroy call, above.
            self.releaseGfxLock()

    def clear(self, *args, **kwargs):
        # Remove all user specified layers from the display.
        self.acquireGfxLock()
        try:
            # The layer list is modified as layers are deleted, so we
            # have to work with a copy.
            layers = self.display[:]
            for layer in layers:
                if layer.listed:
                    self.removeLayer(layer)
        finally:
            self.releaseGfxLock()
        self.draw()

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
            self.display.clear()  
        finally:
            self.releaseGfxLock()
        self.draw()

    def setTimeCB(self, menuitem, time):
        self.setDisplayTime(time)

    def setDisplayTime(self, time):
        if time != self.displayTime:
            self.displayTime = time
            self.displayTimeChanged.increment()
            switchboard.notify((self, "time changed"))

    def toggleAntialias(self, menuitem, antialias):
        self.settings.antialias = antialias

    def toggleContourpane(self, menuitem, contourpane):
        self.settings.showcontourpane = contourpane

    def toggleListAll(self, menuitem, listall):
        self.acquireGfxLock()
        try:
            self.settings.listall = listall
            self.sensitize_menus()
            self.newLayerMembers()
        finally:
            self.releaseGfxLock()

    def toggleAutoReorder(self, menuitem, autoreorder):
        self.acquireGfxLock()
        self.settings.autoreorder = autoreorder
        self.releaseGfxLock()

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

    def contourpanewidthCB(self, menuitem, fraction):
        self.settings.contourpanewidth = fraction

    def zoomfactorCB(self, menuitem, factor):
        self.settings.zoomfactor = factor
        switchboard.notify("zoom factor changed")

    def hScrollCB(self, menuitem, position):
        self.hscrollvalue = position

    def vScrollCB(self, menuitem, position):
        self.vscrollvalue = position

    if config.dimension() == 2:
        def saveImage(self, menuitem, filename, overwrite):
            if overwrite or not os.path.exists(filename):
                pdevice = pdfoutput.PDFoutput(filename=filename)
                pdevice.set_background(self.settings.bgcolor)
                self.display.draw(self, pdevice)

    elif config.dimension() == 3:
        # TODO 3D: we should probably create a GUI-less oofcanvas3d
        # which resides in the IO directory then clean this all up so
        # that we aren't importing from the GUI directory.
        def saveImage(self, menuitem, filename):
            if overwrite or not os.path.exists(filename):
                from ooflib.common.IO.GUI import oofcanvas3d
                self.oofcanvas = oofcanvas3d.OOFCanvas3D(self.settings.antialias, offscreen=True)
                self.oofcanvas.set_bgColor(self.settings.bgcolor)
                from ooflib.common.IO.GUI import canvasoutput
                from ooflib.common.IO import outputdevice
                rawdevice = canvasoutput.CanvasOutput(self.oofcanvas)
                self.device = outputdevice.BufferedOutputDevice(rawdevice)
                self.display.draw(self, self.device)
                self.oofcanvas.reset()
                mainthread.runBlock(self.oofcanvas.saveImageThreaded, (filename,))

    def saveContourmap(self, menuitem, filename, overwrite):
        if overwrite or not os.path.exists(filename):
            pdevice = pdfoutput.PDFoutput(filename=filename)
            pdevice.set_background(self.settings.bgcolor)
            self.display.draw_contourmap(self, pdevice)



    # Called as part of the "layers changed" in response to layer
    # insertion, removal, or reordering.  Sets the current contourable
    # layer to be the topmost one, unconditionally.
    def contourmap_newlayers(self):
        self.current_contourmap_method = \
                                       self.display.set_contourmap_topmost(self)
        switchboard.notify( (self, "new contourmap layer") )
        self.sensitize_menus()

    # Alternate method -- manually set a particular layer to be the
    # current contourable layer.
    def set_contourmap_layer(self, method):
        self.current_contourmap_method.hide_contourmap()
        self.current_contourmap_method = method
        self.current_contourmap_method.show_contourmap()
    
    ###############################

    # Returns the index of the layer in the list.
    def layerID(self, layer):
        return self.display.layerID(layer)

    def getLayer(self, layerNumber):
        return self.display[layerNumber]

    def getLayerSet(self, layerNumber):
        return self.display[layerNumber].layerset
    
    def getSelectedLayerSet(self):
        if self.selectedLayer:
            return self.selectedLayer.layerset
    
    def topwho(self, *whoclasses):
        nlayers = self.display.nlayers()
        for i in range(nlayers-1, -1, -1): # top down
            who = self.display[i].who()
            classname = who.getClassName()
            if (not isinstance(who, whoville.WhoProxy)) and \
                   not self.display[i].hidden and \
                   classname in whoclasses:
                return who

    # Advanced function, returns a reference to the *layer* object
    # which draws the who object referred to.
    def topwholayer(self, *whoclasses):
        nlayers = self.display.nlayers()
        for i in range(nlayers-1, -1, -1): # top down
            who = self.display[i].who()
            classname = who.getClassName()
            if (not isinstance(who, whoville.WhoProxy)) and \
                   not self.display[i].hidden and \
                   classname in whoclasses:
                return self.display[i]

    def topmost(self, *whoclasses):
        # Find the topmost layer whose 'who' belongs to the given
        # whoclass.  Eg, topmost('Image') returns the topmost image.
        who = self.topwho(*whoclasses)
        if who is not None:
            return who.getObject(self)

    def topMethod(self, *displaymethods):
        nlayers = self.display.nlayers()
        for i in range(nlayers-1, -1, -1): # top down
            for method in displaymethods:
                if isinstance(self.display[i], method):
                    return self.display[i]

    #################################

    # Function for doing book-keeping whenever the membership of the
    # current layer set has changed.  Overridden in gfxwindow.
    def newLayerMembers(self):
        self.contourmap_newlayers()
            
    def incorporateLayerSet(self, layerset, force=0, autoselect=1):
        # Called by the LayerEditor when a new LayerSet is being sent
        # to the graphics window.  If there is a currently selected
        # layer, then its LayerSet is replaced by the new one.

        # *** See extensive comments about layers and LayerSets in
        # *** display.py
        self.acquireGfxLock()
        try:
            if len(layerset) == 0:
                return
            selectedLayerSet = self.getSelectedLayerSet()
            newLayerSet = layerset.clone()
            if force:
                newLayerSet.forced = 1
            if selectedLayerSet is None:
                # Add a new LayerSet to the existing layers.
                self.cleanLayerSet(newLayerSet, installed=0)
                if len(newLayerSet) > 0:    # cleanUp didn't remove all layers
                    for layer in newLayerSet:
                        self.newLayer(layer) # overridden in graphics mode
                        self.display.add_layer(layer)
                    if autoselect:
                        self.selectLayer(self.display.layerID(newLayerSet[0]))
            else:
                # selectedLayerSet is not None.  Replace it with the
                # new LayerSet.
                count = 0                   # loop over layers in the LayerSets
                for oldlayer,newlayer in map(None,selectedLayerSet,newLayerSet):
                    if newlayer is None or newlayer is display.emptyLayer:
                        if self.selectedLayer is oldlayer:
                            self.selectedLayer = None
                        if oldlayer is not None:
                            self.display.remove_layer(oldlayer)
                            oldlayer.destroy()
                    elif newlayer.inequivalent(oldlayer):
                        if oldlayer is not None:
                            self.display.replace_layer(oldlayer, newlayer)
                            if self.selectedLayer is oldlayer:
                                self.selectedLayer = newlayer
                            oldlayer.destroy()
                        elif newlayer is not display.emptyLayer:
                            # oldlayer is None
                            self.display.add_layer(newlayer)
                    else:                   # newlayer is equivalent to oldlayer
                        # Use the old layer, since it's been drawn already.
                        newLayerSet.replaceMethod(count, oldlayer)
                    count += 1
                self.cleanLayerSet(newLayerSet, installed=1)
                self.layerSets.remove(selectedLayerSet)
                selectedLayerSet.destroy() #doesn't affect layers, just LayerSet
            if len(newLayerSet) > 0:
                self.layerSets.append(newLayerSet)

            if self.settings.autoreorder:
                self.display.reorderLayers()
            self.sensitize_menus()
            self.newLayerMembers()
        finally:
            self.releaseGfxLock()
        switchboard.notify((self, 'layers changed'))

    def cleanLayerSet(self, layerset, installed):
        if not layerset.forced:
            layers = layerset.methods[:]
            for layer in layers:
                reason = layer.incomputable(self)
                if reason:
                    debug.fmsg('incomputable layer:', layer)
                    # Empty layers are not added to the graphics window,
                    # so we can't remove them.
                    if installed and layer != display.emptyLayer:
                        self.removeLayer(layer) # calls layerset.removeMethod()
                    else:
                        layerset.removeMethod(layer)
        
    def deleteLayerNumber(self, menuitem, n):
        layer = self.display[n]
        layerset = layer.layerset
        self.removeLayer(layer)
        if len(layerset) == 0:
            self.layerSets.remove(layerset)
        switchboard.notify((self, 'layers changed'))
        # This "draw" added so deletions are properly removed from the
        # graphics windows.
        self.draw()

    def removeLayer(self, layer):       # extended in gfxwindow.py
        self.display.remove_layer(layer)
        if layer is self.selectedLayer:
            self.selectedLayer = None
            self.sensitize_menus()
        layer.destroy()
        self.newLayerMembers()
        
    def replaceLayer(self, count, oldlayer, newlayer):
        # extended in gfxwindow.py
        if self.selectedLayer is oldlayer:
            self.selectedLayer = newlayer
        self.display.replace_layer(oldlayer, newlayer)
        layerset = oldlayer.layerset
        layerset.replaceMethod(count, newlayer)
        oldlayer.destroy()

    def newLayer(self, displaylayer):
        pass

    def hideLayer(self, menuitem, n):
        self.display[n].hide()
        self.draw()
        switchboard.notify((self, 'layers changed'))
        self.sensitize_menus()
        self.contourmap_newlayers()

    def showLayer(self, menuitem, n):
        self.display[n].show()
        self.draw()
        switchboard.notify((self, 'layers changed'))
        self.sensitize_menus()
        self.contourmap_newlayers()

    def freezeLayer(self, menuitem, n):
        self.display[n].freeze(self)
        switchboard.notify((self, 'layers frozen'))
        self.sensitize_menus()
    def unfreezeLayer(self, menuitem, n):
        self.display[n].unfreeze(self)
        switchboard.notify((self, 'layers frozen'))
        self.sensitize_menus()
        self.draw()

    # Called at layer-rearrangement time if there is exactly one
    # contour-capable layer.  The timing on this is such that all it
    # has to do is mark the appropriate layer, and the drawing will be
    # correct.
    # def auto_enable_layer_contourmap(self, layer):
    #     layer.show_contourmap()
    #     self.sensitize_menus()
        
        
    # Menu callbacks for layer operations.  Overridden in gfxwindow.
    def hideLayerContourmap(self, menuitem, n):
        self.display[n].hide_contourmap()
        self.current_contourmap_method = None
        self.sensitize_menus()
    
    def showLayerContourmap(self, menuitem, n):
        # At most one contourmap can be shown at a time, so hide all
        # the others.
        for layer in self.display:
            layer.hide_contourmap()
        self.current_contourmap_method = self.display[n]
        self.current_contourmap_method.show_contourmap()
        self.sensitize_menus()

    # Topmost layer on which contours can be drawn -- such a layer
    # must have a mesh as its "who".
    def topcontourable(self):
        return self.display.topcontourable(self)

    def selectLayer(self, n):
        if n is not None:
            self.selectedLayer = self.display[n]
            self.sensitize_menus()
    def deselectLayer(self, n):
        if self.selectedLayer is not None and \
           self.layerID(self.selectedLayer)==n:
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

    def raiseLayer(self, menuitem, n):
        self.display.raise_layer(n)
        switchboard.notify((self, 'layers changed'))
        self.sensitize_menus()
        self.draw()
        self.newLayerMembers()
        
    def raiseToTop(self, menuitem, n):
        self.display.layer_to_top(n)
        switchboard.notify((self, 'layers changed'))
        self.sensitize_menus()
        self.draw()
        self.newLayerMembers()

    def raiseBy(self, menuitem, n, howfar):
        self.display.raise_layer_by(n, howfar)
        switchboard.notify((self, 'layers changed'))
        self.sensitize_menus()
        self.draw()
        self.newLayerMembers()

    def lowerLayer(self, menuitem, n):
        self.display.lower_layer(n)
        switchboard.notify((self, 'layers changed'))
        self.sensitize_menus()
        self.draw()
        self.newLayerMembers()
        
    def lowerToBottom(self, menuitem, n):
        self.display.layer_to_bottom(n)
        switchboard.notify((self, 'layers changed'))
        self.sensitize_menus()
        self.draw()
        self.newLayerMembers()

    def lowerBy(self, menuitem, n, howfar):
        self.display.lower_layer_by(n, howfar)
        switchboard.notify((self, 'layers changed'))
        self.sensitize_menus()
        self.draw()
        self.newLayerMembers()

    def reorderLayers(self, menuitem):
        self.display.reorderLayers()
        switchboard.notify((self, 'layers changed'))
        self.sensitize_menus()
        self.draw()
        self.newLayerMembers()

    def listedLayers(self):             # for testing
        result = []
        for layer in self.display:
            if layer.listed:
                result.append(layer)
        return result
                
    def findAnimationTimes(self):
        # Return a list of all possible times that can appear in an
        # animation, by asking the unfrozen AnimationLayers for their
        # times.
        times = set()
        layersetsseen = set() # only need to check one layer in each layerset
        for layer in self.display.layers:
            if (isinstance(layer, display.AnimationLayer) 
                and layer.animatable(self)
                and layer.layerset not in layersetsseen):
                layersetsseen.add(layer.layerset)
                when = layer.getParamValue('when')
                if when is placeholder.latest:
                    times.update(layer.animationTimes(self))
        times = list(times)
        times.sort()
        return times


    def latestTime(self):
        times = self.findAnimationTimes()
        if times:
            return max(times)
        return None

    #####################################

    # switchboard callbacks

    def newWho(self, classname, who):
        # A new Who (layer context) has been created.  Display it
        # automatically, if nothing else is displayed.
        self.createDefaultLayers()
        ## Don't call self.draw() here!  It should only be called when
        ## a menu item issues the "redraw" switchboard signal.
        ## Otherwise it can be called too often (such as when one menu
        ## item creates more than one new Who object).
        
    def removeWho(self, whoclassname, whoname):
        path = labeltree.makePath(whoname)
        # In each layer containing the removed Who, replace the Who with Nobody.
        for layerset in self.layerSets:
            layerpath = labeltree.makePath(layerset.who.path())
            if layerpath == path and \
                   layerset.who.getClass().name()==whoclassname:
                layerset.changeWho(who=whoville.nobody)
        # self.draw()                     # update graphics display

        switchboard.notify((self, 'layers changed'))
        
        # There is a race condition between the newLayerMembers
        # and the redraw, which results (in the unbuffered case) in
        # the color map not being removed properly if the draw
        # precedes the newLayerMembers.
        self.newLayerMembers()
        self.draw()
        
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
# in a new grraphics window if and only if there is exactly one
# instance of the WhoClass which they display.

class DefaultLayer:
    allDefaultLayers = []
    def __init__(self, whoclass, displaymethodfn):
        DefaultLayer.allDefaultLayers.append(self)
        self.whoclass = whoclass
        self.displaymethodfn = displaymethodfn

    def createLayerSet(self):
        if self.whoclass.nActual() == 1:
            layerset = display.LayerSet(self.whoclass.actualMembers()[0])
            layerset.addMethod(self.displaymethodfn())
            return layerset

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
    def createLayerSet(self):
        layerset = display.LayerSet(self.whoclass[self.path])
        displaymethod = self.displaymethodfn()
        displaymethod.listed = 0
        layerset.addMethod(displaymethod)
        return layerset

################################################

## Set default values for the gfx window size.  This isn't handled by
## GfxSettings, because the window size isn't set in the window's own
## settings menu.

def _setDefaultGfxSize(menuitem, width, height):
    GhostGfxWindow.initial_width = width
    GhostGfxWindow.initial_height = height

mainmenu.gfxdefaultsmenu.addItem(oofmenu.OOFMenuItem(
    'Window',
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
