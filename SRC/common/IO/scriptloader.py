# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# ScriptLoader loads and executes a python file.  It provides hooks
# that can be redefined in a derived class to update a progress bar
# and to halt processing.

from ooflib.common import debug
from ooflib.common import excepthook
from ooflib.SWIG.common import ooferror
from ooflib.common import utils
import ast
import sys

class _ScriptException(ooferror.PyOOFError):
    def __init__(self, filename, line=None):
        self.filename = filename
        self.line = line
    def __repr__(self):
        return self.__class__.__name__

class ScriptInterrupt(_ScriptException):
    def __str__(self):
        if self.line is not None:
            return f"Interrupted while running file \"{self.filename}\", line {self.line}"
        return f"Interrupted while running file {self.filename}"

class ScriptParseError(_ScriptException):
    def __str__(self):
        return f"Error parsing file \"{self.filename}\""
    def __repr__(self):
        return self.__class__.__name__
    
class ScriptException(_ScriptException):
    def __str__(self):
        if self.line is not None:
            return f"Error running file \"{self.filename}\", line {self.line}"
        return f"Error running file {self.filename}"
    def __repr__(self):
        return self.__class__.__name__

utils.OOFdefine("ScriptException", ScriptException)
utils.OOFdefine("ScriptParseError", ScriptParseError)
utils.OOFdefine("ScriptInterrupt", ScriptInterrupt)
        
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class ScriptLoader:
    def __init__(self, filename, locals=None, errhandler=None):
        self.filename = filename
        self.error = None

        # When this is used in SRC/common/IO/mainmenu.py, via the
        # PScriptLoader class, locals is set to the main OOF
        # namespace, sys.modules['__main__'].__dict__.
        self.locals = locals

        # self.errhandler is set this way, and not via a default
        # argument, because excepthook.displayTraceBack may change
        # between class definition and instantiation.

        # In GUI mode, displayTraceBack is set to gui_printTraceBack
        # when reporter_GUI.py is loaded.  In text mode, it's an
        # OOFexceptHook instance, defined in excepthook.py.
        self.errhandler = errhandler or excepthook.displayTraceBack

    def get_lines(self, filename):
        fileobj = None
        try:
            fileobj = open(filename, "r")
            lines = fileobj.read()
        except Exception as exc:
            raise ooferror.PyErrUserError(f"Script {filename} not found!")
        finally:
            if fileobj is not None:
                fileobj.close()
        return lines

    # The following methods can be redefined in derived classes.
    
    def progress(self, current, total): # Called to update progress bar
        pass

    def stop(self):     # Called to see if execution should be stopped
        return False

    def done(self):             # Called when execution is complete
        pass

    # def show_error(self, filename): # Called when an error is found
    #     pass
    #self.error = sys.exc_info()

    def run(self):
        # Loop over top-level nodes of the python Abstract Symbol
        # Tree. Run one node at a time by replacing the list of nodes
        # in the AST with a list containing just the one node.  (This
        # appears to work, but I have no idea if it's legal.)
        lines = self.get_lines(self.filename)
        try:
            self.tree = ast.parse(lines, filename=self.filename)
        except SyntaxError as exc:
            raise ScriptParseError(self.filename) from exc
            # self.error = sys.exc_info()
            # print(f"Caught SyntaxError: {self.error}")
            # self.errhandler(*self.error)
            # self.show_error(self.filename) # sets self.error
        codebody = self.tree.body
        
        if len(codebody) > 0:
            try:
                # self.excepthook = excepthook.assign_excepthook(
                #     _ScriptExceptHook(self))
                lastline = codebody[-1].end_lineno
                curline = 0
                for snippet in codebody:
                    curline = snippet.lineno
                    self.tree.body = [snippet]
                    code = compile(self.tree, self.filename, "exec")
                    exec(code, globals()|self.locals, self.locals)
                    self.progress(snippet.lineno, lastline) 
                    if self.stop():
                        raise ScriptInterrupt(self.filename, snippet.lineno)
            except ScriptInterrupt as exc:
                # This script was interrupted.
                debug.fmsg("Interrupted!")
                raise ScriptInterrupt(self.filename, curline.lineno) from exc
            except ScriptException as exc:
                # A subscript raised an exception
                raise ScriptException(self.filename, curline) from exc
            except Exception as exc:
                # Something else bad happened
                raise ScriptException(self.filename, curline) from exc
            finally:
                self.done()

