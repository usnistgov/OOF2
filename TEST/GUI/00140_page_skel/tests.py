# -*- python -*-
# $RCSfile: tests.py,v $
# $Revision: 1.3 $
# $Author: langer $
# $Date: 2014/09/27 21:41:56 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *

removefile('bones.dat')

def sensitization0():
    return (sensitizationCheck({'Microstructure' : 0,
                                'Skeleton' : 0,
                                'New' : 0,
                                'Simple' : 0,
                                'Rename' : 0,
                                'Copy' : 0,
                                'Delete' : 0,
                                'Save' : 0,
                                },
                               base='OOF2:Skeleton Page')
            and 
            sensitizationCheck({'Method:Chooser' : 1,
                                'OK' : 0,
                                'Prev' : 0,
                                'Next' : 0,
                                'Undo' : 0,
                                'Redo' : 0
                                },
                               base='OOF2:Skeleton Page:Pane:Modification'))

def sensitization1():
    return (sensitizationCheck({'Microstructure' : 1,
                                'Skeleton' : 0,
                                'New' : 1,
                                'Simple' : 1,
                                'Rename' : 0,
                                'Copy' : 0,
                                'Delete' : 0,
                                'Save' : 0,
                                },
                               base='OOF2:Skeleton Page')
            and
            sensitizationCheck({'Method:Chooser' : 1,
                                'OK' : 0,
                                'Prev' : 0,
                                'Next' : 0,
                                'Undo' : 0,
                                'Redo' : 0
                                },
                               base='OOF2:Skeleton Page:Pane:Modification'))

def sensitization2():
    return (sensitizationCheck({'Microstructure' : 1,
                                'Skeleton' : 1,
                                'New' : 1,
                                'Simple' : 1,
                                'Rename' : 1,
                                'Copy' : 1,
                                'Delete' : 1,
                                'Save' : 1,
                                },
                               base='OOF2:Skeleton Page')
            and
            sensitizationCheck({'Method:Chooser' : 1,
                                'OK' : 1,
                                'Prev' : 0,
                                'Next' : 0,
                                'Undo' : 0,
                                'Redo' : 0
                                },
                               base='OOF2:Skeleton Page:Pane:Modification'))

def sensitization3():
    return (sensitizationCheck({'Microstructure' : 1,
                                'Skeleton' : 1,
                                'New' : 1,
                                'Simple' : 1,
                                'Rename' : 1,
                                'Copy' : 1,
                                'Delete' : 1,
                                'Save' : 1,
                                },
                               base='OOF2:Skeleton Page')
            and
            sensitizationCheck({'Method:Chooser' : 1,
                                'OK' : 1,
                                'Prev' : 0,
                                'Next' : 0,
                                'Undo' : 1,
                                'Redo' : 0
                                },
                               base='OOF2:Skeleton Page:Pane:Modification'))

def sensitization4():
    return (sensitizationCheck({'Microstructure' : 1,
                                'Skeleton' : 1,
                                'New' : 1,
                                'Simple' : 1,
                                'Rename' : 1,
                                'Copy' : 1,
                                'Delete' : 1,
                                'Save' : 1,
                                },
                               base='OOF2:Skeleton Page')
            and
            sensitizationCheck({'Method:Chooser' : 1,
                                'OK' : 1,
                                'Prev' : 0,
                                'Next' : 0,
                                'Undo' : 0,
                                'Redo' : 1
                                },
                               base='OOF2:Skeleton Page:Pane:Modification'))

def sensitization5():
    return (sensitizationCheck({'Microstructure' : 1,
                                'Skeleton' : 1,
                                'New' : 1,
                                'Simple' : 1,
                                'Rename' : 1,
                                'Copy' : 1,
                                'Delete' : 1,
                                'Save' : 1,
                                },
                               base='OOF2:Skeleton Page')
            and
            sensitizationCheck({'Method:Chooser' : 1,
                                'OK' : 1,
                                'Prev' : 1,
                                'Next' : 0,
                                'Undo' : 1,
                                'Redo' : 0
                                },
                               base='OOF2:Skeleton Page:Pane:Modification'))

def sensitization6():
    return (sensitizationCheck({'Microstructure' : 1,
                                'Skeleton' : 1,
                                'New' : 1,
                                'Simple' : 1,
                                'Rename' : 1,
                                'Copy' : 1,
                                'Delete' : 1,
                                'Save' : 1,
                                },
                               base='OOF2:Skeleton Page')
            and
            sensitizationCheck({'Method:Chooser' : 1,
                                'OK' : 1,
                                'Prev' : 1,
                                'Next' : 0,
                                'Undo' : 0,
                                'Redo' : 0
                                },
                               base='OOF2:Skeleton Page:Pane:Modification'))

def sensitization7():
    return (sensitizationCheck({'Microstructure' : 1,
                                'Skeleton' : 1,
                                'New' : 1,
                                'Simple' : 1,
                                'Rename' : 1,
                                'Copy' : 1,
                                'Delete' : 1,
                                'Save' : 1,
                                },
                               base='OOF2:Skeleton Page')
            and
            sensitizationCheck({'Method:Chooser' : 1,
                                'OK' : 1,
                                'Prev' : 1,
                                'Next' : 0,
                                'Undo' : 1,
                                'Redo' : 1
                                },
                               base='OOF2:Skeleton Page:Pane:Modification'))

def sensitization8():
    return (sensitizationCheck({'Microstructure' : 1,
                                'Skeleton' : 1,
                                'New' : 1,
                                'Simple' : 1,
                                'Rename' : 1,
                                'Copy' : 1,
                                'Delete' : 1,
                                'Save' : 1,
                                },
                               base='OOF2:Skeleton Page')
            and
            sensitizationCheck({'Method:Chooser' : 1,
                                'OK' : 1,
                                'Prev' : 0,
                                'Next' : 1,
                                'Undo' : 1,
                                'Redo' : 0
                                },
                               base='OOF2:Skeleton Page:Pane:Modification'))

def sensitization9():
    return (sensitizationCheck({'Microstructure' : 1,
                                'Skeleton' : 0,
                                'New' : 1,
                                'Simple' : 1,
                                'Rename' : 0,
                                'Copy' : 0,
                                'Delete' : 0,
                                'Save' : 0,
                                },
                               base='OOF2:Skeleton Page')
            and
            sensitizationCheck({'Method:Chooser' : 1,
                                'OK' : 0,
                                'Prev' : 1,
                                'Next' : 0,
                                'Undo' : 0,
                                'Redo' : 0
                                },
                               base='OOF2:Skeleton Page:Pane:Modification'))

def sensitization10():
    return (sensitizationCheck({'Microstructure' : 0,
                                'Skeleton' : 0,
                                'New' : 0,
                                'Simple' : 0,
                                'Rename' : 0,
                                'Copy' : 0,
                                'Delete' : 0,
                                'Save' : 0,
                                },
                               base='OOF2:Skeleton Page')
            and
            sensitizationCheck({'Method:Chooser' : 1,
                                'OK' : 0,
                                'Prev' : 1,
                                'Next' : 0,
                                'Undo' : 0,
                                'Redo' : 0
                                },
                               base='OOF2:Skeleton Page:Pane:Modification'))

