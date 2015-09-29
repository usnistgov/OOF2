# -*- python -*-
# $RCSfile: display.py,v $
# $Revision: 1.114 $
# $Author: langer $
# $Date: 2010/12/02 21:09:24 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

## Display objects and friends.  A *Display* is basically a collection
## of DisplayMethods, sharing the same output device.  The layers are
## drawn in turn.

#####################################

## Display Object Overview

"""

Each layer in the graphics window is defined by a DisplayMethod
instance.  (Subclasses of DisplayMethod are defined elsewhere.)  The
source of the data for each DisplayMethod is a Who object.  There can
be many DisplayMethods for a single Who, and the user may want to
change each DisplayMethod's Who at the same time, so DisplayMethods
are grouped into LayerSets, and the Who is associated with the
LayerSet instead of with the DisplayMethod directly.  Each
DisplayMethod knows its LayerSet, and each LayerSet contains a list of
its DisplayMethods.  The graphics window, or rather its non-gui
component, the GhostGfxWindow, maintains a list of LayerSets.

The Display is an object contained in a GhostGfxWindow that manages
the DisplayLayers.  (It's not clear at this time why it's a separate
class, and whether or not its functionality should be merged into the
GhostGfxWindow class.  The separation may just be a historical
artifact.  Resolving that is a TODO LATER.)  The Display keeps a list
of DisplayMethods, containing all the methods of all the LayerSets in
the GhostGfxWindow.  The Display's list determines the order in which
the layers are drawn.  The LayerSets' lists have nothing to do with
drawing order.

Layers are added to a graphics window when the LayerEditor calls
GhostGfxWindow.incorporateLayerSet with a new LayerSet as an argument.
If the GhostGfxWindow has no currently selected layer, a clone of the
new LayerSet is added to the Display.  If there is a currently
selected layer, its LayerSet is replaced with a clone of the new
LayerSet.

"""

#####################################

from ooflib.SWIG.common import config
from ooflib.SWIG.common import lock
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import timestamp
from ooflib.common import debug
from ooflib.common import registeredclass
from ooflib.common import subthread
from ooflib.common.IO import parameter
from ooflib.common.IO import placeholder
from ooflib.common.IO import whoville
from ooflib.common.IO import xmlmenudump
import string
import types
import weakref


############

# LayerOrderings are used to determine the default position of a layer
# in the display.  Displays that fill planes are drawn first, followed
# by those that partially fill planes, etc.

class LayerOrdering:
    def __init__(self, order, suborder=0.):
        self.order = order
        self.suborder = suborder
    def __cmp__(self, other):
        if self.order < other.order: return -1
        if self.order > other.order: return 1
        if self.suborder < other.suborder: return -1
        if self.suborder > other.suborder: return 1
        return 0
    def __call__(self, suborder):
        return LayerOrdering(self.order, suborder)

def layercomparator(a, b):
    aordering = a.layerordering()
    bordering = b.layerordering()
    return aordering.__cmp__(bordering)

Abysmal = LayerOrdering(-1000)          # shouldn't ever appear
Planar = LayerOrdering(0.)              # filled meshes, or images
SemiPlanar = LayerOrdering(1.)          # partially filled meshes or images
Linear = LayerOrdering(2.)              # mesh boundaries
SemiLinear = LayerOrdering(3.)          # partial mesh boundaries
PointLike = LayerOrdering(4.)           # single pixels or nodes

############

class DisplayMethodParameter(parameter.RegisteredParameter):
    def __init__(self, name, value=None, default=None, tip=None):
        parameter.RegisteredParameter.__init__(self, name, DisplayMethod,
                                               value, default, tip)

    def clone(self):
        return self.__class__(self.name, self.value, self.default, self.tip)

#############

# DisplayMethods are things like ContourPlots, Bitmaps, etc --
# different ways of displaying different types of Who objects on a
# graphics device.  They must have a 'draw' function, and the
# Registration for each DisplayMethod class must have a 'whoclasses'
# attribute which lists the names of the WhoClasses that the
# DisplayMethod accepts.

