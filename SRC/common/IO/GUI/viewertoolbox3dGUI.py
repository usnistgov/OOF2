# -*- python -*-
# $RCSfile: viewertoolbox3dGUI.py,v $
# $Revision: 1.7 $
# $Author: langer $
# $Date: 2010/06/02 20:25:30 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 


from ooflib.SWIG.common import guitop
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common import primitives
from ooflib.common.IO import reporter
from ooflib.common.IO import viewertoolbox
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import mousehandler
from ooflib.common.IO.GUI import oofcanvas3d
from ooflib.common.IO.GUI import toolboxGUI
from ooflib.common.IO.GUI import tooltips
from ooflib.common.IO.mainmenu import OOF
import gobject
import gtk
import math

ndigits = 10



class ViewerToolbox3DGUI(toolboxGUI.GfxToolbox, mousehandler.MouseHandler):
    def __init__(self, viewertoolbox):
        debug.mainthreadTest()

        toolboxGUI.GfxToolbox.__init__(self, "Viewer", viewertoolbox)
        mainbox = gtk.VBox()
        self.gtk.add(mainbox)

        # camera position
        infoframe = gtk.Frame("Camera Info")
        infoframe.set_shadow_type(gtk.SHADOW_IN)
        mainbox.pack_start(infoframe, fill=0, expand=0)

        infobox = gtk.VBox()
        infoframe.add(infobox)
        positionlabel = gtk.Label("Camera Position:")
        infobox.pack_start(positionlabel,fill=0, expand=0)
        positiontable = gtk.Table(columns=3, rows=1)
        infobox.pack_start(positiontable,fill=0, expand=0)
        self.camera_x = gtk.Entry()
        gtklogger.setWidgetName(self.camera_x, "CameraX")
        self.camera_x.set_size_request(ndigits*guitop.top().digitsize, -1)
        self.camera_x.set_editable(0)
        positiontable.attach(self.camera_x,0,1,0,1)
        self.camera_y = gtk.Entry()
        gtklogger.setWidgetName(self.camera_y, "CameraY")
        self.camera_y.set_size_request(ndigits*guitop.top().digitsize, -1)
        self.camera_y.set_editable(0)
        positiontable.attach(self.camera_y,1,2,0,1)
        self.camera_z = gtk.Entry()
        gtklogger.setWidgetName(self.camera_z, "CameraZ")
        self.camera_z.set_size_request(ndigits*guitop.top().digitsize, -1)
        self.camera_z.set_editable(0)
        positiontable.attach(self.camera_z,2,3,0,1)
        focalpointlabel = gtk.Label("Focal Point:")
        infobox.pack_start(focalpointlabel,fill=0, expand=0)
        focalpointtable = gtk.Table(columns=3, rows=1)
        infobox.pack_start(focalpointtable,fill=0, expand=0)
        self.fp_x = gtk.Entry()
        gtklogger.setWidgetName(self.fp_x, "FocalX")
        self.fp_x.set_size_request(ndigits*guitop.top().digitsize, -1)
        self.fp_x.set_editable(0)
        focalpointtable.attach(self.fp_x,0,1,0,1)
        self.fp_y = gtk.Entry()
        gtklogger.setWidgetName(self.fp_y, "FocalY")
        self.fp_y.set_size_request(ndigits*guitop.top().digitsize, -1)
        self.fp_y.set_editable(0)
        focalpointtable.attach(self.fp_y,1,2,0,1)
        self.fp_z = gtk.Entry()
        gtklogger.setWidgetName(self.fp_z, "FocalZ")
        self.fp_z.set_size_request(ndigits*guitop.top().digitsize, -1)
        self.fp_z.set_editable(0)
        focalpointtable.attach(self.fp_z,2,3,0,1)
        viewuplabel = gtk.Label("View Up Vector:")
        infobox.pack_start(viewuplabel,fill=0, expand=0)
        viewuptable = gtk.Table(columns=3, rows=1)
        infobox.pack_start(viewuptable,fill=0, expand=0)
        self.viewup_x = gtk.Entry()
        gtklogger.setWidgetName(self.viewup_x, "ViewUpX")
        self.viewup_x.set_size_request(ndigits*guitop.top().digitsize, -1)
        self.viewup_x.set_editable(0)
        viewuptable.attach(self.viewup_x,0,1,0,1)
        self.viewup_y = gtk.Entry()
        gtklogger.setWidgetName(self.viewup_y, "ViewUpY")
        self.viewup_y.set_size_request(ndigits*guitop.top().digitsize, -1)
        self.viewup_y.set_editable(0)
        viewuptable.attach(self.viewup_y,1,2,0,1)
        self.viewup_z = gtk.Entry()
        gtklogger.setWidgetName(self.viewup_z, "ViewUpZ")
        self.viewup_z.set_size_request(ndigits*guitop.top().digitsize, -1)
        self.viewup_z.set_editable(0)
        viewuptable.attach(self.viewup_z,2,3,0,1)
        distancetable = gtk.Table(columns=2, rows=1)
        infobox.pack_start(distancetable,fill=0, expand=0)
        distancelabel = gtk.Label("Distance:")
        distancetable.attach(distancelabel,0,1,0,1)
        self.distance = gtk.Entry()
        gtklogger.setWidgetName(self.distance, "Distance")
        self.distance.set_size_request(ndigits*guitop.top().digitsize, -1)
        self.distance.set_editable(0)
        distancetable.attach(self.distance,1,2,0,1)
        angletable = gtk.Table(columns=2, rows=1)
        infobox.pack_start(angletable,fill=0, expand=0)
        anglelabel = gtk.Label("View Angle:")
        angletable.attach(anglelabel,0,1,0,1)
        self.viewangle = gtk.Entry()
        gtklogger.setWidgetName(self.viewangle, "ViewAngle")
        self.viewangle.set_size_request(ndigits*guitop.top().digitsize, -1)
        self.viewangle.set_editable(0)
        angletable.attach(self.viewangle,1,2,0,1)
        camerainfo = gtkutils.StockButton(gtk.STOCK_DIALOG_INFO, "Camera Info")
        gtklogger.connect(camerainfo, 'clicked', self.camera_infoCB)
        tooltips.set_tooltip_text(camerainfo,
            "Display camera information in the message window.")
        infobox.pack_start(camerainfo,fill=0, expand=0)


        # TODO: Do we want to be able to zoom?  As in changing the
        # viewing angle?

        # Translation

        # dolly
        transframe = gtk.Frame("Translation")
        gtklogger.setWidgetName(transframe, "Translation")
        transframe.set_shadow_type(gtk.SHADOW_IN)
        mainbox.pack_start(transframe, fill=0, expand=0)
        transbox = gtk.VBox()
        transframe.add(transbox)
        dollyrow = gtk.HBox(homogeneous=1, spacing=2)
        transbox.pack_start(dollyrow, expand=0, fill=1, padding=2)
        inbutton = gtk.Button('Dolly In')
        gtklogger.setWidgetName(inbutton, 'DollyIn')
        tooltips.set_tooltip_text(inbutton,
            "Translate camera towards focal point by given factor")
        dollyrow.pack_start(inbutton, expand=0, fill=1)
        gtklogger.connect(inbutton, 'clicked', self.dollyin)
        outbutton = gtk.Button('Dolly Out')
        gtklogger.setWidgetName(outbutton, 'DollyOut')
        tooltips.set_tooltip_text(outbutton,
            "Translate camera away from focal point by given factor")
        dollyrow.pack_start(outbutton, expand=0, fill=1)
        gtklogger.connect(outbutton, 'clicked', self.dollyout)
        fillbutton = gtk.Button('Fill')
        gtklogger.setWidgetName(fillbutton,'Fill')
        tooltips.set_tooltip_text(fillbutton,
            "Set camera position such that microstructure approximately fills viewport")
        dollyrow.pack_start(fillbutton, expand=0, fill=1)
        gtklogger.connect(fillbutton, 'clicked', self.dollyfill)
        factorrow = gtk.HBox()
        transbox.pack_start(factorrow, expand=0, fill=0, padding=2)
        factorrow.pack_start(gtk.Label("Factor: "), expand=0, fill=0)
        self.dollyfactor = gtk.Entry()
        self.dollyfactor.set_editable(1)
        self.dollyfactor.set_size_request(ndigits*guitop.top().digitsize, -1)
        gtklogger.setWidgetName(self.dollyfactor, "DollyFactor")
        self.dollyfactor.set_text("1.5")
        tooltips.set_tooltip_text(self.dollyfactor,
            "Factor by which to multiply distance from camera to focal point")
        factorrow.pack_start(self.dollyfactor, expand=1, fill=1)

        # track
        trackrow = gtk.HBox(homogeneous=1, spacing=2)
        transbox.pack_start(trackrow, expand=0, fill=1, padding=2)
        horizbutton = gtk.Button('Horizontal')
        tooltips.set_tooltip_text(horizbutton,
            "Shift camera and focal point horizontally")
        trackrow.pack_start(horizbutton, expand=0, fill=1)
        gtklogger.connect(horizbutton, 'clicked', self.trackh)
        vertbutton = gtk.Button('Vertical')
        tooltips.set_tooltip_text(vertbutton,"Shift camera and focal point vertically")
        trackrow.pack_start(vertbutton, expand=0, fill=1)
        gtklogger.connect(vertbutton, 'clicked', self.trackv)
        recenterbutton = gtk.Button('Recenter')
        tooltips.set_tooltip_text(recenterbutton,"Recenter the microstructure in the viewport")
        trackrow.pack_start(recenterbutton, expand=0, fill=1)
        gtklogger.connect(recenterbutton, 'clicked', self.recenter)        
        distrow = gtk.HBox()
        transbox.pack_start(distrow, expand=0, fill=0, padding=2)
        distrow.pack_start(gtk.Label("Distance: "), expand=0, fill=0)
        self.trackdist = gtk.Entry()
        self.trackdist.set_editable(1)
        self.trackdist.set_size_request(ndigits*guitop.top().digitsize, -1)
        self.trackdist.set_text("10.0")
        tooltips.set_tooltip_text(self.trackdist,"Distance by which to track camera in units of pixels")
        distrow.pack_start(self.trackdist, expand=1, fill=1)


        #rotate
        rotateframe = gtk.Frame("Rotation")
        rotateframe.set_shadow_type(gtk.SHADOW_IN)
        mainbox.pack_start(rotateframe, fill=0, expand=0)
        rotatebox = gtk.VBox()
        rotateframe.add(rotatebox)
        rotrow1 = gtk.HBox(homogeneous=1, spacing=2)
        rotatebox.pack_start(rotrow1, expand=0, fill=1, padding=2)
        rollbutton = gtk.Button('Roll')
        tooltips.set_tooltip_text(rollbutton,"Rotate about direction of projection")
        rotrow1.pack_start(rollbutton, expand=0, fill=1)
        gtklogger.connect(rollbutton, 'clicked', self.roll)
        pitchbutton = gtk.Button('Pitch')
        tooltips.set_tooltip_text(pitchbutton,"Rotate about cross product of direction of projection and view up vector centered at camera position")
        rotrow1.pack_start(pitchbutton, expand=0, fill=1)
        gtklogger.connect(pitchbutton, 'clicked', self.pitch)
        yawbutton = gtk.Button('Yaw')
        tooltips.set_tooltip_text(yawbutton,"Rotate about view up vector centered at camera position")
        rotrow1.pack_start(yawbutton, expand=0, fill=1)
        gtklogger.connect(yawbutton, 'clicked', self.yaw)
        rotrow2 = gtk.HBox(homogeneous=1, spacing=2)
        rotatebox.pack_start(rotrow2, expand=0, fill=1, padding=2)
        azbutton = gtk.Button('Azimuth')
        tooltips.set_tooltip_text(azbutton,"Rotate about view up vector centered at focal point")
        rotrow2.pack_start(azbutton, expand=0, fill=1)
        gtklogger.connect(azbutton, 'clicked', self.azimuth)
        elbutton = gtk.Button('Elevation')
        tooltips.set_tooltip_text(elbutton,"Rotate about cross product of direction of projection and view up vector centered at focal point")
        rotrow2.pack_start(elbutton, expand=0, fill=1)
        gtklogger.connect(elbutton, 'clicked', self.elevation)
        anglerow = gtk.HBox()
        rotatebox.pack_start(anglerow, expand=0, fill=0, padding=2)
        anglerow.pack_start(gtk.Label("Angle: "), expand=0, fill=0)
        self.angle = gtk.Entry()
        self.angle.set_editable(1)
        self.angle.set_size_request(ndigits*guitop.top().digitsize, -1)
        self.angle.set_text("10.0")
        tooltips.set_tooltip_text(self.angle,"Angle in degrees by which to rotate by")
        anglerow.pack_start(self.angle, expand=1, fill=1)

        #clipping planes
        clippingframe = gtk.Frame("Clipping Range")
        clippingframe.set_shadow_type(gtk.SHADOW_IN)
        mainbox.pack_start(clippingframe, fill=0, expand=0)
        clippingbox = gtk.VBox()
        clippingframe.add(clippingbox)
        #self.clippingadj = gtk.Adjustment(value=100, lower=0, upper=100, step_incr=-1, page_incr=-5, page_size=0)
        gtklogger.connect(toolboxGUI.clippingadj, 'value_changed', self.updateview)
        clippingscale = gtk.HScale(toolboxGUI.clippingadj)
        clippingscale.set_update_policy(gtk.UPDATE_DELAYED)
        tooltips.set_tooltip_text(clippingscale,"Adjust the near clipping plane to view cross section")
        clippingbox.pack_start(clippingscale)

        # save and restore
        saverestoreframe = gtk.Frame("Save and Restore Views")
        saverestoreframe.set_shadow_type(gtk.SHADOW_IN)
        mainbox.pack_start(saverestoreframe, fill=0, expand=0)
        saverestorebox = gtk.VBox()
        saverestoreframe.add(saverestorebox)
        viewtable = gtk.Table(columns=2, rows=2)
        saverestorebox.pack_start(viewtable, fill=0, expand=0)
        saveviewbutton = gtk.Button("Save View:")
        tooltips.set_tooltip_text(saveviewbutton,"Save the current view settings")
        gtklogger.connect(saveviewbutton, 'clicked', self.saveview)
        viewtable.attach(saveviewbutton, 0,1,0,1)
        self.viewname = gtk.Entry()
        self.viewname.set_editable(1)
        self.viewname.set_size_request(ndigits*guitop.top().digitsize,-1)
        tooltips.set_tooltip_text(self.viewname,"Enter a name for the current view")
        viewtable.attach(self.viewname,1,2,0,1)
        setviewlabel = gtk.Label("Set View:")
        viewtable.attach(setviewlabel, 0,1,1,2)
        liststore = gtk.ListStore(gobject.TYPE_STRING)
        self.viewmenu = gtk.ComboBox(liststore)
        cell = gtk.CellRendererText()
        self.viewmenu.pack_start(cell, True)
        self.viewmenu.add_attribute(cell, 'text', 0)
        #tooltips.set_tooltip_text(self.viewmenu,"Restore a saved view")
        # menu items filled in later when saved_views is initialized
        self.signal = gtklogger.connect(self.viewmenu, 'changed',
                                        self.setview)
        viewtable.attach(self.viewmenu, 1,2,1,2)

        self.SetDefaultViews()

        # position information
        voxelinfoframe = gtk.Frame("Voxel Info")
        voxelinfoframe.set_shadow_type(gtk.SHADOW_IN)
        mainbox.pack_start(voxelinfoframe)
        voxelinfobox = gtk.VBox()
        voxelinfoframe.add(voxelinfobox)
        voxelinfotable = gtk.Table(rows=3,columns=2)
        voxelinfobox.pack_start(voxelinfotable)
        label = gtk.Label('x=')
        label.set_alignment(1.0, 0.5)
        voxelinfotable.attach(label, 0,1, 0,1, xpadding=5, xoptions=gtk.FILL)
        self.xtext = gtk.Entry()
        self.xtext.set_size_request(ndigits*guitop.top().digitsize, -1)
        voxelinfotable.attach(self.xtext, 1,2, 0,1,
                          xpadding=5, xoptions=gtk.EXPAND|gtk.FILL)
        label = gtk.Label('y=')
        label.set_alignment(1.0, 0.5)
        voxelinfotable.attach(label, 0,1, 1,2, xpadding=5, xoptions=gtk.FILL)
        self.ytext = gtk.Entry()
        self.ytext.set_size_request(ndigits*guitop.top().digitsize, -1)
        voxelinfotable.attach(self.ytext, 1,2, 1,2,
                          xpadding=5, xoptions=gtk.EXPAND|gtk.FILL)
        label = gtk.Label('z=')
        label.set_alignment(1.0, 0.5)
        voxelinfotable.attach(label, 0,1, 2,3, xpadding=5, xoptions=gtk.FILL)
        self.ztext = gtk.Entry()
        self.ztext.set_size_request(ndigits*guitop.top().digitsize, -1)
        voxelinfotable.attach(self.ztext, 1,2, 2,3,
                          xpadding=5, xoptions=gtk.EXPAND|gtk.FILL)




    def activate(self):
        toolboxGUI.GfxToolbox.activate(self)
        self.gfxwindow().setMouseHandler(self)
        self.gfxwindow().toolbar.setSelect()


    def camera_infoCB(self, *args):
        debug.mainthreadTest()
        camera = self.gfxwindow().oofcanvas.getCamera()
        reporter.report(camera)
        

    def updateCameraInfo(self):
        # TODO: where should this be called???
        debug.mainthreadTest()
        camera = self.gfxwindow().oofcanvas.getCamera()
        x,y,z = camera.GetPosition()
        self.camera_x.set_text("%f" %x)
        self.camera_y.set_text("%f" %y)
        self.camera_z.set_text("%f" %z)        
        x,y,z = camera.GetFocalPoint()
        self.fp_x.set_text("%f" %x)
        self.fp_y.set_text("%f" %y)
        self.fp_z.set_text("%f" %z)
        x,y,z = camera.GetViewUp()
        self.viewup_x.set_text("%f" %x)
        self.viewup_y.set_text("%f" %y)
        self.viewup_z.set_text("%f" %z)
        dist = camera.GetDistance()
        self.distance.set_text("%f" %dist)
        angle = camera.GetViewAngle()
        self.viewangle.set_text("%f" %angle)


    def updateview(self, *args):
        toolboxGUI.GfxToolbox.updateview(self)
        self.updateCameraInfo()
        self.viewmenu.set_active(-1)


    # Translation callback functions
    ###########################################################

    def dollyin(self, *args):
        camera = self.gfxwindow().oofcanvas.getCamera()
        dollyfactor = float(self.dollyfactor.get_text())
        camera.Dolly(dollyfactor)
        self.gfxwindow().oofcanvas.setSampleDistances()
        self.updateview()


    def dollyout(self, *args):
        camera = self.gfxwindow().oofcanvas.getCamera()
        dollyfactor = 1./float(self.dollyfactor.get_text())
        camera.Dolly(dollyfactor)
        self.gfxwindow().oofcanvas.setSampleDistances()
        self.updateview()


    def dollyfill(self, *args):
        self.gfxwindow().oofcanvas.dollyfill()
        self.gfxwindow().oofcanvas.setSampleDistances()
        self.updateview()



    def trackh(self, *args):
        d = float(self.trackdist.get_text())
        camera = self.gfxwindow().oofcanvas.getCamera()
        # Get the normalized vector which is horizontal on the screen
        (yp0,yp1,yp2) = camera.GetViewUp()
        (zp0,zp1,zp2) = camera.GetDirectionOfProjection()
        xp0=-zp1*yp2+yp1*zp2
        xp1=-zp2*yp0+yp2*zp0
        xp2=-zp0*yp1+yp0*zp1

        self.gfxwindow().oofcanvas.track(xp0*d,xp1*d,xp2*d)
        self.updateview()


    def trackv(self, *args):
        camera = self.gfxwindow().oofcanvas.getCamera()
        d = float(self.trackdist.get_text())
        (yp0,yp1,yp2) = camera.GetViewUp()
        self.gfxwindow().oofcanvas.track(yp0*d,yp1*d,yp2*d)
        self.updateview()


    def recenter(self, *args):
        camera = self.gfxwindow().oofcanvas.getCamera()
        d = camera.GetDistance()
        dop = camera.GetDirectionOfProjection()
        (width, height, depth) = self.findMicrostructure().size()
        fp = (float(width)/2, float(height)/2, float(depth)/2)
        camera.SetFocalPoint(fp)
        camera.SetPosition(fp[0]-d*dop[0],fp[1]-d*dop[1],fp[2]-d*dop[2])
        self.updateview()


    # Rotation Callback Functions
    ##############################################################

    def roll(self, *args):
        camera = self.gfxwindow().oofcanvas.getCamera()
        angle = float(self.angle.get_text())
        camera.Roll(angle)
        toolboxGUI.clippingadj.set_value(100)
        self.updateview()

    def azimuth(self, *args):
        camera = self.gfxwindow().oofcanvas.getCamera()
        angle =  float(self.angle.get_text())
        camera.Azimuth(angle)
        toolboxGUI.clippingadj.set_value(100)
        self.updateview()
        
    def elevation(self, *args):
        camera = self.gfxwindow().oofcanvas.getCamera()
        angle =  float(self.angle.get_text())
        camera.Elevation(angle)
        toolboxGUI.clippingadj.set_value(100)
        self.updateview()

    def yaw(self, *args):
        camera = self.gfxwindow().oofcanvas.getCamera()
        angle =  float(self.angle.get_text())
        camera.Yaw(angle)
        toolboxGUI.clippingadj.set_value(100)
        self.updateview()

    def pitch(self, *args):
        camera = self.gfxwindow().oofcanvas.getCamera()
        angle =  float(self.angle.get_text())
        camera.Pitch(angle)
        toolboxGUI.clippingadj.set_value(100)
        self.updateview()

    # Save and Restore Views
    ############################################################

    def setview(self, *args):
        viewname = self.get_active_text(self.viewmenu)
        try:
            view = self.saved_views[viewname]
            self.gfxwindow().oofcanvas.set_view(view)
            toolboxGUI.clippingadj.set_value(view.clip)
            self.updateCameraInfo()

        except KeyError:
            pass


    def saveview(self, *args):
        viewname = self.viewname.get_text()

        self.saved_views[viewname]=self.gfxwindow().oofcanvas.get_view()
        self.viewmenu.append_text(viewname)

        
    def SetDefaultViews(self):
        # TODO 3D: this should be called somewhere else - if the
        # graphics window is opened before a microstructure is loaded,
        # this is empty.  Also, it should be reset whenever the
        # microstructure is changed.
        self.saved_views = {}
        camera = self.gfxwindow().oofcanvas.getCamera()
        ms = self.findMicrostructure()
        if ms is not None:
            (width, height, depth) = ms.size()
            distance = height*2.33253175 + depth/2
            # (height*1.25)/(2*tan(angle/2)) assuming an angle of 30
            center = (width/2, height/2, depth/2)
            y_up = (0,1,0)
            nz_up = (0,0,-1)
            pz_up = (0,0,1)

            self.saved_views["Front"]=oofcanvas3d.View( (width/2, height/2, distance+depth/2),
                                            center,y_up)
            self.saved_views["Back"]=oofcanvas3d.View( (width/2, height/2, -distance+depth/2),
                                           center,y_up)
            self.saved_views["Left"]=oofcanvas3d.View( (-distance+width/2, height/2, depth/2),
                                           center,y_up)
            self.saved_views["Right"]=oofcanvas3d.View( (distance+width/2, height/2, depth/2),
                                            center,y_up)
            self.saved_views["Top"]=oofcanvas3d.View( (width/2, distance+height/2, depth/2),
                                          center,nz_up)
            self.saved_views["Bottom"]=oofcanvas3d.View( (width/2, -distance+height/2, depth/2),
                                             center,pz_up)
            views = self.saved_views.keys()
            for view in views:
                self.viewmenu.append_text(view)

    def get_active_text(self, combobox):
        model = combobox.get_model()
        active = combobox.get_active()
        if active < 0:
            return None
        return model[active][0]



    # Mouse interactions
    ###############################################################
    def acceptEvent(self, eventtype):
        return eventtype == "up"

    def up(self, x, y, shift, ctrl):
        position = self.gfxwindow().oofcanvas.voxelInfo(x,y)
        if position is not None:
            self.xtext.set_text(str(position[0]))
            self.ytext.set_text(str(position[1]))
            self.ztext.set_text(str(position[2]))

    ##############################################################

    def findMicrostructure(self):
        who = self.toolbox.gfxwindow().topwho('Microstructure', 'Image',
                                              'Skeleton', 'Mesh')
        if who is not None:
            return who.getMicrostructure()


def _makeGUI(self):
    return ViewerToolbox3DGUI(self)

viewertoolbox.ViewerToolbox.makeGUI = _makeGUI
    
