# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# This file looks for all subdirectories of the current directory and
# runs the gui test contained in each one.  The tests are run in
# alphabetical order of the subdirectory name.  It is assumed that
# each subdirectory contains a file named TESTFILE:

TESTFILE = "test.log"

# The test is run by executing
#    oof2 --pathdir <subdirectory> --replay <subdirectory>/TESTFILE
# and testing its return value. The subdirectory is added to the
# python path so that the log file can contain import statements that
# load tests from other files in the subdirectory.

# Actually, the tests are run in a temporary directory so that any
# files created by the test don't overwrite anything.  This means that
# *this* directory (OOF2/TEST/GUI) is also added to the path.  The
# temp directory also contains a symbolic link to OOF2/TEST/UTILS,
# which is added to the path. It contains links to
# OOF2/TEST/GUI/examples and OOF2/TEST/GUI/TEST_DATA, but they're not
# in the path.

# To temporarily skip a subdirectory, add a file called SKIP to it.
# To permanently skip a subdirectory, add it to the "excluded" list
# here:

excluded = ['CVS','TEST_DATA', 'examples', '__pycache__']

# The subdirectory can contain a file called "args" which contains a
# single line of arguments to be added to the oof2 command.  It can
# also contain a file named 'cleanup.py' which will be run after the
# test, if the test is successful.  cleanup.py is run in the
# guitests.py environment.

# Any test that raises an uncaught exception or calls sys.exit() with
# an non-zero status is considered a failure.  If a test is *supposed*
# to return a non-zero status, that status should be put in a file
# called 'exitstatus' in the test subdirectory.

import getopt
import os
import re
import string
import subprocess
import sys
import tempfile

delaystr = None
debug = False
no_checkpoints = False
sync = False
unthreaded = False
retries = 0
dryrun = False

global tmpdir
tmpdir = None

