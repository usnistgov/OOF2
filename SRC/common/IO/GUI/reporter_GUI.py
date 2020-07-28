# -*- python -*-


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 



# Message window, and the GUI part of the error reporting machinery.

from gi.repository import Gtk
from ooflib.SWIG.common import guitop
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import excepthook
from ooflib.common import mainthread
from ooflib.common import thread_enable
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import reporter
from ooflib.common.IO import reportermenu
from ooflib.common.IO.GUI import gfxmenu
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import subWindow
import os
import string
import sys
import time
import traceback

OOF = mainmenu.OOF

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Flag for indicating if we should auto_open. 
_message_window_auto_open = True

allMessageWindows = set()

class MessageWindow(subWindow.SubWindow):
    count = 1
    def __init__(self):
        debug.mainthreadTest()
        self.menu_name = "MessageWindow_%d" % MessageWindow.count
        self.title = "%s Messages %d" % (subWindow.oofname(),
                                         MessageWindow.count)
        self.windows_menu_name = "Message_%d" % MessageWindow.count
        
        subWindow.SubWindow.__init__(
            self, title=self.title, menu=self.menu_name)

        # We are locally responsible for the windows submenu items.
        self.gtk.connect("destroy", self.destroy)

        # raise_window function is provided by the SubWindow class.
        OOF.Windows.Messages.addItem(
            oofmenu.OOFMenuItem(
            self.windows_menu_name,
            help="Raise Message window %d." % MessageWindow.count,
            cli_only=0, no_log=1,
            gui_callback=self.raise_window) )
            
        MessageWindow.count += 1

        allMessageWindows.add(self)

        # Control box, with buttons.  These could be menu items.
        controlframe = Gtk.Frame()
        controlframe.set_shadow_type(Gtk.ShadowType.IN)
        self.mainbox.pack_start(controlframe,
                                expand=False, fill=False, padding=0)
        buttonbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2,
                            margin=2)
        controlframe.add(buttonbox)
        savebutton = gtkutils.StockButton("document-save-symbolic", "Save...",
                                          margin=2)
        savebutton.set_tooltip_text(
            "Save the contents of this window to a file.")
        buttonbox.pack_start(savebutton, expand=False, fill=False, padding=0)
        gtklogger.setWidgetName(savebutton, "Save")
        gtklogger.connect(savebutton, 'clicked', self.saveButtonCB)

        self.button_dict = {}
        self.signal_dict = {}
        for m in reporter.messageclasses:
            button = Gtk.CheckButton(m)
            gtklogger.setWidgetName(button, m)
            buttonbox.pack_end(button, fill=False, expand=False, padding=0)
            self.signal_dict[m] = gtklogger.connect(button, "clicked",
                                                    self.button_click)
            self.button_dict[m] = button
            button.set_tooltip_text(
                "Show or hide "+ reporter.messagedescriptions[m])

        messagepane = Gtk.ScrolledWindow(shadow_type=Gtk.ShadowType.IN)
        ## The ScrolledWindow's scrollbars are *not* logged in the
        ## gui, because blocking the adjustment "changed" signals in
        ## the write_message function, below, doesn't work to suppress
        ## logging.  This means that programmatic changes to the
        ## scrollbars are logged along with user changes, which fills
        ## up the log file with extraneous lines.
        messagepane.set_policy(Gtk.PolicyType.AUTOMATIC,
                               Gtk.PolicyType.AUTOMATIC)
        self.mainbox.pack_start(messagepane, expand=True, fill=True, padding=0)
        self.messages = Gtk.TextView(name="fixedfont",
                                     editable=False,
                                     cursor_visible=False,
                                     left_margin=5, right_margin=5,
                                     top_margin=5, bottom_margin=5)
        gtklogger.setWidgetName(self.messages, "Text")
        self.messages.set_wrap_mode(Gtk.WrapMode.WORD)

        # Get two marks to be used for automatic scrolling
        bfr = self.messages.get_buffer()
        enditer = bfr.get_end_iter()
        self.endmark = bfr.create_mark(None, enditer, False)
        self.midmark = bfr.create_mark(None, enditer, False)

        messagepane.add(self.messages)

        self.state_dict = {}
        for m in reporter.messageclasses:
            self.state_dict[m]=1
            
        self.sbcbs = [
            switchboard.requestCallbackMain("write message",
                                            self.write_message)
            ]

        self.draw()

    def destroy(self, gtkobj):
        global _message_window_auto_open
        allMessageWindows.remove(self)
        _message_window_auto_open = False
        map(switchboard.removeCallback, self.sbcbs)
        OOF.Windows.Messages.removeItem(self.windows_menu_name)

    def draw(self):
        debug.mainthreadTest()
        self.gtk.show_all()
        for (m,v) in self.state_dict.items():
            b = self.button_dict[m]
            self.signal_dict[m].block()
            if v:
                b.set_active(1)
            else:
                b.set_active(0)
            self.signal_dict[m].unblock()
        self.refresh()

    def refresh(self):
        debug.mainthreadTest()
        msgs = []
        self.messages.move_mark_onscreen(self.midmark)
        for m in reporter.messagemanager.all_messages():
            if self.state_dict[m[1]]:
                msgs.append(m[0])
        self.messages.get_buffer().set_text("\n".join(msgs)+"\n")
        self.messages.scroll_mark_onscreen(self.midmark)

    # After each button click, set your local state.
    def button_click(self, gtkobj):
        for (m,b) in self.button_dict.items():
            if b.get_active():
                self.state_dict[m]=1
            else:
                self.state_dict[m]=0
        self.refresh()

    def write_message(self, message_tuple):
        debug.mainthreadTest()
        if self.state_dict[message_tuple[1]]:
            bfr = self.messages.get_buffer()
            bfr.insert(bfr.get_end_iter(), message_tuple[0]+"\n")
            self.messages.scroll_mark_onscreen(self.endmark)
            
    def saveButtonCB(self, button):
        menuitem = OOF.File.Save.Messages
        if parameterwidgets.getParameters(menuitem.get_arg('filename'),
                                          menuitem.get_arg('mode'),
                                          parentwindow=self.gtk,
                                          title="Save Messages"):
            menuitem.callWithDefaults(**self.state_dict)

