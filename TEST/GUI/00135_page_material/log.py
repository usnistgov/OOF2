checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.20 $
# $Author: langer $
# $Date: 2010/12/27 07:24:49 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests
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
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Create_From_ImageFile
# checkpoint interface page updated
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(153)
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(249, 72)
checkpoint meshable button set
findWidget('Dialog-Create new pixel group:name:Auto').clicked()
checkpoint microstructure page sensitized
findWidget('Dialog-Create new pixel group:name:Text').set_text('g')
findWidget('Dialog-Create new pixel group:name:Text').set_text('gr')
checkpoint meshable button set
findWidget('Dialog-Create new pixel group:name:Text').set_text('gre')
findWidget('Dialog-Create new pixel group:name:Text').set_text('gree')
findWidget('Dialog-Create new pixel group:name:Text').set_text('green')
findWidget('Dialog-Create new pixel group:gtk-ok').clicked()
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint OOF.PixelGroup.New
checkpoint microstructure page sensitized
checkpoint meshable button set
findWidget('OOF2:Microstructure Page:Pane').set_position(197)
findMenu(findWidget('OOF2:MenuBar'), 'Windows:Graphics:New').activate()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(250)
checkpoint Move Node toolbox info updated
checkpoint toplevel widget mapped OOF2 Graphics 1
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(693)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
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
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), 'Pixel Selection')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Chooser'), 'Color')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 2.9673913043478e+01,y=-7.9239130434783e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 2.9673913043478e+01,y=-7.9239130434783e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Color
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.AddSelection
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), 'File:Close').activate()
checkpoint OOF.Graphics_1.File.Close
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
checkpoint Materials page updated
checkpoint page installed Materials
assert tests.sensitization2()
findWidget('OOF2').resize(684, 350)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(249, 72)
findWidget('Dialog-New material:name:Auto').clicked()
findWidget('Dialog-New material:name:Text').set_text('t')
findWidget('Dialog-New material:name:Text').set_text('te')
findWidget('Dialog-New material:name:Text').set_text('tes')
findWidget('Dialog-New material:name:Text').set_text('test')
findWidget('Dialog-New material:gtk-ok').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.Material.New
assert tests.sensitization3()
assert tests.materialListCheck('test')
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((0,))
checkpoint Materials page updated
checkpoint property selected
widget=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget.window))
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Color
findWidget('Dialog-Copy property Color').resize(282, 72)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('Dialog-Copy property Color:new_name:Auto').clicked()
findWidget('Dialog-Copy property Color:new_name:Text').set_text('g')
findWidget('Dialog-Copy property Color:new_name:Text').set_text('gr')
findWidget('Dialog-Copy property Color:new_name:Text').set_text('gre')
findWidget('Dialog-Copy property Color:new_name:Text').set_text('gree')
findWidget('Dialog-Copy property Color:new_name:Text').set_text('green')
findWidget('Dialog-Copy property Color:gtk-ok').clicked()
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((0,), open_all=False)
findWidget('OOF2:Materials Page:Pane').set_position(272)
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy
assert tests.propertyTreeCheck('Color:green')
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Color;green
findWidget('Dialog-Parametrize Color;green').resize(248, 144)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('Dialog-Parametrize Color;green:color:Gray:Gray:slider').get_adjustment().set_value( 1.5873015873016e-02)
findWidget('Dialog-Parametrize Color;green:color:Gray:Gray:slider').get_adjustment().set_value( 9.5238095238095e-02)
findWidget('Dialog-Parametrize Color;green:color:Gray:Gray:slider').get_adjustment().set_value( 1.1111111111111e-01)
findWidget('Dialog-Parametrize Color;green:color:Gray:Gray:slider').get_adjustment().set_value( 1.7460317460317e-01)
findWidget('Dialog-Parametrize Color;green:color:Gray:Gray:slider').get_adjustment().set_value( 2.5396825396825e-01)
findWidget('Dialog-Parametrize Color;green:color:Gray:Gray:slider').get_adjustment().set_value( 3.1746031746032e-01)
findWidget('Dialog-Parametrize Color;green:color:Gray:Gray:slider').get_adjustment().set_value( 3.6507936507937e-01)
findWidget('Dialog-Parametrize Color;green:color:Gray:Gray:slider').get_adjustment().set_value( 3.8095238095238e-01)
findWidget('Dialog-Parametrize Color;green:color:Gray:Gray:slider').get_adjustment().set_value( 4.1269841269841e-01)
findWidget('Dialog-Parametrize Color;green:gtk-ok').clicked()
checkpoint OOF.Property.Parametrize.Color.green
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane').set_position(272)
assert tests.materialPropertyListCheck('Color:green')
assert tests.sensitization4()
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((2,), open_all=False)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((2, 0), open_all=False)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((2, 0, 1), open_all=False)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.9012345679012e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.8024691358025e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.7037037037037e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1604938271605e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4506172839506e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7407407407407e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0308641975309e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.3209876543210e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.6111111111111e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.1913580246914e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.4814814814815e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.7716049382716e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.0617283950617e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((2, 0, 1, 0))
checkpoint Materials page updated
checkpoint property deselected
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.0000000000000e+01)
widget=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget.window))
widget=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget.window))
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated((2, 0, 1, 0), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic
findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic').resize(238, 140)
findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic:kappa:0,0').set_text('')
findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic:kappa:0,0').set_text('1')
findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic:kappa:0,0').set_text('12')
findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic:kappa:0,0').set_text('123')
widget=findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic:kappa:0,0')
widget.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget.window))
widget=findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic:kappa:0,0')
widget.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget.window))
findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic:gtk-ok').clicked()
checkpoint OOF.Property.Parametrize.Thermal.Conductivity.Anisotropic.Cubic
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
findWidget('OOF2:Materials Page:Pane').set_position(272)
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
assert tests.materialPropertyListCheck('Color:green', 'Thermal:Conductivity:Anisotropic:Cubic')
assert tests.sensitization5()
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll:PropertyList').get_selection().unselect_all()
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
assert tests.sensitization3()
findWidget('OOF2:Materials Page:Pane:Material:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Name for the new material.
findWidget('Dialog-Name for the new material.').resize(282, 72)
findWidget('Dialog-Name for the new material.:new_name:Auto').clicked()
findWidget('Dialog-Name for the new material.:new_name:Text').set_text('c')
findWidget('Dialog-Name for the new material.:new_name:Text').set_text('co')
findWidget('Dialog-Name for the new material.:new_name:Text').set_text('cop')
findWidget('Dialog-Name for the new material.:new_name:Text').set_text('copy')
findWidget('Dialog-Name for the new material.:gtk-ok').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.Material.Copy
assert tests.currentMaterialCheck('copy')
assert tests.materialListCheck('test', 'copy')
assert tests.currentPropertyCheck(None)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll:PropertyList').get_selection().select_path((1,))
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
assert tests.currentPropertyCheck('Thermal:Conductivity:Anisotropic:Cubic')
assert tests.sensitization5()
findWidget('OOF2:Materials Page:Pane:Material:RemoveProperty').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.Material.Remove_property
assert tests.materialPropertyListCheck('Color:green')
assert tests.propertyTreeCheck('Thermal:Conductivity:Anisotropic:Cubic')
assert tests.materialPropertyCheck(None)
setComboBox(findWidget('OOF2:Materials Page:Pane:Material:MaterialList'), 'test')
checkpoint Materials page updated
checkpoint Materials page updated
assert tests.currentPropertyCheck('Thermal:Conductivity:Anisotropic:Cubic')
assert tests.materialPropertyListCheck('Color:green', 'Thermal:Conductivity:Anisotropic:Cubic')
assert tests.currentMaterialCheck('test')
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.4814814814815e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.6111111111111e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.3209876543210e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4506172839506e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.7037037037037e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.9012345679012e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((0, 0))
checkpoint Materials page updated
checkpoint property deselected
checkpoint Materials page updated
checkpoint property selected
widget=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget.window))
assert tests.currentPropertyCheck('Color:green')
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(227, 94)
findWidget('Questioner:gtk-ok').clicked()
findWidget('OOF2:Materials Page:Pane').set_position(272)
checkpoint Materials page updated
checkpoint Materials page updated
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().unselect_all()
checkpoint Materials page updated
checkpoint property deselected
findWidget('OOF2:Materials Page:Pane').set_position(272)
checkpoint OOF.Property.Delete
checkpoint_count("Materials page updated")
assert tests.currentPropertyCheck(None)
assert tests.materialPropertyListCheck('Thermal:Conductivity:Anisotropic:Cubic')
findWidget('OOF2:Materials Page:Pane:Material:Rename').clicked()
checkpoint toplevel widget mapped Dialog-New name for the material.
findWidget('Dialog-New name for the material.').resize(249, 72)
findWidget('Dialog-New name for the material.:name:Auto').clicked()
findWidget('Dialog-New name for the material.:name:Text').set_text('m')
findWidget('Dialog-New name for the material.:name:Text').set_text('ma')
findWidget('Dialog-New name for the material.:name:Text').set_text('mat')
findWidget('Dialog-New name for the material.:name:Text').set_text('mate')
findWidget('Dialog-New name for the material.:name:Text').set_text('mater')
findWidget('Dialog-New name for the material.:name:Text').set_text('materi')
findWidget('Dialog-New name for the material.:name:Text').set_text('materia')
findWidget('Dialog-New name for the material.:name:Text').set_text('material')
findWidget('Dialog-New name for the material.:name:Text').set_text('material ')
findWidget('Dialog-New name for the material.:name:Text').set_text('material t')
findWidget('Dialog-New name for the material.:name:Text').set_text('material te')
findWidget('Dialog-New name for the material.:name:Text').set_text('material tes')
findWidget('Dialog-New name for the material.:name:Text').set_text('material test')
findWidget('Dialog-New name for the material.:name:Text').set_text('material tests')
findWidget('Dialog-New name for the material.:name:Text').set_text('material test')
findWidget('Dialog-New name for the material.:gtk-ok').clicked()
# checkpoint interface page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.Material.Rename
assert tests.currentMaterialCheck('material test')
assert tests.materialPropertyListCheck('Thermal:Conductivity:Anisotropic:Cubic')
assert tests.currentPropertyCheck(None)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(249, 72)
findWidget('Dialog-New material:name:Text').set_text('atest')
findWidget('Dialog-New material:name:Text').set_text('antest')
findWidget('Dialog-New material:name:Text').set_text('anotest')
findWidget('Dialog-New material:name:Text').set_text('anottest')
findWidget('Dialog-New material:name:Text').set_text('anothtest')
findWidget('Dialog-New material:name:Text').set_text('anothetest')
findWidget('Dialog-New material:name:Text').set_text('anothertest')
findWidget('Dialog-New material:name:Text').set_text('another test')
findWidget('Dialog-New material:gtk-ok').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.Material.New
assert tests.currentMaterialCheck('another test')
assert tests.materialPropertyListCheck()
assert tests.currentPropertyCheck(None)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((2, 0, 1, 0))
checkpoint Materials page updated
checkpoint property selected
widget=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget.window))
assert tests.propertyTreeCheck('Thermal:Conductivity:Anisotropic:Cubic')
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic
findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic').resize(238, 140)
findWidget('OOF2:Materials Page:Pane').set_position(272)
widget=findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic:kappa:0,0')
widget.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget.window))
findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic:gtk-ok').clicked()
checkpoint OOF.Property.Parametrize.Thermal.Conductivity.Anisotropic.Cubic
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic').resize(282, 72)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name:Text').set_text('')
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name:Text').set_text('c')
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name:Text').set_text('cu')
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name:Text').set_text('cub')
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name:Text').set_text('cubi')
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name:Text').set_text('cubic')
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name:Text').set_text('cubic ')
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name:Text').set_text('cubic c')
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name:Text').set_text('cubic co')
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name:Text').set_text('cubic cop')
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name:Text').set_text('cubic copy')
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:gtk-ok').clicked()
checkpoint OOF.Property.Copy
checkpoint toplevel widget mapped Error
findWidget('Error').resize(592, 166)
findWidget('Error:gtk-ok').clicked()
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic').resize(282, 72)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name:Text').set_text('cubiccopy')
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name:Text').set_text('cubic_copy')
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:gtk-ok').clicked()
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((2, 0, 1, 0), open_all=False)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.8024691358025e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7407407407407e+01)
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy
assert tests.propertyTreeCheck('Thermal:Conductivity:Anisotropic:Cubic:cubic_copy')
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.6111111111111e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.4814814814815e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.8024691358025e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 6.6728395061728e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 6.9629629629630e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.1234567901235e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.7037037037037e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.2839506172840e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.8641975308642e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0154320987654e+02)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane').set_position(272)
assert tests.currentPropertyCheck('Thermal:Conductivity:Anisotropic:Cubic:cubic_copy')
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material another test to pixels
findWidget('Dialog-Assign material another test to pixels').resize(240, 108)
findWidget('OOF2').resize(684, 350)
assert tests.chooserCheck('Dialog-Assign material another test to pixels:pixels', ['<selection>', '<every>', 'green'])
setComboBox(findWidget('Dialog-Assign material another test to pixels:pixels'), 'green')
findWidget('Dialog-Assign material another test to pixels:gtk-ok').clicked()
checkpoint OOF.Material.Assign
findWidget('OOF2').resize(684, 350)
findMenu(findWidget('OOF2:MenuBar'), 'Windows:Graphics:New').activate()
checkpoint Move Node toolbox info updated
checkpoint toplevel widget mapped OOF2 Graphics 1
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(250)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(693)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
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
findWidget('OOF2 Graphics 1').resize(800, 400)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), 'Pixel Info')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 5.2500000000000e+01,y=-6.5543478260870e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 5.2500000000000e+01,y=-6.5543478260870e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
#checkpoint updated pixel material info
assert tests.checkTBMaterial('another test')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.6212121212121e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 3.2424242424242e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 6.4848484848485e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.1348484848485e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.2969696969697e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.7833333333333e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 2.4318181818182e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 3.4045454545455e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 4.5393939393939e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 5.5121212121212e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 6.6469696969697e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 7.2954545454545e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 8.1060606060606e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 8.5924242424242e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.0213636363636e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.0537878787879e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.0700000000000e+02)
findWidget('OOF2:Materials Page:Pane:Material:RemoveMaterial').clicked()
checkpoint toplevel widget mapped Dialog-Remove the assigned material from pixels
findWidget('Dialog-Remove the assigned material from pixels').resize(240, 108)
setComboBox(findWidget('Dialog-Remove the assigned material from pixels:pixels'), '<every>')
setComboBox(findWidget('Dialog-Remove the assigned material from pixels:pixels'), 'green')
findWidget('Dialog-Remove the assigned material from pixels:gtk-ok').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Remove
assert tests.checkTBMaterial()
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 2.4456521739130e+01,y=-5.7717391304348e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 2.4456521739130e+01,y=-5.7717391304348e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
assert tests.checkTBMaterial()
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 6.6195652173913e+01,y=-1.2619565217391e+02,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 6.6195652173913e+01,y=-1.2619565217391e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
assert tests.checkTBMaterial()
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material another test to pixels
findWidget('Dialog-Assign material another test to pixels').resize(240, 108)
setComboBox(findWidget('Dialog-Assign material another test to pixels:pixels'), '<every>')
findWidget('Dialog-Assign material another test to pixels:gtk-ok').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Assign
assert tests.checkTBMaterial('another test')
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 1.0206521739130e+02,y=-1.1836956521739e+02,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 1.0206521739130e+02,y=-1.1836956521739e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
assert tests.checkTBMaterial('another test')
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 6.4239130434783e+01,y=-8.7065217391304e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 6.4239130434783e+01,y=-8.7065217391304e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
assert tests.checkTBMaterial('another test')
findWidget('OOF2:Materials Page:Pane:Material:RemoveMaterial').clicked()
checkpoint toplevel widget mapped Dialog-Remove the assigned material from pixels
findWidget('Dialog-Remove the assigned material from pixels').resize(240, 108)
setComboBox(findWidget('Dialog-Remove the assigned material from pixels:pixels'), 'green')
findWidget('Dialog-Remove the assigned material from pixels:gtk-ok').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Remove
assert tests.checkTBMaterial()
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 3.2934782608696e+01,y=-9.2934782608696e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 3.2934782608696e+01,y=-9.2934782608696e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
assert tests.checkTBMaterial()
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 1.0532608695652e+02,y=-1.3663043478261e+02,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 1.0532608695652e+02,y=-1.3663043478261e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
assert tests.checkTBMaterial('another test')
findWidget('OOF2:Materials Page:Pane:Material:Save').clicked()
checkpoint toplevel widget mapped Dialog-Save Material "another test"
findWidget('Dialog-Save Material "another test"').resize(194, 100)
findWidget('Dialog-Save Material "another test":filename').set_text('m')
findWidget('Dialog-Save Material "another test":filename').set_text('ma')
findWidget('Dialog-Save Material "another test":filename').set_text('mat')
findWidget('Dialog-Save Material "another test":filename').set_text('mate')
findWidget('Dialog-Save Material "another test":filename').set_text('mater')
findWidget('Dialog-Save Material "another test":filename').set_text('materi')
findWidget('Dialog-Save Material "another test":filename').set_text('materia')
findWidget('Dialog-Save Material "another test":filename').set_text('material')
findWidget('Dialog-Save Material "another test":filename').set_text('material.')
findWidget('Dialog-Save Material "another test":filename').set_text('material.d')
findWidget('Dialog-Save Material "another test":filename').set_text('material.da')
findWidget('Dialog-Save Material "another test":filename').set_text('material.dat')
findWidget('Dialog-Save Material "another test":gtk-ok').clicked()
checkpoint OOF.File.Save.Materials
assert tests.filediff('material.dat')
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(194, 94)
findWidget('Questioner:gtk-yes').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(150)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint pixel page updated
checkpoint active area status updated
checkpoint pixel page sensitized
checkpoint mesh bdy page updated
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
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint Field page sensitized
checkpoint microstructure page sensitized
checkpoint Solver page sensitized
checkpoint meshable button set
# checkpoint interface page updated
checkpoint OOF.Microstructure.Delete
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
checkpoint Materials page updated
checkpoint page installed Materials
assert tests.sensitization0()
findWidget('OOF2:Materials Page:Pane:Material:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(227, 94)
findWidget('Questioner:gtk-ok').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Delete
assert tests.chooserStateCheck('OOF2:Materials Page:Pane:Material:MaterialList', 'material test')
assert tests.propertyTreeCheck('Thermal:Conductivity:Anisotropic:Cubic:cubic_copy')
findWidget('OOF2:Materials Page:Pane:Material:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(227, 94)
findWidget('Questioner:gtk-ok').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Delete
assert tests.chooserCheck('OOF2:Materials Page:Pane:Material:MaterialList', ['copy'])
findWidget('OOF2:Materials Page:Pane:Material:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(227, 94)
findWidget('Questioner:gtk-ok').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Delete
assert tests.sensitization1()
assert tests.chooserCheck('OOF2:Materials Page:Pane:Material:MaterialList', [])
assert tests.checkTBMaterial("???")
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(194, 72)
findWidget('Dialog-Python_Log:filename').set_text('m')
findWidget('Dialog-Python_Log:filename').set_text('ma')
findWidget('Dialog-Python_Log:filename').set_text('mat')
findWidget('Dialog-Python_Log:filename').set_text('mate')
findWidget('Dialog-Python_Log:filename').set_text('mater')
findWidget('Dialog-Python_Log:filename').set_text('materi')
findWidget('Dialog-Python_Log:filename').set_text('materia')
findWidget('Dialog-Python_Log:filename').set_text('material')
findWidget('Dialog-Python_Log:filename').set_text('material.')
findWidget('Dialog-Python_Log:filename').set_text('material.l')
findWidget('Dialog-Python_Log:filename').set_text('material.lo')
findWidget('Dialog-Python_Log:filename').set_text('material.log')
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('material.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
checkpoint OOF.Graphics_1.File.Close
