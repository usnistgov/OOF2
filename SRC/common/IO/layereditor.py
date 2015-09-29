# -*- python -*-
# $RCSfile: layereditor.py,v $
# $Revision: 1.52 $
# $Author: langer $
# $Date: 2014/09/27 21:40:31 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import lock
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common import quit
from ooflib.common.IO import display
from ooflib.common.IO import gfxmanager
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import whoville
from ooflib.common.IO import xmlmenudump

# LayerEditor menu items are defined *outside* the LayerEditor class,
# because some of the items (eg, New, Edit) need to exist even if
# there is no LayerEditor.

OOFMenuItem = oofmenu.OOFMenuItem

menu = mainmenu.OOF.addItem(OOFMenuItem(
    'LayerEditor', secret=1,
    help='Construct and modify graphics layers.',
    discussion="""<para>
    Menu commands for creating and modifying graphics layers.  These
    commands are used by the <link
    linkend='Section-Graphics-LayerEditor'>Layer Editor</link> window.
    </para>"""
    ))
layermenu = menu.addItem(OOFMenuItem(
    'LayerSet', cli_only=1,
    help='Construct and modify sets of graphics layers.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/layerset.xml')
    ))

filemenu = menu.addItem(OOFMenuItem('File',
                                    help="File menu for the layer editor."))

def closeLayerEditor(menuitem):
    layerEditor.close()
    
filemenu.addItem(oofmenu.OOFMenuItem(
    'Close',
    callback=closeLayerEditor,
    help="Close the Layer Editor window.",
    no_log=1,
    accel='w',
    threadable=oofmenu.UNTHREADABLE,
    discussion="""<para>
    Closing the &layereditor; window doesn't actually close the Layer
    Editor itself.  The Layer Editor is immortal (for the duration of
    an &oof2; session, at least).  
    </para>"""))

filemenu.addItem(oofmenu.OOFMenuItem(
    'Quit',
    help='Quit the OOF application.',
    callback=quit.quit,
    no_log=1,
    gui_only=1,
    accel='q',
    threadable=oofmenu.UNTHREADABLE,
    discussion="<para>Quit &oof2;, &layereditor; and all.</para>"))


settingsmenu = menu.addItem(OOFMenuItem('Settings'))

# In these menu items, "window" is a string with the name
# of the window in it -- this name is exposed in the UI.
def newLayerSetCB(menuitem, window):
    openLayerEditor()
    layerEditor.newLayerSetCB(window)

layermenu.addItem(OOFMenuItem(
    'New',
    callback=newLayerSetCB,
    params=[parameter.StringParameter('window', tip="Which window.")],
    help="Create a new layer set.",
    discussion=xmlmenudump.loadFile(
    'DISCUSSIONS/common/menu/newlayerset.xml')
    ))

def loadLayerCB(menuitem, window, layer_number):
    openLayerEditor()
    layerEditor.loadLayerCB(window, layer_number)

layermenu.addItem(OOFMenuItem(
    'Edit',
    callback=loadLayerCB,
    params=[parameter.StringParameter('window', tip="Which window."),
            parameter.IntParameter('layer_number', tip="Layer number.")],
    help="Edit the layer.",
    discussion=xmlmenudump.loadFile(
    'DISCUSSIONS/common/menu/editlayerset.xml')
    ))


def displayedObjectCB(menuitem, category, object):
    openLayerEditor()
    layerEditor.displayedObjectCB(category, object)

layermenu.addItem(OOFMenuItem(
    'DisplayedObject',
    callback=displayedObjectCB,
    params=[
    whoville.WhoClassParameter('category', condition=whoville.noSecretClasses,
                               tip='What type of object is being displayed.'),
    whoville.AnyWhoParameter('object',
                             tip='The name of the object being displayed.')],
    help="Change what's being displayed by a LayerSet.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/displayedobject.xml')
    ))

def addMethodCB(menuitem, method):
    openLayerEditor()
    layerEditor.addMethodCB(method)

