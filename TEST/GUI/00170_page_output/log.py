checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.5 $
# $Author: langer $
# $Date: 2010/12/01 20:43:46 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests

setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Scheduled Output')
checkpoint page installed Scheduled Output
findWidget('OOF2').resize(662, 350)
findWidget('OOF2:Scheduled Output Page:HPane0').set_position(305)
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2').set_position(135)
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL').set_position(14)
assert tests.sensitization0()
# Load Mesh file
findMenu(findWidget('OOF2:MenuBar'), 'File:Load:Data').activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(191, 71)
findWidget('Dialog-Data:filename').set_text('TEST_DATA/testmesh.mesh')
findWidget('Dialog-Data:gtk-ok').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
checkpoint microstructure page sensitized
checkpoint pixel page sensitized
checkpoint mesh bdy page updated
checkpoint meshable button set
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint Solver page sensitized
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
# checkpoint interface page updated
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.File.Load.Data
assert tests.sensitization1()
# Create graphics output
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL:Output:New').clicked()
checkpoint toplevel widget mapped Dialog-Define a new Output
findWidget('Dialog-Define a new Output').resize(314, 102)
findWidget('Dialog-Define a new Output:gtk-ok').clicked()
checkpoint OOF.Mesh.Scheduled_Output.New
findWidget('OOF2').resize(673, 350)
findWidget('OOF2:Scheduled Output Page:HPane0').set_position(316)
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL').set_position(25)
assert tests.sensitization2()
# Set schedule
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2:Schedule:New').clicked()
checkpoint toplevel widget mapped Dialog-Set an Output Schedule
findWidget('Dialog-Set an Output Schedule').resize(306, 156)
# Check contents of schedule pull-down menu
assert tests.chooserCheck('Dialog-Set an Output Schedule:schedule:Chooser', ['Periodic', 'Geometric', 'Once', 'Specified Times'])
# Change scheduletype
setComboBox(findWidget('Dialog-Set an Output Schedule:scheduletype:Chooser'), 'Conditional')
# Check contents of schedule pull down menu
assert tests.chooserCheck('Dialog-Set an Output Schedule:schedule:Chooser', ['Every Time'])
# Change back to Absolute scheduletype and click ok
setComboBox(findWidget('Dialog-Set an Output Schedule:scheduletype:Chooser'), 'Absolute')
findWidget('Dialog-Set an Output Schedule:gtk-ok').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Schedule.Set
assert tests.sensitization3()
# Add second output
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL:Output:New').clicked()
checkpoint toplevel widget mapped Dialog-Define a new Output
findWidget('Dialog-Define a new Output').resize(314, 102)
setComboBox(findWidget('Dialog-Define a new Output:output:Chooser'), 'Bulk Analysis')
findWidget('Dialog-Define a new Output').resize(472, 430)
findWidget('Dialog-Define a new Output:gtk-ok').clicked()
checkpoint OOF.Mesh.Scheduled_Output.New
assert tests.sensitization4()
# Select gfx update
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2:Destination:list').get_selection().select_path((0,))
assert tests.sensitization3()
# Copy schedule
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2:Schedule:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy an Output Schedule
findWidget('Dialog-Copy an Output Schedule').resize(441, 160)
setComboBox(findWidget('Dialog-Copy an Output Schedule:target'), 'Displacement[x]//Direct Output')
findWidget('Dialog-Copy an Output Schedule:gtk-ok').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Schedule.Copy
# Select second output
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2:Destination:list').get_selection().select_path((1,))
# Check sensitivity
assert tests.sensitization5()
# Set destination
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2:Destination:Set').clicked()
checkpoint toplevel widget mapped Dialog-Set an Output Destination
findWidget('Dialog-Set an Output Destination').resize(293, 79)
setComboBox(findWidget('Dialog-Set an Output Destination:destination:Chooser'), 'Output Stream')
findWidget('Dialog-Set an Output Destination').resize(300, 129)
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('a')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('ab')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('abc')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('abcd')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('abcde')
findWidget('Dialog-Set an Output Destination:gtk-ok').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Destination.Set
assert tests.sensitization6()
# Delete schedule
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2:Schedule:Delete').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Schedule.Delete
assert tests.sensitization7()
# Delete destination
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2:Destination:Delete').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Destination.Delete
findWidget('OOF2').resize(673, 350)
findWidget('OOF2 Messages 1').resize(720, 200)
findWidget('OOF2 Activity Viewer').resize(400, 300)
assert tests.sensitization4()
# Delete output
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL:Output:Delete').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Delete
assert tests.sensitization8()
# Delete last output
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL:Output:list').get_selection().select_path((0,))
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL:Output:Delete').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Delete
assert tests.sensitization1()
# Create two outputs
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL:Output:New').clicked()
checkpoint toplevel widget mapped Dialog-Define a new Output
findWidget('Dialog-Define a new Output').resize(472, 430)
findWidget('Dialog-Define a new Output:gtk-ok').clicked()
checkpoint OOF.Mesh.Scheduled_Output.New
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL:Output:New').clicked()
checkpoint toplevel widget mapped Dialog-Define a new Output
findWidget('Dialog-Define a new Output').resize(472, 430)
setComboBox(findWidget('Dialog-Define a new Output:output:Bulk Analysis:data:Scalar:Parameters:component'), 'y')
findWidget('Dialog-Define a new Output:gtk-ok').clicked()
checkpoint OOF.Mesh.Scheduled_Output.New
# Set destination
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2:Destination:Set').clicked()
checkpoint toplevel widget mapped Dialog-Set an Output Destination
findWidget('Dialog-Set an Output Destination').resize(300, 129)
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('g')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('gh')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('ghi')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('ghij')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('ghijk')
findWidget('Dialog-Set an Output Destination:gtk-ok').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Destination.Set
assert tests.sensitization7()
# Rewind
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2:Destination:Rewind').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Destination.Rewind
# Rewind All
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2:Destination:RewindAll').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Destination.RewindAll
# Delete All
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL:Output:DeleteAll').clicked()
checkpoint OOF.Mesh.Scheduled_Output.DeleteAll
checkpoint_count("Solver page sensitized")
assert tests.sensitization1()
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(191, 98)
findWidget('Dialog-Python_Log:filename').set_text('o')
findWidget('Dialog-Python_Log:filename').set_text('ou')
findWidget('Dialog-Python_Log:filename').set_text('out')
findWidget('Dialog-Python_Log:filename').set_text('outp')
findWidget('Dialog-Python_Log:filename').set_text('outpu')
findWidget('Dialog-Python_Log:filename').set_text('output')
findWidget('Dialog-Python_Log:filename').set_text('outputp')
findWidget('Dialog-Python_Log:filename').set_text('outputpa')
findWidget('Dialog-Python_Log:filename').set_text('outputpag')
findWidget('Dialog-Python_Log:filename').set_text('outputpage')
findWidget('Dialog-Python_Log:filename').set_text('outputpage.')
findWidget('Dialog-Python_Log:filename').set_text('outputpage.l')
findWidget('Dialog-Python_Log:filename').set_text('outputpage.lo')
findWidget('Dialog-Python_Log:filename').set_text('outputpage.log')
findWidget('Dialog-Python_Log').resize(211, 98)
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('outputpage.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
