# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# Generic tests that can be inluded in GUI test scripts.  Most import
# statements are included in function bodies so that the first import
# is unlikely to come from this file, which might affect program
# behavior if the import has side effects.

from ooflib.common.IO.GUI import gtklogger
import file_utils
import filecmp
import os
import re
import string
import sys
import types

from ooflib.common import debug

## TODO: The naming conventions for functions in this file are not at
## all consistent.

from gi.repository import Gtk

floatpattern = \
    re.compile(r"([-+]?(?:\d+(?:\.\d*)?|\d*\.\d+)(?:[eE][-+]?\d+)?)")
intpattern = re.compile("[0-9]+$")

# fp_string_compare compares two strings.  Any floating point numbers
# within the strings are compared numerically, using the given
# tolerance.  If the tolerance is None or 0, the strings are compared
# character-wise.

def fp_string_compare(str1, str2, tolerance=None):
    try:
        if tolerance is None:
            return str1 == str2

        s1_items = floatpattern.split(str1)
        s2_items = floatpattern.split(str2)

        if len(s1_items) != len(s2_items):
            return False

        for s1, s2 in zip(s1_items, s2_items):
            if not fp_substring_compare(s1, s2, tolerance):
                return False
        return True
    except:
        print("fp_string_compare failed:",
              str1, str2, tolerance, file=sys.stderr)
        raise

def fp_substring_compare(s1, s2, tolerance=None):
    if intpattern.match(s1) and intpattern.match(s2):
        if int(s1) != int(s2):
            print("fp_substring_compare: int mismatch", \
                s1, s2, file=sys.stderr)
            return False
    elif floatpattern.match(s1) and floatpattern.match(s2):
        x1 = float(s1)
        x2 = float(s2)
        diff = abs(x1 - x2)
        reltol = 0.5*(abs(x1) + abs(x2))*tolerance 
        if diff > reltol and diff > tolerance:
            print("fp_substring_compare: float mismatch", \
                s1, s2, "diff=%s" % diff, file=sys.stderr)
            return False
    else:
        if s1 != s2:
            print(("fp_substring_compare: string mismatch\n==>%s<==\n==>%s<=="
                 % (s1, s2)), file=sys.stderr)
            return False
    return True

# fp_string_compare_tail is just like fp_string_compare, but it
# doesn't use all of str1.  It checks to see if str2 appears at the
# end of str1.

def fp_string_compare_tail(str1, str2, tolerance=None):
    if tolerance is None:
        return str1.endswith(str2)
    s1_items = floatpattern.split(str1)
    s2_items = floatpattern.split(str2)
    if len(s1_items) < len(s2_items):
        return False
    # The first items are treated separately, because the piece from
    # str2 only needs to match the end of the piece from str1 if it's
    # not a float.
    s1 = s1_items[-len(s2_items)]
    s2 = s2_items[0]
    if not (floatpattern.match(s1) and floatpattern.match(s2)):
        s1_items = s1_items[1-len(s2_items):]
        s2_items = s2_items[1:]
        if not s1.endswith(s2):
            print(("fp_string_compare_tail: "
                                  "string mismatch\n==>%s<==\n==>%s<=="
                                  % (s1, s2)), file=sys.stderr)
            return False
    else:
        s1_items = s1_items[-len(s2_items):]

    for s1, s2 in zip(s1_items, s2_items):
        if not fp_substring_compare(s1, s2, tolerance):
            return False
    return True

# Compare a test file to a reference file, using a tolerance on any
# floats found.  The test file is assumed to be in the test's working
# directory, and the reference file to be in the test source
# directory.  If the name of the reference file isn't given, it's
# asssumed to be the same as the test file.

def filediff(filename, reference=None, tolerance=1.e-8):
    if reference is None:
        reffile = os.path.join(testdir(), filename)
    else:
        reffile = os.path.join(testdir(), reference)
    return file_utils.fp_file_compare(filename, reffile, tolerance)