layermenu.addItem(OOFMenuItem(
    'Add_Method',
    callback=addMethodCB,
    params=[display.DisplayMethodParameter('method',
                                           tip="Display method to add.")],
    help="Add a graphics layer to the layer set.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/addmethod.xml')
    ))


def copyMethodCB(menuitem, layer_number):
    openLayerEditor()
    layerEditor.copyMethodCB(layer_number)

layermenu.addItem(OOFMenuItem(
    'Copy_Method',
    callback=copyMethodCB,
    params=[parameter.IntParameter('layer_number',
                                   tip="Number of the layer to copy.")],
    help="Copy an existing display method.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/copymethod.xml')
    ))


def replaceMethodCB(menuitem, layer_number, method):
    openLayerEditor()
    layerEditor.replaceMethodCB(layer_number, method)

layermenu.addItem(OOFMenuItem(
    'Replace_Method',
    callback=replaceMethodCB,
    params=[parameter.IntParameter('layer_number',
                                   tip="Number of the layer to replace."),
    display.DisplayMethodParameter('method', tip="Display method to use.")],
    help="Replace an existing display method.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/replacemethod.xml')
    ))


def deleteMethodCB(menuitem, layer_number):
    openLayerEditor()
    layerEditor.deleteMethodCB(layer_number)

layermenu.addItem(OOFMenuItem(
    'Delete_Method',
    callback=deleteMethodCB,
    params=[parameter.IntParameter('layer_number',
                                   tip="Number of the layer to delete.")],
    help="Remove a display method.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/deletemethod.xml')
    ))


def sendLayerCB(menuitem, window):
    openLayerEditor()
    layerEditor.sendLayerCB(window)

layermenu.addItem(OOFMenuItem(
    'Send',
    callback=sendLayerCB,
    params=[parameter.StringParameter('window',
                                      tip="Window to which the layer will be sent.")],
    help="Send the LayerSet to a graphics window.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/sendlayer.xml')
    ))

autoSendFlag = True
def setAutoSendCB(menuitem, value):
    global autoSendFlag
    autoSendFlag = value

settingsmenu.addItem(oofmenu.CheckOOFMenuItem(
    'AutoSend',
    value=autoSendFlag,
    callback=setAutoSendCB,
    help="Send layers to the graphics window as soon as they're edited.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/autosend.xml')
    ))



