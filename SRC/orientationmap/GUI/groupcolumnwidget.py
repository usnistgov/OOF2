# -*- python -*-

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
from ooflib.orientationmap import genericreader

from gi.repository import Gtk
import types

class GCWidgetRow:
    def __init__(self, table, row, parent):
        self.deleteButton = Gtk.Button('-', halign=Gtk.Align.FILL)
        table.attach(self.deleteButton, 0,row+1, 1,1)
        gtklogger.setWidgetName(self.deleteButton, 'Delete%d' % row)
        gtklogger.connect(self.deleteButton, 'clicked', parent.deleteRowCB, row)
        self.deleteButton.set_tooltip_text("Delete this group definition.")

        self.colEntry = Gtk.Entry()
        table.attach(self.colEntry, 1,row+1, 1,1)
        self.colSignal = gtklogger.connect(self.colEntry, 'changed',
                                           parent.changedCB)
        gtklogger.setWidgetName(self.colEntry, 'Column%d' % row)
        self.colEntry.set_tooltip_text(
            'A column number.  Points in the data file with different '
            'values in this column will be assigned to different pixel groups.'
            )

        self.nameEntry = Gtk.Entry(hexpand=True, halign=Gtk.Align.FILL)
        self.nameEntry.set_text('group_%s')
        table.attach(self.nameEntry, 2,row+1, 1,1)
        self.nameSignal = gtklogger.connect(self.nameEntry, 'changed',
                                            parent.changedCB)
        gtklogger.setWidgetName(self.nameEntry, 'Name%d' % row)
        self.nameEntry.set_tooltip_text(
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
        if isinstance(val[1], (str, bytes)):
            self.colEntry.set_text(val[1])
        else:
            self.colEntry.set_text(repr(val[1]))
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
    def __init__(self, param, scope=None, name=None, **kwargs):
        debug.mainthreadTest()
        quargs = kwargs.copy()
        quargs.setdefault('shadow_type', Gtk.ShadowType.IN)
        frame = Gtk.Frame(**quargs)
        self.table = Gtk.Grid(row_spacing=1, column_spacing=1, margin=1)
        frame.add(self.table)
        gtklogger.setWidgetName(self.table, 'GroupTable')

        addbutton = Gtk.Button('+', hexpand=False)
        gtklogger.setWidgetName(addbutton, "Add")
        gtklogger.connect(addbutton, 'clicked', self.addCB)
        self.table.attach(addbutton, 0,0, 1,1)
        addbutton.set_tooltip_text("Add a new group definition.")

        clabel = Gtk.Label("Column", halign=Gtk.Align.CENTER, hexpand=True)
        cframe = Gtk.Frame(shadow_type=Gtk.ShadowType.IN)
        cframe.add(clabel)
        self.table.attach(cframe, 1,0, 1,1)

        nlabel = Gtk.Label("Name", halign=Gtk.Align.CENTER, hexpand=True)
        nlabel.set_alignment(0.0, 0.5)
        nframe = Gtk.Frame(shadow_type=Gtk.ShadowType.IN)
        nframe.add(nlabel)
        self.table.attach(nframe, 2,0, 1,1)

        self.rows = []          #  list of GCWidgetRow objects

        parameterwidgets.ParameterWidget.__init__(self, frame, scope=scope,
                                                  name=name)
        if param.value is not None:
            self.set_value(param.value)
        self.widgetChanged(self.checkValue(), interactive=0)

    def resize(self, newnrows):
        oldnrows = len(self.rows)
        if oldnrows != newnrows:
            # self.table.resize(newnrows+1, 3)
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
        self.resize(len(self.rows) + 1)
        self.widgetChanged(0, interactive=1)
        self.show()

    def checkValue(self):
        for row in self.rows:
            if not row.checkValue():
                return False
        return True 


def _GroupColParameter_makeWidget(self, scope=None, **kwargs):
    return GroupColumnWidget(self, scope=scope, name=self.name, **kwargs)

genericreader.GroupColumnParameter.makeWidget = _GroupColParameter_makeWidget
