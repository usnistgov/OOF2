# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Menu operations for the message manager -- operations for
# changing what is reported on the command-line, plus an entry
# which can be used in the GUI to bring up a new message window.
# Also, menu logging via the message manager is enabled here.

# In the documentation, the menu OOF.Windows.Messages.Messages_1 is
# renamed OOF.Windows.Messages.Messages_n by a sed command in
# MAN_OOF2/Makefile.


from ooflib.common.IO import mainmenu
from ooflib.common.IO import reporter
mainmenu.OOF.addLogger(reporter.log)

from ooflib.common.IO import oofmenu

def new_messages(menuitem):
    reporter._new_messages()

winmenu = mainmenu.OOF.Windows

messagemenu = oofmenu.OOFMenuItem(
    'Messages',
    help="Windows for output, information, and other text.",
    discussion="""<para>

    The <link linkend="Section-Windows-Messages">Messages
    Window</link> displays various kinds of communications from &oof2;
    to the user.
    
    </para>""",
    xrefs=["Section-Windows-Messages"]
)

messagemenu.addItem(oofmenu.OOFMenuItem(
    'New', callback=new_messages,
    help="Open a new Messages window.",
    no_log=1,
    threadable=oofmenu.UNTHREADABLE,
    discussion="""<para>

    Open a new <link
    linkend='Section-Windows-Messages'>Messages</link> window.  The
    window will be called <quote>Messages_&lt;n&gt;</quote>, where
    &lt;n&gt; is an integer.  Different Messages windows can be
    configured to display different data.

    </para>"""
))

winmenu.addItem(messagemenu)

