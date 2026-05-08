# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# Top-level regression test file for the OOF application.  Knows about
# all the test suites in this directory, and what order to run them in
# in order to get a proper regression test.

## TODO: Is it possible to allow wildcards as well as regexp syntax?
## Or is that just dumb?

import sys, os, getopt, copy, unittest, re, errno

test_module_names = [
    "fundamental_test",
    "microstructure_test",
    "image_test",
    "pixel_test",
    "activearea_test",
    "microstructure_extra_test",
    "matrix_test",
    "matrix_method_test",
    "misorientation_test",
    "orientmap_test",
    "skeleton_basic_test",
    "skeleton_select_test",
    "skeleton_bdy_test",
    "skeleton_periodic_test",
    "skeleton_periodic_bdy_test",
    "skeleton_selectionmod_test",
    "skeleton_extra_test",
    "material_property_test",
    "pixel_extra_test",
    "mesh_test",
    "subproblem_test",
    "solver_test",
    "boundary_condition_test",
    "aniso_test",
    "nonlinear_linear_test",
    "nonlinear_floatbc_test",
    "nonconstant_property_test",
    "nonlinear_property_test",
    "nonlinear_plane_flux_test",
    "nonlinear_timedependent_tests",
    "nonlinear_K_timedep_tests",
    "amr_test",
    "output_test",
    "pyproperty_test",
    "scheduled_output_test",
    "time_dependent_bc_test",
    "subproblem_test_extra",
    "r3tensorrotationbug",
    "polefigure_test",
    "zstrain_test",
    # "interface_test"
    ]

dryrun = False

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def errormsg(msg=None):
    if msg:
        print(msg)
    print(f"""
Usage : {os.path.split(sys.argv[0])[1]} [options] [test names]
Options are:
   --list             List all available tests in order, but don't run any.
   --from   testname  Start with the given test.
   --after  testname  Start after the given test.
   --to     testname  Stop at the given test.
   --forever          Repeat tests until they fail.
   --backwards        Run tests in reverse order.
   --oofargs args     Pass arguments to oof2.
   --debug            Run oof2 in debug mode.
   --dryrun           List the tests that will be run, but don't run them.
   --help             Print this message.
Test names can be given in Python's regular expression syntax. See
https://docs.python.org/3/library/re.html#regular-expression-syntax    
""",
   file=sys.stderr)

    sys.exit(1 if msg else 0)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# The startup sequence for regression.py has to imitate the executable
# oof2 script. That one imports the contents of the math module into
# the main oof namespace, so we have to do it here too.  Not importing
# math here will make some tests fail.
from math import *

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Test module name manipulations

def stripdotpy(name):
    if name.endswith(".py"):
        return name[:-3]
    return name

# Command line arguments might be regular expressions.  Return the
# first test module name that matches the given name.

def findmodulename(name):
    regexp = re.compile(name)
    for testname in test_module_names:
        if regexp.fullmatch(testname):
            return testname
    errormsg(f"Test module '{name}' not found.")

# Return all test module names that match the given name.

def findmodulenames(name):
    regexp = re.compile(name)
    matches = [testname for testname in test_module_names
               if regexp.fullmatch(testname)]
    if matches:
        return matches
    errormsg(f"Test module '{name}' not found.")

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

testcount = 1

