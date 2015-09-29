# -*- python -*-
# $RCSfile: tests.py,v $
# $Revision: 1.2 $
# $Author: langer $
# $Date: 2009/09/04 14:49:43 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *

outputpane = 'OOF2:Scheduled Output Page:HPane0:HPaneL:Output'

def outputButtons(new, edit, copy, rename, delete, deleteall):
    return sensitizationCheck({'New' : new,
                               'Edit' : edit,
                               'Copy' : copy,
                               'Rename' : rename,
                               'Delete' : delete,
                               'DeleteAll' : deleteall
                               },
                              base=outputpane)

schedulepane = 'OOF2:Scheduled Output Page:HPane0:HPane2:Schedule'

def scheduleButtons(sett, copy, delete):
    return sensitizationCheck({'New' : sett,
                               'Copy' : copy,
                               'Delete' : delete
                               },
                              base=schedulepane)

destinationpane = 'OOF2:Scheduled Output Page:HPane0:HPane2:Destination'

def destinationButtons(set, delete, rewind, rewindall):
    return sensitizationCheck({'Set' : set,
                               'Delete' : delete,
                               'Rewind' : rewind,
                               'RewindAll' : rewindall
                               },
                              base=destinationpane)


def sensitization0():
    return (outputButtons(0, 0, 0, 0, 0, 0) and scheduleButtons(0, 0, 0)
            and destinationButtons(0, 0, 0, 0))

def sensitization1():
    # Mesh defined, but no outputs
    return (outputButtons(1, 0, 0, 0, 0, 0) and scheduleButtons(0, 0, 0)
            and destinationButtons(0, 0, 0, 0))

def sensitization2():
    # gfx output defined and selected, no schedule, no other outputs
    return (outputButtons(1, 1, 1, 1, 1, 1) and scheduleButtons(1, 0, 0)
            and destinationButtons(0, 0, 0, 1))

def sensitization3():
    # gfx output defined with schedule
    return (outputButtons(1, 1, 1, 1, 1, 1) and scheduleButtons(1, 1, 1)
            and destinationButtons(0, 0, 0, 1))

def sensitization4():
    # two outputs defined, selected non-gfx output w/no schedule or dest
    return (outputButtons(1, 1, 1, 1, 1, 1) and scheduleButtons(1, 0, 0)
            and destinationButtons(1, 0, 0, 1))

def sensitization5():
    # two outputs defined, selected non-gfx output w/ schedule and no dest
    return (outputButtons(1, 1, 1, 1, 1, 1) and scheduleButtons(1, 1, 1)
            and destinationButtons(1, 0, 0, 1))

def sensitization6():
    # two outputs defined, selected non-gfx output w/ schedule and dest
    return (outputButtons(1, 1, 1, 1, 1, 1) and scheduleButtons(1, 1, 1)
            and destinationButtons(1, 1, 1, 1))

def sensitization7():
    # two outputs defined, selected non-gfx w/ dest and no schedule
    return (outputButtons(1, 1, 1, 1, 1, 1) and scheduleButtons(1, 0, 0)
            and destinationButtons(1, 1, 1, 1))

def sensitization8():
    # one output defined but not selected
    return (outputButtons(1, 0, 0, 0, 0, 1) and scheduleButtons(0, 0, 0)
            and destinationButtons(0, 0, 0, 1))
