checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# Basic graphics window tests

import tests

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 511)

# Open an empty graphics window
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
findWidget('OOF2 Graphics 1').resize(800, 492)
findWidget('OOF2').resize(782, 545)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1').resize(800, 492)
assert tests.sensitizationCheck0()
assert tests.layerCheck()
assert tests.allLayerNames('Info', 'Selected Nodes', 'Pinned Nodes', 'Moving Nodes', 'Pixel Info', 'Selected Segments', 'Illegal Elements', 'Info', 'Selected Boundary', 'Cross Section', 'Selected Elements', 'BitmapOverlay', 'BitmapOverlay')
assert tests.noContourBounds()

# Toggle "List All Layers" on
findWidget('OOF2 Graphics 1').resize(800, 492)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'List_All_Layers']).activate()
checkpoint OOF.Graphics_1.Settings.List_All_Layers
# Unfortunately, there doesn't seem to be a way of checking that
# layers are listed, using the gtk.TreeView API.  tests.layerCheck
# just checks for the "listed" flag in the actual layer, and doesn't
# care whether or not the GUI is using the flag.  Toggling
# List_All_Layers doesn't change the flag. IS THAT STILL TRUE?
assert tests.layerCheck()

# Toggle "Long Layer Names" on
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Long_Layer_Names']).activate()
checkpoint OOF.Graphics_1.Settings.Long_Layer_Names
# Similarly, there's no way to check whether long layer names are being used.

# Toggle "Long Layer Names" off
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Long_Layer_Names']).activate()
checkpoint OOF.Graphics_1.Settings.Long_Layer_Names

# Toggle "List All Layers" off
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'List_All_Layers']).activate()
checkpoint OOF.Graphics_1.Settings.List_All_Layers

