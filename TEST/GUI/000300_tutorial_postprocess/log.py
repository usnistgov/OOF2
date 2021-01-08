checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer
import tests
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 545)
findMenu(findWidget('OOF2:MenuBar'), ['Help', 'Tutorials']).activate()
findMenu(findWidget('OOF2:MenuBar'), ['Help', 'Tutorials', 'Postprocessing']).activate()
checkpoint toplevel widget mapped Postprocessing
findWidget('Postprocessing').resize(500, 300)
findWidget('Postprocessing:Next').clicked()
findWidget('OOF2').resize(782, 545)
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Load', 'Data']).activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(192, 92)
findWidget('Dialog-Data:filename').set_text('e')
findWidget('Dialog-Data:filename').set_text('ex')
findWidget('Dialog-Data:filename').set_text('exa')
findWidget('Dialog-Data:filename').set_text('exam')
findWidget('Dialog-Data:filename').set_text('examp')
findWidget('Dialog-Data:filename').set_text('exampl')
findWidget('Dialog-Data:filename').set_text('example')
findWidget('Dialog-Data:filename').set_text('examples')
findWidget('Dialog-Data:filename').set_text('examples/')
findWidget('Dialog-Data:filename').set_text('examples/c')
findWidget('Dialog-Data:filename').set_text('examples/cy')
findWidget('Dialog-Data:filename').set_text('examples/cya')
findWidget('Dialog-Data:filename').set_text('examples/cyal')
findWidget('Dialog-Data:filename').set_text('examples/cyall')
findWidget('Dialog-Data:filename').set_text('examples/cyallo')
findWidget('Dialog-Data:filename').set_text('examples/cyallow')
findWidget('Dialog-Data:filename').set_text('examples/cyallow.')
findWidget('Dialog-Data:filename').set_text('examples/cyallow.m')
findWidget('Dialog-Data:filename').set_text('examples/cyallow.me')
findWidget('Dialog-Data:filename').set_text('examples/cyallow.mes')
findWidget('Dialog-Data:filename').set_text('examples/cyallow.mesh')
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
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
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
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
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
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
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
checkpoint OOF.File.Load.Data
findWidget('Postprocessing:Next').clicked()
findWidget('Postprocessing').resize(500, 530)
event(Gdk.EventType.BUTTON_PRESS,x= 9.0000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Analysis']).activate() # MenuItemLogger
checkpoint page installed Analysis
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Analysis Page:bottom').set_position(320)
findWidget('OOF2:Analysis Page:top:Output:AggregateMode').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 1.3700000000000e+02,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Analysis Page:top:Output:Aggregate:Aggregate_0').get_window())
checkpoint toplevel widget mapped chooserPopup-Aggregate_0
findMenu(findWidget('chooserPopup-Aggregate_0'), ['Flux']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Aggregate_0') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 1.4600000000000e+02,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:bottom:Operation:OperationRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Average and Deviation']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:bottom').set_position(403)
findWidget('OOF2:Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Analyze.Average_and_Deviation
findWidget('OOF2 Messages 1').resize(649, 196)
assert tests.gtkTextviewTail('OOF2 Messages 1:Text', "0.0, 0.128205128213, 0.044862449681, 1.94794604925e-11, 1.06882558947e-09, 0.0384615384699, 0.0134587350299, 0.0, 0.0, 0.0, 0.0, -4.53952110882e-11, 4.21110743392e-10\n")
findWidget('OOF2 Messages 1').resize(649, 196)
findWidget('Postprocessing:Next').clicked()
findWidget('OOF2:Analysis Page:top:Output:ScalarMode').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 1.0600000000000e+02,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:top:Output:Scalar:Scalar_1').get_window())
checkpoint toplevel widget mapped chooserPopup-Scalar_1
findMenu(findWidget('chooserPopup-Scalar_1'), ['Derivative']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Scalar_1') # MenuItemLogger
findWidget('OOF2').resize(794, 592)
findWidget('OOF2:Analysis Page:bottom').set_position(410)
findWidget('OOF2:Analysis Page:top').set_position(416)
findWidget('OOF2').resize(807, 685)
findWidget('OOF2:Analysis Page:bottom').set_position(417)
findWidget('OOF2:Analysis Page:top').set_position(424)
findWidget('OOF2').resize(816, 737)
findWidget('OOF2:Analysis Page:bottom').set_position(421)
findWidget('OOF2:Analysis Page:top').set_position(426)
findWidget('OOF2').resize(816, 738)
event(Gdk.EventType.BUTTON_PRESS,x= 1.8000000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:bottom:Operation:OperationRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Direct Output']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:bottom').set_position(334)
findWidget('OOF2:Analysis Page:bottom:Sampling:Sampling:Grid Points:x_points').set_text('')
findWidget('OOF2:Analysis Page:bottom:Sampling:Sampling:Grid Points:x_points').set_text('5')
findWidget('OOF2:Analysis Page:bottom:Sampling:Sampling:Grid Points:y_points').set_text('')
findWidget('OOF2:Analysis Page:bottom:Sampling:Sampling:Grid Points:y_points').set_text('5')
findWidget('OOF2:Analysis Page:Destination:New').clicked()
checkpoint toplevel widget mapped Dialog-Add a data destination
findWidget('Dialog-Add a data destination').resize(192, 122)
findWidget('Dialog-Add a data destination:filename').set_text('d')
findWidget('Dialog-Add a data destination:filename').set_text('da')
findWidget('Dialog-Add a data destination:filename').set_text('dat')
findWidget('Dialog-Add a data destination:filename').set_text('data')
findWidget('Dialog-Add a data destination:filename').set_text('dataf')
findWidget('Dialog-Add a data destination:filename').set_text('datafi')
findWidget('Dialog-Add a data destination:filename').set_text('datafil')
findWidget('Dialog-Add a data destination:filename').set_text('datafile')
findWidget('Dialog-Add a data destination').resize(194, 122)
findWidget('Dialog-Add a data destination:filename').set_text('datafile.')
findWidget('Dialog-Add a data destination:filename').set_text('datafile.d')
findWidget('Dialog-Add a data destination:filename').set_text('datafile.da')
findWidget('Dialog-Add a data destination:filename').set_text('datafile.dat')
findWidget('Dialog-Add a data destination:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2:Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Analyze.Direct_Output
assert tests.filediff('datafile.dat', reference='datafile0.dat', tolerance=1.e-6)
findWidget('Postprocessing:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 4.2000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:top:Output:Scalar:Parameters:component').get_window())
checkpoint toplevel widget mapped chooserPopup-component
findMenu(findWidget('chooserPopup-component'), ['y']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-component') # MenuItemLogger
findWidget('OOF2:Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Analyze.Direct_Output
assert tests.filediff('datafile.dat', reference='datafile1.dat', tolerance=1.e-6)
findWidget('OOF2:Analysis Page:Destination:Rewind').clicked()
checkpoint OOF.Mesh.Analyze.Rewind
event(Gdk.EventType.BUTTON_PRESS,x= 1.2400000000000e+02,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:top:Output:Scalar:Scalar_2').get_window())
checkpoint toplevel widget mapped chooserPopup-Scalar_2
findMenu(findWidget('chooserPopup-Scalar_2'), ['Invariant']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Scalar_2') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 8.0000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:top:Output:Scalar:Parameters:derivative').get_window())
checkpoint toplevel widget mapped chooserPopup-derivative
findWidget('chooserPopup-derivative').deactivate() # MenuLogger
event(Gdk.EventType.BUTTON_PRESS,x= 1.3200000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:Destination:TextDestChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TextDestChooser
findWidget('chooserPopup-TextDestChooser').deactivate() # MenuLogger
findWidget('OOF2:Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Analyze.Direct_Output
assert tests.filediff('datafile.dat', reference='datafile2.dat', tolerance=1.e-6)
findWidget('Postprocessing:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 6.2000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Analysis']).activate() # MenuItemLogger
checkpoint mesh bdy page updated
checkpoint page installed Boundary Analysis
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Boundary Analysis Page:Pane').set_position(217)
findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([1]))
event(Gdk.EventType.BUTTON_PRESS,x= 1.3700000000000e+02,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Analysis Page:Pane:BdyAnalyzerRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Integrate Flux']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Boundary Analysis Page:Pane').set_position(261)
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.gtkTextviewTail('OOF2 Messages 1:Text', "0.0, 7.6923076853, -1.2726398869e-08\n")
findWidget('Postprocessing:Next').clicked()
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint toplevel widget mapped OOF2 Graphics 1
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
findWidget('OOF2 Graphics 1').resize(800, 492)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New
findWidget('Dialog-New').resize(395, 532)
event(Gdk.EventType.BUTTON_PRESS,x= 7.7000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('Dialog-New:category').get_window())
checkpoint toplevel widget mapped chooserPopup-category
findMenu(findWidget('chooserPopup-category'), ['Mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-category') # MenuItemLogger
findWidget('Dialog-New').resize(467, 532)
findWidget('Dialog-New:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
checkpoint Graphics_1 Mesh Info cleared position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New
findWidget('Postprocessing:Next').clicked()
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New
findWidget('Dialog-New').resize(467, 484)
event(Gdk.EventType.BUTTON_PRESS,x= 1.2300000000000e+02,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('Dialog-New:how:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Filled Contour']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-New').resize(483, 613)
findWidget('Dialog-New:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New
findWidget('Postprocessing:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 1.1600000000000e+02,y= 3.7000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
event(Gdk.EventType.BUTTON_PRESS,x= 1.1600000000000e+02,y= 3.7000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(2)
tree.row_activated(Gtk.TreePath([14]), column)
checkpoint toplevel widget mapped Dialog-Edit Graphics Layer
findWidget('Dialog-Edit Graphics Layer').resize(483, 613)
findWidget('Dialog-Edit Graphics Layer:how:Filled Contour:levels').set_text('')
findWidget('Dialog-Edit Graphics Layer:how:Filled Contour:levels').set_text('2')
findWidget('Dialog-Edit Graphics Layer:how:Filled Contour:levels').set_text('21')
findWidget('Dialog-Edit Graphics Layer:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Edit
findWidget('Postprocessing:Next').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(665)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(210)
findWidget('Postprocessing:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 6.5000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Mesh Info']).activate() # MenuItemLogger
checkpoint Graphics_1 Mesh Info sensitized
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
assert tests.checkTBMode("OOF2 Graphics 1", "Element")
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(225)
findWidget('Postprocessing:Next').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:Click:Node').clicked()
assert tests.checkTBMode("OOF2 Graphics 1", "Node")
findGfxWindow('Graphics_1').simulateMouse('down', 15.484598, 44.305034, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 15.484598, 44.305034, 1, False, False)
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Mesh_Info.QueryNode
assert tests.meshInfoNodeTBCheck('OOF2 Graphics 1', 16, 'FuncNode', (15, 45))
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 2.8000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.0400000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.6200000000000e+02)
findWidget('Postprocessing:Next').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.6110358705947e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.2810358705947e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 2.5103587059468e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:Click:Element').clicked()
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Mesh_Info.QueryElement
assert tests.checkTBMode("OOF2 Graphics 1", "Element")
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:ElementInfo:NodeList').get_selection().select_path(Gtk.TreePath([0]))
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 1.0000000000000e+00)
checkpoint contourmap info updated for Graphics_1
assert tests.meshInfoElementTBCheck('OOF2 Graphics 1', 9, 'Q4_4', ['FuncNode 11 at (15.0, 24.0)', 'FuncNode 12 at (30.0, 24.0)', 'FuncNode 17 at (30.0, 45.0)', 'FuncNode 16 at (15.0, 45.0)'], 'cyan-material')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:ElementInfo:NodeList').get_selection().select_path(Gtk.TreePath([1]))
checkpoint contourmap info updated for Graphics_1
tree=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:ElementInfo:NodeList')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1]), column)
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Mesh_Info.QueryNode
assert tests.meshInfoNodeTBCheck('OOF2 Graphics 1', 12, 'FuncNode', (30, 24))
findWidget('Postprocessing:Next').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 7.9715133144980e-01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 3.5797151331450e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.5179715133145e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.6200000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:NewDataViewer').clicked()
checkpoint Mesh_Data_1 position updated
checkpoint Mesh_Data_1 time updated
checkpoint Mesh_Data_1 mesh updated
checkpoint toplevel widget mapped Mesh Data 1
checkpoint Mesh_Data_1 data updated
findWidget('Mesh Data 1').resize(278, 448)
assert tests.chooserStateCheck('Mesh Data 1:ViewSource:output:Parameters:field', 'Displacement')
assert tests.meshDataViewerCheck('Mesh Data 1', 'Graphics_1', 'cyallow.png:skeleton:mesh', 30, 24, x=5, y=-1.71429)
event(Gdk.EventType.BUTTON_PRESS,x= 7.3000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('Mesh Data 1:ViewSource:output:output_0').get_window())
checkpoint toplevel widget mapped chooserPopup-output_0
findMenu(findWidget('chooserPopup-output_0'), ['Strain']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-output_0') # MenuItemLogger
findWidget('Mesh Data 1').resize(296, 459)
checkpoint Mesh_Data_1 data updated
assert tests.meshDataViewerCheck('Mesh Data 1', 'Graphics_1', 'cyallow.png:skeleton:mesh', 30, 24, xx=0.166667, yy=-0.0714286, xy=1.66908e-10, xz=0, yz=0, zz=0)
findWidget('Mesh Data 1').resize(543, 503)
event(Gdk.EventType.BUTTON_PRESS,x= 1.0000000000000e+02,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('Mesh Data 1:ViewSource:output:output_1').get_window())
checkpoint toplevel widget mapped chooserPopup-output_1
findMenu(findWidget('chooserPopup-output_1'), ['Invariant']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-output_1') # MenuItemLogger
findWidget('Mesh Data 1').resize(543, 544)
checkpoint Mesh_Data_1 data updated
assert tests.meshDataViewerCheck('Mesh Data 1', 'Graphics_1', 'cyallow.png:skeleton:mesh', 30, 24, generic=0.181328)
findWidget('Postprocessing:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 6.7000000000000e+01,y= 2.1000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Mesh Cross Section']).activate() # MenuItemLogger
checkpoint Graphics_1 Mesh Cross Section sensitized
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(268)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.2700000000000e+02)
findWidget('Postprocessing:Next').clicked()
findGfxWindow('Graphics_1').simulateMouse('down', 9.6994741, 49.774606, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.961683, 48.512397, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 17.272727, 41.149512, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 26.739294, 31.893313, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 32.419234, 27.475582, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 38.51991, 22.637115, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.727273, 18.850488, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 45.041322, 16.957175, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 46.513899, 15.694966, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 47.355372, 15.063862, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 47.355372, 14.643125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 47.56574, 14.432757, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 47.56574, 14.222389, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 47.776108, 14.012021, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 47.986476, 13.380917, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 48.617581, 12.96018, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 48.827949, 12.96018, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 48.617581, 12.96018, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 48.617581, 12.96018, 1, False, False)
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Cross_Section.New
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.2600000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 9.3000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 8.8784426877160e-01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Rename').clicked()
checkpoint toplevel widget mapped Dialog-Rename cross section cs
findWidget('Dialog-Rename cross section cs').resize(192, 92)
findWidget('Dialog-Rename cross section cs:name').set_text('')
findWidget('Dialog-Rename cross section cs:name').set_text('M')
findWidget('Dialog-Rename cross section cs:name').set_text('My')
findWidget('Dialog-Rename cross section cs:name').set_text('MyC')
findWidget('Dialog-Rename cross section cs:name').set_text('MyCr')
findWidget('Dialog-Rename cross section cs:name').set_text('MyCro')
findWidget('Dialog-Rename cross section cs:name').set_text('MyCros')
findWidget('Dialog-Rename cross section cs:name').set_text('MyCross')
findWidget('Dialog-Rename cross section cs:name').set_text('MyCrossS')
findWidget('Dialog-Rename cross section cs:name').set_text('MyCrossSe')
findWidget('Dialog-Rename cross section cs:name').set_text('MyCrossSec')
findWidget('Dialog-Rename cross section cs:name').set_text('MyCrossSect')
findWidget('Dialog-Rename cross section cs:name').set_text('MyCrossSecti')
findWidget('Dialog-Rename cross section cs:name').set_text('MyCrossSectio')
findWidget('Dialog-Rename cross section cs:name').set_text('MyCrossSection')
findWidget('Dialog-Rename cross section cs:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint OOF.Mesh.Cross_Section.Rename
assert tests.chooserStateCheck('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:csList', 'MyCrossSection')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.8878442687716e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.6887844268772e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 6.2887844268772e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.2700000000000e+02)
event(Gdk.EventType.BUTTON_PRESS,x= 9.8000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Destination:TextDestChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TextDestChooser
findWidget('chooserPopup-TextDestChooser').deactivate() # MenuLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Destination:New').clicked()
checkpoint toplevel widget mapped Dialog-Add a data destination
findWidget('Dialog-Add a data destination').resize(194, 122)
findWidget('Dialog-Add a data destination:filename').set_text('')
findWidget('Dialog-Add a data destination:filename').set_text('c')
findWidget('Dialog-Add a data destination:filename').set_text('cs')
findWidget('Dialog-Add a data destination:filename').set_text('cs.')
findWidget('Dialog-Add a data destination:filename').set_text('cs.d')
findWidget('Dialog-Add a data destination:filename').set_text('cs.da')
findWidget('Dialog-Add a data destination:filename').set_text('cs.dat')
findWidget('Dialog-Add a data destination:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Go').clicked()
checkpoint OOF.Mesh.Analyze.Direct_Output
assert tests.filediff('cs.dat', tolerance=1.e-6)
findWidget('Postprocessing:Next').clicked()
findWidget('Postprocessing:Close').clicked()
findMenu(findWidget('OOF2:MenuBar'), ['Help', 'Tutorials']).activate()
findMenu(findWidget('OOF2:MenuBar'), ['OrientationMap']).activate()
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
findWidget('Dialog-Python_Log').resize(194, 122)
findWidget('Dialog-Python_Log:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('session.log', tolerance=1.e-6)
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint OOF.Graphics_1.File.Close
