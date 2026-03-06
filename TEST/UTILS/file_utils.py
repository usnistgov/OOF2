# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import itertools
import math
import os
import re
import sys

# Flag that says whether to generate missing reference data files in
# fp_file_compare and pdf_compare.  Should be false unless you really
# know what you're doing.
generate=False
# Max number to report from one file.
maxerrors = 10

errorcount = 0
filename1 = None
filename2 = None
silent = False

# globals, because we can afford to be quick and dirty here.
def print_header():
    global filename1, filename2, silent
    if not silent:
        print("Error comparing files", \
            os.path.abspath(filename1), os.path.abspath(filename2), file=sys.stderr)

def print_mismatch(line, v1, v2):
    global errorcount
    if errorcount==0:
        print_header()
    if errorcount == maxerrors and not silent:
        print("[Skipping further errors]", file=sys.stderr)
    if errorcount < maxerrors and not silent:
        print("   line %5d: %s != %s" % (line+1, v1, v2), file=sys.stderr)
    errorcount += 1

def print_float_mismatch(line, v1, v2):
    global errorcount
    if errorcount==0:
        print_header()
    if errorcount == maxerrors and not silent:
        print("[Skipping further errors]", file=sys.stderr)
    if errorcount < maxerrors and not silent:
        print("   line %5d: %-16.9g != %-16.9g  (diff=% 8g, % .2g%%)" \
            % (line+1, v1, v2,
               v1-v2,
               100.*(v1-v2)/(0.5*(abs(v1) + abs(v2)))), file=sys.stderr)
    errorcount += 1

def print_int_mismatch(line, v1, v2):
    global errorcount
    if errorcount==0:
        print_header()
    if errorcount == maxerrors and not silent:
        print("[Skipping further errors]", file=sys.stderr)
    if errorcount < maxerrors and not silent:
        print("   line %5d: %16d != %16d" % (line+1, v1, v2), file=sys.stderr)
    errorcount += 1

def conversion_error(line, v1, v2):
    global errorcount
    if not errorcount:
        print_header()
    if not silent:
        print(("   line %5d: %s // %s  (conversion error!)"
                              % (line+1, v1, v2)), file=sys.stderr)
    errorcount += 1
        
def eof_error(line, filename):
    global errorcount
    if not errorcount:
        print_header()
    if not silent:
        print(("   Line %5d: Premature EOF in file %s!" 
                              % (line+1, filename)), file=sys.stderr)
    errorcount += 1

def too_many_lines(filename, nlines):
    global errorcount
    if not errorcount:
        print_header()
    if not silent:
        print(("  Too many lines in file %s!  Expected %d."
                              % (filename, nlines)), file=sys.stderr)
    errorcount += 1

def too_few_lines(filename, nlines):
    global errorcount
    if not errorcount:
        print_header()
    if not silent:
        print(("  Too few lines in file %s!  Expected %d."
                              % (filename, nlines)), file=sys.stderr)
    errorcount += 1

# set_reference_dir can be called to change the directory in which
# reference files are to be found.  regression.py sets it to the TEST
# directory before cd'ing to the temp directory.  Files named in the
# *second* argument to fp_file_compare are automatically looked for in
# the reference directory.  Reference filenames used by other routines
# should be processed through reference_file() before being used.

referencedir = ''
def set_reference_dir(path):
    global referencedir
    referencedir = path

def reference_file(*args):
    # This does the right thing if referencedir is an empty string.
    return os.path.join(referencedir, *args)

# Regexp for matching floating-point numbers, copied from section
# 4.2.6 of the Python 2.3 documentation.  The "(...)" group
# constructs in the original have been replaced by "(?:...)"
# constructs, as a way of grouping sub-expressions without
# creating explicit groups in the regexp itself. The explicit
# groups cause split and match to be annoying.
floatpattern = re.compile(
    r"[-+]?(?:\d+(?:\.\d*)?|\d*\.\d+)(?:[eE][-+]?\d+)?")