class DisplayMethod(registeredclass.RegisteredClass):
    registry = []
    def __init__(self):
        self.layerset = None
        self.hidden = False
        self.listed = True     # is it listed in gfxwindow layer list?
        self.frozen = False

        # Different OutputDevices have different internal
        # representations for the layers (DisplayMethods).  A Display
        # may be used on more than one OutputDevice, so each layer
        # keeps a dictionary of all of its device dependent
        # representations.
        self.devicelayers = weakref.WeakKeyDictionary()
        # When was this layer last displayed on this device?
        self.timestamps = weakref.WeakKeyDictionary()

    # Derived classes must redefine this:
    def draw(self, device):
        pass

    # Derived classes which can have contours should redefine these
    # next three functions.
    def contour_capable(self, gfxwindow):
        return 0 # Must be zero, and not "None", arithmetic is done on it.
    
    # Should return the bounds of the contours.
    def get_contourmap_info(self):
        pass

    # Should actually draw the colorbar on the passed-in device.
    def draw_contourmap(self, gfxwindow, device):
        pass

    # Other contour-map-management functions -- only implemented
    # in subclasses of ContourDisplay.
    def explicit_contour_hide(self):
        pass
        
    def hide_contourmap(self):
        pass

    def show_contourmap(self):
        pass

    # Frozen layers won't be *redrawn*, but they will be drawn on new
    # devices.  These functions should be redefined in derived classes
    # that need to do more computation (such as storing the time) when
    # freezing.
    def freeze(self, gfxwindow):
        self.frozen = True
    def unfreeze(self, gfxwindow):
        self.frozen = False
    def refreeze(self, layer):
        # Copy frozen status from another layer.
        self.frozen = layer.frozen
    
    def incomputable(self, gfxwindow):
        # Subclasses may override incomputable().  incomputable() must
        # return None if the DisplayMethod is actually computable, or
        # return a string explaining why the method is incomputable.
        # For example, a method that displays a field defined on a
        # mesh would return 'Field not defined' if that field weren't
        # defined on the mesh self.who().
        who = self.who().resolve(gfxwindow)
        if who is None:
            return "Nothing to draw"
        if not self.acceptsWho(who):
            return "DisplayMethod can't display %s objects" \
                   % who.getClass().name()

    def animatable(self, gfxwindow):
        return False            # redefined in AnimationLayer

    def acceptsWho(self, who):
        return self.acceptsWhoClass(who.getClass())
    def acceptsWhoClass(self, whoclass):
        whoclassname = whoclass.name()
        registration = self.getRegistration()
        return whoclassname in registration.whoclasses
        
    # Bookkeeping routines called by LayerSet.addMethod(), etc.
    def addToLayerSet(self, layerset):
        self.layerset = layerset
    def removeFromLayerSet(self, layerset):
        self.layerset = None

    def clone(self, layerset=None):
        self.setDefaultParams()
        bozo = self.getRegistration()()
        bozo.hidden = self.hidden
        bozo.listed = self.listed
        bozo.frozen = self.frozen
        if layerset is None:
            bozo.addToLayerSet(self.layerset)
        else:
            bozo.addToLayerSet(layerset)
        return bozo

    def name(self):
        return self.getRegistration().name()

    def who(self):
        if self.layerset is not None:
            return self.layerset.who

    # Distinct methods with the same values should not compare
    # equally, so override RegisteredClass's __eq__.
    def __eq__(self, other):
        return id(self)==id(other)
    
    # The former __eq__, negated, for equivalence testing.
    def inequivalent(self, other):
        return other is None or \
               not (other.__class__ is self.__class__ 
                    and other.who() is self.who() 
                    and registeredclass.RegisteredClass.__eq__(self, other))

    def destroy(self):
        if self.layerset is not None:
            self.layerset.removeMethod(self)
        self.layerset = None
        for devicelayer in self.devicelayers.values():
            devicelayer.destroy()
        
    def drawIfNecessary(self, gfxwindow, device):
        # Called by Display.draw().
        try:
            lasttime = self.timestamps[device]
            dlayer = self.devicelayers[device]
        except KeyError:
            # Layer hasn't been drawn on this device yet!
            lasttime = self.timestamps[device] = timestamp.TimeStamp()
            lasttime.backdate()
            dlayer = self.devicelayers[device] = device.begin_layer() 
            actuallydraw = True
        else:
            actuallydraw = not self.frozen

        # This is needed because it keeps the order of the oofcanvas
        # layers in sync with the higher level layers.
        dlayer.raise_to_top() 

        # othertimes is a list of the TimeStamps of events that
        # require the display layer to be redrawn.
        othertimes = [self.getTimeStamp(gfxwindow),
                      self.layerset.whotime,
                      self.layerset.who.getTimeStamp(gfxwindow)]
        if self.animatable(gfxwindow):
            othertimes.append(gfxwindow.displayTimeChanged)

        if lasttime < max(othertimes):
            dlayer.make_current()
            whoobj = self.layerset.who.resolve(gfxwindow)
            whoobj.begin_reading()      # acquire lock
            try:
                if actuallydraw:
                    dlayer.clear()
                    if self.hidden:
                        dlayer.hide()
                    device.comment('Layer: %s' % `self`)
                    # Note that if the device is a buffered output device,
                    # this won't necessarily call the lowest level drawing
                    # calls (and *actually* draw something).  That happens
                    # when the buffer is flushed.
                    self.draw(gfxwindow, device)
                    lasttime.increment()
                    device.end_layer() ## flushes the buffer one last time.
            finally:
                whoobj.end_reading()    # release lock

    def hide(self, device=None):
        self.hidden = True
        if not device:
            for devicelayer in self.devicelayers.values():
                devicelayer.hide()
        else:
            self.devicelayers[device].hide()
    def show(self, device=None):
        self.hidden = False
        if not device:
            for devicelayer in self.devicelayers.values():
                devicelayer.show()
        else:
            self.devicelayers[device].show()

    def clear(self, device=None):
        # Clear a layer on a device (or all devices), backdating its
        # timestamp so that it will be redrawn the next time around.
        if device:
            try:
                dlayer = self.devicelayers[device]
            except KeyError:            # layer hasn't been drawn yet
                return
            dlayer.clear()
            self.timestamps[device].backdate()
        else:
            for device,devicelayer in self.devicelayers.items():
                devicelayer.clear()
                self.timestamps[device].backdate() # force redraw
            
    def backdate(self, device):
        try:
            self.timestamps[device].backdate()
        except KeyError:
            pass

    def getTimeStamp(self, gfxwindow):
        # Return the timestamp for the last event that changed the
        # contents of the display layer.  This must be redefined in
        # subclasses if the timestamp depends on proxy resolution.
        # That's why the gfxwindow is passed as an argument.
        return self.timestamp

    def outOfTime(self, gfxwindow):
        # Has the GfxWindow's displayTime changed since this layer was
        # last drawn?
        try:
            ts = self.timestamps[gfxwindow.device]
        except KeyError:
            return True
        return ts < gfxwindow.displayTimeChanged

    def raise_layer(self, howfar=1):
        for devicelayer in self.devicelayers.values():
            devicelayer.raise_layer(howfar)
    def lower_layer(self, howfar=1):
        for devicelayer in self.devicelayers.values():
            devicelayer.lower_layer(howfar)

    def layerordering(self):
        return self.getRegistration().layerordering
    
    # The short name is just the classname and the "what", if there is
    # one.  Used by the gfxwindow's layer display, if the appropriate
    # setting is set.
    def short_name(self):
        try:
            what = self.what
        except AttributeError:
            return self.__class__.__name__
        else:
            return "%s(%s)" % (self.__class__.__name__, what.shortrepr())

