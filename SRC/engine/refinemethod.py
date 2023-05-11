# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.engine import ooferror
from ooflib.common import debug
from ooflib.common import utils
from ooflib.common import enum
from ooflib.common.IO import xmlmenudump

from ooflib.engine import skeletonelement
ProvisionalQuad = skeletonelement.ProvisionalQuad
ProvisionalTriangle = skeletonelement.ProvisionalTriangle

class RefinementRuleSet:
    allRuleSets = []
    ruleDict = {}
    def __init__(self, name, maxMarks, parent=None, help=None):
        self.rules = {}
        self._name = name
        self._maxMarks = maxMarks
        self._help = help
        RefinementRuleSet.allRuleSets.append(self)
        RefinementRuleSet.ruleDict[name] = self
        if parent:
            self.parent = RefinementRuleSet.ruleDict[parent]
        else:
            self.parent = None
        # updateRuleEnum(name, help) 
    def name(self):
        return self._name
    def help(self):
        return self._help
    def __repr__(self):
        return "getRuleSet('%s')" % self.name()
    def addRule(self, rule, signature):
        self.rules[signature] = rule
    def getRule(self, signature):
        try:
            return self.rules[signature]
        except KeyError:
            if self.parent:
                return self.parent.getRule(signature)
            raise ooferror.PyErrPyProgrammingError(
                f"Refinement rule {signature} not found!")
    def __getitem__(self, signature):
        return self.getRule(signature)
    def maxMarks(self):
        # maximum number of marks on an edge that this rule set can handle
        return self._maxMarks
        
def getRuleSet(name):
    return RefinementRuleSet.ruleDict[name]

utils.OOFdefine('getRefineRuleSet', getRuleSet)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# The large rule set includes all possible subdivisions of all
# signatures, including ones with internal nodes, within reason.  The
# quick rule set is faster to apply, but includes only the simplest
# subdivisions.  
#
# A missing function in the large rule set will be found in the
# quick ruleset, so if there's no difference between the quick and
# large refinements for a signature, just define the quick one.

## TODO PYTHON3?  To make the large rule set really large, we
## could automatically extend each rule by dividing its quads.  This
## could be done automatically when the rule is added to the rule set.
## It would greatly increase the size of the rule set.
##
## Since we are inconsistent about which rules include divided quads,
## perhaps we should *never* create two triangles when we could create
## one quad, but should automatically run SplitQuads after refining.

quickRules = RefinementRuleSet(
    'Quick', 2,
    help="A small set of refinement rules. Quick to apply but maybe not giving great results."
)

largeRules = RefinementRuleSet(
    'Large', 2, parent="Quick",
    help="All reasonable ways of subdividing elements."
)

# The names of the refinement rule sets are stored in an Enum so that
# the UI can handle them correctly.

class RuleSet(enum.EnumClass(*[(r.name(), r.help())
                               for r in RefinementRuleSet.allRuleSets])):
    pass
utils.OOFdefine('RuleSet', RuleSet)

RuleSet.tip = "Refinement rule sets."
RuleSet.discussion = xmlmenudump.loadFile('DISCUSSIONS/engine/enum/ruleset.xml')


def updateRuleEnum(name, help=None):
    enum.addEnumName(RuleSet, name, help)

# This function is used to get the default value for the RuleSet
# parameter in the refinement menu item.
def defaultRuleSetEnum():
    return RuleSet(RefinementRuleSet.allRuleSets[0].name())

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class RefinementRule:
    def __init__(self, ruleset, signature, function):
        self.function = function
        ruleset.addRule(self, signature)
    def apply(self, element, rotation, edgenodes, newSkeleton, alpha):
        # debug.fmsg(
        #     f"{element=} function={self.function.__name__} {edgenodes=}")
        return self.function(element, rotation, edgenodes, newSkeleton, alpha)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#    

# This function is called with an old element and an integer
# 'rotation'.  It returns copies (children in the SkeletonSelectable
# sense) of the nodes of the old element, with the order shifted
# around by the rotation.  The new refined elements will be built from
# these base nodes.

def baseNodes(element, rotation):
    return map(lambda x: x.children[-1],
               element.nodes[rotation:] + element.nodes[0:rotation])
    ## TODO OPT: The old way (below) has moduluses in it, so I changed
    ## it, but haven't actually checked that the new way (above) is
    ## faster.
    # nnodes = element.nnodes()
    # return [element.nodes[(i+rotation)%nnodes].children[-1]
    #         for i in range(nnodes)]

class ProvisionalRefinement:
    def __init__(self, newbies = [], internalNodes = []):
        self.newbies = newbies   # new elements
        self.internalNodes = internalNodes
        self.illegal = False
        # It is not an error if a ProvisionalRefinement contains
        # illegal elements, if the refinement rule provides another
        # ProvisionalRefinement that can be used instead.  But we do
        # need to check.
        for i, element in enumerate(newbies):
            if element.illegal():
                self.illegal = True
                break
    def energy(self, skeleton, alpha):
        energy = 0.0
        for element in self.newbies:
            energy += element.energyTotal(skeleton, alpha)
        return energy/len(self.newbies)
    def accept(self, skeleton):
        return [element.accept(skeleton) for element in self.newbies]
    def __repr__(self):
        return "ProvisionalRefinement" + f"{tuple(self.newbies)}"
        

def theBetter(skeleton, candidates, alpha):
    energy_min = 100000.                # much larger than any possible energy
    theone = None
    for candi in candidates:
        if not candi.illegal:
            energy = candi.energy(skeleton, alpha)
            if energy < energy_min:
                energy_min = energy
                theone = candi
    # Before returning the chosen refinement, we need to remove any internal
    # nodes created for the refinements that were not chosen.
    destroyedNodes = set()
    for candi in candidates:
        if candi is not None and candi is not theone and candi.internalNodes:
            for n in candi.internalNodes:
                if n not in destroyedNodes and (theone is not None and
                                            n not in theone.internalNodes):
                    n.destroy(skeleton)
                    destroyedNodes.add(n)
    
    return [] if theone is None else theone.accept(skeleton)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# ruleZero applies to both triangles and quads which don't need refining.

def ruleZero(element, rotation, edgenodes, newSkeleton, alpha):
    return (newSkeleton.newElement(nodes=list(baseNodes(element, rotation)),
                                   parents=[element]),)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

### 000 ### (Unrefined triangle)

RefinementRule(quickRules, (0,0,0), ruleZero)

### 100 ###

#          2
#         /|\
#        / | \
#       /  |  \
#      /   |   \
#     /    |    \
#    /     |     \
#   /______|______\
#   0      a      1
#

def rule100(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    return (newSkeleton.newElement(nodes=[na, n2, n0], parents=[element]),
            newSkeleton.newElement(nodes=[na, n1, n2], parents=[element]))

RefinementRule(quickRules, (1,0,0), rule100)

### 110 ###

#          2                   2                  2       
#         /|\                  /\                /\        
#        / | \                /  \              /  \       
#       /  |  \              /    \            /    \      
#      /   |   b            /    * b          /      b     
#     /    | /  \          /  *   / \        /      / \    
#    /     |/    \        /*     /   \      /      /   \   
#   /______/______\      /______/_____\    /______/_____\  
#   0      a      1     0      a      1    0      a      1
#

def rule110(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%3][0]
    refine0 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, n2], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, n2], parents=[element]),
         ProvisionalTriangle(nodes=[na, n1, nb], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, nb, n2], parents=[element]),
         ProvisionalTriangle(nodes=[n0, na, nb], parents=[element]),
         ProvisionalTriangle(nodes=[na, n1, nb], parents=[element])])
    refine2 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[na, n1, nb], parents=[element]),
         ProvisionalQuad(nodes=[n0, na, nb, n2], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1, refine2), alpha)

RefinementRule(largeRules, (1,1,0), rule110)

def rule110q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%3][0]
    return (newSkeleton.newElement(nodes=[n0, na, nb, n2], parents=[element]),
            newSkeleton.newElement(nodes=[na, n1, nb], parents=[element]))

RefinementRule(quickRules, (1,1,0), rule110q)

### 111 ###

#             2                             2
#             /\                           / \         
#            /  \                         /   \        
#           /    \                       /     \       
#          /      \                    c/       b     
#       c /________\b                  / \     / \     
#        /\        /\                 /   \   /   \   
#       /  \      /  \               /     \d/     \   
#      /    \    /    \             /       |       \  
#     /      \  /      \           /        |        \ 
#    /________\/________\         /_______ _|_________\
#    0        a          1        0        a           1
#
#              2                        2             
#             /|\                      / \           
#            / | \                    /   \          
#           /  |  \                  /     \         
#          /   |   \                /       \        
#       c /    |    \b           c /         \b      
#        /\    |    /\            /\         /\      
#       /  \   |   /  \          /  \       /  \     
#      /    \  |  /    \        /    \     /    \    
#     /      \ | /      \      /      \   /      \   
#    /________\|/________\    /________\ /________\  
#    0         a          1   0         a          1 

# Helper functions to generate the rotated versions of the diagrams in
# the second row.

