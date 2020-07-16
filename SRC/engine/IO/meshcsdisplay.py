# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common.IO.OOFCANVAS import oofcanvas
from ooflib.common import color
from ooflib.common import primitives
from ooflib.common import registeredclass
from ooflib.common.IO import automatic
from ooflib.common.IO import display
from ooflib.common.IO import ghostgfxwindow
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import placeholder
from ooflib.common.IO import xmlmenudump
from ooflib.engine.IO import meshcsparams
import types

# Layer for showing the mesh cross-sections.
class MeshCrossSectionDisplay(display.DisplayMethod):
    def __init__(self, cross_sections, color, linewidth):
        display.DisplayMethod.__init__(self)
        self.cross_sections = cross_sections
        self.color = color
        self.linewidth = linewidth
        
    # We might need to be redrawn when the mesh's cross-sections have
    # changed.
    def getTimeStamp(self, gfxwindow):
        mesh = self.who.resolve(gfxwindow)
        return max(self.timestamp, mesh.cross_sections.timestamp)


    def draw(self, gfxwindow, canvaslayer):
        mesh = self.who.resolve(gfxwindow)
        segments = []

        if self.cross_sections==placeholder.selection:
            cstoolbox = gfxwindow.getToolboxByName('Mesh_Cross_Section')
            cs = mesh.selectedCS()
            if cs:
                segments = primitives.Segment(cs.start, cs.end)
        else: # List of cs names.
            for k in self.cross_sections:
                try:
                    b = mesh.cross_sections[k]
                except KeyError:
                    pass
                else:
                    segments.append(primitives.Segment(b.start, b.end))
        if segments:
            segs = oofcanvas.CanvasSegments()
            segs.setLineWidth(self.linewidth)
            segs.setLineColor(color.canvasColor(self.color))
            segs.setLineWidthInPixels()
            for seg in segments:
                segs.addSegment(seg.startpt.x, seg.startpt.y,
                                seg.endpt.x, seg.endpt.y)
            canvaslayer.addItem(segs)
            

defaultMeshCSColor = color.gray50
defaultMeshCSLineWidth = 1

def _setMeshCSDefaults(menuitem, color, linewidth):
    global defaultMeshCSColor
    global defaultMeshCSLineWidth
    defaultMeshCSColor = color
    defaultMeshCSLineWidth = linewidth

meshcsdispparams = [
    color.TranslucentColorParameter('color', value=defaultMeshCSColor,
                                    tip="In which color?"),
    parameter.IntRangeParameter('linewidth', (0, 10), defaultMeshCSLineWidth,
                                tip="Thickness of the line.")]

mainmenu.gfxdefaultsmenu.Meshes.addItem(oofmenu.OOFMenuItem(
    "Cross_Section",
    callback=_setMeshCSDefaults,
    params=meshcsdispparams,
    ordering=3,
    help="Set default parameters for Mesh Cross Section displays.",
    discussion="""<para>

    Set default parameters for
    <link linkend="RegisteredClass-MeshCrossSectionDisplay"><classname>MeshCrossSectionDisplays</classname></link>.
    See <xref linkend="RegisteredClass-MeshCrossSectionDisplay"/> for the
    details.  This command may be put into your &oof2rc; file to set
    defaults for all &oof2; sessions.
    
    </para>"""))
                  
meshCrossSectionDisplay = registeredclass.Registration(
    'Cross Section',
    display.DisplayMethod,
    MeshCrossSectionDisplay,
    params=[meshcsparams.MeshCrossSectionSetParameter(
            'cross_sections', placeholder.selection,
            tip="Which cross-section to display?")] + meshcsdispparams,
    ordering=5.0,
    layerordering=display.SemiLinear,
    whoclasses=('Mesh',),
    tip="Determine which cross sections are displayed, and how.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/meshcsdisplay.xml',)
    )


def defaultMeshCrossSectionDisplay():
    return meshCrossSectionDisplay(color=defaultMeshCSColor,
                                   linewidth=defaultMeshCSLineWidth)

ghostgfxwindow.PredefinedLayer('Mesh', '<contourable>',
                               defaultMeshCrossSectionDisplay)
