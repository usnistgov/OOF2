# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from . import adopteelogger
from . import loggers
from . import widgetlogger

# Loggers for various components of a TreeView.

class TreeViewLogger(widgetlogger.WidgetLogger): # I'm a lumberjack and I'm OK.
    classes = (Gtk.TreeView,)
    def record(self, obj, signal, *args):
        if signal == 'row-activated':
            path = args[0].get_indices() # args[0] is a Gtk.TreePath object
            col = args[1]                # gtk.TreeViewColumn obj
            cols = obj.get_columns()
            i = cols.index(col)
            return [
                "tree=%s" % self.location(obj, *args),
                "column = tree.get_column(%d)" % i,
                "tree.row_activated(Gtk.TreePath(%s), column)" % path
                    ]
        if signal == 'row-expanded':
            path = args[1]
            return ["%s.expand_row(Gtk.TreePath(%s), open_all=False)"
                    % (self.location(obj, *args), path.get_indices())]
        if signal == 'row-collapsed':
            path = args[1]
            return ["%s.collapse_row(Gtk.TreePath(%s))"
                    % (self.location(obj,*args), path.get_indices())]
        return super(TreeViewLogger, self).record(obj, signal, *args)

class TreeViewColumnLogger(adopteelogger.AdopteeLogger):
    classes = (Gtk.TreeViewColumn,)
    def record(self, obj, signal, *args):
        if signal == 'clicked':
            # Click in the header of a column in a TreeView
            return ["%s.clicked()" % self.location(obj, args)]
        return super(TreeViewColumnLogger, self).record(obj, signal, *args)

class TreeSelectionLogger(adopteelogger.AdopteeLogger):
    classes = (Gtk.TreeSelection,)
    def record(self, obj, signal, *args):
        if signal == 'changed':
            # See comments in the gtklogger README about handling
            # TreeSelection "changed" signals.
            if obj.get_mode()==Gtk.SelectionMode.MULTIPLE:
                model, rows = obj.get_selected_rows()
                # Unselecting all rows and then selecting the selected
                # ones seems wrong, since unselecting and reselecting
                # might have side effects.  It would be much better
                # just to select or unselect the changed rows, but I
                # don't see how to do that simply.
                return ["%s.unselect_all()" % self.location(obj, *args)] + \
                       ["%s.select_path(Gtk.TreePath(%s))"
                           % (self.location(obj,*args), row.get_indices())
                        for row in rows]
            else:                       # single selection only
                model, iter = obj.get_selected()
                if iter is not None:
                    path = model.get_path(iter).get_indices()
                    return ["%s.select_path(Gtk.TreePath(%s))" 
                            % (self.location(obj, *args), path)]
                else:
                    return ["%s.unselect_all()" % self.location(obj, *args)]
        return super(TreeSelectionLogger, self).record(obj, signal, *args)

class ListStoreLogger(adopteelogger.AdopteeLogger):
    classes = (Gtk.ListStore,)
    insertrow = None                      # destination for row drag'n'drop
    def record(self, obj, signal, *args):
        ## TODO: Logging the row-inserted and row-deleted signals has
        ## not been tested because drag and drop isn't working in OOF2
        ## (yet).  When this is implemented, if the local variables
        ## dvar and lvar are still needed they should be handled the
        ## same way as wvar in the focus_out_event handler in
        ## WidgetLogger.record in widgetlogger.py.
        
        # Drag-and-drop of a line within a ListStore creates a pair of
        # row-inserted and row-deleted signals, with row-inserted
        # coming first.  The two must be logged together, so we don't
        # actually return a non-trivial result until getting the
        # second signal.  If the user has two mice and drags rows of
        # two ListStores simultaneously, this won't work.
        if signal == "row-inserted":
            ListStoreLogger.insertrow = args[0][0] # args[0] is a gtk tree path
            return self.ignore
        if signal == "row-deleted":
            if ListStoreLogger.insertrow is None:
                return self.ignore
            deleterow = args[0][0]      # args[0] is a gtk tree path
            destrow = ListStoreLogger.insertrow # destination row
            # The row to be deleted contains the data that has to be
            # inserted in the new row. "deleterow" was set after the
            # new row was inserted (because 'row-deleted' was sent
            # after 'row-inserted'), so if the new row comes before
            # the deleted row in the list, then on replay, where
            # nothing has happened yet, the row to be deleted has a
            # different index than the source row.
            if ListStoreLogger.insertrow < deleterow:
                sourcerow = deleterow - 1
            else:
                sourcerow = deleterow
            ListStoreLogger.insertrow = None
            lvar = loggers.localvar('ls')
            dvar = loggers.localvar('data')
            return [
"%s = %s" % (lvar, self.location(obj, *args)),
"%(data)s = [%(ls)s.get_value(%(ls)s.get_iter((%(r)d,)),i) for i in range(%(ls)s.get_n_columns())]" % dict(r=sourcerow, data=dvar, ls=lvar),
"%s.insert(%d, %s)" % (lvar, destrow, dvar),
                "%(ls)s.remove(%(ls)s.get_iter((%(r)d,)))" % dict(r=deleterow, ls=lvar),
                "del %s, %s" % (lvar, dvar)
                ]

        return super(ListStoreLogger, self).record(obj, signal, *args)

class CellRendererLogger(adopteelogger.AdopteeLogger):
    classes = (Gtk.CellRenderer,)
    def record(self, obj, signal, *args):
        if signal == 'toggled':
            # args[0] is a tuple of strings representing ints, NOT a
            # Gtk.TreePath.  I don't know why this case is different
            # from the cases above, where an actual Gtk.TreePath is
            # passed in.
            path = args[0]
            return ["%s.emit('toggled', Gtk.TreePath(%s))"
                    % (self.location(obj, *args), path)]
        return super(CellRendererLogger, self).record(obj, signal, *args)

