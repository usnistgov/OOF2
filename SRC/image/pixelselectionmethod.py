# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.


from ooflib.SWIG.image import autograin
from ooflib.SWIG.image import pixelselectioncourieri
from ooflib.common import enum
from ooflib.common import pixelselectionmethod
from ooflib.common import primitives
from ooflib.common.IO import colordiffparameter
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump

class ColorSelector(pixelselectionmethod.SelectionMethod):
    def __init__(self, range):
        self.range = range
    def select(self, immidge, pointlist, selector):
        ms = immidge.getMicrostructure()
        isize = ms.sizeInPixels()
        psize = primitives.Point(*ms.sizeOfPixels())
        pt = ms.pixelFromPoint(pointlist[0])
        pic = immidge.getObject()
        ref_color = pic[pt]
        selector(pixelselectioncourieri.ColorSelection(ms, pic, ref_color,
                                                       self.range))

pixelselectionmethod.PixelSelectionRegistration(
    'Color',
    ColorSelector,
    ordering=0.6,
    events=['up'],
    params=[
        colordiffparameter.ColorDifferenceParameter(
            'range',
            tip='Acceptable deviation from the reference color.')
    ],
    whoclasses=['Image'],
    tip="Select pixels whose color is close to that of a reference pixel.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/colorselect.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

BurnSelection = pixelselectioncourieri.BurnSelection

class Burn(pixelselectionmethod.SelectionMethod):
    def __init__(self, local_flammability, global_flammability,
                 color_space_norm,
                 next_nearest):
        self.local_flammability = local_flammability
        self.global_flammability = global_flammability
        self.color_space_norm = color_space_norm
        self.next_nearest = next_nearest
    def select(self, immidge, points, selector):
        ms = immidge.getMicrostructure()
        startpt = ms.pixelFromPoint(points[0])
        if immidge.getSelectionContext().getObject().checkpixel(startpt):
            cd = autograin.ColorDifferentiator(immidge.path(),
                                     self.local_flammability,
                                     self.global_flammability,
                                     self.color_space_norm=="L2")
            selector(BurnSelection(ms, cd.cobj, startpt, self.next_nearest))
            # b = BasicBurner(self.local_flammability, self.global_flammability,
            #                 self.color_space_norm==L2, self.next_nearest)
            # selector(BurnSelection(ms, b, immidge.getObject(), startpt))


pixelselectionmethod.PixelSelectionRegistration(
    'Burn',
    Burn,
    ordering=1.0,
    params=[
    parameter.FloatRangeParameter(
        'local_flammability',
        range=(0, 1, 0.001), value=0.1,
        tip='Maximum difference in neighboring pixel values across which a burn will extend.'),
    parameter.FloatRangeParameter(
        'global_flammability',
        range=(0, 1, 0.001), value=0.2,
        tip='Difference from initial pixel value beyond which a burn will not spread.'),
    enum.EnumParameter(
        'color_space_norm', autograin.ColorNorm, value=autograin.L1,
        tip="How to compute the difference between two colors in RGB space."),
    parameter.BooleanParameter(
        'next_nearest', value=0,
        tip="Burn next-nearest neighbors?")],
    events=['up'],
    whoclasses=['Image'],
    tip="Select a contiguous set of similar pixels, using a forest fire algorithm.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/burn.xml'))

