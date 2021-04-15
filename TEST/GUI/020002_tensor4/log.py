# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Tests for anisotropic rank 4 tensor widgets, except for cubic.

import tests

checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 545)
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Materials Page:Pane').set_position(289)

# Create a new material
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(196, 122)
findWidget('Dialog-New material:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.New

# Open and parametrize Hexagonal elasticity
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Color')
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0, 1]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Hexagonal')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint HexagonalCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal').resize(528, 292)
widget_0=weakRef(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:0,0'))
if widget_0(): wevent(widget_0(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0().get_window())
checkpoint HexagonalCijklWidget updated
if widget_0(): wevent(widget_0(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0().get_window())
checkpoint HexagonalCijklWidget updated
assert tests.anisoCij("Hexagonal", c11=1.0, c12=0.5, c13=0.5, c22=1.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=0.25)
assert tests.sensitiveAnisoCij("Hexagonal", c11=1, c12=1, c13=1, c33=1, c44=1, c66=1)

# Change C_11
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:0,0').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:0,0').set_text('2')
if widget_0(): wevent(widget_0(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0().get_window())
checkpoint HexagonalCijklWidget updated
if widget_0(): wevent(widget_0(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0().get_window())
checkpoint HexagonalCijklWidget updated
assert tests.anisoCij("Hexagonal", c11=2.0, c12=0.5, c13=0.5, c22=2.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=0.75)

# Change C_12
if widget_0(): wevent(widget_0(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0().get_window())
checkpoint HexagonalCijklWidget updated

findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:0,1').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:0,1').set_text('3')
widget_5=weakRef(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:0,1'))
if widget_5(): wevent(widget_5(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_5().get_window())
checkpoint HexagonalCijklWidget updated
widget_6=weakRef(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:0,2'))
if widget_6(): wevent(widget_6(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_6().get_window())
checkpoint HexagonalCijklWidget updated
if widget_6(): wevent(widget_6(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_6().get_window())
checkpoint HexagonalCijklWidget updated
assert tests.anisoCij("Hexagonal", c11=2.0, c12=3.0, c13=0.5, c22=2.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=-0.5)

# Change C_13
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:0,2').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:0,2').set_text('4')
if widget_6(): wevent(widget_6(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_6().get_window())
checkpoint HexagonalCijklWidget updated
if widget_6(): wevent(widget_6(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_6().get_window())
checkpoint HexagonalCijklWidget updated
assert tests.anisoCij("Hexagonal", c11=2.0, c12=3.0, c13=4.0, c22=2.0, c23=4.0, c33=1.0, c44=0.25, c55=0.25, c66=-0.5)

# Change C_44
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:3,3').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:3,3').set_text('2')
widget_10=weakRef(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:3,3'))
if widget_10(): wevent(widget_10(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_10().get_window())
checkpoint HexagonalCijklWidget updated
widget_11=weakRef(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:5,5'))
if widget_11(): wevent(widget_11(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_11().get_window())
checkpoint HexagonalCijklWidget updated
if widget_11(): wevent(widget_11(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_11().get_window())
checkpoint HexagonalCijklWidget updated
assert tests.anisoCij("Hexagonal", c11=2.0, c12=3.0, c13=4.0, c22=2.0, c23=4.0, c33=1.0, c44=2.0 , c55=2.0, c66=-0.5)

# Change C_66
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:5,5').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:5,5').set_text('-')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:5,5').set_text('-1')
if widget_11(): wevent(widget_11(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_11().get_window())
checkpoint HexagonalCijklWidget updated
if widget_10(): wevent(widget_10(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_10().get_window())
checkpoint HexagonalCijklWidget updated
if widget_10(): wevent(widget_10(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_10().get_window())
checkpoint HexagonalCijklWidget updated
assert tests.anisoCij("Hexagonal", c11=2.0, c12=4.0, c13=4.0, c22=2.0, c23=4.0, c33=1.0, c44=2.0 , c55=2.0, c66=-1.0)

## TODO?: Convert the rest of this file to the new form that uses
## weakRef for all the widget_xx variables.  There are a lot of
## instances and not much to be gained from converting them.

# Add property to material
widget_16=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:3,3')
if widget_16: wevent(widget_16, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_16.get_window())
checkpoint HexagonalCijklWidget updated
del widget_16
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.Hexagonal
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open Tetragonal elasticity
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Tetragonal')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint TetragonalCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal').resize(528, 292)
widget_17=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,0')
if widget_17: wevent(widget_17, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_17.get_window())
checkpoint TetragonalCijklWidget updated
del widget_17
widget_18=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,0')
if widget_18: wevent(widget_18, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_18.get_window())
checkpoint TetragonalCijklWidget updated
del widget_18
assert tests.anisoCij("Tetragonal", c11=1.0, c12=0.5, c13=0.5, c22=1.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=0.25)
assert tests.sensitiveAnisoCij("Tetragonal", c11=1, c12=1, c13=1, c16=1, c33=1, c44=1, c66=1)

# Change C_11
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal').resize(528, 292)
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,0').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,0').set_text('2')
widget_19=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,0')
if widget_19: wevent(widget_19, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_19.get_window())
checkpoint TetragonalCijklWidget updated
del widget_19
widget_20=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,1')
if widget_20: wevent(widget_20, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_20.get_window())
checkpoint TetragonalCijklWidget updated
del widget_20
widget_21=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,1')
if widget_21: wevent(widget_21, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_21.get_window())
checkpoint TetragonalCijklWidget updated
del widget_21
assert tests.anisoCij("Tetragonal", c11=2.0, c12=0.5, c13=0.5, c22=2.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=0.25)

# Change C_12
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal').resize(528, 292)
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,1').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,1').set_text('3')
widget_22=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,1')
if widget_22: wevent(widget_22, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_22.get_window())
checkpoint TetragonalCijklWidget updated
del widget_22
widget_23=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,2')
if widget_23: wevent(widget_23, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_23.get_window())
checkpoint TetragonalCijklWidget updated
del widget_23
widget_24=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,2')
if widget_24: wevent(widget_24, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_24.get_window())
checkpoint TetragonalCijklWidget updated
del widget_24
assert tests.anisoCij("Tetragonal", c11=2.0, c12=3.0, c13=0.5, c22=2.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=0.25)

# Change C_13 
widget_2=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,0')
if widget_2: wevent(widget_2, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_2.get_window())
del widget_2
checkpoint TetragonalCijklWidget updated
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,2').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,2').set_text('4')
widget_3=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,2')
if widget_3: wevent(widget_3, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_3.get_window())
del widget_3
checkpoint TetragonalCijklWidget updated
widget_4=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,2')
if widget_4: wevent(widget_4, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_4.get_window())
del widget_4
checkpoint TetragonalCijklWidget updated

# Change C_16
widget_25=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,2')
if widget_25: wevent(widget_25, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_25.get_window())
checkpoint TetragonalCijklWidget updated
del widget_25
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,5').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,5').set_text('5')
widget_26=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,5')
if widget_26: wevent(widget_26, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_26.get_window())
checkpoint TetragonalCijklWidget updated
del widget_26
widget_27=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,2')
if widget_27: wevent(widget_27, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_27.get_window())
checkpoint TetragonalCijklWidget updated
del widget_27
widget_28=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,2')
if widget_28: wevent(widget_28, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_28.get_window())
checkpoint TetragonalCijklWidget updated
del widget_28
assert tests.anisoCij("Tetragonal", c11=2.0, c12=3.0, c13=4.0, c16=5.0, c22=2.0, c23=4.0, c26=-5.0, c33=1.0, c44=0.25, c55=0.25, c66=0.25)

# Change C_33
widget_29=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,2')
if widget_29: wevent(widget_29, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_29.get_window())
checkpoint TetragonalCijklWidget updated
del widget_29
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:2,2').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:2,2').set_text('6')
widget_30=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:2,2')
if widget_30: wevent(widget_30, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_30.get_window())
checkpoint TetragonalCijklWidget updated
del widget_30
widget_31=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:3,3')
if widget_31: wevent(widget_31, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_31.get_window())
checkpoint TetragonalCijklWidget updated
del widget_31
widget_32=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:3,3')
if widget_32: wevent(widget_32, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_32.get_window())
checkpoint TetragonalCijklWidget updated
del widget_32
assert tests.anisoCij("Tetragonal", c11=2.0, c12=3.0, c13=4.0, c16=5.0, c22=2.0, c23=4.0, c26=-5.0, c33=6.0, c44=0.25, c55=0.25, c66=0.25)

# Change C_44
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:3,3').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:3,3').set_text('7')
widget_33=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:3,3')
if widget_33: wevent(widget_33, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_33.get_window())
checkpoint TetragonalCijklWidget updated
del widget_33
widget_34=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:5,5')
if widget_34: wevent(widget_34, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_34.get_window())
checkpoint TetragonalCijklWidget updated
del widget_34
widget_35=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:5,5')
if widget_35: wevent(widget_35, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_35.get_window())
checkpoint TetragonalCijklWidget updated
del widget_35
assert tests.anisoCij("Tetragonal", c11=2.0, c12=3.0, c13=4.0, c16=5.0, c22=2.0, c23=4.0, c26=-5.0, c33=6.0, c44=7.0, c55=7.0, c66=0.25)

# Change C_66
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:5,5').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:5,5').set_text('8')
widget_36=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:5,5')
if widget_36: wevent(widget_36, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_36.get_window())
checkpoint TetragonalCijklWidget updated
del widget_36
widget_37=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:3,3')
if widget_37: wevent(widget_37, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_37.get_window())
checkpoint TetragonalCijklWidget updated
del widget_37
widget_38=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:3,3')
if widget_38: wevent(widget_38, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_38.get_window())
checkpoint TetragonalCijklWidget updated
del widget_38
assert tests.anisoCij("Tetragonal", c11=2.0, c12=3.0, c13=4.0, c16=5.0, c22=2.0, c23=4.0, c26=-5.0, c33=6.0, c44=7.0, c55=7.0, c66=8.0)

# Close Tetragonal dialog
widget_39=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:3,3')
if widget_39: wevent(widget_39, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_39.get_window())
checkpoint TetragonalCijklWidget updated
del widget_39
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.Tetragonal

# Add property to material
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open TrigonalA
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:TrigonalA')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint TrigonalACijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA').resize(528, 292)
widget_40=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,0')
if widget_40: wevent(widget_40, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_40.get_window())
checkpoint TrigonalACijklWidget updated
del widget_40
widget_41=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,0')
if widget_41: wevent(widget_41, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_41.get_window())
checkpoint TrigonalACijklWidget updated
del widget_41
assert tests.anisoCij("TrigonalA", c11=1.0, c12=0.5, c13=0.5, c22=1.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=0.25)
assert tests.sensitiveAnisoCij("TrigonalA", c11=1, c12=1, c13=1, c14=1, c15=1, c33=1, c44=1, c66=1)

# Change C_11
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,0').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,0').set_text('2')
widget_42=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,0')
if widget_42: wevent(widget_42, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_42.get_window())
checkpoint TrigonalACijklWidget updated
del widget_42
widget_43=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,1')
if widget_43: wevent(widget_43, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_43.get_window())
checkpoint TrigonalACijklWidget updated
del widget_43
widget_44=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,1')
if widget_44: wevent(widget_44, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_44.get_window())
checkpoint TrigonalACijklWidget updated
del widget_44
assert tests.anisoCij("TrigonalA", c11=2.0, c12=0.5, c13=0.5, c22=2.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=0.75)

# Change C_12
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,1').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,1').set_text('3')
widget_45=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,1')
if widget_45: wevent(widget_45, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_45.get_window())
checkpoint TrigonalACijklWidget updated
del widget_45
widget_46=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,2')
if widget_46: wevent(widget_46, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_46.get_window())
checkpoint TrigonalACijklWidget updated
del widget_46
widget_47=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,2')
if widget_47: wevent(widget_47, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_47.get_window())
checkpoint TrigonalACijklWidget updated
del widget_47
assert tests.anisoCij("TrigonalA", c11=2.0, c12=3.0, c13=0.5, c22=2.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=-0.5)

# Change C_13
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,2').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,2').set_text('4')
widget_48=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,2')
if widget_48: wevent(widget_48, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_48.get_window())
checkpoint TrigonalACijklWidget updated
del widget_48
widget_49=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,3')
if widget_49: wevent(widget_49, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_49.get_window())
checkpoint TrigonalACijklWidget updated
del widget_49
widget_50=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,3')
if widget_50: wevent(widget_50, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_50.get_window())
checkpoint TrigonalACijklWidget updated
del widget_50
assert tests.anisoCij("TrigonalA", c11=2.0, c12=3.0, c13=4.0, c22=2.0, c23=4.0, c33=1.0, c44=0.25, c55=0.25, c66=-0.5)

# Change C_14
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,3').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,3').set_text('5')
widget_51=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,3')
if widget_51: wevent(widget_51, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_51.get_window())
checkpoint TrigonalACijklWidget updated
del widget_51
widget_52=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,4')
if widget_52: wevent(widget_52, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_52.get_window())
checkpoint TrigonalACijklWidget updated
del widget_52
widget_53=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,4')
if widget_53: wevent(widget_53, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_53.get_window())
checkpoint TrigonalACijklWidget updated
del widget_53
assert tests.anisoCij("TrigonalA", c11=2.0, c12=3.0, c13=4.0, c14=5.0, c22=2.0, c23=4.0, c24=-5.0, c33=1.0, c44=0.25, c55=0.25, c56=5.0, c66=-0.5)

# Change C_15
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,4').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,4').set_text('6')
widget_54=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,4')
if widget_54: wevent(widget_54, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_54.get_window())
checkpoint TrigonalACijklWidget updated
del widget_54
widget_55=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:2,2')
if widget_55: wevent(widget_55, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_55.get_window())
checkpoint TrigonalACijklWidget updated
del widget_55
widget_56=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:2,2')
if widget_56: wevent(widget_56, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_56.get_window())
checkpoint TrigonalACijklWidget updated
del widget_56
assert tests.anisoCij("TrigonalA", c11=2.0, c12=3.0, c13=4.0, c14=5.0, c15=6.0, c22=2.0, c23=4.0, c24=-5.0, c25=-6.0, c33=1.0, c44=0.25, c46=-6.0, c55=0.25, c56=5.0, c66=-0.5)

# Change C_33
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:2,2').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:2,2').set_text('7')
widget_57=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:2,2')
if widget_57: wevent(widget_57, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_57.get_window())
checkpoint TrigonalACijklWidget updated
del widget_57
widget_58=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:3,3')
if widget_58: wevent(widget_58, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_58.get_window())
checkpoint TrigonalACijklWidget updated
del widget_58
widget_59=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:3,3')
if widget_59: wevent(widget_59, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_59.get_window())
checkpoint TrigonalACijklWidget updated
del widget_59
assert tests.anisoCij("TrigonalA", c11=2.0, c12=3.0, c13=4.0, c14=5.0, c15=6.0, c22=2.0, c23=4.0, c24=-5.0, c25=-6.0, c33=7.0, c44=0.25, c46=-6.0, c55=0.25, c56=5.0, c66=-0.5)

# Change C_44
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:3,3').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:3,3').set_text('8')
widget_60=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:3,3')
if widget_60: wevent(widget_60, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_60.get_window())
checkpoint TrigonalACijklWidget updated
del widget_60
widget_61=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:5,5')
if widget_61: wevent(widget_61, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_61.get_window())
checkpoint TrigonalACijklWidget updated
del widget_61
widget_62=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:5,5')
if widget_62: wevent(widget_62, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_62.get_window())
checkpoint TrigonalACijklWidget updated
del widget_62
assert tests.anisoCij("TrigonalA", c11=2.0, c12=3.0, c13=4.0, c14=5.0, c15=6.0, c22=2.0, c23=4.0, c24=-5.0, c25=-6.0, c33=7.0, c44=8.0, c46=-6.0, c55=8.0, c56=5.0, c66=-0.5)

