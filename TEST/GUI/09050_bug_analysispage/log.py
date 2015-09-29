# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.2 $
# $Author: langer $
# $Date: 2009/02/04 21:42:33 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# This test checks for a strange gtk/Field bug that is only appearing
# on the Mac.  If the user loads a script that defines a Field, and
# then switches immediately to the Analysis page, gtk goes into an
# infinite loop.  If this test finishes, it passes.

# First, make sure that the script has loaded.
checkpoint OOF.Subproblem.Field.Define

# # # # # # # # # # # # # # # # # # 
#
# If the test hangs on the following line, it has failed.  Hit
# control-C in the terminal window to escape the infinite loop.
#
# # # # # # # # # # # # # # # # # # 
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Analysis')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(353, 93)
findWidget('Questioner:gtk-delete').clicked()
checkpoint OOF.ActivityViewer.File.Close
