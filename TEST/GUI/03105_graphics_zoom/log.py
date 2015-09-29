# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.2 $
# $Author: langer $
# $Date: 2010/03/19 18:59:22 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# This test checks for a bug in graphics zooming in unthreaded mode.
# The test passes if it finishes without crashing.

checkpoint page installed Introduction
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint toplevel widget mapped OOF2
findWidget('OOF2').resize(550, 350)
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Microstructure
findWidget('OOF2').resize(577, 350)
findWidget('OOF2:Microstructure Page:Pane').set_position(164)
findMenu(findWidget('OOF2:MenuBar'), 'Windows:Graphics:New').activate()
checkpoint selection info updated
checkpoint Move Node toolbox info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(285)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(692)
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1').resize(800, 400)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(715)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Viewer:Zoom:In').clicked()
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(358, 94)
findWidget('Questioner:gtk-delete').clicked()
