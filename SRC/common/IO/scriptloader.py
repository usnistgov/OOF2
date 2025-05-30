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

# # This flag is used to switch between different versions of
# # ScriptLoader.run().  The flag is available as a global variable so
# # that test programs know which version is being used, if the format
# # of the output (error messages, in particular) depends on the version
# # of run().
# #  Loader types are
# #    basic: Uses exec(lines), does not do progress bars, can't be interrupted
# #    ast:   Uses Abstract Syntax Tree to evaluate blocks of code
# #    trace: Uses sys.settrace to keep track line execution. May be slow?
# _loaderType = "ast"

# def isLoaderType(lt):
#     assert lt in ("basic", "ast", "trace")
#     return _loaderType == lt

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class _ScriptException(ooferror.PyOOFError):
    def __init__(self, filename):
        self.filename = filename

## TODO? __str__ should return a string that is independent of how the
## program was built, so that it's reproducible in testing. That means
## that it can't include the file name.  But these exceptions aren't
## ever exposed to the user directly, and might not ever appear in the
## test suites either.  Maybe something like
## ooferror.sourcePathPrefix() can be used when these exceptions are
## needed in the tests.
        
class ScriptInterrupt(_ScriptException):
    def __str__(self):
        return f"Interrupted while running file {self.filename}"

class ScriptException(_ScriptException):
    def __str__(self):
        return f"Error running file {self.filename}"

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
            raise ScriptException(self.filename) from exc
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
                for snippet in codebody:
                    self.tree.body = [snippet]
                    code = compile(self.tree, self.filename, "exec")
                    exec(code, globals()|self.locals, self.locals)
                    self.progress(snippet.lineno, lastline) 
                    if self.stop():
                        raise ScriptInterrupt(self.filename)
            except ScriptInterrupt as exc:
                # This script was interrupted.
                debug.fmsg("Interrupted!")
                raise ScriptInterrupt(self.filename) from exc
            except ScriptException as exc:
                raise ScriptException(self.filename) from exc
            except Exception as exc:
                debug.fmsg(f"Caught an exception: {exc}")
                raise ScriptException(self.filename) from exc
            finally:
                self.done()

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Attempt to use sys.settrace to write a version of ScriptLoader that
# might be less hacky that the AST version above.  However, by adding
# a callback to every Python line, it might be slow.  This may be
# using obsolete error handling.

# import os

# class ScriptLoader:
#     ...
#     def __run__(self):
#         debug.fmsg()
#         lines = self.get_lines(self.filename)
#         sys.settrace(Tracer(self))
#         try:
#             # This sets frame.f_code.co_filename to '<string>'.  Can
#             # we distinguish that from any other exec lines that might
#             # be run by the script?
#             exec(lines, globals()|self.locals, self.locals())
#             # exec(lines, globals(), self.locals)            
#         except _StopLoading:
#             return
#         except SyntaxError as exc:
#             sys.settrace(None)
#             self.show_error(self.filename)
#             raise
#         except Exception as exc:
#             sys.settrace(None)
#             self.error = sys.exc_info()
#             self.errhandler(*self.error)
#         finally:
#             sys.settrace(None)
#             self.done()

# class _StopLoading(Exception):
#     pass

# class Tracer:
#     def __init__(self, loader):
#         self.loader = loader
#         self.fname = os.path.abspath(loader.filename)
#         self.lineno = 0
#     def __call__(self, frame, event, arg):
#         if event == 'line':
#             # print("Tracer:", self.fname, frame.f_lineno)
#             if frame.f_code.co_filename == self.fname:
#                 if self.lineno < frame.f_lineno:
#                     self.lineno = frame.f_lineno
#                     self.loader.progress.progress(self.lineno,
#                                                   self.loader.lastline)
#                     if self.loader.stop():
#                         sys.settrace(None)
#                         raise _StopLoading
#         return self
        
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Simple version of ScriptLoader, that doesn't support progress bars.
# This may be using obsolete error handling.

# class ScriptLoader:
#     ...
#     def run_basic(self):
#         debug.fmsg()
#         lines = self.get_lines(self.filename)
#         try:
#             exec(lines, globals()|locals(), None)
#         except SyntaxError as exc:
#             self.show_error(self.filename)
#             debug.fmsg("run_no_progress: caught", exc)
#             raise
#         except Exception as exc:
#             self.error = sys.exc_info()
#             self.errhandler(*self.error)
#         finally:
#             self.done()

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