class LayerEditor:
    def __init__(self):
        global menu
        self.menu = menu

        # The state of the editor is kept in a LayerSet, which is the
        # layer currently being edited.  Because it's possible to set
        # the WhoClass in the editor without specifying a Who, and
        # because a LayerSet only contains a Who, it's necessary to
        # keep a separate currentWhoClass variable.
        self.currentLayerSet = display.LayerSet(whoville.nobody)
        self.currentWhoClass = whoville.noclass
        self.lock = lock.Lock()

    def show(self): pass                # redefined in GUI mode
    def close(self): pass               # redefined in GUI mode

    def destroy(self):
        global layerEditor
        layerEditor = None

    def newLayerSetCB(self, window):
        switchboard.notify("deselect all gfxlayers")
        if window is not None:
            gfxwindow = gfxmanager.gfxManager.getWindow(window)
        else:
            gfxwindow = None
        self.initialize(gfxwindow)
        self.updateEditee()
        self.show()

    def loadLayerCB(self, window, layerNumber):
        gfxwindow = gfxmanager.gfxManager.getWindow(window)
        self.initialize(gfxwindow, layerNumber)

    def initialize(self, gfxwindow, layerNumber=None):
        self.lock.acquire()
        try:
            self.currentLayerSet.destroy()
            # If no layer number is explicitly specified, use the selected
            # layer in the given graphics window, if any.
            if gfxwindow is None:
                selectedLayer = None
            else:
                if layerNumber is None:
                    layerNumber = gfxwindow.selectedLayerNumber()
                    if layerNumber is None:
                        selectedLayer = None
                    else:
                        selectedLayer = gfxwindow.getLayer(layerNumber)
                else:
                    selectedLayer = gfxwindow.getLayer(layerNumber)
            if selectedLayer:
                self.currentLayerSet = selectedLayer.layerset.clone()
            else:
                self.currentLayerSet = display.LayerSet() # new empty layer set
            self.currentWhoClass = self.currentLayerSet.who.getClass()
            self.updateEditee(selectedLayer)
        finally:
            self.lock.release()
        
    def addMethodCB(self, method):
        self.lock.acquire()
        try:
            self.currentLayerSet.addMethod(method)
            self.updateMethodList(selected=method)
        finally:
            self.lock.release()
        self.autoSend()
        
    def copyMethodCB(self, layernumber):
        self.lock.acquire()
        try:
            self.currentLayerSet.copyMethod(layernumber)
            self.updateMethodList()
        finally:
            self.lock.release()
        
    def replaceMethodCB(self, layernumber, method):
        self.lock.acquire()
        try:
            self.currentLayerSet.replaceMethod(layernumber, method)
            self.updateMethodList(selected=method)
        finally:
            self.lock.release()
        self.autoSend()
        
    def deleteMethodCB(self, layernumber):
        self.lock.acquire()
        try:
            self.currentLayerSet.doomMethod(layernumber)
            self.updateMethodList()
        finally:
            self.lock.release()
        
    def sendLayerCB(self, window):
        self.lock.acquire()
        try:
            if self.ready():
                gfxwindow = gfxmanager.gfxManager.getWindow(window)
                gfxwindow.incorporateLayerSet(self.currentLayerSet)
                gfxwindow.draw()
        finally:
            self.lock.release()

    def displayedObjectCB(self, category, object):
        self.lock.acquire()
        try:
            self.changeDisplayedObject(category, object)
        finally:
            self.lock.release()

    def autoSend(self):                 # redefined in derived class
        pass

    # When called from a script in gui mode, this function changes the
    # state of the widget, which calls the script...  The widget's
    # callback is recursion proof, but this function would be called
    # twice without its own recursion suppression.
    recursionInhibitor = 0
    def changeDisplayedObject(self, category, object):
        if not LayerEditor.recursionInhibitor:
            LayerEditor.recursionInhibitor = 1
            self.currentWhoClass = whoville.getClass(category)
            if self.currentWhoClass is not None:
                try:
                    who = self.currentWhoClass[object]
                except KeyError:
                    who = None
            else:
                who = None
            self.currentLayerSet.changeWho(who)
            self.updateEditee()
            LayerEditor.recursionInhibitor = 0
            
    def updateEditee(self, selectedlayer=None):
        self.updateWho()
        self.updateMethodList(selected=selectedlayer)

    def updateWho(self): pass           # redefined in LayerEditorGUI
    def updateMethodList(self, *args, **kwargs): pass # ditto

    def ready(self):
        return len(self.currentLayerSet) > 0


##########################

layerEditor = None                      # the one and only layer editor

def openLayerEditor(*args):
    global layerEditor
    if not layerEditor:
        layerEditor = mainthread.runBlock(newLayerEditor)
    layerEditor.show()

def newLayerEditor():
    # This function is redefined when layereditorGUI.py is loaded.
    debug.fmsg("Creating non-GUI layer editor")
    return LayerEditor()

mainmenu.OOF.Windows.addItem(oofmenu.OOFMenuItem(
    'Layer_Editor',
    help="Open or raise the Layer Editor window.",
    callback=openLayerEditor,
    threadable=oofmenu.UNTHREADABLE,
    discussion="""<para>
    Open a new <link linkend='Section-Graphics-LayerEditor'>Layer
    Editor</link>, if none has been opened. Otherwise, raise the Layer
    Editor window.  There can never be more than one Layer Editor.
    </para>"""
    ))

