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

from ooflib.engine.skeletonelement import getProvisionalElement

import itertools

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
    'Quick',
    maxMarks=2,
    help="A small set of refinement rules. "
    "Quick to apply but might give worse results."
)

largeRules = RefinementRuleSet(
    'Large',
    maxMarks=2,
    parent="Quick",
    help="All reasonable ways of subdividing elements."
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# The names of the refinement rule sets are stored in an Enum so that
# the UI can handle them correctly.  This must come after the
# RefinementRuleSet objects are created.  If any RefinementRuleSets
# are created later, update the Enum with Enum.addEnumName.

class RuleSet(enum.EnumClass(*[(r.name(), r.help())
                               for r in RefinementRuleSet.allRuleSets])):
    pass
utils.OOFdefine('RuleSet', RuleSet)

RuleSet.tip = "Refinement rule sets."
RuleSet.discussion = xmlmenudump.loadFile('DISCUSSIONS/engine/enum/ruleset.xml')

# This function is used to get the default value for the RuleSet
# parameter in the Refine menu item.  It will be the name of the first
# RefinementRuleSet created.

def defaultRuleSetEnum():
    return RuleSet(RefinementRuleSet.allRuleSets[0].name())

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Class for the rules in a RefinementRuleSet.

class RefinementRule:
    def __init__(self, ruleset, signature, function):
        self.function = function
        ruleset.addRule(self, signature)
    def apply(self, element, rotation, edgenodes, newSkeleton, alpha):
        return self.function(element, rotation, edgenodes, newSkeleton, alpha)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Utilities used by RefinementRule.function.

# This function is called with an old element and an integer
# 'rotation'.  It returns copies (children in the SkeletonSelectable
# sense) of the nodes of the old element, with the order shifted
# around by the rotation.  The new refined elements will be built from
# these base nodes.

def baseNodes(element, rotation):
    return map(lambda x: x.children[-1],
               element.nodes[rotation:] + element.nodes[0:rotation])

# When there's more than one way to subdivide an element, create a
# ProvisionalRefinement for each and pass them to theBetter(), which
# will pick the best one.

class QuadHandler(enum.EnumClass("NONE", "LEFT", "RIGHT")):
    pass

class ProvisionalRefinement:
    def __init__(self, newbies = [], internalNodes = []):
        self.newbies = newbies   # new elements
        self.internalNodes = internalNodes
        self.illegal = False
        if debug.debug():
            # This is a crude test that the refinement rule provides a
            # proper segmentation of the element.
            area = self.newbies[0].parents[0].area()
            asum = 0.
            for element in self.newbies:
                asum += element.area()
            err = abs(asum - area)
            if err >= 1.e-6*area:
                debug.fmsg(f"{area=} {asum=}")
                raise ooferror.PyErrPyProgrammingError("Area check failed!")
            
        # It is not an error if a ProvisionalRefinement contains
        # illegal elements, if the refinement rule provides another
        # ProvisionalRefinement that can be used instead.  But we do
        # need to check.
        for i, element in enumerate(newbies):
            if element.illegal():
                self.illegal = True
                break
    def energy(self, skeleton, alpha):
        # This does not use SkeletonElement.energyTotal, which woudl
        # be the unweighted average energy of the new elements.
        # Instead, this is a combination of the area-weighted
        # homogeneities and the unweighted shape energies.  This way
        # small badly shaped elements are still prevented, but large
        # homogeneous elements are preferred.  It shouldn't be
        # favorable to subdivide a homogeneous element.
        hsum = 0.0              # weighted sum of homogeneities
        ssum = 0.0              # sum of shape energies
        asum = 0.0              # sum of areas
        for element in self.newbies:
            area = element.area()
            asum += area
            hsum += area*element.homogeneity(skeleton.MS, False)
            ssum += element.energyShape()
        return alpha*(1. - hsum/asum) + (1.-alpha)*ssum/len(self.newbies)
    def accept(self, skeleton):
        return [element.accept(skeleton) for element in self.newbies]
    def __repr__(self):
        return "ProvisionalRefinement" + f"{tuple(self.newbies)}"

    def __hash__(self):
        ## TODO: If this is slow, consider storing the nodes in sorted
        ## order.  See getPositionHash.
        return hash(tuple(e.getPositionHash() for e in self.newbies))
    def __eq__(self, other):
        return hash(self) == hash(other)
    def __ne__(self, other):
        return hash(self) != hash(other)
    def __lt__(self, other):
        return hash(self) < hash(other)
    def __gt__(self, other):
        return hash(self) > hash(other)
    def __le__(self, other):
        return hash(self) <= hash(other)
    def __ge__(self, other):
        return hash(self) >= hash(other)

    def subdivideQuads(self):
        # Return a list of ProvisionalRefinements generated by
        # subdividing the quads in this refinement into two triangles.
        # Do this in all possible ways, dividing each quad along
        # either or neither diagonal.  The null refinement, which
        # divides no additional quads, is included.
        quads = []
        notquads = []
        for element in self.newbies:
            if element.nnodes() == 4:
                quads.append(element)
            else:
                notquads.append(element)
        if not quads:
            return [self]

        refinements = []
        # itertools.product returns the Cartesian product of
        # 'repeat' copies of the components of its first argument.
        # Looping over it gives all the ways of assigning 'NONE',
        # 'LEFT', and 'RIGHT' to each of the quads.
        for divs in itertools.product(QuadHandler.names, repeat=len(quads)):
            provisionals = notquads[:]
            for i, quad in enumerate(quads):
                if divs[i] == "NONE":
                    provisionals.append(quad)
                elif divs[i] == "LEFT":
                    provisionals.append(
                        getProvisionalElement(
                            [quad.nodes[0], quad.nodes[1], quad.nodes[2]],
                            parents=quad.parents))
                    provisionals.append(
                        getProvisionalElement(
                            [quad.nodes[0], quad.nodes[2], quad.nodes[3]],
                            parents=quad.parents))
                else:
                    provisionals.append(
                        getProvisionalElement(
                            [quad.nodes[0], quad.nodes[1], quad.nodes[3]],
                            parents=quad.parents))
                    provisionals.append(
                        getProvisionalElement(
                            [quad.nodes[1], quad.nodes[2], quad.nodes[3]],
                            parents=quad.parents))
            refinements.append(
                ProvisionalRefinement(provisionals,
                                      internalNodes=self.internalNodes))
        return refinements

# TODO PYTHON3: In both theVeryBest and theBetter, cache subelement
# energies, using the ProvisionalElement hash.  The same subelement
# may occur in multiple candidates.

def theVeryBest(skeleton, candidates, alpha):
    # Extend the list of candidates by subdividing the quads in the
    # given candidates.
    extended = []
    for candidate in candidates:
        extended.extend(candidate.subdivideQuads())
    # debug.fmsg("original=", candidates)
    # debug.fmsg("extended=", extended)

    # Loop over the extend set of ProvisionalRefinements, skipping
    # ones that have been seen already, and find the best one.
    seen = set()
    best_energy = 100000        # much larger than any possible energy
    best_refinement = None
    for candidate in extended:
        if candidate not in seen:
            seen.add(candidate)
            if not candidate.illegal:
                energy = candidate.energy(skeleton, alpha)
                if energy < best_energy:
                    best_energy = energy
                    best_refinement = candidate

    # Remove any internal nodes created by refinements that weren't
    # chosen.  The extra refinments added by splitting quads don't add
    # any new internal nodes, so we only have to loop over the
    # original candidate refinements.
    destroyedNodes = set()
    for candidate in candidates:
        if candidate is not best_refinement:
            for node in candidate.internalNodes:
                if (node not in destroyedNodes and
                    (best_refinement is None
                     or node not in best_refinement.internalNodes)):
                    node.destroy(skeleton)
                    destroyedNodes.add(node)
    return [] if best_refinement is None else best_refinement.accept(skeleton)
    

# theBetter is like theVeryBest, but it doesn't extend the list of
# candidate refinements by subdividing quads.
def theBetter(skeleton, candidates, alpha):
    energy_min = 100000.        # much larger than any possible energy
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
        if candi is not theone and candi.internalNodes:
            for n in candi.internalNodes:
                if n not in destroyedNodes and (theone is None or
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
    refine2 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[na, n1, nb], parents=[element]),
         getProvisionalElement(nodes=[n0, na, nb, n2], parents=[element])])
    return theVeryBest(newSkeleton, [refine2], alpha)

