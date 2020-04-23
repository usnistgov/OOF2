# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import ringbuffer
from ooflib.common import utils
from ooflib.common.IO import filenameparam
from ooflib.common.IO import parameter
from ooflib.common.IO import reporter
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import guilogger
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import widgetscope
import cgi
from gi.repository import Gtk
import os
import os.path
import re
import string
import weakref

# FileSelectorWidget and friends.

## TODO: Typing <return> in the File entry should be the same as
## clicking "OK".  (This is hard to do. The OK button is part of a
## generic ParameterDialog, but the FileSelector is just a widget in
## the dialog box.  We don't have a mechanism for the widgets to talk
## to the ParameterDialog buttons.)  The FileSelector could
## conceivably be used outside of a dialog box.


# When using gtklogger, the WriteFileSelectorWidget and
# ReadFileSelectorWidget are inconvenient.  Because the files are
# listed in a TreeView (inside the ScrolledChooserListWidget), when a
# file is selected the corresponding row number of the TreeView is
# logged.  If files are added or removed to the directory, the correct
# row number will change, breaking the test script.  So when recording
# or replaying, we replace the fancy FileSelectorWidget machinery with
# a simple StringWidget, which doesn't have this problem.  However, if
# useFakeFileSelector is False, the fake selector won't be used even
# in gui test mode.
from ooflib.common import runtimeflags
useFakeFileSelector = runtimeflags.useFakeFileSelector

# Globals _last_file and _last_dir are dictionaries used to initialize
# FileSelectorWidgets to the final state of the previous widget with
# the same 'ident'.  _last_hid is a dictionary indicating whether or
# not the previous widget with the same ident was listing hidden
# files.
_last_file = {}
_last_dir = {}
_last_hid = {}


