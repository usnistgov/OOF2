# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import guitop
from ooflib.common import debug
from ooflib.common import thread_enable
from ooflib.common import utils
from ooflib.common.IO import filenameparam
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import reporter
from ooflib.common.IO import parameter
from ooflib.common.IO import progressbar_delay
from ooflib.common.IO import xmlmenudump
from ooflib.common.IO.GUI import activityViewer
from ooflib.common.IO.GUI import gtklogger

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import os
import sys
import traceback

guidebugmenu = mainmenu.debugmenu.addItem(oofmenu.OOFMenuItem(
    "GUI_Logging",
    ordering=1000,
    no_log=True,
    post_hook=None,
    help="Record and replay log files of GUI sessions.",
    discussion="""<para>
    These commands are the &oof2; interface to <ulink
    url="https://www.ctcms.nist.gov/oof/gtklogger">gtklogger</ulink>,
    a tool for recording and replaying log files of GUI sessions.
    Tests can be added to the log files to ensure that the GUI is
    functioning correctly.  This is the mechanism of the
    <application>oof2-guitest</application> program.
    </para>
    """
))

###################################

# menucheckpoint is installed as the main menu's post_hook function.
# It's run after every menu command, and inserts a checkpoint in the
# log file.

def menucheckpoint(menuitem, successful):
    # successful==True means that the menuitem's callback didn't raise
    # an exception.
    gtklogger.checkpoint(menuitem.path())

##################################

_recording = False
_replaying = False

def recording():
    return _recording

def replaying():
    return _replaying

def logFinished():                      # called by GUILogPlayer when done
    global _replaying
    _replaying = False
    if not recording():
        mainmenu.OOF.removeOption('post_hook')
    debug.fmsg("Finished replaying gui log file.")

############################
    
def startLog(menuitem, filename, use_gui): 
    gtklogger.reset_checkpoints()
    menuitem.root().setOption('post_hook', menucheckpoint)
    if debug.debug():
        dblevel = 3
    else:
        dblevel = 0
    global _recording
    _recording = True
    gtklogger.start(filename, debugLevel=dblevel, comment_gui=use_gui)

guidebugmenu.addItem(oofmenu.OOFMenuItem(
    'Record',
    callback=startLog,
    params=[filenameparam.WriteFileNameParameter(
                'filename', ident='guilog', tip="Name of the file."),
            parameter.BooleanParameter(
                'use_gui', True, tip="Use the logger gui to insert comments?")
            ],
    ellipsis=1,
    help="Save GUI events in a log file.",
    discussion=xmlmenudump.emptyDiscussion
    ))

############################

def stopLog(menuitem):
    debug.mainthreadTest()
    global _recording
    _recording = False
    menuitem.root().removeOption('post_hook')
    gtklogger.stop()

guidebugmenu.addItem(oofmenu.OOFMenuItem(
    'Stop',
    callback=stopLog,
    no_log=1,
    threadable=oofmenu.UNTHREADABLE,
    help="Stop recording GUI events",
    discussion=xmlmenudump.emptyDiscussion))

############################

# loggererror is installed as the gtklogger handler for exceptions
# that occur during playback.  Currently commented out because it
# doesn't seem to be necessary.  Pre-gtk3, we had locks that
# interfered with normal exception handling and required a special
# handler during gui playback.

# def loggererror(exc, line):
#     from ooflib.common.IO.GUI import reporter_GUI
#     type, value, tb = sys.exc_info()
#     tblist = traceback.extract_tb(tb)
#     reporter_GUI.gui_printTraceBack(type, value, tblist)
#     return True

####

def loadLog(menuitem, filename, checkpoints):
    if gtklogger.replaying():
        raise ooferror.PyErrUserError(
            "Multiple GUI logs cannot be replayed simultaneously!")
    debug.fmsg("Loading gui script", filename)
    menuitem.root().setOption('post_hook', menucheckpoint)
    dblevel = 0
    if debug.debug():
        dblevel = 3
    #dblevel = 4
    global _replaying
    _replaying = True

    # When replaying, we have to make sure that progress bars *always*
    # appear, so we set the delay time to 0.  If the delay time is
    # non-zero, then a script recorded on a slow machine would insert
    # a checkpoint for opening the activity viewer window, but a
    # faster machine might never open the window, and would wait
    # forever for the checkpoint when replaying the script.
    progressbar_delay.set_delay(None, 0)

    gtklogger.replay(
        filename,
        beginCB=activityViewer.openActivityViewer,
        finishCB=logFinished,
        debugLevel=dblevel,
        threaded=thread_enable.query(),
        #exceptHook=loggererror,
        checkpoints=checkpoints)

