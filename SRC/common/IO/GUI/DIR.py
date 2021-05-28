# -*- python -*- 


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

dirname = 'GUI'
if not DIM_3:
    clib = 'oof2commonGUI'
else:
    clib = 'oof3dcommonGUI'
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
    'fixedwidthtext.py',
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
    'layereditorGUI.py',
    'mainmenuGUI.py',
    'mainthreadGUI.py',
    'matrixparamwidgets.py',
    'microstructurePage.py',
    'mousehandler.py',
    'oofGUI.py',
    'oof_mainiteration.py',
    'parameterwidgets.py',
    'pixelPage.py',
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

cfiles = ['progressGUI.C']

hfiles = ['progressGUI.h']

swigfiles = ['progressGUI.swg']

swigpyfiles = ['progressGUI.spy']

if not DIM_3:

    cfiles += [
        'oofcanvas.C',
        'rubberband.C',
        'canvasdot.C',
        'canvastriangle.C',
        'gfxbrushstyle.C'
        ]

    swigfiles += [
        'oofcanvas.swg',
        'rubberband.swg',
        'gfxbrushstyle.swg'
        ]

    swigpyfiles += [
        'gfxbrushstyle.spy'
        ]

    hfiles += [
        'canvasdot.h',
        'canvastriangle.h',
        'oofcanvas.h',
        'rubberband.h',
        'rbstipple.xbm',
        'rbstubble.xbm',
        'gfxbrushstyle.h'
    ]




def set_clib_flags(clib):
    import oof2setuputils

    # # This is a hack that is needed by pkg-config on Macs using
    # # fink. After merging its pangocairo branch, fink isn't putting
    # # pango.pc and freetype2.pc in the default locations because they
    # # can cause conflicts.  Once fink completes upgrading to modern
    # # versions of these libraries, this hack can be removed.
    # oof2setuputils.extend_path("PKG_CONFIG_PATH",
    #                            "/sw/lib/pango-ft219/lib/pkgconfig",
    #                            "/sw/lib/freetype219/lib/pkgconfig/")

    addOOFlibs(clib, 'oof2common')
    oof2setuputils.pkg_check("gtk+-2.0", GTK_VERSION, clib)
    oof2setuputils.pkg_check("libgnomecanvas-2.0", GNOMECANVAS_VERSION, clib)
    oof2setuputils.pkg_check("pygtk-2.0", PYGTK_VERSION, clib)
    oof2setuputils.pkg_check("pygobject-2.0", PYGOBJECT_VERSION)