# Regexp for quoted substrings with either single or double
# quotes.  It's constructed in two pieces to avoid escape
# character hell.  Outer parentheses put the substring in a group,
# so that re.split will include it in its output.
quotepattern = re.compile(r'("[^"]*"|'   # double quoted substring
                          + r"'[^']*')") # single quoted substring

# Pattern for detecting the time as printed by datetime.today().
timepattern = re.compile(r"\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d\.\d*")

def fp_file_compare(file1, file2, tolerance, comment="#",
                    ignoretime=False, quiet=False, nlines=None):
    # file1 is assumed to be in the current directory. file2 is
    # assumed to be in the reference directory.

    # If nlines is not None, this function will expect there to be
    # exactly nlines lines in file1 and at least nlines lines in
    # file2.


    try:
        file2 = reference_file(file2)
        f2 = open(file2, "r")
    except:
        if generate:
            print("\nMoving file %s to %s.\n" % (file1, file2), file=sys.stderr)
            os.rename(file1,file2)
            return True
        else:
            raise

    f1 = open(file1, "r")

    global errorcount, filename1, filename2, silent
    filename1 = file1           # store in globals
    filename2 = file2
    errorcount = 0
    silent = quiet

    try:
        f1_lineno = -1        # just in case file1 is empty
        for f1_lineno, f1_line in enumerate(f1):
            if nlines is not None and f1_lineno == nlines:
                too_many_lines(filename1, nlines)
            try:
                f2_line = next(f2)
            except StopIteration:
                eof_error(f1_lineno, filename2)
                break
            if comment is not None and f1_line[0] == f2_line[0] == comment:
                continue

            # First, break into quoted and nonquoted substrings.  A
            # quoted string might contain something that looks like an
            # infinite number, eg "1e999", which evaluates to
            # inf. inf-inf is nan, and nan!=nan, so a numerical
            # comparison will fail. (This happens when reading a
            # hex-encoded image from a data file, if the image data is
            # not treated as a quoted string.)
            f1_substrings = quotepattern.split(f1_line)
            f2_substrings = quotepattern.split(f2_line)

            for (f1_sub, f2_sub) in zip(f1_substrings, f2_substrings):
                if not (f1_sub and f2_sub):
                    # Skip empty substrings, which can arise from re.split.
                    continue  
                if not f1_sub or not f2_sub:
                    # If only one substring is empty, its a mismatch.
                    print_mismatch(f1_lineno, f1_sub, f2_sub)
                elif (f1_sub[0] in '"\'' and f2_sub[0] == f1_sub[0]):
                    # Found a quoted substring
                    if f1_sub != f2_sub:
                        print_mismatch(f1_lineno, f1_sub, f2_sub)
                else:
                    # Not a quoted substring.
                    # Check for time stamps, and ignore them.
                    if (ignoretime and timepattern.search(f1_sub) and
                        timepattern.search(f2_sub)):
                        continue
                    
                    # Split substrings by numbers, which will be
                    # compared numerically, with a tolerance for
                    # floating point.
                    f1_text_items = floatpattern.split(f1_sub)
                    f2_text_items = floatpattern.split(f2_sub)
                    f1_numbers = floatpattern.findall(f1_sub)
                    f2_numbers = floatpattern.findall(f2_sub)

                    for (item1, item2) in zip(f1_text_items, f2_text_items):
                        if item1.strip() != item2.strip():
                            print_mismatch(f1_lineno, item1, item2)

                    for(item1, item2) in zip(f1_numbers, f2_numbers):
                        try:
                            int1 = int(item1)
                            int2 = int(item2)
                        except ValueError:
                            try:
                                float1 = float(item1)
                                float2 = float(item2)
                            except ValueError:
                                conversion_error(f1_lineno, item1, item2)
                            else:
                                diff = abs(float1 - float2)
                                reltol = min(abs(float1), abs(float2))*tolerance
                                # This uses the same tolerance for
                                # both absolute and relative error,
                                # which isn't usually a good idea, but
                                # is ok if the numbers being compared
                                # are more or less of order 1.  Use <=
                                # instead of < so that
                                # diff==tolerance==0 is accepted!
                                ok = diff <= reltol or diff <= tolerance
                                if not ok:
                                    print_float_mismatch(f1_lineno,
                                                         float1, float2)
                        else: # Integer conversion worked, do comparison.
                            if int1!=int2:
                                print_int_mismatch(f1_lineno, int1, int2)

        # Is there more to read from file 2?
        try:
            f2_line = next(f2)
        except StopIteration:
            moref2 = False
        else:
            moref2 = True
                        
        if nlines is not None:
            # Check that we read nlines lines, unless we're also done
            # with file 2.  In that case, since the files are the
            # same, the test passes, even if the provided nlines is
            # too large.
            if f1_lineno < nlines-1 and moref2:
                too_few_lines(filename1, nlines)
        else: 
            # nlines is None, so the files must agree exactly.  We're
            # already at the end of file 1.  Check that there's
            # nothing left in file 2.
            if moref2:
                eof_error(f1_lineno, filename1)
        
        if errorcount > 0:
            if not silent:
                print(("%d error%s in file comparison!" %
                                      (errorcount, "s"*(errorcount!=1))), file=sys.stderr)
            return False

        if not silent:
            print("Files", filename1, "and", filename2, "agree.", file=sys.stderr)
        return True
    finally:
        f1.close()
        f2.close()