def refine111_2(n0, na, n1, nb, n2, nc, element):
    return ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nc], parents=[element]),
         ProvisionalTriangle(nodes=[na, n2, nc], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, n2], parents=[element]),
         ProvisionalTriangle(nodes=[na, n1, nb], parents=[element])])

def refine111_3(n0, na, n1, nb, n2, nc, element):
    return ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nc], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, n2, nc], parents=[element]),
         ProvisionalTriangle(nodes=[na, n1, nb], parents=[element])])

def rule111(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%3][0]
    nc = edgenodes[(rotation+2)%3][0]
    nd = newSkeleton.newNodeFromPoint(element.center())
    refinements = (
        ProvisionalRefinement(
            [ProvisionalTriangle(nodes=[n0, na, nc], parents=[element]),
             ProvisionalTriangle(nodes=[na, n1, nb], parents=[element]),
             ProvisionalTriangle(nodes=[nc, nb, n2], parents=[element]),
             ProvisionalTriangle(nodes=[na, nb, nc], parents=[element])]),
        ProvisionalRefinement(
            [ProvisionalQuad(nodes=[n0, na, nd, nc], parents=[element]),
             ProvisionalQuad(nodes=[na, n1, nb, nd], parents=[element]),
             ProvisionalQuad(nodes=[nd, nb, n2, nc], parents=[element])],
            internalNodes = [nd]),
        
        refine111_2(n0, na, n1, nb, n2, nc, element),
        refine111_2(n1, nb, n2, nc, n0, na, element),
        refine111_2(n2, nc, n0, na, n1, nb, element),

        refine111_3(n0, na, n1, nb, n2, nc, element),
        refine111_3(n1, nb, n2, nc, n0, na, element),
        refine111_3(n2, nc, n0, na, n1, nb, element)
        )
    return theBetter(newSkeleton, refinements, alpha)

RefinementRule(largeRules, (1,1,1), rule111)

# The quick refinement for 111 is the symmetric 4 triangle refinement.
# The three quad refinement tends to produce shallow angles at the
# central point.

def rule111q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%3][0]
    nc = edgenodes[(rotation+2)%3][0]
    return (newSkeleton.newElement(nodes=[n0, na, nc], parents=[element]),
            newSkeleton.newElement(nodes=[na, n1, nb], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n2, nc], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc], parents=[element]))

RefinementRule(quickRules, (1,1,1), rule111q)

### 200 ###


#             2
#             /\                         2       
#            /  \                       /|\      
#           / ** \                     / | \     
#          /      \                   /  |  \    
#         /  *  *  \                 /  c|   \   
#        /          \               /   / \   \  
#       /   *    *   \             /   /   \   \ 
#      /              \           /___/_____\___\
#     /    *      *    \          0   a      b  1
#    /__________________\
#   0     a        b    1


def rule200(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = newSkeleton.newNodeFromPoint(element.center())
    refine0 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, n2], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, n2], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, n2], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nc, n2], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, nc], parents=[element]),
         ProvisionalQuad(nodes=[nb, n1, n2, nc], parents=[element])],
        internalNodes=[nc])
    return theBetter(newSkeleton, (refine0, refine1), alpha)

# The quick rule offers the same two choices.  The first one might
# produce sharp angles, but the second one can create illegal
# elements.

RefinementRule(quickRules, (2,0,0), rule200)

### 210 ###

#           2
#           /\
#          /  \
#         /    \c
#        /    /|\
#       /    / | \      
#      /    /  |  \ 
#     /    /   |   \
#    /____/____|____\
#   0    a     b     1

def rule210(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%3][0]
    return (
        newSkeleton.newElement(nodes=[n0, na, nc, n2], parents=[element]),
        newSkeleton.newElement(nodes=[na, nb, nc], parents=[element]),
        newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]))

RefinementRule(quickRules, (2,1,0), rule210)

### 201 ###

#           2
#           /\
#          /  \
#        c/    \ 
#        /|\    \
#       / | \    \      
#      /  |  \    \ 
#     /   |   \    \
#    /____|____\____\
#   0     a     b    1

def rule201(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+2)%3][0]
    return (
        newSkeleton.newElement(nodes=[n0, na, nc], parents=[element]),
        newSkeleton.newElement(nodes=[na, nb, nc], parents=[element]),
        newSkeleton.newElement(nodes=[nb, n1, n2, nc], parents=[element]))

RefinementRule(quickRules, (2,0,1), rule201)

### 211 ###

#            2                     2                     2             
#           / \                   / \                   / \            
#          /   \                 /   \                 /   \           
#        d/_____\c             d/     \c             d/     \c         
#        /|     |\             /|\    |\             /|    /|\         
#       / |     | \           / | \   | \           / |   / | \        
#      /  |     |  \         /  |  \  |  \         /  |  /  |  \       
#     /   |     |   \       /   |   \ |   \       /   | /   |   \      
#    /____|_____|____\     /____|____\|____\     /____|/____|____\     
#   0     a     b    1    0     a     b    1    0     a     b    1     

def rule211(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%3][0]
    nd = edgenodes[(rotation+2)%3][0]
    refine0 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nd], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nd, nc, n2], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nd], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, nd], parents=[element]),
         ProvisionalQuad(nodes=[nb, nc, n2, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element])])
    refine2 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nd], parents=[element]),
         ProvisionalQuad(nodes=[na, nc, n2, nd], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1, refine2), alpha)

RefinementRule(largeRules, (2,1,1), rule211)

def rule211q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%3][0]
    nd = edgenodes[(rotation+2)%3][0]
    return (newSkeleton.newElement(nodes=[n0, na, nd], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nd, nc, n2], parents=[element]))

RefinementRule(quickRules, (2,1,1), rule211q)

### 220 ###

#           2
#           /\
#          /  \
#         /    \d
#        /    / \
#       /    /   \c     
#      /    /    /\ 
#     /    /    /  \
#    /____/____/____\
#   0     a    b     1

def rule220(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%3][0]
    nd = edgenodes[(rotation+1)%3][1]
    return (newSkeleton.newElement(nodes=[n0, na, nd, n2], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]))

RefinementRule(quickRules, (2,2,0), rule220)

### 221 ###

#           2                     2                     2              
#           /\                    /\                    /\           
#          /  \                  /  \                  /  \          
#        e/____\d              e/____\d              e/    \d        
#        /|   / \              /    / \              /|   / \        
#       / |  /   \c           /    /   \c           / |  /   \c      
#      /  | /    /\          /    /    /\          /  | /    /\      
#     /   |/    /  \        /    /    /  \        /   |/    /  \     
#    /____/____/____\      /____/____/____\      /____/____/____\    
#   0     a    b     1    0     a    b     1    0     a    b     1    

def rule221(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%3][0]
    nd = edgenodes[(rotation+1)%3][1]
    ne = edgenodes[(rotation+2)%3][0]
    refine0 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, ne], parents=[element]),
         ProvisionalTriangle(nodes=[na, nd, ne], parents=[element]),
         ProvisionalTriangle(nodes=[ne, nd, n2], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nd, ne], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[ne, nd, n2], parents=[element])])
    refine2 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, ne], parents=[element]),
         ProvisionalQuad(nodes=[na, nd, n2, ne], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1, refine2), alpha)


RefinementRule(largeRules, (2,2,1), rule221)

def rule221q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%3][0]
    nd = edgenodes[(rotation+1)%3][1]
    ne = edgenodes[(rotation+2)%3][0]
    return (newSkeleton.newElement(nodes=[n0, na, ne], parents=[element]),
            newSkeleton.newElement(nodes=[na, nd, ne], parents=[element]),
            newSkeleton.newElement(nodes=[ne, nd, n2], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]))

RefinementRule(quickRules, (2,2,1), rule221q)

### 222 ###

#            2                      2         
#           /\                     /\         
#          /  \                   /  \        
#        e/____\d               e/    \d      
#        /\    /\               /\    /\      
#       /  \  /  \             /  \  /  \     
#     f/____\g____\c         f/____\g____\c   
#     /\    /\    /\         /     /\     \   
#    /  \  /  \  /  \       /     /  \     \  
#   /____\/____\/____\     /____ /____\ ____\ 
#  0      a     b     1   0      a     b     1
#
#            2                      2         
#           /\                     /\          
#          /  \                   /  \         
#        e/____\d               e/____\d       
#        /     /\               /      \     
#       /     /  \             /        \      
#     f/_____g    \c         f/__________\c    
#     /\     \    /\         /\          /\    
#    /  \     \  /  \       /  \        /  \   
#   /____\ ____\/____\     /____\ ____ /____\  
#  0      a     b     1   0      a     b     1 
#
# There are two orientations for the first diagram in the second row
# and three for the second.  It is possible to create other
# configurations by dividing some of the quadrilaterals into
# triangles.  I'm not sure how many configurations should be included.

