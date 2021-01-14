import tests
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 511)
event(Gdk.EventType.BUTTON_PRESS,x= 9.5000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Scheduled Output']).activate() # MenuItemLogger
checkpoint page installed Scheduled Output
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2').resize(782, 545)
assert tests.sensitization0()

# Load Mesh file
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Load', 'Data']).activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(192, 92)
findWidget('Dialog-Data:filename').set_text('TEST_DATA/testmesh.mesh')
findWidget('Dialog-Data:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
checkpoint pixel page sensitized
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint Solver page sensitized
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
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
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.File.Load.Data
assert tests.sensitization1()

# Create graphics output
findWidget('OOF2:Scheduled Output Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Define a new Output
findWidget('Dialog-Define a new Output').resize(206, 133)
findWidget('Dialog-Define a new Output:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Mesh.Scheduled_Output.New
assert tests.sensitization2()
assert tests.outputRowCheck(0, True, "GraphicsUpdate", "---", "<Graphics Window>")

# Set schedule
findWidget('OOF2:Scheduled Output Page:NewSchedule').clicked()
checkpoint toplevel widget mapped Dialog-Set an Output Schedule
findWidget('Dialog-Set an Output Schedule').resize(266, 211)
# Check contents of schedule pull-down menu
assert tests.chooserCheck('Dialog-Set an Output Schedule:schedule:RCFChooser', ['Periodic', 'Geometric', 'Once', 'Specified Times'])

event(Gdk.EventType.BUTTON_PRESS,x= 1.3800000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('Dialog-Set an Output Schedule:schedule:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findWidget('chooserPopup-RCFChooser').deactivate() # MenuLogger
# Change scheduletype
event(Gdk.EventType.BUTTON_PRESS,x= 8.0000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('Dialog-Set an Output Schedule:scheduletype:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Conditional']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
# Check contents of schedule pull down menu
assert tests.chooserCheck('Dialog-Set an Output Schedule:schedule:RCFChooser', ['Every Time'])

# Change back to Absolute scheduletype and click ok
event(Gdk.EventType.BUTTON_PRESS,x= 1.1100000000000e+02,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-Set an Output Schedule:scheduletype:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Absolute']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Set an Output Schedule:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Schedule.Set
assert tests.sensitization3()
assert tests.outputRowCheck(0, True, "GraphicsUpdate", "Absolute/Periodic(delay=0.0,interval=0.0)", "<Graphics Window>")

# Add second output
findWidget('OOF2:Scheduled Output Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Define a new Output
findWidget('Dialog-Define a new Output').resize(206, 133)
event(Gdk.EventType.BUTTON_PRESS,x= 6.6000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-Define a new Output:output:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Bulk Analysis']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Define a new Output').resize(368, 538)
findWidget('Dialog-Define a new Output:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Mesh.Scheduled_Output.New
assert tests.sensitization4()
assert tests.outputRowSelection() == 1
assert tests.outputRowCheck(0, True, "GraphicsUpdate", "Absolute/Periodic(delay=0.0,interval=0.0)", "<Graphics Window>")
assert tests.outputRowCheck(1, True, "Displacement[x]//Direct Output", "---", "---")

# Select gfx update
findWidget('OOF2:Scheduled Output Page:list').get_selection().select_path(Gtk.TreePath([0]))
assert tests.outputRowSelection() == 0
assert tests.sensitization3()

# Copy schedule
findWidget('OOF2:Scheduled Output Page:CopySchedule').clicked()
checkpoint toplevel widget mapped Dialog-Copy an Output Schedule
findWidget('Dialog-Copy an Output Schedule').resize(223, 182)
event(Gdk.EventType.BUTTON_PRESS,x= 9.4000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('Dialog-Copy an Output Schedule:target').get_window())
checkpoint toplevel widget mapped chooserPopup-target
findMenu(findWidget('chooserPopup-target'), ['Displacement[x]//Direct Output']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-target') # MenuItemLogger
findWidget('Dialog-Copy an Output Schedule').resize(299, 182)
findWidget('Dialog-Copy an Output Schedule:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Schedule.Copy
assert tests.outputRowCheck(1, True, "Displacement[x]//Direct Output", "Absolute/Periodic(delay=0.0,interval=0.0)", "---")

# Select second output
findWidget('OOF2:Scheduled Output Page:list').get_selection().select_path(Gtk.TreePath([1]))
assert tests.sensitization5()
assert tests.outputRowSelection() == 1

# Set destination
findWidget('OOF2:Scheduled Output Page:EditDestination').clicked()
checkpoint toplevel widget mapped Dialog-Set an Output Destination
findWidget('Dialog-Set an Output Destination').resize(235, 97)
event(Gdk.EventType.BUTTON_PRESS,x= 1.1500000000000e+02,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('Dialog-Set an Output Destination:destination:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Output Stream']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Set an Output Destination').resize(259, 164)
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('a')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('ab')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('abc')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('abcd')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('abcde')
findWidget('Dialog-Set an Output Destination:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Destination.Set
assert tests.sensitization6()
assert tests.outputRowSelection() == 1
assert tests.outputRowCheck(1, True, "Displacement[x]//Direct Output", "Absolute/Periodic(delay=0.0,interval=0.0)", "abcde")

# Delete last output
findWidget('OOF2:Scheduled Output Page:DeleteOutput').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Delete
assert tests.sensitization8()
assert tests.outputRowSelection() == None
assert tests.outputRowCheck(0, True, "GraphicsUpdate", "Absolute/Periodic(delay=0.0,interval=0.0)", "<Graphics Window>")
assert tests.nOutputRows() == 1

# Create two outputs
findWidget('OOF2:Scheduled Output Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Define a new Output
findWidget('Dialog-Define a new Output').resize(368, 538)
findWidget('Dialog-Define a new Output:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Mesh.Scheduled_Output.New
assert tests.outputRowCheck(1, True, "Displacement[x]//Direct Output", "---", "---")
findWidget('OOF2:Scheduled Output Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Define a new Output
findWidget('Dialog-Define a new Output').resize(368, 538)
event(Gdk.EventType.BUTTON_PRESS,x= 3.6000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('Dialog-Define a new Output:output:Bulk Analysis:data:Scalar:Parameters:component').get_window())
checkpoint toplevel widget mapped chooserPopup-component
findMenu(findWidget('chooserPopup-component'), ['y']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-component') # MenuItemLogger
findWidget('Dialog-Define a new Output:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Mesh.Scheduled_Output.New
findWidget('OOF2').resize(782, 545)
assert tests.outputRowCheck(2, True, "Displacement[y]//Direct Output", "---", "---")
assert tests.outputRowSelection() == 2
assert tests.nOutputRows() == 3

# Set destination
findWidget('OOF2:Scheduled Output Page:EditDestination').clicked()
checkpoint toplevel widget mapped Dialog-Set an Output Destination
findWidget('Dialog-Set an Output Destination').resize(259, 164)
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('g')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('gh')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('ghi')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('ghij')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('ghijk')
findWidget('Dialog-Set an Output Destination:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Destination.Set
assert tests.sensitization7()
assert tests.outputRowCheck(2, True, "Displacement[y]//Direct Output", "---", "ghijk")

# Rewind
findWidget('OOF2:Scheduled Output Page:Rewind').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Destination.Rewind

# Rewind All
findWidget('OOF2:Scheduled Output Page:RewindAll').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Destination.RewindAll

# Delete All
findWidget('OOF2:Scheduled Output Page:DeleteAll').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(233, 86)
findWidget('Questioner:Yes').clicked()
checkpoint OOF.Mesh.Scheduled_Output.DeleteAll
assert tests.sensitization1()
assert tests.nOutputRows() == 0

findMenu(findWidget('OOF2:MenuBar'), ['File', 'Save', 'Python_Log']).activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(192, 122)
findWidget('Dialog-Python_Log:filename').set_text('s')
findWidget('Dialog-Python_Log:filename').set_text('se')
findWidget('Dialog-Python_Log:filename').set_text('ses')
findWidget('Dialog-Python_Log:filename').set_text('sess')
findWidget('Dialog-Python_Log:filename').set_text('sessi')
findWidget('Dialog-Python_Log:filename').set_text('sessio')
findWidget('Dialog-Python_Log:filename').set_text('session')
findWidget('Dialog-Python_Log:filename').set_text('session.')
findWidget('Dialog-Python_Log:filename').set_text('session.l')
findWidget('Dialog-Python_Log:filename').set_text('session.lo')
findWidget('Dialog-Python_Log:filename').set_text('session.log')
findWidget('Dialog-Python_Log:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('session.log')

findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