def binary_file_compare(file1, file2):
    file2 = reference_file(file2)
    try:
        f2 = open(file2, 'rb')
    except:
        if generate:
            print(f"\nMoving file {file1} to {file2}", file=sys.stderr)
            os.rename(file1, file2)
            return True
        else:
            raise
    f1 = open(file1, 'rb')
    try:
        data1 = f1.read()
        data2 = f2.read()
        if f1 != f1:
            print(f"Files {file1} and {file2} differ")
            return False
        return True
    finally:
        f1.close()
        f2.close()
        
pdfTimeStamp = rb"/CreationDate \(D:[0-9]*Z\)"
pdfProducer = rb"/Producer \(cairo [0-9\.]* \(https?://cairographics\.org\)\)"

def pdf_compare(file1, file2, quiet=False):
    # Compare two files byte by byte, allowing them to differ by a pdf
    # date stamp of the form
    #   /CreationDate (D:20220405184305Z)
    # IMPORTANT: To guarantee that the date is of this form, set the TZ
    # environment variable to "Etc/UTC" before generating the
    # reference files.  regression.py sets TZ before running the
    # tests.
    #
    # Also ignore a producer stamp, which will look like this,
    # possibly with a different version number:
    #   /Producer (cairo 1.16.0 (https://cairographics.org))

    # If file2 is a tuple of filenames, compare to each of them, and
    # return true if any one of them works.
    if type(file2) is tuple:
        for f2 in file2:
            if pdf_compare(file1, f2, quiet=True):
                if not quiet:
                    print("Files", file1, "and", f2, "agree", file=sys.stderr)
                return True
        if not quiet:
            print("File", file1, "does not match any of", file2,
                  file=sys.stderr)
        return False

    try:
        file2 = reference_file(file2)
        f2 = open(file2, "rb")
    except:
        if generate:
            print("\nMoving file %s to %s.\n" % (file1, file2), file=sys.stderr)
            os.rename(file1,file2)
            return True
        else:
            raise

    f1 = open(file1, "rb")
    chars1 = f1.read()
    chars2 = f2.read()
    f1.close()
    f2.close()

    # Ranges of indices to omit when comparing the characters
    ranges1 = []
    ranges2 = []

    timeSearch1 = re.search(pdfTimeStamp, chars1)
    timeSearch2 = re.search(pdfTimeStamp, chars2)
    if timeSearch1 is not None or timeSearch2 is not None:
        if timeSearch1 is None or timeSearch2 is None:
            # Timestamp was only found in one file.
            if not quiet:
                print(f"File mismatch: {file1} {file2}", file=sys.stderr)
            return False
        ranges1.append((timeSearch1.start(), timeSearch1.end()))
        ranges2.append((timeSearch2.start(), timeSearch2.end()))
    prodSearch1 = re.search(pdfProducer, chars1)
    prodSearch2 = re.search(pdfProducer, chars2)
    if prodSearch1 is not None or prodSearch2 is not None:
        if prodSearch1 is None or prodSearch2 is None:
            if not quiet:
                print(f"File mismatch: {file1} {file2}", file=sys.stderr)
            return False
        ranges1.append((prodSearch1.start(), prodSearch1.end()))
        ranges2.append((prodSearch2.start(), prodSearch2.end()))

    ranges1.sort()
    ranges2.sort()
    if subStrCompare(chars1, ranges1, chars2, ranges2):
        if not quiet:
            print("Files", file1, "and", file2, "agree", file=sys.stderr)
        return True
    if not quiet:
        print("File mismatch:", file1, file2, file=sys.stderr)
    return False