def rule222(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%3][0]
    nd = edgenodes[(rotation+1)%3][1]
    ne = edgenodes[(rotation+2)%3][0]
    nf = edgenodes[(rotation+2)%3][1]
    ng = newSkeleton.newNodeFromPoint(element.center())
    refine0 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nf], parents=[element]),
         ProvisionalTriangle(nodes=[na, ng, nf], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, ng], parents=[element]),
         ProvisionalTriangle(nodes=[nb, nc, ng], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nf, ng, ne], parents=[element]),
         ProvisionalTriangle(nodes=[ng, nd, ne], parents=[element]),
         ProvisionalTriangle(nodes=[ng, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[ne, nd, n2], parents=[element])],
        internalNodes=[ng])
    refine1 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, ng, nf], parents=[element]),
         ProvisionalQuad(nodes=[n1, nc, ng, nb], parents=[element]),
         ProvisionalQuad(nodes=[n2, ne, ng, nd], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, ng], parents=[element]),
         ProvisionalTriangle(nodes=[nc, nd, ng], parents=[element]),
         ProvisionalTriangle(nodes=[ne, nf, ng], parents=[element])],
        internalNodes=[ng])
    refine2a = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[na, nb, ng, nf], parents=[element]),
         ProvisionalQuad(nodes=[nb, nc, nd, ng], parents=[element]),
         ProvisionalQuad(nodes=[ne, nf, ng, nd], parents=[element]),
         ProvisionalTriangle(nodes=[n0, na, nf], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[ne, nd, n2], parents=[element])],
        internalNodes=[ng])
    refine2b = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[na, nb, nc, ng], parents=[element]),
         ProvisionalQuad(nodes=[ng, nc, nd, ne], parents=[element]),
         ProvisionalQuad(nodes=[na, ng, ne, nf], parents=[element]),
         ProvisionalTriangle(nodes=[n0, na, nf], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[ne, nd, n2], parents=[element])],
        internalNodes=[ng])
    refine3a = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nf], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[ne, nd, n2], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nf], parents=[element]),
         ProvisionalQuad(nodes=[nf, nc, nd, ne], parents=[element])])
    refine3b = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nf], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[ne, nd, n2], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
         ProvisionalQuad(nodes=[na, nd, ne, nf], parents=[element])])
    refine3c = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nf], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[ne, nd, n2], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, ne, nf], parents=[element]),
         ProvisionalQuad(nodes=[nb, nc, nd, ne], parents=[element])])

    return theBetter(newSkeleton,
                     (refine0, refine1, refine2a, refine2b,
                      refine3a, refine3b, refine3c),
                     alpha)
    
RefinementRule(largeRules, (2,2,2), rule222)

def rule222q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%3][0]
    nd = edgenodes[(rotation+1)%3][1]
    ne = edgenodes[(rotation+2)%3][0]
    nf = edgenodes[(rotation+2)%3][1]
    ng = newSkeleton.newNodeFromPoint(element.center())
    return (newSkeleton.newElement(nodes=[n0, na, ng, nf], parents=[element]),
            newSkeleton.newElement(nodes=[n1, nc, ng, nb], parents=[element]),
            newSkeleton.newElement(nodes=[n2, ne, ng, nd], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, ng], parents=[element]),
            newSkeleton.newElement(nodes=[nc, nd, ng], parents=[element]),
            newSkeleton.newElement(nodes=[ne, nf, ng], parents=[element]))

RefinementRule(quickRules, (2,2,2), rule222q)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Quads

# Unrefined quadrilateral
    
RefinementRule(quickRules, (0,0,0,0), ruleZero)

# Quads with no trisected edges.

### 1000 ###

#  3-------------------2     3-------------------2   3-------------------2
#  |\                 /|     |\                  |   |                  /|
#  | \               / |     | \                 |   |                 / |
#  |  \             /  |     |  \                |   |                /  |
#  |   \           /   |     |   \               |   |               /   |
#  |    \         /    |     |    \              |   |              /    |
#  |     \       /     |     |     \             |   |             /     |
#  |      \     /      |     |      \            |   |            /      |
#  |       \   /       |     |       \           |   |           /       |
#  |        \ /        |     |        \          |   |          /        |
#  0---------a---------1     0---------a---------1   0---------a---------1


def rule1000(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    refine0 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, n3], parents=[element]),
         ProvisionalTriangle(nodes=[na, n2, n3], parents=[element]),
         ProvisionalTriangle(nodes=[na, n1, n2], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, n1, n2, n3], parents=[element])])
    refine2 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, n2, n3], parents=[element]),
         ProvisionalTriangle(nodes=[na, n1, n2], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1, refine2), alpha)
             
RefinementRule(largeRules, (1,0,0,0), rule1000)

def rule1000q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    return (newSkeleton.newElement(nodes=[n0, na, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, n2, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, n1, n2], parents=[element]))

RefinementRule(quickRules, (1,0,0,0), rule1000q)

### 1100 ###

#  3----------2   3----------2    3----------2    3----------2   
#  |\         |   |          |    |  *       |    |  *       |   
#  | \        |   | *        |    |     *    |    | *   *    |   
#  |  \       |   |          |b   |        * |b   |        * |b  
#  |   \      |   |  *      /|    |         /|    |  *      /|
#  |   c\_____|b  |        / |    |        / |    |        / |   
#  |    |     |   |   *   /  |    |       /  |    |   *   /  |   
#  |    |     |   |      /   |    |      /   |    |      /   |   
#  |    |     |   |    */    |    |     /    |    |    */    |   
#  0----a-----1   0----a-----1    0----a-----1    0----a-----1    


def rule1100(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%4][0]
    nc = newSkeleton.newNodeFromPoint(element.center())
    debug.fmsg(f"{n0=} {n1=} {n2=} {n3=}")
    debug.fmsg(f"{na=} {nb=} {nc=}")
    refine0 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nc, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, n1, nb, nc], parents=[element]),
         ProvisionalQuad(nodes=[nc, nb, n2, n3], parents=[element])],
        internalNodes=[nc])
    refine1 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, n2, n3], parents=[element]),
         ProvisionalTriangle(nodes=[na, n1, nb], parents=[element])])
    refine2 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nb, n3], parents=[element]),
         ProvisionalTriangle(nodes=[na, n1, nb], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n2, n3], parents=[element])])
    refine3 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, n3], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, n3], parents=[element]),
         ProvisionalTriangle(nodes=[na, n1, nb], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n2, n3], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1, refine2, refine3), alpha)
    
RefinementRule(largeRules, (1,1,0,0), rule1100)

def rule1100q(element, rotation, edgenodes, newSkeleton, alpha):
    # Don't use only refine0 from rule1100 because it can create
    # illegal elements.
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%4][0]
    nc = newSkeleton.newNodeFromPoint(element.center())
    refine0 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nc, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, n1, nb, nc], parents=[element]),
         ProvisionalQuad(nodes=[nc, nb, n2, n3], parents=[element])],
        internalNodes=[nc])
    refine3 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, n3], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, n3], parents=[element]),
         ProvisionalTriangle(nodes=[na, n1, nb], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n2, n3], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine3), alpha)

RefinementRule(quickRules, (1,1,0,0), rule1100q)

### 1010 ###

#  3-----b-----2
#  |     |     |
#  |     |     |
#  |     |     |
#  |     |     |
#  0-----a-----1

def rule1010(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+2)%4][0]
    return (
        newSkeleton.newElement(nodes=[n0, na, nb, n3], parents=[element]),
        newSkeleton.newElement(nodes=[na, n1, n2, nb], parents=[element]))

RefinementRule(quickRules, (1,0,1,0), rule1010)

### 1110 ###

#  3-----c--2   3-----c--2    3-----c--2    3-----c--2 
#  |    / \ |   |\     \ |    |     |\ |    |     |  | 
#  |   /   \|   | \     \|    |     | \|    |     |  | 
#  |  /     b   |  \     b    |     |  b    |     |  b 
#  | /     /|   |   \   /|    |     |  |    |     | /| 
#  |/     / |   |    \ / |    |     |  |    |     |/ | 
#  0-----a--1   0-----a--1    0-----a--1    0-----a--1 

def rule1110(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%4][0]
    nc = edgenodes[(rotation+2)%4][0]
    refine0 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nb, nc], parents=[element]),
         ProvisionalTriangle(nodes=[na, n1, nb], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n2, nc], parents=[element]),
         ProvisionalTriangle(nodes=[n0, nc, n3], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n3, na, nb, nc], parents=[element]),
         ProvisionalTriangle(nodes=[na, n1, nb], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n2, nc], parents=[element]),
         ProvisionalTriangle(nodes=[n0, na, n3], parents=[element])])
    refine2 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nc, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, n1, nb, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n2, nc], parents=[element])])
    refine3 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nc, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, n2, nc], parents=[element]),
         ProvisionalTriangle(nodes=[na, n1, nb], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1, refine2, refine3), alpha)

RefinementRule(largeRules, (1,1,1,0), rule1110)

def rule1110q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%4][0]
    nc = edgenodes[(rotation+2)%4][0]
    refine2 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nc, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, n1, nb, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n2, nc], parents=[element])])
    refine3 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nc, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, n2, nc], parents=[element]),
         ProvisionalTriangle(nodes=[na, n1, nb], parents=[element])])
    return theBetter(newSkeleton, (refine2, refine3), alpha)

RefinementRule(quickRules, (1,1,1,0), rule1110q)

### 1111 ###