class FileSelectorWidget(parameterwidgets.ParameterWidget):
    
    # Base class for ReadFileSelectorWidget and WriteFileSelectorWidget.
    
    def __init__(self, param, scope=None, name=None, ident=None, **kwargs):

        debug.mainthreadTest()
        self.ident = ident or param.ident

        self.lastFile = {}      # last file selected in each directory
        self.fileNames = []     # files in the current directory
        self.dirHier = []       # directories in the current hierarchy
        self.dirHistory = ringbuffer.RingBuffer(50)

        quargs = kwargs.copy()
        quargs.setdefault('margin', 2)
        parameterwidgets.ParameterWidget.__init__(
            self, Gtk.Frame(**quargs), scope, name, expandable=True)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                       margin=2)
        self.gtk.add(vbox)

        # Directory selector
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        vbox.pack_start(hbox, expand=False, fill=False, padding=0)
        hbox.pack_start(Gtk.Label("Directory:"), expand=False, fill=False,
                        padding=0)
        self.dirWidget = chooser.ChooserComboWidget([],
                                                    callback=self.dirChangedCB, 
                                                    name="Directory")
        hbox.pack_start(self.dirWidget.gtk, expand=True, fill=True, padding=0)

        # Directory selection buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                        homogeneous=False, spacing=2)
        vbox.pack_start(hbox, expand=False, fill=False, padding=0)

        self.backbutton = gtkutils.StockButton('go-previous-symbolic', "Back",
                                               halign=Gtk.Align.START)
        gtklogger.setWidgetName(self.backbutton, "Back")
        gtklogger.connect(self.backbutton, 'clicked', self.backCB)
        hbox.pack_start(self.backbutton, expand=True, fill=True, padding=0)

        self.addDirButtons(hbox)

        homebutton = gtkutils.StockButton('go-home-symbolic')
        gtklogger.setWidgetName(homebutton, "Home")
        gtklogger.connect(homebutton, 'clicked', self.homeCB)
        hbox.pack_start(homebutton, expand=False, fill=True, padding=0)

        self.nextbutton = gtkutils.StockButton("go-next-symbolic", "Next",
                                               reverse=True,
                                               halign=Gtk.Align.END)
        gtklogger.setWidgetName(self.nextbutton, "Next")
        gtklogger.connect(self.nextbutton, 'clicked', self.nextCB)
        hbox.pack_start(self.nextbutton, expand=True, fill=True, padding=0)

        # File list
        self.fileList = chooser.ScrolledChooserListWidget(
            name="FileList",
            callback=self.fileListCB, 
            dbcallback=self.fileListDoubleCB,
            markup=True)
        self.fileList.gtk.set_size_request(-1, 100)
        vbox.pack_start(self.fileList.gtk, expand=True, fill=True, padding=0)
        # Set the comparison function used when typing in the file
        # list.  _filename_cmp matches the beginnings of file names,
        # ignoring the markup added to directories and escaped
        # characters.
        self.fileList.treeview.set_search_equal_func(_filename_cmp, None)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                       halign=Gtk.Align.START, spacing=2)
        vbox.pack_start(hbox, expand=False, fill=False, padding=0)
        label = Gtk.Label("show hidden files", halign=Gtk.Align.START)
        hbox.pack_start(label, expand=False, fill=False, padding=0)
        self.hiddenButton = Gtk.CheckButton()
        hbox.pack_start(self.hiddenButton, expand=False, fill=False, padding=0)
        gtklogger.setWidgetName(self.hiddenButton, "ShowHidden")
        gtklogger.connect(self.hiddenButton, 'clicked', self.showHiddenCB)
        
        # Include additional widgets required by subclasses.
        self.addMoreWidgets(vbox)

        # Set initial state.
        if param.value is not None:
            directory, phile = os.path.split(param.value)
            # param.value might not have a directory component,
            # especially if the last value was set by a script or
            # command line argument.
            if not directory or not os.path.isdir(directory):
                directory = _last_dir.get(self.ident,
                                          os.path.abspath(os.getcwd()))
        else:
            directory = _last_dir.get(self.ident,
                                      os.path.abspath(os.getcwd()))
            phile = _last_file.get(self.ident, None)
        self.hiddenButton.set_active(_last_hid.get(self.ident, False))
        directory = endSlash(directory)
        self.lastFile[directory] = phile
        self.dirHistory.push(directory)
        self.dirWidget.suppress_signals()
        self.dirHier = getDirectoryHierarchy(directory)
        self.dirWidget.update(self.dirHier)
        self.dirWidget.set_state(directory)
        self.dirWidget.allow_signals()

        self.fileList.suppress_signals()
        self.updateFiles(directory)
        if phile:
            self.fileList.set_selection(phile)
        self.fileList.allow_signals()

        self.initializeExtras(directory, phile)
        
        self.sensitize()
        self.widgetChanged(self.checkValidity(), interactive=False)

    def show(self):
        parameterwidgets.ParameterWidget.show(self)
        # Don't let the directory widget have the focus.
        self.fileList.grab_focus()

    def cwd(self):              # Current working directory
        directory = self.dirWidget.get_value()
        if directory == "":
            # Return "" if directory is "".  normpath would return "."
            return ""
        return endSlash(os.path.normpath(directory))

    def updateHierarchy(self, directory):
        # Update the directory hierarchy in the pull down menu part of
        # the ChooserComboWidget.  *Don't* change the hierarchy if the
        # new directory is in the old hierarchy.  This lets the user
        # move up and down the hierarchy easily.
        if directory not in self.dirHier:
            newhier = getDirectoryHierarchy(directory)
            self.dirWidget.update(newhier)
            self.dirHier = newhier

    def updateFiles(self, directory):
        debug.mainthreadTest()
        # Update the displayed list and the internal list of files in
        # the current directory.
        self.fileNames = os.listdir(directory)
        if not self.hiddenButton.get_active():
            self.fileNames = [f for f in self.fileNames if f[0] != "."]
        self.fileNames.sort()
        displaylist = [_addMarkup(directory, filename)
                       for filename in self.fileNames]
        self.fileList.update(objlist=self.fileNames, displaylist=displaylist)
        # Make sure that the last file visited is still there.
        try:
            if self.lastFile[directory] not in self.fileNames:
                del self.lastFile[directory]
        except KeyError:
            pass

    def switchDir(self, directory):
        debug.mainthreadTest()
        # switchDir is called when double-clicking a directory name in
        # the fileList, when typing a directory name in the fileEntry,
        # or after creating a new directory.  In all cases, both the
        # directory widget and the file widgets need to be updated.
        directory = endSlash(directory)
        self.fileList.suppress_signals()
        self.dirWidget.suppress_signals()
        try:
            self.updateHierarchy(directory)
            self.dirWidget.set_state(directory)
            self.updateFiles(directory)
            _last_dir[self.ident] = directory
            self.setLastFile(directory)
            self.sensitize()
            self.widgetChanged(self.checkValidity(), interactive=True)
        finally:
            self.dirWidget.allow_signals()
            self.fileList.allow_signals()


    def sensitize(self):
        debug.mainthreadTest()
        self.backbutton.set_sensitive(not self.dirHistory.atBottom())
        self.nextbutton.set_sensitive(not self.dirHistory.atTop())
        directory = self.cwd()
        dirok = os.path.isdir(directory)
        self.fileList.gtk.set_sensitive(dirok)
        self.sensitizeExtras(directory)

    # Callbacks

    def dirChangedCB(self, val): # directory widget callback
        directory = self.cwd()   # adds trailing slash if needed
        ## Don't do anything except sensitize widgets if the new
        ## directory isn't valid, or isn't different from the old one.
        ## Typing in the directory widget may cause it to be set to
        ## something that's not a directory.  Adding or deleting a "/"
        ## doesn't actually change the directory.
        if os.path.isdir(directory) and directory!=self.dirHistory.current():
            self.dirHistory.push(directory)
            _last_dir[self.ident] = directory
            self.updateFiles(directory)
            self.setLastFile(directory)
            self.dirWidget.suppress_signals()
            try:
                self.updateHierarchy(directory)
            finally:
                self.dirWidget.allow_signals()
        self.sensitize()
        self.widgetChanged(self.checkValidity(), interactive=True)

    def backCB(self, button):
        self.switchDir(self.dirHistory.prev())

    def nextCB(self, button):
        self.switchDir(self.dirHistory.next())

    def homeCB(self, button):
        directory = os.path.expanduser("~")
        self.dirHistory.push(directory)
        self.switchDir(directory)

    def fileListCB(self, filename, interactive):
        debug.mainthreadTest()
        if len(self.dirHistory) == 0: # not initialized yet
            return
        if filename:
            self.lastFile[self.dirHistory.current()] = filename
            _last_file[self.ident] = filename
        self.fileListCBextras(filename)
        self.widgetChanged(self.checkValidity(), interactive)

    def showHiddenCB(self, button):
        _last_hid[self.ident] = button.get_active()
        self.updateFiles(self.dirHistory.current())

    def fileListDoubleCB(self, filename):
        debug.mainthreadTest()
        self.lastFile[self.dirHistory.current()] = filename
        filepath = os.path.join(self.dirWidget.get_value(), filename)
        if os.path.isdir(filepath):
            self.dirHistory.push(endSlash(filepath))
            self.switchDir(filepath)

