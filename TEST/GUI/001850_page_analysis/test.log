# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# Basic tests for the analysis page

import tests

checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint active area status updated
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint microstructure page sensitized
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
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
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.File.LoadStartUp.Data
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 511)
findWidget('OOF2').resize(782, 545)
event(Gdk.EventType.BUTTON_PRESS,x= 8.0000000000000e+01,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Analysis']).activate() # MenuItemLogger
checkpoint page installed Analysis
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Analysis Page:mainpane:bottom').set_position(320)
assert tests.goSensitive(1)
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')
assert tests.samplingParams('Grid Points', ['x_points', 'y_points', 'show_x', 'show_y'])

findWidget('OOF2:Analysis Page:mainpane:bottom:Sampling:Sampling:Grid Points:x_points').set_text('')
findWidget('OOF2:Analysis Page:mainpane:bottom:Sampling:Sampling:Grid Points:x_points').set_text('3')
findWidget('OOF2:Analysis Page:mainpane:bottom:Sampling:Sampling:Grid Points:y_points').set_text('')
findWidget('OOF2:Analysis Page:mainpane:bottom:Sampling:Sampling:Grid Points:y_points').set_text('3')
findWidget('OOF2:Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Analyze.Direct_Output
assert tests.msgTextTail('10.0, 10.0, 0.0')

event(Gdk.EventType.BUTTON_PRESS,x= 1.6000000000000e+02,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:top:Domain:DomainRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Pixel Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.goSensitive(1)
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')
assert tests.samplingParams('Grid Points', ['x_points', 'y_points', 'show_x', 'show_y'])

event(Gdk.EventType.BUTTON_PRESS,x= 1.0500000000000e+02,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:top:Domain:DomainRCF:Pixel Group:pixels').get_window())
checkpoint toplevel widget mapped chooserPopup-pixels
findMenu(findWidget('chooserPopup-pixels'), ['green']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-pixels') # MenuItemLogger
assert tests.goSensitive(1)
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')
assert tests.samplingParams('Grid Points', ['x_points', 'y_points', 'show_x', 'show_y'])

findWidget('OOF2:Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Analyze.Direct_Output
assert tests.msgTextTail('0.0, 10.0, 0.0')

event(Gdk.EventType.BUTTON_PRESS,x= 1.3400000000000e+02,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:top:Domain:DomainRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Entire Mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.goSensitive(1)
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')
assert tests.samplingParams('Grid Points', ['x_points', 'y_points', 'show_x', 'show_y'])

event(Gdk.EventType.BUTTON_PRESS,x= 1.1900000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:top:Domain:DomainRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Cross Section']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:mainpane:top').set_position(297)
findWidget('OOF2:Analysis Page:mainpane:bottom').set_position(287)
assert tests.goSensitive(0)
assert tests.samplingOptions('Line Points', 'Element Segments')
assert tests.samplingParams('Line Points', ['n_points', 'show_distance', 'show_fraction', 'show_x', 'show_y'])
assert tests.csWidgetCheck0()

event(Gdk.EventType.BUTTON_PRESS,x= 4.0000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:bottom:Sampling:Sampling:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Element Segments']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:mainpane:bottom').set_position(224)
assert tests.goSensitive(0)
assert tests.samplingOptions('Line Points', 'Element Segments')
assert tests.samplingParams('Element Segments', ['n_points', 'show_segment', 'show_distance', 'show_fraction', 'show_x', 'show_y'])

event(Gdk.EventType.BUTTON_PRESS,x= 8.8000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:top:Domain:DomainRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Element Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:mainpane:bottom').set_position(320)
assert tests.goSensitive(1)
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points')
assert tests.samplingParams('Grid Points', ['x_points', 'y_points', 'show_x', 'show_y'])

findWidget('OOF2:Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Analyze.Direct_Output
assert tests.msgTextTail("OOF.Mesh.Analyze.Direct_Output(mesh='el_shape.png:skeleton:mesh', time=latest, data=getOutput('Field:Component',component='x',field=Displacement), domain=ElementGroup(elements=selection), sampling=GridSampleSet(x_points=3,y_points=3,show_x=True,show_y=True), destination=MessageWindowStream())")

event(Gdk.EventType.BUTTON_PRESS,x= 1.0900000000000e+02,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:top:Domain:DomainRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Entire Mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 1.1100000000000e+02,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:bottom:Operation:OperationRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Average']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:mainpane:bottom').set_position(278)
assert tests.goSensitive(1)
assert tests.samplingOptions('Element Set', 'Grid Points', 'Spaced Grid Points', 'Pixels')
assert tests.samplingParams('Grid Points', ['x_points', 'y_points'])

event(Gdk.EventType.BUTTON_PRESS,x= 1.4400000000000e+02,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:bottom:Operation:OperationRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Direct Output']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:mainpane:bottom').set_position(320)
assert tests.goSensitive(1)
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')
assert tests.samplingParams('Grid Points', ['x_points', 'y_points', 'show_x', 'show_y'])

event(Gdk.EventType.BUTTON_PRESS,x= 1.4900000000000e+02,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:bottom:Operation:OperationRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Standard Deviation']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:mainpane:bottom').set_position(362)
assert tests.goSensitive(1)
assert tests.samplingOptions('Element Set', 'Grid Points', 'Spaced Grid Points', 'Pixels')
assert tests.samplingParams('Grid Points', ['x_points', 'y_points'])

event(Gdk.EventType.BUTTON_PRESS,x= 8.3000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:bottom:Sampling:Sampling:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Spaced Grid Points']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:mainpane:bottom').set_position(369)
assert tests.goSensitive(1)
assert tests.samplingParams('Spaced Grid Points', ['delta_x', 'delta_y'])

event(Gdk.EventType.BUTTON_PRESS,x= 2.0000000000000e+02,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:bottom:Operation:OperationRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Direct Output']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:mainpane:bottom').set_position(324)
assert tests.goSensitive(1)
assert tests.samplingParams('Spaced Grid Points', ['delta_x', 'delta_y', 'show_x', 'show_y'])

event(Gdk.EventType.BUTTON_PRESS,x= 1.5600000000000e+02,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:bottom:Sampling:Sampling:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Grid Points']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:mainpane:bottom').set_position(320)
event(Gdk.EventType.BUTTON_PRESS,x= 1.4400000000000e+02,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:bottom:Operation:OperationRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Standard Deviation']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:mainpane:bottom').set_position(362)
assert tests.goSensitive(1)
assert tests.samplingParams('Grid Points', ['x_points', 'y_points'])

event(Gdk.EventType.BUTTON_PRESS,x= 1.2500000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:bottom:Sampling:Sampling:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Pixels']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:mainpane:bottom').set_position(489)
assert tests.goSensitive(1)
assert tests.samplingParams('Pixels', [])

findWidget('OOF2:Analysis Page:Destination:New').clicked()
checkpoint toplevel widget mapped Dialog-Add a data destination
findWidget('Dialog-Add a data destination').resize(192, 122)
findWidget('Dialog-Add a data destination:filename').set_text('m')
findWidget('Dialog-Add a data destination:filename').set_text('ms')
findWidget('Dialog-Add a data destination:filename').set_text('msg')
findWidget('Dialog-Add a data destination:filename').set_text('msg.')
findWidget('Dialog-Add a data destination:filename').set_text('msg.d')
findWidget('Dialog-Add a data destination:filename').set_text('msg.da')
findWidget('Dialog-Add a data destination:filename').set_text('msg.dat')
findWidget('Dialog-Add a data destination:filename').set_text('msg.data')
findWidget('Dialog-Add a data destination:widget_GTK_RESPONSE_OK').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 1.9900000000000e+02,y= 2.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:bottom:Operation:OperationRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Direct Output']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
from ooflib.common.IO.GUI import gtklogger
print >> sys.stderr, gtklogger.findAllWidgets('OOF2:Analysis Page:Destination')
assert tests.chooserCheck('OOF2:Analysis Page:Destination:TextDestChooser', ['<Message Window>', 'msg.data'])
findWidget('OOF2:Analysis Page:mainpane:bottom').set_position(346)
findWidget('OOF2:Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Analyze.Direct_Output
assert tests.filediff('msg.data')

findWidget('OOF2:Analysis Page:Destination:Clear').clicked()
assert tests.chooserCheck('OOF2:Analysis Page:Destination:TextDestChooser', ['<Message Window>'])

event(Gdk.EventType.BUTTON_PRESS,x= 1.9000000000000e+02,y= 1.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:bottom:Operation:OperationRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Average']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:mainpane:bottom').set_position(405)
assert tests.samplingParams('Pixels', [])

findWidget('OOF2:Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Analyze.Average
assert tests.msgTextTail('# 1. time\n# 2. average of Displacement[x]\n0.0, 0.0')

findWidget('OOF2').resize(782, 545)
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint Solver page sensitized
checkpoint page installed Solver
findWidget('OOF2:Solver Page:VPane').set_position(170)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Solver page sensitized
tree=findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList')
column = tree.get_column(3)
tree.row_activated(Gtk.TreePath([0]), column)
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(475, 490)
findWidget('Dialog-Specify Solver:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Set_Solver
findWidget('OOF2:Solver Page:end').set_text('0')
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:solve').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Solve
findWidget('OOF2:Solver Page:end').set_text('0.0')
findWidget('OOF2:Solver Page:end').set_text('')
checkpoint Solver page sensitized
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Analysis
findWidget('OOF2:Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Analyze.Average
assert tests.msgTextValue(0.0, -0.00856624900601, tolerance=1.e-9)

# Open a graphics window
findMenu(findWidget('OOF2:MenuBar'), ['Settings', 'Graphics_Defaults', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
event(Gdk.EventType.BUTTON_PRESS,x= 3.1000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Settings.Graphics_Defaults.New_Layer_Policy
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint toplevel widget mapped OOF2 Graphics 1
checkpoint OOF.Graphics_1.Layer.Select
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([10]))
findWidget('OOF2 Graphics 1').resize(800, 492)
findWidget('OOF2 Messages 1').resize(738, 394)

# Create a cross section
event(Gdk.EventType.BUTTON_PRESS,x= 3.7000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Mesh Cross Section']).activate() # MenuItemLogger
checkpoint Graphics_1 Mesh Cross Section sensitized
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(271)
findGfxWindow('Graphics_1').simulateMouse('up', 0.40785879, 0.42374155, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('down', 0.40785879, 0.38166792, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.40785879, 0.42374155, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.44993242, 0.46581518, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.49200604, 0.59203606, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.61822693, 0.80240421, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.82859508, 1.0127724, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.99688959, 1.2231405, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 1.2072577, 1.4755823, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 1.3755523, 1.728024, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 1.5859204, 1.8542449, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 1.7962885, 1.9804658, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 1.8804358, 2.0225394, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 1.9645831, 2.0646131, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 2.0066567, 2.1066867, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 2.0487303, 2.1487603, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 2.1328776, 2.190834, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 2.3011721, 2.2749812, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 2.3432457, 2.3170548, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 2.3853193, 2.3591285, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 2.3853193, 2.3591285, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 2.3853193, 2.3591285, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 2.3853193, 2.4012021, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 2.427393, 2.4012021, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 2.427393, 2.4012021, 1, False, False)
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Cross_Section.New
findWidget('OOF2 Graphics 1').resize(800, 492)
findWidget('OOF2').resize(782, 545)
# Create a second cross section
findGfxWindow('Graphics_1').simulateMouse('down', 2.0487303, 1.5597295, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 2.0487303, 1.5597295, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 2.2170248, 1.5597295, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 2.6798347, 1.5176559, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 3.3950864, 1.4755823, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 4.1524118, 1.4335086, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 4.8676634, 1.391435, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 5.4566942, 1.391435, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 6.0877987, 1.391435, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 6.845124, 1.3493614, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.3079339, 1.3493614, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.6445229, 1.391435, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.8969647, 1.4335086, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.1073329, 1.5176559, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.3597746, 1.5597295, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.6122164, 1.6018032, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.6963637, 1.6018032, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.7384373, 1.6438768, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.8225846, 1.6438768, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.8225846, 1.6438768, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.8646582, 1.6438768, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 8.8646582, 1.6438768, 1, False, False)
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Cross_Section.New
assert tests.goSensitive(1)
assert tests.samplingParams('Pixels', [])

# Set the Domain to Cross Section
event(Gdk.EventType.BUTTON_PRESS,x= 1.5600000000000e+02,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:top:Domain:DomainRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Cross Section']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:mainpane:top').set_position(297)
assert tests.goSensitive(1)
assert tests.samplingParams('Line Points', ['n_points'])
assert tests.samplingOptions('Line Points', 'Element Segments')

# Set Sampling to Element Segments
event(Gdk.EventType.BUTTON_PRESS,x= 7.5000000000000e+01,y= 7.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:bottom:Sampling:Sampling:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Element Segments']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
# Set Operation to Direct Output
event(Gdk.EventType.BUTTON_PRESS,x= 1.2300000000000e+02,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:bottom:Operation:OperationRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Direct Output']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.goSensitive(1)
assert tests.samplingOptions('Line Points', 'Element Segments')
assert tests.samplingParams('Element Segments', ['n_points', 'show_segment', 'show_distance', 'show_fraction', 'show_x', 'show_y'])

event(Gdk.EventType.BUTTON_PRESS,x= 5.2000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:bottom:Sampling:Sampling:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Line Points']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
# Create an output destination
event(Gdk.EventType.BUTTON_PRESS,x= 9.3000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:Destination:TextDestChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TextDestChooser
findWidget('chooserPopup-TextDestChooser').deactivate() # MenuLogger
findWidget('OOF2:Analysis Page:Destination:New').clicked()
checkpoint toplevel widget mapped Dialog-Add a data destination
findWidget('Dialog-Add a data destination').resize(194, 122)
findWidget('Dialog-Add a data destination:filename').set_text('.data')
findWidget('Dialog-Add a data destination:filename').set_text('c.data')
findWidget('Dialog-Add a data destination:filename').set_text('cs.data')
findWidget('Dialog-Add a data destination:widget_GTK_RESPONSE_OK').clicked()
assert tests.goSensitive(1)
assert tests.csWidgetCheck1()

findWidget('OOF2:Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Analyze.Direct_Output
# Check contents of cs.data
assert tests.filediff("cs.data")

# Remove the second cross section using the gfxwindow toolbox
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 1.2631578947368e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 3.7894736842105e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 6.3157894736842e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 1.1368421052632e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 1.6421052631579e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.1473684210526e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.9052631578947e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 3.6631578947368e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.4210526315789e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.1789473684211e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.8105263157895e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 6.4421052631579e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 6.9473684210526e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 7.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Remove').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Cross_Section.Remove
assert tests.goSensitive(1)
assert tests.csWidgetCheck2()

# Remove the first cross section
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Remove').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Cross_Section.Remove
assert tests.goSensitive(0)
assert tests.csWidgetCheck0()

# Create a Skeleton element group
event(Gdk.EventType.BUTTON_PRESS,x= 5.5000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Selection']).activate() # MenuItemLogger
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint page installed Skeleton Selection
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(474)
findWidget('OOF2:Skeleton Selection Page:Pane:Groups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new Element group
findWidget('Dialog-Create a new Element group').resize(192, 92)
findWidget('Dialog-Create a new Element group:name').delete_text(0, 11)
findWidget('Dialog-Create a new Element group:name').insert_text('g', 11)
findWidget('Dialog-Create a new Element group:name').insert_text('r', 1)
findWidget('Dialog-Create a new Element group:name').insert_text('e', 2)
findWidget('Dialog-Create a new Element group:name').insert_text('e', 3)
findWidget('Dialog-Create a new Element group:name').insert_text('n', 4)
findWidget('Dialog-Create a new Element group:name').insert_text('e', 5)
findWidget('Dialog-Create a new Element group:name').delete_text(5, 6)
findWidget('Dialog-Create a new Element group:name').delete_text(4, 5)
findWidget('Dialog-Create a new Element group:name').insert_text('n', 4)
findWidget('Dialog-Create a new Element group:name').insert_text(' ', 5)
findWidget('Dialog-Create a new Element group:name').insert_text('e', 6)
findWidget('Dialog-Create a new Element group:name').insert_text('l', 7)
findWidget('Dialog-Create a new Element group:name').insert_text('e', 8)
findWidget('Dialog-Create a new Element group:name').insert_text('m', 9)
findWidget('Dialog-Create a new Element group:name').insert_text('e', 10)
findWidget('Dialog-Create a new Element group:name').insert_text('n', 11)
findWidget('Dialog-Create a new Element group:name').insert_text('t', 12)
findWidget('Dialog-Create a new Element group:name').insert_text('s', 13)
findWidget('Dialog-Create a new Element group:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint OOF.ElementGroup.New_Group
event(Gdk.EventType.BUTTON_PRESS,x= 7.3000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select by Material']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 4.4000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Material:material').get_window())
checkpoint toplevel widget mapped chooserPopup-material
findMenu(findWidget('chooserPopup-material'), ['green-material']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-material') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Select_by_Material
findWidget('OOF2:Skeleton Selection Page:Pane:Groups:Add').clicked()
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.ElementGroup.Add_to_Group
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Clear').clicked()
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Clear
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint page installed Analysis
# Use the element group as the output domain
event(Gdk.EventType.BUTTON_PRESS,x= 6.7000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:top:Domain:DomainRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Element Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 1.0400000000000e+02,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:top:Domain:DomainRCF:Element Group:elements').get_window())
checkpoint toplevel widget mapped chooserPopup-elements
findMenu(findWidget('chooserPopup-elements'), ['green elements']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-elements') # MenuItemLogger
assert tests.goSensitive(1)
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points')
assert tests.samplingParams('Grid Points',                             ['x_points', 'y_points', 'show_x', 'show_y'])

# Set operation to average
event(Gdk.EventType.BUTTON_PRESS,x= 1.6100000000000e+02,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:mainpane:bottom:Operation:OperationRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Average']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.goSensitive(1)
assert tests.samplingOptions('Element Set', 'Grid Points', 'Spaced Grid Points')
assert tests.samplingParams('Grid Points', ['x_points', 'y_points'])

findWidget('OOF2:Analysis Page:mainpane:bottom:Sampling:Sampling:Grid Points:x_points').set_text('')
findWidget('OOF2:Analysis Page:mainpane:bottom:Sampling:Sampling:Grid Points:x_points').set_text('1')
findWidget('OOF2:Analysis Page:mainpane:bottom:Sampling:Sampling:Grid Points:x_points').set_text('10')
findWidget('OOF2:Analysis Page:mainpane:bottom:Sampling:Sampling:Grid Points:y_points').set_text('')
findWidget('OOF2:Analysis Page:mainpane:bottom:Sampling:Sampling:Grid Points:y_points').set_text('1')
findWidget('OOF2:Analysis Page:mainpane:bottom:Sampling:Sampling:Grid Points:y_points').set_text('10')
# Set destination back to Message Window
event(Gdk.EventType.BUTTON_PRESS,x= 8.5000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Analysis Page:Destination:TextDestChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TextDestChooser
findMenu(findWidget('chooserPopup-TextDestChooser'), ['<Message Window>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TextDestChooser') # MenuItemLogger
# Compute average
findWidget('OOF2:Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Analyze.Average
assert tests.filediff("cs.data")

# Create a second Skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 4.9000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
checkpoint skeleton page sensitized
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint page installed Skeleton
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(417)
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(346, 254)
findWidget('Dialog-New skeleton:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.New
# Create a second Mesh
event(Gdk.EventType.BUTTON_PRESS,x= 8.1000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(116)
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(299, 244)
findWidget('Dialog-Create a new mesh:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.New
# go back to the analysis page
event(Gdk.EventType.BUTTON_PRESS,x= 1.0200000000000e+02,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Analysis']).activate() # MenuItemLogger
checkpoint page installed Analysis
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
assert tests.goSensitive(0)
assert tests.samplingParams('Grid Points', ['x_points', 'y_points']) ## ???

# Create a new Mesh using the new skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 6.7000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 7.2000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:FE Mesh Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton<2>']).activate() # MenuItemLogger
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(299, 244)
findWidget('Dialog-Create a new mesh:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.New
event(Gdk.EventType.BUTTON_PRESS,x= 9.3000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Analysis']).activate() # MenuItemLogger
checkpoint page installed Analysis
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
assert tests.goSensitive(0)

event(Gdk.EventType.BUTTON_PRESS,x= 6.1000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
assert tests.goSensitive(1)

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
checkpoint OOF.Graphics_1.File.Close
