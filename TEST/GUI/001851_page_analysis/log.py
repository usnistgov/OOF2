# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# Test that the analysis page offers the correct options for various
# kinds of outputs, especially ones that can or can't be meaningfully
# averaged.

import tests

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 511)
findWidget('OOF2').resize(782, 545)

# Create a Microstructure
event(Gdk.EventType.BUTTON_PRESS,x= 7.2000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(210, 236)
findWidget('Dialog-Create Microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
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
checkpoint OOF.Microstructure.New

# Create a Material
event(Gdk.EventType.BUTTON_PRESS,x= 7.6000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane').set_position(289)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(196, 122)
findWidget('Dialog-New material:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.New

# Add Material to pixels
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(235, 122)
event(Gdk.EventType.BUTTON_PRESS,x= 5.5000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('Dialog-Assign material material to pixels:pixels').get_window())
checkpoint toplevel widget mapped chooserPopup-pixels
findMenu(findWidget('chooserPopup-pixels'), ['<every>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-pixels') # MenuItemLogger
findWidget('Dialog-Assign material material to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Material.Assign

# Add elasticity and mass density properties to the material
event(Gdk.EventType.BUTTON_RELEASE,x= 1.2000000000000e+01,y= 2.9000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 1.0000000000000e+01,y= 2.8000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 2.7000000000000e+01,y= 4.5000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree("PropertyTree").simulateSelect(Gtk.TreePath([1, 0, 0]))
checkpoint Materials page updated
checkpoint property selected
event(Gdk.EventType.BUTTON_RELEASE,x= 7.2000000000000e+01,y= 6.1000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 4]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 2.7000000000000e+01,y= 1.7000000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree("PropertyTree").simulateSelect(Gtk.TreePath([1, 4, 0]))
checkpoint Materials page updated
checkpoint property selected
event(Gdk.EventType.BUTTON_RELEASE,x= 8.9000000000000e+01,y= 1.8800000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
# Create a Skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 6.4000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton
findWidget('OOF2:Skeleton Page:Pane').set_position(417)
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(346, 254)
findWidget('Dialog-New skeleton:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton page sensitized
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton page info updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton page info updated
checkpoint skeleton selection page selection sensitized Element
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.New
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized

# Create a Mesh
event(Gdk.EventType.BUTTON_PRESS,x= 9.2000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(130)
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(299, 244)
findWidget('Dialog-Create a new mesh:widget_GTK_RESPONSE_OK').clicked()
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
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.New

# Define temperature and displacement fields
event(Gdk.EventType.BUTTON_PRESS,x= 6.2000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Fields & Equations']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane').set_position(470)
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Define
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Define

# Go to the Analysis page
event(Gdk.EventType.BUTTON_PRESS,x= 9.4000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Analysis']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Analysis
findWidget('OOF2:Analysis Page:bottom').set_position(320)

# Scalar/Field/Component
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

# Aggregate/Field/Value Temperature
findWidget('OOF2:Analysis Page:top:Output:AggregateMode').clicked()
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

# Aggregate/Field/Value Displacement
event(Gdk.EventType.BUTTON_PRESS,x= 8.7000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:top:Output:Aggregate:Parameters:field').get_window())
checkpoint toplevel widget mapped chooserPopup-field
findMenu(findWidget('chooserPopup-field'), ['Displacement']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-field') # MenuItemLogger
assert tests.operationOptions('Direct Output', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

# Cijkl
event(Gdk.EventType.BUTTON_PRESS,x= 1.5500000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:top:Output:Aggregate:Aggregate_0').get_window())
checkpoint toplevel widget mapped chooserPopup-Aggregate_0
findMenu(findWidget('chooserPopup-Aggregate_0'), ['Material Constants']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Aggregate_0') # MenuItemLogger
assert tests.operationOptions('Direct Output')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

# Mass density
event(Gdk.EventType.BUTTON_PRESS,x= 1.2200000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:top:Output:Aggregate:Aggregate_1').get_window())
checkpoint toplevel widget mapped chooserPopup-Aggregate_1
findWidget('chooserPopup-Aggregate_1').deactivate() # MenuLogger
event(Gdk.EventType.BUTTON_PRESS,x= 1.8300000000000e+02,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:top:Output:Aggregate:Aggregate_2').get_window())
checkpoint toplevel widget mapped chooserPopup-Aggregate_2
findMenu(findWidget('chooserPopup-Aggregate_2'), ['Mass Density']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Aggregate_2') # MenuItemLogger
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

# Mass density/ Range
event(Gdk.EventType.BUTTON_PRESS,x= 1.6200000000000e+02,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:bottom:Operation:OperationRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Range']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:bottom').set_position(261)
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

# Mass density/ Average
event(Gdk.EventType.BUTTON_PRESS,x= 1.4400000000000e+02,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:bottom:Operation:OperationRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Average']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:bottom').set_position(296)
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Element Set', 'Grid Points', 'Spaced Grid Points', 'Pixels')

# Cijkl/ Direct Output
event(Gdk.EventType.BUTTON_PRESS,x= 1.6600000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:bottom:Operation:OperationRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Direct Output']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger


event(Gdk.EventType.BUTTON_PRESS,x= 2.1000000000000e+02,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:top:Output:Aggregate:Aggregate_2').get_window())
checkpoint toplevel widget mapped chooserPopup-Aggregate_2
findMenu(findWidget('chooserPopup-Aggregate_2'), ['Elastic Modulus C']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Aggregate_2') # MenuItemLogger

findWidget('OOF2:Analysis Page:bottom').set_position(320)
assert tests.operationOptions('Direct Output')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

# Concatenate Field/Value Field/Value
event(Gdk.EventType.BUTTON_PRESS,x= 1.4800000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:top:Output:Aggregate:Aggregate_0').get_window())
checkpoint toplevel widget mapped chooserPopup-Aggregate_0
findMenu(findWidget('chooserPopup-Aggregate_0'), ['Concatenate']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Aggregate_0') # MenuItemLogger
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

# Concatenate Field/Value/Temperature Field/Value/Temperature Range
event(Gdk.EventType.BUTTON_PRESS,x= 1.6100000000000e+02,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:bottom:Operation:OperationRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Range']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:bottom').set_position(261)
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

# Concatenate Field/Value/Displacement Field/Value/Temperature  Direct Output
event(Gdk.EventType.BUTTON_PRESS,x= 8.1000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:top:Output:Aggregate:Parameters:first:first_1').get_window())
checkpoint toplevel widget mapped chooserPopup-first_1
findWidget('chooserPopup-first_1').deactivate() # MenuLogger
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 2.0151515151515e+00)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 4.0303030303030e+00)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 6.0454545454545e+00)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 8.0606060606061e+00)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 1.0075757575758e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 1.2090909090909e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 1.4106060606061e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 1.6121212121212e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 2.0151515151515e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 2.2166666666667e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 2.4181818181818e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 2.6196969696970e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 2.8212121212121e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 3.0227272727273e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 3.2242424242424e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 3.4257575757576e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 3.6272727272727e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 3.8287878787879e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 4.2318181818182e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 4.4333333333333e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 4.8363636363636e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 5.2393939393939e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 5.6424242424242e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 6.4484848484848e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 6.8515151515152e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 7.2545454545455e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 7.4560606060606e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 7.6575757575758e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 7.8590909090909e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 8.0606060606061e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 8.2621212121212e+01)
event(Gdk.EventType.BUTTON_PRESS,x= 6.1000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:top:Output:Aggregate:Parameters:first:Parameters:field').get_window())
checkpoint toplevel widget mapped chooserPopup-field
findMenu(findWidget('chooserPopup-field'), ['Displacement']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-field') # MenuItemLogger
findWidget('OOF2:Analysis Page:bottom').set_position(320)
assert tests.operationOptions('Direct Output', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

# Concatenate Field/Value/Temperature Field/Value/Temperature  Direct Output
event(Gdk.EventType.BUTTON_PRESS,x= 7.1000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:top:Output:Aggregate:Parameters:first:Parameters:field').get_window())
checkpoint toplevel widget mapped chooserPopup-field
findMenu(findWidget('chooserPopup-field'), ['Temperature']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-field') # MenuItemLogger
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

# Concatenate Field/Value/Temperature Field/Value/Temperature  Range
event(Gdk.EventType.BUTTON_PRESS,x= 1.4100000000000e+02,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:bottom:Operation:OperationRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Range']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:bottom').set_position(261)
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

# Concatenate Cijkl Field/Value/Temperature  Direct Output
findWidget('OOF2').resize(786, 552)
findWidget('OOF2:Analysis Page:bottom').set_position(263)
findWidget('OOF2:Analysis Page:top').set_position(262)
findWidget('OOF2').resize(817, 602)
findWidget('OOF2:Analysis Page:bottom').set_position(273)
findWidget('OOF2:Analysis Page:top').set_position(273)
findWidget('OOF2').resize(835, 625)
findWidget('OOF2:Analysis Page:bottom').set_position(279)
findWidget('OOF2:Analysis Page:top').set_position(279)
findWidget('OOF2').resize(835, 664)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 7.3000000000000e+01)
findWidget('OOF2').resize(835, 673)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 6.9000000000000e+01)
findWidget('OOF2').resize(831, 671)
findWidget('OOF2:Analysis Page:top').set_position(278)
findWidget('OOF2:Analysis Page:bottom').set_position(278)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 6.8653846153846e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 6.7307692307692e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 6.5961538461538e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 6.4615384615385e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 6.3269230769231e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 6.1923076923077e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 6.0576923076923e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 5.9230769230769e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 5.7884615384615e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 5.6538461538462e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 5.3846153846154e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 5.2500000000000e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 5.1153846153846e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 4.9807692307692e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 4.8461538461538e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 4.7115384615385e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 4.5769230769231e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 4.4423076923077e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 4.3076923076923e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 4.1730769230769e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 4.0384615384615e+01)
event(Gdk.EventType.BUTTON_PRESS,x= 1.1300000000000e+02,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:top:Output:Aggregate:Parameters:first:first_0').get_window())
checkpoint toplevel widget mapped chooserPopup-first_0
findMenu(findWidget('chooserPopup-first_0'), ['Material Constants']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-first_0') # MenuItemLogger
findWidget('OOF2:Analysis Page:top').set_position(301)
assert tests.operationOptions('Direct Output')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

# Concatenate MassDensity Field/Value/Temperature  Direct Output
event(Gdk.EventType.BUTTON_PRESS,x= 5.3000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:top:Output:Aggregate:Parameters:first:first_2').get_window())
checkpoint toplevel widget mapped chooserPopup-first_2
findMenu(findWidget('chooserPopup-first_2'), ['Mass Density']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-first_2') # MenuItemLogger
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

# Concatenate MassDensity Field/Value Temperature  Range
event(Gdk.EventType.BUTTON_PRESS,x= 1.4500000000000e+02,y= 7.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Analysis Page:bottom:Operation:OperationRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Range']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

# Concatenate Cijkl Field/Value Temperature  DirectOutput
event(Gdk.EventType.BUTTON_PRESS,x= 9.6000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:top:Output:Aggregate:Parameters:first:first_2').get_window())
checkpoint toplevel widget mapped chooserPopup-first_2
findMenu(findWidget('chooserPopup-first_2'), ['Elastic Modulus C']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-first_2') # MenuItemLogger
assert tests.operationOptions('Direct Output')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

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
assert tests.filediff("session.log")
checkpoint OOF.File.Save.Python_Log
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
