# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# The "director" oofenum class.  Used by the boundary constructor,
# but in common because it just might be useful elsewhere also.
from ooflib.common import oofenum
from ooflib.common import utils

class Director(oofenum.EnumClass('Clockwise','Counterclockwise',
                              'Left to right', 'Right to left',
                              'Top to bottom', 'Bottom to top',
                              'Non-sequenceable')): #Interface branch
    tip = "Directions for arranging objects."
    discussion = """<para>
    <classname>Director</classname> objects are used to specify the
    direction of things like &skel; <link
    linkend='Section-Concepts-Skeleton-Boundary-Edge'>edge
    boundaries</link>.
    </para>"""
    xrefs=["Section-Tasks-SkeletonBoundaries"]


utils.OOFdefine('Director', Director)

# Toplogy hints, used by the DirectorWidget.
loopables = ['Clockwise', 'Counterclockwise']
unloopables = ['Left to right', 'Right to left',
               'Top to bottom', 'Bottom to top']

# Trivial subclass allows directors to have a custom widget.
class DirectorParameter(oofenum.EnumParameter):
    def __init__(self, name, value=None, default=None, tip=None):
        oofenum.EnumParameter.__init__(self, name, Director, value, default,
                                       tip)

#Interface branch
#Widget is in boundarybuilderGUI.py.
class DirectorInterfacesParameter(oofenum.EnumParameter):
    def __init__(self, name, value=None, default=None, tip=None):
        oofenum.EnumParameter.__init__(self, name, Director, value, default,
                                       tip)
