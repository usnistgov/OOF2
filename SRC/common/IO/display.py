# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

## The DisplayMethod class and friends. A DisplayMethod defines a
## layer in the canvas.  Different subclasses of DisplayMethod display
## different Who objects in different ways.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import lock
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import timestamp
from ooflib.common import color
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common import registeredclass
from ooflib.common import subthread
from ooflib.common import utils
from ooflib.common.IO import parameter
from ooflib.common.IO import placeholder
from ooflib.common.IO import whoville
from ooflib.common.IO import xmlmenudump

import oofcanvas

import types
import weakref


#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# LayerOrderings are used to determine the default position of a layer
# in the display.  Displays that fill planes are drawn first, followed
# by those that partially fill planes, etc.

class LayerOrdering:
    def __init__(self, order, suborder=0.):
        self.order = order
        self.suborder = suborder
    def __lt__(self, other):
        return (self.order < other.order or
                (self.order == other.order and self.suborder < other.suborder))
    def __ge__(self, other):
        return not self.__lt__(other)
    def __gt__(self, other):
        return (self.order > other.order or
                (self.order == other.order and self.suborder > other.suborder))
    def __le__(self, other):
        return not self.__gt__(other)
    def __call__(self, suborder):
        return LayerOrdering(self.order, suborder)

Abysmal = LayerOrdering(-1000)          # shouldn't ever appear
Planar = LayerOrdering(0.)              # filled meshes, or images
SemiPlanar = LayerOrdering(1.)          # partially filled meshes or images
Linear = LayerOrdering(2.)              # mesh boundaries
SemiLinear = LayerOrdering(3.)          # partial mesh boundaries
PointLike = LayerOrdering(4.)           # single pixels or nodes

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class DisplayMethodParameter(parameter.RegisteredParameter):
    def __init__(self, name, value=None, default=None, tip=None):
        parameter.RegisteredParameter.__init__(self, name, DisplayMethod,
                                               value, default, tip)

    def clone(self):
        return self.__class__(self.name, self.value, self.default, self.tip)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# DisplayMethods are things like ContourPlots, Bitmaps, etc --
# different ways of displaying different types of Who objects on a
# graphics device.  They must have a 'draw' function, and the
# Registration for each DisplayMethod class must have a 'whoclasses'
# attribute which lists the names of the WhoClasses that the
# DisplayMethod accepts.