class ReadFileSelectorWidget(FileSelectorWidget):
    def addDirButtons(self, hbox):
        pass
    def addMoreWidgets(self, vbox):
        pass
    def initializeExtras(self, directory, phile):
        pass
    def sensitizeExtras(self, directory):
        pass
    def setLastFile(self, directory):
        debug.mainthreadTest()
        # Set the file list and file entry to the name of the last
        # file visited in this directory, if any.  Called whenever the
        # directory changes.
        try:
            name = self.lastFile[directory]
        except KeyError:    # no last file
            self.fileList.set_selection(None)
            self.fileList.scroll_to_line(0)
            _last_file[self.ident] = None
        else:
            self.fileList.set_selection(name)
            _last_file[self.ident] = name
    def get_value(self):
        return os.path.join(self.cwd(), self.fileList.get_value())
    def checkValidity(self):
        filename = self.fileList.get_value()
        return (filename is not None and 
                os.path.isfile(os.path.join(self.cwd(), filename)))
    def fileListCBextras(self, filename):
        pass
    

class WriteFileSelectorWidget(FileSelectorWidget):

    ## TODO: Add an option for forbidding append mode.  It doesn't
    ## make sense to append to some types of files (such as images).

    def addDirButtons(self, hbox): # directory navigation buttons
        self.newdirbutton = gtkutils.StockButton('folder-new-symbolic', "New")
        gtklogger.setWidgetName(self.newdirbutton, "NewDir")
        gtklogger.connect(self.newdirbutton, 'clicked', self.newdirCB)
        hbox.pack_start(self.newdirbutton, expand=False, fill=True, padding=0)

    def addMoreWidgets(self, vbox): # Widgets below the file list.
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        vbox.pack_start(hbox, expand=False, fill=False, padding=0)
        label = Gtk.Label('File:')
        hbox.pack_start(Gtk.Label('File:'), expand=False, fill=False, padding=0)
        self.fileEntry = Gtk.Entry()
        gtklogger.setWidgetName(self.fileEntry, 'File')
        self.fileEntrySignal = gtklogger.connect(self.fileEntry, 'changed',
                                                 self.entryChangeCB)
        hbox.pack_start(self.fileEntry, expand=True, fill=True, padding=0)

        # Add file-name completion in the fileEntry widget.  The
        # fileList already has file-name completion in it.
        self.completion = Gtk.EntryCompletion()
        self.fileEntry.set_completion(self.completion)
        self.completion.set_model(self.fileList.liststore)
        self.completion.set_text_column(0)

    def show(self):
        FileSelectorWidget.show(self)
        # If the file entry widget doesn't grab focus here, then the
        # directory entry widget will have it, and careless users will
        # overwrite the directory name.
        self.fileEntry.grab_focus()

    def initializeExtras(self, directory, phile):
        if phile:
            self.fileEntrySignal.block()
            try:
                self.fileEntry.set_text(phile)
            finally:
                self.fileEntrySignal.unblock()

    def sensitizeExtras(self, directory):
        self.fileEntry.set_sensitive(os.path.isdir(directory))

    def setLastFile(self, directory):
        debug.mainthreadTest()
        # Set the file list and file entry to the name of the last
        # file visited in this directory, if any.  Called whenever the
        # directory changes.
        self.fileEntrySignal.block()
        try:
            try:
                name = self.lastFile[directory]
            except KeyError:    # no last file
                self.fileEntry.set_text("")
                self.fileList.set_selection(None)
                self.fileList.scroll_to_line(0)
                _last_file[self.ident] = None
            else:
                self.fileEntry.set_text(name)
                self.fileList.set_selection(name)
                _last_file[self.ident] = name
        finally:
            self.fileEntrySignal.unblock()

    def get_value(self):
        debug.mainthreadTest()
        phile = os.path.join(self.cwd(), self.fileEntry.get_text())
        if not os.path.isdir(phile):
            return phile
        else:
            return None

    def checkValidity(self):
        debug.mainthreadTest()
        directory = self.cwd()
        filename = os.path.join(directory, self.fileEntry.get_text())
        return (os.path.isdir(directory) and 
                filename != "" and filename is not None and
                not os.path.isdir(filename))

    def newdirCB(self, button):
        dirnameparam = parameter.StringParameter('directory name')
        if parameterwidgets.getParameters(dirnameparam,
                                          title="New Directory"):
            if dirnameparam.value[0] != os.sep:
                dirname = os.path.join(self.cwd(), dirnameparam.value)
            else:
                dirname = dirnameparam.value
            os.mkdir(dirname)   # raises exception if file exists
            self.dirHistory.push(dirname)
            self.switchDir(dirname)

    def entryChangeCB(self, entry): # Typing in the file entry widget
        debug.mainthreadTest()
        self.widgetChanged(self.checkValidity(), interactive=True)
        # Set fileList, if typing matches
        filename = self.fileEntry.get_text()
        if filename in self.fileNames:
            self.fileList.set_selection(filename)
            _last_file[self.ident] = filename
        else:
            self.fileList.set_selection(None)
            if filename:
                # Scroll to the last match for the current text.
                ## TODO: Is this going to be too slow for large
                ## directories?  The linear search may be inappropriate.
                # It would be cleaner to use 'reversed(enumerate(names))',
                # but reversed doesn't work on iterators.
                for rlineno, fname in enumerate(reversed(self.fileNames)):
                    if fname.startswith(filename):
                        self.fileList.scroll_to_line(
                            len(self.fileNames)-rlineno-1)
          
    ## See comment about about handling <return>.
