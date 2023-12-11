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
from ooflib.common import mainthread
from ooflib.common.IO import filenameparam
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO.GUI import fileselector
from ooflib.common.IO.GUI import fontselector
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import subWindow
from ooflib.tutorials import tutorial

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import textwrap

## TODO: Add a table of contents.

tutorialInProgress = None

def start_class(tutor, progress=0):
    debug.mainthreadTest()
    global tutorialInProgress
    if not tutorialInProgress:
        tutorialInProgress = TutorialClassGUI(tutor)
    tutorialInProgress.raise_window()
    mainmenu.OOF.Windows.Tutorial.enable()
    if progress != 0:
        tutorialInProgress.resume(progress)

tutorial.start_tutorial = start_class

# Resume a tutorial from a saved script.
def resume_tutorial(menuitem, subject, progress):
    tutor = tutorial.allTutorials[subject]
    mainthread.runBlock(start_class, (tutor, progress))
    
mainmenu.OOF.Help.Tutorials.addItem(
    oofmenu.OOFMenuItem(
        'Resume',
        callback=resume_tutorial,
        secret=1,
        ordering=10000,
        params=[
            parameter.StringParameter('subject',
                                      tip="The name of the tutorial."),
            parameter.IntParameter('progress',
                                   tip="The current page number.")],
        help="Resume a tutorial.",
        discussion="""<para>
        This command is used when a tutorial session is saved in a
        script.  It's not available to the user directly.
        </para>"""
                        )
    )

def raise_tutorial(menuitem):
    debug.mainthreadTest()
    tutorialInProgress.raise_window()

mainmenu.OOF.Windows.addItem(oofmenu.OOFMenuItem(
    'Tutorial',
    help="Raise the tutorial window.",
    callback=raise_tutorial,
    threadable=oofmenu.UNTHREADABLE,
    gui_only=1,
    ordering=1000))
mainmenu.OOF.Windows.Tutorial.disable() # there's no window to raise, yet.

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#
                                             
