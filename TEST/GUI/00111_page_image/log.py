#checkpoint toplevel widget mapped OOF2
checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.8 $
# $Author: langer $
# $Date: 2010/12/01 20:43:44 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

#Check that the "Load" button on the Image page is sensitized correctly.

import tests

findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(150)
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Image
findWidget('OOF2').resize(593, 350)
findWidget('OOF2:Image Page:Pane').set_position(380)
checkpoint meshable button set
assert tests.loadSensitive(0)
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint page installed Microstructure
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(162)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
checkpoint meshable button set
findWidget('Dialog-Create Microstructure').resize(314, 166)
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(165)
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint active area status updated
checkpoint pixel page updated
checkpoint mesh bdy page updated
checkpoint microstructure page sensitized
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
# checkpoint interface page updated
checkpoint OOF.Microstructure.New
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Image
findWidget('OOF2:Image Page:Pane').set_position(380)
assert tests.loadSensitive(1)
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(352, 92)
findWidget('Questioner:gtk-delete').clicked()
