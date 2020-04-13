# -*- python -*-


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import labeltree
from ooflib.common import microstructure
from ooflib.common.IO import mainmenu
from ooflib.common.IO import placeholder
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import oofGUI
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import regclassfactory
from ooflib.common.IO.GUI import tooltips
from ooflib.common.IO.GUI import whowidget
from ooflib.engine import meshbdyanalysis
from ooflib.engine import namedanalysis
from ooflib.engine import skeletoncontext
from ooflib.engine.IO import meshbdymenu
from ooflib.engine.IO.GUI import analyzePage
from ooflib.engine.IO.GUI import outputdestinationwidget
import ooflib.engine.mesh

from gi.repository import Gtk

class BoundaryAnalysisPage(analyzePage.BaseAnalysisPage):
    def __init__(self):
        self.built = False
        oofGUI.MainPage.__init__(self, name="Boundary Analysis",
                                 ordering=271,
                                 tip="Examine the boundaries of the system.")

        self.timeparam = placeholder.TimeParameter('time', value=0.0)

        mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.gtk.add(mainbox)

        centerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2,
                            halign=Gtk.Align.CENTER)
        mainbox.pack_start(centerbox, expand=False, fill=False, padding=0)
        self.meshwidget = whowidget.WhoWidget(ooflib.engine.mesh.meshes,
                                              callback=self.meshCB,
                                              scope=self)
        label = Gtk.Label("Microstructure=", halign=Gtk.Align.END)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        centerbox.pack_start(self.meshwidget.gtk[0],
                             expand=False, fill=False, padding=0)
        label = Gtk.Label("Skeleton=", halign=Gtk.Align.END)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        centerbox.pack_start(self.meshwidget.gtk[1],
                             expand=False, fill=False, padding=0)
        label = Gtk.Label("Mesh=", halign=Gtk.Align.END)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        centerbox.pack_start(self.meshwidget.gtk[2],
                             expand=False, fill=False, padding=0)

        centerbox = gtk.HBox(orientation=Gtk.Orientation.HORIZONTAL, spacing=2,
                             halign=Gtk.Align.CENTER)
        mainbox.pack_start(centerbox, expand=False, fill=False)
        self.timeWidget = self.timeparam.makeWidget(scope=self)
        centerbox.pack_start(Gtk.Label("Time:"),
                             expand=False, fill=False, padding=0)
        centerbox.pack_start(self.timeWidget.gtk,
                             expand=False, fill=False, padding=0)

        mainpane = Gtk.Paned(orientation.Gtk.Orientation.HORIZONTAL,
                             wide_handle=True)
        gtklogger.setWidgetName(mainpane, 'Pane')
        mainbox.pack_start(mainpane, expand=True, fill=True, padding=0)
        gtklogger.connect_passive(mainpane, 'notify::position')

        leftbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        mainpane.pack1(leftbox, resize=1, shrink=0) # ??

        boundarylistframe = gtk.Frame("Boundaries")
        gtklogger.setWidgetName(boundarylistframe, 'frame')
        boundarylistframe.set_shadow_type(gtk.SHADOW_IN)
        leftbox.pack_start(boundarylistframe, expand=True, fill=True)

        self.bdylist = chooser.ScrolledChooserListWidget(
            callback=self.boundarylistCB,
            dbcallback=self.doubleclickCB,
            autoselect=1,
            name="BoundaryList")
        boundarylistframe.add(self.bdylist.gtk)

        rightbox = gtk.VBox()
        mainpane.pack2(rightbox, resize=True, shrink=False) # ??

        analyzerframe = Gtk.Frame(label="Boundary Operation",
                                  shadow_type=Gtk.ShadowType.IN)
        rightbox.pack_start(analyzerframe, expand=True, fill=True, padding=0)
        self.analysisWidget = regclassfactory.RegisteredClassFactory(
            meshbdyanalysis.MeshBdyAnalyzer.registry,
            scope=self,
            name="BdyAnalyzerRCF")
        analyzerframe.add(self.analysisWidget.gtk)

        self.buildBottomRow(mainbox)
        self.built = True

        switchboard.requestCallbackMain(("new who", "Mesh"), self.newmeshCB)
        switchboard.requestCallbackMain(("new who", "Skeleton"), self.newskelCB)
        switchboard.requestCallbackMain(self.meshwidget, self.meshwidgetCB)
        switchboard.requestCallbackMain("mesh changed", self.meshchangedCB)
        switchboard.requestCallbackMain(self.analysisWidget,
                                        self.analysisWidgetCB)
        switchboard.requestCallbackMain("new boundary created", self.newbdyCB)
        switchboard.requestCallbackMain("boundary removed", self.newbdyCB)
        switchboard.requestCallbackMain("boundary renamed", self.newbdyCB)
        switchboard.requestCallbackMain("named boundary analyses changed",
                                        self.analysesChangedCB)
        switchboard.requestCallbackMain("retrieve boundary analysis",
                                        self.retrieve_analysis)
        switchboard.requestCallbackMain(('validity', self.timeWidget), 
                                        self.validityChangeCB)
        switchboard.requestCallbackMain("mesh status changed",
                                        self.meshchangedCB)

    menuWidgetName = 'BdyNamedOpsMenu'

    def installed(self):
        self.update()

    def currentFullMeshName(self):
        return self.meshwidget.get_value()
    def currentMeshContext(self):
        try:
            return ooflib.engine.mesh.meshes[self.currentFullMeshName()]
        except KeyError:
            return None
    def currentSkeletonPath(self):
        return self.meshwidget.get_value(depth=2)
    def currentSkeletonContext(self):
        try:
            return skeletoncontext.skeletonContexts[
                self.meshwidget.get_value(depth=2)]
        except KeyError:
            return None

        
    def currentMSName(self):
        path = labeltree.makePath(self.meshwidget.get_value(depth=1))
        if path:
            return path[0]
    def currentMS(self):
        msname = self.currentMSName()
        if msname:
            ms = microstructure.microStructures[msname].getObject()
            return ms

    def update(self):
        mesh = self.currentMeshContext()
        if mesh:
            bdynames = mesh.edgeBoundaryNames()
            self.bdylist.update(bdynames)
        else:
            self.bdylist.update([])
        self.sensitize()
        gtklogger.checkpoint("mesh bdy page updated")

    def validityChangeCB(self, validity):
        self.sensitize()
        
    def sensitize(self):
        debug.mainthreadTest()
        meshctxt = self.currentMeshContext()
        meshok = meshctxt and not meshctxt.outOfSync()
        go_sensitive = bool(meshok and
                            self.bdylist.get_value() is not None and
                            self.timeWidget.isValid() and
                            self.analysisWidget.isValid())
        self.go_button.set_sensitive(go_sensitive)
        namedok = len(namedanalysis.bdyAnalysisNames()) > 0
        self.sensitizeBottomRow(go_sensitive, namedok)

    def newmeshCB(self, meshpath):      # switchboard ("new who", "Mesh")
        self.meshwidget.set_value(meshpath)
        self.update()

    def newskelCB(self, skelpath):
        if not self.currentMeshContext():
            self.meshwidget.set_value(skelpath)
        
    def meshwidgetCB(self, interactive):
        self.update()
    def newbdyCB(self, skelctxt):
        if skelctxt.path() == self.currentSkeletonPath():
            self.update()

    def meshchangedCB(self, *args, **kwargs):
        self.sensitize()

    def go_buttonCB(self, gtkbutton):
        menuitem = mainmenu.OOF.Mesh.Boundary_Analysis.Analyze
        bdy = self.bdylist.get_value()
        if bdy:
            menuitem.callWithDefaults(mesh=self.currentFullMeshName(),
                                      time = self.timeWidget.get_value(),
                                      boundary=bdy,
                                      analyzer=self.analysisWidget.get_value(),
                                      destination=self.destwidget.get_value())

    def meshCB(self, meshpath):
        self.update()

    def boundarylistCB(self, obj, interactive):
        if self.built:
            self.sensitize()
            self.setNamedAnalysisChooser()
    def doubleclickCB(self, obj):
        if self.analysisWidget.isValid():
            self.sensitize()
            self.go_buttonCB(obj)

    def analysisWidgetCB(self, *args):
        self.setNamedAnalysisChooser()
        self.sensitize()

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    def analysesChangedCB(self):
        self.setNamedAnalysisChooser()

    def setNamedAnalysisChooser(self, *args):
        if self.suppressRetrievalLoop:
            return
        self.namedAnalysisChooser.update(['']
                                         + namedanalysis.bdyAnalysisNames())
        
        try:
            currentname = namedanalysis.findNamedBdyAnalysis(
                self.bdylist.get_value(),
                self.analysisWidget.get_value())
        except Exception, exc:
            currentname = ""
        self.namedAnalysisChooser.set_state(currentname)
        gtklogger.checkpoint("named boundary analysis chooser set")

    def createCB(self, gtkobj): # create a named analysis
        menuitem = meshbdymenu.bdyanalysismenu.Create
        if parameterwidgets.getParameters(menuitem.get_arg('name'),
                                          title='Name an analysis operation',
                                          scope=self):
            menuitem.callWithDefaults(
                boundary=self.bdylist.get_value(),
                analyzer=self.analysisWidget.get_value())

    def deleteCB(self, gtkobj):
        menuitem = meshbdymenu.bdyanalysismenu.Delete
        if parameterwidgets.getParameters(
            menuitem.get_arg('name'),
            title='Delete a named boundary analysis',
            scope=self):
            menuitem.callWithDefaults()

    def retrieveCB(self, gtkobj, name):
        if name:
            menuitem = meshbdymenu.bdyanalysismenu.RetrieveNamedAnalysis
            menuitem.get_arg('name').value = name
            menuitem.callWithDefaults()

    def retrieve_analysis(self, name): # sb "retrieve boundary analysis"
        analysis = namedanalysis.getNamedBdyAnalysis(name)
        self.suppressRetrievalLoop = True
        try:
            self.bdylist.set_selection(analysis.boundary)
            self.analysisWidget.set(analysis.analyzer, interactive=False)
        finally:
            self.suppressRetrievalLoop = False
        gtklogger.checkpoint("retrieved named boundary analysis")
        self.setNamedAnalysisChooser()
        
        
    def savenamedCB(self, gtkobj):
        menuitem = meshbdymenu.bdyanalysismenu.SaveAnalysisDefs
        if parameterwidgets.getParameters(
            title="Save Boundary Analysis Definitions",
            ident="SaveAnalysis",
            *menuitem.params):
            menuitem.callWithDefaults()

boundaryAnalysisPage = BoundaryAnalysisPage()


