checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.15 $
# $Author: langer $
# $Date: 2011/01/14 22:43:17 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests

findMenu(findWidget('OOF2:MenuBar'), 'Windows:Graphics:New').activate()
checkpoint Graphics_1 Mesh Info sensitized
checkpoint toplevel widget mapped OOF2 Graphics 1
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(250)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(693)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(250)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(693)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1').resize(800, 400)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(250)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(693)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), 'Layer:New').activate()
checkpoint layereditor layerset changed
checkpoint toplevel widget mapped OOF2 Graphics Layer Editor
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.New
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
assert tests.sensitivityCheck0()
assert tests.categoryCheck("Nothing")
assert tests.objectCheck("Nothing", "Nobody")
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
findWidget('OOF2:Microstructure Page:Pane').set_position(150)
findWidget('OOF2:Microstructure Page:NewFromFile').clicked()
checkpoint toplevel widget mapped Dialog-Load Image and create Microstructure
findWidget('Dialog-Load Image and create Microstructure').resize(342, 144)
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('e')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('ex')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('exa')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('exam')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examp')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('exampl')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('example')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_s')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_sm')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_sma')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_smal')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small.')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small.p')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small.pg')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small.pgm')
findWidget('Dialog-Load Image and create Microstructure:gtk-ok').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Microstructure Page:Pane').set_position(153)
checkpoint contourmap info updated for Graphics_1
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint OOF.Microstructure.Create_From_ImageFile
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.layerCheck("Graphics_1", "Bitmap")
assert tests.selectedLayerCheck("Graphics_1", None)
assert tests.sensitivityCheck0()
findWidget('OOF2:Microstructure Page:Pane').set_position(153)
setComboBox(findWidget('OOF2 Graphics Layer Editor:ObjectScroll:category'), 'Image')
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.DisplayedObject
assert tests.categoryCheck("Image")
assert tests.objectCheck("Microstructure", "K1_small.pgm")
assert tests.objectCheck("Image", "K1_small.pgm")
assert tests.sensitivityCheck1()
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
findWidget('OOF2').resize(593, 434)
findWidget('OOF2:Skeleton Page:Pane').set_position(249)
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
checkpoint skeleton page sensitized
findWidget('Dialog-New skeleton').resize(334, 152)
findWidget('Dialog-New skeleton:gtk-ok').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton page sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint OOF.Skeleton.New
findWidget('OOF2:Skeleton Page:Pane').set_position(249)
assert tests.layerCheck("Graphics_1", "Bitmap", "Element Edges")
assert tests.selectedLayerCheck("Graphics_1", None)
setComboBox(findWidget('OOF2 Graphics Layer Editor:ObjectScroll:category'), 'Skeleton')
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.DisplayedObject
assert tests.categoryCheck("Skeleton")
assert tests.objectCheck("Microstructure", "K1_small.pgm")
assert tests.objectCheck("Skeleton", "skeleton")
assert tests.sensitivityCheck1()
findWidget('OOF2 Graphics Layer Editor:NewLayer').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.New
assert tests.categoryCheck("Nothing")
assert tests.objectCheck("Nothing", "Nobody")
assert tests.sensitivityCheck0()
assert tests.selectedLayerCheck("Graphics_1", None)
setComboBox(findWidget('OOF2 Graphics Layer Editor:ObjectScroll:category'), 'Skeleton')
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.DisplayedObject
assert tests.categoryCheck("Skeleton")
assert tests.objectCheck("Microstructure", "K1_small.pgm")
assert tests.objectCheck("Skeleton", "skeleton")
assert tests.sensitivityCheck1()
assert tests.layerEditorListCheck()
findWidget('OOF2 Graphics Layer Editor:DisplayMethods:New').clicked()
checkpoint toplevel widget mapped Dialog-New Display Method for Skeleton skeleton
assert tests.newMethodCheck("Skeleton", "skeleton", "Element Edges")
findWidget('Dialog-New Display Method for Skeleton skeleton').resize(333, 200)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 1.5873015873016e-02)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.1746031746032e-02)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 2.0634920634921e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 2.5396825396825e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 2.6984126984127e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 2.8571428571429e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.0158730158730e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.1746031746032e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.3333333333333e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.4920634920635e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 1.0416666666667e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 2.0833333333333e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 3.1250000000000e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 5.2083333333333e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 9.3750000000000e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 1.4583333333333e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 1.8750000000000e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 2.1875000000000e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 2.3958333333333e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 2.5000000000000e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 2.6041666666667e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 2.7083333333333e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 2.8125000000000e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 2.9166666666667e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 3.0208333333333e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:gtk-ok').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint OOF.LayerEditor.LayerSet.Send
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Add_Method
assert tests.sensitivityCheck2()
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.layerEditorListCheck("Element Edges")
assert tests.layerEditorSelectionCheck("Element Edges")
assert tests.layerCheck("Graphics_1", "Bitmap", "Element Edges", "Element Edges")
assert tests.selectedLayerCheck("Graphics_1", "Element Edges")
findWidget('OOF2 Graphics Layer Editor:DisplayMethods:New').clicked()
checkpoint toplevel widget mapped Dialog-New Display Method for Skeleton skeleton
findWidget('Dialog-New Display Method for Skeleton skeleton').resize(333, 200)
assert tests.newElementEdgeWidthCheck(3)
setComboBox(findWidget('Dialog-New Display Method for Skeleton skeleton:method:Chooser'), 'Material Color')
findWidget('Dialog-New Display Method for Skeleton skeleton:gtk-ok').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint OOF.LayerEditor.LayerSet.Send
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Add_Method
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.layerCheck("Graphics_1", "Bitmap", "Material Color", "Element Edges", "Element Edges")
assert tests.selectedLayerCheck("Graphics_1", "Element Edges")
assert tests.layerEditorListCheck("Element Edges", "Material Color")
assert tests.layerEditorSelectionCheck("Material Color")
assert tests.sensitivityCheck2()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(277)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(207)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(207)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((11,))
checkpoint OOF.Graphics_1.Layer.Select
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((11,), column)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
assert tests.layerEditorListCheck("Element Edges")
assert tests.layerEditorSelectionCheck("Element Edges")
assert tests.categoryCheck("Skeleton")
assert tests.objectCheck("Skeleton", "skeleton")
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((15,))
checkpoint OOF.Graphics_1.Layer.Select
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((15,), column)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((11,))
checkpoint OOF.Graphics_1.Layer.Select
assert tests.layerEditorSelectionCheck("Material Color")
assert tests.layerEditorListCheck("Element Edges", "Material Color")
assert tests.categoryCheck("Skeleton")
assert tests.objectCheck("Skeleton", "skeleton")
assert tests.sensitivityCheck2()
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((11,), column)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
assert tests.layerEditorListCheck("Element Edges")
assert tests.layerEditorSelectionCheck("Element Edges")
assert tests.categoryCheck("Skeleton")
assert tests.objectCheck("Skeleton", "skeleton")
assert tests.sensitivityCheck2()
findWidget('OOF2 Graphics Layer Editor:DisplayMethods:Edit').clicked()
checkpoint toplevel widget mapped Dialog-New Display Method for Skeleton skeleton
findWidget('Dialog-New Display Method for Skeleton skeleton').resize(333, 200)
assert tests.newMethodCheck("Skeleton", "skeleton", "Element Edges")
assert tests.newElementEdgeWidthCheck(0)
findWidget('Dialog-New Display Method for Skeleton skeleton:gtk-cancel').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((10,))
checkpoint OOF.Graphics_1.Layer.Select
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((10,), column)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
assert tests.layerEditorSelectionCheck("Element Edges")
assert tests.layerEditorListCheck("Element Edges", "Material Color")
assert tests.sensitivityCheck2()
tree=findWidget('OOF2 Graphics Layer Editor:DisplayMethods:ListScroll:List')
column = tree.get_column(0)
tree.row_activated((0,), column)
checkpoint toplevel widget mapped Dialog-New Display Method for Skeleton skeleton
assert tests.newElementEdgeWidthCheck(3)
findWidget('Dialog-New Display Method for Skeleton skeleton').resize(333, 200)
setComboBox(findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Chooser'), 'RGBColor')
findWidget('Dialog-New Display Method for Skeleton skeleton').resize(342, 248)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 3.6507936507937e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 3.8095238095238e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 4.1269841269841e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 4.2857142857143e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 4.4444444444444e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 4.7619047619048e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 4.9206349206349e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 5.0793650793651e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 5.3968253968254e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 5.5555555555556e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 5.8730158730159e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 6.0317460317460e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 6.1904761904762e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:gtk-ok').clicked()
findWidget('OOF2 Messages 1').resize(644, 200)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint OOF.LayerEditor.LayerSet.Send
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Replace_Method
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
assert tests.layerCheck("Graphics_1", "Bitmap", "Material Color", "Element Edges", "Element Edges")
assert tests.selectedLayerCheck("Graphics_1", "Element Edges")
findWidget('OOF2 Graphics Layer Editor:DisplayMethods:ListScroll:List').get_selection().select_path((1,))
findWidget('OOF2 Graphics Layer Editor:DisplayMethods:Delete').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Delete_Method
findWidget('OOF2 Graphics Layer Editor:Send').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint OOF.LayerEditor.LayerSet.Send
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
assert tests.layerCheck("Graphics_1", "Bitmap", "Element Edges", "Element Edges")
assert tests.selectedLayerCheck("Graphics_1", "Element Edges")
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((11,))
checkpoint OOF.Graphics_1.Layer.Select
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((10,))
checkpoint OOF.Graphics_1.Layer.Select
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((10,), column)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
assert tests.layerEditorListCheck("Element Edges")
assert tests.layerEditorSelectionCheck("Element Edges")
assert tests.sensitivityCheck2()
assert tests.categoryCheck("Skeleton")
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((11,))
checkpoint OOF.Graphics_1.Layer.Select
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((11,), column)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
assert tests.layerEditorSelectionCheck("Element Edges")
assert tests.layerEditorListCheck("Element Edges")
findCellRenderer(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), col=0, rend=0).emit('toggled', '11')
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint OOF.Graphics_1.Layer.Hide
findCellRenderer(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), col=0, rend=0).emit('toggled', '11')
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint OOF.Graphics_1.Layer.Show
findCellRenderer(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), col=0, rend=0).emit('toggled', '10')
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((10,))
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint OOF.Graphics_1.Layer.Select
checkpoint selection info updated
checkpoint OOF.Graphics_1.Layer.Hide
findCellRenderer(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), col=0, rend=0).emit('toggled', '10')
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint OOF.Graphics_1.Layer.Show
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((10,), column)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
findWidget('OOF2 Graphics Layer Editor:DisplayMethods:New').clicked()
checkpoint toplevel widget mapped Dialog-New Display Method for Skeleton skeleton
findWidget('Dialog-New Display Method for Skeleton skeleton').resize(253, 80)
assert tests.newMethodCheck("Skeleton", "skeleton", "Material Color")
findWidget('Dialog-New Display Method for Skeleton skeleton:gtk-ok').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint OOF.LayerEditor.LayerSet.Send
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Add_Method
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((15,))
checkpoint OOF.Graphics_1.Layer.Select
ls_0 = findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_model()
data_0 = [ls_0.get_value(ls_0.get_iter((15,)),i) for i in range(ls_0.get_n_columns())]
ls_0.insert(5, data_0)
ls_0.remove(ls_0.get_iter((16,)))
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint OOF.Graphics_1.Layer.Raise.By
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics Layer Editor:DisplayMethods:ListScroll:List').get_selection().select_path((0,))
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((11,))
checkpoint OOF.Graphics_1.Layer.Select
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((11,), column)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
assert tests.layerEditorListCheck("Element Edges", "Material Color")
assert tests.layerEditorSelectionCheck("Element Edges")
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((12,))
checkpoint OOF.Graphics_1.Layer.Select
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((12,), column)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
assert tests.layerEditorSelectionCheck("Element Edges")
assert tests.layerEditorListCheck("Element Edges")
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((11,))
checkpoint OOF.Graphics_1.Layer.Select
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((11,), column)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
assert tests.layerEditorSelectionCheck("Element Edges")
assert tests.layerEditorListCheck("Element Edges", "Material Color")
findWidget('OOF2 Graphics Layer Editor:DisplayMethods:Delete').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Delete_Method
assert tests.layerEditorListCheck("(invalid) <deleted>", "Material Color")
assert tests.layerEditorSelectionCheck()
findWidget('OOF2 Graphics Layer Editor:Send').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint OOF.LayerEditor.LayerSet.Send
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
assert tests.layerCheck("Graphics_1", "Bitmap", "Material Color", "Element Edges")
assert tests.selectedLayerCheck("Graphics_1", None)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((14,))
checkpoint OOF.Graphics_1.Layer.Select
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((14,), column)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
assert tests.layerEditorSelectionCheck("Material Color")
assert tests.layerEditorListCheck("Material Color")
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), 'File:Clone').activate()
checkpoint Graphics_2 Mesh Info sensitized
checkpoint toplevel widget mapped OOF2 Graphics 2
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
findWidget('OOF2 Graphics 2:Pane0:Pane1:Pane2').set_position(250)
findWidget('OOF2 Graphics 2:Pane0:Pane1').set_position(693)
findWidget('OOF2 Graphics 2:Pane0').set_position(278)
findWidget('OOF2 Graphics 2:Pane0:Pane1:Pane2').set_position(250)
findWidget('OOF2 Graphics 2:Pane0:Pane1').set_position(693)
findWidget('OOF2 Graphics 2:Pane0').set_position(278)
findWidget('OOF2 Graphics 2').resize(800, 400)
findWidget('OOF2 Graphics 2:Pane0:Pane1:Pane2').set_position(250)
findWidget('OOF2 Graphics 2:Pane0:Pane1').set_position(693)
findWidget('OOF2 Graphics 2:Pane0').set_position(278)
findWidget('OOF2 Graphics 2:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 2:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 2:Pane0').set_position(278)
checkpoint OOF.Graphics_1.File.Clone
assert tests.layerCheck("Graphics_2", "Bitmap", "Material Color", "Element Edges")
assert tests.selectedLayerCheck("Graphics_2", "Material Color")
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2').resize(800, 400)
findWidget('OOF2 Graphics 2:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 2:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 2:Pane0').set_position(277)
findWidget('OOF2 Graphics 2:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 2:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 2:Pane0').set_position(203)
findWidget('OOF2 Graphics 2:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 2:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 2:Pane0').set_position(203)
findWidget('OOF2 Graphics 2:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 2:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 2:Pane0').set_position(177)
findWidget('OOF2 Graphics 2:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 2:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 2:Pane0').set_position(175)
findWidget('OOF2 Graphics 2:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 2:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 2:Pane0:LayerScroll:LayerList').get_selection().select_path((10,))
checkpoint OOF.Graphics_2.Layer.Select
tree=findWidget('OOF2 Graphics 2:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((10,), column)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
assert tests.layerEditorListCheck("Element Edges")
assert tests.layerEditorSelectionCheck("Element Edges")
assert tests.layerEditorDestination("Graphics_2")
assert tests.layerEditorDestinationList("Graphics_1", "Graphics_2", "all")
assert tests.selectedLayerCheck("Graphics_2", "Element Edges")
findWidget('OOF2 Graphics Layer Editor:DisplayMethods:Edit').clicked()
checkpoint toplevel widget mapped Dialog-New Display Method for Skeleton skeleton
assert tests.newMethodCheck("Skeleton", "skeleton", "Element Edges")
assert tests.newElementEdgeWidthCheck(0)
findWidget('Dialog-New Display Method for Skeleton skeleton').resize(333, 200)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 1.5873015873016e-02)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.1746031746032e-02)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 6.3492063492063e-02)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.0158730158730e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.1746031746032e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.3333333333333e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.4920634920635e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.6507936507937e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.8095238095238e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.9682539682540e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 1.0416666666667e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 2.0833333333333e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 3.1250000000000e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 5.2083333333333e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 1.2500000000000e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 3.4375000000000e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 3.7500000000000e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 4.1666666666667e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 4.3750000000000e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 4.6875000000000e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 4.7916666666667e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 4.8958333333333e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 5.1041666666667e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:gtk-ok').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.Send
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Replace_Method
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
setComboBox(findWidget('OOF2 Graphics Layer Editor:Destination'), 'all')
findWidget('OOF2 Graphics Layer Editor:Send').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint OOF.LayerEditor.LayerSet.Send
checkpoint Graphics_1 Pixel Info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.LayerEditor.LayerSet.Send
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
assert tests.layerCheck("Graphics_1", "Bitmap", "Element Edges", "Element Edges")
assert tests.layerCheck("Graphics_2", "Bitmap", "Material Color", "Element Edges")
assert tests.selectedLayerCheck("Graphics_1", "Element Edges")
assert tests.selectedLayerCheck("Graphics_1", "Element Edges")
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics Layer Editor:DisplayMethods:Copy').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Copy_Method
assert tests.layerEditorSelectionCheck("Element Edges")
assert tests.layerEditorListCheck("Element Edges", "Element Edges")
tree=findWidget('OOF2 Graphics Layer Editor:DisplayMethods:ListScroll:List')
column = tree.get_column(0)
tree.row_activated((0,), column)
checkpoint toplevel widget mapped Dialog-New Display Method for Skeleton skeleton
assert tests.newMethodCheck("Skeleton", "skeleton", "Element Edges")
assert tests.newElementEdgeWidthCheck(5)
findWidget('Dialog-New Display Method for Skeleton skeleton').resize(333, 200)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 4.8958333333333e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 4.7916666666667e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 4.4791666666667e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 3.1250000000000e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 2.0833333333333e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 1.1458333333333e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 5.2083333333333e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:width:slider').get_adjustment().set_value( 0.0000000000000e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.8095238095238e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.6507936507937e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.0158730158730e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 2.2222222222222e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 0.0000000000000e+00)
setComboBox(findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Chooser'), 'RGBColor')
findWidget('Dialog-New Display Method for Skeleton skeleton').resize(342, 248)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 1.5873015873016e-02)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 4.7619047619048e-02)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 9.5238095238095e-02)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 1.9047619047619e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 2.8571428571429e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 3.6507936507937e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 4.9206349206349e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 6.1904761904762e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 8.0952380952381e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 8.2539682539683e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:RGBColor:Red:slider').get_adjustment().set_value( 8.4126984126984e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:gtk-ok').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint Graphics_1 Pixel Info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.LayerEditor.LayerSet.Send
checkpoint OOF.LayerEditor.LayerSet.Send
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Replace_Method
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
assert tests.layerCheck("Graphics_1", "Bitmap", "Element Edges", "Element Edges", "Element Edges")
assert tests.layerCheck("Graphics_2", "Bitmap", "Material Color", "Element Edges", "Element Edges")
assert tests.selectedLayerCheck("Graphics_1", "Element Edges")
assert tests.selectedLayerCheck("Graphics_2", "Element Edges")
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
setComboBox(findWidget('OOF2 Graphics Layer Editor:Destination'), 'Graphics_1')
setComboBox(findWidget('OOF2 Graphics Layer Editor:Destination'), 'Graphics_2')
findWidget('OOF2 Graphics Layer Editor:Send').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint OOF.LayerEditor.LayerSet.Send
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
assert tests.layerCheck("Graphics_2", "Bitmap", "Material Color", "Element Edges", "Element Edges")
assert tests.layerCheck("Graphics_1", "Bitmap", "Element Edges", "Element Edges", "Element Edges")
assert tests.selectedLayerCheck("Graphics_1", "Element Edges")
assert tests.selectedLayerCheck("Graphics_2", "Element Edges")
ls_1 = findWidget('OOF2 Graphics 2:Pane0:LayerScroll:LayerList').get_model()
data_1 = [ls_1.get_value(ls_1.get_iter((11,)),i) for i in range(ls_1.get_n_columns())]
ls_1.insert(10, data_1)
ls_1.remove(ls_1.get_iter((12,)))
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
checkpoint OOF.Graphics_2.Layer.Raise.By
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), 'Layer:Delete').activate()
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
checkpoint Graphics_1 Pixel Info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Layer.Delete
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((10,))
checkpoint OOF.Graphics_1.Layer.Select
ls_2 = findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_model()
data_2 = [ls_2.get_value(ls_2.get_iter((10,)),i) for i in range(ls_2.get_n_columns())]
ls_2.insert(12, data_2)
ls_2.remove(ls_2.get_iter((10,)))
checkpoint Graphics_1 Pixel Info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Layer.Lower.By
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((11,), column)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
assert tests.layerEditorListCheck("Element Edges")
assert tests.layerEditorSelectionCheck("Element Edges")
assert tests.layerCheck("Graphics_1", "Bitmap", "Element Edges", "Element Edges")
assert tests.selectedLayerCheck("Graphics_1", "Element Edges")
assert tests.selectedLayerCheck("Graphics_2", "Element Edges")
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((10,))
checkpoint OOF.Graphics_1.Layer.Select
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(2)
tree.row_activated((10,), column)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
assert tests.layerEditorListCheck("Element Edges")
assert tests.layerEditorSelectionCheck("Element Edges")
assert tests.layerEditorDestination("Graphics_1")
tree=findWidget('OOF2 Graphics 2:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((10,), column)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
assert tests.layerEditorSelectionCheck("Element Edges")
assert tests.layerEditorListCheck("Element Edges", "Element Edges")
assert tests.layerEditorSelectionWhichCheck(0)
assert tests.layerEditorDestination("Graphics_2")
findWidget('OOF2 Graphics 2:Pane0:LayerScroll:LayerList').get_selection().select_path((11,))
checkpoint OOF.Graphics_2.Layer.Select
tree=findWidget('OOF2 Graphics 2:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((11,), column)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
assert tests.layerEditorSelectionCheck("Element Edges")
assert tests.layerEditorListCheck("Element Edges", "Element Edges")
assert tests.layerEditorSelectionWhichCheck(1)
findWidget('OOF2 Graphics 2:Pane0:LayerScroll:LayerList').get_selection().select_path((15,))
checkpoint OOF.Graphics_2.Layer.Select
tree=findWidget('OOF2 Graphics 2:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((15,), column)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
assert tests.layerEditorListCheck("Material Color")
assert tests.layerEditorSelectionCheck("Material Color")
findWidget('OOF2 Graphics Layer Editor:DisplayMethods:Delete').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Delete_Method
assert tests.layerEditorListCheck("(invalid) <deleted>")
assert tests.sensitivityCheck3()
findWidget('OOF2 Graphics Layer Editor:Send').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint OOF.LayerEditor.LayerSet.Send
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 1:Pane0').set_position(192)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
assert tests.layerCheck("Graphics_2", "Bitmap", "Element Edges", "Element Edges")
assert tests.selectedLayerCheck("Graphics_1", "Element Edges")
assert tests.selectedLayerCheck("Graphics_2", None)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((11,))
checkpoint OOF.Graphics_1.Layer.Select
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((11,), column)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
assert tests.layerEditorListCheck("Element Edges")
assert tests.layerEditorSelectionCheck("Element Edges")
assert tests.layerEditorDestination("Graphics_1")
assert tests.sensitivityCheck2()
setComboBox(findWidget('OOF2 Graphics Layer Editor:Destination'), 'all')
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((10,))
checkpoint OOF.Graphics_1.Layer.Select
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((10,), column)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
assert tests.selectedLayerCheck("Graphics_1", "Element Edges")
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), 'File:Close').activate()
checkpoint OOF.Graphics_1.File.Close
assert tests.layerEditorDestination("Graphics_2")
tree=findWidget('OOF2 Graphics Layer Editor:DisplayMethods:ListScroll:List')
column = tree.get_column(0)
tree.row_activated((0,), column)
checkpoint toplevel widget mapped Dialog-New Display Method for Skeleton skeleton
findWidget('Dialog-New Display Method for Skeleton skeleton').resize(333, 200)
setComboBox(findWidget('Dialog-New Display Method for Skeleton skeleton:method:Chooser'), 'Selected Segments')
findWidget('Dialog-New Display Method for Skeleton skeleton').resize(371, 248)
assert tests.newMethodCheck("Skeleton", "skeleton", "Selected Segments")
findWidget('Dialog-New Display Method for Skeleton skeleton:gtk-ok').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.Send
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Replace_Method
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
assert tests.layerCheck("Graphics_2", "Bitmap", "Element Edges", "Element Edges", "Selected Segments")
assert tests.selectedLayerCheck("Graphics_2", "Selected Segments")
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 2:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_2')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 3.5756521739130e+01,y=-4.4510869565217e+01,state=0,window=findCanvasGdkWindow('Graphics_2')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 2:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_2')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 3.5756521739130e+01,y=-4.4510869565217e+01,state=256,window=findCanvasGdkWindow('Graphics_2')))
findWidget('OOF2 Graphics 2:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 2:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
setComboBox(findWidget('OOF2 Graphics 2:Pane0:Pane1:Pane2:TBChooser'), 'Skeleton Selection')
findWidget('OOF2 Graphics 2:Pane0:Pane1:Pane2').set_position(259)
checkpoint Graphics_2 Element sensitized
checkpoint Graphics_2 Element sensitized
findWidget('OOF2 Graphics 2:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 2:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 2:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findWidget('OOF2 Graphics 2:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Segment').clicked()
checkpoint Graphics_2 Segment sensitized
checkpoint Graphics_2 Element sensitized
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 2:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_2')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 3.5756521739130e+01,y=-4.4510869565217e+01,state=0,window=findCanvasGdkWindow('Graphics_2')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 2:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_2')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 3.5756521739130e+01,y=-4.4510869565217e+01,state=256,window=findCanvasGdkWindow('Graphics_2')))
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_2 Segment sensitized
checkpoint Graphics_2 Segment sensitized
checkpoint OOF.Graphics_2.Toolbox.Select_Segment.Single_Segment
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
tree=findWidget('OOF2 Graphics Layer Editor:DisplayMethods:ListScroll:List')
column = tree.get_column(0)
tree.row_activated((0,), column)
checkpoint toplevel widget mapped Dialog-New Display Method for Skeleton skeleton
findWidget('Dialog-New Display Method for Skeleton skeleton').resize(371, 248)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 2.3809523809524e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 2.6984126984127e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 3.3333333333333e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 3.9682539682540e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 7.3015873015873e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 7.4603174603175e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 7.6190476190476e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 7.7777777777778e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 7.9365079365079e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:gtk-ok').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint Graphics_2 Element sensitized
checkpoint Graphics_2 Segment sensitized
checkpoint OOF.LayerEditor.LayerSet.Send
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Replace_Method
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
assert tests.layerCheck("Graphics_2", "Bitmap", "Element Edges", "Element Edges", "Selected Segments")
assert tests.selectedLayerCheck("Graphics_2", "Selected Segments")
assert tests.layerEditorListCheck("Selected Segments")
findMenu(findWidget('OOF2 Graphics Layer Editor:MenuBar'), 'Settings:AutoSend').activate()
checkpoint OOF.LayerEditor.Settings.AutoSend
findWidget('OOF2 Graphics Layer Editor:DisplayMethods:Edit').clicked()
checkpoint toplevel widget mapped Dialog-New Display Method for Skeleton skeleton
findWidget('Dialog-New Display Method for Skeleton skeleton').resize(371, 248)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 7.7777777777778e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 7.6190476190476e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 7.4603174603175e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 6.5079365079365e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 6.3492063492063e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 5.7142857142857e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 5.0793650793651e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 4.2857142857143e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 3.8095238095238e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 3.3333333333333e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 2.2222222222222e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 1.5873015873016e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 6.3492063492063e-02)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Selected Segments:color:RGBColor:Blue:slider').get_adjustment().set_value( 0.0000000000000e+00)
findWidget('Dialog-New Display Method for Skeleton skeleton:gtk-ok').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Replace_Method
findWidget('OOF2 Graphics Layer Editor:Send').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint Graphics_2 Element sensitized
checkpoint Graphics_2 Segment sensitized
checkpoint OOF.LayerEditor.LayerSet.Send
findWidget('OOF2 Graphics 2:Pane0').set_position(176)
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(194, 72)
findWidget('Dialog-Python_Log:filename').set_text('l')
findWidget('Dialog-Python_Log:filename').set_text('la')
findWidget('Dialog-Python_Log:filename').set_text('lay')
findWidget('Dialog-Python_Log:filename').set_text('laye')
findWidget('Dialog-Python_Log:filename').set_text('layer')
findWidget('Dialog-Python_Log:filename').set_text('layert')
findWidget('Dialog-Python_Log:filename').set_text('layerte')
findWidget('Dialog-Python_Log:filename').set_text('layertes')
findWidget('Dialog-Python_Log:filename').set_text('layertest')
findWidget('Dialog-Python_Log:filename').set_text('layertest.')
findWidget('Dialog-Python_Log:filename').set_text('layertest.l')
findWidget('Dialog-Python_Log:filename').set_text('layertest.lo')
findWidget('Dialog-Python_Log:filename').set_text('layertest.log')
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('layertest.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