#     def entryActivateCB(self, entry): 
#         pass

    def fileListCBextras(self, filename):
        self.fileEntrySignal.block()
        try:
            self.fileEntry.set_text(filename or "")
            self.fileEntry.set_position(-1) # cursor at end
        finally:
            self.fileEntrySignal.unblock()
        
    
# Utility functions used by FileSelectorWidget

def _addMarkup(directory, filename):
    if filename and os.path.isdir(os.path.join(directory, filename)):
        return "<b>" + cgi.escape(filename) + "</b>"
    return cgi.escape(filename)

def _filename_cmp(model, column, key, iter, data):
    # Comparisons made while searching in the file list use the raw
    # file name, in column 1 of the model, instead of the marked-up
    # file name in column 0.
    name = model[iter][1]
    return not name.startswith(key)

def endSlash(dirname):
    # Make sure all directory names end consistently with "/" so that
    # string comparisons on them don't fail because of inconsequential
    # ending slashes.
    if not dirname:
        return os.sep
    if (dirname[-1] == os.sep or dirname.endswith(os.sep+".") or
        dirname.endswith(os.sep+"..")):
        return dirname
    return dirname + os.sep

def getDirectoryHierarchy(directory):
    # Return a list of all directories in the hierarchy from root
    # to the given directory, eg. ["/", "/Users/", "/Users/oofuser/"]
    names = filter(None, os.path.abspath(directory).split(os.sep))
    if names:
        return [os.sep] + [os.sep + os.path.join(*names[:n]) + os.sep
                           for n in range(1,len(names)+1)]
    return [os.sep]