RefinementRule(largeRules, (1,1,0), rule110)

def rule110q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%3][0]
    return (newSkeleton.newElement(nodes=[n0, na, nb, n2], parents=[element]),
            newSkeleton.newElement(nodes=[na, n1, nb], parents=[element]))

RefinementRule(quickRules, (1,1,0), rule110q)

### 111 ###

#              2                         2            
#             / \                       / \           
#            /   \                     /   \          
#           /     \                   /     \         
#         c/       b                 /       \        
#         / \     / \             c /         \b      
#        /   \   /   \             /\         /\      
#       /     \ /     \           /  \       /  \     
#      /       d       \         /    \     /    \    
#     /        |        \       /      \   /      \   
#    /_________|_________\     /________\ /________\  
#    0         a          1    0         a          1 
#
# These will be generated automatically from the above by bisecting quads:
#
#              2                         2          
#             /|\                        /\         
#            / | \                      /  \        
#           /  |  \                    /    \       
#          /   |   \                  /      \      
#       c /    |    \b             c /________\b    
#        /\    |    /\              /\        /\    
#       /  \   |   /  \            /  \      /  \   
#      /    \  |  /    \          /    \    /    \  
#     /      \ | /      \        /      \  /      \ 
#    /________\|/________\      /________\/________\
#    0         a          1     0        a          1



# Helper function to generate the rotated versions of the second
# refinement in the first row.

def helper111(n0, na, n1, nb, n2, nc, element):
    return ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nc], parents=[element]),
         getProvisionalElement(nodes=[na, nb, n2, nc], parents=[element]),
         getProvisionalElement(nodes=[na, n1, nb], parents=[element])])

def rule111(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%3][0]
    nc = edgenodes[(rotation+2)%3][0]
    nd = newSkeleton.newNodeFromPoint(element.center())
    # Only the 3-quad refinement and the 1-quad 2-triangle refinement
    # need to be given explicitly.  The others will be generated from
    # them.
    refinements = (
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nd, nc], parents=[element]),
             getProvisionalElement(nodes=[na, n1, nb, nd], parents=[element]),
             getProvisionalElement(nodes=[nd, nb, n2, nc], parents=[element])],
            internalNodes = [nd]),
        helper111(n0, na, n1, nb, n2, nc, element),
        helper111(n1, nb, n2, nc, n0, na, element),
        helper111(n2, nc, n0, na, n1, nb, element)
    )
    return theVeryBest(newSkeleton, refinements, alpha)

RefinementRule(largeRules, (1,1,1), rule111)

# The quick refinement for 111 is the symmetric 4 triangle refinement.
# The three quad refinement tends to produce shallow angles at the
# central point.

def rule111q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%3][0]
    nc = edgenodes[(rotation+2)%3][0]
    # Since there's only one choice and it contains no quads, there's
    # no need to call theVeryBest.
    return (newSkeleton.newElement(nodes=[n0, na, nc], parents=[element]),
            newSkeleton.newElement(nodes=[na, n1, nb], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n2, nc], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc], parents=[element]))

RefinementRule(quickRules, (1,1,1), rule111q)

### 200 ###


#             2                          2           
#            / \                        /|\          
#           /   \                      / | \         
#          / * * \                    /  |  \        
#         /       \                  /   |   \       
#        /  *   *  \                /    c    \      
#       /           \              /    / \    \     
#      /   *     *   \            /    /   \    \    
#     /               \          /    /     \    \   
#    /    *       *    \        /    /       \    \  
#   /                   \      /    /         \    \ 
#  0-----a---------b-----1    0----a-----------b----1

def rule200(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = newSkeleton.newNodeFromPoint(element.center())
    refine0 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, n2], parents=[element]),
         getProvisionalElement(nodes=[na, nb, n2], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, n2], parents=[element])])
    refine1 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nc, n2], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, n2, nc], parents=[element])],
        internalNodes=[nc])
    return theVeryBest(newSkeleton, (refine0, refine1), alpha)

# The quick rule offers the same two choices.  The first one might
# produce sharp angles, but the second one might create illegal
# elements, so both are required.

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
    refine = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nc, n2], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element])])
    return theVeryBest(newSkeleton, (refine,), alpha)

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
    refine = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nc], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, n2, nc], parents=[element])])
    return theVeryBest(newSkeleton, (refine,), alpha)

RefinementRule(largeRules, (2,0,1), rule201)

def rule201q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+2)%3][0]
    return (newSkeleton.newElement(nodes=[n0, na, nc], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, n2, nc], parents=[element]))

RefinementRule(quickRules, (2,0,1), rule201q)

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
        [getProvisionalElement(nodes=[n0, na, nd], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
         getProvisionalElement(nodes=[nd, nc, n2], parents=[element])])
    refine1 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nd], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, nc, n2, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element])])
    refine2 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nd], parents=[element]),
         getProvisionalElement(nodes=[na, nc, n2, nd], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element])])
    return theVeryBest(newSkeleton, (refine0, refine1, refine2), alpha)

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
    refine = ProvisionalRefinement([
        getProvisionalElement(nodes=[n0, na, nd, n2], parents=[element]),
        getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
        getProvisionalElement(nodes=[nb, n1, nc], parents=[element])])
    return theVeryBest(newSkeleton, (refine,), alpha)

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
    refine1 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nd, ne], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
         getProvisionalElement(nodes=[ne, nd, n2], parents=[element])])
    refine2 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, ne], parents=[element]),
         getProvisionalElement(nodes=[na, nd, n2, ne], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element])])
    return theVeryBest(newSkeleton, (refine1, refine2), alpha)


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
#        e/____\d               e/    \d       The first refinement in 
#        /\    /\               /\    /\       this row will be generated
#       /  \  /  \             /  \  /  \      automatially from the others.
#     f/____\g____\c         f/____\g____\c   
#     /\    /\    /\         /     /\     \   
#    /  \  /  \  /  \       /     /  \     \  
#   /____\/____\/____\     /_____/____\_____\ 
#  0      a     b     1   0      a     b     1
#
#            2                      2         
#           /\                     /\          
#          /  \                   /  \         There are two orientations
#        e/____\d               e/____\d       for the first diagram in this
#        /     /\               /      \       row, and three for the second.
#       /     /  \             /        \      
#     f/_____g    \c         f/__________\c    
#     /\     \    /\         /\          /\    
#    /  \     \  /  \       /  \        /  \   
#   /____\_____\/____\     /____\______/____\  
#  0      a     b     1   0      a     b     1 
#

