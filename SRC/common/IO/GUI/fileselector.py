# -*- python -*-
# $RCSfile: fileselector.py,v $
# $Revision: 1.46 $
# $Author: langer $
# $Date: 2010/12/13 21:52:10 $


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
import gtk
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

# Installing a search callback via gtk.TreeView.set_search_equal_func
# causes pygtk 2.6 to dump core the second time a FileSelectorWidget
# is used.  We only need to use set_search_equal_func because there's
# pango markup in the file list, so we just don't use markup if we're
# using version 2.6.  This hasn't been tested with 2.7.
version = gtk.pygtk_version
use_markup = version[0] > 2 or (version[0] == 2 and version[1] > 6)
#            ^^^^^^^^^^^^^^ <--- as if this code will still work with pygtk3


class FileSelectorWidget(parameterwidgets.ParameterWidget):
    
    # Base class for ReadFileSelectorWidget and WriteFileSelectorWidget.
    
    def __init__(self, param, scope=None, name=None, ident=None):

        debug.mainthreadTest()
        self.ident = ident or param.ident

        self.lastFile = {}      # last file selected in each directory
        self.fileNames = []     # files in the current directory
        self.dirHier = []       # directories in the current hierarchy
        self.dirHistory = ringbuffer.RingBuffer(50)

        parameterwidgets.ParameterWidget.__init__(self, gtk.Frame(), scope,
                                                  name, expandable=True)
        vbox = gtk.VBox()
        self.gtk.add(vbox)

        # Directory selector
        hbox = gtk.HBox()
        vbox.pack_start(hbox, expand=False, fill=False)
        hbox.pack_start(gtk.Label("Directory:"), expand=False, fill=False)
        self.dirWidget = chooser.ChooserComboWidget([],
                                                    callback=self.dirChangedCB, 
                                                    name="Directory")
        hbox.pack_start(self.dirWidget.gtk, expand=True, fill=True)

        # Directory selection buttons
        hbox = gtk.HBox(homogeneous=False)
        vbox.pack_start(hbox, expand=False, fill=False)

        self.backbutton = gtkutils.StockButton(gtk.STOCK_GO_BACK, "Back",
                                               align=0.0)
        gtklogger.setWidgetName(self.backbutton, "Back")
        gtklogger.connect(self.backbutton, 'clicked', self.backCB)
        hbox.pack_start(self.backbutton, expand=True, fill=True)

        self.addDirButtons(hbox)

        homebutton = gtkutils.StockButton(gtk.STOCK_HOME)
        gtklogger.setWidgetName(homebutton, "Home")
        gtklogger.connect(homebutton, 'clicked', self.homeCB)
        hbox.pack_start(homebutton, expand=False, fill=True)

        self.nextbutton = gtkutils.StockButton(gtk.STOCK_GO_FORWARD, "Next",
                                               reverse=True, align=1.0)
        gtklogger.setWidgetName(self.nextbutton, "Next")
        gtklogger.connect(self.nextbutton, 'clicked', self.nextCB)
        hbox.pack_start(self.nextbutton, expand=True, fill=True)

        # File list
        self.fileList = chooser.ScrolledChooserListWidget(
            name="FileList",
            callback=self.fileListCB, 
            dbcallback=self.fileListDoubleCB,
            markup=True)
        self.fileList.gtk.set_size_request(-1, 100)
        vbox.pack_start(self.fileList.gtk, expand=True, fill=True)
        # Set the comparison function used when typing in the file
        # list.  _filename_cmp matches the beginnings of file names,
        # ignoring the markup added to directories and escaped
        # characters.
        if use_markup:
            self.fileList.treeview.set_search_equal_func(_filename_cmp, None)

        align = gtk.Alignment(xalign=1.0)
        vbox.pack_start(align, expand=False, fill=False)
        hbox = gtk.HBox()
        align.add(hbox)
        hbox.pack_start(gtk.Label("show hidden files"), expand=False, fill=False)
        self.hiddenButton = gtk.CheckButton()
        hbox.pack_start(self.hiddenButton, expand=False, fill=False)
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

    def dirChangedCB(self, combobox): # directory widget callback
        directory = self.cwd()        # adds trailing slash if needed
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
        self.newdirbutton = gtkutils.StockButton(gtk.STOCK_DIRECTORY, "New")
        gtklogger.setWidgetName(self.newdirbutton, "NewDir")
        gtklogger.connect(self.newdirbutton, 'clicked', self.newdirCB)
        hbox.pack_start(self.newdirbutton, expand=False, fill=True)

    def addMoreWidgets(self, vbox): # Widgets below the file list.
        hbox = gtk.HBox()
        vbox.pack_start(hbox, expand=False, fill=False)
        label = gtk.Label('File:')
        hbox.pack_start(gtk.Label('File:'), expand=False, fill=False)
        self.fileEntry = gtk.Entry()
        gtklogger.setWidgetName(self.fileEntry, 'File')
        self.fileEntrySignal = gtklogger.connect(self.fileEntry, 'changed',
                                                 self.entryChangeCB)
        hbox.pack_start(self.fileEntry, expand=True, fill=True)

        # Add file-name completion in the fileEntry widget.  The
        # fileList already has file-name completion in it.
        self.completion = gtk.EntryCompletion()
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
    if use_markup:
        if filename and os.path.isdir(os.path.join(directory, filename)):
            return "<b>" + cgi.escape(filename) + "</b>"
        return cgi.escape(filename)
    return filename