#  3-----c-----2       3-----c-----2   
#  |     |     |       |    / \    |   
#  |     |     |       |   /   \   |   
#  |     |     |       |  /     \  |   
#  d_____e_____b       d /       \ b   
#  |     |     |       | \       / |   
#  |     |     |       |  \     /  |   
#  |     |     |       |   \   /   |   
#  |     |     |       |    \ /    |   
#  0-----a-----1       0-----a-----1   

def rule1111(element, rotation, edgenodes, newSkeleton, alpha):
    # rotation is not necessary here, but baseNodes expects it.
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%4][0]
    nc = edgenodes[(rotation+2)%4][0]
    nd = edgenodes[(rotation+3)%4][0]
    ne = newSkeleton.newNodeFromPoint(element.center())
    refine0 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, ne, nd], parents=[element]),
         ProvisionalQuad(nodes=[na, n1, nb, ne], parents=[element]),
         ProvisionalQuad(nodes=[ne, nb, n2, nc], parents=[element]),
         ProvisionalQuad(nodes=[nd, ne, nc, n3], parents=[element])],
        internalNodes=[ne])
    refine1 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nd], parents=[element]),
         ProvisionalTriangle(nodes=[na, n1, nb], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n2, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nd, nc, n3], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1), alpha)
    
RefinementRule(largeRules, (1,1,1,1), rule1111)

def rule1111q(element, rotation, edgenodes, newSkeleton, alpha):
    # rotation is not necessary here, but baseNodes expects it.
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%4][0]
    nc = edgenodes[(rotation+2)%4][0]
    nd = edgenodes[(rotation+3)%4][0]
    ne = newSkeleton.newNodeFromPoint(element.center())
    return (newSkeleton.newElement(nodes=[n0, na, ne, nd], parents=[element]),
            newSkeleton.newElement(nodes=[na, n1, nb, ne], parents=[element]),
            newSkeleton.newElement(nodes=[ne, nb, n2, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nd, ne, nc, n3], parents=[element]))

RefinementRule(quickRules, (1,1,1,1), rule1111q)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Quads with one trisected edge.

### 2000 ###

#  3-----------------------2     3-------------2
#  |\                     /|     |\           /|
#  | \                   / |     | \         / |
#  |  \                 /  |     |  \       /  |
#  |   \               /   |     |   \     /   |
#  |    \             /    |     |    d---c    |
#  |     \           /     |     |    |   |    |
#  |      \         /      |     |    |   |    |
#  |       \       /       |     |    |   |    |
#  |        \     /        |     |    |   |    |
#  0---------a---b---------1     0----a---b----1

def rule2000(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    # TODO PYTHON3: na and nb might be way off to one side, which
    # could make elements 0ad3 and b12c illegal if we're not careful
    # about the location of nodes c and d.  For instance, if na and nb
    # are close to node n0, b12c might be convex at nc.  Currently
    # theBetter() rejects illegal provisional elements.  Would it be
    # better to come up with legal positions for c and d instead?
    center = element.center()
    # midline is the vector from the center of side 03 to the center of side 12.
    midline = 0.5*(n1.position()+n2.position()-n0.position()-n3.position())
    nc = newSkeleton.newNodeFromPoint(center + midline/6.)
    nd = newSkeleton.newNodeFromPoint(center - midline/6.)
    refine0 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, n2, n3], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, n2], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nd, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
         ProvisionalQuad(nodes=[nb, n1, n2, nc], parents=[element]),
         ProvisionalQuad(nodes=[nd, nc, n2, n3], parents=[element])],
        internalNodes=[nc, nd])
    return theBetter(newSkeleton, (refine0, refine1), alpha)

RefinementRule(largeRules, (2,0,0,0), rule2000)

def rule2000q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    return (newSkeleton.newElement(nodes=[n0, na, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, n2, n3], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, n2], parents=[element]))

RefinementRule(quickRules, (2,0,0,0), rule2000q)


### 2001 ###

#  3-----------------------2      3-----------------------2
#  |                    * /|      |\                     /|
#  |                *    / |      | \                   / |
#  |            *       /  |      |  \                 /  |
#  |        *          /   |      |   \               /   |
#  |    *             /    |      |    \             /    |
#  c *               /     |      c     \           /     |
#  |   *            /      |      | *    \         /      |
#  |     *         /       |      |    *  \       /       |
#  |       *      /        |      |       *\     /        |
#  0---------a---b---------1      0---------a---b---------1
#
#   3--------------2       3----------2
#   |\             |       |         /| 
#   | \            |       |        / |
#   |  \           |       |       /  |
#   |   \          |       |      /   |
#   c    \         |       |     /    |
#   |\    \        |       c----d     |
#   | \    \       |       |    |\    |
#   |  \    \      |       |    | \   |
#   |   \    \     |       |    |  \  |
#   0----a----b----1       0----a---b-1


def rule2001(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+3)%4][0]
    nd = newSkeleton.newNodeFromPoint(element.center())
    refine0 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nc], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, n2, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, n2], parents=[element]),
         ProvisionalTriangle(nodes=[n2, n3, nc], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nc], parents=[element]),
         ProvisionalTriangle(nodes=[na, n3, nc], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, n2, n3], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, n2], parents=[element])])
    refine2 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nc], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, n3, nc], parents=[element]),
         ProvisionalQuad(nodes=[nb, n1, n2, n3], parents=[element])])
    refine3 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nd, nc], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, nd], parents=[element]),
         ProvisionalQuad(nodes=[nb, n1, n2, nd], parents=[element]),
         ProvisionalQuad(nodes=[nc, nd, n2, n3], parents=[element])],
        internalNodes=[nd])
    return theBetter(newSkeleton, (refine0, refine1, refine2, refine3), alpha)
         
RefinementRule(largeRules, (2,0,0,1), rule2001)

def rule2001q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+3)%4][0]
    return (newSkeleton.newElement(nodes=[n0, na, nc], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, n3, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, n2, n3], parents=[element]))

RefinementRule(quickRules, (2,0,0,1), rule2001q)

### 2010 ###

#  3----------c----------2
#  |         / \         |
#  |        /   \        |
#  |       /     \       |
#  |      /       \      |
#  |     /         \     |
#  0----a-----------b----1

def rule2010(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+2)%4][0]
    return (
        newSkeleton.newElement(nodes=[n0, na, nc, n3], parents=[element]),
        newSkeleton.newElement(nodes=[na, nb, nc], parents=[element]),
        newSkeleton.newElement(nodes=[nb, n1, n2, nc], parents=[element]))

RefinementRule(quickRules, (2,0,1,0), rule2010)

### 2011 ###

#  3---------c----------2   3---------c----------2  
#  |        **          |   |         *          |  
#  |      *             |   |                    |  
#  |    *     *         |   |          *         |  
#  |  *                 |   |                    |  
#  d*          *        |   d           *        |  
#  |\                   |   |\ *                 |  
#  | \          *       |   | \   *      *       |  
#  |  \                 |   |  \     *           |  
#  |   \         *      |   |   \       * *      |  
#  0----a---------b-----1   0----a---------b-----1  
#
#  3---------c----------2   3-----------c---------2   
#  |        / \         |   |        * / \        |   
#  d       /   \        |   |     *   /   \       |   
#  |\     /     \       |   |  *     /     \      |   
#  | \   /       \      |   d       /       \     |   
#  |  \ /         \     |   |      /         \    |   
#  0---a-----------b----1   0-----a-----------b---1

   
def rule2011(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+2)%4][0]
    nd = edgenodes[(rotation+3)%4][0]
    refine0 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nd], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
         ProvisionalQuad(nodes=[nb, n1, n2, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nc, n3, nd], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nd], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, nd], parents=[element]),
         ProvisionalQuad(nodes=[nb, nc, n3, nd], parents=[element]),
         ProvisionalQuad(nodes=[nb, n1, n2, nc], parents=[element])])
    refine2 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nd], parents=[element]),
         ProvisionalQuad(nodes=[na, nc, n3, nd], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, nc], parents=[element]),
         ProvisionalQuad(nodes=[nb, n1, n2, nc], parents=[element])])
    refine3 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[nd, nc, n3], parents=[element]),
         ProvisionalQuad(nodes=[n0, na, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, nc], parents=[element]),
         ProvisionalQuad(nodes=[nb, n1, n2, nc], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1, refine2, refine3), alpha)
    
RefinementRule(largeRules, (2,0,1,1), rule2011)

def rule2011q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+2)%4][0]
    nd = edgenodes[(rotation+3)%4][0]
    return (newSkeleton.newElement(nodes=[n0, na, nd], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, n2, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nc, n3, nd], parents=[element]))

RefinementRule(quickRules, (2,0,1,1), rule2011q)

### 2100 ###

# 2100 is the left-right reflection of 2001