class AnimationLayer:
    def __init__(self, when):
        self.when = when
    def animatable(self, gfxwindow):
        return (not self.frozen and self.when is placeholder.latest
                and not self.incomputable(gfxwindow))
    def animationTimes(self, gfxwindow):
        # Return a list of available times.
        raise ooferror.ErrPyProgrammingError(
            "Someone forgot to redefine animationTimes for",
            self.__class__.__name__)

#######################

# Routine to add lists of DisplayMethods sorted by their target
# objects to the xml documentation for the DisplayMethod base class.

def _addMethodList(text, obj):
    regdict = {}
    for reg in DisplayMethod.registry:
        for whoclass in reg.whoclasses:
            try:
                classlist = regdict[whoclass]
            except KeyError:
                regdict[whoclass] = classlist = []
            classlist.append(reg)
    whoclasses = regdict.keys()
    whoclasses.sort()
    lines = ["""
    <para>Here is a list of the types of displayable objects and the
    DisplayMethods that apply to them:
    <itemizedlist>
        """]
    for whoclass in whoclasses:
        lines.append("<listitem><para>%s" % whoclass)
        lines.append("<itemizedlist spacing='compact' id='DisplayMethods:%s'>" % whoclass)
        for reg in regdict[whoclass]:
            lines.append("<listitem><simpara><link linkend='%s'>%s (%s</link>) -- %s</simpara></listitem>"
                         % (xmlmenudump.registrationID(reg), reg.name(),
                         reg.subclass.__name__, reg.tip))

        lines.append("</itemizedlist></para></listitem>")

    lines.append("</itemizedlist></para>")
    return text + string.join(lines, '\n')

