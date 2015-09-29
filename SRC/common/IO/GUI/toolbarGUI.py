# -*- python -*-
# $RCSfile: toolbarGUI.py,v $
# $Revision: 1.8 $
# $Author: langer $
# $Date: 2010/12/01 22:22:41 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import gobject
import gtk

from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import mousehandler
from ooflib.common.IO.GUI import toolboxGUI
from ooflib.common.IO.GUI import tooltips


class ToolBar:

    def __init__(self, gfxwindow):
        self.gfxwindow = gfxwindow

        buttonrow = gtk.HBox()
        # TODO 3D: make better icons for each of these, this is
        # complicated, we have to find a way to not use absolute
        # paths, and to include the icons in the build....
##         select_image = gtk.Image()
##         select_image.set_from_file("/users/vrc/i686_4.0/stow/oof2-dist3d-2.4/lib/python2.4/site-packages/oof3d/ooflib/common/IO/GUI/icons/select.png")
##         rotate_image = gtk.Image()
##         rotate_image.set_from_file("/users/vrc/i686_4.0/stow/oof2-dist3d-2.4/lib/python2.4/site-packages/oof3d/ooflib/common/IO/GUI/icons/rotate.png")
##         dolly_image = gtk.Image()
##         dolly_image.set_from_file("/users/vrc/i686_4.0/stow/oof2-dist3d-2.4/lib/python2.4/site-packages/oof3d/ooflib/common/IO/GUI/icons/dolly.png")

        # Use the "pressed" and "released" signals because the "clicked" signal is
        # emitted when the state is changed by setactive
        self.selectbutton = gtk.ToggleButton("Select")
        #self.selectbutton.set_image(select_image)
        buttonrow.pack_start(self.selectbutton)
        tooltips.set_tooltip_text(self.selectbutton,
            "Select objects according to toolbox behavior")
        gtklogger.connect(self.selectbutton, "pressed", self.selectCB)
        gtklogger.connect(self.selectbutton, "released", self.selectReleaseCB)
        self.tumblebutton = gtk.ToggleButton("Tumble")
        #self.tumblebutton.set_image(rotate_image)
        buttonrow.pack_start(self.tumblebutton)
        tooltips.set_tooltip_text(self.tumblebutton,"Tumble the view using the mouse")
        gtklogger.connect(self.tumblebutton, "pressed", self.tumbleCB)
        gtklogger.connect(self.tumblebutton, "released", self.tumbleReleaseCB)
        self.dollybutton = gtk.ToggleButton("Dolly")
        #self.dollybutton.set_image(dolly_image)
        buttonrow.pack_start(self.dollybutton)
        tooltips.set_tooltip_text(self.dollybutton,"Dolly in and out using the mouse")
        gtklogger.connect(self.dollybutton, "pressed", self.dollyCB)
        gtklogger.connect(self.dollybutton, "released", self.dollyReleaseCB)
        self.trackbutton = gtk.ToggleButton("Track")
        buttonrow.pack_start(self.trackbutton)
        tooltips.set_tooltip_text(self.trackbutton,
            "Move camera and visible objects parallel to focal plane")
        gtklogger.connect(self.trackbutton, "pressed", self.trackCB)
        gtklogger.connect(self.trackbutton, "released", self.trackReleaseCB)
        # TODO 3D: separator between stateful and non-stateful buttons?
        self.fillbutton = gtk.Button("Fill")
        buttonrow.pack_start(self.fillbutton)
        tooltips.set_tooltip_text(self.fillbutton,
            "Dolly in or out such that visible objects approximately fill viewport")
        gtklogger.connect(self.fillbutton, "clicked", self.fillCB)
        clippingscale = gtk.HScale(toolboxGUI.clippingadj)
        clippingscale.set_update_policy(gtk.UPDATE_DELAYED)
        clippingscale.set_value_pos(gtk.POS_RIGHT)
        buttonrow.pack_start(clippingscale)
        tooltips.set_tooltip_text(clippingscale,
            "Adjust the near clipping plane to view cross section")


        # TODO 3D: more useful things in the toolbar?
        self.gtk = buttonrow

        # self.selectHandler = SelectMouseHandler(gfxwindow)
        self.tumbleHandler = TumbleMouseHandler(gfxwindow)
        self.dollyHandler = DollyMouseHandler(gfxwindow)
        self.trackHandler = TrackMouseHandler(gfxwindow)

        self.selectbutton.set_active(True)


    def setSelect(self):
        self.selectbutton.set_active(True)
        self.tumblebutton.set_active(False)
        self.dollybutton.set_active(False)
        self.trackbutton.set_active(False)


    def selectCB(self, *args):
        self.tumblebutton.set_active(False)
        self.dollybutton.set_active(False)
        self.trackbutton.set_active(False)

    def selectReleaseCB(self, *args):
        self.selectbutton.set_active(True)
        self.gfxwindow.current_toolbox.activate()

    def tumbleCB(self, *args):
        self.selectbutton.set_active(False)
        self.dollybutton.set_active(False)
        self.trackbutton.set_active(False)

    def tumbleReleaseCB(self, *args):
        self.tumblebutton.set_active(True)
        self.gfxwindow.setMouseHandler(self.tumbleHandler)

    def dollyCB(self, *args):
        self.tumblebutton.set_active(False)
        self.selectbutton.set_active(False)
        self.trackbutton.set_active(False)

    def dollyReleaseCB(self, *args):
        self.dollybutton.set_active(True)
        self.gfxwindow.setMouseHandler(self.dollyHandler)

    def trackCB(self, *args):
        self.tumblebutton.set_active(False)
        self.dollybutton.set_active(False)
        self.selectbutton.set_active(False)

    def trackReleaseCB(self, *args):
        self.trackbutton.set_active(True)
        self.gfxwindow.setMouseHandler(self.trackHandler)

    def fillCB(self, *args):
        self.gfxwindow.oofcanvas.dollyfill()
        self.gfxwindow.oofcanvas.setSampleDistances()
        self.gfxwindow.current_toolbox.updateview()