checkpoint_count = gtklogger.checkpoint_count

def testdir():
    # guitests.py sets OOFTESTDIR before running each test.  It's the
    # directory containing the log file and reference data files for
    # the test.
    return os.getenv('OOFTESTDIR')

def removefile(filename):
    if os.path.exists(filename):
        os.remove(filename)

def mainPageCheck(name):
    from ooflib.SWIG.common import guitop
    return guitop.top().currentPageName == name 

def whoNameCheck(whoclass, names):
    from ooflib.common.IO import whoville
    classmembers = whoville.getClass(whoclass).actualMembers()
    if len(classmembers) != len(names):
        return False
    for whoobj in classmembers:
        if whoobj.name() not in names:
            return False
    return True

def gfxWindowCheck(names):
    from ooflib.common.IO import gfxmanager
    windows = gfxmanager.gfxManager.getAllWindows()
    if len(names) != len(windows):
        return False
    for window in windows:
        if window.name not in names:
            return False
    return True

def emptyGraphicsWindow(windowname):
    from ooflib.common.IO import gfxmanager
    gfxwindow = gfxmanager.gfxManager.getWindow(windowname)
    return not gfxwindow.drawable()

def treeViewLength(widgetpath):
    # Return the number of items in the given TreeView.
    treeview = gtklogger.findWidget(widgetpath)
    return len(treeview.get_model())

def chooserCheck(widgetpath, choices):
    # chooserCheck works for ChooserWidget, but not ChooserListWidget
    stack = gtklogger.findWidget(widgetpath + ':stack')
    # stack is a Gtk.Stack of Gtk.Boxes containing labels and images.
    # box.get_children()[0] is a Gtk.Label.
    names = [box.get_children()[0].get_text() for box in stack.get_children()]
    names.remove("---")         # emptyMarker
    # stack.get_children doesn't return the children in a predictable
    # order, so just compare the sorted lists.
    if sorted(names) != sorted(choices):
        print("chooserCheck failed!", file=sys.stderr)
        print("   Expected:", sorted(choices), file=sys.stderr)
        print("        Got:", sorted(names), file=sys.stderr)
        return False
    return True

def chooserListCheck(widgetpath, choices, tolerance=None):
    if choices:
        return treeViewColCheck(widgetpath, 0, choices, tolerance)
    return (treeViewColCheck(widgetpath, 0, ['None']) and
            not gtklogger.findWidget(widgetpath).get_sensitive())
    

def treeViewColCheck(widgetpath, col, choices, tolerance=None):
    # Check that the contents of the given column of a TreeView match
    # the given list of choices.  'widgetpath' is the gtklogger path
    # to the gtk TreeView.  'col' is actually a TreeStore or ListStore
    # column number.
    treeview = gtklogger.findWidget(widgetpath)
    liststore = treeview.get_model()
    if len(liststore) != len(choices):
        print("length mismatch: %d!=%d" % (len(liststore),
                                           len(choices)), file=sys.stderr)
        print("expected: ", choices, file=sys.stderr)
        print("     got: ", [x[col] for x in liststore], file=sys.stderr)
        return False
    for i,x in enumerate(liststore):
        if choices[i] != None:
            if not fp_string_compare(x[col], choices[i], tolerance):
                print(x[col], '!=', choices[i], file=sys.stderr)
                print("expected: ", choices, file=sys.stderr)
                print("     got: ",
                      [x[col] for x in liststore], file=sys.stderr)
                return False
    return True

def treeViewColValues(widgetpath, col):
    treeview = gtklogger.findWidget(widgetpath)
    liststore = treeview.get_model()
    return [x[col] for  x in iter(liststore)]

def treeViewRowValues(widgetpath, row):
    # row can be an int or a list of ints, if the tree is nested
    treeview = gtklogger.findWidget(widgetpath)
    liststore = treeview.get_model()
    treepath = Gtk.TreePath(row)
    model = treeview.get_model()
    return list(model[treepath])