# Set New Layer Policy to Single
findWidget('OOF2 Graphics 1').resize(800, 492)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
wevent(findWidget('Dialog-New_Layer_Policy:policy'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Graphics_1.Settings.New_Layer_Policy

# Create a Microstructure from "examples/small.ppm"
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
checkpoint page installed Microstructure
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:NewFromFile').clicked()
checkpoint toplevel widget mapped Dialog-Load Image and create Microstructure
findWidget('Dialog-Load Image and create Microstructure').resize(237, 200)
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('e')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('ex')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('exa')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('exam')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examp')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('exampl')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('example')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/s')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/sm')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/sma')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/smal')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/smal.')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/smal')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/small')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/small.')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/small.p')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/small.pp')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/small.ppm')
findWidget('Dialog-Load Image and create Microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
checkpoint pixel page sensitized
checkpoint mesh bdy page updated
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
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
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Microstructure.Create_From_ImageFile
assert tests.sensitizationCheck0()
assert tests.layerCheck("Bitmap")
assert tests.selectedLayerCheck(None)
assert tests.allLayerNames('Info', 'Selected Nodes', 'Pinned Nodes', 'Moving Nodes', 'Pixel Info', 'Selected Segments', 'Illegal Elements', 'Info', 'Selected Boundary', 'Cross Section', 'Selected Elements', 'BitmapOverlay', 'BitmapOverlay', 'Bitmap')

# Create a Skeleton
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
checkpoint page installed Skeleton
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Pane').set_position(417)
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(346, 254)
findWidget('Dialog-New skeleton:x_elements').set_text('')
findWidget('Dialog-New skeleton:x_elements').set_text('6')
findWidget('Dialog-New skeleton:y_elements').set_text('')
findWidget('Dialog-New skeleton:y_elements').set_text('6')
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
assert tests.sensitizationCheck0()
assert tests.layerCheck("Bitmap", "Element Edges")
assert tests.allLayerNames('Info', 'Selected Nodes', 'Pinned Nodes', 'Moving Nodes', 'Pixel Info', 'Selected Segments', 'Illegal Elements', 'Info', 'Selected Boundary', 'Cross Section', 'Element Edges', 'Selected Elements', 'BitmapOverlay', 'BitmapOverlay', 'Bitmap')

# Select the Skeleton layer
wevent(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([10]))
checkpoint OOF.Graphics_1.Layer.Select
assert tests.sensitizationCheck1()

# Add a Material color layer for the Skeleton
findWidget('OOF2 Graphics 1').resize(800, 492)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New Graphics Layer
findWidget('Dialog-New Graphics Layer').resize(395, 532)
wevent(findWidget('Dialog-New Graphics Layer:category'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New Graphics Layer:category').get_window())
checkpoint toplevel widget mapped chooserPopup-category
findMenu(findWidget('chooserPopup-category'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-category') # MenuItemLogger
wevent(findWidget('Dialog-New Graphics Layer:how:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New Graphics Layer:how:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Material Color']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-New Graphics Layer:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.6000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New
assert tests.layerCheck("Bitmap", "Material Color", "Element Edges")
assert tests.selectedLayerCheck("Material Color")
assert tests.allLayerNames('Info', 'Selected Nodes', 'Pinned Nodes', 'Moving Nodes', 'Pixel Info', 'Selected Segments', 'Illegal Elements', 'Info', 'Selected Boundary', 'Cross Section', 'Element Edges', 'Selected Elements', 'BitmapOverlay', 'BitmapOverlay', 'Material Color', 'Bitmap')
assert tests.sensitizationCheck1()
assert tests.noContourBounds()

# Delete Material color layer
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'Delete']).activate()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Delete
assert tests.sensitizationCheck0()
assert tests.layerCheck("Bitmap", "Element Edges")
assert tests.selectedLayerCheck(None)
assert tests.allLayerNames('Info', 'Selected Nodes', 'Pinned Nodes', 'Moving Nodes', 'Pixel Info', 'Selected Segments', 'Illegal Elements', 'Info', 'Selected Boundary', 'Cross Section', 'Element Edges', 'Selected Elements', 'BitmapOverlay', 'BitmapOverlay', 'Bitmap')
assert tests.sensitizationCheck0()

# Create new skeleton material layer again
findWidget('OOF2 Graphics 1').resize(800, 492)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New Graphics Layer
findWidget('Dialog-New Graphics Layer').resize(203, 193)
findWidget('Dialog-New Graphics Layer:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.6000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New
assert tests.layerCheck("Bitmap", "Material Color", "Element Edges")
assert tests.selectedLayerCheck("Material Color")
assert tests.allLayerNames('Info', 'Selected Nodes', 'Pinned Nodes', 'Moving Nodes', 'Pixel Info', 'Selected Segments', 'Illegal Elements', 'Info', 'Selected Boundary', 'Cross Section', 'Element Edges', 'Selected Elements', 'BitmapOverlay', 'BitmapOverlay', 'Material Color', 'Bitmap')
assert tests.sensitizationCheck1()

# Lower Skeleton edge layer to bottom
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.5000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.4000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.3000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.1000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 3.9000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 3.7000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 3.6000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 3.4000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 3.3000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 3.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 3.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.8000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.7000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.5000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.1000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.9000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.8000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.7000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.6000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.5000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_hadjustment().set_value( 7.6989876674950e-01)
wevent(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([10]))
checkpoint OOF.Graphics_1.Layer.Select
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'Lower', 'To_Bottom']).activate()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.6000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Lower.To_Bottom
assert tests.sensitizationCheck2()
assert tests.layerCheck("Element Edges", "Bitmap", "Material Color")
assert tests.selectedLayerCheck("Element Edges")
assert tests.allLayerNames('Info', 'Selected Nodes', 'Pinned Nodes', 'Moving Nodes', 'Pixel Info', 'Selected Segments', 'Illegal Elements', 'Info', 'Selected Boundary', 'Cross Section', 'Selected Elements', 'BitmapOverlay', 'BitmapOverlay', 'Material Color', 'Bitmap', 'Element Edges')

# Reorder the layers with "Reorder All"
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'Reorder_All']).activate()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Reorder_All
assert tests.sensitizationCheck1()
assert tests.layerCheck("Bitmap", "Material Color", "Element Edges")
assert tests.selectedLayerCheck("Element Edges")
assert tests.allLayerNames('Info', 'Selected Nodes', 'Pinned Nodes', 'Moving Nodes', 'Pixel Info', 'Selected Segments', 'Illegal Elements', 'Info', 'Selected Boundary', 'Cross Section', 'Element Edges', 'Selected Elements', 'BitmapOverlay', 'BitmapOverlay', 'Material Color', 'Bitmap')

# Raise image layer until it's above the Skeleton edge layer
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.1000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.5000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 3.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.5000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.6000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_hadjustment().set_value( 1.7698987667495e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_hadjustment().set_value( 1.9996483385011e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_hadjustment().set_value( 2.9996483385011e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_hadjustment().set_value( 3.9996483385011e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_hadjustment().set_value( 4.9996483385011e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_hadjustment().set_value( 5.9996483385011e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_hadjustment().set_value( 6.9996483385011e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_hadjustment().set_value( 7.9996483385011e+00)
wevent(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([15]))
checkpoint OOF.Graphics_1.Layer.Select
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_hadjustment().set_value( 5.9996483385011e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_hadjustment().set_value( 4.9996483385011e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_hadjustment().set_value( 1.9996483385011e+00)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'Raise', 'One_Level']).activate()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.6000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Raise.One_Level
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'Raise', 'One_Level']).activate()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.6000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Raise.One_Level
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'Raise', 'One_Level']).activate()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.4000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Raise.One_Level
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'Raise', 'One_Level']).activate()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.2000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Raise.One_Level
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'Raise', 'One_Level']).activate()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Raise.One_Level
assert tests.sensitizationCheck3()
assert tests.allLayerNames('Info', 'Selected Nodes', 'Pinned Nodes', 'Moving Nodes', 'Pixel Info', 'Selected Segments', 'Illegal Elements', 'Info', 'Selected Boundary', 'Cross Section', 'Bitmap', 'Element Edges', 'Selected Elements', 'BitmapOverlay', 'BitmapOverlay', 'Material Color')
assert tests.layerCheck("Material Color", "Element Edges", "Bitmap")
assert tests.selectedLayerCheck("Bitmap")

