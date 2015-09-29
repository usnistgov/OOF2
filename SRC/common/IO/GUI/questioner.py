# -*- python -*-
# $RCSfile: questioner.py,v $
# $Revision: 1.30 $
# $Author: langer $
# $Date: 2009/12/14 20:37:22 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 


# The function 'questioner' brings up a dialog box containing a
# question and a bunch of buttons corresponding to the possible
# answers.  The answer clicked on is returned.  The arguments are the
# question, followed by the answers.  An optional keyword argument,
# 'default', specifies which answer has the focus when the dialog is
# brought up.  If the value of the default argument isn't in the list
# of answers, it is *prepended* to the list.

from ooflib.SWIG.common import guitop
from ooflib.SWIG.common import ooferror
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common import thread_enable
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
import gtk
import threading

# Ugly code here...  We want questions posed with the questioner to be
# completely independent of the GUI, since there's a non-GUI API for
# it.  But in GUI mode it would be nice to have pretty icons on the
# questioner's answer buttons.  The _stock dictionary here maps
# answers to gtk stock icons.  More than one answer string can be
# mapped to the same stock icon.  The stock label won't be used --
# just the icon.  This code is ugly because answers that don't appear
# in this dictionary won't have icons on their buttons -- this file
# has to anticipate questions that will be asked elsewhere.

_stock = {"Yes"    : gtk.STOCK_YES,
          "No"     : gtk.STOCK_NO,
          "No!"     : gtk.STOCK_NO,
          "Cancel" : gtk.STOCK_CANCEL,
          "OK"     : gtk.STOCK_OK,
          "Save"   : gtk.STOCK_SAVE,
          "Don't Save" : gtk.STOCK_DELETE,
          "Append" : gtk.STOCK_ADD
          }

class _Questioner:
    def __init__(self, question, *answers, **kwargs):
        debug.mainthreadTest()

        if len(answers)==0:
            raise ooferror.ErrSetupError(
                "Questioner must have at least one possible answer.")

        self.answers = answers
        self.gtk = gtklogger.Dialog(parent=guitop.top().gtk)
        gtklogger.newTopLevelWidget(self.gtk, "Questioner")
        hbox = gtk.HBox()
        self.gtk.vbox.pack_start(hbox, padding=15)
        hbox.pack_start(gtk.Label(question), padding=15)
        self.defaultbutton = None

        try:
            self.default = kwargs['default']
        except KeyError:
            self.default=None
        else:
            if not self.default in answers:
                self.answers = (self.default,)+answers

        self.answerdict = {}
        count = 1
        for answer in self.answers:
            try:
                stock = _stock[answer]
                button = self.gtk.add_button(stock, count)
                # Replace the label on the stock button with the answer text.
                label = gtkutils.findChild(gtk.Label, button)
                label.set_text(answer)
            except KeyError:
                debug.fmsg('no stock icon for', answer)
                self.gtk.add_button(answer, count)
            self.answerdict[count] = answer
            if answer == self.default:
                self.gtk.set_default_response(count)
            count += 1
        hbox.show_all()

    def inquire(self):
        debug.mainthreadTest()
        result = self.gtk.run()
        self.gtk.destroy()
        if result in (gtk.RESPONSE_DELETE_EVENT, gtk.RESPONSE_NONE):
            return
##            if self.default:
##                return self.default
##            return self.answers[0]
        return self.answerdict[result]

# Wrapper, callable from any thread, which calls questionerGUI
# on the main thread, blocking until it gets the result.
def questioner_(question, *args, **kwargs):
    q = mainthread.runBlock(_Questioner, (question,)+args, kwargs)
    result = mainthread.runBlock(q.inquire)
    return result


questioner = questioner_

# Override non-GUI questioner.
import ooflib.common.IO.questioner
ooflib.common.IO.questioner.questioner = questioner_