def subStrCompare(chars1, ranges1, chars2, ranges2):
    # Compare the strings chars1 and chars2 while excluding the ranges
    # given in ranges1 and ranges2, which are lists of (begin,end)
    # tuples.
    assert len(ranges1) == len(ranges2)
    last1 = 0
    last2 = 0
    for r1, r2 in zip(ranges1, ranges2):
        # Check that the substring [last1, r1[0]] in chars1 is the
        # same as [last2, r2[0]] in chars2.
        if r1[0]-last1 != r2[0]-last2:
            print("Substring length mismatch", file=sys.stderr)
            return False
        for i in range(r1[0]-last1):
            if chars1[last1+i] != chars2[last2+i]:
                print("Substring mismatch", file=sys.stderr)
                return False
        last1 = r1[1]
        last2 = r2[1]
    # Check the substrings after the last excluded range.
    if len(chars1)-last1 != len(chars2)-last2:
        print("Final substring length mismatch", file=sys.stderr)
        return False
    for i in range(len(chars1)-last1):
        if chars1[last1+i] != chars2[last2+i]:
            print("Final substring mismatch", file=sys.stderr)
            return False
    return True

def compare_last(filename, numbers, tolerance=1.e-10):
    # The last line of the given file contains a bunch of numbers
    # separated by commas.  Check that the numbers in the file are
    # within tolerance of the tuple 'numbers'.
    phile = open(filename, "r")
    filenumbers = eval(phile.readlines()[-1])
    if len(numbers) != len(filenumbers):
        print("*** Expected", len(numbers), "numbers.  Got",\
            len(filenumbers), file=sys.stderr)
        return False
    for (x, y) in zip(numbers, filenumbers):
        if math.fabs(x-y) > tolerance:
            print("*** Expected", numbers, file=sys.stderr)
            print("***    Found", filenumbers, file=sys.stderr) 
            return False
    return True
        
# remove() should be used to remove a file that a test generated for
# comparison with fp_file_compare.  If fp_file_compare was running
# with generate==True, the file might not exist, but remove() won't
# complain.

def remove(filename):
    try:
        os.remove(filename)
    except:
        if generate:
            pass
        else:
            raise

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# This file can be run on its own to compare two data files with
# fp_file_compare().

if __name__ == "__main__":
    import sys
    import getopt

    tolerance = 0
    commentchar = '#'

    option_list = ['tolerance=', 'comment', 'max=']
    try:
        optlist, args = getopt.getopt(sys.argv[1:], 'c:t:pm:', option_list)
    except getopt.error as message:
        print(message)
        sys.exit()

    for opt in optlist:
        if opt[0] in ('--tolerance', '-t'):
            tolerance = float(opt[1])
        if opt[0] in ('--comment', '-c'):
            commentchar = opt[1]
        if opt[0] in ('--max', '-m'):
            maxerrors = int(opt[1])

    ok = fp_file_compare(args[0], args[1], tolerance=tolerance,
                         comment=commentchar)
    if not ok:
        print('Files differ.')
        sys.exit(1)
    sys.exit(0)