class TutorialClassGUI(subWindow.SubWindow):
    def __init__(self, tutor):
        debug.mainthreadTest()

        for menuitem in mainmenu.OOF.Help.Tutorials.items:
            menuitem.disable()

        subWindow.SubWindow.__init__(self, title=tutor.subject, menu="")

        self.subwindow_menu.File.addItem(oofmenu.OOFMenuItem(
            'Save_Text',
            callback=self.savePrintable,
            params=[filenameparam.WriteFileNameParameter('filename',
                                                         ident="FileMenu"),
                    filenameparam.WriteModeParameter('mode')],
            help="Save the text of this tutorial in a file.",
            no_log=1,
            ordering=-1))

        labelhbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        self.subject = Gtk.Label()
        self.slideIndex = Gtk.Label()
        labelhbox.pack_start(self.subject, expand=True, fill=True, padding=0)
        labelhbox.pack_end(self.slideIndex, expand=False, fill=False, padding=0)
        self.mainbox.pack_start(labelhbox, expand=False, fill=False, padding=0)

        textframe = Gtk.Frame(shadow_type=Gtk.ShadowType.IN)
        self.mainbox.pack_start(textframe,
                                expand=True, fill=True, padding=0)
        self.textview = Gtk.TextView(wrap_mode=Gtk.WrapMode.WORD_CHAR,
                                     left_margin=5, right_margin=5,
                                     top_margin=5, bottom_margin=5)
        self.textview.set_cursor_visible(False)
        self.textview.set_editable(False)
        textframe.add(self.textview)

        buttonbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                             homogeneous=1, spacing=2)
        self.mainbox.pack_end(buttonbox, expand=False, fill=False, padding=0)
        self.backbutton = gtkutils.StockButton("go-previous-symbolic", "Back")
        gtklogger.setWidgetName(self.backbutton, "Back")
        gtklogger.connect(self.backbutton, "clicked", self.backCB)
        self.backbutton.set_tooltip_text("Move to the previous slide.")

        self.nextbutton = gtkutils.StockButton("go-next-symbolic", "Next")
        gtklogger.setWidgetName(self.nextbutton, "Next")
        gtklogger.connect(self.nextbutton, "clicked", self.nextCB)
        self.nextbutton.set_tooltip_text("Move to the next slide.")
        
        self.jumpbutton = gtkutils.StockButton("go-jump-symbolic", "Jump")
        gtklogger.setWidgetName(self.jumpbutton, "Jump")
        gtklogger.connect(self.jumpbutton, "clicked", self.jumpCB)
        self.jumpbutton.set_tooltip_text("Jump to the leading slide.")

        self.savebutton = gtkutils.StockButton("document-save-symbolic",
                                               "Save...")
        gtklogger.setWidgetName(self.savebutton, "Save")
        gtklogger.connect(self.savebutton, "clicked", self.saveCB)
        self.savebutton.set_tooltip_text("Save your tutorial session.")

        self.closebutton = gtkutils.StockButton("window-close-symbolic",
                                                "Close")
        gtklogger.setWidgetName(self.closebutton, "Close")
        gtklogger.connect(self.closebutton, "clicked", self.closeCB)
        self.closebutton.set_tooltip_text("Quit the tutorial.")
        
        buttonbox.pack_start(self.backbutton, expand=True, fill=True, padding=2)
        buttonbox.pack_start(self.nextbutton, expand=True, fill=True, padding=2)
        buttonbox.pack_start(self.jumpbutton, expand=True, fill=True, padding=2)
        buttonbox.pack_start(self.savebutton, expand=True, fill=True, padding=2)
        buttonbox.pack_end(self.closebutton, expand=True, fill=True, padding=2)

        self.gtk.connect('destroy', self.closeCB)
        self.gtk.set_default_size(500, 300)

        self.progress = 0  # How far has the tutorial gone?
                           # It's not affected by "Back" command.
        self.index = 0     # which slide?
        self.tutor = tutor
        self.newLesson()
        self.saved = None  # if saved or not

    def updateGUI(self):
        debug.mainthreadTest()
        self.lesson = self.tutor.lessons[self.index]  # current lesson
        if self.lesson.subject is not None:
            self.subject.set_text(self.lesson.subject)
        else:
            self.subject.set_text("????")
        self.slideIndex.set_text("%d/%d" %
                                 ((self.index+1), len(self.tutor.lessons)))
        
        bfr = self.textview.get_buffer()
        bfr.set_text("")
        bfr.insert_markup(bfr.get_end_iter(), self.lesson.comments, -1)
        self.sensitize()
        self.gtk.show_all()

    def newLesson(self):
        self.updateGUI()

    def sensitize(self):
        debug.mainthreadTest()
        self.backbutton.set_sensitive(self.index != 0)
        self.jumpbutton.set_sensitive(self.index != self.progress)
        self.nextbutton.set_sensitive(self.lesson != self.tutor.lessons[-1])

    def destroy(self):
        self.closeCB()

    def backCB(self, *args):
        self.index -= 1
        self.updateGUI()

    def nextCB(self, *args):
        if self.index == self.progress:  # move forward
            self.progress += 1
            self.index += 1
            self.newLesson()
        else:
            self.index += 1
            self.updateGUI()

    def jumpCB(self, *args):
        self.index = self.progress
        self.updateGUI()

    def saveCB(self, *args):
        filename = fileselector.getFile(
            ident="FileMenu", title="Save Tutorial Session",
            parentwindow=self.gtk)
        if filename is not None:
            phile = open(filename, "w")
            mainmenu.OOF.saveLog(phile)
            phile.write("OOF.Help.Tutorials.Resume(subject='%s', progress=%d)\n"
                       % (self.tutor.subject, self.progress))
            phile.close()
        self.saved = self.progress  # saved!

    def closeCB(self, *args):
        debug.mainthreadTest()        
        global tutorialInProgress
        if self.gtk:
            tutorialInProgress = None
            mainmenu.OOF.Windows.Tutorial.disable()
            for menuitem in mainmenu.OOF.Help.Tutorials.items:
                menuitem.enable()
            self.gtk.destroy()
            self.gtk = None

    def resume(self, where):
        self.progress = where
        self.index = self.progress
        self.updateGUI()

    def savePrintable(self, menuitem, filename, mode):
        file = open(filename, mode.string())
        pageno = 0
        for lesson in self.tutor.lessons:
            pageno += 1
            print(pageno, lesson.subject, file=file)
            print(file=file)               # blank line
            # Split the text up according to paragraphs.
            paragraphs = lesson.comments.split('\n\n')
            # Print out each paragraph, wrapping to 70 character lines. 
            for paragraph in paragraphs:
                print(textwrap.fill(paragraph), file=file)
                print(file=file)           # blank line
        file.close()
