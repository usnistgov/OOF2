# -*- python -*- 

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

dirname = 'image'
clib = 'oof2image'
clib_order = 2

subdirs = ['IO']
if ENABLE_SEGMENTATION:
    subdirs.append('SEGMENTATION')

cfiles = ['oofimage.C', 'burn.C', 'evenlyilluminate.C',
          'pixelselectioncourieri.C', 'autogroupMP.C',
          'autograin.C']

swigfiles = ['oofimage.swg', 'pixelselectioncourieri.swg',
             'autogroupMP.swg', 'autograin.swg']

swigpyfiles = ['oofimage.spy', 'burn.spy', 'autograin.spy']


hfiles = ['oofimage.h', 'burn.h', 'pixelselectioncourieri.h',
          'autogroupMP.h', 'autograin.h']

pyfiles = ['initialize.py', 'pixelselectionmethod.py',
           'pixelselectionmod.py', 'imagemodifier.py']



def set_clib_flags(c_lib):
    import oof2setuputils
    # if oof2setuputils.check_exec('Magick++-config'):
    #     # Hack. Check that ImageMagick is really installed, not
    #     # GraphicsMagick.
    #     f = os.popen('Magick++-config --libs', 'r')
    #     line = f.readline()
    #     if 'GraphicsMagick' in line:
    #         print "You seem to be using GraphicsMagick instead of ImageMagick.  OOF2 cannot use GraphicsMagick."
    #         sys.exit()
    #     # Add ImageMagick headers and libs.

    #     oof2setuputils.add_third_party_includes(
    #         'Magick++-config --cppflags', c_lib)
    #     oof2setuputils.add_third_party_libs(
    #         'Magick++-config --ldflags --libs', c_lib)
    # else:
    #     print "Can't find Magick++-config!  Your ImageMagick installation may be defective."
    oof2setuputils.pkg_check("Magick++", MAGICK_VERSION, c_lib)
    c_lib.externalLibs.append('oof2common')
        



