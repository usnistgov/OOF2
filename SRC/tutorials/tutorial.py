# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import utils

from ooflib.common.IO import oofmenu
from ooflib.common.IO import mainmenu

allTutorials = {}
        
tutorialMenu = mainmenu.OOF.Help.addItem(
    oofmenu.OOFMenuItem(
        'Tutorials',
        gui_only=1,
        no_log=1,
        ordering=-10,
        help="Interactive tutorials for learning OOF2.",
        discussion="""<para>
        The items in this menu, other than <command>Resume</command>,
        are step-by-step lessons in how to use OOF2.  Please go through
        them in order from <command>A Simple Example</command> to
        <command>Solving Time Dependent Systems</command>.
        </para>""",
        alphabetize=False
    ))

def start_tutorial(tutorial, progress): # redefined in GUI mode
    pass

def startTutorial(menuitem):           
    start_tutorial(menuitem.data, 0)

class TutorialClass:
    def __init__(self, subject, ordering, lessons, tip=None, discussion=None):
        # subject is the title, which will appear in the Tutorials menu.
        # ordering is a number by which tutorials are sorted in the menu.
        # lessons is a list of TutoringItems.
        # tip is a tooltip string for menus and documentation
        # discussion is a short xml text for the manual
        self.subject = subject
        self.lessons = lessons
        self.ordering = ordering
        menuitem = tutorialMenu.addItem(
            oofmenu.OOFMenuItem(utils.space2underscore(subject),
                                ordering=ordering,
                                gui_callback=startTutorial,
                                threadable=oofmenu.UNTHREADABLE,
                                help=tip,
                                discussion=discussion))
        menuitem.data = self
        allTutorials[subject] = self
        
    def getTutorId(self):
        return self.subject

class TutoringItem:
    def __init__(self, subject=None, comments=None):
        self.subject = subject
        self.comments = comments
