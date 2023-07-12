# -*- python -*-

# Special file for regenerating reference files for skeleton
# comparisons, after changes are made to the skeleton code.
# Obviously, such reference data should not be generated until/unless
# the corresponding modifiers are known to function correctly --
# running this file will generate reference data such that the
# regression tests will pass.

# The file writes the reference data in the local directory with the
# prefix "skel_".  Users must manually overwrite the older reference
# data.  Automatically overwriting test reference data is just wrong.

# Note that this file does *not* generate the snap-nodes-with-pinning
# reference data needed by skeleton_extra_test.py.

# After running this script, you can use skelcomp.py to compare the
# old and new reference files before overwriting the old file with the
# new one.

import filecmp, os, random

def generate():
    from ooflib.SWIG.common import crandom
    from ooflib.engine import skeletonmodifier
    from ooflib.engine import skeletonnode
    from ooflib.engine import skeletonelement
    from ooflib.engine import skeletonsegment
    for r in skeletonmodifier.SkeletonModifier.registry:
        try:
            mods = skel_modify_args[r.name()]
        except KeyError:
            print("No data for skeleton modifier %s." % r.name())
        else:
            # Saved skeleton must be named "modtest".
            for (startfile, destfile, kwargs) in mods:
                OOF.File.Load.Data(
                    filename=os.path.join("skeleton_data", startfile))
                mod = r(**kwargs)
                random.seed(17)
                crandom.rndmseed(17)
                OOF.Skeleton.Modify(skeleton="skeltest:modtest",
                                    modifier=mod)
                OOF.Microstructure.Rename(microstructure="skeltest",
                                          name="skelcomp")
                OOF.Skeleton.Rename(skeleton="skelcomp:modtest",
                                    name="reference")
                OOF.File.Save.Skeleton(filename="skel_"+destfile,
                                       mode="w", format="ascii",
                                       skeleton="skelcomp:reference")
                OOF.Microstructure.Delete(microstructure="skelcomp")




# Data for the skeleton modifier tests.  This is a dictionary indexed by
# skeleton modifier name, and for each modifier, there is a set of
# arguments to supply to the modifier menu item for the test, and the
# name of a file containing correct results for that test.
skel_modify_args = {}
def build_mod_args():
    global skel_modify_args
    skel_modify_args = {
        "Refine" :
    [
          ("modgroups","refine_4L",
          {"targets" : CheckAllElements(),
           "criterion" : Unconditionally(),
           "divider" : Bisection(),
           "rules" : "Large",
           "alpha" : 0.5
           }
          ),
         ("modtriangle", "refine_7L",
          { "targets" : CheckHomogeneity(threshold=0.6),
            "criterion" : Unconditionally(),
            "divider" : Bisection(),
            "rules" : "Large",
            "alpha" : 0.5
           }
          ),
         ("modtriangle", "refine_8L",
          { "targets" : CheckHomogeneity(threshold=0.6),
            "criterion" : Unconditionally(),
            "divider" : Trisection(),
            "rules" : "Large",
            "alpha" :  0.5
           }
          ),
         ("modtriangle", "snaprefine_1LT",
          dict(targets=CheckHomogeneity(threshold=0.9),
               criterion=Unconditionally(),
               divider=TransitionPoints(minlength=0.1),
               rules='Large',
               alpha=0.5)),
         ("modtriangle", "snaprefine_2LT",
          dict(targets=CheckHomogeneity(threshold=0.9),
               criterion=Unconditionally(),
               divider=TransitionPoints(minlength=5.0),
               rules='Large',
               alpha=0.5)),
   ],
    }


def run():
    build_mod_args()
    generate()

###################################################################
# The code below this line should be common to all testing files. #
###################################################################

if __name__=="__main__":
    # If directly run, then start oof, and run the local tests, then quit.
    import sys
    try:
        import oof2
        sys.path.append(os.path.dirname(oof2.__file__))
        from ooflib.common import oof
    except ImportError:
        print("OOF is not correctly installed on this system.")
        sys.exit(4)
    sys.argv.append("--text")
    sys.argv.append("--quiet")
    sys.argv.append("--seed=17")
    oof.run(no_interp=1)
    
    success = run()

    OOF.File.Quit()
    