def treeViewSelectCheck(widgetpath, col):
    # Returns the contents of the given column of a TreeStore in the
    # selected row of the given TreeView.
    treeview = gtklogger.findWidget(widgetpath)
    selection = treeview.get_selection()
    model, iter = selection.get_selected()
    if iter is not None:
        return model[iter][col]

def listViewSelectedRowNo(widgetpath):
    # widgetpath must be a TreeView displaying a ListStore.  Returns
    # the index of the selected row, or None if nothing is selected.
    treeview = gtklogger.findWidget(widgetpath)
    selection = treeview.get_selection()
    model, iter = selection.get_selected()
    if iter is not None:
        return model.get_path(iter)[0]
    return None                         # nothing selected

def gtkTextCompare(widgetpath, targettext, tolerance=None):
    # Check the contents of a GtkEntry.  For a GtkTextView, use
    # gtkTextviewCompare.
    gtktxt = gtklogger.findWidget(widgetpath)
    if not gtktxt:
        print("Text widget not found: %s." % widgetpath, file=sys.stderr)
        return False
    sourcetext = gtktxt.get_text().strip()
    if not fp_string_compare(sourcetext, targettext, tolerance):
        print(("Text compare failed for path %s, got >%s<, expected >%s<"
               % (widgetpath, sourcetext, targettext)), file=sys.stderr)
        return False
    return True

# Compare the value of text representing the value of a floating point
# number.
## TODO: This is redundant, now that gtkTextCompare uses
## fp_string_compare.
def gtkFloatCompare(widgetpath, targetval, tolerance=1.e-6):
    gtktxt = gtklogger.findWidget(widgetpath)
    if not gtktxt:
        print("Text widget not found: %s." % widgetpath, file=sys.stderr)
        return False
    sourceval = float(gtktxt.get_text())
    if abs(sourceval - targetval) > tolerance:
        print(("Floating point comparison failed for %s, %g!=%g"
               % (widgetpath, sourceval, targetval)), file=sys.stderr)
        return False
    return True

# Similar to the sensitizationCheck, takes a dictionary of widgets and
# their target texts.  If tolerance is nonzero, floating point
# comparison is done on any numbers found in the strings.
def gtkMultiTextCompare(widgetdict, widgetbase=None, tolerance=None):
    for (wname, ttext) in widgetdict.items():
        if widgetbase:
            w = widgetbase + ":" + wname
        else:
            w = wname
        if not gtkTextCompare(w, ttext, tolerance):
            return False
    return True

# gtkMultiFloatCompare is like gtkMultiTextCompare, but it only
# compares floats, and the values in widgetdict must be numbers, not
# strings.
def gtkMultiFloatCompare(widgetdict, widgetbase=None, tolerance=1.e-6):
    for (wname, val) in widgetdict.items():
        if widgetbase:
            w = widgetbase + ":" + wname
        else:
            w = wname
        if not gtkFloatCompare(w, val, tolerance):
            return False
    return True

def gtkTextviewCompare(widgetpath, targettext, tolerance=None):
    widget = gtklogger.findWidget(widgetpath)
    msgbuffer = gtklogger.findWidget(widgetpath).get_buffer()
    text = msgbuffer.get_text(msgbuffer.get_start_iter(),
                              msgbuffer.get_end_iter(), True)
    if not fp_string_compare(text, targettext, tolerance):
        print(("Textview compare failed for %s, >%s<!=>%s<."
               % (widgetpath, text, targettext)), file=sys.stderr)
        return False
    return True

