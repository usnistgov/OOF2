# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.image import oofimage
from ooflib.common import debug
from ooflib.common import labeltree
from ooflib.common import mainthread
from ooflib.common import microstructure
from ooflib.common import ringbuffer
from ooflib.common import subthread
from ooflib.common import utils
from ooflib.common.IO import mainmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import reporter
from ooflib.common.IO import whoville
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import historian
from ooflib.common.IO.GUI import oofGUI
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import regclassfactory
from ooflib.common.IO.GUI import whowidget
from ooflib.image import imagecontext
from ooflib.image import imagemodifier
from gi.repository import Gtk

class ImagePage(oofGUI.MainPage):
    def __init__(self):
        oofGUI.MainPage.__init__(self, name="Image", ordering=50,
                                 tip='Manipulate Images')

        mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.gtk.add(mainbox)

        centerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                            spacing=3, margin=2, halign=Gtk.Align.CENTER)
        mainbox.pack_start(centerbox, expand=False, fill=False, padding=0)
        label = Gtk.Label('Microstructure=', halign=Gtk.Align.END)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        self.imagewidget = whowidget.WhoWidget(imagecontext.imageContexts)
        centerbox.pack_start(self.imagewidget.gtk[0],
                             expand=False, fill=False, padding=0)
        label = Gtk.Label('Image=', halign=Gtk.Align.END)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        centerbox.pack_start(self.imagewidget.gtk[1],
                             expand=False, fill=False, padding=0)

        centerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                            homogeneous=True,
                            spacing=3, margin=2, halign=Gtk.Align.CENTER)
        mainbox.pack_start(centerbox, expand=False, fill=False, padding=0)

        self.loadbutton = Gtk.Button('Load...')
        gtklogger.setWidgetName(self.loadbutton, 'Load')
        centerbox.pack_start(self.loadbutton, expand=True, fill=True, padding=0)
        gtklogger.connect(self.loadbutton, 'clicked', self.loadCB)
        self.loadbutton.set_tooltip_text(
            'Load a new image into an existing Microstructure')
        
        self.copybutton = gtkutils.StockButton("edit-copy-symbolic", 'Copy...')
        gtklogger.setWidgetName(self.copybutton, 'Copy')
        gtklogger.connect(self.copybutton, 'clicked', self.copyCB)
        centerbox.pack_start(self.copybutton, expand=True, fill=True, padding=0)
        self.copybutton.set_tooltip_text(
            "Copy the current image.  The copy can be in the same"
            " or a different Microstructure.")

        self.renamebutton = gtkutils.StockButton("document-edit-symbolic",
                                                 'Rename...')
        gtklogger.setWidgetName(self.renamebutton, 'Rename')
        gtklogger.connect(self.renamebutton, 'clicked', self.renameCB)
        self.renamebutton.set_tooltip_text('Rename the current image.')
        centerbox.pack_start(self.renamebutton,
                             expand=True, fill=True, padding=0)

        self.deletebutton = gtkutils.StockButton("edit-delete-symbolic",
                                                 'Delete')
        gtklogger.setWidgetName(self.deletebutton, 'Delete')
        gtklogger.connect(self.deletebutton, 'clicked', self.deleteCB)
        self.deletebutton.set_tooltip_text('Delete the current image.')
        centerbox.pack_start(self.deletebutton,
                             expand=True, fill=True, padding=0)

        self.savebutton = gtkutils.StockButton('document-save-symbolic',
                                               'Save...')
        gtklogger.setWidgetName(self.savebutton, 'Save')
        gtklogger.connect(self.savebutton, 'clicked', self.saveCB)
        self.savebutton.set_tooltip_text('Save the current image to a file.')
        centerbox.pack_start(self.savebutton, expand=True, fill=True, padding=0)

        self.autogroupbutton = Gtk.Button('Group...')
        gtklogger.setWidgetName(self.autogroupbutton, 'Group')
        gtklogger.connect(self.autogroupbutton, 'clicked', self.autogroupCB)
        centerbox.pack_start(self.autogroupbutton,
                             expand=True, fill=True, padding=0)
        self.autogroupbutton.set_tooltip_text(
            "Create a pixel group in the current image's microstructure"
            " for each color pixel in the image.  The 'Auto' button on the"
            " Microstructure page is more powerful version of this.")

        mainpane = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL,
                             wide_handle=True)
        gtklogger.setWidgetName(mainpane, 'Pane')
        mainbox.pack_start(mainpane, expand=True, fill=True, padding=0)
        gtklogger.connect_passive(mainpane, 'notify::position')

        frame = Gtk.Frame(label='Image Information', margin=2)
        frame.set_shadow_type(Gtk.ShadowType.IN)
        mainpane.pack1(frame, resize=True, shrink=False)
        scroll = Gtk.ScrolledWindow(shadow_type=Gtk.ShadowType.IN, margin=2)
        gtklogger.logScrollBars(scroll, "StatusScroll")
        scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        frame.add(scroll)

        self.infoarea = Gtk.TextView(name="fixedfont")
        self.infoarea.set_wrap_mode(Gtk.WrapMode.WORD)
        self.infoarea.set_editable(False)
        self.infoarea.set_cursor_visible(False)
        scroll.add(self.infoarea)

        frame = Gtk.Frame(label='Image Modification', margin=2)
        frame.set_shadow_type(Gtk.ShadowType.IN)
        mainpane.pack2(frame, resize=False, shrink=False)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                       spacing=2, margin=2)
        frame.add(vbox)
        self.imageModFactory = regclassfactory.RegisteredClassFactory(
            imagemodifier.ImageModifier.registry,
            title="Method:", name="Method")
        vbox.pack_start(self.imageModFactory.gtk,
                        expand=True, fill=True, padding=0)
        self.historian = historian.Historian(self.imageModFactory.set,
                                             self.sensitizeHistory,
                                             setCBkwargs={'interactive':1})
        self.imageModFactory.set_callback(self.historian.stateChangeCB)

        # Prev, OK, and Next buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                       spacing=2, margin=2)
        vbox.pack_start(hbox, expand=False, fill=False, padding=2)
        self.prevmethodbutton = gtkutils.prevButton()
        gtklogger.connect(self.prevmethodbutton, 'clicked',
                          self.historian.prevCB)
        hbox.pack_start(self.prevmethodbutton,
                        expand=False, fill=False, padding=0)
        self.prevmethodbutton.set_tooltip_text(
            'Recall the previous image modification operation.')
        self.okbutton = gtkutils.StockButton("gtk-ok", "OK")
        gtklogger.setWidgetName(self.okbutton, 'OK')
        hbox.pack_start(self.okbutton, expand=True, fill=True, padding=5)
        gtklogger.connect(self.okbutton, 'clicked', self.okbuttonCB)
        self.okbutton.set_tooltip_text(
            'Perform the image modification operation defined above.')
        self.nextmethodbutton = gtkutils.nextButton()
        gtklogger.connect(self.nextmethodbutton, 'clicked',
                          self.historian.nextCB)
        hbox.pack_start(self.nextmethodbutton,
                        expand=False, fill=False, padding=0)
        self.nextmethodbutton.set_tooltip_text(
            "Recall the next image modification operation.")

        # Undo and Redo buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                       spacing=2, margin=2)
        vbox.pack_start(hbox, expand=False, fill=False, padding=0)
        self.undobutton = gtkutils.StockButton('edit-undo-symbolic', 'Undo')
        gtklogger.setWidgetName(self.undobutton, 'Undo')
        gtklogger.connect(self.undobutton, 'clicked', self.undoCB)
        self.undobutton.set_tooltip_text('Undo the latest image modification.')
        hbox.pack_start(self.undobutton, expand=True, fill=False, padding=0)
        self.redobutton = gtkutils.StockButton('edit-redo-symbolic', 'Redo')
        gtklogger.setWidgetName(self.redobutton, 'Redo')
        gtklogger.connect(self.redobutton, 'clicked', self.redoCB)
        self.redobutton.set_tooltip_text(
            'Redo the latest undone image modification.')
        hbox.pack_start(self.redobutton, expand=True, fill=False, padding=0)

        self.sbcallbacks = [
            switchboard.requestCallbackMain(('new who', 'Microstructure'),
                                            self.newMicrostructureCB),
            switchboard.requestCallbackMain(('new who', 'Image'),
                                            self.newImageCB),
            switchboard.requestCallbackMain(('remove who', 'Image'),
                                            self.rmWhoCB),
            switchboard.requestCallbackMain('modified image',
                                            self.modifiedImageCB),
            switchboard.requestCallbackMain(imagemodifier.ImageModifier,
                                            self.updateImageModifiers),
            switchboard.requestCallbackMain(self.imagewidget,
                                            self.iWidgetChanged),
            switchboard.requestCallbackMain(('validity',
                                             self.imageModFactory),
                                            self.validityChangeCB),
            switchboard.requestCallbackMain(('WhoDoUndo buffer change',
                                             'Image'),
                                            self.whoBufChangeCB)
            ]

    def installed(self):
        self.sensitize()
        self.sensitizeHistory()
        subthread.execute(self.displayImageInfo)
        
    def sensitize(self):
        debug.mainthreadTest()
        image = self.getCurrentImage()
        selected = image is not None
        self.copybutton.set_sensitive(selected)
        self.renamebutton.set_sensitive(selected)
        self.deletebutton.set_sensitive(selected)
        self.savebutton.set_sensitive(selected)
        self.okbutton.set_sensitive(selected and self.imageModFactory.isValid())
        self.autogroupbutton.set_sensitive(selected)
        self.loadbutton.set_sensitive(self.getCurrentMS() is not None)
        if selected:
            self.undobutton.set_sensitive(image.undoable())
            self.redobutton.set_sensitive(image.redoable())
        else:
            self.undobutton.set_sensitive(0)
            self.redobutton.set_sensitive(0)

    def sensitizeHistory(self):
        debug.mainthreadTest()
        self.nextmethodbutton.set_sensitive(self.historian.nextSensitive())
        self.prevmethodbutton.set_sensitive(self.historian.prevSensitive())

    def validityChangeCB(self, validity):
        self.sensitize()

    def whoBufChangeCB(self):
        self.sensitize()

    def iWidgetChanged(self, interactive):
        self.sensitize()
        subthread.execute(self.displayImageInfo)
        
    def displayImageInfo(self):
        debug.subthreadTest()
        imagecontext = self.getCurrentImage()
        text = ""
        if imagecontext:
            imagecontext.begin_reading()
            try:
                if config.dimension() == 2:
                    image = imagecontext.getObject()
                    size = image.sizeInPixels()
                    text += 'Pixel size: %dx%d\n' % (size.x, size.y)
                    size = image.size()
                    text += 'Physical size: %sx%s\n' % (size.x, size.y)
                    if image.comment():
                        text += '\nComments:\n%s\n' % image.comment()
                elif config.dimension() == 3:
                    image = imagecontext.getObject()
                    size = image.sizeInPixels()
                    text += 'Voxel size: %dx%dx%d\n' % (size.x, size.y, size.z)
                    size = image.size()
                    text += 'Physical size: %sx%sx%s\n' % (size.x, size.y, size.z)                    
            finally:
                imagecontext.end_reading()
        mainthread.runBlock(self.displayImageInfo_thread, (text,))

    def displayImageInfo_thread(self, text):
        debug.mainthreadTest()
        self.infoarea.get_buffer().set_text(text)

    def getCurrentImageName(self):
        path = labeltree.makePath(self.imagewidget.get_value())
        if path:
            return path[-1]

    def getCurrentMSName(self):
        return self.imagewidget.get_value(depth=1)

    def getCurrentMS(self):
        try:
            return microstructure.microStructures[self.getCurrentMSName()]
        except KeyError:
            pass
        
    def getCurrentImage(self):
        try:
            return imagecontext.imageContexts[self.imagewidget.get_value()]
        except KeyError:
            pass

    def updateImageModifiers(self):
        self.imageModFactory.update(imagemodifier.ImageModifier.registry)

    def newImageCB(self, whoname):        # switchboard 'new who', 'Image'
        self.imagewidget.set_value(whoname)
        self.sensitize()

    def rmWhoCB(self, whoname):         # switchboard 'remove who'
        self.sensitize()

    def newMicrostructureCB(self, msname):
        if not self.getCurrentImage():
            self.imagewidget.set_value(msname)

    ############### GUI callbacks ################

    def loadCB(self, button):
        menuitem = mainmenu.OOF.File.Load.Image
        if parameterwidgets.getParameters(title='Load Image',
                                          *menuitem.params):
            menuitem.callWithDefaults()

    def copyCB(self, button):
        menuitem = mainmenu.OOF.Image.Copy
        nameparam = menuitem.get_arg('name')
        msparam = menuitem.get_arg('microstructure')
        if parameterwidgets.getParameters(msparam, nameparam,
                                          title="Copy Image"):
            menuitem.callWithDefaults(image=self.imagewidget.get_value())

    def renameCB(self, button):
        menuitem = mainmenu.OOF.Image.Rename
        namearg = menuitem.get_arg('name')
        namearg.value = labeltree.makePath(self.imagewidget.get_value())[-1]
        if parameterwidgets.getParameters(namearg, title='Rename Image'):
            menuitem.callWithDefaults(image=self.imagewidget.get_value())

    def deleteCB(self, button):
        if reporter.query("Really delete %s?"
                          % self.getCurrentImageName(),
                          "No", default="Yes") == "Yes":
            mainmenu.OOF.Image.Delete(image=self.imagewidget.get_value())
            
    def saveCB(self,button):
        menuitem = mainmenu.OOF.File.Save.Image
        params = filter(lambda x: x.name!="image", menuitem.params)
        if parameterwidgets.getParameters(title='Save Image', *params):
            menuitem.callWithDefaults(image=self.imagewidget.get_value())
                                          
    def okbuttonCB(self, button):
        modmeth = self.imageModFactory.getRegistration()
        if modmeth is not None:
            # buildImageModMenu() in imagemenu.py builds the
            # Image.Modify menu items from the members of the
            # ImageModifier RegisteredClass.  The Parameters in the
            # menu items are identically the Parameters in the
            # Registrations.  So copying new values out of the Factory
            # into the Registrations, and invoking the menu item with
            # callWithDefaults() executes the command with the current
            # arguments.
            self.imageModFactory.set_defaults() # copy from gui to Registration
            menuitem = getattr(mainmenu.OOF.Image.Modify, modmeth.name())
            menuitem.callWithDefaults(image=self.imagewidget.get_value())

    def modifiedImageCB(self, imageModifier, imagename): # sb 'modified image'
        # Called whenever the image is changed, either by applying an
        # ImageModifier or the Undo and Redo buttons, in which case
        # the imageModifier arg is None.
        if imageModifier is not None:
            self.historian.record(imageModifier)
        self.sensitize()
        
    def undoCB(self, button):
        mainmenu.OOF.Image.Undo(image=self.imagewidget.get_value())

    def redoCB(self, button):
        mainmenu.OOF.Image.Redo(image=self.imagewidget.get_value())

    def autogroupCB(self, button):
        menuitem = mainmenu.OOF.Image.AutoGroup
        params = [p for p in menuitem.params if p.name != 'image']
        if parameterwidgets.getParameters(title='AutoGroup', *params):
            menuitem.callWithDefaults(image=self.imagewidget.get_value())

        
ImagePage()

