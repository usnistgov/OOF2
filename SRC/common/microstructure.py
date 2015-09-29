# -*- python -*-
# $RCSfile: microstructure.py,v $
# $Revision: 1.153 $
# $Author: langer $
# $Date: 2010/12/04 03:49:53 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# A Microstructure object is a segmentation of an Image.  It stores the
# Pixelgroups to which the pixels in the Image have been assigned, as
# well as other PixelAttributes, such as Materials.

from ooflib.SWIG.common import config

from ooflib.SWIG.common import activearea
from ooflib.SWIG.common import cmicrostructure
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.common import ooferror
from ooflib.common import color
from ooflib.common import debug
from ooflib.common import pixelselection
from ooflib.common import primitives
from ooflib.common import utils
from ooflib.common.IO import whoville
from types import *
import string
import sys

#############################

# MicrostructurePlugIns are objects that can be defined in other
# modules.  An instance of each plug-in is created when a
# Microstructure is created, and destroyed when it's destroyed.  What
# happens in between is up to the plug-in.  When the Microstructure is
# created, the plug-in's constructor is called with the Microstructure
# as an argument.

class MicrostructurePlugIn:
    def __init__(self, microstructure):
        self.microstructure = microstructure
    def destroy(self):
        self.microstructure = None

plugInClasses = {}

def registerMicrostructurePlugIn(plugIn, name):
    plugInClasses[name] = plugIn

#############################

# TODO: There should be a way to resize a microstructure, and all of
# its contained components.

class Microstructure(cmicrostructure.CMicrostructure):
    def __init__(self, name, isize, size):
        cmicrostructure.CMicrostructure.__init__(self, name, isize, size)
        self._isize = isize     # iPoint(width, height) in pixels

        # Make sure that the physical size isn't stored as ints, which
        # could cause problems later (specifically when computing the
        # aspect ratio of the microstructure, as in
        # Skeleton.hashNodes).  This *isn't* done in the Point
        # constructor, since it might be slow.
        if config.dimension() == 2:
            self._size = primitives.Point(float(size.x), float(size.y))
        elif config.dimension() == 3:
            self._size = primitives.Point(float(size.x), float(size.y), float(size.z))
        # Also store increments.
        if config.dimension() == 2:
            self._delta  = (self._size[0]/self._isize[0],
                            self._size[1]/self._isize[1])
        elif config.dimension() == 3:
            self._delta  = (self._size[0]/self._isize[0],
                            self._size[1]/self._isize[1],
                            self._size[2]/self._isize[2])

        # The 'parent' arg to pixelselectionWhoClass.add and
        # activeareaWhoClass.add should be set to the Who object for
        # this MS, which hasn't been created yet. So it's set to None
        # here, and fixed later.
        pixsel = pixelselection.PixelSelection(isize, size, self)
        pixelselection.pixelselectionWhoClass.add(name, pixsel, parent=None)
        self.pixelselection = pixelselection.pixelselectionWhoClass[name]

        self.activearea = activearea.activeareaWhoClass.add(
            name, activearea.ActiveArea(isize, size, self), parent=None)
        self.namedActiveAreas = []
        self.setCurrentActiveArea(self.activearea.getObject())

        # Plug-ins have to be created before the Microstructure
        # context Who object is created, because Who object creation
        # might trigger switchboard calls that use the plug-ins.
        self.plugins = {}
        for pluginname, pluginclass in plugInClasses.items():
            self.plugins[pluginname] = pluginclass(self)

        # Create the Who object for this Microstructure, and add it to
        # list of all Microstructures.  Do this last, because it calls
        # switchboard callbacks that may assume that the MS is fully
        # constructed.
        mswho = microStructures.add(name, self, parent=None)
        # Fix the 'parent' for the pixelselection and activearea. See
        # comment above.
        self.pixelselection.setParent(mswho)
        self.activearea.setParent(mswho)

        self.sbcallbacks = [
            switchboard.requestCallback(('who changed', 'Active Area'),
                                        self.aaChangedCB)
            ]

    def aaChangedCB(self, activearea):
        if activearea.name() == self.name():
            self.setCurrentActiveArea(activearea.getObject())

    def nominalCopy(self, name):
        return Microstructure(name, self._isize, self._size)
        
    def destroy(self):
        for plugin in self.plugins.values():
            plugin.destroy()
        map(switchboard.removeCallback, self.sbcallbacks)
        # sbcallbacks must be explicitly cleared because
        # CMicrostructure has a swigged destructor.  That is,
        # sbcallbacks contains a SwitchboardCallback object which
        # contains a reference to the Microstructure (because the
        # callback function is SELF.aaChangedCB). That means that
        # there are circular references between Microstructure,
        # Microstructure.sbcallbacks, and the callback.  Circular
        # references aren't garbage collected if one of them has a
        # __del__ method, and Microstructure has a __del__ method
        # because it's derived from CMicrostructure, which has a
        # swigged destructor.
        self.sbcallbacks = []

        self.pixelselection = None
        self.activearea = None

    def getPlugIn(self, name):
        return self.plugins[name]

    def addImage(self, image):
        switchboard.notify('images changed in microstructure')

    def removeImage(self, image):
        image.removeMicrostructure(self)
        whoville.getClass('Image').remove([self.name(), image.name()])
        switchboard.notify('images changed in microstructure')

    def imageNames(self):
        imageclass = whoville.getClass('Image')
        return [path[0] for path in imageclass.keys(base=self.name())]

    def getImageContexts(self):
        imageclass = whoville.getClass('Image')
        return [imageclass[self.name()+':'+name[0]]
                for name in imageclass.keys(base=self.name())]

    # Many of these small utility functions are duplicated in C++ in
    # CMicrostructure.  That's intentional.
    
    def sizeInPixels(self):
        "iPoint(width, height) in pixels"
        return self._isize

    def sizeOfPixels(self):
        "(delta-x, delta-y) in a tuple."
        return self._delta

    def areaOfPixels(self):
        return self._delta[0]*self._delta[1]

    def area(self):
        return self._size[0]*self._size[1]

    if config.dimension() == 3:
        def volumeOfPixels(self):
            return self._delta[0]*self._delta[1]*self._delta[2]

        def volume(self):
            return self._size[0]*self._size[1]*self._size[2]
    
    def size(self):
        "Point(width, height) in physical units"
        return self._size

    def coords(self):
        if config.dimension() == 2:
            for j in range(self._isize[1]):
                for i in range(self._isize[0]):
                    yield primitives.iPoint(i, j)
        if config.dimension() == 3:
            for k in range(self._isize[2]):
                for j in range(self._isize[1]):
                    for i in range(self._isize[0]):
                        yield primitives.iPoint(i, j, k)

    def renameGroup(self, oldname, newname):