def gtkTextviewTail(widgetpath, targettext, tolerance=None, quiet=False):
    msgbuffer = gtklogger.findWidget(widgetpath).get_buffer()
    text = msgbuffer.get_text(msgbuffer.get_start_iter(),
                              msgbuffer.get_end_iter(), True)
    if not fp_string_compare_tail(text, targettext, tolerance):
        if not quiet:
            print((f"gtkTextviewTail failed for {widgetpath}\n"
                   f"expected =>{targettext}<=\ngot =>{text}<="),
                  file=sys.stderr)
        return False
    return True

def gtkTextviewHead(widgetpath, targettext):
    msgbuffer = gtklogger.findWidget(widgetpath).get_buffer()
    text = msgbuffer.get_text(msgbuffer.get_start_iter(),
                              msgbuffer.get_end_iter(), True)
    ok = text.startswith(targettext)
    if not ok:
        print((
            "gtkTextviewHead failed for %s: text =>%s< doesn't start with >%s<"
            % (widgetpath, text, targettext)), file=sys.stderr)
    return ok

def gtkTextviewGetLines(widgetpath):
    msgbuffer = gtklogger.findWidget(widgetpath).get_buffer()
    text = msgbuffer.get_text(msgbuffer.get_start_iter(),
                              msgbuffer.get_end_iter(), True).split('\n')
    return text
    
def gtkTextviewGetLine(widgetpath, line):
    return gtkTextviewGetLines(widgetpath)[line]

def gtkTextviewLine(widgetpath, line, targettext):
    if gtkTextviewGetLine(widgetpath, line) != targettext:
        print(("gtkTextviewLine failed for %s: text=  >%s<!=>%s<"
               % (widgetpath, text, targettext)), file=sys.stderr)
        return False
    return True

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Chooser checks

def chooserStateCheck(widgetpath, choice):
    # only for ChooserWidget, not ChooserListWidget.  Checks that the
    # currently selected item is 'choice'.
    stack = gtklogger.findWidget(widgetpath + ":stack")
    current = stack.get_visible_child()
    if current is None:
        return choice is None
    return choice == current.get_children()[0].get_text()


def chooserListStateCheck(widgetpath, choices, tolerance=None):
    # for ChooserListWidget and friends, including MultiListWidget.
    # Checks that everything in the list 'choices' is selected.
    treeview = gtklogger.findWidget(widgetpath)
    selection = treeview.get_selection()
    model, paths = selection.get_selected_rows()
    if len(paths) != len(choices):
        print("Wrong number of selections:",
              len(paths), "!=", len(choices), file=sys.stderr)
        return False
    for path in paths:          # loop over actually selected objects
        val = model[path][0]
        for choice in choices:
            if fp_string_compare(val, choice, tolerance):
                break
        else:
            print("Expected:", choices, file=sys.stderr)
            print("     Got:", [model[p][0] for p in paths], file=sys.stderr)
            return False
    return True

def chooserListStateCheckN(widgetpath, choices):
    # Just like chooserListStateCheck, but choices is a list of integers
    treeview = gtklogger.findWidget(widgetpath)
    selection = treeview.get_selection()
    model, paths = selection.get_selected_rows()
    if len(paths) != len(choices):
        print("Wrong number of selections:",
              len(paths), "!=", len(choices), file=sys.stderr)
        return False
    selected = [p[0] for p in paths]
    if selected == choices:
        return True
    print("Selected rows are", selected, file=sys.stderr)
    return False

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def checkLabelledSlider(widgetpath, value, tolerance=None):
    # value should be a float
    
    # print >> sys.stderr, "checkLabelledSlider: widgetpath=", widgetpath
    # print >> sys.stderr, "checkLabelledSlider: widgets=", gtklogger.findAllWidgets(widgetpath)
    slider = gtklogger.findWidget(widgetpath + ':slider')
    sliderval = slider.get_value()
    diff = abs(sliderval - value)
    if tolerance:
        reltol = 0.5*(abs(sliderval) + abs(value))*tolerance
        sliderok = diff <= reltol or diff <= tolerance
    else:
        sliderok = diff == 0
    entry = gtklogger.findWidget(widgetpath + ':entry')
    entryval = float(entry.get_text().strip())
    diff = abs(entryval - value)
    if tolerance:
        reltol = 0.5*(abs(entryval) + abs(value))*tolerance
        entryok = diff <= reltol or diff <= tolerance
    else:
        entryok = diff == 0

    if entryok and sliderok:
        return True
    print(
        "Labelled slider check failed. Slider=%.8g, text='%s'. Expected %g. tolerance=%s" % \
        (sliderval, entryval, value, tolerance), file=sys.stderr)

