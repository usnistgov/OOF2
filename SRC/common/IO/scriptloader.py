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
import ast
import sys

# class _ScriptExceptHook(excepthook.OOFexceptHook):
#     def __init__(self, scriptloader):
#         self.scriptloader = scriptloader
#     def __call__(self, e_type, e_value, tback):
#         self.scriptloader.error = (e_type, e_value, tback)
#         self.scriptloader.progress.stop()
#         self.scriptloader.errhandler(*self.scriptloader.error)
#         oldhook = excepthook.remove_excepthook(self)

# This flag is used to switch between different versions of
# ScriptLoader.run().  The flag is available as a global variable so
# that test programs know which version is being used, if the format
# of the output (error messages, in particular) depends on the version
# of run().
loadScriptsWithProgress = False

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

    def run(self):
        if loadScriptsWithProgress:
            self.run_with_progress()
        else:
            self.run_no_progress()
    
            
    def run_with_progress(self):
        ## TODO: Fix this.  Despite the comment below, it doesn't
        ## actually work.  Global variables defined in the file are
        ## not available inside a function defined in the file.
        ##
        ## It doesn't work because when a function is called, the
        ## current set of local variables is temporarily added to the
        ## current set of global variables. By passing the same locals
        ## dict to every code snippet, we're losing locally defined
        ## varibles in the calling scope.  Should we never use locals?
        ## Just copy it into globals?

        ## Loop over top-level nodes of the AST. Run one node at a time
        ## by replacing the list of nodes in the AST with a list
        ## containing just the one node.  (This appears to work, but I
        ## have no idea if it's legal.)
        lines = self.get_lines(self.filename)
        try:
            # Get the Abstract Syntax Tree
            self.tree = ast.parse(lines, filename=self.filename)
        except SyntaxError:
            self.show_error(self.filename)
            raise

        codebody = self.tree.body
        if len(codebody) > 0:
            try:
                # self.excepthook = excepthook.assign_excepthook(
                #     _ScriptExceptHook(self))
                lastline = codebody[-1].end_lineno
                for snippet in codebody:
                    self.tree.body = [snippet]
                    code = compile(self.tree, self.filename, "exec")
                    exec(code, globals(), self.locals)
                    self.progress(snippet.lineno, lastline) 
                    if self.stop() or self.error:
                        break
            except Exception as exc:
                self.error = sys.exc_info()
                self.errhandler(*self.error)
#                self.errhandler(*sys.exc_info())
                # excepthook.remove_excepthook(self.excepthook)
            finally:
                self.done()

    def run_no_progress(self):
        lines = self.get_lines(self.filename)
        try:
            exec(lines, globals(), self.locals)
        except SyntaxError as ecx:
            self.show_error(self.filename)
        except Exception as exc:
            self.error = sys.exc_info()
            self.errhandler(*self.error)
            #self.errhandler(*sys.exc_info())
        finally:
            self.done()

    # The following methods can be redefined in derived classes.
    
    def progress(self, current, total): # Called to update progress bar
        pass

    def stop(self):     # Called to see if execution should be stopped
        return False

    def done(self):             # Called when execution is complete
        pass

    def show_error(self, filename): # Called when a syntax error is found
        debug.fmsg("Calling dumpCaller")
        debug.dumpCaller()
        self.error = sys.exc_info()
        raise
    
