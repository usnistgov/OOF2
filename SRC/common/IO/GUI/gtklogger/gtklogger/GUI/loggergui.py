# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

## This is a gui for gtklogger, to be used when recording log files.
## It must be run as a separate process, not as part of the program
## being instrumented.  The output from gtklogger should be piped to
## this program.  This program takes the name of the log file as a
## command line argument.

## The gui allows comments to be inserted into the log file as the log
## is recorded, making it easier to instrument it later.  It also can
## filter the log file to remove redundant lines.

## TODO GTK3: This isn't quitting on EOF on Linux.

## TODO GTK3: If log lines all ended with a comment indicating their
## origin, the postprocessing done here could be more specific.  For
## example, it could act only on resize events for certain types of
## widgets.

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GObject
from gi.repository import Gtk
import sys
import re

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Filtering

# actions is a list of functions that take a log line and the
# LogProcessor as arguments, and tell the LogProcessor what to do with
# the line by calling the appropriate LogProcessor method
# (replaceLine, addLine, etc).  The actions return True if the line
# has been handled in some way.  They should return False if they
# don't know how to handle the line, in which case other actions will
# get a chance to handle it.  If no actions can handle a line, the
# line is simply appended to the output.

actions = []

# ReplaceLine constructs an action for the situation in which the
# previously added line is replaced by the current line. The
# replacement is done if the current line matches the regular
# expression in regexp and the previous line matches the one in
# regexpprev.  If regexpprev is omitted, the replacement is done if
# both lines match regexp.  groups is a list of pairs of integers.
# For each (i,j) in the list, the replacement is done only if group i
# in the current line is identical to group j in the previous line.

class ReplaceLine(object):
    def __init__(self, regexp, regexpprev=None, groups=[]):
        self.regexp = re.compile(regexp)
        if regexpprev is None:
            self.regexpprev = self.regexp
        else:
            self.regexpprev = re.compile(regexpprev)
        self.groups = groups
    def __call__(self, line, logProc):
        lastLine = logProc.lastLine()
        if lastLine is not None:
            match = self.regexp.match(line)
            if match is None:   # not what we're looking for
                return False
            lastMatch = self.regexpprev.match(lastLine)
            if lastMatch is None:
                return False
            # line and lastLine fit the pattern.  Are their groups the same?
            for grp in self.groups:
                if match.group(grp[0]) != lastMatch.group(grp[1]):
                    # The lines fit the templates, but their data
                    # (groups) is different.
                    logProc.addLine(line)
                    return True
            # groups are the same.  Replace the previous line.
            logProc.replaceLastLine(line)
            return True         # line was handled successfully.
        return False            # line was not dealt with.

# Look for pairs of lines like
#   findWidget('WIDGETNAME').resize(x0, y0)
#   findWidget('WIDGETNAME').resize(x1, y1)
# and delete the first one.
actions.append(
    ReplaceLine(
        r"^findWidget\('(.+)'\).resize\([0-9]+, [0-9]+\)$",
        groups=[(1,1)]))

# Look for pairs of lines like
#    findWidget('MENUNAME').deactivate()
#    findMenu(findWidget('MENUNAME'), MENUITEM).activate()
# and delete the first one.  This occurs when an item is selected from
# a menu.  The menu's deactivate signal is sent before the menu item
# is activated, but on replay the menu must not be destroyed before
# its item is activated.  Activating the menu item will deactivate the
# menu, so explicit deactivation isn't necessary.

actions.append(
    ReplaceLine(
        r"^findMenu\(findWidget\('(.+)'\), '.+'\).activate\(\)$",
        r"^findWidget\('(.+)'\).deactivate\(\)$",
        groups=[(1,1)]))

# Look for pairs of lines like
#   findWidget('MENUNAME').deactivate()
#   findMenu(findWidget('MENUNAME'), MENUITEM).set_active(BOOL)
# and delete the first one.  This is just like the case above, but for
# CheckMenuItems and RadioMenuItems.
actions.append(
    ReplaceLine(
        r"^findMenu\(findWidget\('(.+)'\), '.+'\).set_active\(0|1|True|False\)$",
        r"^findWidget\('(.+)'\).deactivate\(\)$",
        groups=[(1,1)]))
    
