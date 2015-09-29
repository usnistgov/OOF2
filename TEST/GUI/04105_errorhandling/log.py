# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.4 $
# $Author: langer $
# $Date: 2010/05/27 20:40:05 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.common import utils
import generics

checkpoint OOF.File.LoadStartUp.Script
checkpoint toplevel widget mapped Error
findWidget('Error').resize(592, 160)
assert generics.errorMsg("NameError: global name 'y' is not defined\n\nErrUserError: Script 'TEST_DATA/pyerror.py' raised a NameError exception")
findWidget('Error:gtk-ok').clicked()
assert utils.OOFeval('teststring') == 'ok'
findMenu(findWidget('OOF2:MenuBar'), 'File:Load:Script').activate()
checkpoint toplevel widget mapped Dialog-Script
findWidget('Dialog-Script').resize(191, 71)
findWidget('Dialog-Script:filename').set_text('TEST_DATA/pyerror.py')
findWidget('Dialog-Script:gtk-ok').clicked()
checkpoint OOF.File.Load.Script
checkpoint toplevel widget mapped Error
findWidget('Error').resize(592, 160)
assert generics.errorMsg("NameError: global name 'y' is not defined\n\nErrUserError: Script 'TEST_DATA/pyerror.py' raised a NameError exception")
findWidget('Error:gtk-ok').clicked()
assert utils.OOFeval('teststring') == 'ok'
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