def raiseMessageWindows():
    for window in allMessageWindows:
        window.raise_window()

# Suppress the message manager's terminal output.
reporter.messagemanager.gui_mode = True

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class WarningPopUp(object):
    # Argument "message" is a single string for the second GtkLabel.
    def __init__(self, message):
        debug.mainthreadTest()
        self.gtk = gtklogger.Dialog(title="%s Warning"%subWindow.oofname(),
                                    parent=guitop.top().gtk)
        gtklogger.newTopLevelWidget(self.gtk, "Warning")

        vbox = self.gtk.get_content_area()
        vbox.set_spacing(3)

        vbox.pack_start(Gtk.Label("WARNING"),
                                 expand=False, fill=False, padding=0)
        vbox.pack_start(Gtk.Label(message),
                                 expand=False, fill=False, padding=0)
        button = gtkutils.StockButton("gtk-ok", "OK")
        self.gtk.add_action_widget(button, Gtk.ResponseType.OK)

        disable_button = Gtk.Button("Disable warnings")
        self.gtk.add_action_widget(disable_button, Gtk.ResponseType.REJECT)

        disable_button.set_tooltip_text(
            "Warnings can be re-enabled in the Help menu of the main window.")

        vbox.show_all()
    def run(self):
        debug.mainthreadTest()
        return self.gtk.run()
    def close(self):
        debug.mainthreadTest()
        self.gtk.destroy()

def _warning_pop_up(message):
    if reporter.messagemanager.get_warning_pop_up():
        popup = WarningPopUp(message)
        result = popup.run()
        popup.close()
        if result == Gtk.ResponseType.REJECT:
            ## This used to call OOF.Help.Popup_warnings(0), but menu
            ## items shouldn't call other menu items, and the warning
            ## was presumably triggered by a menu item, so it can't
            ## call OOF.Help.etc here.
            reporter.messagemanager.set_warning_pop_up(False)

switchboard.requestCallbackMain("messagemanager warning", _warning_pop_up)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# The error pop up optionally allows you to view the traceback,
# and save it to a file.  The file is automatically named.

