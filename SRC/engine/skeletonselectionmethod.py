# -*- python -*-
# $RCSfile: skeletonselectionmethod.py,v $
# $Revision: 1.15 $
# $Author: langer $
# $Date: 2014/09/27 21:40:56 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.


# This file contains the selection methods for the Skeleton Selection
# Toolboxes.  The toolboxes are derived from GenericSelectToolbox, so
# the menu callback associated with each selection method is
# GenericSelectToolbox.selectCB.  The menus are created by
# GenericSelectToolbox.rebuildMenus.

from ooflib.SWIG.common import config
from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common import registeredclass
from ooflib.common.IO import xmlmenudump

############################

## Common base class for the different types of skeleton selection
## method registrations.  The only purpose of this base class is so
## that a common default rubberband function can be assigned to it in
## engine/IO/GUI/skeletonselectiontoolboxGUI.py.

class SkeletonSelectionRegistration(registeredclass.Registration):
    def __init__(self, name, regclass, subclass, ordering, params=[],
                 secret=0, **kwargs):
        registeredclass.Registration.__init__(self, name, regclass,
                                              subclass, ordering, params,
                                              secret, **kwargs)

############################

class NodeSelectMethod(registeredclass.RegisteredClass):
    registry = []
    def select(self, skeletoncontext, pointlist, selector):
        pass
    ## No tip or discussion members are required here because the
    ## NodeSelectMethod classes are converted into menu items.

class NodeSelectionRegistration(SkeletonSelectionRegistration):
    def __init__(self, name, subclass, ordering, params=[], secret=0, **kwargs):
        SkeletonSelectionRegistration.__init__(self,
                                               name=name,
                                               regclass=NodeSelectMethod,
                                               subclass=subclass,
                                               ordering=ordering,
                                               params=params,
                                               secret=secret,
                                               **kwargs)
# # # # # # # # # # # # # # # #

# Should call the selector with the skeletoncontext and a list of
# nodes on which to operate.
class SingleNodeSelect(NodeSelectMethod):
    def select(self, skeletoncontext, pointlist, selector):
        closest = skeletoncontext.getObject().nearestNode(pointlist[0])
        selector([closest])
        
