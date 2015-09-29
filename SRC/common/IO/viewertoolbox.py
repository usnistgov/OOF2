# -*- python -*-
# $RCSfile: viewertoolbox.py,v $
# $Revision: 1.5 $
# $Author: langer $
# $Date: 2014/09/27 21:40:33 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

from ooflib.common import toolbox

# Toolbox for viewing.
# Major functionality: zooming, panning

class ViewerToolbox(toolbox.Toolbox):
    def __init__(self, gfxwindow):
        toolbox.Toolbox.__init__(self, 'Viewer', gfxwindow)
    tip="Seeing is believing."
    discussion="""<para>
    This toolbox doesn't have any of its own menu items, so this text
    that you're reading right now shouldn't appear in the
    documentation.  If it does, please file a bug report.
    </para>"""


toolbox.registerToolboxClass(ViewerToolbox, ordering=0.0)