def rule222(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%3][0]
    nd = edgenodes[(rotation+1)%3][1]
    ne = edgenodes[(rotation+2)%3][0]
    nf = edgenodes[(rotation+2)%3][1]
    ng = newSkeleton.newNodeFromPoint(element.center())
    refinements = (
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, ng, nf], parents=[element]),
             getProvisionalElement(nodes=[n1, nc, ng, nb], parents=[element]),
             getProvisionalElement(nodes=[n2, ne, ng, nd], parents=[element]),
             getProvisionalElement(nodes=[na, nb, ng], parents=[element]),
             getProvisionalElement(nodes=[nc, nd, ng], parents=[element]),
             getProvisionalElement(nodes=[ne, nf, ng], parents=[element])],
            internalNodes=[ng]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[na, nb, ng, nf], parents=[element]),
             getProvisionalElement(nodes=[nb, nc, nd, ng], parents=[element]),
             getProvisionalElement(nodes=[ne, nf, ng, nd], parents=[element]),
             getProvisionalElement(nodes=[n0, na, nf], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[ne, nd, n2], parents=[element])],
            internalNodes=[ng]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[na, nb, nc, ng], parents=[element]),
             getProvisionalElement(nodes=[ng, nc, nd, ne], parents=[element]),
             getProvisionalElement(nodes=[na, ng, ne, nf], parents=[element]),
             getProvisionalElement(nodes=[n0, na, nf], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[ne, nd, n2], parents=[element])],
            internalNodes=[ng]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nf], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[ne, nd, n2], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, nf], parents=[element]),
             getProvisionalElement(nodes=[nf, nc, nd, ne], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nf], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[ne, nd, n2], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
             getProvisionalElement(nodes=[na, nd, ne, nf], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nf], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[ne, nd, n2], parents=[element]),
             getProvisionalElement(nodes=[na, nb, ne, nf], parents=[element]),
             getProvisionalElement(nodes=[nb, nc, nd, ne], parents=[element])])
        )

    return theVeryBest(newSkeleton, refinements, alpha)
    
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
    refinement = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, ng, nf], parents=[element]),
         getProvisionalElement(nodes=[n1, nc, ng, nb], parents=[element]),
         getProvisionalElement(nodes=[n2, ne, ng, nd], parents=[element]),
         getProvisionalElement(nodes=[na, nb, ng], parents=[element]),
         getProvisionalElement(nodes=[nc, nd, ng], parents=[element]),
         getProvisionalElement(nodes=[ne, nf, ng], parents=[element])],
        internalNodes=[ng])
    return theVeryBest(newSkeleton, (refinement,), alpha)

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
    refine1 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, n3], parents=[element]),
         getProvisionalElement(nodes=[na, n1, n2, n3], parents=[element])])
    refine2 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, n2, n3], parents=[element]),
         getProvisionalElement(nodes=[na, n1, n2], parents=[element])])
    return theVeryBest(newSkeleton, (refine1, refine2), alpha)
             
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
    refine0 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nc, n3], parents=[element]),
         getProvisionalElement(nodes=[na, n1, nb, nc], parents=[element]),
         getProvisionalElement(nodes=[nc, nb, n2, n3], parents=[element])],
        internalNodes=[nc])
    refine1 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, n3], parents=[element]),
         getProvisionalElement(nodes=[na, nb, n2, n3], parents=[element]),
         getProvisionalElement(nodes=[na, n1, nb], parents=[element])])
    refine2 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nb, n3], parents=[element]),
         getProvisionalElement(nodes=[na, n1, nb], parents=[element]),
         getProvisionalElement(nodes=[nb, n2, n3], parents=[element])])
    return theVeryBest(newSkeleton, (refine0, refine1, refine2), alpha)
    
RefinementRule(largeRules, (1,1,0,0), rule1100)

def rule1100q(element, rotation, edgenodes, newSkeleton, alpha):
    # Don't just use refine0 from rule1100 because it can create
    # illegal elements if the original element is highly skewed.
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%4][0]
    nc = newSkeleton.newNodeFromPoint(element.center())
    refine0 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nc, n3], parents=[element]),
         getProvisionalElement(nodes=[na, n1, nb, nc], parents=[element]),
         getProvisionalElement(nodes=[nc, nb, n2, n3], parents=[element])],
        internalNodes=[nc])
    refine3 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, n3], parents=[element]),
         getProvisionalElement(nodes=[na, nb, n3], parents=[element]),
         getProvisionalElement(nodes=[na, n1, nb], parents=[element]),
         getProvisionalElement(nodes=[nb, n2, n3], parents=[element])])
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
    refine = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nb, n3], parents=[element]),
         getProvisionalElement(nodes=[na, n1, n2, nb], parents=[element])])
    return theVeryBest(newSkeleton, (refine,), alpha)

RefinementRule(quickRules, (1,0,1,0), rule1010)

### 1110 ###

#  3-----c--2    3-----c--2    
#  |    / \ |    |\     \ |    
#  |   /   \|    | \     \|    
#  |  /     b    |  \     b    
#  | /     /|    |   \   /|    
#  |/     / |    |    \ / |    
#  0-----a--1    0-----a--1   
#
#  3-----c--2    3-----c--2 
#  |     |\ |    |     |  |
#  |     | \|    |     |  |   These two are in the quick rule
#  |     |  b    |     |  b
#  |     |  |    |     | /|
#  |     |  |    |     |/ |
#  0-----a--1    0-----a--1
#
#  3---c----2 
#  |\  |    | 
#  | \ |    | 
#  |  \|    |
#  |   d----b 
#  |  /|    |
#  | / |    | 
#  |/  |    | 
#  0---a----1 

def rule1110(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%4][0]
    nc = edgenodes[(rotation+2)%4][0]
    nd = newSkeleton.newNodeFromPoint(element.center())
    refinements = (
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nb, nc], parents=[element]),
             getProvisionalElement(nodes=[na, n1, nb], parents=[element]),
             getProvisionalElement(nodes=[nb, n2, nc], parents=[element]),
             getProvisionalElement(nodes=[n0, nc, n3], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n3, na, nb, nc], parents=[element]),
             getProvisionalElement(nodes=[na, n1, nb], parents=[element]),
             getProvisionalElement(nodes=[nb, n2, nc], parents=[element]),
             getProvisionalElement(nodes=[n0, na, n3], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nc, n3], parents=[element]),
             getProvisionalElement(nodes=[na, n1, nb, nc], parents=[element]),
             getProvisionalElement(nodes=[nb, n2, nc], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nc, n3], parents=[element]),
             getProvisionalElement(nodes=[na, nb, n2, nc], parents=[element]),
             getProvisionalElement(nodes=[na, n1, nb], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nd], parents=[element]),
             getProvisionalElement(nodes=[na, n1, nb, nd], parents=[element]),
             getProvisionalElement(nodes=[nd, nb, n2, nc], parents=[element]),
             getProvisionalElement(nodes=[nd, nc, n3], parents=[element]),
             getProvisionalElement(nodes=[n0, nd, n3], parents=[element])],
            internalNodes=[nd])
        )
    return theVeryBest(newSkeleton, refinements, alpha)

RefinementRule(largeRules, (1,1,1,0), rule1110)

def rule1110q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%4][0]
    nc = edgenodes[(rotation+2)%4][0]
    refinements = (
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nc, n3], parents=[element]),
             getProvisionalElement(nodes=[na, n1, nb, nc], parents=[element]),
             getProvisionalElement(nodes=[nb, n2, nc], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nc, n3], parents=[element]),
             getProvisionalElement(nodes=[na, nb, n2, nc], parents=[element]),
             getProvisionalElement(nodes=[na, n1, nb], parents=[element])])
        )
    return theVeryBest(newSkeleton, refinements, alpha)

RefinementRule(quickRules, (1,1,1,0), rule1110q)

### 1111 ###

#  3-----c-----2    3-----c-----2    3-------c---2   3---c-------2 
#  |     |     |    |    / \    |    |        \  |   |  /        |
#  |     |     |    |   /   \   |    |         \ |   | /         |
#  |     |     |    |  /     \  |    |          \|   |/          |
#  d-----e-----b    d /       \ b    d---------- b   d---------- b
#  |     |     |    | \       / |    |\          |   |          /|
#  |     |     |    |  \     /  |    | \         |   |         / |
#  |     |     |    |   \   /   |    |  \        |   |        /  |
#  |     |     |    |    \ /    |    |   \       |   |       /   |
#  0-----a-----1    0-----a-----1    0----a------1   0------a----1