class ErrorPopUp(object):
    def __init__(self, e_type, value, tbacklist):
        debug.mainthreadTest()
        
        errorstrings = []     # list of strings
        self.tracebacks = []  # list of lists of \n-terminated strings

        # If there are previous unprocessed exceptions, print them
        # too.  The oldest exception is the first in the
        # _savedExceptions list.
        global _savedExceptions
        _savedExceptions.append((e_type, value, tbacklist))
        for e_type, value, tbacklist in _savedExceptions:
            # format_exception_only returns a list of string, each
            # terminated whith a newline.  The list has length 1,
            # except for syntax errors.
            errorstrings.extend(
                [line.rstrip() for line in
                 traceback.format_exception_only(e_type, value)])

            if isinstance(value, ooferror.ErrErrorPtr):
                moreinfo = value.details()
                if moreinfo:
                    errorstrings.append(moreinfo)
            errorstrings.append("") # blank line
            if tbacklist:
                self.tracebacks.append(traceback.format_list(tbacklist))

        _savedExceptions = []

        self.answer = None
        
        self.datestampstring = time.strftime("%Y %b %d %H:%M:%S %Z")
        self.gtk = gtklogger.Dialog(
            title="%s Error" % subWindow.oofname(),
            flags=Gtk.DialogFlags.MODAL,
            parent=guitop.top().gtk,
            border_width=3)
        self.gtk.set_keep_above(True) # might not work
        gtklogger.newTopLevelWidget(self.gtk, "Error")

        vbox = self.gtk.get_content_area()
        vbox.set_spacing(3)

        classname = string.split(str(e_type),'.')[-1]
        vbox.pack_start(Gtk.Label("ERROR"),
                                 expand=False, fill=False, padding=0)

        self.errframe = Gtk.Frame()
        self.errframe.set_shadow_type(Gtk.ShadowType.IN)
        vbox.pack_start(self.errframe,
                                 expand=True, fill=True, padding=0)

        ## TODO GTK3: On Ubuntu, the TextView comes up showing only
        ## half the height of the first line.
        errscroll = Gtk.ScrolledWindow()
        gtklogger.logScrollBars(errscroll, "ErrorScroll")
        errscroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.errframe.add(errscroll)
        self.errbox = Gtk.TextView(name="fixedfont",
                                   wrap_mode=Gtk.WrapMode.WORD,
                                   editable=False,
                                   left_margin=5, right_margin=5,
                                   top_margin=5, bottom_margin=5)
        gtklogger.setWidgetName(self.errbox, "ErrorText")
        errscroll.add(self.errbox)
        self.errbox.get_buffer().set_text("\n".join(errorstrings))

        # Buttons for viewing and saving the traceback.  These can't
        # go in the action area with the OK and Abort buttons because
        # they don't close the dialog.
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2,
                       homogeneous=True)
        vbox.pack_start(hbox, expand=False, fill=False, padding=0)
        self.tracebutton = Gtk.Button("View Traceback")
        gtklogger.setWidgetName(self.tracebutton, "ViewTraceback")
        gtklogger.connect(self.tracebutton, "clicked", self.trace)
        hbox.pack_start(self.tracebutton, expand=False, fill=False, padding=0)
                       
        self.savebutton = gtkutils.StockButton("document-save-symbolic",
                                               "Save Traceback")
        gtklogger.setWidgetName(self.savebutton, "SaveTraceback")
        gtklogger.connect(self.savebutton, "clicked", self.savetrace)
        hbox.pack_start(self.savebutton, expand=False, fill=False, padding=0)

        # OK and Abort buttons
        okbut = gtkutils.StockButton("gtk-ok", "OK")
        okbut.set_can_default(True)
        self.gtk.add_action_widget(okbut,
                                   Gtk.ResponseType.OK)
        self.gtk.add_action_widget(Gtk.Button("Abort"),
                                   Gtk.ResponseType.CLOSE)
        self.gtk.set_default_response(Gtk.ResponseType.OK)


        self.scroll = Gtk.ScrolledWindow()
        gtklogger.logScrollBars(self.scroll, "TraceScroll")
        self.scroll.set_policy(Gtk.PolicyType.AUTOMATIC,
                               Gtk.PolicyType.AUTOMATIC)
        self.scroll.set_shadow_type(Gtk.ShadowType.IN)
        
        self.tracepane = Gtk.TextView(name="fixedfont",
                                      editable=False,
                                      wrap_mode=Gtk.WrapMode.WORD,
                                      left_margin=5, right_margin=5,
                                      top_margin=5, bottom_margin=5)

        self.traceframe = Gtk.Frame()
        self.traceframe.set_shadow_type(Gtk.ShadowType.NONE)
        vbox.pack_start(self.traceframe, expand=False, fill=False, padding=0)

        # Scroll is not added to the frame until the traceback button
        # is pressed.
        self.scroll.add(self.tracepane)

        if self.tracebacks:
            tbtext = ""
            for err, tb in zip(errorstrings, self.tracebacks):
                if tbtext:
                    tbtext += '\n----------\n\n'
                tbtext += err + '\n'
                tbtext += "".join(tb)
            self.tracepane.get_buffer().set_text(tbtext)
            
        else:
            self.savebutton.set_sensitive(False)
            self.tracebutton.set_sensitive(False)

        self.gtk.show_all()


    def close(self):
        debug.mainthreadTest()
        self.gtk.destroy()

    def run(self):
        debug.mainthreadTest()
        # The error dialog's parent window is the main oof window.
        # Make sure it's visible so that the dialog will be visible.
        ## TODO GTK3: This doesn't seem to be necessary.  Check if
        ## it's needed on Linux.