skipdirs = ["__pycache__"]

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def run_tests(dirs, rerecord, forever):
    homedir = os.getcwd()
    global tmpdir
    tmpdir = tempfile.mkdtemp(prefix='oof2temp_')
    print(f"Using temp dir {tmpdir}", file=sys.stderr)

    linkfile(homedir, 'examples')
    linkfile(homedir, 'TEST_DATA')
    os.symlink(os.path.abspath(os.path.join('..', 'UTILS')),
               os.path.join(tmpdir, 'UTILS'))
    os.chdir(tmpdir)
    try:
        if forever:
            counter = 1
            while True:
                print(f"******* {counter} ********", file=sys.stderr)
                ok = really_run_tests(homedir, dirs, counter, rerecord)
                counter += 1
        else:
            really_run_tests(homedir, dirs, None, rerecord)
    except Exception as exc:
        # Test failed by raising an exception.
        print(f"Not removing temp directory {tmpdir}", file=sys.stderr)
        raise
    else:
        # All tests executed successfully.  Remove everything from the
        # temp directory.  There may be stray data files, as well as
        # the subdirectories linked above, even if everything ran
        # correctly.
        for f in os.listdir(tmpdir):
            os.remove(f)
        # Remove the now empty temp directory.
        os.rmdir(tmpdir)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def really_run_tests(homedir, dirs, counter, rerecord):
    # 'counter' counts the iterations through the 'forever' loop in
    # run_tests().  It is None if the tests are being looped over.
    
    skipped = []    # list of skipped directories, reported at the end
    nrun = 0
    retried = [] # tests which had to be repeated, reported at the end
    for directory in dirs:
        originaldir = os.path.join(homedir, directory)
        # Check that the directory and log file exist, and that
        # there's no SKIP file, before bothering to make the symlink
        # to the directory.
        if not os.path.isdir(originaldir):
            print(f"Can't find directory {directory}", file=sys.stderr)
            return
        if os.path.exists(os.path.join(originaldir, 'SKIP')) and len(dirs) > 1:
            print(f" **** Skipping {directory} ****", file=sys.stderr)
            skipped.append(directory)
            continue
        if not os.path.exists(os.path.join(originaldir, TESTFILE)):
            print(f" **** Skipping {directory} (No log file!) ****",
                  file=sys.stderr)
            skipped.append(directory)
            continue

        # Ok, everything's there.  Get ready to run this test.  Make a
        # symlink to the test directory.
        ## TODO: Is the symlink really necessary? We could provide a
        ## full path to TESTFILE.  The test directory is already in
        ## PYTHONPATH.
        testdir = os.path.join(tmpdir, directory)
        if not dryrun:
            os.symlink(os.path.join(homedir, directory), testdir)

        # Read extra oof2 args from the args file, if it exists.
        if os.path.exists(os.path.join(directory, 'args')):
            argfile = open(os.path.join(directory, 'args'))
            extraargs = argfile.readline().rstrip().split()
            argfile.close()
        else:
            extraargs = []
        # Read the expected exit status from the exitstatus file, if
        # it exists.
        if os.path.exists(os.path.join(directory, 'exitstatus')):
            exitstatfile = open(os.path.join(directory, 'exitstatus'))
            exitstatus = int(exitstatfile.readline())
            exitstatfile.close()
        else:
            exitstatus = 0
        
        global delaystr
        if delaystr:
            extraargs += ["--replaydelay=", delaystr]
        if debug:
            extraargs += ["--debug"]
        if no_checkpoints:
            extraargs += ["--no-checkpoints"]
        if sync:
            extraargs += ["--gtk=", "--sync"]
        if unthreaded:
            extraargs += ["--unthreaded"]
        if rerecord:
            replayarg = 'rerecord'
        else:
            replayarg = 'replay'

        for iteration in range(retries+1):
            cmd = ["oof2",
                   "--no-rc",       # .oof2rc might affect tests.  Don't use it.
                   "--pathdir", ".",
                   "--pathdir", "%s" % directory,
                   "--pathdir", "%s" % homedir,
                   "--pathdir", "UTILS",
                   "--%s" % replayarg, # 'replay' or 'rerecord'
                   os.path.join(directory, TESTFILE)] + extraargs
            # The 'replayprefix' argument depends on the iteration
            # number and has to be constructed inside the loop.
            iterstring = f"({iteration})" if retries > 0 else ''
            counterstring = f"{counter}" if counter is not None else ''
            pstrings = [directory, counterstring, iterstring]
            cmd.extend(["--replayprefix", ' '.join(s for s in pstrings if s)])

            if not dryrun: 
                print("-------------------------", file=sys.stderr)
            print("--- Running %s" % ' '.join(cmd), file=sys.stderr)
            if dryrun:
                continue
            
            os.environ["OOFTESTDIR"] = directory
            result = subprocess.call(cmd)
            print("--- Return value =", result, file=sys.stderr)
            if result < 0:
                print(f"Child was terminated by signal {-result}",
                      file=sys.stderr)
                print(f"Test {directory} failed!", file=sys.stderr)
                print(f"Not removing {tmpdir}", file=sys.stderr)
                if iteration==retries:
                    print("Test iteration limit exceeded.", file=sys.stderr)
                    sys.exit(result)

            elif result != exitstatus:
                print(f"Test {directory} failed! Status={result}, expected={exitstatus}",
                      file=sys.stderr)
                if iteration==retries:
                    sys.exit(result)
            else:
                break           # success.  Don't retry.
            # end retry loop
        if iteration != 0:
            retried.append((directory, iteration))
        if not dryrun:
            print(f"--- Finished {directory}", file=sys.stderr)
            cleanupscript = os.path.join(directory, 'cleanup.py')
            if os.path.exists(cleanupscript):
                sys.path.append(directory)
                sys.path.append(homedir)
                sys.path.append("UTILS")
                exec(
                    compile(open(cleanupscript, "rb").read(),
                            cleanupscript, 'exec'),
                    globals(), locals())
            # Remove the symlink to the source test directory
            # <prefix>/lib/pythonX.Y/site-packages/oof2/TEST/GUI/<testname>
            os.remove(testdir)
        nrun += 1

    if not dryrun:
        print(f"{pluralize(nrun, 'test')} ran successfully!", file=sys.stderr)
        # print("%d test%s ran successfully!" % (nrun, "s"*(nrun!=1)),
        #       file=sys.stderr)
        if retried:
            print(f"Repeated {pluralize(len(retried), 'test')}",
                  file=sys.stderr) 
            # print(f"Repeated {len(retried)} test{'s'*(len(retried)!=1)}:",
            #       file=sys.stderr)
            for directory, count in retried:
                print(f"    {directory}: repeats = {count}", file=sys.stderr)
    if skipped:
        print(f"Skipped {pluralize(len(skipped), 'test')}:", file=sys.stderr)
        # print("Skipped %d test%s:" % (len(skipped), "s"*(len(skipped)!=1)),
        #       file=sys.stderr)
        for skipdir in skipped:
            print(f"    {skipdir}", file=sys.stderr)

def pluralize(i, s):
    if i != 1:
        return f"{i} {s}s"
    else:
        return f"1 {s}"
       
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def get_dirs():
    # Return the full set of test directory names.
    files = sorted([f for f in os.listdir('.')
                    if os.path.isdir(f) and f not in excluded])
    return files

def expanddirs(name, alldirs):
    # Return the subset of alldirs that matches the given name, which
    # might be a regular expression.
    regexp = re.compile(name)
    return [testname for testname in alldirs if regexp.fullmatch(testname)]

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def removefile(filename):
    fullname = os.path.normpath(os.path.join(tmpdir, filename))
    print("Removing file", fullname, file=sys.stderr)
    if os.path.exists(fullname):
        os.remove(fullname)

