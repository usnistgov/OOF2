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
    'orientmapdata.C', 'orientmapproperty.C', 'polefigure.C', 'burn.C']

swigfiles = [
    'orientmapdata.swg', 'orientmapproperty.swg', 'polefigure.swg', 'burn.swg']

pyfiles = [
    'hkl.py', 'tsl.py', 'genericreader.py', 
    'initialize.py', 'orientmapdisplay.py',
    'orientmapmenu.py', 'orientmapIO.py']

swigpyfiles = [
    'orientmapdata.spy', 'orientmapproperty.spy', 'polefigure.spy', 'burn.spy']

hfiles = [
    'orientmapdata.h', 'orientmapproperty.h', 'polefigure.h', 'burn.h']

def set_clib_flags(c_lib):
    import oof2setuputils
    # if oof2setuputils.check_exec('Magick++-config'):
    #     oof2setuputils.add_third_party_includes('Magick++-config --cppflags',
    #                                             c_lib)
    #     oof2setuputils.add_third_party_libs('Magick++-config --ldflags --libs',
    #                                         c_lib)
    # else:
    #     print "Can't find Magick++-config!  Your ImageMagick installation may be defective."
    oof2setuputils.pkg_check("Magick++", MAGICK_VERSION, c_lib)
    c_lib.externalLibs.append('oof2common')


if not NO_GUI:
    subdirs = ['GUI']