# Change C_66
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:5,5').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:5,5').set_text('-')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:5,5').set_text('-1')
widget_63=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:5,5')
if widget_63: wevent(widget_63, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_63.get_window())
checkpoint TrigonalACijklWidget updated
del widget_63
widget_64=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:3,3')
if widget_64: wevent(widget_64, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_64.get_window())
checkpoint TrigonalACijklWidget updated
del widget_64
widget_65=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:3,3')
if widget_65: wevent(widget_65, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_65.get_window())
checkpoint TrigonalACijklWidget updated
del widget_65
widget_66=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:3,3')
if widget_66: wevent(widget_66, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_66.get_window())
checkpoint TrigonalACijklWidget updated
del widget_66
assert tests.anisoCij("TrigonalA", c11=2.0, c12=4.0, c13=4.0, c14=5.0, c15=6.0, c22=2.0, c23=4.0, c24=-5.0, c25=-6.0, c33=7.0, c44=8.0, c46=-6.0, c55=8.0, c56=5.0, c66=-1.0)

# Close and add property to material
widget_67=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:3,3')
if widget_67: wevent(widget_67, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_67.get_window())
checkpoint TrigonalACijklWidget updated
del widget_67
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.TrigonalA
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# TrigonalB
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:TrigonalB')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 4]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint TrigonalBCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB').resize(528, 292)
widget_68=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,0')
if widget_68: wevent(widget_68, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_68.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_68
widget_69=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,0')
if widget_69: wevent(widget_69, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_69.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_69
assert tests.anisoCij("TrigonalB", c11=1.0, c12=0.5, c13=0.5, c22=1.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=0.25)
assert tests.sensitiveAnisoCij("TrigonalB", c11=1, c12=1, c13=1, c14=1, c33=1, c44=1, c66=1)

# Change C_11
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,0').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,0').set_text('2')
widget_70=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,0')
if widget_70: wevent(widget_70, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_70.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_70
widget_71=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,1')
if widget_71: wevent(widget_71, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_71.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_71
widget_72=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,1')
if widget_72: wevent(widget_72, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_72.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_72
assert tests.anisoCij("TrigonalB", c11=2.0, c12=0.5, c13=0.5, c22=2.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=0.75)

# Change C_12
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,1').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,1').set_text('3')
widget_73=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,1')
if widget_73: wevent(widget_73, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_73.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_73
widget_74=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,1')
if widget_74: wevent(widget_74, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_74.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_74
assert tests.anisoCij("TrigonalB", c11=2.0, c12=3.0, c13=0.5, c22=2.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=-0.5)

# Change C_13
widget_75=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,1')
if widget_75: wevent(widget_75, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_75.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_75
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,2').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,2').set_text('4')
widget_76=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,2')
if widget_76: wevent(widget_76, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_76.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_76
widget_77=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,2')
if widget_77: wevent(widget_77, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_77.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_77
assert tests.anisoCij("TrigonalB", c11=2.0, c12=3.0, c13=4.0, c22=2.0, c23=4.0, c33=1.0, c44=0.25, c55=0.25, c66=-0.5)

# Change C_14
widget_78=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,2')
if widget_78: wevent(widget_78, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_78.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_78
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,3').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,3').set_text('5')
widget_79=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,3')
if widget_79: wevent(widget_79, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_79.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_79
widget_80=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,3')
if widget_80: wevent(widget_80, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_80.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_80
assert tests.anisoCij("TrigonalB", c11=2.0, c12=3.0, c13=4.0, c14=5.0, c22=2.0, c23=4.0, c24=-5.0, c33=1.0, c44=0.25, c55=0.25, c56=5.0, c66=-0.5)

# Change C_33
widget_81=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,3')
if widget_81: wevent(widget_81, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_81.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_81
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:2,2').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:2,2').set_text('6')
widget_82=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:2,2')
if widget_82: wevent(widget_82, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_82.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_82
widget_83=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:2,2')
if widget_83: wevent(widget_83, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_83.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_83
assert tests.anisoCij("TrigonalB", c11=2.0, c12=3.0, c13=4.0, c14=5.0, c22=2.0, c23=4.0, c24=-5.0, c33=6.0, c44=0.25, c55=0.25, c56=5.0, c66=-0.5)

# Change C_66
widget_84=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:2,2')
if widget_84: wevent(widget_84, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_84.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_84
widget_85=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:5,5')
if widget_85: wevent(widget_85, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_85.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_85
widget_86=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:5,5')
if widget_86: wevent(widget_86, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_86.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_86
# Change C_44  DELETE BACK TO PREV COMMENT
widget_87=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:5,5')
if widget_87: wevent(widget_87, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_87.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_87
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:3,3').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:3,3').set_text('7')
widget_88=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:3,3')
if widget_88: wevent(widget_88, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_88.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_88
widget_89=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:3,3')
if widget_89: wevent(widget_89, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_89.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_89
assert tests.anisoCij("TrigonalB", c11=2.0, c12=3.0, c13=4.0, c14=5.0, c22=2.0, c23=4.0, c24=-5.0, c33=6.0, c44=7.0, c55=7.0, c56=5.0, c66=-0.5)

# Change C_66
widget_90=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:3,3')
if widget_90: wevent(widget_90, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_90.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_90
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:5,5').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:5,5').set_text('8')
widget_91=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:5,5')
if widget_91: wevent(widget_91, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_91.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_91
widget_92=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:5,5')
if widget_92: wevent(widget_92, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_92.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_92
widget_93=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:5,5')
if widget_93: wevent(widget_93, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_93.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_93
assert tests.anisoCij("TrigonalB", c11=2.0, c12=-14.0, c13=4.0, c14=5.0, c22=2.0, c23=4.0, c24=-5.0, c33=6.0, c44=7.0, c55=7.0, c56=5.0, c66=8.0)

# Save and add to material
widget_94=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:5,5')
if widget_94: wevent(widget_94, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_94.get_window())
checkpoint TrigonalBCijklWidget updated
del widget_94
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.TrigonalB
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Orthorhombic
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0000000000000e+00)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Orthorhombic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 5]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint OrthorhombicCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic').resize(528, 292)
widget_95=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,0')
if widget_95: wevent(widget_95, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_95.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_95
widget_96=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,0')
if widget_96: wevent(widget_96, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_96.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_96
assert tests.anisoCij("Orthorhombic", c11=1.0, c12=0.5, c13=0.5, c22=1.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=0.25)
assert tests.sensitiveAnisoCij("Orthorhombic", c11=1, c12=1, c13=1, c22=1, c23=1, c33=1, c44=1, c55=1, c66=1)

# Change C_11
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,0').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,0').set_text('2')
widget_97=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,0')
if widget_97: wevent(widget_97, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_97.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_97
widget_98=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,0')
if widget_98: wevent(widget_98, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_98.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_98
assert tests.anisoCij("Orthorhombic", c11=2.0, c12=0.5, c13=0.5, c22=1.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=0.25)

# Change C_12
widget_99=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,0')
if widget_99: wevent(widget_99, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_99.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_99
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,1').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,1').set_text('3')
widget_100=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,1')
if widget_100: wevent(widget_100, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_100.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_100
widget_101=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,1')
if widget_101: wevent(widget_101, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_101.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_101

# Change C_13
widget_102=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,1')
if widget_102: wevent(widget_102, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_102.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_102
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,2').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,2').set_text('4')
widget_103=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,2')
if widget_103: wevent(widget_103, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_103.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_103
widget_104=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,2')
if widget_104: wevent(widget_104, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_104.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_104
assert tests.anisoCij("Orthorhombic", c11=2.0, c12=3.0, c13=4.0, c22=1.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=0.25)

# Change C_22
widget_105=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,2')
if widget_105: wevent(widget_105, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_105.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_105
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:1,1').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:1,1').set_text('5')
widget_106=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:1,1')
if widget_106: wevent(widget_106, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_106.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_106
widget_107=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:1,1')
if widget_107: wevent(widget_107, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_107.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_107
widget_108=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:1,1')
if widget_108: wevent(widget_108, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_108.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_108
assert tests.anisoCij("Orthorhombic", c11=2.0, c12=3.0, c13=4.0, c22=5.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=0.25)

# Change C_23
widget_109=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:1,1')
if widget_109: wevent(widget_109, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_109.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_109
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:1,2').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:1,2').set_text('6')
widget_110=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:1,2')
if widget_110: wevent(widget_110, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_110.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_110
widget_111=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:1,2')
if widget_111: wevent(widget_111, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_111.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_111
assert tests.anisoCij("Orthorhombic", c11=2.0, c12=3.0, c13=4.0, c22=5.0, c23=6.0, c33=1.0, c44=0.25, c55=0.25, c66=0.25)

# Change C_33
widget_112=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:1,2')
if widget_112: wevent(widget_112, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_112.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_112
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:2,2').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:2,2').set_text('7')
widget_113=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:2,2')
if widget_113: wevent(widget_113, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_113.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_113
widget_114=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:2,2')
if widget_114: wevent(widget_114, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_114.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_114
assert tests.anisoCij("Orthorhombic", c11=2.0, c12=3.0, c13=4.0, c22=5.0, c23=6.0, c33=7.0, c44=0.25, c55=0.25, c66=0.25)

# Change C_44
widget_115=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:2,2')
if widget_115: wevent(widget_115, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_115.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_115
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:3,3').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:3,3').set_text('8')
widget_116=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:3,3')
if widget_116: wevent(widget_116, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_116.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_116
widget_117=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:3,3')
if widget_117: wevent(widget_117, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_117.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_117
assert tests.anisoCij("Orthorhombic", c11=2.0, c12=3.0, c13=4.0, c22=5.0, c23=6.0, c33=7.0, c44=8.0, c55=0.25, c66=0.25)

# Change C_55
widget_118=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:3,3')
if widget_118: wevent(widget_118, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_118.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_118
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:4,4').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:4,4').set_text('9')
widget_119=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:4,4')
if widget_119: wevent(widget_119, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_119.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_119
widget_120=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:4,4')
if widget_120: wevent(widget_120, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_120.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_120
assert tests.anisoCij("Orthorhombic", c11=2.0, c12=3.0, c13=4.0, c22=5.0, c23=6.0, c33=7.0, c44=8.0, c55=9.0, c66=0.25)

# Change C_66
widget_121=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:4,4')
if widget_121: wevent(widget_121, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_121.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_121
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:5,5').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:5,5').set_text('1')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:5,5').set_text('10')
widget_122=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:5,5')
if widget_122: wevent(widget_122, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_122.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_122
widget_123=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:5,5')
if widget_123: wevent(widget_123, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_123.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_123
assert tests.anisoCij("Orthorhombic", c11=2.0, c12=3.0, c13=4.0, c22=5.0, c23=6.0, c33=7.0, c44=8.0, c55=9.0, c66=10.0)

# Save and add to material
widget_124=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:5,5')
if widget_124: wevent(widget_124, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_124.get_window())
checkpoint OrthorhombicCijklWidget updated
del widget_124
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.Orthorhombic
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Monoclinic
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Monoclinic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 6]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint MonoclinicCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic').resize(528, 292)
widget_125=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,0')
if widget_125: wevent(widget_125, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_125.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_125
widget_126=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,0')
if widget_126: wevent(widget_126, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_126.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_126
assert tests.anisoCij("Monoclinic", c11=1.0, c12=0.5, c13=0.5, c22=1.0, c23=0.5, c33=0.25, c44=0.25, c55=0.25, c66=0.25)
assert tests.sensitiveAnisoCij("Monoclinic", c11=1, c12=1, c13=1, c15=1, c22=1, c23=1, c25=1, c33=1, c35=1, c44=1, c46=1, c55=1, c66=1)

# Change C_00
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,0').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,0').set_text('2')
widget_127=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,0')
if widget_127: wevent(widget_127, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_127.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_127
widget_128=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,0')
if widget_128: wevent(widget_128, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_128.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_128
assert tests.anisoCij("Monoclinic", c11=2.0, c12=0.5, c13=0.5, c22=1.0, c23=0.5, c33=0.25, c44=0.25, c55=0.25, c66=0.25)

# Change C_12
widget_129=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,0')
if widget_129: wevent(widget_129, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_129.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_129
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,1').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,1').set_text('3')
widget_130=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,1')
if widget_130: wevent(widget_130, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_130.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_130
widget_131=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,1')
if widget_131: wevent(widget_131, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_131.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_131
assert tests.anisoCij("Monoclinic", c11=2.0, c12=3.0, c13=0.5, c22=1.0, c23=0.5, c33=0.25, c44=0.25, c55=0.25, c66=0.25)

# Change C_13
widget_132=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,1')
if widget_132: wevent(widget_132, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_132.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_132
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,2').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,2').set_text('4')
widget_133=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,2')
if widget_133: wevent(widget_133, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_133.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_133
widget_134=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,2')
if widget_134: wevent(widget_134, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_134.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_134
assert tests.anisoCij("Monoclinic", c11=2.0, c12=3.0, c13=4.0, c22=1.0, c23=0.5, c33=0.25, c44=0.25, c55=0.25, c66=0.25)

# Change C_15
widget_135=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,2')
if widget_135: wevent(widget_135, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_135.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_135
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,4').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,4').set_text('5')
widget_136=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,4')
if widget_136: wevent(widget_136, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_136.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_136
widget_137=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,4')
if widget_137: wevent(widget_137, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_137.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_137
assert tests.anisoCij("Monoclinic", c11=2.0, c12=3.0, c13=4.0, c15=5.0, c22=1.0, c23=0.5, c33=0.25, c44=0.25, c55=0.25, c66=0.25)

# Change C_22
widget_138=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,4')
if widget_138: wevent(widget_138, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_138.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_138
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:1,1').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:1,1').set_text('6')
widget_139=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:1,1')
if widget_139: wevent(widget_139, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_139.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_139
widget_140=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:1,1')
if widget_140: wevent(widget_140, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_140.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_140
assert tests.anisoCij("Monoclinic", c11=2.0, c12=3.0, c13=4.0, c15=5.0, c22=6.0, c23=0.5, c33=0.25, c44=0.25, c55=0.25, c66=0.25)

# Change C_23
widget_141=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:1,1')
if widget_141: wevent(widget_141, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_141.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_141
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:1,2').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:1,2').set_text('7')
widget_142=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:1,2')
if widget_142: wevent(widget_142, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_142.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_142
widget_143=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:1,2')
if widget_143: wevent(widget_143, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_143.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_143
assert tests.anisoCij("Monoclinic", c11=2.0, c12=3.0, c13=4.0, c15=5.0, c22=6.0, c23=7.0, c33=0.25, c44=0.25, c55=0.25, c66=0.25)

# Change C_25
widget_144=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:1,2')
if widget_144: wevent(widget_144, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_144.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_144
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:1,4').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:1,4').set_text('8')
widget_145=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:1,4')
if widget_145: wevent(widget_145, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_145.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_145
widget_146=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:1,4')
if widget_146: wevent(widget_146, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_146.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_146
assert tests.anisoCij("Monoclinic", c11=2.0, c12=3.0, c13=4.0, c15=5.0, c22=6.0, c23=7.0, c25=8.0, c33=0.25, c44=0.25, c55=0.25, c66=0.25)

# Change C_33
widget_147=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:1,4')
if widget_147: wevent(widget_147, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_147.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_147
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:2,2').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:2,2').set_text('9')
widget_148=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:2,2')
if widget_148: wevent(widget_148, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_148.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_148
widget_149=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:2,2')
if widget_149: wevent(widget_149, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_149.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_149
#
assert tests.anisoCij("Monoclinic", c11=2.0, c12=3.0, c13=4.0, c15=5.0, c22=6.0, c23=7.0, c25=8.0, c33=9.0, c44=0.25, c55=0.25, c66=0.25)

# Change C_35
widget_150=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:2,2')
if widget_150: wevent(widget_150, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_150.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_150
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:2,4').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:2,4').set_text('1')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:2,4').set_text('10')
widget_151=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:2,4')
if widget_151: wevent(widget_151, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_151.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_151
widget_152=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:2,4')
if widget_152: wevent(widget_152, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_152.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_152
assert tests.anisoCij("Monoclinic", c11=2.0, c12=3.0, c13=4.0, c15=5.0, c22=6.0, c23=7.0, c25=8.0, c33=9.0, c35=10, c44=0.25, c55=0.25, c66=0.25)

# Change C_44
widget_153=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:2,4')
if widget_153: wevent(widget_153, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_153.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_153
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:3,3').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:3,3').set_text('1')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:3,3').set_text('11')
widget_154=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:3,3')
if widget_154: wevent(widget_154, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_154.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_154
widget_155=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:3,3')
if widget_155: wevent(widget_155, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_155.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_155
assert tests.anisoCij("Monoclinic", c11=2.0, c12=3.0, c13=4.0, c15=5.0, c22=6.0, c23=7.0, c25=8.0, c33=9.0, c35=10, c44=11.0, c55=0.25, c66=0.25)

# Change C_46
widget_156=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:3,3')
if widget_156: wevent(widget_156, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_156.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_156
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:3,5').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:3,5').set_text('1')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:3,5').set_text('12')
widget_157=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:3,5')
if widget_157: wevent(widget_157, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_157.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_157
widget_158=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:3,5')
if widget_158: wevent(widget_158, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_158.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_158
assert tests.anisoCij("Monoclinic", c11=2.0, c12=3.0, c13=4.0, c15=5.0, c22=6.0, c23=7.0, c25=8.0, c33=9.0, c35=10, c44=11.0, c46=12.0, c55=0.25, c66=0.25)

# Change C_55
widget_159=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:3,5')
if widget_159: wevent(widget_159, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_159.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_159
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:4,4').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:4,4').set_text('1')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:4,4').set_text('13')
widget_160=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:4,4')
if widget_160: wevent(widget_160, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_160.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_160
widget_161=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:4,4')
if widget_161: wevent(widget_161, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_161.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_161
assert tests.anisoCij("Monoclinic", c11=2.0, c12=3.0, c13=4.0, c15=5.0, c22=6.0, c23=7.0, c25=8.0, c33=9.0, c35=10, c44=11.0, c46=12.0, c55=13.0, c66=0.25)

# Change C_66
widget_162=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:4,4')
if widget_162: wevent(widget_162, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_162.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_162
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:5,5').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:5,5').set_text('1')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:5,5').set_text('14')
widget_163=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:5,5')
if widget_163: wevent(widget_163, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_163.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_163
widget_164=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:5,5')
if widget_164: wevent(widget_164, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_164.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_164
#
assert tests.anisoCij("Monoclinic", c11=2.0, c12=3.0, c13=4.0, c15=5.0, c22=6.0, c23=7.0, c25=8.0, c33=9.0, c35=10, c44=11.0, c46=12.0, c55=13.0, c66=14.0)

# Save and add to material
widget_165=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:5,5')
if widget_165: wevent(widget_165, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_165.get_window())
checkpoint MonoclinicCijklWidget updated
del widget_165
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.Monoclinic
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Triclinic
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Triclinic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 7]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint TriclinicCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic').resize(528, 292)
widget_166=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:0,0')
if widget_166: wevent(widget_166, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_166.get_window())
checkpoint TriclinicCijklWidget updated
del widget_166
widget_167=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:0,0')
if widget_167: wevent(widget_167, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_167.get_window())
checkpoint TriclinicCijklWidget updated
del widget_167
assert tests.anisoCij("Triclinic", c11=1.0, c12=0.5, c13=0.5, c22=1.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=0.25)
assert tests.sensitiveAnisoCij("Triclinic", c11=1, c12=1, c13=1, c14=1, c15=1, c16=1, c22=1, c23=1, c24=1, c25=1, c26=1, c33=1, c34=1, c35=1, c36=1, c44=1, c45=1, c46=1, c55=1, c56=1, c66=1)

# Change C_16
widget_168=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:0,0')
if widget_168: wevent(widget_168, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_168.get_window())
checkpoint TriclinicCijklWidget updated
del widget_168
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:0,5').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:0,5').set_text('1')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:0,5').set_text('12')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:0,5').set_text('123')
widget_169=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:0,5')
if widget_169: wevent(widget_169, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_169.get_window())
checkpoint TriclinicCijklWidget updated
del widget_169
widget_170=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:0,5')
if widget_170: wevent(widget_170, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_170.get_window())
checkpoint TriclinicCijklWidget updated
del widget_170
assert tests.anisoCij("Triclinic", c11=1.0, c12=0.5, c13=0.5, c16=123., c22=1.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=0.25)

# Change C_25
widget_171=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:0,5')
if widget_171: wevent(widget_171, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_171.get_window())
checkpoint TriclinicCijklWidget updated
del widget_171
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:1,4').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:1,4').set_text('3')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:1,4').set_text('34')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:1,4').set_text('3')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:1,4').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:1,4').set_text('4')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:1,4').set_text('45')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:1,4').set_text('456')
widget_172=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:1,4')
if widget_172: wevent(widget_172, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_172.get_window())
checkpoint TriclinicCijklWidget updated
del widget_172

# Change C_34
widget_1=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:0,0')
if widget_1: wevent(widget_1, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_1.get_window())
del widget_1
checkpoint TriclinicCijklWidget updated
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:2,3').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:2,3').set_text('7')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:2,3').set_text('78')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:2,3').set_text('789')
widget_2=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:2,3')
if widget_2: wevent(widget_2, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_2.get_window())
del widget_2
checkpoint TriclinicCijklWidget updated
widget_3=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:2,3')
if widget_3: wevent(widget_3, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_3.get_window())
del widget_3
checkpoint TriclinicCijklWidget updated
assert tests.anisoCij("Triclinic", c11=1.0, c12=0.5, c13=0.5, c16=123., c22=1.0, c23=0.5, c25=456., c33=1.0, c34=789., c44=0.25, c55=0.25, c66=0.25)

# Save and add to material
widget_4=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:2,3')
if widget_4: wevent(widget_4, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_4.get_window())
del widget_4
checkpoint TriclinicCijklWidget updated
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.Triclinic
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
# Save material to a file
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Save', 'Materials']).activate()
checkpoint toplevel widget mapped Dialog-Materials
findWidget('Dialog-Materials').resize(192, 227)
findWidget('Dialog-Materials:filename').set_text('a')
findWidget('Dialog-Materials:filename').set_text('an')
findWidget('Dialog-Materials:filename').set_text('ani')
findWidget('Dialog-Materials:filename').set_text('anis')
findWidget('Dialog-Materials:filename').set_text('aniso')
findWidget('Dialog-Materials:filename').set_text('aniso.')
findWidget('Dialog-Materials:filename').set_text('aniso.d')
findWidget('Dialog-Materials:filename').set_text('aniso.da')
findWidget('Dialog-Materials:filename').set_text('aniso.dat')
findWidget('Dialog-Materials:materials').get_selection().unselect_all()
findWidget('Dialog-Materials:materials').get_selection().select_path(Gtk.TreePath([0]))
findWidget('Dialog-Materials:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Save.Materials

# Delete the material
findWidget('OOF2:Materials Page:Pane:Material:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(192, 86)
findWidget('Questioner:OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.Delete

# Before reloading the Material, change one entry in each Cij so that
# we can tell that reading the Material resets them.
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 6.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.0000000000000e+00)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Hexagonal')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint HexagonalCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal').resize(528, 292)
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:0,0').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:0,0').set_text('5')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:0,0').set_text('55')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:0,0').set_text('555')
widget_0=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:0,0')
if widget_0: wevent(widget_0, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0.get_window())
del widget_0
checkpoint HexagonalCijklWidget updated
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.Hexagonal
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Tetragonal')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 2]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint TetragonalCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal').resize(528, 292)
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,0').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,0').set_text('5')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,0').set_text('55')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,0').set_text('555')
widget_1=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,0')
if widget_1: wevent(widget_1, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_1.get_window())
del widget_1
checkpoint TetragonalCijklWidget updated
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.Tetragonal
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:TrigonalA')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 3]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint TrigonalACijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA').resize(528, 292)
widget_2=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,0')
if widget_2: wevent(widget_2, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_2.get_window())
del widget_2
checkpoint TrigonalACijklWidget updated
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,0').set_text('1.05')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,0').set_text('1.055')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,0').set_text('1.0555')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,0').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,0').set_text('5')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,0').set_text('55')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,0').set_text('555')
widget_3=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,0')
if widget_3: wevent(widget_3, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_3.get_window())
del widget_3
checkpoint TrigonalACijklWidget updated
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.TrigonalA
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:TrigonalB')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 4]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint TrigonalBCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB').resize(528, 292)
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,0').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,0').set_text('5')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,0').set_text('55')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,0').set_text('555')
widget_4=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,0')
if widget_4: wevent(widget_4, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_4.get_window())
del widget_4
checkpoint TrigonalBCijklWidget updated
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.TrigonalB
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Orthorhombic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 5]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint OrthorhombicCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic').resize(528, 292)
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,0').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,0').set_text('5')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,0').set_text('55')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,0').set_text('555')
widget_5=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,0')
if widget_5: wevent(widget_5, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_5.get_window())
del widget_5
checkpoint OrthorhombicCijklWidget updated
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.Orthorhombic
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Monoclinic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 6]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint MonoclinicCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic').resize(528, 292)
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,0').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,0').set_text('5')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,0').set_text('55')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,0').set_text('555')
widget_6=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,0')
if widget_6: wevent(widget_6, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_6.get_window())
del widget_6
checkpoint MonoclinicCijklWidget updated
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.Monoclinic
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Triclinic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 7]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint TriclinicCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic').resize(528, 292)
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:0,0').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:0,0').set_text('5')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:0,0').set_text('55')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:0,0').set_text('555')
widget_7=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:0,0')
if widget_7: wevent(widget_7, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_7.get_window())
del widget_7
checkpoint TriclinicCijklWidget updated
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.Triclinic

# Load the Material
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Load', 'Data']).activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(192, 92)
findWidget('Dialog-Data:filename').set_text('a')
findWidget('Dialog-Data:filename').set_text('an')
findWidget('Dialog-Data:filename').set_text('ani')
findWidget('Dialog-Data:filename').set_text('anis')
findWidget('Dialog-Data:filename').set_text('aniso')
findWidget('Dialog-Data:filename').set_text('aniso.')
findWidget('Dialog-Data:filename').set_text('aniso.d')
findWidget('Dialog-Data:filename').set_text('aniso.da')
findWidget('Dialog-Data:filename').set_text('aniso.dat')
findWidget('Dialog-Data:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.File.Load.Data
# Open hexagonal elasticity
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Hexagonal')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint HexagonalCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal').resize(528, 292)
widget_5=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:0,0')
if widget_5: wevent(widget_5, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_5.get_window())
del widget_5
checkpoint HexagonalCijklWidget updated
widget_6=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:0,0')
if widget_6: wevent(widget_6, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_6.get_window())
del widget_6
checkpoint HexagonalCijklWidget updated
assert tests.anisoCij("Hexagonal", c11=2.0, c12=4.0, c13=4.0, c22=2.0, c23=4.0, c33=1.0, c44=2.0 , c55=2.0, c66=-1.0)
widget_7=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:0,0')
if widget_7: wevent(widget_7, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_7.get_window())
del widget_7
checkpoint HexagonalCijklWidget updated
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Hexagonal:widget_GTK_RESPONSE_CANCEL').clicked()
# Open and check Tetragonal
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Tetragonal')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 2]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint TetragonalCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal').resize(528, 292)
widget_8=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,0')
if widget_8: wevent(widget_8, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_8.get_window())
del widget_8
checkpoint TetragonalCijklWidget updated
widget_9=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,0')
if widget_9: wevent(widget_9, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_9.get_window())
del widget_9
checkpoint TetragonalCijklWidget updated
assert tests.anisoCij("Tetragonal", c11=2.0, c12=3.0, c13=4.0, c16=5.0, c22=2.0, c23=4.0, c26=-5.0, c33=6.0, c44=7.0, c55=7.0, c66=8.0)

widget_10=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:0,0')
if widget_10: wevent(widget_10, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_10.get_window())
del widget_10
checkpoint TetragonalCijklWidget updated
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Tetragonal:widget_GTK_RESPONSE_CANCEL').clicked()
# Open and check TrigonalA
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:TrigonalA')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 3]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint TrigonalACijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA').resize(528, 292)
widget_11=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,0')
if widget_11: wevent(widget_11, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_11.get_window())
del widget_11
checkpoint TrigonalACijklWidget updated
widget_12=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,0')
if widget_12: wevent(widget_12, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_12.get_window())
del widget_12
checkpoint TrigonalACijklWidget updated
widget_13=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,0')
if widget_13: wevent(widget_13, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_13.get_window())
del widget_13
checkpoint TrigonalACijklWidget updated
assert tests.anisoCij("TrigonalA", c11=2.0, c12=4.0, c13=4.0, c14=5.0, c15=6.0, c22=2.0, c23=4.0, c24=-5.0, c25=-6.0, c33=7.0, c44=8.0, c46=-6.0, c55=8.0, c56=5.0, c66=-1.0)

widget_14=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:0,0')
if widget_14: wevent(widget_14, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_14.get_window())
del widget_14
checkpoint TrigonalACijklWidget updated
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalA:widget_GTK_RESPONSE_CANCEL').clicked()
# Open and check TrigonalB
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:TrigonalB')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 4]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint TrigonalBCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB').resize(528, 292)
widget_15=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,0')
if widget_15: wevent(widget_15, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_15.get_window())
del widget_15
checkpoint TrigonalBCijklWidget updated
assert tests.anisoCij("TrigonalB", c11=2.0, c12=-14.0, c13=4.0, c14=5.0, c22=2.0, c23=4.0, c24=-5.0, c33=6.0, c44=7.0, c55=7.0, c56=5.0, c66=8.0)

widget_16=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:0,0')
if widget_16: wevent(widget_16, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_16.get_window())
del widget_16
checkpoint TrigonalBCijklWidget updated
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;TrigonalB:widget_GTK_RESPONSE_CANCEL').clicked()
# Open and check Orthorhombic
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Orthorhombic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 5]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint OrthorhombicCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic').resize(528, 292)
widget_17=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,0')
if widget_17: wevent(widget_17, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_17.get_window())
del widget_17
checkpoint OrthorhombicCijklWidget updated
widget_18=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,0')
if widget_18: wevent(widget_18, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_18.get_window())
del widget_18
checkpoint OrthorhombicCijklWidget updated
assert tests.anisoCij("Orthorhombic", c11=2.0, c12=3.0, c13=4.0, c22=5.0, c23=6.0, c33=7.0, c44=8.0, c55=9.0, c66=10.0)

widget_19=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:0,0')
if widget_19: wevent(widget_19, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_19.get_window())
del widget_19
checkpoint OrthorhombicCijklWidget updated
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Orthorhombic:widget_GTK_RESPONSE_CANCEL').clicked()
# Open and check Monoclinic
findWidget('OOF2').resize(782, 545)
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Monoclinic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint MonoclinicCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic').resize(528, 292)
widget_20=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,0')
if widget_20: wevent(widget_20, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_20.get_window())
del widget_20
checkpoint MonoclinicCijklWidget updated
widget_21=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,0')
if widget_21: wevent(widget_21, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_21.get_window())
del widget_21
checkpoint MonoclinicCijklWidget updated
assert tests.anisoCij("Monoclinic", c11=2.0, c12=3.0, c13=4.0, c15=5.0, c22=6.0, c23=7.0, c25=8.0, c33=9.0, c35=10, c44=11.0, c46=12.0, c55=13.0, c66=14.0)

widget_22=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:0,0')
if widget_22: wevent(widget_22, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_22.get_window())
del widget_22
checkpoint MonoclinicCijklWidget updated
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Monoclinic:widget_GTK_RESPONSE_CANCEL').clicked()

# Open and check Triclinic
findWidget('OOF2').resize(782, 545)
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Triclinic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 7]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint TriclinicCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic').resize(528, 292)
widget_23=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:0,0')
if widget_23: wevent(widget_23, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_23.get_window())
del widget_23
checkpoint TriclinicCijklWidget updated
widget_24=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:0,0')
if widget_24: wevent(widget_24, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_24.get_window())
del widget_24
checkpoint TriclinicCijklWidget updated
assert tests.anisoCij("Triclinic", c11=1.0, c12=0.5, c13=0.5, c16=123., c22=1.0, c23=0.5, c25=456., c33=1.0, c34=789., c44=0.25, c55=0.25, c66=0.25)

widget_25=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:0,0')
if widget_25: wevent(widget_25, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_25.get_window())
del widget_25
checkpoint TriclinicCijklWidget updated
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Triclinic:widget_GTK_RESPONSE_CANCEL').clicked()
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