def rule1111(element, rotation, edgenodes, newSkeleton, alpha):
    # rotation is not necessary here, but baseNodes expects it.
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%4][0]
    nc = edgenodes[(rotation+2)%4][0]
    nd = edgenodes[(rotation+3)%4][0]
    ne = newSkeleton.newNodeFromPoint(element.center())
    refinements = (
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, ne, nd], parents=[element]),
             getProvisionalElement(nodes=[na, n1, nb, ne], parents=[element]),
             getProvisionalElement(nodes=[ne, nb, n2, nc], parents=[element]),
             getProvisionalElement(nodes=[nd, ne, nc, n3], parents=[element])],
            internalNodes=[ne]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nd], parents=[element]),
             getProvisionalElement(nodes=[na, n1, nb], parents=[element]),
             getProvisionalElement(nodes=[nb, n2, nc], parents=[element]),
             getProvisionalElement(nodes=[nd, nc, n3], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nd], parents=[element]),
             getProvisionalElement(nodes=[na, n1, nb, nd], parents=[element]),
             getProvisionalElement(nodes=[nd, nb, nc, n3], parents=[element]),
             getProvisionalElement(nodes=[nb, n2, nc], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nb, nd], parents=[element]),
             getProvisionalElement(nodes=[na, n1, nb], parents=[element]),
             getProvisionalElement(nodes=[nd, nc, n3], parents=[element]),
             getProvisionalElement(nodes=[nd, nb, n2, nc], parents=[element])])
        )
    return theVeryBest(newSkeleton, refinements, alpha)
    
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
    # TODO? na and nb might be way off to one side, which could make
    # elements 0ad3 and b12c illegal if we're not careful about the
    # location of nodes c and d.  For instance, if na and nb are close
    # to node n0, b12c might be convex at nc.  Currently theVeryBest()
    # rejects illegal provisional elements.  Would it be better to
    # come up with legal positions for c and d instead?
    center = element.center()
    # midline is the vector from the center of side 30 to the center of side 12.
    midline = 0.5*(n1.position()+n2.position()-n0.position()-n3.position())
    nc = newSkeleton.newNodeFromPoint(center + midline/6.)
    nd = newSkeleton.newNodeFromPoint(center - midline/6.)
    refine0 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, n3], parents=[element]),
         getProvisionalElement(nodes=[na, nb, n2, n3], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, n2], parents=[element])])
    refine1 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nd, n3], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, n2, nc], parents=[element]),
         getProvisionalElement(nodes=[nd, nc, n2, n3], parents=[element])],
        internalNodes=[nc, nd])
    return theVeryBest(newSkeleton, (refine0, refine1), alpha)

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

# 2001 is the left-right reflection of 2100

#  3-----------------------2      3-----------------------2 
#  |                    * /|      |\                     /|
#  |                *    / |      | \                   / |
#  |            *       /  |      |  \                 /  |
#  |        *          /   |      |   \               /   |
#  |    *             /    |      |    \             /    |
#  c *               /     |      c     \           /     |
#  |   *            /      |      | *    \         /      |
#  |     *         /       |      |    *  \       /       |
#  |       *      /        |      |      * \     /        |
#  0---------a---b---------1      0---------a---b---------1
#                                
#  3--------------2       3----------2
#  |\             |       |         /| 
#  | \            |       |        / |
#  |  \           |       |       /  |
#  |   \          |       |      /   |
#  c    \         |       |     /    |
#  |\    \        |       c----d     |
#  | \    \       |       |    |\    |
#  |  \    \      |       |    | \   |
#  |   \    \     |       |    |  \  |
#  0----a----b----1       0----a---b-1
#
#  3---------------------2   
#  |                    /|   
#  |                   / |   
#  |                  /  |   3---------------------2
#  |                 /   |   |                  * /|
#  |                /    |   |                *  / |
#  c               /     |   c              *   /  |
#  |\*            /      |   |\           *    /   |
#  | \ *         /       |   | \        *     /    |
#  |  \  *      /        |   |  \     *      /     |
#  |   \   *   /         |   |   \  *       /      |
#  0----a-----b----------1   0----a--------b-------1


def rule2001(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+3)%4][0]
    nd = newSkeleton.newNodeFromPoint(element.center())
    refinements = (
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nc], parents=[element]),
             getProvisionalElement(nodes=[na, nb, n2, nc], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, n2], parents=[element]),
             getProvisionalElement(nodes=[n2, n3, nc], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nc], parents=[element]),
             getProvisionalElement(nodes=[na, n3, nc], parents=[element]),
             getProvisionalElement(nodes=[na, nb, n2, n3], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, n2], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nc], parents=[element]),
             getProvisionalElement(nodes=[na, nb, n3, nc], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, n2, n3], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nd, nc], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nd], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, n2, nd], parents=[element]),
             getProvisionalElement(nodes=[nc, nd, n2, n3], parents=[element])],
            internalNodes=[nd]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nc], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc], parents=[element]),
             getProvisionalElement(nodes=[nb, n2, n3, nc], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, n2], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nc], parents=[element]),
             getProvisionalElement(nodes=[na, n2, n3, nc], parents=[element]),
             getProvisionalElement(nodes=[na, nb, n2], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, n2], parents=[element])])
        )
    return theVeryBest(newSkeleton, refinements, alpha)
         
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
    refinement = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nc, n3], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, n2, nc], parents=[element])])
    return theVeryBest(newSkeleton, (refinement,), alpha)

RefinementRule(largeRules, (2,0,1,0), rule2010)

def rule2010q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+2)%4][0]
    return (
        newSkeleton.newElement(nodes=[n0, na, nc, n3], parents=[element]),
        newSkeleton.newElement(nodes=[na, nb, nc], parents=[element]),
        newSkeleton.newElement(nodes=[nb, n1, n2, nc], parents=[element]))

RefinementRule(quickRules, (2,0,1,0), rule2010q)

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
        [getProvisionalElement(nodes=[n0, na, nd], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, n2, nc], parents=[element]),
         getProvisionalElement(nodes=[nc, n3, nd], parents=[element])])
    refine1 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nd], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, nc, n3, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, n2, nc], parents=[element])])
    refine2 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nd], parents=[element]),
         getProvisionalElement(nodes=[na, nc, n3, nd], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, n2, nc], parents=[element])])
    refine3 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[nd, nc, n3], parents=[element]),
         getProvisionalElement(nodes=[n0, na, nc, nd], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, n2, nc], parents=[element])])
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

#   3-----------------------2      3----------------------2
#   |\                     /|      |\ *                   | 
#   | \                   / |      | \    *               | 
#   |  \                 /  |      |  \       *           | 
#   |   \               /   |      |   \          *       | 
#   |    \             /    |      |    \             *   | 
#   |     \           /     c      |     \               *c 
#   |      \         /    * |      |      \            *  | 
#   |       \       /  *    |      |       \         *    | 
#   |        \     /*       |      |        \      *      | 
#   0---------a---b---------1      0---------a---b--------1 
# 
#   3----------2       3--------------2  
#   |\         |       |             /|  
#   | \        |       |            / |  
#   |  \       |       |           /  |  
#   |   \      |       |          /   |  
#   |    \     |       |         /    c  
#   |     d----c       |        /    /|  
#   |    /|    |       |       /    / |  
#   |   / |    |       |      /    /  |  
#   |  /  |    |       |     /    /   |  
#   0-a---b----1       0----a----b----1
#
#   3---------------------2
#   |\                    |
#   | \                   |
#   |  \                  |   3---------------------2
#   |   \                 |   |\ *                  | 
#   |    \                |   | \  *                |
#   |     \               c   |  \   *              c
#   |      \            */|   |   \    *           /|
#   |       \         * / |   |    \     *        / |
#   |        \      *  /  |   |     \      *     /  |
#   |         \   *   /   |   |      \       *  /   |
#   0----------a-----b----1   0-------a--------b----1