# FakeFileSelectorWidget is just a StringWidget, but it's a derived
# class so that so that the WriteModeWidget can find it.

class FakeFileSelectorWidget(parameterwidgets.StringWidget):
    pass

def _WFileNameParameter_makeWidget(self, scope=None, **kwargs):
    if (useFakeFileSelector=='always' or
        (useFakeFileSelector =='sometimes' and
         (guilogger.recording() or guilogger.replaying()))):
        return FakeFileSelectorWidget(self, scope=scope, name=self.name,
                                      **kwargs)
    else:
        return WriteFileSelectorWidget(self, scope=scope, name=self.name,
                                       **kwargs)

def _RFileNameParameter_makeWidget(self, scope=None, **kwargs):
    if (useFakeFileSelector=='always' or
        (useFakeFileSelector=='sometimes' 
         and (guilogger.recording() or guilogger.replaying()))):
        return FakeFileSelectorWidget(self, scope=scope, name=self.name,
                                      **kwargs)
    else:
        return ReadFileSelectorWidget(self, scope=scope, name=self.name,
                                      **kwargs)

filenameparam.WriteFileNameParameter.makeWidget = _WFileNameParameter_makeWidget
filenameparam.ReadFileNameParameter.makeWidget = _RFileNameParameter_makeWidget

########################

# The WriteModeWidget sets a WriteModeParameter to either 'w' or 'a'.
# It's not a simple EnumWidget because the choices it presents to the
# user depend on whether or not the file selected in the associated
# FileSelectorWidget exists already or not.

# TODO: If there are ever two WriteFileNameParameters and two
# WriteModeParameters in the same widget scope, both
# WriteModeParameters will probably refer to the same
# WriteFileNameParameter.  Some cleverer scheme will have to be used.

