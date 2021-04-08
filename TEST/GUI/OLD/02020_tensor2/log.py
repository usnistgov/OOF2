checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests

# Create a material
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
findWidget('OOF2').resize(684, 350)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(249, 72)
findWidget('Dialog-New material:gtk-ok').clicked()
checkpoint OOF.Material.New
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((0,))
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((5,), open_all=False)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((5, 0), open_all=False)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9135135135135e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.0297297297297e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.8270270270270e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.9000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((5, 0, 1), open_all=False)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.8090909090909e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 6.0857142857143e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 6.6389610389610e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 6.9155844155844e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.1922077922078e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.4688311688312e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.7454545454545e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.0220779220779e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.2987012987013e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.5753246753247e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.8519480519481e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.1285714285714e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0511688311688e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0788311688312e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1341558441558e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1894805194805e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2171428571429e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2448051948052e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2724675324675e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.3277922077922e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.3554545454545e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4107792207792e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4384415584416e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4661038961039e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4937662337662e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5214285714286e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5490909090909e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5767532467532e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6044155844156e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6320779220779e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6597402597403e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6874025974026e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7150649350649e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((5, 0, 1, 0))
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7100000000000e+02)

# Open Cubic thermal expansion
widget_0=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_0.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_0.window))
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated((4, 0, 1, 0), column)
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic
# Check initial values
assert tests.testAij("Cubic", a11=1.0, a22=1.0, a33=1.0)
assert tests.sensitiveAij("Cubic", a11=1)
# Change a_11 to 3
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic').resize(257, 164)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0').set_text('3')
widget_1=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0')
widget_1.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_1.window))
assert tests.testAij("Cubic", a11=3.0, a22=3.0, a33=3.0)
# Close and add to material
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:gtk-ok').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Cubic
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
findWidget('OOF2:Materials Page:Pane').set_position(272)
checkpoint OOF.Material.Add_property
# Open hexagonal thermal expansion
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((5, 0, 1, 1))
widget_2=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_2.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_2.window))
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated((4, 0, 1, 1), column)
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal
# Check initial values
assert tests.testAij("Hexagonal", a11=1.0, a22=1.0, a33=0.5)
assert tests.sensitiveAij("Hexagonal", a11=1, a33=1)
# Change a_11 to 4
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal').resize(257, 164)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:0,0').set_text('4')
widget_3=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:0,0')
widget_3.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_3.window))
assert tests.testAij("Hexagonal", a11=4.0, a22=4.0, a33=0.5)
# Change a_33 to 1
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:2,2').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:2,2').set_text('1')
widget_4=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:2,2')
widget_4.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_4.window))
assert tests.testAij("Hexagonal", a11=4.0, a22=4.0, a33=1.0)
# Close and add to material
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:gtk-ok').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Hexagonal
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
findWidget('OOF2:Materials Page:Pane').set_position(272)
checkpoint OOF.Material.Add_property
# Open trigonal thermal expansion
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((5, 0, 1, 2))
widget_5=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_5.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_5.window))
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated((4, 0, 1, 2), column)
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal
# Check initial values
assert tests.testAij("Trigonal", a11=1.0, a22=1.0, a33=0.5)
assert tests.sensitiveAij("Trigonal", a11=1, a33=1)
# Change a_11 to 5
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal').resize(257, 164)
widget_6=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:0,0')
widget_6.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_6.window))
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:0,0').set_text('5')
widget_7=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:0,0')
widget_7.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_7.window))
assert tests.testAij("Trigonal", a11=5.0, a22=5.0, a33=0.5)
# Change a_33 to 0.6
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:2,2').set_text('0.')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:2,2').set_text('0.6')
widget_8=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:2,2')
widget_8.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_8.window))
assert tests.testAij("Trigonal", a11=5.0, a22=5.0, a33=0.6)
# Close and add to material
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:gtk-ok').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Trigonal
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
findWidget('OOF2:Materials Page:Pane').set_position(272)
checkpoint OOF.Material.Add_property
# Open tetragonal thermalexpansion
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 4.0000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((5, 0, 1, 3))
widget_9=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_9.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_9.window))
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated((4, 0, 1, 3), column)
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal
# Check initial values
assert tests.testAij('Tetragonal', a11=1.0, a22=1.0, a33=0.5)
assert tests.sensitiveAij("Tetragonal", a11=1, a33=1)
# Change a_11 to 6
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal').resize(257, 164)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:0,0').set_text('6')
widget_10=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:0,0')
widget_10.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_10.window))
assert tests.testAij('Tetragonal', a11=6.0, a22=6.0, a33=0.5)
# Change a_33 to 1
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:2,2').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:2,2').set_text('1')
widget_11=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:2,2')
widget_11.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_11.window))
assert tests.testAij('Tetragonal', a11=6.0, a22=6.0, a33=1.0)
# Close and add to material
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:gtk-ok').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Tetragonal
# Open orthorhombic thermalexpansion
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((5, 0, 1, 4))
widget_12=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_12.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_12.window))
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated((4, 0, 1, 4), column)
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic
# Check initial values
assert tests.testAij("Orthorhombic", a11=1.0, a22=1.0, a33=1.0)
assert tests.sensitiveAij("Orthorhombic", a11=1, a22=1, a33=1)
# Change a_11 to 3
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic').resize(257, 164)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:0,0').set_text('3')
widget_13=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:0,0')
widget_13.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_13.window))
assert tests.testAij("Orthorhombic", a11=3.0, a22=1.0, a33=1.0)
# Change a_22 to 4
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:1,1').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:1,1').set_text('4')
widget_14=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:1,1')
widget_14.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_14.window))
assert tests.testAij("Orthorhombic", a11=3.0, a22=4.0, a33=1.0)
# Change a_33 to 5
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:2,2').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:2,2').set_text('5')
widget_15=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:2,2')
widget_15.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_15.window))
assert tests.testAij("Orthorhombic", a11=3.0, a22=4.0, a33=5.0)
# Save and add to material
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:gtk-ok').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Orthorhombic
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
findWidget('OOF2:Materials Page:Pane').set_position(272)
checkpoint OOF.Material.Add_property
# Open monoclinic thermalexpansion
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 6.2000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 1.8000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8710000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0320000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((5, 0, 1, 5))
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0300000000000e+02)
widget_16=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_16.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_16.window))
widget_17=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_17.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_17.window))
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated((4, 0, 1, 5), column)
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic
# Check initial values
assert tests.testAij("Monoclinic", a11=1.0, a13=0.5, a22=1.0, a33=1.0)
assert tests.sensitiveAij("Monoclinic", a11=1, a13=1, a22=1, a33=1)
# Change a_11 to 2
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic').resize(257, 164)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,0').set_text('2')
widget_18=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,0')
widget_18.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_18.window))
assert tests.testAij("Monoclinic", a11=2.0, a13=0.5, a22=1.0, a33=1.0)
# Change a_13 to 3
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,2').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,2').set_text('3')
widget_19=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,2')
widget_19.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_19.window))
assert tests.testAij("Monoclinic", a11=2.0, a13=3.0, a22=1.0, a33=1.0)
# Change a_22 to 4
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:1,1').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:1,1').set_text('4')
widget_20=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:1,1')
widget_20.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_20.window))
assert tests.testAij("Monoclinic", a11=2.0, a13=3.0, a22=4.0, a33=1.0)
# Change a_33 to 45
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:2,2').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:2,2').set_text('4')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:2,2').set_text('45')
widget_21=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:2,2')
widget_21.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_21.window))
assert tests.testAij("Monoclinic", a11=2.0, a13=3.0, a22=4.0, a33=45.0)
# Close and add to material
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:gtk-ok').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Monoclinic
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
findWidget('OOF2:Materials Page:Pane').set_position(272)
checkpoint OOF.Material.Add_property
# Open triclinic thermalexpansion
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 8.4000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 4.0000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((5, 0, 1, 6))
widget_22=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_22.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_22.window))
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated((4, 0, 1, 6), column)
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic
# Check initial values
assert tests.testAij("Triclinic", a11=1.0, a22=1.0, a33=1.0)
assert tests.sensitiveAij("Triclinic", a11=1, a12=1, a13=1, a22=1, a23=1, a33=1)
# Change a_11 to 2
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic').resize(257, 164)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,0').set_text('2')
widget_23=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,0')
widget_23.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_23.window))
assert tests.testAij("Triclinic", a11=2.0, a22=1.0, a33=1.0)
# Change a_12 to 34
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,1').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,1').set_text('3')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,1').set_text('34')
widget_24=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,1')
widget_24.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_24.window))
assert tests.testAij("Triclinic", a11=2.0, a12=34.0, a22=1.0, a33=1.0)
# Change a_13 to 5
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,2').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,2').set_text('5')
widget_25=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,2')
widget_25.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_25.window))
assert tests.testAij("Triclinic", a11=2.0, a12=34.0, a13=5.0, a22=1.0, a33=1.0)
# Change a_22 to 6
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:1,1').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:1,1').set_text('6')
widget_26=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:1,1')
widget_26.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_26.window))
assert tests.testAij("Triclinic", a11=2.0, a12=34.0, a13=5.0, a22=6.0, a33=1.0)
# Change a_23 = 7
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:1,2').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:1,2').set_text('7')
widget_27=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:1,2')
widget_27.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_27.window))
assert tests.testAij("Triclinic", a11=2.0, a12=34.0, a13=5.0, a22=6.0, a23=7.0, a33=1.0)
# Change a_33 to 8
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:2,2').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:2,2').set_text('8')
widget_28=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:2,2')
widget_28.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_28.window))
assert tests.testAij("Triclinic", a11=2.0, a12=34.0, a13=5.0, a22=6.0, a23=7.0, a33=8.0)
# Close and add to material
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:gtk-ok').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Triclinic
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
findWidget('OOF2:Materials Page:Pane').set_position(272)
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 1.0600000000000e+02)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 6.2000000000000e+01)
# Save material to rank2mat.dat
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Materials').activate()
checkpoint toplevel widget mapped Dialog-Materials
findWidget('Dialog-Materials').resize(194, 170)
findWidget('Dialog-Materials:filename').set_text('r')
findWidget('Dialog-Materials:filename').set_text('ra')
findWidget('Dialog-Materials:filename').set_text('ran')
findWidget('Dialog-Materials:filename').set_text('rank')
findWidget('Dialog-Materials:filename').set_text('rank2')
findWidget('Dialog-Materials:filename').set_text('rank2m')
findWidget('Dialog-Materials:filename').set_text('rank2ma')
findWidget('Dialog-Materials:filename').set_text('rank2mat')
findWidget('Dialog-Materials:filename').set_text('rank2mat.')
findWidget('Dialog-Materials:filename').set_text('rank2mat.d')
findWidget('Dialog-Materials:filename').set_text('rank2mat.da')
findWidget('Dialog-Materials:filename').set_text('rank2mat.dat')
findWidget('Dialog-Materials:materials').get_selection().unselect_all()
findWidget('Dialog-Materials:materials').get_selection().select_path((0,))
findWidget('Dialog-Materials:gtk-ok').clicked()
checkpoint OOF.File.Save.Materials
assert tests.filediff('rank2mat.dat')
# Delete material
findWidget('OOF2:Materials Page:Pane:Material:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(194, 94)
findWidget('Questioner:gtk-ok').clicked()
checkpoint OOF.Material.Delete
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.1300000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.1023376623377e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0746753246753e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0193506493506e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9916883116883e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9640259740260e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9363636363636e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8810389610390e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8533766233766e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8257142857143e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7980519480519e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7703896103896e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7427272727273e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7150649350649e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6874025974026e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6320779220779e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6044155844156e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5490909090909e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5214285714286e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4937662337662e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4661038961039e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4384415584416e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((5, 0, 1, 0))
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4300000000000e+02)
widget_29=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_29.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_29.window))
widget_30=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_30.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_30.window))
widget_31=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_31.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_31.window))
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
# Open cubic thermalexpansion and check for previous values
column = tree.get_column(0)
tree.row_activated((4, 0, 1, 0), column)
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic
assert tests.testAij("Cubic", a11=3.0, a22=3.0, a33=3.0)
# Change a_00 to 5
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic').resize(257, 164)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0').set_text('5')
widget_32=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0')
widget_32.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_32.window))
assert tests.testAij("Cubic", a11=5.0, a22=5.0, a33=5.0)
# Close thermalexpansion
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:gtk-ok').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Cubic
# TODO: Change all other thermalexpansion moduli so that we can check that reloading has worked
# Load rank2mat.dat
findMenu(findWidget('OOF2:MenuBar'), 'File:Load:Data').activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(194, 72)
findWidget('Dialog-Data:filename').set_text('r')
findWidget('Dialog-Data:filename').set_text('ra')
findWidget('Dialog-Data:filename').set_text('ran')
findWidget('Dialog-Data:filename').set_text('rank')
findWidget('Dialog-Data:filename').set_text('rank2')
findWidget('Dialog-Data:filename').set_text('rank2m')
findWidget('Dialog-Data:filename').set_text('rank2ma')
findWidget('Dialog-Data:filename').set_text('rank2mat')
findWidget('Dialog-Data:filename').set_text('rank2mat.')
findWidget('Dialog-Data:filename').set_text('rank2mat.d')
findWidget('Dialog-Data:filename').set_text('rank2mat.da')
findWidget('Dialog-Data:filename').set_text('rank2mat.dat')
findWidget('Dialog-Data:gtk-ok').clicked()
checkpoint OOF.File.Load.Data
# Open cubic thermalexpansion
widget_33=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_33.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_33.window))
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated((4, 0, 1, 0), column)
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic
assert tests.testAij("Cubic", a11=3.0, a22=3.0, a33=3.0)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic').resize(257, 164)
widget_34=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0')
widget_34.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_34.window))
# Cancel
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:gtk-cancel').clicked()
# Open hexagonal thermalexpansion
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((5, 0, 1, 1))
widget_35=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_35.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_35.window))
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated((4, 0, 1, 1), column)
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal
assert tests.testAij("Hexagonal", a11=4.0, a22=4.0, a33=1.0)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal').resize(257, 164)
widget_36=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:0,0')
widget_36.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_36.window))
# Cancel
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:gtk-cancel').clicked()
# Open trigonal thermalexpansion
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((5, 0, 1, 2))
widget_37=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_37.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_37.window))
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated((4, 0, 1, 2), column)
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal
assert tests.testAij("Trigonal", a11=5.0, a22=5.0, a33=0.6)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal').resize(257, 164)
widget_38=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:0,0')
widget_38.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_38.window))
# Cancel
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:gtk-cancel').clicked()
# Open tetragonal thermalexpansion
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((5, 0, 1, 3))
widget_39=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_39.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_39.window))
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated((4, 0, 1, 3), column)
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal
assert tests.testAij('Tetragonal', a11=6.0, a22=6.0, a33=1.0)
# Open orthorhombic thermalexpansion
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal').resize(257, 164)
widget_40=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:0,0')
widget_40.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_40.window))
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:gtk-cancel').clicked()
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4661038961039e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4937662337662e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5214285714286e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5490909090909e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6044155844156e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6874025974026e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7150649350649e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7427272727273e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7703896103896e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8257142857143e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8533766233766e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8810389610390e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9087012987013e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9363636363636e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9640259740260e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0193506493506e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0470129870130e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0746753246753e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.1023376623377e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((5, 0, 1, 4))
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.1000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 1.7000000000000e+01)
widget_41=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_41.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_41.window))
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated((4, 0, 1, 4), column)
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic
assert tests.testAij("Orthorhombic", a11=3.0, a22=4.0, a33=5.0)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic').resize(257, 164)
widget_42=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:0,0')
widget_42.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_42.window))
# Cancel
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:gtk-cancel').clicked()
# Open monoclinic thermalexpansion
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((5, 0, 1, 5))
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 3.9000000000000e+01)
widget_43=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_43.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_43.window))
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated((4, 0, 1, 5), column)
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic
assert tests.testAij("Monoclinic", a11=2.0, a13=3.0, a22=4.0, a33=45.0)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic').resize(257, 164)
widget_44=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,0')
widget_44.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_44.window))
# Cancel
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:gtk-cancel').clicked()
# Open triclinic thermalexpansion
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((5, 0, 1, 6))
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 6.1000000000000e+01)
widget_45=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_45.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_45.window))
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated((4, 0, 1, 6), column)
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic
assert tests.testAij("Triclinic", a11=2.0, a12=34.0, a13=5.0, a22=6.0, a23=7.0, a33=8.0)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic').resize(257, 164)
widget_46=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,0')
widget_46.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_46.window))
# Cancel
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:gtk-cancel').clicked()
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Messages').activate()
checkpoint toplevel widget mapped Dialog-Messages
findWidget('Dialog-Messages').resize(194, 197)
findWidget('Dialog-Messages:gtk-cancel').clicked()
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(194, 72)
findWidget('Dialog-Python_Log:filename').set_text('r')
findWidget('Dialog-Python_Log:filename').set_text('ra')
findWidget('Dialog-Python_Log:filename').set_text('ran')
findWidget('Dialog-Python_Log:filename').set_text('rank')
findWidget('Dialog-Python_Log:filename').set_text('rank2')
findWidget('Dialog-Python_Log:filename').set_text('rank2m')
findWidget('Dialog-Python_Log:filename').set_text('rank2ma')
findWidget('Dialog-Python_Log:filename').set_text('rank2mat')
findWidget('Dialog-Python_Log:filename').set_text('rank2mat.')
findWidget('Dialog-Python_Log:filename').set_text('rank2mat.l')
findWidget('Dialog-Python_Log:filename').set_text('rank2mat.lo')
findWidget('Dialog-Python_Log:filename').set_text('rank2mat.log')
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('rank2mat.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