DisplayMethod.tip = "Methods for drawing &oof2; objects in the graphics window."
DisplayMethod.discussion = xmlmenudump.loadFile(
    'DISCUSSIONS/common/reg/displaymethod.xml', _addMethodList)

######################

class EmptyLayer:
    # Dummy layer that replaces layers removed from a LayerSet
    def name(self):
        return "<deleted>"
    def clone(self, layerset=None):
        return self
    def removeFromLayerSet(self, *args):
        pass
    def addToLayerSet(self, *args):
        pass
    def acceptsWhoClass(self, *args):
        return 0
    def acceptsWho(self, *args):
        return 0
    def inequivalent(self, otherlayer):
        return otherlayer is not self
    def incomputable(self, gfxwindow):
        return "empty!"
    def layerordering(self):
        return Abysmal
    def who(self):
        return None
    def __repr__(self):
        return "EmptyLayer"

emptyLayer = EmptyLayer()
    
class LayerSet:
    def __init__(self, who=whoville.nobody):
        self.who = who
        self.methods = []               # DisplayMethod objects
        self.whotime = timestamp.TimeStamp() # When self.who was changed last
        self.forced = 0                 # should it be incorporated into a
                                        # gfxwindow even if it's not computable?
    def clone(self):
        bozo = LayerSet(self.who)
        for m in self.methods:
            bozo.addMethod(m.clone())
        bozo.forced = self.forced
        return bozo
    def destroy(self):
        # Breaks circular references.  Does not remove layers from displays.
        self.methods = []
        self.who = None
    def addMethod(self, method):
        self.methods.append(method)
        method.addToLayerSet(self)
    def removeMethod(self, method):
        self.methods.remove(method)
        method.removeFromLayerSet(self)
    def doomMethod(self, which):
        # Methods that are removed are replaced by emptyLayer, rather
        # than actually being removed from the list, so that the
        # ordering isn't messed up when copying LayerSets from the
        # layer editor to the graphics window.  When it's safe, the
        # empty layers are removed by LayerSet.cleanUp.  doomMethod is
        # called by the layereditor.
        self.methods[which] = emptyLayer
    def removeAll(self):
        self.methods = [emptyLayer]*len(self.methods)
    def replaceMethod(self, which, newmethod):
        oldmethod = self.methods[which]
        oldmethod.removeFromLayerSet(self)
        self.methods[which] = newmethod
        newmethod.addToLayerSet(self)
    def copyMethod(self, which):
        self.methods.append(self.methods[which].clone(self))
    def changeWho(self, who):
        self.whotime.increment()
        self.who = who
    def __getitem__(self, i):
        return self.methods[i]
    def __len__(self):
        return len(self.methods)
    def invalid(self):
        if not self.methods:
            return 1
        if not self.who:
            return 1
        for m in self.methods:
            if m != emptyLayer and not m.acceptsWho(self.who):
                return 1
        return 0
    def index(self, method):
        return self.methods.index(method)
    def __repr__(self):
        return 'LayerSet(%s, force=%d, %s)' % (`self.who`, self.forced,
                                               `self.methods`)
            