NodeSelectionRegistration(
    'Single_Node',
    SingleNodeSelect,
    ordering=0,
    events=['up'],
    tip="Select a single node.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/single_node.xml'))

if config.dimension() == 2:
    class RectangleNodeSelect(NodeSelectMethod):
        def select(self, skeletoncontext, pointlist, selector):
            reslist = []
            xmin = min(pointlist[0].x, pointlist[1].x)
            xmax = max(pointlist[0].x, pointlist[1].x)
            ymin = min(pointlist[0].y, pointlist[1].y)
            ymax = max(pointlist[0].y, pointlist[1].y)
            for n in skeletoncontext.getObject().nodes:
                if n.position().x < xmax and n.position().x > xmin and \
                       n.position().y < ymax and n.position().y > ymin:
                    reslist.append(n)
            selector(reslist)

    rectangleNodeSelector = NodeSelectionRegistration(
        'Rectangle',
        RectangleNodeSelect,
        ordering=1,
        events=['down', 'up'],
        tip="Drag to select nodes within a rectangle.",
        discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/rectangle_node.xml')
        )


    class CircleNodeSelect(NodeSelectMethod):
        def select(self, skeletoncontext, pointlist, selector):
            reslist = []
            center = pointlist[0]
            radius2 = (pointlist[1]-pointlist[0])**2

            for n in skeletoncontext.getObject().nodes:
                dist2 = (n.position() - center)**2
                if dist2 < radius2:
                    reslist.append(n)
            selector(reslist)

    circleNodeSelector = NodeSelectionRegistration(
        'Circle',
        CircleNodeSelect,
        ordering=2,
        events=['down', 'up'],
        tip="Drag to select nodes within a circle.",
        discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/circle_node.xml')
        )


    class EllipseNodeSelect(NodeSelectMethod):
        def select(self, skeletoncontext, pointlist, selector):
            reslist = []
            aa = (0.5*(pointlist[0].x - pointlist[-1].x))**2
            bb = (0.5*(pointlist[0].y - pointlist[-1].y))**2
            center = 0.5*(pointlist[0]+pointlist[-1])
            for n in skeletoncontext.getObject().nodes:
                dx = n.position() - center
                if dx.x*dx.x*bb + dx.y*dx.y*aa < aa*bb:
                    reslist.append(n)
            selector(reslist)

    ellipseNodeSelector = NodeSelectionRegistration(
        'Ellipse',
        EllipseNodeSelect,
        ordering=3,
        events=['down', 'up'],
        tip="Drag to select nodes within an ellipse.",
        discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/ellipse_node.xml'))
                
##########################################

# Segment selection is like node selection, except for details.
# SegmentSelectMethods convert mouse-clicks into lists of segments.
class SegmentSelectMethod(registeredclass.RegisteredClass):
    registry = []
    def select(self, skeletoncontext, pointlist, selector):
        pass
    ## No tip or discussion members are required here because the
    ## SegmentSelectMethod classes are converted into menu items.


class SegmentSelectionRegistration(SkeletonSelectionRegistration):
    def __init__(self, name, subclass, ordering, params=[], secret=0, **kwargs):
        SkeletonSelectionRegistration.__init__(
            self,
            name=name,
            regclass=SegmentSelectMethod,
            subclass=subclass,
            ordering=ordering,
            params=params,
            secret=secret,
            **kwargs)

class SingleSegmentSelect(SegmentSelectMethod):
    def select(self, skeletoncontext, pointlist, selector):
        nearseg = skeletoncontext.getObject().nearestSgmt(pointlist[0])
        selector([nearseg])

SegmentSelectionRegistration(
    'Single_Segment',
    SingleSegmentSelect, ordering=0,
    events=['up'],
    tip="Select a segment joining two nodes.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/single_segment.xml')
    )


if config.dimension() == 2:
    # Parent class for all the area selectors.  Sets self.xmin, self.xmax,
    # self.ymin, self.ymax.  Subclasses provide the "interior" function.
    class AreaSegmentSelect(SegmentSelectMethod):
        def select(self, skeletoncontext, pointlist, selector):
            reslist = []
            self.first = pointlist[0]
            self.xmin = min(pointlist[0].x, pointlist[1].x)
            self.xmax = max(pointlist[0].x, pointlist[1].x)
            self.ymin = min(pointlist[0].y, pointlist[1].y)
            self.ymax = max(pointlist[0].y, pointlist[1].y)
            self.xspan2 = (self.xmax-self.xmin)**2
            self.yspan2 = (self.ymax-self.ymin)**2
            self.center = primitives.Point(0.5*(self.xmax+self.xmin),
                                           0.5*(self.ymax+self.ymin))

            for (k,v) in skeletoncontext.getObject().segments.items():
                if self.interior(k[0]) and self.interior(k[1]):
                    reslist.append(v)
            selector(reslist)

    class RectangleSegmentSelect(AreaSegmentSelect):
        # Determine whether or a point is inside the rectangle.
        def interior(self, n):
            if n.position().x < self.xmax and n.position().x > self.xmin and \
                   n.position().y < self.ymax and n.position().y > self.ymin:
                return 1
            return 0

    rectangleSegmentSelector = SegmentSelectionRegistration(
        'Rectangle',
        RectangleSegmentSelect,
        ordering=1,
        events=['down', 'up'],
        tip="Drag to select segments within a rectangle.",
        discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/rectangle_segment.xml')
        )


    class CircleSegmentSelect(AreaSegmentSelect):
        # Determine whether or not a point is inside the ellipse.
        def interior(self, n):
            delta = n.position() - self.first
            if delta**2 < (self.xspan2 + self.yspan2):
                return 1
            return None

    circleSegmentSelector = SegmentSelectionRegistration(
        'Circle',
        CircleSegmentSelect,
        ordering=2,
        events=['down', 'up'],
        tip="Drag to select segments within an ellipse.",
        discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/circle_segment.xml')
        )


    class EllipseSegmentSelect(AreaSegmentSelect):
        # Determine whether or not a point is inside the ellipse.
        def interior(self, n):
            delta = n.position() - self.center
            if delta.x*delta.x*self.yspan2 + delta.y*delta.y*self.xspan2 < \
                   (self.xspan2*self.yspan2)/4.0:
                return 1
            return None


    ellipseSegmentSelector = SegmentSelectionRegistration(
        'Ellipse',
        EllipseSegmentSelect,
        ordering=3,
        events=['down', 'up'],
        tip="Drag to select segments within an ellipse.",
        discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/ellipse_segment.xml')
        )


#############################################


class ElementSelectMethod(registeredclass.RegisteredClass):
    registry = []
    def select(self, skeletoncontext, pointlist, selector):
        pass
    ## No tip or discussion members are required here because the
    ## ElementSelectMethod classes are converted into menu items.


class ElementSelectionRegistration(SkeletonSelectionRegistration):
    def __init__(self, name, subclass, ordering, params=[], secret=0, **kwargs):
        SkeletonSelectionRegistration.__init__(
            self,
            name=name,
            regclass=ElementSelectMethod,
            subclass=subclass,
            ordering=ordering,
            params=params,
            secret=secret,
            **kwargs)

class SingleElementSelect(ElementSelectMethod):
    def select(self, skeletoncontext, pointlist, selector):
        pt = pointlist[0]
        res = []
        el = skeletoncontext.getObject().enclosingElement(pt)
        if el and el.interior(pt):
            res = [el]
        selector(res)
        
ElementSelectionRegistration(
    'Single_Element',
    SingleElementSelect,
    ordering=0,
    events=['up'],
    tip="Select an element.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/single_element.xml')
    )

#####################################

if config.dimension() == 2:
    class AreaElementSelect(ElementSelectMethod):
        def select(self, skeletoncontext, pointlist, selector):
            reslist = []
            self.first = pointlist[0]
            self.xmin = min(pointlist[0].x, pointlist[-1].x)
            self.xmax = max(pointlist[0].x, pointlist[-1].x)
            self.ymin = min(pointlist[0].y, pointlist[-1].y)
            self.ymax = max(pointlist[0].y, pointlist[-1].y)
            self.xspan2 = (self.xmax-self.xmin)**2
            self.yspan2 = (self.ymax-self.ymin)**2
            self.center = primitives.Point(0.5*(self.xmax+self.xmin),
                                           0.5*(self.ymax+self.ymin))

            for e in skeletoncontext.getObject().elements:
                for n in e.nodes:
                    if not self.interior(n):
                        break
                else:
                    reslist.append(e)
            selector(reslist)


    class RectangleElementSelect(AreaElementSelect):
        # Determine whether or a point is inside the rectangle.
        def interior(self, n):
            if n.position().x < self.xmax and n.position().x > self.xmin and \
                   n.position().y < self.ymax and n.position().y > self.ymin:
                return 1
            return 0

    rectangleElementSelector = ElementSelectionRegistration(
        'Rectangle',
        RectangleElementSelect,
        ordering=1,
        events=['down', 'up'],
        tip="Drag to select elements within a rectangle.",
        discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/rectangle_element.xml')
        )


    class CircleElementSelect(AreaElementSelect):
        # Determine whether or not a point is inside the ellipse.
        def interior(self, n):
            delta = n.position() - self.first
            if delta**2 < (self.xspan2 + self.yspan2):
                return 1
            return None

    circleElementSelector = ElementSelectionRegistration(
        'Circle',
        CircleElementSelect,
        ordering=2,
        events=['down', 'up'],
        tip="Drag to select elements within a circle.",
        discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/circle_element.xml')
        )


    class EllipseElementSelect(AreaElementSelect):
        # Determine whether or not a point is inside the ellipse.
        def interior(self, n):
            delta = n.position() - self.center
            if delta.x*delta.x*self.yspan2 + delta.y*delta.y*self.xspan2 < \
                   (self.xspan2*self.yspan2)/4.0:
                return 1
            return None

    ellipseElementSelector = ElementSelectionRegistration(
        'Ellipse',
        EllipseElementSelect,
        ordering=3,
        events=['down', 'up'],
        tip="Drag to select elements within an ellipse.",
        discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/ellipse_element.xml')
        )


class PixelElementSelect(ElementSelectMethod):
    def select(self, skeletoncontext, pointlist, selector):
        reslist = []
        skel = skeletoncontext.getObject()
        MS = skel.MS
        category = MS.categoryFromPoint(pointlist[0])
        for e in skel.element_iterator():
            if e.dominantPixel(skel.MS) == category:
                reslist.append(e)
        selector(reslist)

ElementSelectionRegistration(
    'ByDominantPixel',
    PixelElementSelect, ordering=4,
    events=['up'],
    tip='Click on a pixel to select all elements with that type of dominant pixel.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/dominant_pixel.xml')
    )