# 3-----------------------2      3-----------------------2
# |\                     /|      |\ *                    | 
# | \                   / |      | \    *                | 
# |  \                 /  |      |  \       *            | 
# |   \               /   |      |   \          *        | 
# |    \             /    |      |    \             *    | 
# |     \           /     c      |     \               * c 
# |      \         /    * |      |      \            *   | 
# |       \       /  *    |      |       \         *     | 
# |        \     /*       |      |        \      *       | 
# 0---------a---b---------1      0---------a---b---------1 
# 
# 3----------2       3--------------2  
# |\         |       |             /|  
# | \        |       |            / |  
# |  \       |       |           /  |  
# |   \      |       |          /   |  
# |    \     |       |         /    c  
# |     d----c       |        /    /|  
# |    /|    |       |       /    / |  
# |   / |    |       |      /    /  |  
# |  /  |    |       |     /    /   |  
# 0-a---b----1       0----a----b----1  

def rule2100(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = newSkeleton.newNodeFromPoint(element.center())
    refine0 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nb, nc, n2], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, n2, n3], parents=[element]),
         ProvisionalTriangle(nodes=[n0, na, n3], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, n3], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nc, n2, n3], parents=[element])])
    refine2 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nd, n3], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, nd], parents=[element]),
         ProvisionalQuad(nodes=[nb, n1, nc, nd], parents=[element]),
         ProvisionalQuad(nodes=[nd, nc, n2, n3], parents=[element])],
        internalNodes=[nd])
    refine3 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, n2], parents=[element]),
         ProvisionalQuad(nodes=[n0, na, n2, n3], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1, refine2, refine3), alpha)
    
RefinementRule(largeRules, (2,1,0,0), rule2100)

def rule2100q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    return (newSkeleton.newElement(nodes=[n0, na, n2. n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, n2], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]))

RefinementRule(quickRules, (2,0,0,1), rule2001q)

### 2101 ###

#  3---------------2   3---------------2   3---------------2
#  |               |   |\              |   |              /|
#  |               |   | \             |   |             / |
#  |               |   |  \            |   |            /  |
#  d---------------c   d   \           c   d           /   c
#  |\             /|   |\   \         /|   |\         /   /|
#  | \           / |   | \   \       / |   | \       /   / |
#  |  \         /  |   |  \   \     /  |   |  \     /   /  |
#  |   \       /   |   |   \   \   /   |   |   \   /   /   |
#  |    \     /    |   |    \   \ /    |   |    \ /   /    |
#  0-----a---b-----1   0-----a---b-----1   0-----a---b-----1

def rule2101(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+3)%4][0]
    refine0 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nd], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalQuad(nodes=[nd, nc, n2, n3], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nd], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, n3, nd], parents=[element]),
         ProvisionalQuad(nodes=[nb, nc, n2, n3], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element])])
    refine2 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nd], parents=[element]),
         ProvisionalQuad(nodes=[na, n2, n3, nd], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, n2], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1, refine2), alpha)
    
RefinementRule(largeRules, (2,1,0,1), rule2101)

def rule2101q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+3)%4][0]
    return (newSkeleton.newElement(nodes=[n0, na, nd], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nd, nc, n2, n3], parents=[element]))

RefinementRule(quickRules, (2,1,0,1), rule2101q)

### 2110 ###

# 2110 is the left-right reflection of 2011

#   3----------d---------2   3----------d---------2 
#   |          *         |   |          **        | 
#   |                    |   |             *      | 
#   |         *          |   |         *     *    | 
#   |                    |   |                 *  | 
#   |        *           c   |        *          *c 
#   |                 * /|   |                   /| 
#   |       *      *   / |   |       *          / | 
#   |           *     /  |   |                 /  | 
#   |      * *       /   |   |      *         /   | 
#   0-----a---------b----1   0-----a---------b----1 
# 
#   3---------d-----------2   3----------d---------2 
#   |        / \ *        |   |         / \        | 
#   |       /   \   *     |   |        /   \       c 
#   |      /     \     *  |   |       /     \     /| 
#   |     /       \       c   |      /       \   / | 
#   |    /         \      |   |     /         \ /  | 
#   0---a-----------b-----1   0----a-----------b---1  

def rule2110(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+2)%4][0]
    refine0 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nd, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, nc, n2, nd], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nd, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nc, n2, nd], parents=[element])])
    refine2 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nd, n3], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, nd], parents=[element]),
         ProvisionalQuad(nodes=[nb, n1, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nc, n2, nd], parents=[element])])
    refine3 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nd, n3], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, nd], parents=[element]),
         ProvisionalQuad(nodes=[nb, nc, n2, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1, refine2, refine3), alpha)

RefinementRule(largeRules, (2,1,1,0), rule2110)

def rule2110q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+2)%4][0]
    return (newSkeleton.newElement(nodes=[n0, na, nd, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nc, n2, nd], parents=[element]))

RefinementRule(quickRules, (2,1,1,0), rule2110q)

### 2111 ###

#  3---------d--------2                            
#  |        **        |    3------------d-----------2
#  |      *    *      |    |           /\           |
#  |    *        *    |    |          /  \          |
#  |  *            *  |    |         /    \         |
#  e*----------------*c    e        /      \        c
#  |\                /|    |\      /        \      /|
#  | \              / |    | \    /          \    / |
#  |  \            /  |    |  \  /            \  /  |
#  |   \          /   |    |   \/              \/   |
#  0----a--------b----1    0----a---------------b---1
#
#  3---d--------------2   3--------------d---2 
#  |  / \             |   |             / \  | 
#  | /   \            |   |            /   \ | 
#  |/     \           |   |           /     \| 
#  e       \          c   e          /       c 
#  |\       \        /|   |\        /       /| 
#  | \       \      / |   | \      /       / | 
#  |  \       \    /  |   |  \    /       /  | 
#  |   \       \  /   |   |   \  /       /   | 
#  |    \       \/    |   |    \/       /    | 
#  0-----a-------b----1   0-----a-------b----1 

def rule2111(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+2)%4][0]
    ne = edgenodes[(rotation+3)%4][0]
    refine0 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, ne], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, ne], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nc, n2, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nd, n3, ne], parents=[element]),
         ProvisionalTriangle(nodes=[ne, nc, nd], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, ne], parents=[element]),
         ProvisionalQuad(nodes=[na, nd, n3, ne], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, nd], parents=[element]),
         ProvisionalQuad(nodes=[nb, nc, n2, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element])])
    refine2 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, ne], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nd, ne], parents=[element]),
         ProvisionalQuad(nodes=[nb, nc, n2, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[ne, nd, n3], parents=[element])])
    refine3 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, ne], parents=[element]),
         ProvisionalQuad(nodes=[na, nd, n3, ne], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nc, n2, nd], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1, refine2, refine3), alpha)
    
RefinementRule(largeRules, (2,1,1,1), rule2111)

def rule2111q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+2)%4][0]
    ne = edgenodes[(rotation+3)%4][0]
    return (newSkeleton.newElement(nodes=[n0, na, ne], parents=[element]),
            newSkeleton.newElement(nodes=[na, nd, n3, ne], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, nc, n2, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]))

RefinementRule(quickRules, (2,1,1,1), rule2111q)

### Quads with two trisected edges

### 2200 ###

#    3--------------2   3--------------2   3--------------2  
#    | *            |   | *            |   |              | 
#    |    *         |   |    *         |   |              | 
#    |*      *      |   |       *      |   |*             | 
#    |          *   |   |          *   |   |              | 
#    |             *d   |             *d   |              d 
#    | *           /|   |             /|   | *           /| 
#    |            / |   |            / |   |            / | 
#    |           /  |   |           /  |   |           /  | 
#    |  *       /   |   |          /   |   |  *       /   | 
#    |         /    c   |         /    c   |         /    c 
#    |        /    /|   |        /    /|   |        /    /| 
#    |   *   /    / |   |       /    / |   |   *   /    / | 
#    |      /    /  |   |      /    /  |   |      /    /  | 
#    |    */    /   |   |     /    /   |   |    */    /   | 
#    0----a----b----1   0----a----b----1   0----a----b----1 

def rule2200(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    refine0 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, n3], parents=[element]),
         ProvisionalTriangle(nodes=[na, nd, n3], parents=[element]),
         ProvisionalTriangle(nodes=[nd, n2, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nd, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nd, n2, n3], parents=[element])])
    refine2 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, nd, n2, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1, refine2), alpha)

RefinementRule(largeRules, (2,2,0,0), rule2200)

def rule2200q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    return (newSkeleton.newElement(nodes=[n0, na, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, nd, n3], parents=[element]),
            newSkeleton.newElement(nodes=[nd, n2, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]))

RefinementRule(quickRules, (2,2,0,0), rule2200q)

### 2020 ###

#  3---d---c---2
#  |   |   |   |
#  |   |   |   |
#  |   |   |   |
#  |   |   |   |
#  |   |   |   |
#  |   |   |   |
#  0---a---b---1

def rule2020(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+2)%4][0]
    nd = edgenodes[(rotation+2)%4][1]
    return (
        newSkeleton.newElement(nodes=[n0, na, nd, n3], parents=[element]),
        newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
        newSkeleton.newElement(nodes=[nb, n1, n2, nc], parents=[element]))

RefinementRule(quickRules, (2,0,2,0), rule2020)

### 2201 ###

