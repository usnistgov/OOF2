# -*- python -*-
# $RCSfile: regression.py,v $
# $Revision: 1.2 $
# $Author: vrc $
# $Date: 2008/10/14 22:29:42 $

# Top-level regression test file for the OOF application.  Knows about
# all the test suites in this directory, and what order to run them in
# in order to get a proper regression test.

import sys, imp, os

test_module_names = [
    "fundamental_test",
    "microstructure_test",
    "image_test",
    "pixel_test",
    "activearea_test",
##     "microstructure_extra_test",
##     "skeleton_basic_test",
##     "skeleton_select_test",
##     "skeleton_bdy_test",
##     "skeleton_periodic_test",
##     "skeleton_periodic_bdy_test",
##     "skeleton_selectionmod_test",
##     "skeleton_extra_test",
    "material_property_test",
##     "pixel_extra_test",
##     "mesh_test",
##     "subproblem_test",
##     "mesh_modify_test",
##     "solver_test",
##     "boundary_condition_test",
##     "output_test",
##     "subproblem_test_extra"
    ]


if __name__=="__main__":
    try:
        import oof3d
        sys.path.append(os.path.dirname(oof3d.__file__))
        from ooflib.common import oof
    except ImportError:
        print "OOF is not correctly installed on this system."
        sys.exit(4)
    sys.argv.extend(["--text", "--quiet", "--seed=17"])
    oof.run(no_interp=1)

    for m in test_module_names:
        try:
            exec "import " + m + " as test_module" 
        except ImportError:
            print "Unable to load module '%s'." % m
        else:
            print "Running test module %s." % m
            # Make sure all the goodies in the OOF namespace are available.
            test_module.__dict__.update(globals())
            res = test_module.run_tests()
            if res==0: # failure.
                break
    OOF.File.Quit()
