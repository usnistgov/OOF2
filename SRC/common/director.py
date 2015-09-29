# -*- python -*-
# $RCSfile: director.py,v $
# $Revision: 1.16 $
# $Author: langer $
# $Date: 2014/09/27 21:40:19 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# The "director" enum class.  Used by the boundary constructor,
# but in common because it just might be useful elsewhere also.
from ooflib.common import enum
from ooflib.common import utils

class Director(enum.EnumClass('Clockwise','Counterclockwise',
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


utils.OOFdefine('Director', Director)

# Toplogy hints, used by the DirectorWidget.
loopables = ['Clockwise', 'Counterclockwise']
unloopables = ['Left to right', 'Right to left',
               'Top to bottom', 'Bottom to top']

# Trivial subclass allows directors to have a custom widget.
class DirectorParameter(enum.EnumParameter):
    def __init__(self, name, value=None, default=None, tip=None):
        enum.EnumParameter.__init__(self, name, Director, value, default, tip)

#Interface branch
#Widget is in boundarybuilderGUI.py.
class DirectorInterfacesParameter(enum.EnumParameter):
    def __init__(self, name, value=None, default=None, tip=None):
        enum.EnumParameter.__init__(self, name, Director, value, default, tip)