def rule2100(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = newSkeleton.newNodeFromPoint(element.center())
    refinements = (
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[nb, nc, n2], parents=[element]),
             getProvisionalElement(nodes=[na, nb, n2, n3], parents=[element]),
             getProvisionalElement(nodes=[n0, na, n3], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, n3], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, n3], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[nc, n2, n3], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nd, n3], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nd], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc, nd], parents=[element]),
             getProvisionalElement(nodes=[nd, nc, n2, n3], parents=[element])],
            internalNodes=[nd]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, n2], parents=[element]),
             getProvisionalElement(nodes=[n0, na, n2, n3], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, n3], parents=[element]),
             getProvisionalElement(nodes=[na, nc, n2, n3], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, n3], parents=[element]),
             getProvisionalElement(nodes=[na, nb, n3], parents=[element]),
             getProvisionalElement(nodes=[nb, nc, n2, n3], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element])])
        )
    return theBetter(newSkeleton, refinements, alpha)
    
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
        [getProvisionalElement(nodes=[n0, na, nd], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
         getProvisionalElement(nodes=[nd, nc, n2, n3], parents=[element])])
    refine1 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nd], parents=[element]),
         getProvisionalElement(nodes=[na, nb, n3, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, nc, n2, n3], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element])])
    refine2 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nd], parents=[element]),
         getProvisionalElement(nodes=[na, n2, n3, nd], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc, n2], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element])])
    return theVeryBest(newSkeleton, (refine0, refine1, refine2), alpha)
    
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
        [getProvisionalElement(nodes=[n0, na, nd, n3], parents=[element]),
         getProvisionalElement(nodes=[na, nc, n2, nd], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element])])
    refine1 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nd, n3], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
         getProvisionalElement(nodes=[nc, n2, nd], parents=[element])])
    refine2 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nd, n3], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc, nd], parents=[element]),
         getProvisionalElement(nodes=[nc, n2, nd], parents=[element])])
    refine3 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nd, n3], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, nc, n2, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element])])
    return theVeryBest(newSkeleton, (refine0, refine1, refine2, refine3), alpha)

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

#  3----d-------------2   3-------------d----2                            
#  |   /              |   |              \   |   3------------d-----------2
#  |  /               |   |               \  |   |           /\           |
#  | /                |   |                \ |   |          /  \          |
#  |/                 |   |                 \|   |         /    \         |
#  e------------------c   e------------------c   e        /      \        c
#  |\                /|   |\                /|   |\      /        \      /|
#  | \              / |   | \              / |   | \    /          \    / |
#  |  \            /  |   |  \            /  |   |  \  /            \  /  |
#  |   \          /   |   |   \          /   |   |   \/              \/   |
#  0----a--------b----1   0----a--------b----1   0----a---------------b---1
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
    refinements = (
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, ne], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, ne], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[nc, n2, nd, ne], parents=[element]),
             getProvisionalElement(nodes=[ne, nd, n3], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, ne], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, ne], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[nc, nd, n3, ne], parents=[element]),
             getProvisionalElement(nodes=[nc, n2, nd], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, ne], parents=[element]),
             getProvisionalElement(nodes=[na, nd, n3, ne], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nd], parents=[element]),
             getProvisionalElement(nodes=[nb, nc, n2, nd], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, ne], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nd, ne], parents=[element]),
             getProvisionalElement(nodes=[nb, nc, n2, nd], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[ne, nd, n3], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, ne], parents=[element]),
             getProvisionalElement(nodes=[na, nd, n3, ne], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[nc, n2, nd], parents=[element])]))
    return theVeryBest(newSkeleton, refinements, alpha)
    
RefinementRule(largeRules, (2,1,1,1), rule2111)

# 2111q is the third refinement in 2111.

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

#    3--------------2   3--------------2  
#    | *            |   |              | 
#    |    *         |   |              | 
#    |       *      |   |*             | 
#    |          *   |   |              | 
#    |             *d   |              d 
#    |             /|   | *           /| 
#    |            / |   |            / | 
#    |           /  |   |           /  | 
#    |          /   |   |  *       /   | 
#    |         /    c   |         /    c 
#    |        /    /|   |        /    /| 
#    |       /    / |   |   *   /    / | 
#    |      /    /  |   |      /    /  | 
#    |     /    /   |   |    */    /   | 
#    0----a----b----1   0----a----b----1 

def rule2200(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    refine1 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nd, n3], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
         getProvisionalElement(nodes=[nd, n2, n3], parents=[element])])
    refine2 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, n3], parents=[element]),
         getProvisionalElement(nodes=[na, nd, n2, n3], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element])])
    return theVeryBest(newSkeleton, (refine1, refine2), alpha)

RefinementRule(largeRules, (2,2,0,0), rule2200)

#    3--------------2 
#    | *            |
#    |    *         |
#    |*      *      |
#    |          *   |
#    |             *d
#    | *           /|
#    |            / |
#    |           /  |
#    |  *       /   |
#    |         /    c
#    |        /    /|
#    |   *   /    / |
#    |      /    /  |
#    |    */    /   |
#    0----a----b----1

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
    refinement = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nd, n3], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, n2, nc], parents=[element])])
    return theVeryBest(newSkeleton, (refinement,), alpha)

RefinementRule(largeRules, (2,0,2,0), rule2020)

def rule2020q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+2)%4][0]
    nd = edgenodes[(rotation+2)%4][1]
    return (
        newSkeleton.newElement(nodes=[n0, na, nd, n3], parents=[element]),
        newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
        newSkeleton.newElement(nodes=[nb, n1, n2, nc], parents=[element]))

RefinementRule(quickRules, (2,0,2,0), rule2020q)

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
        [getProvisionalElement(nodes=[n0, na, ne, n3], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nd, ne], parents=[element]),
         getProvisionalElement(nodes=[nb, nc, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
         getProvisionalElement(nodes=[nc, n2, nd], parents=[element])])
    refine1 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, ne, n3], parents=[element]),
         getProvisionalElement(nodes=[na, nf, ne], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nf], parents=[element]),
         getProvisionalElement(nodes=[nf, nd, ne], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc, nf], parents=[element]),
         getProvisionalElement(nodes=[nf, nc, n2, nd], parents=[element])],
        internalNodes=[nf])
    return theVeryBest(newSkeleton, (refine0, refine1), alpha)

RefinementRule(largeRules, (2,1,2,0), rule2120)

def rule2120q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+2)%4][0]
    ne = edgenodes[(rotation+2)%4][1]
    return (
        newSkeleton.newElement(nodes=[n0, na, ne, n3], parents=[element]),
        newSkeleton.newElement(nodes=[na, nb, nd, ne], parents=[element]),
        newSkeleton.newElement(nodes=[nb, nc, nd], parents=[element]),
        newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
        newSkeleton.newElement(nodes=[nc, n2, nd], parents=[element]))

RefinementRule(quickRules, (2,1,2,0), rule2120q)

### 2121 ###

