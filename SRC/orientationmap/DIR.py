# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

dirname = 'orientationmap'

clib = 'oof2orientmap'
clib_order = 10

cfiles = [
    'orientmapdata.C', 'orientmapproperty.C', 'polefigure.C',
    'pixelselectioncouriero.C', 'pixeldifferentiatoro.C']

swigfiles = [
    'orientmapdata.swg', 'orientmapproperty.swg', 'polefigure.swg',
    'pixelselectioncouriero.swg', 'pixeldifferentiatoro.swg']

pyfiles = [
    'hkl.py', 'tsl.py', 'genericreader.py',
    'initialize.py', 'orientmapdisplay.py', 'pixelselectionmod.py',
    'orientmapmenu.py', 'orientmapIO.py', 'pixelinfoplugin.py']

swigpyfiles = [
    'orientmapdata.spy', 'orientmapproperty.spy', 'polefigure.spy',
    'pixeldifferentiatoro.spy']

hfiles = [
    'orientmapdata.h', 'orientmapproperty.h', 'polefigure.h',
    'pixelselectioncouriero.h', 'pixeldifferentiatoro.h']

def set_clib_flags(c_lib):
    import oof2setuputils
    oof2setuputils.pkg_check("oofcanvas", OOFCANVAS_VERSION, c_lib)
    addOOFlibs(c_lib, 'oof2common')

if not NO_GUI:
    subdirs = ['GUI']

