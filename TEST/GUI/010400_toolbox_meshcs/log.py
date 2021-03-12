# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import tests
import os
tbox = "OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section"

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 511)
# Open graphics window
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1').resize(800, 492)
findWidget('OOF2').resize(782, 545)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
wevent(findWidget('Dialog-New_Layer_Policy:policy'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Graphics_1.Settings.New_Layer_Policy
findWidget('OOF2 Graphics 1').resize(800, 492)
# Open Mesh CS toolbox
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Mesh Cross Section']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
checkpoint Graphics_1 Mesh Cross Section sensitized
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(271)
# Load a Mesh
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Load', 'Data']).activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(192, 92)
findWidget('Dialog-Data:filename').set_text('T')
findWidget('Dialog-Data:filename').set_text('TS')
findWidget('Dialog-Data:filename').set_text('T')
findWidget('Dialog-Data:filename').set_text('TE')
findWidget('Dialog-Data:filename').set_text('TES')
findWidget('Dialog-Data:filename').set_text('TEST')
findWidget('Dialog-Data:filename').set_text('TEST_')
findWidget('Dialog-Data:filename').set_text('TEST_D')
findWidget('Dialog-Data:filename').set_text('TEST_DA')
findWidget('Dialog-Data:filename').set_text('TEST_DAT')
findWidget('Dialog-Data:filename').set_text('TEST_DATA')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/m')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/me')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/mes')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/mesh')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshi')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshin')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinf')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfo')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfot')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfotb')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfotbo')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfotbox')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfotbox.')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfotbox.m')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfotbox.me')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfotbox.mes')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfotbox.mesh')
findWidget('Dialog-Data:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
checkpoint mesh bdy page updated
checkpoint pixel page sensitized
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
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint Move Node toolbox writable changed
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint contourmap info updated for Graphics_1
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
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
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
checkpoint Graphics_1 Mesh Info cleared position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint contourmap info updated for Graphics_1
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
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint toplevel widget mapped OOF2 Activity Viewer
findWidget('OOF2 Activity Viewer').resize(400, 300)
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.File.Load.Data
assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':''},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","<None>")
assert tests.chooserCheck(tbox+":csList",["<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Line Points')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Line Points:n_points','50')
assert findWidget(tbox+":Sampling:Line Points:show_distance").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_x").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_y").get_active()
assert tests.sensitizationCheck({'Rename':False,'Edit':False,'Copy':False,'Remove':False},tbox)
print findAllWidgets(tbox+":Destination")
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','<Message Window>')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert not tests.is_sensitive(tbox+":Go")

# Hide the default displaced mesh layer because it would be confusing later
wevent(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
findCellRenderer(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), col=0, rend=0).emit('toggled', Gtk.TreePath(10))
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([10]))
checkpoint OOF.Graphics_1.Layer.Select
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+01)
checkpoint Graphics_1 Mesh Info cleared position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Hide
findWidget('OOF2 Graphics 1').resize(810, 505)
findWidget('OOF2 Graphics 1:Pane0').set_position(373)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(682)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(275)
findWidget('OOF2 Graphics 1').resize(810, 507)
findWidget('OOF2 Graphics 1:Pane0').set_position(375)
findWidget('OOF2 Graphics 1').resize(814, 516)
findWidget('OOF2 Graphics 1:Pane0').set_position(384)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(686)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(277)
findWidget('OOF2 Graphics 1').resize(818, 522)
findWidget('OOF2 Graphics 1:Pane0').set_position(390)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(690)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(279)
findWidget('OOF2 Graphics 1').resize(818, 524)
findWidget('OOF2 Graphics 1:Pane0').set_position(392)
findWidget('OOF2 Graphics 1').resize(819, 526)
findWidget('OOF2 Graphics 1:Pane0').set_position(394)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(691)
findWidget('OOF2 Graphics 1').resize(821, 529)
findWidget('OOF2 Graphics 1:Pane0').set_position(397)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(693)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(280)
findWidget('OOF2 Graphics 1').resize(822, 529)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(694)
findWidget('OOF2 Graphics 1').resize(824, 530)
findWidget('OOF2 Graphics 1:Pane0').set_position(398)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(696)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(281)
findWidget('OOF2 Graphics 1').resize(825, 530)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(697)
findWidget('OOF2 Graphics 1').resize(826, 530)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(698)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(282)
assert tests.gtkMultiTextCompare({'meshname':'No Mesh Displayed!','layername':''},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","<None>")
assert tests.chooserCheck(tbox+":csList",["<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Line Points')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Line Points:n_points','50')
assert findWidget(tbox+":Sampling:Line Points:show_distance").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_x").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_y").get_active()
assert tests.sensitizationCheck({'Rename':False,'Edit':False,'Copy':False,'Remove':False},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','<Message Window>')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert not tests.is_sensitive(tbox+":Go")

# Create a contour plot of the magnitude of the displacement
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New
findWidget('Dialog-New').resize(395, 532)
wevent(findWidget('Dialog-New:category'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New:category').get_window())
checkpoint toplevel widget mapped chooserPopup-category
findMenu(findWidget('chooserPopup-category'), ['Mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-category') # MenuItemLogger
findWidget('Dialog-New').resize(467, 532)
wevent(findWidget('Dialog-New:how:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New:how:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Filled Contour']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-New').resize(483, 613)
wevent(findWidget('Dialog-New:how:Filled Contour:what:what_1'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New:how:Filled Contour:what:what_1').get_window())
checkpoint toplevel widget mapped chooserPopup-what_1
findMenu(findWidget('chooserPopup-what_1'), ['Invariant']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-what_1') # MenuItemLogger
findWidget('Dialog-New').resize(483, 624)
findWidget('Dialog-New:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.6000000000000e+01)
checkpoint Graphics_1 Mesh Info cleared position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New
assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':"Magnitude(Displacement)"},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","<None>")
assert tests.chooserCheck(tbox+":csList",["<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Line Points')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Line Points:n_points','50')
assert findWidget(tbox+":Sampling:Line Points:show_distance").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_x").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_y").get_active()
assert tests.sensitizationCheck({'Rename':False,'Edit':False,'Copy':False,'Remove':False},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','<Message Window>')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert not tests.is_sensitive(tbox+":Go")

# Create a cross section
findGfxWindow('Graphics_1').simulateMouse('down', 45.09141, 94.26872, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 44.740796, 7.6671675, 1, False, False)
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Cross_Section.New
assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':"Magnitude(Displacement)"},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","cs")
assert tests.chooserCheck(tbox+":csList",["cs","<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Line Points')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Line Points:n_points','50')
assert findWidget(tbox+":Sampling:Line Points:show_distance").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_x").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_y").get_active()
assert tests.sensitizationCheck({'Rename':True,'Edit':True,'Copy':True,'Remove':True},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','<Message Window>')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert tests.is_sensitive(tbox+":Go")

# Click Go
findWidget('OOF2 Graphics 1').resize(834, 533)
findWidget('OOF2 Graphics 1:Pane0').set_position(401)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(706)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(285)
findWidget('OOF2 Graphics 1').resize(847, 539)
findWidget('OOF2 Graphics 1:Pane0').set_position(407)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(719)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(290)
findWidget('OOF2 Graphics 1').resize(862, 554)
findWidget('OOF2 Graphics 1:Pane0').set_position(422)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(734)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(297)
findWidget('OOF2 Graphics 1').resize(872, 575)
findWidget('OOF2 Graphics 1:Pane0').set_position(443)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(744)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(301)
findWidget('OOF2 Graphics 1').resize(876, 596)
findWidget('OOF2 Graphics 1:Pane0').set_position(464)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(748)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(302)
findWidget('OOF2 Graphics 1').resize(884, 614)
findWidget('OOF2 Graphics 1:Pane0').set_position(482)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(756)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(306)
findWidget('OOF2 Graphics 1').resize(886, 628)
findWidget('OOF2 Graphics 1:Pane0').set_position(496)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(758)
findWidget('OOF2 Graphics 1').resize(887, 633)
findWidget('OOF2 Graphics 1:Pane0').set_position(501)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(759)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(307)
findWidget('OOF2 Graphics 1').resize(887, 635)
findWidget('OOF2 Graphics 1:Pane0').set_position(503)
findWidget('OOF2 Graphics 1').resize(887, 634)
findWidget('OOF2 Graphics 1:Pane0').set_position(502)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Go').clicked()
checkpoint OOF.Mesh.Analyze.Direct_Output
# Output written to message window.
assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':"Magnitude(Displacement)"},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","cs")
assert tests.chooserCheck(tbox+":csList",["cs","<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Line Points')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Line Points:n_points','50')
assert findWidget(tbox+":Sampling:Line Points:show_distance").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_x").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_y").get_active()
assert tests.sensitizationCheck({'Rename':True,'Edit':True,'Copy':True,'Remove':True},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','<Message Window>')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert tests.is_sensitive(tbox+":Go")

# Compare output in Message window to expected values
infile = file(os.path.join('010400_toolbox_meshcs','tail.txt'))
text = infile.read(-1)
infile.close()
assert tests.floatTextTail('OOF2 Messages 1:Text',text)
assert tests.gtkTextviewTail('OOF2 Messages 1:Text',text)

# Create a second cross section
findGfxWindow('Graphics_1').simulateMouse('down', 15.990483, 55.350614, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 87.165039, 55.701227, 1, False, False)
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Cross_Section.New
assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':"Magnitude(Displacement)"},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","cs<2>")
assert tests.chooserCheck(tbox+":csList",["cs","cs<2>","<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Line Points')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Line Points:n_points','50')
assert findWidget(tbox+":Sampling:Line Points:show_distance").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_x").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_y").get_active()
assert tests.sensitizationCheck({'Rename':True,'Edit':True,'Copy':True,'Remove':True},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','<Message Window>')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',["<Message Window>"])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert tests.is_sensitive(tbox+":Go")

# Create a destination
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Destination:New').clicked()
checkpoint toplevel widget mapped Dialog-Add a data destination
findWidget('Dialog-Add a data destination').resize(192, 122)
findWidget('Dialog-Add a data destination:filename').set_text('t')
findWidget('Dialog-Add a data destination:filename').set_text('te')
findWidget('Dialog-Add a data destination:filename').set_text('tes')
findWidget('Dialog-Add a data destination:filename').set_text('test')
findWidget('Dialog-Add a data destination:filename').set_text('test.')
findWidget('Dialog-Add a data destination:filename').set_text('test.o')
findWidget('Dialog-Add a data destination:filename').set_text('test.ou')
findWidget('Dialog-Add a data destination:filename').set_text('test.out')
findWidget('Dialog-Add a data destination:widget_GTK_RESPONSE_OK').clicked()
assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':"Magnitude(Displacement)"},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","cs<2>")
assert tests.chooserCheck(tbox+":csList",["cs","cs<2>","<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Line Points')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Line Points:n_points','50')
assert findWidget(tbox+":Sampling:Line Points:show_distance").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_x").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_y").get_active()
assert tests.sensitizationCheck({'Rename':True,'Edit':True,'Copy':True,'Remove':True},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','test.out')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>','test.out'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert tests.is_sensitive(tbox+":Go")

# Go
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Go').clicked()
checkpoint OOF.Mesh.Analyze.Direct_Output
assert tests.filediff('test.out')

assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':"Magnitude(Displacement)"},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","cs<2>")
assert tests.chooserCheck(tbox+":csList",["cs","cs<2>","<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Line Points')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Line Points:n_points','50')
assert findWidget(tbox+":Sampling:Line Points:show_distance").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_x").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_y").get_active()
assert tests.sensitizationCheck({'Rename':True,'Edit':True,'Copy':True,'Remove':True},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','test.out')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>','test.out'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert tests.is_sensitive(tbox+":Go")

# Copy the cross section
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy cross section cs<2>
findWidget('Dialog-Copy cross section cs<2>').resize(192, 188)
findWidget('Dialog-Copy cross section cs<2>:name').delete_text(4, 5)
findWidget('Dialog-Copy cross section cs<2>:name').delete_text(3, 4)
findWidget('Dialog-Copy cross section cs<2>:name').delete_text(2, 3)
findWidget('Dialog-Copy cross section cs<2>:name').insert_text('_', 2)
findWidget('Dialog-Copy cross section cs<2>:name').insert_text('c', 3)
findWidget('Dialog-Copy cross section cs<2>:name').insert_text('o', 4)
findWidget('Dialog-Copy cross section cs<2>:name').insert_text('p', 5)
findWidget('Dialog-Copy cross section cs<2>:name').insert_text('y', 6)
findWidget('Dialog-Copy cross section cs<2>:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint OOF.Mesh.Cross_Section.Copy
assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':"Magnitude(Displacement)"},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","cs_copy")
assert tests.chooserCheck(tbox+":csList",["cs","cs<2>","cs_copy","<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Line Points')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Line Points:n_points','50')
assert findWidget(tbox+":Sampling:Line Points:show_distance").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_x").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_y").get_active()
assert tests.sensitizationCheck({'Rename':True,'Edit':True,'Copy':True,'Remove':True},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','test.out')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>','test.out'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert tests.is_sensitive(tbox+":Go")

# Create a destination for the copy
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Destination:New').clicked()
checkpoint toplevel widget mapped Dialog-Add a data destination
findWidget('Dialog-Add a data destination').resize(194, 122)
findWidget('Dialog-Add a data destination:filename').set_text('ctest.out')
findWidget('Dialog-Add a data destination:filename').set_text('cotest.out')
findWidget('Dialog-Add a data destination:filename').set_text('coptest.out')
findWidget('Dialog-Add a data destination:filename').set_text('copytest.out')
findWidget('Dialog-Add a data destination:filename').set_text('copy_test.out')
findWidget('Dialog-Add a data destination:widget_GTK_RESPONSE_OK').clicked()
# Go
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Go').clicked()
checkpoint OOF.Mesh.Analyze.Direct_Output
assert tests.filediff('copy_test.out')
os.remove('copy_test.out')

assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':"Magnitude(Displacement)"},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","cs_copy")
assert tests.chooserCheck(tbox+":csList",["cs","cs<2>","cs_copy","<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Line Points')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Line Points:n_points','50')
assert findWidget(tbox+":Sampling:Line Points:show_distance").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_x").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_y").get_active()
assert tests.sensitizationCheck({'Rename':True,'Edit':True,'Copy':True,'Remove':True},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','copy_test.out')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>', 'test.out', 'copy_test.out'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert tests.is_sensitive(tbox+":Go")

# Switch to the first cross section and edit it.
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:csList'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:csList').get_window())
checkpoint toplevel widget mapped chooserPopup-csList
findMenu(findWidget('chooserPopup-csList'), ['cs']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-csList') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 3.0000000000000e+01)
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Cross_Section.Select
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Edit').clicked()
checkpoint toplevel widget mapped Dialog-Edit cross section cs
findWidget('Dialog-Edit cross section cs').resize(366, 170)
findWidget('Dialog-Edit cross section cs:cross_section:Straight:start:X').set_text('45.')
findWidget('Dialog-Edit cross section cs:cross_section:Straight:start:X').set_text('45.5')
findWidget('Dialog-Edit cross section cs:cross_section:Straight:end:X').set_text('468895')
findWidget('Dialog-Edit cross section cs:cross_section:Straight:end:X').set_text('4568895')
findWidget('Dialog-Edit cross section cs:cross_section:Straight:end:X').set_text('45.68895')
findWidget('Dialog-Edit cross section cs:cross_section:Straight:end:X').set_text('45.568895')
findWidget('Dialog-Edit cross section cs:cross_section:Straight:end:X').set_text('45.5')
findWidget('Dialog-Edit cross section cs:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Cross_Section.Edit
assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':"Magnitude(Displacement)"},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","cs")
assert tests.chooserCheck(tbox+":csList",["cs","cs<2>","cs_copy","<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Line Points')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Line Points:n_points','50')
assert findWidget(tbox+":Sampling:Line Points:show_distance").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_x").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_y").get_active()
assert tests.sensitizationCheck({'Rename':True,'Edit':True,'Copy':True,'Remove':True},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','copy_test.out')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>', 'test.out', 'copy_test.out'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert tests.is_sensitive(tbox+":Go")

# Create a new destination for the edited cross section
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Destination:New').clicked()
checkpoint toplevel widget mapped Dialog-Add a data destination
findWidget('Dialog-Add a data destination').resize(194, 122)
findWidget('Dialog-Add a data destination:filename').set_text('cop_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('co_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('c_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('e_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('ed_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('edi_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('edit_test.out')
findWidget('Dialog-Add a data destination:widget_GTK_RESPONSE_OK').clicked()
assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':"Magnitude(Displacement)"},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","cs")
assert tests.chooserCheck(tbox+":csList",["cs","cs<2>","cs_copy","<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Line Points')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Line Points:n_points','50')
assert findWidget(tbox+":Sampling:Line Points:show_distance").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_x").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_y").get_active()
assert tests.sensitizationCheck({'Rename':True,'Edit':True,'Copy':True,'Remove':True},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','edit_test.out')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>', 'test.out', 'copy_test.out', 'edit_test.out'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert tests.is_sensitive(tbox+":Go")

# Go
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Go').clicked()
checkpoint OOF.Mesh.Analyze.Direct_Output
assert tests.filediff('edit_test.out')
os.remove('edit_test.out')

assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':"Magnitude(Displacement)"},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","cs")
assert tests.chooserCheck(tbox+":csList",["cs","cs<2>","cs_copy","<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Line Points')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Line Points:n_points','50')
assert findWidget(tbox+":Sampling:Line Points:show_distance").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_x").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_y").get_active()
assert tests.sensitizationCheck({'Rename':True,'Edit':True,'Copy':True,'Remove':True},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','edit_test.out')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>', 'test.out', 'copy_test.out', 'edit_test.out'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert tests.is_sensitive(tbox+":Go")

# Rename the cross section
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Rename').clicked()
checkpoint toplevel widget mapped Dialog-Rename cross section cs
findWidget('Dialog-Rename cross section cs').resize(192, 92)
findWidget('Dialog-Rename cross section cs:name').set_text('rcs')
findWidget('Dialog-Rename cross section cs:name').set_text('recs')
findWidget('Dialog-Rename cross section cs:name').set_text('rencs')
findWidget('Dialog-Rename cross section cs:name').set_text('renacs')
findWidget('Dialog-Rename cross section cs:name').set_text('renamcs')
findWidget('Dialog-Rename cross section cs:name').set_text('renamecs')
findWidget('Dialog-Rename cross section cs:name').set_text('renamedcs')
findWidget('Dialog-Rename cross section cs:name').set_text('renamed_cs')
findWidget('Dialog-Rename cross section cs:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint OOF.Mesh.Cross_Section.Rename
assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':"Magnitude(Displacement)"},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","renamed_cs")
assert tests.chooserCheck(tbox+":csList",["renamed_cs","cs<2>","cs_copy","<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Line Points')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Line Points:n_points','50')
assert findWidget(tbox+":Sampling:Line Points:show_distance").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_x").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_y").get_active()
assert tests.sensitizationCheck({'Rename':True,'Edit':True,'Copy':True,'Remove':True},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','edit_test.out')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>', 'test.out', 'copy_test.out', 'edit_test.out'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert tests.is_sensitive(tbox+":Go")

# Create destination for renamed cross section
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Destination:New').clicked()
checkpoint toplevel widget mapped Dialog-Add a data destination
findWidget('Dialog-Add a data destination').resize(194, 122)
findWidget('Dialog-Add a data destination:filename').set_text('_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('r_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('re_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('ren_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('rena_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('renam_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('rename_test.out')
findWidget('Dialog-Add a data destination:widget_GTK_RESPONSE_OK').clicked()

# Go
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Go').clicked()
checkpoint OOF.Mesh.Analyze.Direct_Output
assert tests.filediff('rename_test.out')
os.remove('rename_test.out')

assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':"Magnitude(Displacement)"},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","renamed_cs")
assert tests.chooserCheck(tbox+":csList",["renamed_cs","cs<2>","cs_copy","<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Line Points')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Line Points:n_points','50')
assert findWidget(tbox+":Sampling:Line Points:show_distance").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_x").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_y").get_active()
assert tests.sensitizationCheck({'Rename':True,'Edit':True,'Copy':True,'Remove':True},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','rename_test.out')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>', 'test.out', 'copy_test.out', 'edit_test.out', 'rename_test.out'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert tests.is_sensitive(tbox+":Go")

# Create plot of second invariant of stress
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New
findWidget('Dialog-New').resize(483, 624)
wevent(findWidget('Dialog-New:how:Filled Contour:what:what_0'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New:how:Filled Contour:what:what_0').get_window())
checkpoint toplevel widget mapped chooserPopup-what_0
findMenu(findWidget('chooserPopup-what_0'), ['Flux']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-what_0') # MenuItemLogger
wevent(findWidget('Dialog-New:how:Filled Contour:what:what_1'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New:how:Filled Contour:what:what_1').get_window())
checkpoint toplevel widget mapped chooserPopup-what_1
findMenu(findWidget('chooserPopup-what_1'), ['Invariant']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-what_1') # MenuItemLogger
wevent(findWidget('Dialog-New:how:Filled Contour:what:Parameters:invariant:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New:how:Filled Contour:what:Parameters:invariant:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['SecondInvariant']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-New:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 6.8000000000000e+01)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New
assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':"SecondInvariant(Stress)"},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","renamed_cs")
assert tests.chooserCheck(tbox+":csList",["renamed_cs","cs<2>","cs_copy","<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Line Points')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Line Points:n_points','50')
assert findWidget(tbox+":Sampling:Line Points:show_distance").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_x").get_active()
assert findWidget(tbox+":Sampling:Line Points:show_y").get_active()
assert tests.sensitizationCheck({'Rename':True,'Edit':True,'Copy':True,'Remove':True},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','rename_test.out')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>', 'test.out', 'copy_test.out', 'edit_test.out', 'rename_test.out'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert tests.is_sensitive(tbox+":Go")

# Change cs sampling and show_* options
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Sampling:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Sampling:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Element Segments']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.5000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Sampling:Element Segments:show_fraction').clicked()

# Add a destination
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Destination:New').clicked()
checkpoint toplevel widget mapped Dialog-Add a data destination
findWidget('Dialog-Add a data destination').resize(194, 122)
findWidget('Dialog-Add a data destination:filename').set_text('e_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('ne_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('nee_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('newe_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('newle_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('newlae_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('newlaye_test.out')
findWidget('Dialog-Add a data destination:filename').set_text('newlayer_test.out')
findWidget('Dialog-Add a data destination:widget_GTK_RESPONSE_OK').clicked()
# Go
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Go').clicked()
checkpoint OOF.Mesh.Analyze.Direct_Output
assert tests.filediff('newlayer_test.out')
os.remove('newlayer_test.out')

assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':"SecondInvariant(Stress)"},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","renamed_cs")
assert tests.chooserCheck(tbox+":csList",["renamed_cs","cs<2>","cs_copy","<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Element Segments')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Element Segments:n_points:entry','2')
assert findWidget(tbox+":Sampling:Element Segments:show_segment").get_active()
assert findWidget(tbox+":Sampling:Element Segments:show_distance").get_active()
assert not findWidget(tbox+":Sampling:Element Segments:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Element Segments:show_x").get_active()
assert findWidget(tbox+":Sampling:Element Segments:show_y").get_active()
assert tests.sensitizationCheck({'Rename':True,'Edit':True,'Copy':True,'Remove':True},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','newlayer_test.out')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>', 'test.out', 'copy_test.out', 'edit_test.out', 'rename_test.out', 'newlayer_test.out'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert tests.is_sensitive(tbox+":Go")

# Switch to cs<2>
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:csList'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:csList').get_window())
checkpoint toplevel widget mapped chooserPopup-csList
findMenu(findWidget('chooserPopup-csList'), ['cs<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-csList') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.9000000000000e+01)
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Cross_Section.Select
assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':"SecondInvariant(Stress)"},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","cs<2>")
assert tests.chooserCheck(tbox+":csList",["renamed_cs","cs<2>","cs_copy","<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Element Segments')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Element Segments:n_points:entry','2')
assert findWidget(tbox+":Sampling:Element Segments:show_distance").get_active()
assert not findWidget(tbox+":Sampling:Element Segments:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Element Segments:show_x").get_active()
assert findWidget(tbox+":Sampling:Element Segments:show_y").get_active()
assert tests.sensitizationCheck({'Rename':True,'Edit':True,'Copy':True,'Remove':True},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','newlayer_test.out')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>', 'test.out', 'copy_test.out', 'edit_test.out', 'rename_test.out', 'newlayer_test.out'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert tests.is_sensitive(tbox+":Go")

# Remove cs<2>
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:Remove').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Cross_Section.Remove
assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':"SecondInvariant(Stress)"},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","cs_copy")
assert tests.chooserCheck(tbox+":csList",["renamed_cs","cs_copy","<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Element Segments')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Element Segments:n_points:entry','2')
assert findWidget(tbox+":Sampling:Element Segments:show_distance").get_active()
assert not findWidget(tbox+":Sampling:Element Segments:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Element Segments:show_x").get_active()
assert findWidget(tbox+":Sampling:Element Segments:show_y").get_active()
assert tests.sensitizationCheck({'Rename':True,'Edit':True,'Copy':True,'Remove':True},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','newlayer_test.out')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>', 'test.out', 'copy_test.out', 'edit_test.out', 'rename_test.out', 'newlayer_test.out'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert tests.is_sensitive(tbox+":Go")

# Switch to renamed_cs
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:csList'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Cross Section:csList').get_window())
checkpoint toplevel widget mapped chooserPopup-csList
findMenu(findWidget('chooserPopup-csList'), ['renamed_cs']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-csList') # MenuItemLogger
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Cross_Section.Select
assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':"SecondInvariant(Stress)"},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","renamed_cs")
assert tests.chooserCheck(tbox+":csList",["renamed_cs","cs_copy","<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Element Segments')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Element Segments:n_points:entry','2')
assert findWidget(tbox+":Sampling:Element Segments:show_distance").get_active()
assert not findWidget(tbox+":Sampling:Element Segments:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Element Segments:show_x").get_active()
assert findWidget(tbox+":Sampling:Element Segments:show_y").get_active()
assert tests.sensitizationCheck({'Rename':True,'Edit':True,'Copy':True,'Remove':True},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','newlayer_test.out')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>', 'test.out', 'copy_test.out', 'edit_test.out', 'rename_test.out', 'newlayer_test.out'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert tests.is_sensitive(tbox+":Go")

# Delete the Stress layer
findWidget('OOF2 Graphics 1').resize(887, 634)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'Delete']).activate()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.8000000000000e+01)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Delete
assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','layername':"Magnitude(Displacement)"},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","renamed_cs")
assert tests.chooserCheck(tbox+":csList",["renamed_cs","cs_copy","<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Element Segments')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Element Segments:n_points:entry','2')
assert findWidget(tbox+":Sampling:Element Segments:show_distance").get_active()
assert not findWidget(tbox+":Sampling:Element Segments:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Element Segments:show_x").get_active()
assert findWidget(tbox+":Sampling:Element Segments:show_y").get_active()
assert tests.sensitizationCheck({'Rename':True,'Edit':True,'Copy':True,'Remove':True},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','newlayer_test.out')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>', 'test.out', 'copy_test.out', 'edit_test.out', 'rename_test.out', 'newlayer_test.out'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert tests.is_sensitive(tbox+":Go")

# Delete the other mesh layer
wevent(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([15]))
checkpoint OOF.Graphics_1.Layer.Select
wevent(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), Gdk.EventType.BUTTON_PRESS, button=3, state=0, window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
checkpoint toplevel widget mapped PopUp-0
findMenu(findWidget('PopUp-0'), ['Delete']).activate() # MenuItemLogger
deactivatePopup('PopUp-0') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Mesh Cross Section sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Delete

assert tests.gtkMultiTextCompare({'meshname':'No Mesh Displayed!','layername':""},tbox+":Source")
assert tests.chooserStateCheck(tbox+":csList","<None>")
assert tests.chooserCheck(tbox+":csList",["<None>"])
assert tests.chooserStateCheck(tbox+':Sampling:RCFChooser','Element Segments')
assert tests.chooserCheck(tbox+':Sampling:RCFChooser',['Line Points','Element Segments'])
assert tests.gtkTextCompare(tbox+':Sampling:Element Segments:n_points:entry','2')
assert findWidget(tbox+":Sampling:Element Segments:show_distance").get_active()
assert not findWidget(tbox+":Sampling:Element Segments:show_fraction").get_active()
assert findWidget(tbox+":Sampling:Element Segments:show_x").get_active()
assert findWidget(tbox+":Sampling:Element Segments:show_y").get_active()
assert tests.sensitizationCheck({'Rename':False,'Edit':False,'Copy':False,'Remove':False},tbox)
assert tests.chooserStateCheck(tbox+':Destination:TextDestChooser','newlayer_test.out')
assert tests.chooserCheck(tbox+':Destination:TextDestChooser',['<Message Window>', 'test.out', 'copy_test.out', 'edit_test.out', 'rename_test.out', 'newlayer_test.out'])
assert tests.sensitizationCheck({'New':True,'Clear':True},tbox+":Destination")
assert not tests.is_sensitive(tbox+":Go")

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
assert tests.filediff("session.log")

findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint OOF.Graphics_1.File.Close