def _filename_cmp(model, column, key, iter, data):
    # Comparisons made while searching in the file list use the raw
    # file name, in column 1 of the model, instead of the marked-up
    # file name in column 0. Only used if use_markup is True.
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

def _WFileNameParameter_makeWidget(self, scope=None):
    if (useFakeFileSelector=='always' or
        (useFakeFileSelector =='sometimes' and
         (guilogger.recording() or guilogger.replaying()))):
        return FakeFileSelectorWidget(self, scope=scope, name=self.name)
    else:
        return WriteFileSelectorWidget(self, scope=scope, name=self.name)

def _RFileNameParameter_makeWidget(self, scope=None):
    if (useFakeFileSelector=='always' or
        (useFakeFileSelector=='sometimes' 
         and (guilogger.recording() or guilogger.replaying()))):
        return FakeFileSelectorWidget(self, scope=scope, name=self.name)
    else:
        return ReadFileSelectorWidget(self, scope=scope, name=self.name)

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
    def __init__(self, param, scope=None, name=None):
        self.state = None
        self.widget = chooser.ChooserWidget([], self.chooserCB, name=name)
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

def _writeModeParam_makeWidget(self, scope=None):
    return WriteModeWidget(self, scope=scope, name=self.name)

filenameparam.WriteModeParameter.makeWidget = _writeModeParam_makeWidget

# The OverwriteModeWidget is for files that can't be appended to.  The
# user has to agree to overwrite, or the widget declares itself to be
# in an invalid state, therefore disabling the associated dialog or
# page's OK button.

class OverwriteWidget(parameterwidgets.BooleanWidget):
    def __init__(self, param, scope=None, name=None):
        parameterwidgets.BooleanWidget.__init__(self, param, scope, name)
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

def _overwriteParam_makeWidget(self, scope=None):
    return OverwriteWidget(self, scope=scope, name=self.name)

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

###########################################################
###############  OLD STUFF  ###############################
###########################################################

## TODO: Get rid of code below here after new widgets are created for
## loading 3D image slices.

# The _selectors dictionary keeps track of file selectors to be
# reused.  They are reused so that they preserve their state (current
# directory, etc).  The dictionary is a WeakValueDictionary because
# the selectors can be destroyed by the window manager, and we don't
# have any control over that.

_selectors = weakref.WeakValueDictionary()