guidebugmenu.addItem(oofmenu.OOFMenuItem(
    'Replay',
    callback=loadLog,
    params=[filenameparam.ReadFileNameParameter('filename', ident='guilog',
                                                tip="Name of the file."),
            parameter.BooleanParameter('checkpoints', True,
                                       tip='obey checkpoints?')
            ],
    ellipsis=1,
    help="Load a GUI log file.",
    discussion=xmlmenudump.emptyDiscussion))

##############################

def rerecordLog(menuitem, filename, checkpoints, use_gui):
    if gtklogger.replaying():
        raise ooferror.PyErrUserError(
            "Multiple GUI logs cannot be replayed simultaneously!")
    menuitem.root().setOption('post_hook', menucheckpoint)
    dblevel = 0
    if debug.debug():
        dblevel = 3
    #dblevel = 4
    global _replaying, _recording
    _replaying = True
    _recording = True
    progressbar_delay.set_delay(None, 0)

    # Find a suitable new name for the backup copy of the old log
    # file.  Just append ".bak", but if that file already exists,
    # append ".bakX", where X is an integer.
    if not os.path.exists(filename + '.bak'):
        backupname = filename + '.bak'
    else:
        backupname = None
        count = 2
        while not backupname:
            trialname = "%s.bak%d" % (filename, count)
            if not os.path.exists(trialname):
                backupname = trialname
            count += 1
    os.system('cp '+filename+' '+backupname)
    debug.fmsg("Loading gui script", backupname)

    gtklogger.replay(
        backupname,
        beginCB=activityViewer.openActivityViewer,
        finishCB=logFinished,
        debugLevel=dblevel,
        threaded=thread_enable.query(),
        #exceptHook=loggererror,
        rerecord=filename,
        checkpoints=checkpoints,
        comment_gui=use_gui)

guidebugmenu.addItem(oofmenu.OOFMenuItem(
    'Rerecord',
    callback=rerecordLog,
    params=[
        filenameparam.FileNameParameter('filename', ident='guilog',
                                        tip='Name of the log file'),
        parameter.BooleanParameter('checkpoints', True,
                                   tip='obey checkpoints?'),
        parameter.BooleanParameter('use_gui', True,
                                   tip="Use the logger gui to insert comments?")
            ],
    ellipsis=1,
    help="Load and rerecord a GUI log file.",
    discussion=xmlmenudump.emptyDiscussion))

#####################

def sanity_check(menuitem):
    gtklogger.comprehensive_sanity_check()

guidebugmenu.addItem(oofmenu.OOFMenuItem(
    'Sanity_Check',
    callback=sanity_check,
    no_log=1,
    help="Check that widget names are unique.",
    discussion=xmlmenudump.emptyDiscussion))


############################

# Selecting 'Pause' from the logger menu when recording will cause the
# program to pause on playback until the Continue button is pressed.
# Clicks on the Continue button are *not* recorded, so that playback
# won't proceed without user intervention.

def pauseLog(menuitem):
    pass

def pauseGUI(menuitem):
    dialog = Gtk.Dialog(modal=True, transient_for=guitop.top())
    dialog.set_title("OOF2 Pause")
    content = dialog.get_content_area()
    content.pack_start(Gtk.Label(label="Continue?"),
                       expand=True, fill=True, padding=2)
    dialog.add_action_widget(gtkutils.StockButton("gtk-ok", "OK"),
                             Gtk.ResponseType.OK)
    dialog.show_all()
    result = dialog.run()
    dialog.destroy()
    menuitem.callWithDefaults()

guidebugmenu.addItem(oofmenu.OOFMenuItem(
    'Pause',
    callback=pauseLog,
    gui_callback=pauseGUI,
    help="Stop replaying until the 'Continue' button is pressed.",
    discussion=xmlmenudump.emptyDiscussion))

############################

# Save some typing in the Console window when debugging.

utils.OOFdefine('findAllWidgets', gtklogger.findAllWidgets)
utils.OOFdefine('findWidget', gtklogger.findWidget)
