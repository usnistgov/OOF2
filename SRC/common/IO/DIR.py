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
    subdirs = ['GUI']

cfiles = ['bitoverlay.C']

swigfiles = ['bitoverlay.swg']

pyfiles = [
    'activeareamenu.py', 'activeareamodmenu.py',
    'activityviewermenu.py', 'automatic.py', 'automaticdoc.py',
    'binarydata.py', 'bitmapdisplay.py', 'bitoverlaydisplay.py',
    'colordiffparameter.py', 'colormap.py', 'datafile.py',
    'display.py', 'genericselecttoolbox.py', 'gfxmanager.py',
    'ghostgfxwindow.py', 'mainmenu.py', 'menudump.py',
    'menuparser.py', 'microstructureIO.py', 'microstructuremenu.py',
    'oofmenu.py', 'parameter.py', 'pixelgroupmenu.py',
    'pixelgroupparam.py', 'pixelinfo.py', 'pixelinfodisplay.py',
    'pixelselectionmenu.py', 'pixelselectiontoolbox.py',
    'placeholder.py', 'progressbar_delay.py', 'questioner.py',
    'reporter.py', 'reporterIO.py', 'reportermenu.py',
    'scriptloader.py', 'socket2me.py', 'threadmanager.py',
    'topwho.py', 'typename.py', 'viewertoolbox.py', 'whoville.py',
    'words.py', 'xmlmenudump.py',
]

swigpyfiles = ['bitoverlay.spy']

hfiles = ['bitoverlay.h']

if HAVE_MPI:
    pyfiles.extend(['parallelmainmenu.py', 'microstructureIPC.py',
                    'pixelgroupIPC.py'])


def set_clib_flags(clib):
    import oof2setuputils
    oof2setuputils.pkg_check("gtk+-3.0", GTK_VERSION, clib)
    clib.externalLibs.append('oofcanvas')

    ## TODO GTK3:  This should really be
    ##  oof2setuputils.pkg_check("oofcanvas", 1.0, clib)
    ## which will add the compile and link flags for cairomm and others.
    oof2setuputils.pkg_check("cairomm-1.0", CAIROMM_VERSION, clib)