# Replace repeated set_position events from Paned widgets
actions.append(
    ReplaceLine(
        r"^findWidget\('(.+)'\).set_position\([0-9]+\)$",
        groups=[(1,1)]))

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class LogProcessor(object):
    def __init__(self, logfilename):
        self.logfilename = logfilename
        self.inbuf = ""
        self.lines = []
        self.strikeThrough = True # TODO: make this settable in the GUI

        window = Gtk.Window(Gtk.WindowType.TOPLEVEL,
                            title="gtklogger:" + logfilename)
        window.connect('delete-event', self.quit)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2, margin=5)
        window.add(box)

        logscroll = Gtk.ScrolledWindow()
        logscroll.set_shadow_type(Gtk.ShadowType.IN)
        box.pack_start(logscroll, expand=True, fill=True, padding=0)
        self.logtextview = Gtk.TextView(editable=False, cursor_visible=False)
        self.logtextview.set_wrap_mode(Gtk.WrapMode.WORD)
        logscroll.add(self.logtextview)

        commentbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                             spacing=2)
        box.pack_start(commentbox, expand=False, fill=False, padding=0)
        
        self.commentText = Gtk.Entry()
        commentbox.pack_start(self.commentText,
                              expand=True, fill=True, padding=0)
        
        self.commentButton = Gtk.Button("Comment")
        commentbox.pack_start(self.commentButton, expand=False, fill=False,
                              padding=0)
        self.commentButton.connect('clicked', self.commentCB)

        self.clearButton = Gtk.Button('Clear')
        commentbox.pack_start(self.clearButton, expand=False, fill=False,
                              padding=0)
        self.clearButton.connect('clicked', self.clearCB)

        GObject.io_add_watch(sys.stdin, GObject.IO_IN, self.inputHandler)

        window.show_all()
        
    def inputHandler(self, source, condition):
        line = sys.stdin.readline()
        if not line:
            self.quit()
            return False
        if line[-1] == '\n':
            fullline = self.inbuf + line
            self.handleLine(fullline.rstrip())
            self.inbuf = ""
        else:
            self.inbuf += line
        return True

    def handleLine(self, line):
        # Decide what to do with this line.  It can be appended to the
        # existing lines, replace the previous line, or be discarded.
        for action in actions:
            if action(line, self):
                return
        # No actions applied.  Just append to the output.
        self.addLine(line)

    def addLine(self, line):
        self.lines.append(line)
        bfr = self.logtextview.get_buffer()
        bfr.insert(bfr.get_end_iter(), line+"\n")
        self.scrollToEnd()

    def replaceLastLine(self, line):
        if self.lines:
            # Delete the last line, then add the new one.
            bfr = self.logtextview.get_buffer()
            lastLineIter = bfr.get_iter_at_line(len(self.lines)-1)
            endIter = bfr.get_end_iter()
            del self.lines[-1]  # delete previous last line from output
            if self.strikeThrough:
                # If strikeThrough is True, then the deleted line is
                # still displayed, but crossed out.
                lastLine = bfr.get_text(lastLineIter, endIter, True).rstrip()
                bfr.delete(lastLineIter, endIter)
                markup = ('<span strikethrough="t" strikethrough-color="red">'
                          + lastLine
                          + '</span>\n')
                bfr.insert_markup(bfr.get_end_iter(), markup , -1);

            else:
                # strikeThrough is False.  Don't display the deleted line.
                bfr.delete(lastLineIter, endIter)
        self.addLine(line)


    def scrollToEnd(self):
        bfr = self.logtextview.get_buffer()
        mark = bfr.create_mark(None, bfr.get_end_iter())
        self.logtextview.scroll_mark_onscreen(mark)
        bfr.delete_mark(mark)

    def lastLine(self):
        if self.lines:
            return self.lines[-1]
    
    def quit(self, *args):
        Gtk.main_quit()
    
    def clearCB(self, button):
        self.commentText.set_text("")

    def commentCB(self, button):
        self.addLine("# " + self.commentText.get_text())

    def writeLog(self):
        logfile = file(self.logfilename, "w")
        for line in self.lines:
            print >> logfile, line
        logfile.close()

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def start(filename):
    logproc = LogProcessor(filename)
    Gtk.main()
    logproc.writeLog()
    
if __name__ == "__main__":
    # The one argument is the name of the log file to be created.
    start(sys.argv[1])
