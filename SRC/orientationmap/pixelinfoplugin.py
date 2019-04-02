# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import latticesystem
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common.IO import pixelinfo
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.engine.IO import orientationmatrix

class MisorientationPlugIn(pixelinfo.PixelInfoPlugIn):
    def __init__(self, toolbox):
        self.referenceOrientation = None
        self.referencePoint = None
        self.symmetry = None
        pixelinfo.PixelInfoPlugIn.__init__(self, toolbox)

    def makeMenu(self, menu):
        mismenu = menu.addItem(oofmenu.OOFMenuItem('Misorientation'))
        mismenu.addItem(
            oofmenu.OOFMenuItem(
                "Set_Reference",
                callback=self.setReference,
                params=[
                    primitives.PointParameter(
                        'point',
                        tip="The location of the reference pixel."),
                    parameter.ConvertibleRegisteredParameter(
                        'orientation', orientationmatrix.Orientation,
                        tip='Calculate misorientations relative to this.'
                    )
                ],
                help="Set the reference orientation."))
        symcmd = mismenu.addItem(
            oofmenu.OOFMenuItem(
                "Set_Symmetry",
                callback=self.setSymmetry,
                params=[latticesystem.LatticeSymmetryParameter('symmetry')],
                help="Set lattice symmetry used when comparing orientations"))
        self.symmetry = symcmd.get_arg('symmetry').value

    def setReference(self, menuitem, point, orientation):
        self.referencePoint = point
        self.referenceOrientation = orientation
        switchboard.notify("set reference orientation",
                           self.toolbox.gfxwindow())

    def setSymmetry(self, menuitem, symmetry):
        self.symmetry = symmetry
        switchboard.notify("set misorientation symmetry",
                           self.toolbox.gfxwindow())

    def clear(self):
        # There is no menu command for "clear" here in this toolbox
        # plug-in, because the Clear command is in the Pixel Info
        # toolbox itself.  That command calls the GUI plug-in's clear
        # method, which calls this one.
        self.referenceOrientation = None

    def draw(self, displaymethod, device, pixel, microstructure):
        # Called by PixelInfoDisplay.draw()
        if self.referenceOrientation is not None:
            n0, n1, n2, n3 = displaymethod.getNodes(self.referencePoint,
                                                    microstructure)
            device.draw_segment(primitives.Segment(n0, n1))
            device.draw_segment(primitives.Segment(n1, n2))
            device.draw_segment(primitives.Segment(n2, n3))
            device.draw_segment(primitives.Segment(n3, n0))
            device.draw_segment(primitives.Segment(0.25*(3*n0 + n2),
                                                   0.25*(5*n0 - n2)))
            device.draw_segment(primitives.Segment(0.25*(3*n2 + n0),
                                                   0.25*(5*n2 - n0)))
            device.draw_segment(primitives.Segment(0.25*(3*n1 + n3),
                                                   0.25*(5*n1 - n3)))
            device.draw_segment(primitives.Segment(0.25*(3*n3 + n1),
                                                   0.25*(5*n3 - n1)))