_modes = {'w':gtk.FILE_CHOOSER_ACTION_SAVE,
         'r':gtk.FILE_CHOOSER_ACTION_OPEN}

class FileSelector(widgetscope.WidgetScope):
    OK = 1
    CANCEL = 2
    def __init__(self, mode, title=None, filename=None, params=None,
                 pattern=False):
        debug.mainthreadTest()
        widgetscope.WidgetScope.__init__(self, None)
        self.dialog = gtklogger.Dialog()
        self.set_title(title)
        gtklogger.newTopLevelWidget(self.dialog, self.dialog.get_title())
        self.filechooser = gtk.FileChooserWidget(action=_modes[mode])
        self.dialog.set_default_size(500, 300)
        self.filechooser.show()
        self.dialog.vbox.pack_start(self.filechooser, expand=1, fill=1)
        gtklogger.setWidgetName(self.filechooser, "FileChooser")
        gtklogger.connect(self.filechooser, 'selection-changed',
                          self.selectionchangedCB)
        self.dialog.add_button(gtk.STOCK_OK, self.OK)
        self.dialog.add_button(gtk.STOCK_CANCEL, self.CANCEL)
        self.dialog.set_default_response(self.OK)

        self.pattern = (pattern and (mode=='r'))
        if self.pattern:
            # TODO: Fix aesthetics of the widgets.
            self.filechooser.set_select_multiple(True)
            self.patternrow = gtk.HBox()
            self.patternrow.pack_start(gtk.Label("Pattern: "), expand=0, fill=0, padding=5)
            self.pattern_entry = gtk.Entry()
            self.pattern_entry.set_editable(1)
            self.pattern_entry.set_text("*")
            gtklogger.connect(self.pattern_entry, 'changed', self.patternchangedCB)
            self.patternrow.pack_start(self.pattern_entry, expand=1, fill=1, padding=5)
            self.patternrow.show_all()

        if params is None:
            self.table = None
            if self.pattern:
                self.filechooser.set_extra_widget(self.patternrow)
        else:
            self.table = parameterwidgets.ParameterTable(params, scope=self,
                                                         name="Parameters")
            self.sbcallback = switchboard.requestCallbackMain(
                ('validity', self.table), self.validityCB)
            if not self.pattern:
                self.filechooser.set_extra_widget(self.table.gtk)
            else:
                vbox = gtk.VBox()
                vbox.pack_start(self.patternrow)
                vbox.pack_start(self.table.gtk)
                vbox.show()
                self.filechooser.set_extra_widget(vbox)

        if filename is not None:
            self.filechooser.set_current_name(filename)

    def set_mode(self, mode):
        debug.mainthreadTest()
        self.filechooser.set_action(_modes[mode])
        # Calling sensitize() here wouldn't be required if we could
        # catch keystrokes in the Entry. See comment in sensitize(),
        # below.
        self.sensitize()
    def set_title(self, title):
        debug.mainthreadTest()
        self.dialog.set_title(title or "OOF2 File Selector")
    def sensitize(self):
        debug.mainthreadTest()
        valid = self.table is None or self.table.isValid()
        # If we're opening an existing file, check to see if it's
        # really there.  If we're opening a new file, it would be nice
        # to check to see if the file entry widget has text in it, but
        # there seems to be no way to do that.  There's no way to call
        # this function after every keystroke, since the Entry widget
        # inside the FileChooserWidget isn't accessible and we can't
        # connect to it.
        if valid and \
               self.filechooser.get_action() == gtk.FILE_CHOOSER_ACTION_OPEN:
            if not self.pattern:
                filename = self.filechooser.get_filename()
                valid = filename is not None and os.path.isfile(filename)
            # check that there are files that fit the pattern
            else:                
                matchcount = utils.countmatches(self.pattern_entry.get_text(), self.filechooser.get_current_folder(), utils.matchvtkpattern)
                valid = valid and self.pattern_entry.get_text() != "*" and matchcount

        self.dialog.set_response_sensitive(self.OK, valid)

    def patternchangedCB(self, *args):
        # select the files that match
        self.filechooser.unselect_all()
        items = os.listdir(self.filechooser.get_current_folder())
        for item in items:
            if utils.matchvtkpattern(self.pattern_entry.get_text(), item):
                self.filechooser.select_filename(os.path.join(self.filechooser.get_current_folder(),item))
        
        self.sensitize()
        
    def validityCB(self, validity):
        self.sensitize()
    def selectionchangedCB(self, *args):
        self.sensitize()
    def get_values(self):
        if self.table:
            return self.table.get_values()
    def getFileName(self):
        if self.table:
            self.table.get_values()
        return self.filechooser.get_filename()
    def getFilePattern(self):
        if self.table:
            self.table.get_values()
        return os.path.join(self.filechooser.get_current_folder(), self.pattern_entry.get_text())
    def run(self):
        debug.mainthreadTest()
        return self.dialog.run()
    def close(self):
        debug.mainthreadTest()
        if self.table:
            switchboard.removeCallback(self.sbcallback)
        self.dialog.destroy()
        self.destroyScope()
    def hide(self):
        debug.mainthreadTest()
        self.dialog.hide()
        

        
