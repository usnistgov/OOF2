# -*- python -*- 

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

dirname = 'IO'
clib = 'oof2common'
if not NO_GUI:
    subdirs = ['OOFCANVAS', 'GUI']

cfiles = ['bitoverlay.C']

swigfiles = ['bitoverlay.swg']

pyfiles = ['activeareamodmenu.py', 'automatic.py', 'binarydata.py',
'bitmapdisplay.py', 'bitoverlaydisplay.py', 'colordiffparameter.py',
'colormap.py', 'datafile.py', 'display.py',
'genericselecttoolbox.py', 'gfxmanager.py', 'ghostgfxwindow.py',
'layereditor.py', 'mainmenu.py', 'menudump.py', 'menuparser.py',
'microstructureIO.py',
'microstructuremenu.py', 'oofmenu.py', 'outputdevice.py',
'parameter.py', 'pixelgroupmenu.py',
'pixelgroupparam.py', 'pixelinfo.py', 'pixelinfodisplay.py',
'pixelselectionmenu.py', 'pixelselectiontoolbox.py',
'progressbar_delay.py', 'pdfoutput.py', 'questioner.py', 'reporter.py',
'reportermenu.py', 'scriptloader.py', 'placeholder.py',
'socket2me.py', 'threadmanager.py', 'activityviewermenu.py',
'topwho.py', 'typename.py', 'viewertoolbox.py', 'whoville.py',
'words.py', 'reporterIO.py', 'xmlmenudump.py', 'automaticdoc.py',
'activeareamenu.py']

swigpyfiles = ['bitoverlay.spy']

hfiles = ['bitoverlay.h']

if HAVE_MPI:
    pyfiles.extend(['parallelmainmenu.py', 'microstructureIPC.py',
                    'pixelgroupIPC.py'])


def set_clib_flags(clib):
    import oof2setuputils
    oof2setuputils.pkg_check("cairomm-1.0", CAIROMM_VERSION, clib)
    oof2setuputils.pkg_check("gtk+-3.0", GTK_VERSION, clib)
    oof2setuputils.pkg_check("pango", PANGO_VERSION, clib)
    oof2setuputils.pkg_check("pangocairo", PANGOCAIRO_VERSION, clib)
    clib.extra_compile_args.extend(["-DOOFCANVAS_USE_PYTHON",
                                    "-DOOFCANVAS_USE_IMAGEMAGICK"])
