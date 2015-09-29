# -*- python -*-
# $RCSfile: pixelinfo.py,v $
# $Revision: 1.24 $
# $Author: langer $
# $Date: 2014/09/27 21:40:32 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.common import timestamp
from ooflib.common import toolbox
from ooflib.common import primitives
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import reporter


# Despite the name "PixelInfoToolbox", this class works for both 2D
# and 3D

class PixelInfoToolbox(toolbox.Toolbox):
    def __init__(self, gfxwindow):
        self.point = None               # location of last query
        self.timestamp = timestamp.TimeStamp()
        toolbox.Toolbox.__init__(self, "Pixel_Info", gfxwindow)
        
    def makeMenu(self, menu):
        self.menu = menu
        if config.dimension() == 2:
            positionparams=[parameter.IntParameter('x', 0, tip="The x coordinate."),
                    parameter.IntParameter('y', 0, tip="The y coordinate.")]
            helpstring="Query the pixel that is closest to the given point(x,y)."
        elif config.dimension() == 3:
            positionparams=[parameter.IntParameter('x', 0, tip="The x coordinate."),
                    parameter.IntParameter('y', 0, tip="The y coordinate."),
                    parameter.IntParameter('z', 0, tip="The z coordinate.")]
            helpstring="Query the pixel that is closest to the given point(x,y,z)." 
        menu.addItem(oofmenu.OOFMenuItem(
            'Query',
            callback=self.queryPixel,
            params=positionparams,
            help=helpstring,
            discussion="""<para>
            Display information about the pixel that is closest to the
            given point.  In GUI mode, the information appears in the
            <link linkend='Section-Graphics-PixelInfo'>Pixel
            Info</link> toolbox in the graphics window.  This command
            has no effect when the GUI is not running.
            </para>"""
            ))
        menu.addItem(oofmenu.OOFMenuItem(
            'Clear',
            callback=self.clearPixel,
            params=[],
            help="Reset the pixel info toolbox.",
            discussion="""<para>
            Clear any displayed information from previous mouse clicks.
            In GUI mode, this clears the <link
            linkend='Section-Graphics-PixelInfo'>Pixel Info</link>
            toolbox in the graphics window.  This command has no
            effect if the GUI is not running.
            </para>"""
            ))

    def queryPixel(self, menuitem, x, y, z=0): # menu callback
        self.timestamp.increment()
        if config.dimension() == 2:
            self.point = primitives.iPoint(x, y)
        elif config.dimension() == 3:
            self.point = primitives.iPoint(x, y, z)
        switchboard.notify(self)        # caught by GUI toolbox
        switchboard.notify('redraw')

    def clearPixel(self, menuitem): # Menu callback.
        self.timestamp.increment()
        self.point = None
        switchboard.notify(self)
        switchboard.notify('redraw')
        
    def currentPixel(self):
        return self.point

    def findMicrostructure(self):
        ## This used to check for Skeletons and Meshes, too, and use
        ## their getMicrostructure function.  That led to some
        ## confusing situations, when a Skeleton was displayed over an
        ## Image from a different Microstructure, for example.  So now
        ## it doesn't return anything when no Microstructure or Image
        ## is displayed.
        who = self.gfxwindow().topwho('Microstructure', 'Image')
        if who is not None:
            return who.getMicrostructure()
        return None

    def getTimeStamp(self):
        return self.timestamp

    tip="Get information about a pixel."
    discussion="""<para>
    Get information about a pixel, based on mouse input.
    </para>"""
    
toolbox.registerToolboxClass(PixelInfoToolbox, ordering=1.0)
