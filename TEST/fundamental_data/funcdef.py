# This tests whether or not the ScriptLoader class can deal with
# function definitions and various scopes.  This test assumes that
# exception handling in scripts is working.

# Ensure that objects defined at module scope are available in
# function scope.  pie should be defined in the
# top OOF scope and equal 3.14.
pie = 3.14

# Check that objects defined in script scope are available within
# functions defined in that scope.  If not, a NameError will be
# raised.

def func(x):
    return pie*x

tart = func(2)