# Reorder again
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'Reorder_All']).activate()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.6000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Reorder_All
assert tests.sensitizationCheck4()
assert tests.layerCheck("Bitmap", "Material Color", "Element Edges")
assert tests.selectedLayerCheck("Bitmap")
assert tests.allLayerNames('Info', 'Selected Nodes', 'Pinned Nodes', 'Moving Nodes', 'Pixel Info', 'Selected Segments', 'Illegal Elements', 'Info', 'Selected Boundary', 'Cross Section', 'Element Edges', 'Selected Elements', 'BitmapOverlay', 'BitmapOverlay', 'Material Color', 'Bitmap')

# Hide the Skeleton Material layer from the menu bar
wevent(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([14]))
checkpoint OOF.Graphics_1.Layer.Select
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'Hide']).activate()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.6000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Hide
# TODO: I don't know how to check the state of a CellRendererToggle,
# so there's no test here to see if the show/hide buttons are set
# correctly. Gtk.CellRendererToggle has set_active() and get_active()
# methods, but they appear to be only usable in the context of a
# "toggled" signal handler, where an iterator for the row is provided.
# There doesn't seem to be any way to call get_active() on a
# particular row.
assert tests.sensitizationCheck5()

# Unhide the Skeleton material layer from the layer list
wevent(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
findCellRenderer(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), col=0, rend=0).emit('toggled', Gtk.TreePath(14))
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.6000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Show
assert tests.sensitizationCheck1()