# Always check the return value of fileSelector()!  fileSelector
# returns None if the user cancels the operation or doesn't type in a
# name in 'w' mode.

# mode should be 'r' or 'w'.

from ooflib.common.IO.GUI import guilogger

def fileSelector(mode, ident=None, title=None, filename=None, params=None,
                 pattern=False):
    # GUI logging doesn't work for the file selector, so we use a
    # simple StringParameter and ParameterDialog when either logging
    # or replaying.  This is a hack. TODO EVENTUALLY: fix this.
    # TODO: will need to fix logging for pattern?

    if (useFakeFileSelector=='always' or 
        (useFakeFileSelector=='sometimes' and 
         (guilogger.recording() or guilogger.replaying()))):
        return fakeFileSelector(mode, ident, title, filename, params)

    try:
        selector = _selectors[ident]
    except KeyError:
        # Make new selector
        selector = FileSelector(mode=mode, title=title, filename=filename,
                                params=params, pattern=pattern)
        if ident is not None:
            _selectors[ident] = selector
    else:
        # Reuse old selector
        selector.set_mode(mode)
        selector.set_title(title)

    result = selector.run()
    selector.hide()

    if result in (FileSelector.CANCEL,
                  gtk.RESPONSE_DELETE_EVENT,
                  gtk.RESPONSE_NONE):
        return None

    if not pattern:
        return selector.getFileName()
    else:
        return selector.getFilePattern()
        

def fakeFileSelector(mode, ident=None, title=None, filename=None, params=None):
    nameparam = parameter.StringParameter('filename')
    parameters = [nameparam]
    if params:
        parameters.extend(params)
    if parameterwidgets.getParameters(title='Fake FileSelector', *parameters):
        return nameparam.value
    
#########################

# # This function should be called before you write to a file.
# # If the file exists, it will prompt the user, asking whether to
# # over-write or append.  It will return either 'w' for writing,
# # 'a' for appending, or None, in which case the caller should not
# # write to the file at all.
# def get_file_mode(filename, no_append=0):
#     mode = None
#     try:
#         os.stat(filename)               # does file exist?
#     except OSError:                     # file not found
#         mode = 'w'
#     else:
#         if no_append:
#             ans = reporter.query("Overwrite file\n%s?" % filename,
#                                  "OK", "Cancel", default="OK")
#             if ans == "OK":
#                 mode = 'w'
#         else:
#             ans = reporter.query("Overwrite file\n%s?" % filename,
#                                  "OK", "Append", "Cancel", default="OK")
#             if ans == 'OK':
#                 mode = 'w'
#             elif ans == 'Append':
#                 mode = 'a'
#     return mode
    
