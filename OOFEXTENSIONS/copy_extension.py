# -*- python -*-
# $RCSfile: copy_extension.py,v $
# $Revision: 1.1 $
# $Author: langer $
# $Date: 2011-02-17 22:44:02 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.


# This is a script to automatically make a copy of the example
# general nonlinear elasticity property, taking care of all of the
# renaming of files and things in the files.  Takes as input the desired
# filename, the new property's classname, and the new property's
# sequence number.  If the new classname is unqualified, it will be
# added in "Mechanical:Elasticity:<classname>", but if it's
# fully-qualified, the full path will be used.  If the sequence number
# is omitted, the new property will have an incremented sequence
# number (this means multiple copies might have the same sequence number).

import getopt, sys, subprocess, os

def usage(err):
    print >> sys.stderr,  err
    print >> sys.stderr, """
Usage:

# python %s --template=<template-dir-name> --module=<new-module-name> --dir=<new-dir-name> \
--class=<new-class-name> --sequenceno=<number>

Short options are -t, -m, -d, -c, and -s, in the same order as above.

""" % sys.argv[0]

###############

def is_source_file(filename, exclude=[]):
    if os.path.isdir(filename) or (os.path.basename(filename) in exclude):
        return False
    for ext in [".py", ".spy", ".swg", ".h", ".c", ".C", ".cpp"]:
        if filename.endswith(ext):
            return True
    return False

###############

if __name__ == '__main__':
    templatedir = None
    modulename = None
    dirname = None
    classname = None
    sequenceno = None

    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            't:f:d:c:s:',
            ["template=","module=","dir=","class=","sequenceno="])

    except getopt.GetoptError, err:
        usage(err)
        sys.exit(1)

    for o, a in opts:
        if o in ["-t", "--template"]:
            templatedir = a
            if templatedir.endswith('/'):
                templatedir = templatedir[:-1]
        elif o in ["-m","--module"]:
            modulename = a
        elif o in ["-d","--dir"]:
            dirname = a
        elif o in ["-c","--class"]:
            classname = a
        elif o in ["-s","--sequenceno"]:
            try:
                sequenceno = int(a)
            except ValueError:
                usage("Sequence number must be an integer.")
                sys.exit(1)
        else:
            usage("Unrecognized option '%s'." % o)
            sys.exit(2)

    if templatedir is None:
        usage("template must be provided.")
        sys.exit(2)

    if dirname is None:
        usage("dirname must be provided.")
        sys.exit(2)

    if os.path.exists(dirname):
        print dirname, "already exists.  Please remove it or choose another name."
        sys.exit(2)

    refextdir = templatedir #os.path.join(templatedir, "oofextensions")
    refdir = os.path.join(templatedir, templatedir)

    if modulename==None:
        usage("Module name argument is mandatory.")
        sys.exit(2)

    if dirname==None:
        usage("Directory name argument is mandatory.")
        sys.exit(2)

    if classname==None:
        usage("Class name argument is mandatory.")
        sys.exit(2)

    if sequenceno == None:
        sequenceno = 1000

    # files/dirs not to be copied
    blacklist = ["README", "CVS", "build", modulename+"_SWIG", "substitutions"]

    # These are the strings in the template files that will be
    # replaced when the files are copied.
    refmodule = '%MODULENAME%'
    refheader = '%HEADER%'
    refclass = '%CLASS%'
    refseqno = '%SEQNO%'


    header = modulename.upper()+"_H"

    # The general scheme is to copy all the files, and in every case, change:
    #  - the file name itself, from refmodule<ext> to modulename<ext>
    #  - the file name in the file, from refmodule to modulename.
    #  - the classname, from refclass to classname
    #  - the header line, from refheader to header.
    #  - the sequence number, from refseqno to the new one.
    sedstart = ["sed", "-e", "s/%s/%s/g" % (refmodule, modulename),
                "-e", "s/%s/%s/g" % (refclass, classname),
                "-e", "s/%s/%s/g" % (refheader, header),
                "-e", "s/%s,/%s,/" % (refseqno, str(sequenceno))]


    # We assume we are in the parent directory of both the source and
    # target directories.  This should probably actually be checked,
    # although if we're not, the "read" operation will fail anyways.
    try:
        # Create ./dirname and ./dirname/modulename
        targetdir = dirname
        os.mkdir(dirname, 0755)  # Octal!
        targetdir = os.path.join(targetdir, modulename)
        os.mkdir(targetdir, 0755)  # dirname/modulename
    except OSError:
        print >> sys.stderr, "Unable to create target directory %s."%targetdir
        print >> sys.stderr, "Exiting."
        sys.exit(4)

    file_list = ([os.path.join("template", "setup.py")]
                  + [os.path.join(refdir,f)
                     for f in os.listdir(refdir)])
    # print file_list
    for source in file_list:
        if is_source_file(source, blacklist):
            targetpath = source.split(os.sep)
            # print "targetpath0=", targetpath
            targetpath[0] = dirname
            # print "targetpath1=", targetpath
            for level, pathcomp in enumerate(targetpath[1:]):
                targetpath[level+1] = pathcomp.replace(templatedir, modulename)
            # print "targetpath2=", targetpath
            sedcmd = sedstart + [source]
            # print "targetpath=", targetpath
            target = os.path.join(*targetpath)
            try:
                fout = file(target, "w")
            except:
                print >> sys.stderr, "Unable to open target file %s" % target
                print >> sys.stderr, "Exiting."
                sys.exit(4)
            print "Copying", source, "to", target
            p1 = subprocess.Popen(sedcmd, stdout=subprocess.PIPE)
            for ell in p1.communicate():
                if ell is not None:
                    fout.write(ell)
            fout.close()
        # else:
        #     print "Not copying", source
