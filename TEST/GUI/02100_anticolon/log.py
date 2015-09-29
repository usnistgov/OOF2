checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.6 $
# $Author: langer $
# $Date: 2014/09/27 21:42:10 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests

findWidget('OOF2:Navigation:Next').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(150)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(314, 168)
findWidget('Dialog-Create Microstructure:name:Auto').clicked()
assert not tests.msOKsensitive()
findWidget('Dialog-Create Microstructure:name:Text').set_text('a')
findWidget('Dialog-Create Microstructure:name:Text').set_text('ab')
findWidget('Dialog-Create Microstructure:name:Text').set_text('abc')
assert tests.msOKsensitive()
findWidget('Dialog-Create Microstructure:name:Text').set_text('abc:')
assert not tests.msOKsensitive()
findWidget('Dialog-Create Microstructure:name:Text').set_text('abc')
assert tests.msOKsensitive()
findWidget('Dialog-Create Microstructure:name:Text').set_text('abcd')
findWidget('Dialog-Create Microstructure:name:Text').set_text('abcde')
findWidget('Dialog-Create Microstructure:name:Text').set_text('abcdef')
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(153)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
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
checkpoint OOF.Microstructure.New
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
findWidget('OOF2').resize(684, 350)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((0,))
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1,), open_all=False)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1, 0), open_all=False)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((1, 0, 0))
widget_0=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_0.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_0.window))
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Mechanical;Elasticity;Isotropic
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic').resize(282, 72)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name:Auto').clicked()
assert not tests.propertyOKsensitive()
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name:Text').set_text('a')
assert tests.propertyOKsensitive()
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name:Text').set_text('ab')
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name:Text').set_text('abc')
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name:Text').set_text('abc:')
assert not tests.propertyOKsensitive()
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name:Text').set_text('abc')
assert tests.propertyOKsensitive()
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:gtk-ok').clicked()
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1, 0, 0), open_all=False)
findWidget('OOF2:Materials Page:Pane').set_position(272)
checkpoint OOF.Property.Copy
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Mechanical;Elasticity;Isotropic;abc
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc').resize(282, 72)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name:Text').set_text('abc:')
assert not tests.property2OKsensitive()
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name:Text').set_text('abc:d')
assert not tests.property2OKsensitive()
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name:Text').set_text('abc:de')
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name:Text').set_text('abc:def')
assert not tests.property2OKsensitive()
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name:Text').set_text('abc:de')
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name:Text').set_text('abc:d')
assert not tests.property2OKsensitive()
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name:Text').set_text('abc:')
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name:Text').set_text('abc')
assert tests.property2OKsensitive()
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name:Text').set_text('abcd')
assert tests.property2OKsensitive()
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:gtk-ok').clicked()
findWidget('OOF2:Materials Page:Pane').set_position(272)
checkpoint OOF.Property.Copy
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
findWidget('OOF2').resize(691, 434)
findWidget('OOF2:Skeleton Page:Pane').set_position(347)
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(389, 202)
findWidget('Dialog-New skeleton:name:Auto').clicked()
assert not tests.skelOKsensitive()
findWidget('Dialog-New skeleton:name:Text').set_text(':')
assert not tests.skelOKsensitive()
findWidget('Dialog-New skeleton:name:Text').set_text('')
assert not tests.skelOKsensitive()
findWidget('Dialog-New skeleton:name:Text').set_text('a')
assert tests.skelOKsensitive()
findWidget('Dialog-New skeleton:name:Text').set_text('ab')
findWidget('Dialog-New skeleton:name:Text').set_text('ab:')
assert not tests.skelOKsensitive()
findWidget('Dialog-New skeleton:name:Text').set_text('ab')
assert tests.skelOKsensitive()
findWidget('Dialog-New skeleton:name:Text').set_text('abd')
findWidget('Dialog-New skeleton:name:Text').set_text('abde')
assert tests.skelOKsensitive()
findWidget('Dialog-New skeleton:name:Text').set_text('abde:')
assert not tests.skelOKsensitive()
findWidget('Dialog-New skeleton:name:Text').set_text('abde')
assert tests.skelOKsensitive()
findWidget('Dialog-New skeleton:gtk-cancel').clicked()
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(358, 94)
findWidget('Questioner:gtk-delete').clicked()