# Create a Mesh
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(130)
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(299, 244)
findWidget('Dialog-Create a new mesh:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.8000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info cleared position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint toplevel widget mapped Warning
findWidget('Warning').resize(323, 68)
findWidget('Warning:widget_GTK_RESPONSE_OK').clicked()
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
checkpoint toplevel widget mapped Warning
findWidget('Warning').resize(323, 68)
findWidget('Warning:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.New

# Create a Material and assign it to all pixels
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findWidget('chooserPopup-PageMenu').deactivate() # MenuLogger
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Materials Page:Pane').set_position(289)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(196, 122)
findWidget('Dialog-New material:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.New
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(214, 122)
wevent(findWidget('Dialog-Assign material material to pixels:pixels'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Assign material material to pixels:pixels').get_window())
checkpoint toplevel widget mapped chooserPopup-pixels
findMenu(findWidget('chooserPopup-pixels'), ['<every>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-pixels') # MenuItemLogger
findWidget('Dialog-Assign material material to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Assign

# Give Material a Color Property w/ gray=0.5
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Color')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Color
findWidget('Dialog-Parametrize Color').resize(279, 206)
findWidget('Dialog-Parametrize Color:color:TranslucentGray:gray:entry').set_text('0.')
findWidget('Dialog-Parametrize Color:color:TranslucentGray:gray:entry').set_text('0.5')
widget_0=findWidget('Dialog-Parametrize Color:color:TranslucentGray:gray:entry')
if widget_0: wevent(widget_0, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0.get_window())
del widget_0
findWidget('Dialog-Parametrize Color:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Property.Parametrize.Color
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
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
checkpoint property selected
checkpoint Materials page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Add_property

# Define Temperature
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Fields & Equations']).activate() # MenuItemLogger
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Fields & Equations Page:HPane').set_position(470)
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Subproblem.Field.Define

# Initialize temperature to x*y
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Solver']).activate() # MenuItemLogger
checkpoint Solver page sensitized
checkpoint page installed Solver
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Solver Page:VPane').set_position(170)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Solver page sensitized
tree=findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([0]), column)
checkpoint toplevel widget mapped Dialog-Initialize field Temperature
findWidget('Dialog-Initialize field Temperature').resize(232, 134)
wevent(findWidget('Dialog-Initialize field Temperature:initializer:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Initialize field Temperature:initializer:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['XYTFunction']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Initialize field Temperature').resize(245, 134)
findWidget('Dialog-Initialize field Temperature:initializer:XYTFunction:function').set_text('x')
findWidget('Dialog-Initialize field Temperature:initializer:XYTFunction:function').set_text('x*')
findWidget('Dialog-Initialize field Temperature:initializer:XYTFunction:function').set_text('x*y')
findWidget('Dialog-Initialize field Temperature:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Set_Field_Initializer
findWidget('OOF2:Solver Page:VPane:FieldInit:Apply').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Apply_Field_Initializers
assert tests.noContourBounds()
assert tests.noContourInterval()

# Add a solid fill mesh display layer
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New Graphics Layer
findWidget('Dialog-New Graphics Layer').resize(203, 193)
wevent(findWidget('Dialog-New Graphics Layer:category'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New Graphics Layer:category').get_window())
checkpoint toplevel widget mapped chooserPopup-category
findMenu(findWidget('chooserPopup-category'), ['Mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-category') # MenuItemLogger
findWidget('Dialog-New Graphics Layer').resize(467, 298)
wevent(findWidget('Dialog-New Graphics Layer:how:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New Graphics Layer:how:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Solid Fill']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-New Graphics Layer').resize(483, 561)
findWidget('Dialog-New Graphics Layer:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 9.0000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New
assert tests.contourBounds(156, 1.89e4, tolerance=1.e-3)
assert tests.noContourInterval()

# Change aspect ratio of the contour map to 3
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Aspect_Ratio']).activate()
checkpoint toplevel widget mapped Dialog-Aspect_Ratio
findWidget('Dialog-Aspect_Ratio').resize(192, 92)
findWidget('Dialog-Aspect_Ratio:ratio').set_text('')
findWidget('Dialog-Aspect_Ratio:ratio').set_text('3')
findWidget('Dialog-Aspect_Ratio:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Settings.Aspect_Ratio

# Click on the contour map
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(665)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(210)
findGfxWindow('Graphics_1').simulateCMapMouse('up', 2868.6523, 10327.148, 1, 0, 0)
checkpoint contourmap info updated for Graphics_1
assert tests.contourInterval(9.84e+03, 1.02e+04)

# Change contour marker size to 5
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Contourmap_Marker_Size']).activate()
checkpoint toplevel widget mapped Dialog-Contourmap_Marker_Size
findWidget('Dialog-Contourmap_Marker_Size').resize(192, 92)
findWidget('Dialog-Contourmap_Marker_Size:width').set_text('')
findWidget('Dialog-Contourmap_Marker_Size:width').set_text('5')
findWidget('Dialog-Contourmap_Marker_Size:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Graphics_1.Settings.Contourmap_Marker_Size

# Change contour map marker color
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Color', 'Contourmap_Marker']).activate()
checkpoint toplevel widget mapped Dialog-Contourmap_Marker
findWidget('Dialog-Contourmap_Marker').resize(279, 206)
findWidget('Dialog-Contourmap_Marker:color:TranslucentGray:gray:slider').get_adjustment().set_value( 5.2777777777778e-01)
findWidget('Dialog-Contourmap_Marker:color:TranslucentGray:gray:slider').get_adjustment().set_value( 5.8333333333333e-01)
findWidget('Dialog-Contourmap_Marker:color:TranslucentGray:gray:slider').get_adjustment().set_value( 6.2500000000000e-01)
findWidget('Dialog-Contourmap_Marker:color:TranslucentGray:gray:slider').get_adjustment().set_value( 7.3611111111111e-01)
findWidget('Dialog-Contourmap_Marker:color:TranslucentGray:gray:slider').get_adjustment().set_value( 9.0277777777778e-01)
findWidget('Dialog-Contourmap_Marker:color:TranslucentGray:gray:slider').get_adjustment().set_value( 9.4444444444444e-01)
findWidget('Dialog-Contourmap_Marker:color:TranslucentGray:gray:slider').get_adjustment().set_value( 9.7222222222222e-01)
findWidget('Dialog-Contourmap_Marker:color:TranslucentGray:gray:slider').get_adjustment().set_value( 9.8611111111111e-01)
findWidget('Dialog-Contourmap_Marker:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Graphics_1.Settings.Color.Contourmap_Marker
# Clear the contour map marker
findWidget('OOF2 Graphics 1:Pane0:Pane1:ContourMap:Clear').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
checkpoint contourmap info updated for Graphics_1
assert tests.noContourInterval()

# Change background color
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Color', 'Background']).activate()
checkpoint toplevel widget mapped Dialog-Background
findWidget('Dialog-Background').resize(273, 172)
findWidget('Dialog-Background:color:Gray:gray:slider').get_adjustment().set_value( 9.8611111111111e-01)
findWidget('Dialog-Background:color:Gray:gray:slider').get_adjustment().set_value( 9.7222222222222e-01)
findWidget('Dialog-Background:color:Gray:gray:slider').get_adjustment().set_value( 9.3055555555556e-01)
findWidget('Dialog-Background:color:Gray:gray:slider').get_adjustment().set_value( 9.1666666666667e-01)
findWidget('Dialog-Background:color:Gray:gray:slider').get_adjustment().set_value( 9.0277777777778e-01)
findWidget('Dialog-Background:color:Gray:gray:slider').get_adjustment().set_value( 8.8888888888889e-01)
findWidget('Dialog-Background:color:Gray:gray:slider').get_adjustment().set_value( 8.6111111111111e-01)
findWidget('Dialog-Background:color:Gray:gray:slider').get_adjustment().set_value( 8.4722222222222e-01)
findWidget('Dialog-Background:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Graphics_1.Settings.Color.Background

# Raise the temperature display
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'Raise', 'One_Level']).activate()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 7.0000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Raise.One_Level

# Zoom in from Settings menu
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'In']).activate()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.0000000000000e+01)
checkpoint OOF.Graphics_1.Settings.Zoom.In
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 7.5000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('scroll', -0, -0, 0, False, False)

# Zoom in again
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'In']).activate()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 1.3700000000000e+02)
checkpoint OOF.Graphics_1.Settings.Zoom.In
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 1.8700000000000e+02)

# Zoom in again
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'In']).activate()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 3.1300000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 3.5500000000000e+02)
checkpoint OOF.Graphics_1.Settings.Zoom.In

# Zoom to fill
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'Fill_Window']).activate()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 0.0000000000000e+00)
checkpoint OOF.Graphics_1.Settings.Zoom.Fill_Window
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 0.0000000000000e+00)

# Zoom out
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'Out']).activate()
findGfxWindow('Graphics_1').simulateMouse('scroll', -1, -0, 0, False, False)
checkpoint OOF.Graphics_1.Settings.Zoom.Out
findGfxWindow('Graphics_1').simulateMouse('scroll', -0, -0, 0, False, False)

