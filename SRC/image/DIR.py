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

cfiles = ['oofimage.C', 'evenlyilluminate.C',
          'pixelselectioncourieri.C', 'autogroupMP.C',
          'pixeldifferentiator.C']

swigfiles = ['oofimage.swg', 'pixelselectioncourieri.swg',
             'autogroupMP.swg', 'pixeldifferentiator.swg']

swigpyfiles = ['oofimage.spy', 'pixeldifferentiator.spy']


hfiles = ['oofimage.h', 'pixelselectioncourieri.h',
          'autogroupMP.h', 'pixeldifferentiator.h']

pyfiles = ['initialize.py', 'pixelselectionmethod.py',
           'pixelselectionmod.py', 'imagemodifier.py']



def set_clib_flags(c_lib):
    import oof2setuputils
    oof2setuputils.pkg_check("Magick++", MAGICK_VERSION, c_lib)
    oof2setuputils.pkg_check("cairomm-1.0", CAIROMM_VERSION, c_lib)
    oof2setuputils.pkg_check("pangocairo", PANGOCAIRO_VERSION, c_lib)
    addOOFlibs(c_lib, 'oof2common')
    c_lib.extra_compile_args.extend(['-DOOFCANVAS_USE_IMAGEMAGICK',
                                     '-DOOFCANVAS_USE_PYTHON'])
        