#  3-----e----d-----2   3-----e----d-----2
#  |     |    |     |   |     |    |\    |
#  |     |    |     |   |     |    | \   |
#  |     |    |     |   |     |    |  \  |
#  |     |    |     |   |     |    |   \ |
#  |     |    |     |   |     |    |    \|
#  f     |    |     c   f     |    |     c
#  |\    |    |    /|   |\    |    |     |
#  | \   |    |   / |   | \   |    |     |
#  |  \  |    |  /  |   |  \  |    |     |
#  |   \ |    | /   |   |   \ |    |     |
#  |    \|    |/    |   |    \|    |     |
#  0-----a----b-----1   0-----a----b-----1
#  
#  3-----e----d-----2   3-----e----d-----2
#  |    /|    |     |   |    /|    |\    |
#  |   / |    |     |   |   / |    | \   |
#  |  /  |    |     |   |  /  |    |  \  |
#  | /   |    |     |   | /   |    |   \ |
#  |/    |    |     |   |/    |    |    \|
#  f     |    |     c   f     |    |     c
#  |     |    |    /|   |     |    |     |
#  |     |    |   / |   |     |    |     |
#  |     |    |  /  |   |     |    |     |
#  |     |    | /   |   |     |    |     |
#  |     |    |/    |   |     |    |     |
#  0-----a----b-----1   0-----a----b-----1
#  
#  3-----e-----d-----2
#  |     |     |     |
#  |     |     |     |
#  |     |     |     |
#  |     |     |     |
#  |     |     |     |
#  f-----g-----h-----c
#  |     |     |     |
#  |     |     |     |
#  |     |     |     |
#  |     |     |     |
#  |     |     |     |
#  0-----a-----b-----1

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
    refinements = (
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nf], parents=[element]),
             getProvisionalElement(nodes=[na, ne, n3, nf], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nd, ne], parents=[element]),
             getProvisionalElement(nodes=[nb, nc, n2, nd], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nf], parents=[element]),
             getProvisionalElement(nodes=[na, ne, n3, nf], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nd, ne], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc, nd], parents=[element]),
             getProvisionalElement(nodes=[nc, n2, nd], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, ne, nf], parents=[element]),
             getProvisionalElement(nodes=[ne, n3, nf], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nd, ne], parents=[element]),
             getProvisionalElement(nodes=[nb, nc, n2, nd], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, ne, nf], parents=[element]),
             getProvisionalElement(nodes=[ne, n3, nf], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nd, ne], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc, nd], parents=[element]),
             getProvisionalElement(nodes=[nc, n2, nd], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, ng, nf], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nh, ng], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc, nh], parents=[element]),
             getProvisionalElement(nodes=[nh, nc, n2, nd], parents=[element]),
             getProvisionalElement(nodes=[ng, nh, nd, ne], parents=[element]),
             getProvisionalElement(nodes=[nf, ng, ne, n3], parents=[element])],
            internalNodes = (ng, nh))
        )
    return theVeryBest(newSkeleton, refinements, alpha)

RefinementRule(largeRules, (2,1,2,1), rule2121)

#  3-----e----d-----2 
#  |    /|    |\    | 
#  |   / |    | \   | 
#  |  /  |    |  \  | 
#  | /   |    |   \ | 
#  |/    |    |    \| 
#  f     |    |     c 
#  |\    |    |    /| 
#  | \   |    |   / | 
#  |  \  |    |  /  | 
#  |   \ |    | /   | 
#  |    \|    |/    | 
#  0-----a----b-----1 

def rule2121q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+2)%4][0]
    ne = edgenodes[(rotation+2)%4][1]
    nf = edgenodes[(rotation+3)%4][0]
    return (
        newSkeleton.newElement(nodes=[n0, na, nf], parents=[element]),
        newSkeleton.newElement(nodes=[na, ne, nf], parents=[element]),
        newSkeleton.newElement(nodes=[nf, ne, n3], parents=[element]),
        newSkeleton.newElement(nodes=[na, nb, nd, ne], parents=[element]),
        newSkeleton.newElement(nodes=[nb, nc, nd], parents=[element]),
        newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
        newSkeleton.newElement(nodes=[nc, n2, nd], parents=[element]))

RefinementRule(quickRules, (2,1,2,1), rule2121q)


### 2201 ###

#  3--------------2   3--------------2   3--------------2  
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
#
#  3--------------2   3--------------2  
#  |              |   |              |  
#  e--------------d   e--------------d  
#  |\             |   | *            |  
#  |*\            |   |    *         |  
#  |  \           |   |       *      |  
#  | * \          |   |          *   |  
#  |    \         c   |             *c  
#  |  *  \       /|   |           * /|  
#  |      \     / |   |         *  / |  
#  |   *   \   /  |   |       *   /  |  
#  |        \ /   |   |     *    /   |  
#  0----a----b----1   0---a-----b----1  

# All refinements that don't include segment ed have new edges going
# though the corner nodes 2 and 3.

def rule2201(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+3)%4][0]
    refinements = (
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nd, ne], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[nd, n2, n3, ne], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, ne], parents=[element]),
             getProvisionalElement(nodes=[na, nb, ne], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc, ne], parents=[element]),
             getProvisionalElement(nodes=[nc, nd, ne], parents=[element]),
             getProvisionalElement(nodes=[nd, n2, n3, ne], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, ne], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, ne], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[nc, nd, ne], parents=[element]),
             getProvisionalElement(nodes=[nd, n2, n3, ne], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, ne], parents=[element]),
             getProvisionalElement(nodes=[na, nb, ne], parents=[element]),
             getProvisionalElement(nodes=[nb, nc, nd, ne], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[nd, n2, n3, ne], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, nc, ne], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[nc, nd, ne], parents=[element]),
             getProvisionalElement(nodes=[nd, n2, n3, ne], parents=[element])])
        )
    return theVeryBest(newSkeleton, refinements, alpha)

RefinementRule(largeRules, (2,2,0,1), rule2201)

def rule2201q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+3)%4][0]
    return (
        newSkeleton.newElement(nodes=[n0, na, nd, ne], parents=[element]),
        newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
        newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
        newSkeleton.newElement(nodes=[nd, n2, n3, ne], parents=[element]))

RefinementRule(quickRules, (2,2,0,1), rule2201q)

### 2210 ###

## 2210 is the same as 2201 but flipped on the diagonal.

#  3---e------2   3---e------2   3---e---------2   3----e------2    
#  |   |      |   |   |\     |   |   |\        |   |    |\     | 
#  |   |      |   |   |*\    |   |   |*\       |   |    |*\    | 
#  |   |      |   |   |  \   |   |   |  \      |   |    |  \   | 
#  |   |      |   |   | + \  |   |   | * \     |   |    | * \  | 
#  |   |      |   |   |*   \ |   |   |    \    |   |    |    \ | 
#  |   |      d   |   |  +  \|   |   |  *  \   |   |    |  *  \| 
#  |   |     /|   |   |      d   |   |      \  |   |    |      d 
#  |   |    / |   |   | * +  |   |   |   *   \ |   |    |   *  | 
#  |   |   /  c   |   |      |   |   |        \|   |    |      | 
#  |   |  /  /|   |   |     +|   |   |    *    d   |    |    * | 
#  |   | /  / |   |   |  *   c   |   |         |   |    |      c 
#  |   |/  /  |   |   |      |   |   |     *   |   |    |     /| 
#  0---a--b---1   |   |      |   |   |         c   |    |    / | 
#                 |   |   *  |   |   |      * /|   |    |   /  |
#                 0---a----b-1   0---a-------b-1   0----a--b---1
#
#
#  3---e---------------2
#  |   |               |
#  |   |*              |
#  |   |               |
#  |   | *             |
#  |   |               |
#  |   |  *            |
#  |   |               d
#  |   |   *          /|
#  |   |             / |
#  |   |    *       /  |
#  |   |           /   |
#  |   |     *    /    c
#  |   |         /   * |
#  |   |      * / *    |
#  0---a-------b-------1
#  

def rule2210(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+2)%4][0]
    refinements = (
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, ne, n3], parents=[element]),
             getProvisionalElement(nodes=[na, nd, n2, ne], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, ne, n3], parents=[element]),
             getProvisionalElement(nodes=[na, nb, ne], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc, ne], parents=[element]),
             getProvisionalElement(nodes=[nc, nd, ne], parents=[element]),
             getProvisionalElement(nodes=[nd, n2, ne], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, ne, n3], parents=[element]),
             getProvisionalElement(nodes=[na, nb, ne], parents=[element]),
             getProvisionalElement(nodes=[nb, nc, nd, ne], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[nd, n2, ne], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, ne, n3], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, ne], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[nc, nd, ne], parents=[element]),
             getProvisionalElement(nodes=[nd, n2, ne], parents=[element])]),
        ProvisionalRefinement(
            [getProvisionalElement(nodes=[n0, na, ne, n3], parents=[element]),
             getProvisionalElement(nodes=[na, nb, ne], parents=[element]),
             getProvisionalElement(nodes=[nb, nd, n2, ne], parents=[element]),
             getProvisionalElement(nodes=[nb, nc, nd], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element])])
        )
    return theVeryBest(newSkeleton, refinements, alpha)