class DisplayMethod(registeredclass.RegisteredClass):
    registry = []
    def __init__(self):
        self.hidden = False
        self.listed = True     # is it listed in gfxwindow layer list?
        self.frozen = False

        self.canvaslayer = None # an oofcanvas.CanvasLayer

        # When was this layer last modified?
        self.timestamp = timestamp.TimeStamp()
        # When was this layer last drawn?
        self.lastDrawn = timestamp.TimeStamp()
        self.lastDrawn.backdate() # it hasn't been drawn yet

    def build(self, gfxwindow):
        self.canvaslayer = gfxwindow.oofcanvas.newLayer(self.short_name())
        if self.hidden:
            self.canvaslayer.hide()
        else:
            self.canvaslayer.show()

    def destroy(self):
        # The OOFCanvas owns its CanvasLayers, so just deleting a
        # layer in Python doesn't delete it from the canvas.  It has
        # to be explicitly destroyed.
        self.canvaslayer.destroy()
        del self.canvaslayer

    def empty(self):
        return self.canvaslayer is None or self.canvaslayer.empty()

    def setWho(self, who):
        self.who = who

    def getWho(self, gfxwindow):
        return self.who.resolve(gfxwindow)

    # Derived classes must redefine this.
    def draw(self, gfxwindow):
        pass

    # Derived classes which can have contours should redefine these
    # next three functions.
    def contour_capable(self, gfxwindow):
        return 0 # Must be zero, and not "None", arithmetic is done on it.
    
    # Should return the bounds of the contours.
    def get_contourmap_info(self):
        pass

    # Should actually draw the colorbar on the passed-in
    # OOFCanvas.CanvasLayer.
    def draw_contourmap(self, gfxwindow, canvaslayer):
        pass

    # Frozen layers won't be redrawn, but they will be drawn once.
    # These functions should be redefined in derived classes that need
    # to do more computation (such as storing the time) when freezing.
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
        # defined on the mesh self.who.
        ## TODO: just returning True or False is probably sufficient.
        who = self.who.resolve(gfxwindow)
        if who is None or who.getObject() is None:
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
        
    def clone(self):
        self.setDefaultParams()
        bozo = self.getRegistration()()
        bozo.hidden = self.hidden
        bozo.listed = self.listed
        bozo.frozen = self.frozen
        return bozo

    def name(self):
        return self.getRegistration().name()

    # Distinct methods with the same values should not compare
    # equally, so override RegisteredClass's __eq__.  This is so that
    # it's possible to have two identical layers in the layer list but
    # still be able to refer to them individually.  I think.  If you
    # need to see if two different Display objects are identical, use
    # Display.equivalent().
    def __eq__(self, other):
        return id(self)==id(other)
    
    def equivalent(self, other):
        return registeredclass.RegisteredClass.__eq__(self, other)

    def drawIfNecessary(self, gfxwindow):
        if self.frozen and self.lastDrawn != timestamp.timeZero:
            return
        
        # othertimes is a list of the TimeStamps of events that
        # require the display layer to be redrawn.
        othertimes = [self.getTimeStamp(gfxwindow),
                      self.who.getTimeStamp(gfxwindow)]
        if self.animatable(gfxwindow):
            othertimes.append(gfxwindow.displayTimeChanged)

        if self.lastDrawn < max(othertimes):
            whoobj = self.who.resolve(gfxwindow)
            whoobj.begin_reading()      # acquire lock
            try:
                # make surface and context
                mainthread.runBlock(self.canvaslayer.rebuild) 
                self.canvaslayer.removeAllItems()
                if self.hidden:
                    self.canvaslayer.hide()
                self.draw(gfxwindow)
                self.lastDrawn.increment()
            finally:
                whoobj.end_reading()    # release lock

    def hide(self):
        self.hidden = True
        self.canvaslayer.hide()
    def show(self):
        self.hidden = False
        self.canvaslayer.show()

    def clear(self):
        # Clear a layer, backdating its timestamp so that it will be
        # redrawn the next time around.
        if self.canvaslayer:
            self.canvaslayer.removeAllItems()
        self.backdate()
            
    def backdate(self):
        self.lastDrawn.backdate()

    def getTimeStamp(self, gfxwindow):
        # Return the timestamp for the last event that changed the
        # contents of the display layer.  This must be redefined in
        # subclasses if the timestamp depends on proxy resolution.
        # That's why the gfxwindow is passed as an argument.
        return self.timestamp

    def outOfTime(self, gfxwindow):
        # Has the GfxWindow's displayTime changed since this layer was
        # last drawn?
        return self.lastDrawn < gfxwindow.displayTimeChanged

    def raise_layer(self, howfar=1):
        self.canvaslayer.raiseBy(howfar)
    def lower_layer(self, howfar=1):
        self.canvaslayer.lowerBy(howfar)

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

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

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
    whoclasses = sorted(list(regdict.keys()))
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
    return text + utils.stringjoin(lines, '\n')

DisplayMethod.tip = "Methods for drawing &oof2; objects in the graphics window."
DisplayMethod.discussion = xmlmenudump.loadFile(
    'DISCUSSIONS/common/reg/displaymethod.xml', _addMethodList)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class MicrostructurePerimeterDisplay(DisplayMethod):
    def __init__(self, color, width):
        self.color = color
        self.width = width
        DisplayMethod.__init__(self)

    def draw(self, gfxwindow):
        size = self.getWho(gfxwindow).getObject().size()
        rect = oofcanvas.CanvasRectangle.create((0, 0), size)
        rect.setLineWidthInPixels(self.width)
        rect.setLineColor(color.canvasColor(self.color))
        self.canvaslayer.addItem(rect)
        

registeredclass.Registration(
    'Perimeter',
    DisplayMethod,
    MicrostructurePerimeterDisplay,
    ordering=100,
    layerordering=Linear(0),
    params=[
        color.TranslucentColorParameter('color', color.black),
        parameter.FloatParameter('width', 1.0)],
    whoclasses = ('Microstructure',),
    )


