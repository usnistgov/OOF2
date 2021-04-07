# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Check that the homogeneity index on the Skeleton page is updated
# when Materials are added to or removed from pixels.

import tests

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction

# Create a microstructure
findWidget('OOF2').resize(782, 511)
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(210, 236)
findWidget('OOF2').resize(782, 545)
findWidget('Dialog-Create Microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
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
checkpoint OOF.Microstructure.New

# Set the default color for skeleton edges to gray 0.7
findWidget('OOF2').resize(782, 545)
findMenu(findWidget('OOF2:MenuBar'), ['Settings', 'Mesh_Defaults']).activate()
findMenu(findWidget('OOF2:MenuBar'), ['Settings', 'Output_Formatting']).activate()
findMenu(findWidget('OOF2:MenuBar'), ['Settings', 'Mesh_Defaults']).activate()
findMenu(findWidget('OOF2:MenuBar'), ['Settings', 'Graphics_Defaults', 'Skeletons']).activate()
findMenu(findWidget('OOF2:MenuBar'), ['Settings', 'Graphics_Defaults', 'Skeletons', 'Skeleton_Edges']).activate()
checkpoint toplevel widget mapped Dialog-Skeleton_Edges
findWidget('Dialog-Skeleton_Edges').resize(281, 242)
findWidget('Dialog-Skeleton_Edges:color:TranslucentGray:gray:entry').set_text('0.')
findWidget('Dialog-Skeleton_Edges:color:TranslucentGray:gray:entry').set_text('0.7')
widget_0=findWidget('Dialog-Skeleton_Edges:color:TranslucentGray:gray:entry')
if widget_0: wevent(widget_0, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0.get_window())
del widget_0
findWidget('Dialog-Skeleton_Edges:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Settings.Graphics_Defaults.Skeletons.Skeleton_Edges

# Create a skeleton 
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
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
assert tests.homogindex(1.0)

# Set default new layer policy to Single
findMenu(findWidget('OOF2:MenuBar'), ['Settings', 'Graphics_Defaults', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
wevent(findWidget('Dialog-New_Layer_Policy:policy'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Settings.Graphics_Defaults.New_Layer_Policy

# Open a graphics window
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([10]))
checkpoint OOF.Graphics_1.Layer.Select
findWidget('OOF2 Graphics 1').resize(800, 492)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New

# Create a microstructure material display layer
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New
findWidget('Dialog-New').resize(395, 532)
findWidget('Dialog-New:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New

# Select a rectangle of pixels (0<=x<=5, 0<=y<=4)
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(249)
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Rectangle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 0.0003756574, 0.016153268, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.0003756574, 0.016153268, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.010894065, 0.026671675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.021412472, 0.051214626, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.038943151, 0.089782119, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.045955422, 0.12484348, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.056473829, 0.15289256, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.066992236, 0.18094165, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.070498372, 0.19847233, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.070498372, 0.21950914, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.077510644, 0.23703982, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.088029051, 0.26508891, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.10555973, 0.28612572, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.13360882, 0.30015026, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.16867017, 0.31066867, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.2107438, 0.32118708, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.25281743, 0.32819935, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.28787879, 0.33170548, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.32294015, 0.33521162, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.3474831, 0.33521162, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36501377, 0.33521162, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.38254445, 0.33521162, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.39306286, 0.33871776, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.39306286, 0.33871776, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.40007513, 0.33871776, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.40358127, 0.33871776, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.40358127, 0.33871776, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.4070874, 0.34222389, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.41059354, 0.34222389, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.42812422, 0.34573003, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.44916103, 0.34923616, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.46318557, 0.3527423, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.47019785, 0.3527423, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.47370398, 0.3527423, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.47370398, 0.3527423, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.47370398, 0.3527423, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.48071625, 0.35624843, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.48422239, 0.35624843, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.48422239, 0.35624843, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.48772852, 0.35624843, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.48772852, 0.35624843, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.48772852, 0.35624843, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.48772852, 0.35624843, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Rectangle

# Create a material
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
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

# Assign the material to the selected pixels
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(235, 122)
findWidget('Dialog-Assign material material to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Assign

# Switch to the Skeleton page to check homogeneity
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton
checkpoint skeleton page sensitized
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
assert tests.homogindex(0.95)

# Remove material from all pixels
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane:Material:RemoveMaterial').clicked()
checkpoint toplevel widget mapped Dialog-Remove the assigned material from pixels
findWidget('Dialog-Remove the assigned material from pixels').resize(235, 122)
wevent(findWidget('Dialog-Remove the assigned material from pixels:pixels'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Remove the assigned material from pixels:pixels').get_window())
checkpoint toplevel widget mapped chooserPopup-pixels
findMenu(findWidget('chooserPopup-pixels'), ['<every>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-pixels') # MenuItemLogger
findWidget('Dialog-Remove the assigned material from pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Remove

# Go back to the Skeleton page to check homogeneity
findWidget('OOF2').resize(782, 545)
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Skeleton
checkpoint skeleton page sensitized
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
assert tests.homogindex(1.0)

# Go back to the Materials page
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint Materials page updated
checkpoint page installed Materials

# Assign the material to the selected pixels again
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(235, 122)
findWidget('Dialog-Assign material material to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Assign

# Go back to the Skeleton page to check homogeneity again
findWidget('OOF2').resize(782, 545)
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint page installed Active Area
findWidget('OOF2:Active Area Page:Pane').set_position(529)
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton
checkpoint skeleton page sensitized
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
assert tests.homogindex(0.95)

# Go back to the Materials page and delete the material
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane:Material:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(192, 86)
findWidget('Questioner:OK').clicked()
checkpoint Materials page updated
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Delete

# Go back to the Skeleton page to check homogeneity yet again
findWidget('OOF2').resize(782, 545)
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint page installed Active Area
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton
checkpoint skeleton page sensitized
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
assert tests.homogindex(1.0)

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