#  3--------------2   3--------------2   3--------------2 
#  |              |   |              |   |              |
#  |              |   |              |   |              |
#  |              |   |              |   |              |
#  |              |   |              |   |              |
#  e--------------d   e--------------d   e--------------d
#  |             /|   |\*            |   | *            |
#  |            / |   |*\  *         |   |*   *         |
#  |           /  |   |  \    *      |   |       *      |
#  |          /   |   | * \      *   |   | *        *   |
#  |         /    c   |    \        *c   |             *c
#  |        /    /|   |  *  \        |   |  *          /|
#  |       /    / |   |      \       |   |            / |
#  |      /    /  |   |   *   \      |   |   *       /  |
#  |     /    /   |   |        \     |   |          /   |
#  0----a----b----1   0----a----b----1   0----a----b----1

def rule2201(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+3)%4][0]
    refine0 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nd, ne], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalQuad(nodes=[nd, n2, n3, ne], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, ne], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, ne], parents=[element]),
         ProvisionalQuad(nodes=[nb, n1, nc, ne], parents=[element]),
         ProvisionalTriangle(nodes=[nc, nd, ne], parents=[element]),
         ProvisionalQuad(nodes=[nd, n2, n3, ne], parents=[element])])
    refine2 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, ne], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, ne], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nc, nd, ne], parents=[element]),
         ProvisionalQuad(nodes=[nd, n2, n3, ne], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1, refine2), alpha)

RefinementRule(largeRules, (2,2,0,1), rule2201)

def rule2201q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+3)%4][0]
    return (newSkeleton.newElement(nodes=[n0, na, nd, ne], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nd, n2, n3, ne], parents=[element]))

RefinementRule(quickRules, (2,2,0,1), rule2201q)

### 2210 ###

#  3-----e------2   3-----e------2   3-----e------2    
#  |     |\     |   |     |\     |   |     |\     |   
#  |     | \    |   |     |*\    |   |     |*\    |   
#  |     |  \   |   |     |  \   |   |     |  \   |   
#  |     |   \  |   |     | * \  |   |     | + \  |   
#  |     |    \ |   |     |    \ |   |     |*   \ |   
#  |     |     \d   |     |  *  \|   |     |  +  \|   
#  |     |     /|   |     |      d   |     |      d   
#  |     |    / |   |     |   *  |   |     | * +  |   
#  |     |   /  c   |     |      |   |     |      |   
#  |     |  /  /|   |     |    * |   |     |     +|  Pretend that the *s and +s
#  |     | /  / |   |     |      c   |     |  *   c  form straight lines from
#  |     |/  /  |   |     |     /|   |     |      |  b and c to e.
#  0-----a--b---1   |     |    / |   |     |      |   
#                   |     |   /  |   |     |   *  |
#                   0-----a--b---1   0-----a----b-1

#
#  3-------------e--------------2
#  |            / \             |
#  |           /   \            |
#  |          /     \           d
#  |         /       \         /|
#  |        /         \       / |
#  |       /           \     /  c
#  |      /             \   / * |
#  |     /               \ /*   |
#  0----a-----------------b-----1
# 

def rule2210(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+2)%4][0]
    refine0 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, ne, n3], parents=[element]),
         ProvisionalTriangle(nodes=[na, nd, ne], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nd, n2, ne], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, ne, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, ne], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nc, nd, ne], parents=[element]),
         ProvisionalTriangle(nodes=[nd, n2, ne], parents=[element])])
    refine2 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, ne, n3], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, ne], parents=[element]),
         ProvisionalQuad(nodes=[nb, n1, nc, ne], parents=[element]),
         ProvisionalTriangle(nodes=[nc, nd, ne], parents=[element]),
         ProvisionalTriangle(nodes=[nd, n2, ne], parents=[element])])
    refine3 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, ne, n3], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, ne], parents=[element]),
         ProvisionalQuad(nodes=[nb, nd, n2, ne], parents=[element]),
         ProvisionalTriangle(nodes=[nb, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1, refine2, refine3), alpha)

RefinementRule(largeRules, (2,2,1,0), rule2210)

def rule2210q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+2)%4][0]
    return (newSkeleton.newElement(nodes=[n0, na, ne, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, nd, ne], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nd, n2, ne], parents=[element]))

RefinementRule(quickRules, (2,2,1,0), rule2210q)

### 2211 ###

#  3------e------2   3------e------2   3------e------2 
#  |     / \     |   |      |\     |   |     /|\     | 
#  |    /   \    |   |      | \    |   |    / | \    | 
#  |   /     \   |   |      |  \   |   |   /  |  \   | 
#  |  /       \  |   |      |   \  |   |  /   |   \  | 
#  | /         \ |   |      |    \ |   | /    |    \ | 
#  |/           \|   |      |     \|   |/     |     \| 
#  f             d   f      |      d   f      |      d 
#  |\           /|   |\     |     /|   |      |     /| 
#  | \         / |   | \    |    / |   |      |    / | 
#  |  \       /  c   |  \   |   /  c   |      |   /  c 
#  |   \     /  /|   |   \  |  /  /|   |      |  /  /| 
#  |    \   /  / |   |    \ | /  / |   |      | /  / | 
#  |     \ /  /  |   |     \|/  /  |   |      |/  /  | 
#  0------a--b---1   0------a--b---1   0------a--b---1 

#   3----- e-------2    3----- e-------2
#   |     /*\      |    |     / \      |
#   |    /   \     |    |    /   \     |
#   |   /     \    |    |   /     \    |
#   |  /    *  \   |    |  /       \   |
#   | /         \  |    | /         \  |
#   |/           \ |    |/           \ |
#   f        *    \|    f             \|
#   |\             d    |\  *          d
#   | \            |    | \     *      |
#   |  \      *    c    |  \        *  c
#   |   \         /|    |   \         /|
#   |    \     * / |    |    \       / |
#   0-----a-----b--1    0-----a-----b--1


def rule2211(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+2)%4][0]
    nf = edgenodes[(rotation+3)%4][0]
    refine0 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nf], parents=[element]),
         ProvisionalQuad(nodes=[na, nd, ne, nf], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nd, n2, ne], parents=[element]),
         ProvisionalTriangle(nodes=[ne, n3, nf], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nf], parents=[element]),
         ProvisionalQuad(nodes=[na, ne, n3, nf], parents=[element]),
         ProvisionalTriangle(nodes=[na, nd, ne], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nd, n2, ne], parents=[element])])
    refine2 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, ne, nf], parents=[element]),
         ProvisionalTriangle(nodes=[na, nd, ne], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nd, n2, ne], parents=[element]),
         ProvisionalTriangle(nodes=[ne, n3, nf], parents=[element])])
    refine3 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nf], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, ne, nf], parents=[element]),
         ProvisionalQuad(nodes=[nb, nc, nd, ne], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nd, n2, ne], parents=[element]),
         ProvisionalTriangle(nodes=[ne, n3, nf], parents=[element])])
    refine4 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nf], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nc, nf], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalQuad(nodes=[nc, nd, ne, nf], parents=[element]),
         ProvisionalTriangle(nodes=[nd, n2, ne], parents=[element]),
         ProvisionalTriangle(nodes=[ne, n3, nf], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1, refine2, refine3, refine4),
                     alpha)

RefinementRule(largeRules, (2,2,1,1), rule2211)

def rule2211q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+2)%4][0]
    nf = edgenodes[(rotation+3)%4][0]
    return (newSkeleton.newElement(nodes=[n0, na, nf], parents=[element]),
            newSkeleton.newElement(nodes=[na, nd, ne, nf], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nd, n2, ne], parents=[element]),
            newSkeleton.newElement(nodes=[ne, n3, nf], parents=[element]))

RefinementRule(quickRules, (2,2,1,1), rule2211q)

### Quads with three trisected edges

### 2220 ###

#  3----f----e----2     3----f----e----2     3----f----e----2
#  |    |    |\   |     |    |\   |    |     |\   |    |    |
#  |    |    | \  |     |    | \  |    |     | \  |    |    |
#  |    |    |  \ |     |    |  \ |    |     |  \ |    |    |
#  |    |    |   \|     |    |   \|    |     |   \|    |    |
#  |    |    |    d     |    |    g----d     |    i----g----d
#  |    |    |    |     |    |    |    |     |    |    |    |
#  |    |    |    c     |    |    h----c     |    j----h----c
#  |    |    |   /|     |    |   /|    |     |   /|    |    |
#  |    |    |  / |     |    |  / |    |     |  / |    |    |
#  |    |    | /  |     |    | /  |    |     | /  |    |    |
#  |    |    |/   |     |    |/   |    |     |/   |    |    |
#  0----a----b----1     0----a----b----1     0----a----b----1
#                      TODO: Are these two too complicated?
#                      Should they be implemented?