#        guitop.top().gtk.present_with_time(Gtk.get_current_event_time())
        return self.gtk.run()
            
    def trace(self, gtk):
        debug.mainthreadTest()
        vbox = self.gtk.get_content_area()
        c = self.traceframe.get_children()
        if len(c)==0:
            self.traceframe.add(self.scroll)
            self.tracebutton.set_label("Hide Traceback")
            # When the traceback is visible, it expands when the
            # window size changes, and the error box doesn't.
            _switchpacking(vbox, self.errframe)
            _switchpacking(vbox, self.traceframe)
        else:
            self.traceframe.remove(c[0])
            self.tracebutton.set_label("View Traceback")
            # When the traceback isn't visible, the error box expands
            # to fill the window.
            _switchpacking(vbox, self.errframe)
            _switchpacking(vbox, self.traceframe)
        self.gtk.show_all()

    def savetrace(self, gtk):
        debug.mainthreadTest()
        fname = "traceback_oof."+str(os.getpid())
        errbuf = self.errbox.get_buffer()
        try:
            fobj = file(fname, "a+")
            fobj.write("%s\n\n" % self.datestampstring)
            
            tbuf = self.tracepane.get_buffer()
            fobj.write(
                tbuf.get_text(tbuf.get_start_iter(), tbuf.get_end_iter()))
            errbuf.insert(errbuf.get_end_iter(), "\nTraceback written to %s.\n"
                          % fname)
        except IOError:
            errbuf.insert(erfbuf.get_end_iter(),
                          "\nUnable to write traceback.\n")
        self.errbox.scroll_to_iter(errbuf.get_end_iter(), 0.4)

def _switchpacking(parent, child):
    # Toggle the 'expand' and 'fill' gtk packing properties of the
    # child.
    debug.mainthreadTest()
    packinfo = parent.query_child_packing(child)
    parent.set_child_packing(child,
                             expand=not packinfo.expand,
                             fill=not packinfo.fill,
                             padding=packinfo.padding,
                             pack_type=packinfo.pack_type)

# Blocking function, which raises an error pop up, blocks, and returns
# ErrorPopUp.OK if the "OK" button was pressed, and ErrorPopUp.ABORT
# otherwise.

def errorpopup_(e_type, e_value, tbacklist):
    e = ErrorPopUp(e_type, e_value, tbacklist)
    result = e.run()
    e.close()
    return result

#########

## gui_printTraceBack overrides excepthook.displayTraceBack, and is
## called when an exception occurs.

def gui_printTraceBack(e_type, e_value, tbacklist):
    # If the mainloop isn't running yet, just display to the terminal.
    # In debugging mode, always display to the terminal.
    if debug.debug() or not guitop.getMainLoop():
        excepthook.printTraceBack(e_type, e_value, tbacklist)
    if guitop.getMainLoop():
        # Transfer control to the main thread to report errors in the GUI.
        res = mainthread.runBlock(errorpopup_, (e_type, e_value, tbacklist))
        if res == Gtk.ResponseType.CLOSE:
            from ooflib.common.IO.GUI import quit
            # The first argument to doQueryQuit is the window that the
            # Quit dialog box will appear in front of.
            if not mainthread.runBlock(quit.doQueryQuit,
                                       (guitop.top().gtk,),
                                       kwargs=dict(exitstatus=1)):
                sys.exc_clear() # quitting was cancelled
        else:
            # Not aborting.  Clear the exception because it can
            # contain references to objects and prevent garbage
            # collection.
            sys.exc_clear()

excepthook.displayTraceBack = gui_printTraceBack

#########

# subScriptErrorHandler is used as ScriptLoader's exception handler
# when loading a script in GUI mode.  The exception in the "subscript"
# will cause an exception in the calling script, but we only want one
# error dialog to appear.  That dialog must display the traceback from
# both scripts.

_savedExceptions = []      

def subScriptErrorHandler(e_type, e_value, tbacklist):
    _savedExceptions.append((e_type, e_value, tbacklist))
    if debug.debug() or not guitop.getMainLoop():
        excepthook.printTraceBack(e_type, e_value, tbacklist)

mainmenu.subScriptErrorHandler = subScriptErrorHandler

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Override the nonGUI function called by the message-window-creating
# menu callback.
reporter._new_messages = MessageWindow

# Module-level switchboard callback for auto-opening.  Takes an
# argument just because the signal we're using has one.
def _auto_open(message_tuple):
    global _message_window_auto_open
    if _message_window_auto_open and len(allMessageWindows)==0:
        MessageWindow()

switchboard.requestCallbackMain("write message", _auto_open)