def linkfile(homedir, filename):
    os.symlink(os.path.join(homedir, filename),
               os.path.join(tmpdir, filename))

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def errormsg(msg=None):
    if msg:
        print(msg, file=sys.stderr)
    print(f"""
Usage:  {os.path.split(sys.argv[0])[1]} [options] [test names]

Options are:
   --list             List all available tests in order, but don't run any.
   --from   testname  Start with the given test.
   --after  testname  Start after the given test.
   --to     testname  Stop at the given test.
   --retries n        Repeat failed tests at most this many times (default=0)
   --forever          Repeat tests until they fail.
   --delay  ms        Delay (in milliseconds) between lines of each test.
   --debug            Run tests in debug mode.
   --unthreaded       Run tests in unthreaded mode.
   --sync             Run tests in X11 sync mode (very slow over a network!).
   --rerecord         Re-record log files, without actually testing.
                      This is useful if new checkpoints have been added.
   --no-checkpoints   Ignore checkpoints in log files (not very useful).
   --dryrun           Don't actually run anything, but print what would be run.
   --help             Print this message.
""", file=sys.stderr)

    sys.exit(1 if msg else 0)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def run(homedir):
    os.chdir(homedir)
    try:
        optlist, args = getopt.getopt(sys.argv[1:], '', 
                                      ['delay=', 'debug',
                                       'list',
                                       'from=', 'after=', 'to=',
                                       'rerecord', 'no-checkpoints',
                                       'sync', 'unthreaded', 'dryrun',
                                       'forever', 'retries=',
                                       'help'])
    except getopt.GetoptError as message:
        errormsg(message)

    global debug, unthreaded, sync, no_checkpoints, delaystr, retries, dryrun
    fromdir = None
    afterdir = None
    todir = None
    rerecord = False
    forever = False
    listtests = False
    for opt in optlist:
        if opt[0] == "--debug":
            debug = True
        elif opt[0] == "--delay":
            delaystr = opt[1]
        elif opt[0] == '--from':
            # normpath is necessary here because if the shell's
            # filename completion was used to construct the argument,
            # the directory name may have a trailing slash, and the
            # index() calls below will fail.
            fromdir = os.path.normpath(opt[1])
        elif opt[0] == '--after':
            afterdir = os.path.normpath(opt[1])
        elif opt[0] == '--to':
            todir = os.path.normpath(opt[1])
        elif opt[0] == '--rerecord':
            rerecord = True
        elif opt[0] == '--no-checkpoints':
            no_checkpoints = True
        elif opt[0] == '--unthreaded':
            unthreaded = True
        elif opt[0] == '--sync':
            sync = True
        elif opt[0] == '--forever':
            forever = True
        elif opt[0] == '--retries':
            retries = int(opt[1])
        elif opt[0] == '--list':
            listtests = True
        elif opt[0] == '--dryrun':
            dryrun = True
        elif opt[0] == '--help':
            errormsg()

    dirs = get_dirs()        # list of subdirectories in OOF/TEST/GUI.

    if listtests:
        print("\n".join(dirs))
        sys.exit(0)


    expdirs = []  # list of subdirectories to be actually used
    
    if args:
        # Test directories or regexps for them were explicitly listed
        # on the command line.  Expand each regexp, checking for
        # errors.
        for regexp in args:
            edirs = expanddirs(regexp, dirs)
            if not edirs:
                errormsg(f"Directory {regexp} not found.")
            expdirs.extend(edirs)
    else:
        # Resolve --from, --after, and --to arguments
        fromindex = 0
        toindex = -1
        if fromdir and afterdir:
            errormsg("You cannot use both --from and --after!")

        if fromdir:
            try:
                fromds = expanddirs(fromdir, dirs)
                fromindex = dirs.index(fromds[0])
            except IndexError:
                errormsg(f"Test directory {fromddir} not found!")
            except Exception as exc:
                errormsg(exc)

        if afterdir:
            try:
                afterds = expanddirs(afterdir, dirs)
                fromindex = dirs.index(afterds[0]) + 1
                if fromindex >= len(dirs):
                    fromindex = -1
            except IndexError:
                errormsg(f"Test directory {afterdir} not found!")
            except Exception as exc:
                errormsg(exc)

        if todir:
            try:
                tods = expanddirs(todir, dirs)
                toindex = dirs.index(tods[0]) + 1
            except:
                errormsg(f"Directory {todir} not found!")

        expdirs = dirs[fromindex:toindex]
            
    run_tests(expdirs, rerecord, forever)
                         
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

if __name__ == "__main__":
    homedir = os.path.realpath(sys.path[0])
    run(homedir)
    