#         grp = self.findGroup(oldname)
        realnewname = self.uniqueGroupName(newname, oldname)
        self.renameGroupC(oldname, realnewname)
#         grp.rename(realnewname)
        

    def uniqueGroupName(self, name, oldname=None):
        return utils.uniqueName(name, self.groupNames(), exclude=oldname)

    # For this one, "where" is a Point.
    def categoryFromPoint(self, where):
        xx=where.x/self._delta[0]
        if xx==self._isize[0]: xx=self._isize[0]-1
        yy=where.y/self._delta[1]
        if yy==self._isize[1]: yy=self._isize[1]-1
        if config.dimension() == 2:
            return self.category(primitives.iPoint(xx,yy))
        elif config.dimension() == 3:
            zz=where.z/self._delta[2]
            if zz==self._isize[2]: zz=self._isize[2]-1
            return self.category(primitives.iPoint(xx,yy,zz))

    # Return the iPoint pixel index corresponding to the passed-in Point.
    def pixelFromPoint(self, where):
        xx=where.x/self._delta[0]
        if xx==1.0*self._isize[0]: xx=self._isize[0]-1
        yy=where.y/self._delta[1]
        if yy==1.0*self._isize[1]: yy=self._isize[1]-1
        if config.dimension() == 2:
            return primitives.iPoint(xx,yy)
        elif config.dimension() == 3:
            zz=where.z/self._delta[2]
            if zz==1.0*self._isize[2]: zz=self._isize[2]-1
            return primitives.iPoint(xx,yy,zz)

    def pixelInBounds(self, where):
        if where.x < 0 or where.x >= self._isize[0] or \
           where.y<0 or where.y >= self._isize[1]:
            return False
        if config.dimension() == 3:
            if where.z<0 or where.z >= self._isize[2]:
                return False
        return True

    def pointFromPixel(self, where):
        # This returns the center of the pixel, given integer pixel
        # coordinates. This is not the same thing as the general
        # transformation from (floating point) pixel coordinates to
        # physical coordinates, which is done by
        # CMicrostructure::pixel2Physical.
        if config.dimension() == 2:
            return primitives.Point((where.x+0.5)*self._delta[0],
                                    (where.y+0.5)*self._delta[1])
        elif config.dimension() == 3:
            return primitives.Point((where.x+0.5)*self._delta[0],
                                    (where.y+0.5)*self._delta[1],
                                    (where.z+0.5)*self._delta[2])

    def activePoint(self,point):
        # Is the given point in the active area?  No need to check
        # bounds, since isSelected calls BitmapOverlay::get(), which
        # does the checking.
        return self.activearea.isActive(self.pixelFromPoint(point))

    def saveActiveArea(self, name):
        aa = self.activearea.getObject().clone()
        self.namedActiveAreas.append(activearea.NamedActiveArea(name, aa))
        for pxl in aa.members():
            activearea.areaListFromPixel(self, pxl).add(name)
        
    def renameActiveArea(self, oldname, newname):
        for naa in self.namedActiveAreas:
            if naa.name == oldname:
                real_new_name = utils.uniqueName(newname,
                                                 self.activeAreaNames(),
                                                 exclude=oldname)
                naa.name = real_new_name
                for pxl in naa.activearea.members():
                    aal = activearea.areaListFromPixel(self, pxl)
                    aal.remove(oldname)
                    aal.add(real_new_name)

    def deleteActiveArea(self, name):
        for i in range(len(self.namedActiveAreas)):
            if self.namedActiveAreas[i].name == name:
                aa = self.namedActiveAreas[i]
                for pxl in aa.activearea.members():
                    activearea.areaListFromPixel(self, pxl).remove(name)
                del self.namedActiveAreas[i]
                return
            
    def getNamedActiveArea(self, name):
        for naa in self.namedActiveAreas:
            if naa.name == name:
                return naa
    def activeAreaNames(self):
        return [aa.name for aa in self.namedActiveAreas]
        

    # Microstructures are fairly complex objects, hard to construct,
    # but easy to retrieve, so the repr is a "retriever".
    def __repr__(self):
        return "getMicrostructure(%s)" % `self.name()`

    def transitionPointWithPoints(self, c0, c1):
        okay, point = cmicrostructure.CMicrostructurePtr.transitionPointWithPoints(self, c0, c1)
        if okay:
            return point

    #For SnapRefine
    def transitionPointWithPoints_unbiased(self, c0, c1):
        okay, point = cmicrostructure.CMicrostructurePtr.transitionPointWithPoints_unbiased(self, c0, c1)
        if okay:
            return point