#######################################

class Display:
    def __init__(self):
        self.layers = [] # Displaymethod objects, from bottom to top. 
        self.layerChangeTime = timestamp.TimeStamp()
        self.sorted = True
        # This lock just protects the local list.
        self.lock = lock.SLock()

    def add_layer(self, displaylayer):
        self.lock.acquire()
        try:
            self.layers.append(displaylayer)
            self.layerChangeTime.increment()
            self.sorted = False
            return displaylayer
        finally:
            self.lock.release()
    def remove_layer(self, displaylayer):
        self.lock.acquire()
        try:
            self.layers.remove(displaylayer)
            self.layerChangeTime.increment()
            self.sorted = False
        finally:
            self.lock.release()
    def replace_layer(self, oldlayer, newlayer):
        newlayer.refreeze(oldlayer)
        self.lock.acquire()
        try:
            self.layers[self.layers.index(oldlayer)] = newlayer
            self.layerChangeTime.increment()
            self.sorted = False
        finally:
            self.lock.release()
    def topcontourable(self,gfxwindow):
        # Iterate over the list from back to front.
        for i in range(len(self.layers)):
            ell = self.layers[-(i+1)]
            if ell.contour_capable(gfxwindow) and not ell.hidden:
                return ell
    def layerID(self, layer):
        try:
            return self.layers.index(layer)
        except ValueError:
            for hen in self.layers:
                print "        ", hen
            raise
    def getLayerChangeTimeStamp(self):
        return self.layerChangeTime
    def nlayers(self):
        return len(self.layers)
    def __len__(self):
        return len(self.layers)
    def __getitem__(self, i):
        return self.layers[i]
    def __setitem__(self, i, displaymethod):
        self.layers[i] = displaymethod
        self.sorted = False

    def draw(self, gfxwindow, device):
        # High level drawing action is done here.  Loop through the
        # layers and drawIfNecessary.  Note that if the device is a
        # bufferedoutputdevice, the low level drawing calls will be
        # added to the buffer and excecuted after device.show is
        # called.
        self.lock.acquire()
        try:
            for layer in self.layers:
                reason = layer.incomputable(gfxwindow)
                if reason:      # ignore incomputable display methods
#                    debug.fmsg('ignoring layer:', layer, reason)
                    layer.clear(device)
                else:
                    try:
                        layer.drawIfNecessary(gfxwindow, device)
                    except subthread.StopThread:
#                         print layer, "has a problem!"
                        return
                    # TODO SWIG1.3: After conversion to SWIG 1.3, OOF
                    # exceptions will probably be subclasses of
                    # Exception.
                    except (Exception, ooferror.ErrErrorPtr), exc:
                        # This should not happen for computable Outputs
                        debug.fmsg('Exception while drawing!', exc)
                        raise
        finally:
            self.lock.release()
            # If the device is a buffered output device, this flushes
            # the buffer and executes the low level drawing calls --
            # ie actually draws something on the screen.
        device.show()
        # Finally, if it is 3D and some layers were actually
        # drawn, render the scene.  We only want to call this at a
        # high level because 3D rendering is slow.
        if config.dimension() == 3:
            gfxwindow.oofcanvas.update_volume_and_render()