## class SelectMouseHandler(mousehandler.MouseHandler):
##     def __init__(self, gfxwindow):
##         self.gfxwindow = gfxwindow

##     def up(self, x, y, shift, ctrl):
##         print "select voxel at",x,y

##     def acceptEvent(self, eventtype):
##         return eventtype == "up"    


class ViewManipulatorMouseHandler(mousehandler.MouseHandler):
    def __init__(self, gfxwindow):
        self.gfxwindow = gfxwindow
        self.downed = 0

    def up(self, x, y, shift, ctrl):
        self.downed = 0
        self.gfxwindow.oofcanvas._RenderWindow.SetDesiredUpdateRate(self.gfxwindow.oofcanvas._StillUpdateRate)
        self.gfxwindow.current_toolbox.updateview()

    def down(self, x, y, shift, ctrl):
        self.downed = 1
        self.gfxwindow.oofcanvas._RenderWindow.SetDesiredUpdateRate(self.gfxwindow.oofcanvas._DesiredUpdateRate)
        self.gfxwindow.oofcanvas.updateXY(x,y)

    def acceptEvent(self, eventtype):
        return eventtype=='down' or \
               (self.downed and eventtype in ('move', 'up'))


class TumbleMouseHandler(ViewManipulatorMouseHandler):

    def up(self, x, y, shift, ctrl):
        toolboxGUI.clippingadj.set_value(100)
        ViewManipulatorMouseHandler.up(self,x,y,shift,ctrl)

    def move(self, x, y, shift, ctrl):
        self.gfxwindow.oofcanvas.mouseTumble(x,y)
        toolboxGUI.clippingadj.set_value(100)
        self.gfxwindow.current_toolbox.updateview()


class DollyMouseHandler(ViewManipulatorMouseHandler):

    def move(self, x, y, shift, ctrl):
        self.gfxwindow.oofcanvas.mouseDolly(x,y)
        self.gfxwindow.current_toolbox.updateview()

    def up(self, x, y, shift, ctrl):
        self.gfxwindow.oofcanvas.setSampleDistances()
        ViewManipulatorMouseHandler.up(self,x,y,shift,ctrl)
        

class TrackMouseHandler(ViewManipulatorMouseHandler):

    def move(self, x, y, shift, ctrl):
        self.gfxwindow.oofcanvas.mouseTrack(x,y)
        self.gfxwindow.current_toolbox.updateview()






