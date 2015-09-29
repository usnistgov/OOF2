# -*- python -*-
# $RCSfile: groupcolumnwidget.py,v $
# $Revision: 1.2 $
# $Author: langer $
# $Date: 2012/03/08 19:48:46 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.common import debug
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import tooltips
from ooflib.orientationmap import genericreader

import gtk
import types

class GCWidgetRow(object):
    def __init__(self, table, row, parent):
        self.deleteButton = gtk.Button('-')
        table.attach(self.deleteButton, 0,1, row+1,row+2,
                     xoptions=gtk.FILL, yoptions=0, xpadding=0, ypadding=0)
        gtklogger.setWidgetName(self.deleteButton, 'Delete%d' % row)
        gtklogger.connect(self.deleteButton, 'clicked', parent.deleteRowCB, row)
        tooltips.set_tooltip_text(self.deleteButton,
                                  "Delete this group definition.")

        self.colEntry = gtk.Entry()
        table.attach(self.colEntry, 1,2, row+1,row+2,
                     xoptions=0, yoptions=0, xpadding=0, ypadding=0)
        self.colSignal = gtklogger.connect(self.colEntry, 'changed',
                                           parent.changedCB)
        gtklogger.setWidgetName(self.colEntry, 'Column%d' % row)
        tooltips.set_tooltip_text(
            self.colEntry,
            'A column number.  Points in the data file with different '
            'values in this column will be assigned to different pixel groups.'
            )

        self.nameEntry = gtk.Entry()
        self.nameEntry.set_text('group_%s')
        table.attach(self.nameEntry, 2,3, row+1,row+2,
                     xoptions=gtk.FILL|gtk.EXPAND, yoptions=0,
                     xpadding=0, ypadding=0)
        self.nameSignal = gtklogger.connect(self.nameEntry, 'changed',
                                            parent.changedCB)
        gtklogger.setWidgetName(self.nameEntry, 'Name%d' % row)
        tooltips.set_tooltip_text(
            self.nameEntry, 
            'The name to assign to the group. A "%s" in the name '
            'will be replaced by the contents of the column.'
            )

        
    def suppress(self):
        self.nameSignal.block()
        self.colSignal.block()
    def unsuppress(self):
        self.nameSignal.unblock()
        self.colSignal.unblock()
    def get_value_as_text(self):
        return (self.nameEntry.get_text(), self.colEntry.get_text())
    def set_value(self, val):
        self.suppress()
        self.nameEntry.set_text(val[0])
        if type(val[1]) is types.StringType:
            self.colEntry.set_text(val[1])
        else:
            self.colEntry.set_text(`val[1]`)
        self.unsuppress()
    def checkValue(self):
        try:
            col = int(self.colEntry.get_text())
        except ValueError:
            return False
        return bool(self.nameEntry.get_text().strip())
    def destroy(self):
        self.nameEntry.destroy()
        self.colEntry.destroy()
        self.deleteButton.destroy()


class GroupColumnWidget(parameterwidgets.ParameterWidget):
    def __init__(self, param, scope=None, name=None):
        debug.mainthreadTest()
        frame = gtk.Frame()
        frame.set_shadow_type(gtk.SHADOW_IN)
        self.table = gtk.Table(rows=1, columns=3)
        self.table.set_row_spacings(0)
        self.table.set_col_spacings(0)
        frame.add(self.table)
        gtklogger.setWidgetName(self.table, 'GroupTable')

        addbutton = gtk.Button('+')
        gtklogger.setWidgetName(addbutton, "Add")
        gtklogger.connect(addbutton, 'clicked', self.addCB)
        self.table.attach(addbutton, 0,1, 0,1, xoptions=gtk.FILL, yoptions=0,
                     xpadding=0, ypadding=0)
        tooltips.set_tooltip_text(addbutton, "Add a new group definition.")

        clabel = gtk.Label("Column")
        clabel.set_alignment(0.0, 0.5)
        cframe = gtk.Frame()
        cframe.set_shadow_type(gtk.SHADOW_OUT)
        cframe.add(clabel)
        self.table.attach(cframe, 1,2, 0,1,
                          xoptions=gtk.FILL|gtk.EXPAND, yoptions=gtk.FILL,
                          xpadding=0, ypadding=0)

        nlabel = gtk.Label("Name")
        nlabel.set_alignment(0.0, 0.5)
        nframe = gtk.Frame()
        nframe.set_shadow_type(gtk.SHADOW_OUT)
        nframe.add(nlabel)
        self.table.attach(nframe, 2,3, 0,1,
                          xoptions=gtk.FILL|gtk.EXPAND, yoptions=gtk.FILL,
                          xpadding=0, ypadding=0)

        self.rows = []          #  list of GCWidgetRow objects

        parameterwidgets.ParameterWidget.__init__(self, frame, scope=scope,
                                                  name=name)
        if param.value is not None:
            self.set_value(param.value)
        self.widgetChanged(self.checkValue(), interactive=0)

    def nrows(self):
        return self.table.get_property('n-rows') - 1

    def resize(self, newnrows):
        oldnrows = self.nrows()
        if oldnrows != newnrows:
            self.table.resize(newnrows+1, 3)
            if oldnrows < newnrows:
                for r in range(oldnrows, newnrows):
                    self.rows.append(GCWidgetRow(self.table, r, self))
            if oldnrows > newnrows:
                del self.rows[newnrows:]

    def set_value(self, value):
        debug.mainthreadTest()
        newnrows = len(value)
        self.resize(newnrows)
        for r in range(newnrows):
            self.rows[r].set_value(value[r])
        self.widgetChanged(self.checkValue(), interactive=0)

    def get_value_as_text(self):
        return [r.get_value_as_text() for r in self.rows]

    def get_value(self):
        return [(n, int(c)) for n,c in self.get_value_as_text()]

    def changedCB(self, gtkobj):
        self.widgetChanged(self.checkValue(), interactive=1)

    def deleteRowCB(self, gtkobj, which):
        vals = self.get_value_as_text()
        del vals[which]
        self.rows[which].destroy()
        self.set_value(vals)
        self.show()
        

    def addCB(self, gtkobj):
        self.resize(self.nrows() + 1)
        self.widgetChanged(0, interactive=1)
        self.show()

    def checkValue(self):
        for row in self.rows:
            if not row.checkValue():
                return False
        return True 


def _GroupColParameter_makeWidget(self, scope=None):
    return GroupColumnWidget(self, scope=scope, name=self.name)

genericreader.GroupColumnParameter.makeWidget = _GroupColParameter_makeWidget