RefinementRule(largeRules, (2,2,1,0), rule2210)

def rule2210q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+2)%4][0]
    return (
        newSkeleton.newElement(nodes=[n0, na, ne, n3], parents=[element]),
        newSkeleton.newElement(nodes=[na, nd, n2, ne], parents=[element]),
        newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
        newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]))
    
RefinementRule(quickRules, (2,2,1,0), rule2210q)

### 2211 ###

#   3------e------2   3------e------2   3------e------2   3------e------2
#   |      |      |   |     /|      |   |       \     |   |     /       |
#   |      |      |   |    / |      |   |        \    |   |    /        |
#   |      |      |   |   /  |      |   |         \   |   |   /         |
#   |      |      |   |  /   |      |   |          \  |   |  /          |
#   |      |      |   | /    |      |   |           \ |   | /           |
#   |      |      |   |/     |      |   |            \|   |/            |
#   f      |      d   f      |      d   f-------------d   f-------------d
#   |\     |     /|   |      |     /|   |            /|   |            /|
#   | \    |    / |   |      |    / |   |           / |   |           / |
#   |  \   |   /  c   |      |   /  c   |          /  c   |          /  c
#   |   \  |  /  /|   |      |  /  /|   |         /  /|   |         /  /|
#   |    \ | /  / |   |      | /  / |   |        /  / |   |        /  / |
#   |     \|/  /  |   |      |/  /  |   |       /  /  |   |       /  /  |
#   0------a--b---1   0------a--b---1   0------a--b---1   0------a--b---1
#         (1)               (2)               (3)               (4)      

#   3------e-------2    3------e-------2 
#   |     /*\      |    |     / \      | 
#   |    /   \     |    |    /   \     | 
#   |   /     \    |    |   /     \    | 
#   |  /    *  \   |    |  /       \   | 
#   | /         \  |    | /         \  | 
#   |/           \ |    |/           \ | 
#   f        *    \|    f             \| 
#   |\             d    |\  *          d 
#   | \            |    | \     *      | 
#   |  \      *    |    |  \        *  | 
#   |   \          c    |   \          c 
#   |    \     *  /|    |    \        /| 
#   |     \      / |    |     \      / | 
#   0------a----b--1    0------a----b--1 
#          (5)                (6)         

# There are at least 20 refinements containing ae or df, not counting
# the additional ones that can be generated by further subdividing
# quads.  We're not including them all. For example, we've skipped
# these:

#   3------e------2   3------e-------2    3------e------2   3------e------2
#   |      |\     |   |     /|\      |    |     /|\     |   |      |\     |
#   |      | \    |   |    / | \     |    |    / | \    |   |      | \    |
#   |      |  \   |   |   /  |  \    |    |   /  | *\   |   |      |  \   |
#   |      |   \  |   |  /   |*  \   |    |  /   |   \  |   |      |   \  |
#   |      |    \ |   | /    |    \  |    | /    |  * \ |   |      |    \ |
#   |      |     \|   |/     |     \ |    |/     |     \|   |      |     \|
#   f      |      d   f      | *    \|    f      |   *  d   f      |      d
#   |\     |      |   |\     |       d    |      |      |   |\     |     *|
#   | \    |      |   | \    |       |    |      |    * |   | \    |      |
#   |  \   |      c   |  \   |  *    |    |      |      c   |  \   |    * c
#   |   \  |    */|   |   \  |       c    |      |     /|   |   \  |     /|
#   |    \ |  * / |   |    \ |   *  /|    |      |    / |   |    \ |   */ |
#   |     \|*  /  |   |     \|     / |    |      |   /  |   |     \|   /  |
#   0------a--b---1   0------a----b--1    0------a--b---1   0------a--b---1

## TODO: Include them all?  Write a program to generate code for them?


def rule2211(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+2)%4][0]
    nf = edgenodes[(rotation+3)%4][0]
    refinements = (
        ProvisionalRefinement(  # (1)
            [getProvisionalElement(nodes=[n0, na, nf], parents=[element]),
             getProvisionalElement(nodes=[na, ne, n3, nf], parents=[element]),
             getProvisionalElement(nodes=[na, nd, n2, ne], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element])]),
        ProvisionalRefinement(  # (2)
            [getProvisionalElement(nodes=[n0, na, ne, nf], parents=[element]),
             getProvisionalElement(nodes=[na, nd, n2, ne], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[nf, ne, n3], parents=[element])]),
        ProvisionalRefinement(  # (3)
            [getProvisionalElement(nodes=[n0, na, nd, nf], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[nd, n2, ne], parents=[element]),
             getProvisionalElement(nodes=[nd, ne, n3, nf], parents=[element])]),
        ProvisionalRefinement(  # (4)
            [getProvisionalElement(nodes=[n0, na, nd, nf], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[nd, n2, ne, nf], parents=[element]),
             getProvisionalElement(nodes=[ne, n3, nf])]),
        ProvisionalRefinement(  # (5)
            [getProvisionalElement(nodes=[n0, na, nf], parents=[element]),
             getProvisionalElement(nodes=[na, nb, ne, nf], parents=[element]),
             getProvisionalElement(nodes=[nb, nc, nd, ne], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[nd, n2, ne], parents=[element]),
             getProvisionalElement(nodes=[ne, n3, nf], parents=[element])]),
        ProvisionalRefinement(  # (6)
            [getProvisionalElement(nodes=[n0, na, nf], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, nf], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[nc, nd, ne, nf], parents=[element]),
             getProvisionalElement(nodes=[nd, n2, ne], parents=[element]),
             getProvisionalElement(nodes=[ne, n3, nf], parents=[element])]),
        )
    return theVeryBest(newSkeleton, refinements, alpha)

RefinementRule(largeRules, (2,2,1,1), rule2211)

#   3------e------2 
#   |     / \     | 
#   |    /   \    | 
#   |   /     \   | 
#   |  /       \  | 
#   | /         \ | 
#   |/           \| 
#   f             d 
#   |\           /| 
#   | \         / | 
#   |  \       /  c 
#   |   \     /  /| 
#   |    \   /  / | 
#   |     \ /  /  | 
#   0------a--b---1 
        
def rule2211q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+2)%4][0]
    nf = edgenodes[(rotation+3)%4][0]
    refinement = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nf], parents=[element]),
         getProvisionalElement(nodes=[na, nd, ne, nf], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
         getProvisionalElement(nodes=[nd, n2, ne], parents=[element]),
         getProvisionalElement(nodes=[ne, n3, nf], parents=[element])])
    return theVeryBest(newSkeleton, (refinement,), alpha)

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

# TODO: Add more refinements?

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
        [getProvisionalElement(nodes=[n0, na, nf, n3], parents=[element]),
         getProvisionalElement(nodes=[na, nb, ne, nf], parents=[element]),
         getProvisionalElement(nodes=[nb, nc, nd, ne], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
         getProvisionalElement(nodes=[nd, n2, ne], parents=[element])])
    refine1 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nf, n3], parents=[element]),
         getProvisionalElement(nodes=[na, nh, ng, nf], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nh], parents=[element]),
         getProvisionalElement(nodes=[ng, ne, nf], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc, nh], parents=[element]),
         getProvisionalElement(nodes=[nh, nc, nd, ng], parents=[element]),
         getProvisionalElement(nodes=[ng, nd, n2, ne], parents=[element])],
        internalNodes=[ng, nh])
    refine2 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nj], parents=[element]),
         getProvisionalElement(nodes=[na, nb, nh, nj], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc, nh], parents=[element]),
         getProvisionalElement(nodes=[nh, nc, nd, ng], parents=[element]),
         getProvisionalElement(nodes=[ng, nd, n2, ne], parents=[element]),
         getProvisionalElement(nodes=[ni, ng, ne, nf], parents=[element]),
         getProvisionalElement(nodes=[ni, nf, n3], parents=[element]),
         getProvisionalElement(nodes=[n0, nj, ni, n3], parents=[element]),
         getProvisionalElement(nodes=[nj, nh, ng, ni], parents=[element])],
        internalNodes=[ng, nh, ni, nj])
        
    return theVeryBest(newSkeleton, (refine0, refine1, refine2), alpha)

