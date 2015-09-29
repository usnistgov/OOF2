# -*- python -*-
# $RCSfile: menu.py,v $
# $Revision: 1.5 $
# $Author: langer $
# $Date: 2014/09/27 21:41:40 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

##from SWIG.image.imagemanip import demo
##from SWIG.image import oofimage
##from common.IO import mainmenu
##from common.IO import oofmenu
##from common.IO import whoville
##from common.IO import parameter
##from common import debug
##from types import *

##menu = mainmenu.OOF.File.addItem(oofmenu.OOFMenuItem('ImageManip'))

### OOFMenu callback function:

##def demoCB(menuitem, image, arg2):
##    debug.fmsg(image, arg2)
##    demo.testfunction(oofimage.getImage(image), arg2) #  SWIGged C++ function

### Menu Item definition:

##menu.addItem(oofmenu.OOFMenuItem(
##    'Demo',
##    callback=demoCB,
##    # parameter names *must* match the arguments in the callback function
##    params=[whoville.WhoParameter('image', whoville.getClass('Image')),
##            parameter.Parameter('arg2', IntType, 123)]))
