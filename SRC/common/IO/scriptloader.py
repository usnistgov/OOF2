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

class _ScriptExceptHook(excepthook.OOFexceptHook):
    def __init__(self, scriptloader):
        self.scriptloader = scriptloader
    def __call__(self, e_type, e_value, tback):
        self.scriptloader.error = (e_type, e_value, tback)
        self.scriptloader.errhandler(*self.scriptloader.error)
        oldhook = excepthook.remove_excepthook(self)
        

class ScriptLoader:
    def __init__(self, filename, locals=None, errhandler=None):
        self.filename = filename
        self.locals = locals
        self.error = None
        fileobj = open(self.filename)
        try:
            self.tree = ast.parse(fileobj.read()) # get the Abstract Syntax Tree
        except SyntaxError:
            self.showsyntaxerror(self.filename)
        fileobj.close()
            
    def run(self):
        # Loop over top-level nodes of the AST. Run one node at a time
        # by replacing the list of nodes in the AST with a list
        # containing just the one node.  (This appears to work, but I
        # have no idea if it's legal.)
        if self.error is None:
            codebody = self.tree.body
            if len(codebody) > 0:
                self.excepthook = excepthook.assign_excepthook(
                    _ScriptExceptHook(self))
                lastline = codebody[-1].end_lineno
                for snippet in codebody:
                    self.tree.body = [snippet]
                    code = compile(self.tree, self.filename, "exec")
                    exec(code, globals(), self.locals)
                    self.progress(snippet.lineno, lastline) 
                    if self.stop() or self.error:
                        break
                excepthook.remove_excepthook(self.excepthook)
        self.done()

    def progress(self, current, total): # May be redefined in subclasses
        pass

    def stop(self):             # Call this to stop execution
        return False

    def done(self):             # Called when execution is complete
        pass

    def showsyntaxerror(self, filename):
        self.error = sys.exc_info()
        raise
    