class MicrostructureContext(whoville.Who):
    def getMicrostructure(self):
        return self.getObject()
    def getSelectionContext(self):
        return self.getObject().pixelselection
    def lockAndDelete(self):
        self.reserve()
        ms = self.getObject()
        try:
            # We have to remove Images, etc, from the Microstructure
            # *before* acquiring the write-lock on the Microstructure,
            # because we can't obtain the write locks on the Image and
            # the Microstructure at the same time.  (An Image can't be
            # locked unless it can obtain its Microstructure's read
            # lock.)
            for imagename in ms.imageNames():
                image = whoville.getClass('Image')[[self.name(), imagename]]
                image.begin_writing()
                try:
                    image.removeMicrostructure(ms)
                    ms.removeImage(image)
                finally:
                    image.end_writing()
            aa = activearea.activeareaWhoClass[self.name()]
            aa.begin_writing()
            try:
                activearea.activeareaWhoClass.remove(aa.name())
            finally:
                aa.end_writing()
            aa.setParent(None)
            pixsel = pixelselection.pixelselectionWhoClass[self.name()]
            pixsel.begin_writing()
            try:
                pixelselection.pixelselectionWhoClass.remove(pixsel.name())
            finally:
                pixsel.end_writing()
            pixsel.setParent(None)

            # Remove Skeletons
            skelclass = whoville.getClass('Skeleton')
            # TODO 3D: Remove this when engine is added to 3d
            if skelclass is not None:
                for skeletonname in skelclass.keys(base=self.name()):
                    skelcontext = skelclass[[self.name(), skeletonname[0]]]
                    skelcontext.lockAndDelete()
                    skelcontext.setParent(None)
            self.begin_writing()
            try:
                microStructures.remove(self.name())
                ms.destroy()
            finally:
                self.end_writing()
        finally:
            self.cancel_reservation()

## microsctructures is an instance of the WhoClass, which hosts
## a set of MicrostructureContext objects. The MicrostructureContext
## class was subclassed from the Who class, and it contains
## a Microstructure object.
microStructures = whoville.WhoClass('Microstructure', 150,
                                    instanceClass=MicrostructureContext,
                                    proxyClasses=['<topmost>',
                                                  '<top bitmap>'])

# Handy utility function, returns the microstructure object, not the
# context, and so is not equivalent to microStructures[name].
def getMicrostructure(name):
    try:
        return microStructures[name].getObject()
    except KeyError:
        return None

def getMSContextFromMS(microstructure):
    return microStructures[microstructure.name()]

utils.OOFdefine('Microstructure', Microstructure)
utils.OOFdefine('getMicrostructure', getMicrostructure)