def run_modules(test_module_names, oofglobals, backwards):
    logan = unittest.TextTestRunner()
    if backwards:
        test_module_names.reverse()
    for m in test_module_names:
        try:
            ldict = {}
            exec(f"from oof2.TEST import {m} as test_module",
                 globals(), ldict)
            test_module = ldict["test_module"]
        except ImportError:
            print(f"Import error: {m}", file=sys.stderr)
            print(f"path is {sys.path}")
        else:
            print(f"--- Running test module {m}. ---")
            # Make sure all the goodies in the OOF namespace are available.
            test_module.__dict__.update(oofglobals)
            if not dryrun and hasattr(test_module, "initialize"):
                test_module.initialize()
            for t in test_module.test_set:
                global testcount
                print(f"*** Running test {testcount}: {t.id()} ***",
                      file=sys.stderr)
                testcount += 1
                if dryrun:
                    continue
                res = logan.run(t)
                if not res.wasSuccessful():
                    return False
    return True

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def run(homedir):
    global test_module_names
    try:
        opts,args = getopt.getopt(sys.argv[1:],"f:a:t:o:",
                                  ["from=", "after=", "to=", "oofargs=",
                                   "forever", "debug", "backwards",
                                   "dryrun", "help", "list"])
    except getopt.GetoptError as err:
        errormsg(str(err))

    oofargs = []
    
    fromgiven = False           # actually from_or_after_given
    togiven = False
    forever = False
    debug = False
    backwards = False
    global dryrun

    for o,v in opts:
        if o in ("-f", "--from"):
            if fromgiven:
                errormsg("You can only use --from or --after once.")
            fromgiven = True
            v = findmodulename(stripdotpy(v))
            if v:
                test_module_names = \
                    test_module_names[test_module_names.index(v):]
        if o in ("-a", "--after"):
            if fromgiven:
                errormsg("You can only use --after or --from once.")
            fromgiven = True
            v = findmodulename(stripdotpy(v))
            if v:
                test_module_names = \
                    test_module_names[test_module_names.index(v)+1:]
            limitsgiven = True
        elif o in ("-t", "--to"):
            if togiven:
                errormsg("You can only use --to once.")
            togiven = True
            v = findmodulename(stripdotpy(v))
            if v:
                test_module_names = \
                    test_module_names[:test_module_names.index(v)+1]
            limitsgiven = True
        elif o in ("-o","--oofargs"):
            oofargs = v.split()
        elif o == "--forever":
            forever = True
        elif o == "--debug":
            debug = True
        elif o == "--backwards":
            backwards = True
        elif o == "--list":
            print("\n".join(test_module_names))
            sys.exit(0)
        elif o == "--dryrun":
            dryrun = True
        elif o == "--help":
            errormsg()

    if args:
        # Test names were listed explicitly on the command line.
        if fromgiven or togiven:
            errormsg("You can't explicitly list tests *and* use --from, --after, or --to.")

        # Expand regular expressions and add all tests that match, in
        # the order given on the command line.  If an argument matches
        # more than one test, add it more than once.  That may not be
        # what the user meant to do, but it's what they asked for.
        if args:
            tnames = []
            for t in args:
                v = findmodulenames(stripdotpy(t))
                if v:
                    tnames.extend(v)
            test_module_names = tnames

    # Effectively pass these through.
    sys.argv = [sys.argv[0]] + oofargs

    try:
        import oof2
        ## TODO: Shouldn't the next line be
        ##  "if os.path.dirname(oof2.__file__) not in sys.path"  ?
        ## But if it's not in sys.path, how was it loaded?  What is
        ## the purpose of this? Maybe it's leftover from before there
        ## were path modifications in oof2-test?
        if oof2.__file__ not in sys.path:
            sys.path.append(os.path.dirname(oof2.__file__))
        from ooflib.common import oof
    except ImportError:
        print("OOF is not correctly installed on this system.")
        sys.exit(4)

    sys.argv.extend(["--text", "--quiet", "--seed=17"])
    if debug:
        sys.argv.append("--debug")

    # Set the time zone here so that pdf files generated in the tests
    # are in the same zone as the reference files.  The pdf files
    # created by Cairo include a creation time, which is ignored
    # during comparison, but they also include a file length, which
    # changes if the time format changes.  Setting TZ here means that
    # the creation time will always include time zone information, and
    # will always use the same number of characters.
    ## Commented out, because pdf testing isn't reproducible anyway,
    ## so we're not doing it.
    # os.environ["TZ"] = "Etc/UTC"

    oof.run(no_interp=1)

    # Make a temp directory and cd to it, but put the current
    # directory in the path first, so imports will still work.  By
    # cd'ing to a temp directory, we ensure that all files written
    # during the tests won't clobber or be clobbered by files written
    # by another test being run in the same file system.
    import tempfile
    sys.path[0] = os.path.realpath(sys.path[0])
    tmpdir = tempfile.mkdtemp(prefix='oof2temp_')
    print("Using temp dir", tmpdir, file=sys.stderr)
    os.chdir(tmpdir)
    # Tell file_utils where the home directory is, since reference
    # files are named relative to it.  See comment in
    # fundamental_test.py about using the absolute path name here.
    from oof2.TEST.UTILS import file_utils
    file_utils.set_reference_dir(homedir)

    # utils.OOFglobals() returns OOF namespace objects that we will be
    # making available to each test script.  If test scripts modify
    # globals (eg, by using utils.OOFdefine or the scriptloader), we
    # don't want those modifications to affect later test scripts.
    # Therefore we create a pristine copy of globals now, and use it
    # instead of utils.OOFglobals() later.
    from ooflib.common import utils
    oofglobals = copy.copy(utils.OOFglobals())
    ok = False
    try:
        if forever:
            count = 0
            ok = False
            while run_modules(test_module_names, oofglobals, backwards):
                count += 1
                print("******* Finished", count, \
                    "iteration%s"%("s"*(count>1)), "*******", file=sys.stderr)
        else:
            ok = run_modules(test_module_names, oofglobals, backwards)
    finally:
        if ok:
            print("All tests completed successfully!", file=sys.stderr)
            if not debug:
                try:
                    os.rmdir(tmpdir)
                except OSError as exc:
                    if exc.errno == errno.ENOTEMPTY:
                        print("Temp dir", tmpdir, "is not empty. Not removing it.")
                    else:
                        raise
            else:
                print("Temp dir", tmpdir, "was not removed.", file=sys.stderr)
        else:
            print("Test failed. Temp dir", tmpdir, "was not removed.", file=sys.stderr)


#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

if __name__=="__main__":
    homedir = os.path.realpath(sys.path[0])
    run(homedir)
    OOF.File.Quit()