def checkSliders(widgetpath, tolerance=None, **params):
    for pname, val in params.items():
        if not checkLabelledSlider(widgetpath+':'+pname, val,
                                   tolerance=tolerance):
            return False
    return True

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Sensitization checks

def is_sensitive(widgetpath):
    return gtklogger.findWidget(widgetpath).is_sensitive()

def menuSensitive(menu, item):
    topmenuwidget = gtklogger.findWidget(menu)
    if not topmenuwidget:
        print("Didn't find widget for", menu, file=sys.stderr)
        raise RuntimeError("Menu sensitization check failed!")
    menuitemwidget = gtklogger.findMenu(topmenuwidget, item)
    if not menuitemwidget:
        print("Didn't find widget for %s:%s" % (menu, item), file=sys.stderr)
        raise RuntimeError("Menu sensitization check failed!!")
    return menuitemwidget.is_sensitive()

def sensitizationCheck(wdict, base=None):
    # Check widget sensitization.  wdict is a dictionary whose keys
    # are the gtklogger paths to widgets and whose values are 0 or 1,
    # indicating whether (1) or not (0) the widget is sensitive.  If
    # provided, base is prepended to each widget path.
    for wname, sense in wdict.items():
        if base:
            path = base + ':' + wname
        else:
            path = wname
        if is_sensitive(path) != sense:
            print("Sensitization test failed for", path, file=sys.stderr)
            return False
    return True

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Skeleton-specific tests

def skeletonNodeSelectionCheck(skeleton, nodelist):
    from ooflib.common.IO import whoville
    sc = whoville.getClass('Skeleton')[skeleton]
    nodes = sc.nodeselection.retrieve()
    nodeindices = sorted([node.index for node in nodes])
    nodelist.sort()
    ok = (nodeindices == nodelist)
    if not ok:
        print(nodeindices, file=sys.stderr)
    return ok

def skeletonElementSelectionCheck(skeleton, elemlist):
    from ooflib.common.IO import whoville
    sc = whoville.getClass('Skeleton')[skeleton]
    elems = sc.elementselection.retrieve()
    elemindices = sorted([el.index for el in elems])
    elemlist.sort()
    ok = (elemindices == elemlist)
    if not ok:
        print(elemindices, file=sys.stderr)
    return ok

def skeletonSegmentSelectionCheck(skeleton, seglist):
    from ooflib.common.IO import whoville
    sc = whoville.getClass('Skeleton')[skeleton]
    segs = sc.segmentselection.retrieve()
    nodepairs = sorted([[n.index for n in seg.nodes()] for seg in segs])
    seglist.sort()
    ok = nodepairs == seglist
    if not ok:
        print(nodepairs, file=sys.stderr)
    return ok

def skeletonSelectionTBSizeCheck(windowname, category, n):
    # Check that the right size is displayed in the Skeleton Selection
    # toolbox. 'category' must be "Element", "Node", or "Segment".
    text = gtklogger.findWidget(
        '%s:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:%s:size' %
        (windowname, category))
    # The line is either "0" or "n (p%)" for some n and p.
    return eval(text.get_text().split()[0]) == n

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Pixel group and selection tests

