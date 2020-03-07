# -*- python -*- 

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

dirname = 'OOFCANVAS'
clib = 'oof2common'

cfiles = ['canvas.C', 'canvascircle.C', 'canvasimage.C', 'canvasitem.C',
          'canvaslayer.C', 'canvaspolygon.C', 'canvasrectangle.C',
          'canvassegment.C', 'canvassegments.C', 'canvasshape.C',
          'canvastext.C', 'utility.C']

hfiles = ['canvas.h', 'canvascircle.h', 'canvasimage.h', 'canvasitem.h',
          'canvaslayer.h', 'canvaspolygon.h', 'canvasrectangle.h',
          'canvassegment.h', 'canvassegments.h', 'canvasshape.h',
          'canvastext.h', 'oofcanvas.h', 'utility.h']


swigfiles = ['oofcanvas.swg']

swigpyfiles = ['oofcanvas.spy']