class WriteModeWidget(parameterwidgets.ParameterWidget):
    def __init__(self, param, scope=None, name=None, **kwargs):
        self.state = None
        self.widget = chooser.ChooserWidget([], self.chooserCB, name=name,
                                            **kwargs)
        parameterwidgets.ParameterWidget.__init__(self, self.widget.gtk,
                                                  scope=scope)
        if (useFakeFileSelector=='always' or
            (useFakeFileSelector=='sometimes' and
             (guilogger.recording() or guilogger.replaying()))):
            self.fileSelector = self.scope.findWidget(
                lambda x: (isinstance(x, FakeFileSelectorWidget)))
        else:
            self.fileSelector = self.scope.findWidget(
                lambda x: (isinstance(x, WriteFileSelectorWidget)))
        if self.fileSelector is None:
            raise ooferror.ErrPyProgrammingError("Can't find file selector")
        self.set_options()
        self.widgetChanged(True, True)
        self.sbcallback = switchboard.requestCallbackMain(self.fileSelector,
                                                          self.fileSelectorCB)
    
    def cleanUp(self):
        switchboard.removeCallback(self.sbcallback)
        parameterwidgets.ParameterWidget.cleanUp(self)

    def chooserCB(self, *args):
        self.set_options()
        self.widgetChanged(True, True)

    def fileSelectorCB(self, *args):
        self.set_options()

    def set_options(self):
        phile = self.fileSelector.get_value()
        if phile and os.path.exists(phile):
            if self.state != "overwrite":
                self.state = "overwrite"
                ## TODO: render "OVERWRITE" in bold
                self.widget.update(["OVERWRITE", "append"])
        else:
            if self.state != "write":
                self.state = "write"
                self.widget.update(["write", "append"])

    def get_value(self):
        widgetval = self.widget.get_value()
        if widgetval == "append":
            return 'a'
        return 'w'

def _writeModeParam_makeWidget(self, scope=None, **kwargs):
    return WriteModeWidget(self, scope=scope, name=self.name, **kwargs)

filenameparam.WriteModeParameter.makeWidget = _writeModeParam_makeWidget

# The OverwriteModeWidget is for files that can't be appended to.  The
# user has to agree to overwrite, or the widget declares itself to be
# in an invalid state, therefore disabling the associated dialog or
# page's OK button.

class OverwriteWidget(parameterwidgets.BooleanWidget):
    def __init__(self, param, scope=None, name=None, **kwargs):
        parameterwidgets.BooleanWidget.__init__(self, param, scope, name,
                                                **kwargs)
        self.fileSelector = self.scope.findWidget(
            lambda x: (isinstance(x, (WriteFileSelectorWidget,
                                      FakeFileSelectorWidget))))
        if self.fileSelector is None:
            raise ooferror.ErrPyProgrammingError("Can't find file selector")
        self.set_validity()
        self.sbcallback = switchboard.requestCallbackMain(self.fileSelector,
                                                          self.fileSelectorCB)
    def cleanUp(self):
        switchboard.removeCallback(self.sbcallback)
        parameterwidgets.ParameterWidget.cleanUp(self)
        
    def set_validity(self):
        phile = self.fileSelector.get_value()
        if phile and os.path.exists(phile) and not self.get_value():
            self.widgetChanged(False, interactive=False)
        else:
            self.widgetChanged(True, interactive=False)

    def buttonCB(self, button):
        parameterwidgets.BooleanWidget.buttonCB(self, button)
        self.set_validity()

    def fileSelectorCB(self, *args):
        self.set_validity()

def _overwriteParam_makeWidget(self, scope=None, **kwargs):
    return OverwriteWidget(self, scope=scope, name=self.name, **kwargs)

filenameparam.OverwriteParameter.makeWidget = _overwriteParam_makeWidget

############################

# Utilities that just get a file name or a file name and a mode.  If
# it's necessary to get a bunch of parameter values that include a
# FileNameParameter, use parameterwidgets.getParameters() instead.

def getFileAndMode(ident=None, title=""):
    fileparam = filenameparam.WriteFileNameParameter('filename', ident=ident)
    modeparam = filenameparam.WriteModeParameter('mode')
    if parameterwidgets.getParameters(fileparam, modeparam, title=title):
        return fileparam.value, modeparam.value.string()

def getFile(ident=None, title=""):
    fileparam = filenameparam.WriteFileNameParameter('filename', ident=ident)
    if parameterwidgets.getParameters(fileparam, title=title):
        return fileparam.value

