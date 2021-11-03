# -*- python -*- 

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

dirname = 'GUI'
clib = 'oof2commonGUI'
clib_order = 100

pyfiles = [
    'activeareaPage.py',
    'activityViewer.py',
    'canvasoutput.py',
    'chooser.py',
    'colorparamwidgets.py',
    'console.py',
    'displaymethodwidget.py',
##    'fakecanvas.py',
    'fileselector.py',
    'fontselector.py',
    'genericselectGUI.py',
    'gfxLabelTree.py',
    'gfxmenu.py',
    'gfxwindow.py',
    'gtklogger.py',
    'gtkutils.py',
    'guilogger.py',
    'historian.py',
    'initialize.py',
    'introPage.py',
    'labelledslider.py',
    'mainmenuGUI.py',
    'mainthreadGUI.py',
    'matrixparamwidgets.py',
    'microstructurePage.py',
    'mousehandler.py',
    'oofGUI.py',
    'parameterwidgets.py',
    'pixelPage.py',
    'pixeldifferentiatorwidget.py',
    'pixelgroupwidget.py',
    'pixelinfoGUI.py',
    'pixelselecttoolboxGUI.py',
    'progressbarGUI.py',
    'questioner.py',
    'quit.py',
    'regclassfactory.py',
    'reporter_GUI.py',
    'subWindow.py',
    'toolboxGUI.py',
    'tooltips.py',
    'tutorialsGUI.py',
    'viewertoolboxGUI.py',
    'whowidget.py',
    'widgetscope.py',
    'workerGUI.py'
 ]

cfiles = ['progressGUI.C', 'rubberband.C', 'gfxbrushstyle.C']

hfiles = ['progressGUI.h', 'rubberband.h', 'gfxbrushstyle.h']

swigfiles = ['progressGUI.swg', 'rubberband.swg', 'gfxbrushstyle.swg']

swigpyfiles = ['progressGUI.spy', 'gfxbrushstyle.spy']


def set_clib_flags(clib):
    import oof2setuputils
    oof2setuputils.pkg_check("gtk+-3.0", GTK_VERSION, clib)
    oof2setuputils.pkg_check("oofcanvas", OOFCANVAS_VERSION, clib)
    addOOFlibs(clib, 'oof2common')