RefinementRule(largeRules, (2,2,2,0), rule2220)

def rule2220q(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+2)%4][0]
    nf = edgenodes[(rotation+2)%4][1]
    refinement = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nf, n3], parents=[element]),
         getProvisionalElement(nodes=[na, nb, ne, nf], parents=[element]),
         getProvisionalElement(nodes=[nb, nc, nd, ne], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
         getProvisionalElement(nodes=[nd, n2, ne], parents=[element])])
    return theVeryBest(newSkeleton, (refinement,), alpha)

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

# TODO: Add more refinements?

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
        [getProvisionalElement(nodes=[n0, na, ng], parents=[element]),
         getProvisionalElement(nodes=[na, nf, ng], parents=[element]),
         getProvisionalElement(nodes=[na, nb, ne, nf], parents=[element]),
         getProvisionalElement(nodes=[nb, nc, nd, ne], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
         getProvisionalElement(nodes=[nd, n2, ne], parents=[element]),
         getProvisionalElement(nodes=[nf, n3, ng], parents=[element])])
    refine1 = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, nh, ng], parents=[element]),
         getProvisionalElement(nodes=[na, nb, ni, nh], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc, ni], parents=[element]),
         getProvisionalElement(nodes=[nc, nd, ni], parents=[element]),
         getProvisionalElement(nodes=[nd, n2, ne, ni], parents=[element]),
         getProvisionalElement(nodes=[ni, ne, nf, nh], parents=[element]),
         getProvisionalElement(nodes=[nh, nf, n3, ng], parents=[element])],
        internalNodes=[nh, ni])
    return theVeryBest(newSkeleton, (refine0, refine1), alpha)

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
    refinement = ProvisionalRefinement(
        [getProvisionalElement(nodes=[n0, na, ng], parents=[element]),
         getProvisionalElement(nodes=[na, nf, ng], parents=[element]),
         getProvisionalElement(nodes=[na, nb, ne, nf], parents=[element]),
         getProvisionalElement(nodes=[nb, nc, nd, ne], parents=[element]),
         getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
         getProvisionalElement(nodes=[nd, n2, ne], parents=[element]),
         getProvisionalElement(nodes=[nf, n3, ng], parents=[element])])
    return theVeryBest(newSkeleton, (refinement,), alpha)

RefinementRule(quickRules, (2,2,2,1), rule2221q)


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
#  3---f--e------2     3------f--e---2 
#  |  /  /       |     |       \  \  | 
#  | /  /        |     |        \  \ | 
#  |/  /         |     |         \  \| 
#  g  /          |     |          \  d 
#  | /           |     |           \ | 
#  |/            |     |            \| 
#  h-------------d     g-------------c   4 and 4a
#  |            /|     |\            | 
#  |           / |     | \           | 
#  |          /  c     h  \          | 
#  |         /  /|     |\  \         | 
#  |        /  / |     | \  \        | 
#  |       /  /  |     |  \  \       | 
#  0------a--b---1     0---a--b------1 
#


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
            [getProvisionalElement(nodes=[n0, na, nh], parents=[element]),
             getProvisionalElement(nodes=[na, nf, ng, nh], parents=[element]),
             getProvisionalElement(nodes=[ng, nf, n3], parents=[element]),
             getProvisionalElement(nodes=[na, nb, ne, nf], parents=[element]),
             getProvisionalElement(nodes=[nb, nc, nd, ne], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[nd, n2, ne], parents=[element])]),
        ProvisionalRefinement(  # 1
            [getProvisionalElement(nodes=[n0, na, nh], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, nh], parents=[element]),
             getProvisionalElement(nodes=[ng, nf, n3], parents=[element]),
             getProvisionalElement(nodes=[nh, nc, nd, ng], parents=[element]),
             getProvisionalElement(nodes=[ng, nd, ne, nf], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element]),
             getProvisionalElement(nodes=[nd, n2, ne], parents=[element])]),
        ProvisionalRefinement( # 2
            [getProvisionalElement(nodes=[n0, na, nk, nh], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nl, nk], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc, nl], parents=[element]),
             getProvisionalElement(nodes=[nh, nk, ni, ng], parents=[element]),
             getProvisionalElement(nodes=[nk, nl, nj, ni], parents=[element]),
             getProvisionalElement(nodes=[nl, nc, nd, nj], parents=[element]),
             getProvisionalElement(nodes=[ng, ni, nf, n3], parents=[element]),
             getProvisionalElement(nodes=[ni, nj, ne, nf], parents=[element]),
             getProvisionalElement(nodes=[nj, nd, n2, ne], parents=[element])],
            internalNodes = (ni, nj, nk, nl)),
        ProvisionalRefinement(  # 3
            [getProvisionalElement(nodes=[ng, nf, n3], parents=[element]),
             getProvisionalElement(nodes=[nh, ne, nf, ng], parents=[element]),
             getProvisionalElement(nodes=[n0, na, ne, nh], parents=[element]),
             getProvisionalElement(nodes=[na, nd, n2, ne], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element])]),
        ProvisionalRefinement( # 3a
            [getProvisionalElement(nodes=[n0, na, nh], parents=[element]),
             getProvisionalElement(nodes=[na, nb, ng, nh], parents=[element]),
             getProvisionalElement(nodes=[nb, nf, n3, ng], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc, nf], parents=[element]),
             getProvisionalElement(nodes=[nc, nd, ne, nf], parents=[element]),
             getProvisionalElement(nodes=[nd, n2, ne], parents=[element])]),
        ProvisionalRefinement(  # 4
            [getProvisionalElement(nodes=[ng, nf, n3], parents=[element]),
             getProvisionalElement(nodes=[nh, ne, nf, ng], parents=[element]),
             getProvisionalElement(nodes=[nh, nd, n2, ne], parents=[element]),
             getProvisionalElement(nodes=[n0, na, nd, nh], parents=[element]),
             getProvisionalElement(nodes=[na, nb, nc, nd], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc], parents=[element])]),
        ProvisionalRefinement(  # 4a
            [getProvisionalElement(nodes=[n0, na, nh], parents=[element]),
             getProvisionalElement(nodes=[na, nb, ng, nh], parents=[element]),
             getProvisionalElement(nodes=[nb, n1, nc, ng], parents=[element]),
             getProvisionalElement(nodes=[ng, nc, nf, n3], parents=[element]),
             getProvisionalElement(nodes=[nc, nd, ne, nf], parents=[element]),
             getProvisionalElement(nodes=[nd, n2, ne], parents=[element])])
    )
    return theVeryBest(newSkeleton, refinements, alpha)

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
    return (
        newSkeleton.newElement(nodes=[n0, na, nk, nh], parents=[element]),
        newSkeleton.newElement(nodes=[na, nb, nl, nk], parents=[element]),
        newSkeleton.newSkeleton(nodes=[nb, n1, nc, nl], parents=[element]),
        newSkeleton.newElement(nodes=[nh, nk, ni, ng], parents=[element]),
        newSkeleton.newElement(nodes=[nk, nl, nj, ni], parents=[element]),
        newSkeleton.newElement(nodes=[nl, nc, nd, nj], parents=[element]),
        newSkeleton.newElement(nodes=[ng, ni, nf, n3], parents=[element]),
        newSkeleton.newElement(nodes=[ni, nj, ne, nf], parents=[element]),
        newSkeleton.newElement(nodes=[nj, nd, n2, ne], parents=[element]))

RefinementRule(quickRules, (2,2,2,2), rule2222q)
