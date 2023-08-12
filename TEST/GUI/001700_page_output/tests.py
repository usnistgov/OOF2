# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *

def buttons(bdict):
    return sensitizationCheck(bdict, base='OOF2:Scheduled Output Page')


def sensitization0():
    # No Mesh
    return buttons({
        'New' : 0,
        'EditOutput' : 0,
        'CopyOutput' : 0,
        'Rename' : 0,
        'DeleteOutput' : 0,
        'DeleteAll' : 0,
        'CopySchedule' : 0,
        'NewSchedule' : 0,
        'EditDestination' : 0,
        'Rewind' : 0,
        'RewindAll' : 0})
    
def sensitization1():
    # Mesh defined, but no outputs
    return buttons({
        'New' : 1,
        'EditOutput' : 0,
        'CopyOutput' : 0,
        'Rename' : 0,
        'DeleteOutput' : 0,
        'DeleteAll' : 0,
        'CopySchedule' : 0,
        'NewSchedule' : 0,
        'EditDestination' : 0,
        'Rewind' : 0,
        'RewindAll' : 0})

def sensitization2():
    # gfx output defined and selected, no schedule, no other outputs
    return buttons({
        'New' : 1,
        'EditOutput' : 1,
        'CopyOutput' : 1,
        'Rename' : 1,
        'DeleteOutput' : 1,
        'DeleteAll' : 1,
        'CopySchedule' : 0,
        'NewSchedule' : 1,
        'EditDestination' : 0,
        'Rewind' : 0,
        'RewindAll' : 1})

def sensitization3():
    # gfx output defined with schedule
    return buttons({
        'New' : 1,
        'EditOutput' : 1,
        'CopyOutput' : 1,
        'Rename' : 1,
        'DeleteOutput' : 1,
        'DeleteAll' : 1,
        'CopySchedule' : 1,
        'NewSchedule' : 1,
        'EditDestination' : 0,
        'Rewind' : 0,
        'RewindAll' : 1})

def sensitization4():
    # two outputs defined, selected non-gfx output w/no schedule or dest
    return buttons({
        'New' : 1,
        'EditOutput' : 1,
        'CopyOutput' : 1,
        'Rename' : 1,
        'DeleteOutput' : 1,
        'DeleteAll' : 1,
        'CopySchedule' : 0,
        'NewSchedule' : 1,
        'EditDestination' : 1,
        'Rewind' : 0,
        'RewindAll' : 1})

def sensitization5():
    # two outputs defined, selected non-gfx output w/ schedule and no dest
    return buttons({
        'New' : 1,
        'EditOutput' : 1,
        'CopyOutput' : 1,
        'Rename' : 1,
        'DeleteOutput' : 1,
        'DeleteAll' : 1,
        'CopySchedule' : 1,
        'NewSchedule' : 1,
        'EditDestination' : 1,
        'Rewind' : 0,
        'RewindAll' : 1})

def sensitization6():
    # two outputs defined, selected non-gfx output w/ schedule and dest
    return buttons({
        'New' : 1,
        'EditOutput' : 1,
        'CopyOutput' : 1,
        'Rename' : 1,
        'DeleteOutput' : 1,
        'DeleteAll' : 1,
        'CopySchedule' : 1,
        'NewSchedule' : 1,
        'EditDestination' : 1,
        'Rewind' : 1,
        'RewindAll' : 1})

def sensitization7():
    # two outputs defined, selected non-gfx w/ dest and no schedule
    return buttons({
        'New' : 1,
        'EditOutput' : 1,
        'CopyOutput' : 1,
        'Rename' : 1,
        'DeleteOutput' : 1,
        'DeleteAll' : 1,
        'CopySchedule' : 0,
        'NewSchedule' : 1,
        'EditDestination' : 1,
        'Rewind' : 1,
        'RewindAll' : 1})

def sensitization8():
    # one output defined but not selected
    return buttons({
        'New' : 1,
        'EditOutput' : 0,
        'CopyOutput' : 0,
        'Rename' : 0,
        'DeleteOutput' : 0,
        'DeleteAll' : 1,
        'CopySchedule' : 0,
        'NewSchedule' : 0,
        'EditDestination' : 0,
        'Rewind' : 0,
        'RewindAll' : 1})

def nOutputRows():
    treeview = gtklogger.findWidget('OOF2:Scheduled Output Page:list')
    return len(treeview.get_model())

def outputRowSelection():
    return listViewSelectedRowNo('OOF2:Scheduled Output Page:list')

def outputRowCheck(rowNo, active, outputname, schedule, destination):
    # rowNo is the row to check.  The other arguments are what is
    # supposed to appear in the GUI.  active is a bool and the others
    # are strings.
    
    # It's not possible (or at least not easy) to get Gtk to tell us
    # what is actually displayed in a GtkTreeView, but we can get the
    # object stored in the underlying GtkListStore, which in this case
    # is an Output.  We have to ask the Output for the data that the
    # cell data functions (OutputPage.renderOutputCell, et al) use in
    # when rendering the TreeView.  This test is therefore not really
    # at the right level -- if there were bugs in the cell data
    # functions we wouldn't detect them here.
    
    vals = treeViewRowValues('OOF2:Scheduled Output Page:list', rowNo)
    output = vals[0]
    
    if active != output.active:
        return False
    if outputname != output.name():
        print("Expected output '%s', got '%s'" % \
            (outputname, output.name()), file=sys.stderr)
        return False
    if ((output.schedule is None and schedule != '---') or
        (output.schedule is not None and
         schedule != (output.scheduleType.shortrepr() + "/" +
                      output.schedule.shortrepr()))):
        print("Expected schedule '%s', got '%s'" % \
            (schedule, ('---' if output.schedule is None else
                        output.scheduleType.shortrepr() +"/" +
                        output.schedule.shortrepr())), file=sys.stderr)
        return False
    if ((output.destination is None and destination != '---') or
        (output.destination is not None and
         destination != output.destination.shortrepr())):
        
        print("Expected destination '%s', got '%s'" % \
            (destination, ('---' if output.destination is None
                           else output.destination.shortrepr())), file=sys.stderr)
        return False
    return True
