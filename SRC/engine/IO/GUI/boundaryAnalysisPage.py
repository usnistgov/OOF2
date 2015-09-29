# -*- python -*-
# $RCSfile: boundaryAnalysisPage.py,v $
# $Revision: 1.35 $
# $Author: langer $
# $Date: 2011/04/08 17:58:51 $


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
import gtk

class BoundaryAnalysisPage(analyzePage.BaseAnalysisPage):
    def __init__(self):
        self.built = False
        oofGUI.MainPage.__init__(self, name="Boundary Analysis",
                                 ordering=271,
                                 tip="Examine the boundaries of the system.")

        self.timeparam = placeholder.TimeParameter('time', value=0.0)

        mainbox = gtk.VBox(spacing=2)
        self.gtk.add(mainbox)

        align = gtk.Alignment(xalign=0.5)
        mainbox.pack_start(align, expand=0, fill=0)
        centerbox = gtk.HBox(spacing=3)
        align.add(centerbox)
        self.meshwidget = whowidget.WhoWidget(ooflib.engine.mesh.meshes,
                                              callback=self.meshCB,
                                              scope=self)
        label = gtk.Label("Microstructure=")
        label.set_alignment(1.0, 0.5)
        centerbox.pack_start(label, expand=0, fill=0)
        centerbox.pack_start(self.meshwidget.gtk[0], expand=0, fill=0)
        label = gtk.Label("Skeleton=")
        label.set_alignment(1.0, 0.5)
        centerbox.pack_start(label, expand=0, fill=0)
        centerbox.pack_start(self.meshwidget.gtk[1], expand=0, fill=0)
        label = gtk.Label("Mesh=")
        label.set_alignment(1.0, 0.5)
        centerbox.pack_start(label, expand=0, fill=0)
        centerbox.pack_start(self.meshwidget.gtk[2], expand=0, fill=0)

        align = gtk.Alignment(xalign=0.5)
        mainbox.pack_start(align, expand=0, fill=0)
        centerbox = gtk.HBox(spacing=3)
        align.add(centerbox)
        self.timeWidget = self.timeparam.makeWidget(scope=self)
        centerbox.pack_start(gtk.Label("Time:"), expand=0, fill=0)
        centerbox.pack_start(self.timeWidget.gtk, expand=0, fill=0)

        mainpane = gtk.HPaned()
        gtklogger.setWidgetName(mainpane, 'Pane')
        mainbox.pack_start(mainpane, expand=1, fill=1)
        gtklogger.connect_passive(mainpane, 'notify::position')

        leftbox = gtk.VBox()
        mainpane.pack1(leftbox, resize=1, shrink=0) # ??

        boundarylistframe = gtk.Frame("Boundaries")
        gtklogger.setWidgetName(boundarylistframe, 'frame')
        boundarylistframe.set_shadow_type(gtk.SHADOW_IN)
        leftbox.pack_start(boundarylistframe, expand=1, fill=1)

        self.bdylist = chooser.ScrolledChooserListWidget(
            callback=self.boundarylistCB,
            dbcallback=self.doubleclickCB,
            autoselect=1,
            name="BoundaryList")
        boundarylistframe.add(self.bdylist.gtk)

        rightbox = gtk.VBox()
        mainpane.pack2(rightbox, resize=1, shrink=0) # ??

        analyzerframe = gtk.Frame("Boundary Operation")
        analyzerframe.set_shadow_type(gtk.SHADOW_IN)
        rightbox.pack_start(analyzerframe, expand=1, fill=1)
        self.analysisWidget = regclassfactory.RegisteredClassFactory(
            meshbdyanalysis.MeshBdyAnalyzer.registry,
            scope=self,
            name="BdyAnalyzerRCF")
        analyzerframe.add(self.analysisWidget.gtk)

        self.buildBottomRow(mainbox)
        # hbox2 = gtk.HBox(homogeneous=True)
        # namebox.pack_start(hbox2, expand=0, fill=0)

        # self.create_button = gtkutils.StockButton(gtk.STOCK_NEW, 'Create...')
        # hbox2.pack_start(self.create_button, expand=1, fill=1)
        # gtklogger.setWidgetName(self.create_button, 'Set')
        # gtklogger.connect(self.create_button, 'clicked', self.createCB)
        # tooltips.set_tooltip_text(
        #     self.create_button,
        #     "Assign a name to the current analysis operation,"
        #     " so that it can be retrieved later.")

        # self.retrieve_button = gtkutils.StockButton(gtk.STOCK_REFRESH,
        #                                             'Retrieve...')
        # hbox2.pack_start(self.retrieve_button, expand=1, fill=1)
        # gtklogger.connect(self.retrieve_button, 'clicked', self.retrieveCB)
        # tooltips.set_tooltip_text(self.retrieve_button,
        #                           'Retrieve a name analysis.')

        # hbox3 = gtk.HBox(homogeneous=True)
        # namebox.pack_start(hbox3, expand=0, fill=0)

        # self.savenamed_button = gtkutils.StockButton(gtk.STOCK_SAVE_AS,
        #                                              'Save...')
        # hbox3.pack_start(self.savenamed_button, expand=1, fill=1)
        # gtklogger.setWidgetName(self.savenamed_button, 'Save')
        # gtklogger.connect(self.savenamed_button, 'clicked', self.savenamedCB)
        # tooltips.set_tooltip_text(self.savenamed_button,
        #                      'Save definitions of named analyses to a file.')
        
        # self.delete_button = gtkutils.StockButton(gtk.STOCK_DELETE, 'Delete...')
        # hbox3.pack_start(self.delete_button, expand=1, fill=1)
        # gtklogger.setWidgetName(self.delete_button, 'Delete')
        # gtklogger.connect(self.delete_button, 'clicked', self.deleteCB)
        # tooltips.set_tooltip_text(self.delete_button,
        #                      "Delete a named analysis operation")
        
        # # Destination
        # destframe = gtk.Frame("Destination")
        # destframe.set_shadow_type(gtk.SHADOW_IN)
        # hbox.pack_start(destframe, expand=1, fill=1, padding=3)
        # destbox = gtk.HBox()
        # destframe.add(destbox)
        # self.destwidget = outputdestinationwidget.TextDestinationWidget(
        #     name="Destination", framed=False)
        # destbox.pack_start(self.destwidget.gtk, expand=1, fill=1, padding=2)
        
        # # Go button
        # self.gobutton = gtkutils.StockButton(gtk.STOCK_EXECUTE, "Go!")
        # gtklogger.setWidgetName(self.gobutton, 'Go')
        # gtklogger.connect(self.gobutton, "clicked", self.goCB)
        # tooltips.set_tooltip_text(self.gobutton,
        #                           "Send the output to the destination.")
        # hbox.pack_end(self.gobutton, expand=1, fill=1, padding=2)

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
        # self.create_button.set_sensitive(go_sensitive)
        # self.delete_button.set_sensitive(namedok)
        # self.retrieve_button.set_sensitive(namedok)
        # self.savenamed_button.set_sensitive(namedok)

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