# Zoom out
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'In']).activate()
checkpoint OOF.Graphics_1.Settings.Zoom.In
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'Out']).activate()
checkpoint OOF.Graphics_1.Settings.Zoom.Out
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'Out']).activate()
checkpoint OOF.Graphics_1.Settings.Zoom.Out

# Zoom to fill
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'Fill_Window']).activate()
checkpoint OOF.Graphics_1.Settings.Zoom.Fill_Window

# Change margin to 0.01
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Margin']).activate()
checkpoint toplevel widget mapped Dialog-Margin
findWidget('Dialog-Margin').resize(192, 92)
findWidget('Dialog-Margin:fraction').set_text('0.0')
findWidget('Dialog-Margin:fraction').set_text('0.01')
findWidget('Dialog-Margin:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Graphics_1.Settings.Margin

# Redraw from file menu
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['File', 'Redraw']).activate()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.File.Redraw

# Zoom to fill again
findWidget('OOF2 Graphics 1').resize(800, 492)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'Fill_Window']).activate()
checkpoint OOF.Graphics_1.Settings.Zoom.Fill_Window

# Add a solid contour mesh layer displaying x**2 + y**2
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New Graphics Layer
findWidget('Dialog-New Graphics Layer').resize(483, 561)
wevent(findWidget('Dialog-New Graphics Layer:how:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New Graphics Layer:how:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Filled Contour']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-New Graphics Layer').resize(483, 597)
wevent(findWidget('Dialog-New Graphics Layer:how:Filled Contour:what:what_0'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New Graphics Layer:how:Filled Contour:what:what_0').get_window())
checkpoint toplevel widget mapped chooserPopup-what_0
findMenu(findWidget('chooserPopup-what_0'), ['XYFunction']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-what_0') # MenuItemLogger
findWidget('Dialog-New Graphics Layer:how:Filled Contour:what:Parameters:f').set_text('')
findWidget('Dialog-New Graphics Layer:how:Filled Contour:what:Parameters:f').set_text('x')
findWidget('Dialog-New Graphics Layer:how:Filled Contour:what:Parameters:f').set_text('x*')
findWidget('Dialog-New Graphics Layer:how:Filled Contour:what:Parameters:f').set_text('x**')
findWidget('Dialog-New Graphics Layer:how:Filled Contour:what:Parameters:f').set_text('x**2')
findWidget('Dialog-New Graphics Layer:how:Filled Contour:what:Parameters:f').set_text('x**2 ')
findWidget('Dialog-New Graphics Layer:how:Filled Contour:what:Parameters:f').set_text('x**2 +')
findWidget('Dialog-New Graphics Layer:how:Filled Contour:what:Parameters:f').set_text('x**2 + ')
findWidget('Dialog-New Graphics Layer:how:Filled Contour:what:Parameters:f').set_text('x**2 + y')
findWidget('Dialog-New Graphics Layer:how:Filled Contour:what:Parameters:f').set_text('x**2 + y*')
findWidget('Dialog-New Graphics Layer:how:Filled Contour:what:Parameters:f').set_text('x**2 + y**')
findWidget('Dialog-New Graphics Layer:how:Filled Contour:what:Parameters:f').set_text('x**2 + y**2')
wevent(findWidget('Dialog-New Graphics Layer:how:Filled Contour:colormap:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New Graphics Layer:how:Filled Contour:colormap:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['TequilaSunrise']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-New Graphics Layer:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 7.0000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New
assert tests.contourBounds(0, 4.5e+04, tolerance=1.e-3)

findWidget('OOF2 Graphics 1').resize(800, 492)
findWidget('OOF2').resize(782, 545)

# Lower the x**2 + y**2 layer to the bottom
wevent(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), Gdk.EventType.BUTTON_PRESS, button=3, state=0, window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
checkpoint toplevel widget mapped PopUp-0
findMenu(findWidget('PopUp-0'), ['Lower', 'To_Bottom']).activate() # MenuItemLogger
deactivatePopup('PopUp-0') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.1200000000000e+02)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Lower.To_Bottom
assert tests.contourBounds(156, 1.89e+04, tolerance=1.e-3)

# Raise the layer back to the top
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'Raise', 'To_Top']).activate()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Raise.To_Top
assert tests.contourBounds(0, 4.5e+04, tolerance=1.e-3)

# Hide the layer
wevent(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
findCellRenderer(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), col=0, rend=0).emit('toggled', Gtk.TreePath(0))
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Hide
assert tests.contourBounds(156, 1.89e+04, tolerance=1.e-3)

# Unhide it
wevent(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
findCellRenderer(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), col=0, rend=0).emit('toggled', Gtk.TreePath(0))
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Show
assert tests.contourBounds(0, 4.5e+04, tolerance=1.e-3)

findMenu(findWidget('OOF2:MenuBar'), ['File', 'Save', 'Python_Log']).activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(192, 122)
findWidget('Dialog-Python_Log:filename').set_text('d')
findWidget('Dialog-Python_Log:filename').set_text('')
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
