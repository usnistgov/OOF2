# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common import registeredclass
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import whoville
from ooflib.image import imagecontext
from ooflib.image.IO import imagemenu

import numpy
import skimage.color

class SegmentationMethod(registeredclass.RegisteredClass):
    registry = []

    def segment(self, image):
        debug.fmsg("SegmentationMethod.segment is not defined in",
                   self.__class__)

    def labelsToGroups(self, labels, n_regions=None):
        # labels is a numpy array of integer labels.
        groups = []
        if n_regions is None:
            n_regions = labels.max()
        for k in range(n_regions):
            indices0, indices1 = (labels == k).nonzero()
            # numpy is interpreting the indices as (row, column), but
            # we want (x,y) and have to flip them.
            groups.append([primitives.iPoint(j,i) 
                           for i,j in zip(indices0, indices1)])
        return groups

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class Threshold(SegmentationMethod):
    def __init__(self, thresholds):
        self.thresholds = thresholds # list or tuple of doubles in [0, 1]
    def segment(self, image):
        n_regions = len(self.thresholds) + 1
        npimage = image.numpy()
        image = skimage.color.rgb2gray(npimage)
        n0,n1 = image.shape
        labels = (n_regions-1) * numpy.ones( (n0,n1), dtype=int )
        for k in range(n_regions-2,-1,-1):
            labels[ image <= self.thresholds[k] ] = k
        return self.labelsToGroups(labels, n_regions)

registeredclass.Registration(
    "Threshold",
    SegmentationMethod,
    Threshold,
    ordering=1,
    params = [
        parameter.ListOfFloatsParameter(
            "thresholds", value=[0.25, 0.5, 0.75],
            tip="A list of thresholds between 0 and 1.")
    ]
)


#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# menuitem callback for all segmentation methods derived from
# SegmentationMethod.

def segment(menuitem, image, method, name_template):
    immidge = imagecontext.imageContexts[image]
    mscontext = immidge.getParent()
    ms = mscontext.getObject()
    immidge.begin_reading()
    try:
        # method.segment returns a list of list of iPoints
        pixels = method.segment(immidge.getObject())
    finally:
        immidge.end_reading()
    ngroups = len(pixels)
    maxdigits = len(str(ngroups-1))
    # format for groupname
    nfmt = "%0" + `maxdigits` + "d" # number format
    fmt = name_template.replace("%n", nfmt)
    if fmt == name_template:
        # %n wasn't in name_template
        fmt = name_template + "_" + nfmt
    mscontext.begin_writing()
    try:
        for i,pixellist in enumerate(pixels):
            groupname = fmt % i
            group, newness = ms.getGroup(groupname)
            if not newness:
                group.clear() # TODO: Make this optional?
            group.addWithoutCheck(pixellist)
    finally:
        mscontext.end_writing()
    switchboard.notify("new pixel group", group)
    switchboard.notify("changed pixel group", group, mscontext.path())


imagemenu.imagemenu.addItem(
    oofmenu.OOFMenuItem(
        'Segment',
        callback=segment,
        params = [
            whoville.WhoParameter(
                'image',
                whoville.getClass('Image'),
                tip=parameter.emptyTipString),
            parameter.RegisteredParameter(
                'method',
                SegmentationMethod,
                tip="How to segment the image"),
            parameter.StringParameter(
                'name_template', value="group%n")
            ]
    ))
