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

from gi.repository import Gtk
from gi.repository import Pango

import re
import string
import textwrap


## TODO: Add a table of contents.

## TODO: The Next button isn't sensitized correctly sometimes when a
## saved session is loaded, if the user saves the session after the
## button is sensitized but before clicking Next.  The sensitivity
## probably needs to be saved in the file.

## TODO PYTHON3: Get rid of the signals and just make the Next button
## always sensitive.

boldtag = "BOLD("
lenboldtag = len(boldtag)
delimexpr = re.compile(r'[^\\]\)')      # finds ')' not preceded by '\'
nondelimexpr = re.compile(r'\\\)')      # finds '\)'
parasplit = re.compile(r'\n\s*\n')      # finds lines with only white space
endline = re.compile(r'\s*\n\s*')


## TODO: This is ugly.  It should be rewritten to take advantage of
## pango markup.

class Comment:
    def __init__(self, comment, font=None):
        self.font = font
        self.commentList = []
        self.fontList = []
        # Split comment into paragraphs at blank lines.
        paragraphs = parasplit.split(comment)

        for para in paragraphs:
            # Replace newlines with spaces within paragraphs, and get
            # rid of excess white space.
            para = endline.sub(' ', para).strip()

            # Separate paragraph into strings so that each string has
            # a single font, by looking for BOLD(...).
            while para:
                index_bold = para.find(boldtag)
                if index_bold == -1:    # no bold text in remainder of para
                    self.commentList.append(para)
                    self.fontList.append(0)
                    break
                self.commentList.append(para[:index_bold])
                self.fontList.append(0)
                para = para[index_bold + lenboldtag:]
                # look for closing ')'
                endmatch = delimexpr.search(para)
                if not endmatch:
                    raise ooferror.PyErrPyProgrammingError(
                        "Missing delimeter for BOLD tag in tutorial!")
                boldtext = para[:endmatch.start()+1]
                # replace all occurences of '\)' with ')'
                self.commentList.append(nondelimexpr.sub(')', boldtext))
                self.fontList.append('bold')
                para = para[endmatch.end():]
            self.commentList.append('\n\n')
            self.fontList.append(0)

    def isBold(self, index):
        return self.fontList[index]
    def __len__(self):
        return len(self.commentList)
    def __getitem__(self, i):
        return self.commentList[i]


####################################            

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
    oofmenu.OOFMenuItem('Resume',
                        callback=resume_tutorial,
                        secret=1,
                        params=[parameter.StringParameter('subject'),
                                parameter.IntParameter('progress')],
                        help="Resume a tutorial.  This command is only used when tutorials are saved."
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
        textattrs = self.textview.get_default_attributes()
        self.boldTag = self.textview.get_buffer().create_tag(
            "bold",
            weight=Pango.Weight.BOLD,
            foreground="blue")
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
        self.tutor.lessons[0].activate()
        self.saved = None  # if saved or not

        switchboard.requestCallbackMain("task finished", self.signalCB)

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
        comments = Comment(self.lesson.comments)
        for i in range(len(comments)):
            comment = comments[i]
            font = comments.isBold(i)
            if font:
                bfr.insert_with_tags(bfr.get_end_iter(), comment, self.boldTag)
            else:
                bfr.insert(bfr.get_end_iter(), comment)
        # for s in self.scrollsignals:
        #     s.block()
        # self.msgscroll.get_hadjustment().set_value(0.)
        # self.msgscroll.get_vadjustment().set_value(0.)
        # for s in self.scrollsignals:
        #     s.unblock()
        self.sensitize()
        self.gtk.show_all()

    def newLesson(self):
        self.updateGUI()

    def sensitize(self):
        debug.mainthreadTest()
        # Back, Jump, Done
        self.backbutton.set_sensitive(self.index != 0)
        self.jumpbutton.set_sensitive(self.index != self.progress)
        # Next
        self.nextbutton.set_sensitive(True)  # Default
        if self.index == self.progress:
            if (self.lesson.signal and not self.lesson.done and
                not debug.debug()):
                self.nextbutton.set_sensitive(False)
        if self.lesson == self.tutor.lessons[-1]:  # the last one?
            self.nextbutton.set_sensitive(False)

    def signalCB(self):
        debug.mainthreadTest()
        if self.lesson != self.tutor.lessons[-1]:
            self.nextbutton.set_sensitive(True)

    def destroy(self):
        self.closeCB()

    def backCB(self, *args):
        self.index -= 1
        self.updateGUI()

    def nextCB(self, *args):
        if self.index == self.progress:  # move forward
            self.tutor.lessons[self.progress].deactivate()
            self.progress += 1
            self.tutor.lessons[self.progress].activate()
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
        self.tutor.lessons[self.progress].activate()

    def savePrintable(self, menuitem, filename, mode):
        file = open(filename, mode.string())
        pageno = 0
        for lesson in self.tutor.lessons:
            comments = Comment(lesson.comments)
            pageno += 1
            print(pageno, lesson.subject, file=file)
            print(file=file)               # blank line

            # comments acts like a list of strings, where each string
            # might be formatted differently when displayed in the
            # GUI.  Here we are discarding formatting, so just join
            # all the strings together.
            fulltext = "".join(comments)
            # Now split them up according to paragraphs.
            # Comment.__init__, above, inserted '\n\n' at the ends of
            # paragraphs.
            paragraphs = fulltext.split('\n\n')
            # Now print out each paragraph, wrapping to 70 character lines. 
            for paragraph in paragraphs:
                print(textwrap.fill(paragraph), file=file)
                print(file=file)           # blank line
        file.close()