def rule2220(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+2)%4][0]
    nf = edgenodes[(rotation+2)%4][1]
    be = ne.position() - nb.position()
    ng = newSkeleton.newNodeFromPoint(nb.position() + 2/3*be)
    nh = newSkeleton.newNodeFromPoint(nb.position() + 1/3*be)
    af = nf.position() - na.position()
    ni = newSkeleton.newNodeFromPoint(na.position() + 2/3*af)
    nj = newSkeleton.newNodeFromPoint(na.position() + 1/3*af)
    refine0 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nf, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, ne, nf], parents=[element]),
         ProvisionalQuad(nodes=[nb, nc, nd, ne], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nd, n2, ne], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nf, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, nh, ng, nf], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, nh], parents=[element]),
         ProvisionalTriangle(nodes=[ng, ne, nf], parents=[element]),
         ProvisionalQuad(nodes=[nb, n1, nc, nh], parents=[element]),
         ProvisionalQuad(nodes=[nh, nc, nd, ng], parents=[element]),
         ProvisionalQuad(nodes=[ng, nd, n2, ne], parents=[element])],
        internalNodes=[ng, nh])
    refine2 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nj], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nh, nj], parents=[element]),
         ProvisionalQuad(nodes=[nb, n1, nc, nh], parents=[element]),
         ProvisionalQuad(nodes=[nh, nc, nd, ng], parents=[element]),
         ProvisionalQuad(nodes=[ng, nd, n2, ne], parents=[element]),
         ProvisionalQuad(nodes=[ni, ng, ne, nf], parents=[element]),
         ProvisionalTriangle(nodes=[ni, nf, n3], parents=[element]),
         ProvisionalQuad(nodes=[n0, nj, ni, n3], parents=[element]),
         ProvisionalQuad(nodes=[nj, nh, ng, ni], parents=[element])],
        internalNodes=[ng, nh, ni, nj])
        
    return theBetter(newSkeleton, (refine0, refine1, refine3), alpha)

RefinementRule(largeRules, (2,2,2,0), rule2220)

def rule2220q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+2)%4][0]
    nf = edgenodes[(rotation+2)%4][1]
    return (newSkeleton.newElement(nodes=[n0, na, nf, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, ne, nf], parents=[element]),
            newSkeleton.newElement(nodes=[nb, nc, nd, ne], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nd, n2, ne], parents=[element]))

RefinementRule(quickRules, (2,2,2,0), rule2220q)

### 2221 ###

#  3-----f----e----2     3-----f----e--2
#  |    /|    |\   |     |     |    |  |
#  |   / |    | \  |     |     |    |  |
#  |  /  |    |  \ |     |     |    |  d
#  | /   |    |   \|     |     |    | /|
#  |/    |    |    d     |     |    |/ |
#  g     |    |    |     g-----h----i  |
#  |\    |    |    c     |     |    |\ | 
#  | \   |    |   /|     |     |    | \|
#  |  \  |    |  / |     |     |    |  c
#  |   \ |    | /  |     |     |    |  |
#  |    \|    |/   |     |     |    |  |
#  0-----a----b----1     0-----a----b--1

def rule2221(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+2)%4][0]
    nf = edgenodes[(rotation+2)%4][1]
    ng = edgenodes[(rotation+3)%4][0]
    midpt = 0.5*(nc.position() + nd.position())
    nh = newSkeleton.newNodeFromPoint(2/3*ng.position() + 1/3*midpt)
    ni = newSkeleton.newNodeFromPoint(1/3*ng.position() + 2/3*midpt)
    refine0 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, ng], parents=[element]),
         ProvisionalTriangle(nodes=[na, nf, ng], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, ne, nf], parents=[element]),
         ProvisionalQuad(nodes=[nb, nc, nd, ne], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nd, n2, ne], parents=[element]),
         ProvisionalTriangle(nodes=[nf, n3, ng], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, nh, ng], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, ni, nh], parents=[element]),
         ProvisionalQuad(nodes=[nb, n1, nc, ni], parents=[element]),
         ProvisionalTriangle(nodes=[nc, nd, ni], parents=[element]),
         ProvisionalQuad(nodes=[nd, n2, ne, ni], parents=[element]),
         ProvisionalQuad(nodes=[ni, ne, nf, nh], parents=[element]),
         ProvisionalQuad(nodes=[nh, nf, n3, ng], parents=[element])],
        internalNodes=[nh, ni])
    return theBetter(newSkeleton, (refine0, refine1), alpha)

RefinementRule(largeRules, (2,2,2,1), rule2221)

def rule2221q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+2)%4][0]
    nf = edgenodes[(rotation+2)%4][1]
    ng = edgenodes[(rotation+3)%4][0]
    return (newSkeleton.newElement(nodes=[n0, na, ng], parents=[element]),
            newSkeleton.newElement(nodes=[na, nf, ng], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, ne, nf], parents=[element]),
            newSkeleton.newElement(nodes=[nb, nc, nd, ne], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nd, n2, ne], parents=[element]),
            newSkeleton.newElement(nodes=[nf, n3, ng], parents=[element]))

RefinementRule(quickRules, (2,2,2,1), rule2221q)

### 2120 ###

#  3----e----d-----2    3----e-----d-----2 
#  |    |    |\    |    |    |\    |     |
#  |    |    | \   |    |    | \   |     |
#  |    |    |  \  |    |    |  \  |     |
#  |    |    |   \ |    |    |   \ |     |
#  |    |    |    \|    |    |    \|     | 
#  |    |    |     c    |    |     f-----c 
#  |    |    |    /|    |    |    /|     |
#  |    |    |   / |    |    |   / |     |
#  |    |    |  /  |    |    |  /  |     |
#  |    |    | /   |    |    | /   |     | 
#  |    |    |/    |    |    |/    |     |
#  0----a----b-----1    0----a-----b-----1 

def rule2120(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+2)%4][0]
    ne = edgenodes[(rotation+2)%4][1]
    nf = newSkeleton.newNodeFromPoint(0.5*(nb.position() + nd.position()))
    refine0 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, ne, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nd, ne], parents=[element]),
         ProvisionalTriangle(nodes=[nb, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nc, n2, nd], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, ne, n3], parents=[element]),
         ProvisionalTriangle(nodes=[na, nf, ne], parents=[element]),
         ProvisionalTriangle(nodes=[na, nb, nf], parents=[element]),
         ProvisionalTriangle(nodes=[nf, nd, ne], parents=[element]),
         ProvisionalQuad(nodes=[nb, n1, nc, nf], parents=[element]),
         ProvisionalQuad(nodes=[nf, nc, n2, nd], parents=[element])],
        internalNodes=[nf])
    return theBetter(newSkeleton, (refine0, refine1), alpha)

RefinementRule(largeRules, (2,1,2,0), rule2120)

def rule2120q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+2)%4][0]
    ne = edgenodes[(rotation+2)%4][1]
    return (newSkeleton.newElement(nodes=[n0, na, ne, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nd, ne], parents=[element]),
            newSkeleton.newElement(nodes=[nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nc, n2, nd], parents=[element]))

RefinementRule(quickRules, (2,1,2,0), rule2120q)

### 2121 ###

#  3-----e----d-----2    3-----e-----d-----2 
#  |    /|    |\    |    |     |     |     |
#  |   / |    | \   |    |     |     |     |
#  |  /  |    |  \  |    |     |     |     |
#  | /   |    |   \ |    |     |     |     |
#  |/    |    |    \|    |     |     |     | 
#  f     |    |     c    f-----g-----h-----c 
#  |\    |    |    /|    |     |     |     |
#  | \   |    |   / |    |     |     |     |
#  |  \  |    |  /  |    |     |     |     |
#  |   \ |    | /   |    |     |     |     | 
#  |    \|    |/    |    |     |     |     |
#  0-----a----b-----1    0-----a-----b-----1 

def rule2121(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+2)%4][0]
    ne = edgenodes[(rotation+2)%4][1]
    nf = edgenodes[(rotation+3)%4][0]
    ng = newSkeleton.newNodeFromPoint(2/3*nf.position() + 1/3*nc.position())
    nh = newSkeleton.newNodeFromPoint(1/3*nf.position() + 2/3*nc.position())
    refine0 = ProvisionalRefinement(
        [ProvisionalTriangle(nodes=[n0, na, nf], parents=[element]),
         ProvisionalTriangle(nodes=[na, ne, nf], parents=[element]),
         ProvisionalTriangle(nodes=[nf, ne, n3], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nd, ne], parents=[element]),
         ProvisionalTriangle(nodes=[nb, nc, nd], parents=[element]),
         ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
         ProvisionalTriangle(nodes=[nc, n2, nd], parents=[element])])
    refine1 = ProvisionalRefinement(
        [ProvisionalQuad(nodes=[n0, na, ng, nf], parents=[element]),
         ProvisionalQuad(nodes=[na, nb, nh, ng], parents=[element]),
         ProvisionalQuad(nodes=[nb, n1, nc, nh], parents=[element]),
         ProvisionalQuad(nodes=[nh, nc, n2, nd], parents=[element]),
         ProvisionalQuad(nodes=[ng, nh, nd, ne], parents=[element]),
         ProvisionalQuad(nodes=[nf, ng, ne, n3], parents=[element])],
        internalNodes = (ng, nh))
    return theBetter(newSkeleton, (refine0, refine1), alpha)

RefinementRule(largeRules, (2,1,2,1), rule2121)

