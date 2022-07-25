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

# Flag that says whether to generate missing reference data files.
# Should be false unless you really know what you're doing.
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

def fp_file_compare(file1, file2, tolerance, comment="#", pdfmode=False,
                    ignoretime=False, quiet=False, nlines=None):
    # file1 is assumed to be in the current directory. file2 is
    # assumed to be in the reference directory.

    # If nlines is not None, this function will expect there to be
    # exactly nlines lines in file1 and at least nlines lines in
    # file2.

    # Regexp for matching floating-point numbers, copied from section
    # 4.2.6 of the Python 2.3 documentation.  The "(...)" group
    # constructs in the original have been replaced by "(?:...)"
    # constructs, as a way of grouping sub-expressions without
    # creating explicit groups in the regexp itself. The explicit
    # groups cause split and match to be annoying.
    floatpattern = re.compile(
        "[-+]?(?:\d+(?:\.\d*)?|\d*\.\d+)(?:[eE][-+]?\d+)?")

    ## TODO: Delete pdfmode?  It's not used, and pdf_compare(), below,
    ## is better when comparing pdf files created by cairo.
    ##
    # Pattern for detecting PDF date strings, which should not be
    # compared.  This looks for a non-digit or beginning of a line,
    # followed by exactly 14 digits, followed by 'Z'.
    datepattern = re.compile("(?:\D|^)\d{14}Z")
    # Pattern for detecting the time as printed by datetime.today().
    timepattern = re.compile("\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d\.\d*")

    try:
        file2 = reference_file(file2)
        f2 = file(file2, "r")
    except:
        if generate:
            print("\nMoving file %s to %s.\n" % (file1, file2), file=sys.stderr)
            os.rename(file1,file2)
            return True
        else:
            raise

    f1 = file(file1, "r")

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

            # If we're comparing PDF files, and both lines contain
            # date strings, just go on to the next lines.  This
            # ignores anything else on a line containing dates.  It's
            # not generally true that there's nothing else interesting
            # on date lines, but it is true of the pdf's generated by
            # oof.
            if ((pdfmode and 
                datepattern.search(f1_line) and datepattern.search(f2_line)) or
                (ignoretime and 
                timepattern.search(f1_line) and timepattern.search(f2_line))):
                continue
                
            f1_text_items = floatpattern.split(f1_line)
            f2_text_items = floatpattern.split(f2_line)
            f1_float_items = floatpattern.findall(f1_line)
            f2_float_items = floatpattern.findall(f2_line)

            for (item1, item2) in zip(f1_text_items, f2_text_items):
                if item1.strip() != item2.strip():
                    print_mismatch(f1_lineno, item1, item2)
            
            for(item1, item2) in zip(f1_float_items, f2_float_items):
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
                        # This uses the same tolerance for both absolute
                        # and relative error, which isn't usually a good
                        # idea, but is ok if the numbers being compared
                        # are more or less of order 1.
                        ok = diff < reltol or diff < tolerance
                        if not ok:
                            print_float_mismatch(f1_lineno, float1, float2)
                else: # Integer conversion worked, do comparison.
                    if int1!=int2:
                        print_int_mismatch(f1_lineno, int1, int2)

        # end for f1_lineno, f1_line in enumerate(f1)

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

pdfTimeStamp = r"/CreationDate \(D:[0-9]*Z\)"
pdfProducer = r"/Producer \(cairo [0-9\.]* \(https?://cairographics\.org\)\)"

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
    phile = file(filename, "r")
    filenumbers = eval(phile.readlines()[-1])
    if len(numbers) != len(filenumbers):
        print("*** Expected", len(numbers), "numbers.  Got",\
            len(philenumbers), file=sys.stderr)
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
    
if __name__ == "__main__":
    import sys
    import getopt

    tolerance = 0
    pdf = False
    commentchar = '#'

    option_list = ['tolerance=', 'pdf', 'comment', 'max=']
    try:
        optlist, args = getopt.getopt(sys.argv[1:], 'c:t:pm:', option_list)
    except getopt.error as message:
        print(message)
        sys.exit()

    for opt in optlist:
        if opt[0] in ('--tolerance', '-t'):
            tolerance = float(opt[1])
        if opt[0] in ('--pdf', '-p'):
            pdf = True
        if opt[0] in ('--comment', '-c'):
            commentchar = opt[1]
        if opt[0] in ('--max', '-m'):
            maxerrors = int(opt[1])

    ok = fp_file_compare(args[0], args[1], tolerance=tolerance,
                         comment=commentchar, pdfmode=pdf)
    if not ok:
        print('Files differ.')
        sys.exit(1)
    sys.exit(0)
