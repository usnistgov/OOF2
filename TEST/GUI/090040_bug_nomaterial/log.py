# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

## This tests for the absense of a bug that crashed the program when
## computing PropertyOutputs of Meshes that had elements with no
## assigned Material.

import tests

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 511)

# Create a 4x4 pixel Microstructure
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
checkpoint meshable button set
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(210, 236)
findWidget('Dialog-Create Microstructure:width_in_pixels').set_text('')
findWidget('Dialog-Create Microstructure:width_in_pixels').set_text('4')
findWidget('Dialog-Create Microstructure:height_in_pixels').set_text('')
findWidget('Dialog-Create Microstructure:height_in_pixels').set_text('4')
findWidget('Dialog-Create Microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
checkpoint pixel page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
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

# Add isotropic elasticity
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Color')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Isotropic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open a graphics window
findMenu(findWidget('OOF2:MenuBar'), ['Settings', 'Graphics_Defaults', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
wevent(findWidget('Dialog-New_Layer_Policy:policy'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Always']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
wevent(findWidget('Dialog-New_Layer_Policy:policy'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Settings.Graphics_Defaults.New_Layer_Policy
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1').resize(800, 492)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New

# Add a microstructure material display
findWidget('OOF2 Graphics 1').resize(800, 492)
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findWidget('chooserPopup-TBChooser').deactivate() # MenuLogger
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New
findWidget('Dialog-New').resize(395, 532)
findWidget('Dialog-New:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New

# Select all pixels around the perimeter
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(249)
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
findGfxWindow('Graphics_1').simulateMouse('down', 0.07475, 0.9095, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.07475, 0.9095, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
findGfxWindow('Graphics_1').simulateMouse('down', 0.32675, 0.8815, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.32675, 0.8815, 1, True, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
findGfxWindow('Graphics_1').simulateMouse('down', 0.55075, 0.8675, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.55075, 0.8675, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.55075, 0.8675, 1, True, False)
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
findGfxWindow('Graphics_1').simulateMouse('down', 0.84125, 0.857, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.84125, 0.857, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.84125, 0.8535, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.84125, 0.8535, 1, True, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
findGfxWindow('Graphics_1').simulateMouse('down', 0.88325, 0.668, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.88325, 0.668, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.88325, 0.661, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.88325, 0.661, 1, True, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
findGfxWindow('Graphics_1').simulateMouse('down', 0.90775, 0.402, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.90775, 0.402, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.91125, 0.388, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.91125, 0.381, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.91125, 0.381, 1, True, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
findGfxWindow('Graphics_1').simulateMouse('down', 0.88325, 0.1535, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.88325, 0.1535, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.88325, 0.1535, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.88325, 0.1535, 1, True, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
findGfxWindow('Graphics_1').simulateMouse('down', 0.60675, 0.0975, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.60325, 0.0975, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.59275, 0.0975, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.59275, 0.0975, 1, True, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
findGfxWindow('Graphics_1').simulateMouse('down', 0.45275, 0.108, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.45275, 0.108, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.45275, 0.108, 1, True, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
findGfxWindow('Graphics_1').simulateMouse('down', 0.15875, 0.0905, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.15875, 0.0905, 1, True, False)
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
findGfxWindow('Graphics_1').simulateMouse('down', 0.12025, 0.3285, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.12025, 0.3285, 1, True, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
findGfxWindow('Graphics_1').simulateMouse('down', 0.13775, 0.605, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.13775, 0.605, 1, True, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point

# Assign the material to the selected pixels
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(235, 122)
findWidget('Dialog-Assign material material to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Assign

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
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton page sensitized
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
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
checkpoint contourmap info updated for Graphics_1
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
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.New

# Create a mesh
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
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
checkpoint Graphics_1 Skeleton Info sensitized
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
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.New

# Create a display later for filled contours of total energy
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
findWidget('Dialog-New').resize(483, 597)
wevent(findWidget('Dialog-New:how:Filled Contour:what:what_0'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New:how:Filled Contour:what:what_0').get_window())
checkpoint toplevel widget mapped chooserPopup-what_0
findMenu(findWidget('chooserPopup-what_0'), ['Energy']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-what_0') # MenuItemLogger
findWidget('Dialog-New:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 6.8000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New
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