def pixelSelectionTBSizeCheck(windowname, minpxls, maxpxls=None):
    # Check that the pixel selection size is displayed correctly in
    # the graphics window.  Since different versions of ImageMagick
    # can cause pixel selection operations to work differently after
    # image modifications, it's possible to specify a range of pixel
    # counts for this test.
    text = gtklogger.findWidget(
        '%s:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size' % windowname)
    # The line is either "0" or "n (p%)" for some n and p.
    n = eval(text.get_text().split()[0])
    if maxpxls is None:
        return n == minpxls
    else:
        return minpxls <= n <= maxpxls

def pixelSelectionSizeCheck(msname, n):
    from ooflib.common.IO import whoville
    ms = whoville.getClass('Microstructure')[msname].getObject()
    return ms.pixelselection.size() == n


def pixelGroupSizeCheck(msname, grpname, n):
    from ooflib.common.IO import whoville
    ms = whoville.getClass('Microstructure')[msname].getObject()
    grp = ms.findGroup(grpname)
    return len(grp) == n

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Error message tests

# The exact form of an error message can change from one python
# version to another.  errorMsg() can accept a bunch of expected
# messages, and returns True if one of them matches the contents of
# the error message dialog.
## TODO: It would be better if this explicitly specified which message
## to expect for each python version, but that would break each time a
## new version came out.  This version breaks only when a new message
## format appears.

def errorMsg(*texts):
    for text in texts:
        if gtkTextviewTail('Error:ErrorText', text+'\n', quiet=(len(texts)>1)):
            return True
    # Failed!
    msgbuffer = gtklogger.findWidget('Error:ErrorText').get_buffer()
    realtext = msgbuffer.get_text(msgbuffer.get_start_iter(),
                              msgbuffer.get_end_iter(), True)
    print("errorMsg test failed!", file=sys.stderr)
    print(f"Got =>{realtext}<=", file=sys.stderr)
    return False

# Check the contents of the message window.

def msgTextTail(text):
    return gtkTextviewTail('OOF2 Messages 1:Text', text+'\n')

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Check the state of an Orientation RCF widget.  Since the form of the
# RCF subwidgets depends on the Orientation subclass, this is ugly.
# It might be cleaner if ParameterWidgets knew how to check
# themselves.

def checkOrientationWidget(widgetpath, orClass, tolerance=1.e-5, **orParams):
    if not chooserStateCheck(widgetpath + ':RCFChooser',
                             orClass):
        print("Orientation chooser check failed.", file=sys.stderr)
        return False
    # Orientation subclasses that only use LabelledSliders in their
    # widgets:
    if orClass in("Abg", "X", "XYZ", "Bunge"):
        return checkSliders(widgetpath + ':' + orClass, tolerance=tolerance,
                            **orParams)
    # Orientation subclasses that only use GtkEntries
    if orClass in ("Quaternion", "Rodrigues"):
        return gtkMultiFloatCompare(orParams, widgetpath + ':' + orClass,
                                    tolerance)
    if orClass == "Axis":
        xyz = orParams.copy()
        del xyz['angle']
        return (
            checkLabelledSlider(widgetpath+':Axis:angle', orParams['angle'],
                                tolerance=tolerance)
            and
            gtkMultiFloatCompare(xyz, widgetpath+':Axis', tolerance))
    print("checkOrientationWidget: unknown class", orClass, file=sys.stderr)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Memory leak checker checks for the presence of allocated and
# inventoried C++ objects.

from ooflib.SWIG.common import cmicrostructure
from ooflib.SWIG.engine import cskeleton, femesh
def objectInventory(microstructures=0, nodes=0, elements=0, meshes=0):
    counts = (cmicrostructure.get_globalMicrostructureCount(),
              cskeleton.get_globalNodeCount(),
              cskeleton.get_globalElementCount(),
              femesh.get_globalFEMeshCount())
    expected = (microstructures, nodes, elements, meshes)
    if counts != expected:
        print(
            "objectInventory failed. Expected (micro, nodes, elems, meshes) =",
            expected, "Got", counts, file=sys.stderr)
    return counts == expected