#        debug.fmsg("Exiting.")

    def drawable(self, gfxwindow):
        # Can any layer be drawn? Used when testing the gui.
        self.lock.acquire()
        try:
            for layer in self.layers:
                if not layer.incomputable(gfxwindow):
                    return True
        finally:
            self.lock.release()
        return False

    # Return the non-hidden contour-capable method.  There should only
    # be one, so returning the first one is safe.
    def get_contourmap_method(self, gfxwindow):
        for layer in self.layers:
            if layer.contour_capable(gfxwindow):
                if not layer.contourmaphidden:
                    return layer
        return None # Default behavior, not required.

    # Find the topmost contourable method, and set it to be the
    # only nonhidden one.
    def set_contourmap_topmost(self, gfxwindow):
        for layer in self.layers:
            layer.hide_contourmap()
        topmost = self.topcontourable(gfxwindow)
        if topmost:
            topmost.show_contourmap()
            return topmost

    # Contourmaps are drawn on the canvas directly by the gfxwindow,
    # which has additional auxiliary info, like min/max values for the
    # text boxes.  This routine is called for drawing it into a file,
    # typically with the "device" being PSOutput.
    def draw_contourmap(self, gfxwindow, device):
        contourmap_layer = self.get_contourmap_method(gfxwindow)
        if contourmap_layer:
            device.begin_layer()
            contourmap_layer.draw_contourmap(gfxwindow, device)
            device.end_layer()
            device.show()

            
    def clear(self, device=None):       # device is None ==> all devices
        "Clear layers and backdate timestamps so that they'll be redrawn."
        for layer in self.layers:
            layer.clear(device)

    def hide_layer(self, device, n):
        # If the layer hasn't been drawn yet, the lookup in the
        # devicelayers dictionary will fail.
        try:
            self.layers[n].devicelayers[device].hide()
        except KeyError:
            pass
    def show_layer(self, device, n):
        # If the layer hasn't been drawn yet, the lookup in the
        # devicelayers dictionary will fail.
        try:
            self.layers[n].devicelayers[device].show()
        except KeyError:
            pass
    def raise_layer_by(self, n, howfar):
        self.lock.acquire()
        try:
            if n < self.nlayers()-howfar:
                thislayer = self.layers[n]
                # update our list of layers
                for i in range(howfar):
                    self.layers[n+i] = self.layers[n+i+1]
                self.layers[n+howfar] = thislayer
                # actually reorder layers in devices
                thislayer.raise_layer(howfar)
                self.layerChangeTime.increment()
                self.sorted = False
        finally:
            self.lock.release()
    def raise_layer(self, n):
        self.raise_layer_by(n, 1)
    def layer_to_top(self, n):
        self.raise_layer_by(n, self.nlayers()-n-1)

    def lower_layer_by(self, n, howfar):
        self.lock.acquire()
        try:
            if n >= howfar:
                thislayer = self.layers[n]
                for i in range(howfar):
                    self.layers[n-i] = self.layers[n-i-1]
                self.layers[n-howfar] = thislayer
                thislayer.lower_layer(howfar)
                self.layerChangeTime.increment()
                self.sorted = False
        finally:
            self.lock.release()
    def lower_layer(self, n):
        self.lower_layer_by(n, 1)
    def layer_to_bottom(self, n):
        self.lower_layer_by(n, n)

    def reorderLayers(self):
        self.lock.acquire()
        try:
            if not self.sorted:
                self.layers.sort(layercomparator)
                self.layerChangeTime.increment()
                self.sorted = True
        finally:
            self.lock.release()