def rule2121q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+2)%4][0]
    ne = edgenodes[(rotation+2)%4][1]
    nf = edgenodes[(rotation+3)%4][0]
    return (newSkeleton.newElement(nodes=[n0, na, nf], parents=[element]),
            newSkeleton.newElement(nodes=[na, ne, nf], parents=[element]),
            newSkeleton.newElement(nodes=[nf, ne, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nd, ne], parents=[element]),
            newSkeleton.newElement(nodes=[nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nc, n2, nd], parents=[element]))

RefinementRule(quickRules, (2,1,2,1), rule2121q)

### 2222 ###

#  3----f----e----2    3----f----e----2    3----f----e----2
#  |   /|    |\   |    |   /      \   |    |    |    |    |
#  |  / |    | \  |    |  /        \  |    |    |    |    |
#  | /  |    |  \ |    | /          \ |    |    |    |    |
#  |/   |    |   \|    |/            \|    |    |    |    |
#  g    |    |    d    g--------------d    g----i----j----d
#  |    |    |    |    |              |    |    |    |    |   0, 1, and 2
#  h    |    |    c    h--------------c    h----k----l----c
#  |\   |    |   /|    |\            /|    |    |    |    |
#  | \  |    |  / |    | \          / |    |    |    |    |
#  |  \ |    | /  |    |  \        /  |    |    |    |    |
#  |   \|    |/   |    |   \      /   |    |    |    |    |
#  0----a----b----1    0----a----b----1    0----a----b----1
#
#  3----f----e---------2     3---------f----e----2 
#  |   /    /|         |     |         |\    \   | 
#  |  /    / |         d     g         | \    \  | 
#  | /    /  |        /|     |\        |  \    \ | 
#  |/    /   |       / |     | \       |   \    \| 
#  g    /    |      /  |     |  \      |    \    d 
#  |   /     |     /   |     |   \     |     \   |    3 and 3a
#  |  /      |    /    c     h    \    |      \  | 
#  | /       |   /    /|     |\    \   |       \ | 
#  |/        |  /    / |     | \    \  |        \| 
#  h         | /    /  |     |  \    \ |         c 
#  |         |/    /   |     |   \    \|         | 
#  0---------a----b----1     0----a----b---------1
#
#
#  3----f----e---------2     3---------f----e----2 
#  |   /    /          |     |          \    \   | 
#  |  /    /           |     |           \    \  | 
#  | /    /            |     |            \    \ | 
#  |/    /             |     |             \    \| 
#  g    /              |     |              \    d 
#  |   /               |     |               \   | 
#  |  /                |     |                \  | 
#  | /                 |     |                 \ | 
#  |/                  |     |                  \|   4 and 4a
#  h-------------------d     g-------------------c 
#  |                  /|     |\                  | 
#  |                 / |     | \                 | 
#  |                /  |     |  \                | 
#  |               /   |     |   \               | 
#  |              /    c     h    \              | 
#  |             /    /|     |\    \             | 
#  |            /    / |     | \    \            | 
#  |           /    /  |     |  \    \           | 
#  |          /    /   |     |   \    \          | 
#  0---------a----b----1     0----a----b---------1 

# Other configurations are possible by collapsing some or all of the
# sides of the central quad in refine2.



def rule2222(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+2)%4][0]
    nf = edgenodes[(rotation+2)%4][1]
    ng = edgenodes[(rotation+3)%4][0]
    nh = edgenodes[(rotation+3)%4][1]
    ni = newSkeleton.newNodeFromPoint(2/3*ng.position() + 1/3*nd.position())
    nj = newSkeleton.newNodeFromPoint(1/3*ng.position() + 2/3*nd.position())
    nk = newSkeleton.newNodeFromPoint(2/3*nh.position() + 1/3*nc.position())
    nl = newSkeleton.newNodeFromPoint(1/3*nh.position() + 2/3*nc.position())
    refinements = (
        ProvisionalRefinement(  # 0
            [ProvisionalTriangle(nodes=[n0, na, nh], parents=[element]),
             ProvisionalQuad(nodes=[na, nf, ng, nh], parents=[element]),
             ProvisionalTriangle(nodes=[ng, nf, n3], parents=[element]),
             ProvisionalQuad(nodes=[na, nb, ne, nf], parents=[element]),
             ProvisionalQuad(nodes=[nb, nc, nd, ne], parents=[element]),
             ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
             ProvisionalTriangle(nodes=[nd, n2, ne], parents=[element])]),
        ProvisionalRefinement(  # 1
            [ProvisionalTriangle(nodes=[n0, na, nh], parents=[element]),
             ProvisionalQuad(nodes=[na, nb, nc, nh], parents=[element]),
             ProvisionalTriangle(nodes=[ng, nf, n3], parents=[element]),
             ProvisionalQuad(nodes=[nh, nc, nd, ng], parents=[element]),
             ProvisionalQuad(nodes=[ng, nd, ne, nf], parents=[element]),
             ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
             ProvisionalTriangle(nodes=[nd, n2, ne], parents=[element])]),
        ProvisionalRefinement( # 2
            [ProvisionalQuad(nodes=[n0, na, nk, nh], parents=[element]),
             ProvisionalQuad(nodes=[na, nb, nl, nk], parents=[element]),
             ProvisionalQuad(nodes=[nb, n1, nc, nl], parents=[element]),
             ProvisionalQuad(nodes=[nh, nk, ni, ng], parents=[element]),
             ProvisionalQuad(nodes=[nk, nl, nj, ni], parents=[element]),
             ProvisionalQuad(nodes=[nl, nc, nd, nj], parents=[element]),
             ProvisionalQuad(nodes=[ng, ni, nf, n3], parents=[element]),
             ProvisionalQuad(nodes=[ni, nj, ne, nf], parents=[element]),
             ProvisionalQuad(nodes=[nj, nd, n2, ne], parents=[element])],
            internalNodes = (ni, nj, nk, nl)),
        ProvisionalRefinement(  # 3
            [ProvisionalTriangle(nodes=[ng, nf, n3], parents=[element]),
             ProvisionalQuad(nodes=[nh, ne, nf, ng], parents=[element]),
             ProvisionalQuad(nodes=[n0, na, ne, nh], parents=[element]),
             ProvisionalQuad(nodes=[na, nd, n2, ne], parents=[element]),
             ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
             ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element])]),
        ProvisionalRefinement( # 3a
            [ProvisionalTriangle(nodes=[n0, na, nh], parents=[element]),
             ProvisionalQuad(nodes=[na, nb, ng, nh], parents=[element]),
             ProvisionalQuad(nodes=[nb, nf, n3, ng], parents=[element]),
             ProvisionalQuad(nodes=[nb, n1, nc, nf], parents=[element]),
             ProvisionalQuad(nodes=[nc, nd, ne, nf], parents=[element]),
             ProvisionalTriangle(nodes=[nd, n2, ne], parents=[element])]),
        ProvisionalRefinement(  # 4
            [ProvisionalTriangle(nodes=[ng, nf, n3], parents=[element]),
             ProvisionalQuad(nodes=[nh, ne, nf, ng], parents=[element]),
             ProvisionalQuad(nodes=[nh, nd, n2, ne], parents=[element]),
             ProvisionalQuad(nodes=[n0, na, nd, nh], parents=[element]),
             ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
             ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element])]),
        ProvisionalRefinement(  # 4a
            [ProvisionalTriangle(nodes=[n0, na, nh], parents=[element]),
             ProvisionalQuad(nodes=[na, nb, ng, nh], parents=[element]),
             ProvisionalQuad(nodes=[nb, n1, nc, ng], parents=[element]),
             ProvisionalQuad(nodes=[ng, nc, nf, n3], parents=[element]),
             ProvisionalQuad(nodes=[nc, nd, ne, nf], parents=[element]),
             ProvisionalTriangle(nodes=[nd, n2, ne], parents=[element])])
    )
    return theBetter(newSkeleton, refinements, alpha)

RefinementRule(largeRules, (2,2,2,2), rule2222)

def rule2222q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+2)%4][0]
    nf = edgenodes[(rotation+2)%4][1]
    ng = edgenodes[(rotation+3)%4][0]
    nh = edgenodes[(rotation+3)%4][1]
    ni = newSkeleton.newNodeFromPoint(2/3*ng.position() + 1/3*nd.position())
    nj = newSkeleton.newNodeFromPoint(1/3*ng.position() + 2/3*nd.position())
    nk = newSkeleton.newNodeFromPoint(2/3*nh.position() + 1/3*nc.position())
    nl = newSkeleton.newNodeFromPoint(1/3*nh.position() + 2/3*nc.position())
    return (newSkeleton.newElement(nodes=[n0, na, nk, nh], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nl, nk], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc, nl], parents=[element]),
            newSkeleton.newElement(nodes=[nh, nk, ni, ng], parents=[element]),
            newSkeleton.newElement(nodes=[nk, nl, nj, ni], parents=[element]),
            newSkeleton.newElement(nodes=[nl, nc, nd, nj], parents=[element]),
            newSkeleton.newElement(nodes=[ng, ni, nf, n3], parents=[element]),
            newSkeleton.newElement(nodes=[ni, nj, ne, nf], parents=[element]),
            newSkeleton.newElement(nodes=[nj, nd, n2, ne], parents=[element]))

RefinementRule(quickRules, (2,2,2,2), rule2222q)
