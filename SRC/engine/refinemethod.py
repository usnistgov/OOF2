# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.common import ooferror
from ooflib.common import debug
from ooflib.common import utils
from ooflib.common import primitives
from ooflib.common import enum
from ooflib.common.IO import xmlmenudump

from ooflib.engine import skeletonelement
ProvisionalQuad = skeletonelement.ProvisionalQuad
ProvisionalTriangle = skeletonelement.ProvisionalTriangle
Point = primitives.Point
onethird = 1./3.

class RefinementRuleSet:
    allRuleSets = []
    ruleDict = {}
    def __init__(self, name, parent=None, help=None):
        self.rules = {}
        self._name = name
        self._help = help
        RefinementRuleSet.allRuleSets.append(self)
        RefinementRuleSet.ruleDict[name] = self
        if parent:
            self.parent = RefinementRuleSet.ruleDict[parent]
        else:
            self.parent = None
        updateRuleEnum(name, help) 
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
            raise
    def __getitem__(self, signature):
        return self.getRule(signature)
        
def getRuleSet(name):
    return RefinementRuleSet.ruleDict[name]

utils.OOFdefine('getRuleSet', getRuleSet)

#########################################

# The names of the refinement rule sets are stored in an Enum so that
# the UI can handle them correctly.

class RuleSet(enum.EnumClass(*[(r.name(), r.help())
                               for r in RefinementRuleSet.allRuleSets])):
    pass
##    def __repr__(self):
##	return "RuleSet('%s')" % self.name
utils.OOFdefine('RuleSet', RuleSet)

RuleSet.tip = "Refinement rule sets."
RuleSet.discussion = xmlmenudump.loadFile('DISCUSSIONS/engine/enum/ruleset.xml')

def updateRuleEnum(name, help=None):
    enum.addEnumName(RuleSet, name, help)

# This function is used to get the default value for the RuleSet
# parameter in the refinement menu item.
def conservativeRuleSetEnum():
    return RuleSet(RefinementRuleSet.allRuleSets[0].name())

##########################################

class RefinementRule:
    def __init__(self, ruleset, signature, function):
        self.function = function
        ruleset.addRule(self, signature)
    def apply(self, element, signature_info, edgenodes, newSkeleton, alpha):
        # The first member of the signature_info is the rotation
        newels = self.function(element, signature_info[0], edgenodes,
                               newSkeleton, alpha)
        return newels

##########################################

# This function is called with an old element and an integer
# 'rotation'.  It returns copies (children in the SkeletonSelectable
# sense) of the nodes of the old element, with the order shifted
# around by the rotation.  The new refined elements will be built from
# these base nodes.

def baseNodes(element, rotation):
    nnodes = element.nnodes()
    return [element.nodes[(i+rotation)%nnodes].children[-1]
            for i in range(nnodes)]

class ProvisionalRefinement:
    def __init__(self, newbies = [], internalNodes = []):
        self.newbies = newbies
        self.internalNodes = internalNodes
    def energy(self, skeleton, alpha):
        energy = 0.0
        for element in self.newbies:
            energy += element.energyTotal(skeleton, alpha)
        return energy/len(self.newbies)
    def accept(self, skeleton):
        return [element.accept(skeleton) for element in self.newbies]

def theBetter(skeleton, candidates, alpha):
    energy_min = 100000.                # much larger than any possible energy
    theone = None
    for candi in candidates:
        energy = candi.energy(skeleton, alpha)
        if energy < energy_min:
            energy_min = energy
            theone = candi
    # Before returning the chosen refinement, we need to remove any internal
    # nodes created for the refinements that were not chosen.
    destroyedNodes = {}
    for candi in candidates:
        if candi is theone or not candi.internalNodes:
            continue
        for n in candi.internalNodes:
            if n not in theone.internalNodes and n not in destroyedNodes:
                n.destroy(skeleton)
                destroyedNodes[n] = 1
                
    return theone.accept(skeleton)

##########################################

# A missing function in the liberal rule set will be found in
# conservative ruleset. 
conservativeRuleSet = RefinementRuleSet(
    'conservative',
    help='Preserve topology: quads are refined into quads and triangles into triangles (whenever possible).')

liberalRuleSet = RefinementRuleSet(
    'liberal',
    parent='conservative',
    help="If there's a choice, choose the refinement that minimizes E, without trying to preserve topology.")

##########################################

#            BEGIN 2D RULES

##########################################


# Unrefined triangle
def rule000(element, rotation, edgenodes, newSkeleton, alpha):
    el = newSkeleton.newElement(nodes=baseNodes(element, rotation),
                                parents=[element])
    return (el,)
RefinementRule(conservativeRuleSet, (0,0,0), rule000)

#          2
#         /\
#        / |\
#       /  | \
#      /   |  \
#     /    |   \
#    /     |    \
#   /______|_____\
#   0      a      1
def rule100(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    return (newSkeleton.newElement(nodes=[na, n2, n0], parents=[element]),
            newSkeleton.newElement(nodes=[na, n1, n2], parents=[element]))
RefinementRule(conservativeRuleSet, (1,0,0), rule100)

#          2
#         /\
#        / |\
#       /  | \
#      /   |  b
#     /    | / \
#    /     |/   \
#   /______/_____\
#   0      a      1
#
#         OR
#
#          2
#         /\
#        /  \
#       /    \
#      /    . b
#     /  .   / \
#    /.     /   \
#   /______/_____\
#   0      a      1
#
# Choose the one with best shape - lower shape energy

def rule110(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%3][0]
    refine0 = ProvisionalRefinement(
        newbies=[ProvisionalTriangle(nodes=[n0, na, n2], parents=[element]),
                 ProvisionalTriangle(nodes=[na, n1, nb], parents=[element]),
                 ProvisionalTriangle(nodes=[na, nb, n2], parents=[element])])
    refine1 = ProvisionalRefinement(
        newbies=[ProvisionalTriangle(nodes=[n0, nb, n2], parents=[element]),
                 ProvisionalTriangle(nodes=[n0, na, nb], parents=[element]),
                 ProvisionalTriangle(nodes=[na, n1, nb], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1), alpha)
RefinementRule(conservativeRuleSet, (1,1,0), rule110)

#          2
#         /\
#        /  \
#       /    \
#      /      b
#     /      / \
#    /      /   \
#   /______/_____\
#   0      a      1
def rule110L(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%3][0]
    # refine0, refine1: conservative rules
    # refine2: the figure above
    refine0 = ProvisionalRefinement(
        newbies=[ProvisionalTriangle(nodes=[n0, na, n2], parents=[element]),
                 ProvisionalTriangle(nodes=[na, n1, nb], parents=[element]),
                 ProvisionalTriangle(nodes=[na, nb, n2], parents=[element])])
    refine1 = ProvisionalRefinement(
        newbies=[ProvisionalTriangle(nodes=[n0, nb, n2], parents=[element]),
                 ProvisionalTriangle(nodes=[n0, na, nb], parents=[element]),
                 ProvisionalTriangle(nodes=[na, n1, nb], parents=[element])])
    refine2 = ProvisionalRefinement(
        newbies=[ProvisionalQuad(nodes=[n0, na, nb, n2], parents=[element]),
                 ProvisionalTriangle(nodes=[na, n1, nb], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1, refine2), alpha)
RefinementRule(liberalRuleSet, (1,1,0), rule110L)

#          2
#         /\
#        /  \ 
#       /    \
#      c______b
#     / \    / \ 
#    /   \  /   \
#   /_____\/_____\
#   0      a      1

# There is actually another possibility for this signature:
#          2
#         /\
#        / |\ 
#       /  | \
#      c   |  b
#     / \  | / \ 
#    /   \ |/   \
#   /_____\/_____\
#   0      a      1
# (and its two other symmetric counterparts).  This isn't
# implemented here as it can be achieved through use of the
# SwapEdges routine in 2D.

def rule111(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%3][0]
    nc = edgenodes[(rotation+2)%3][0]
    return (
        newSkeleton.newElement(nodes=[n0, na, nc], parents=[element]),
        newSkeleton.newElement(nodes=[n1, nb, na], parents=[element]),
        newSkeleton.newElement(nodes=[n2, nc, nb], parents=[element]),
        newSkeleton.newElement(nodes=[na, nb, nc], parents=[element]))
RefinementRule(conservativeRuleSet, (1,1,1), rule111)

#             2
#             /\
#            /  \
#           /    \
#          c      b
#         / \    / \
#        /   \  /   \
#       /     \d     \
#      /      |       \
#     /       |        \
#    0________a_________1
#
def rule111L(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%3][0]
    nc = edgenodes[(rotation+2)%3][0]
    pos = element.center()
    nd = newSkeleton.newNode(pos.x, pos.y)

    # Compare two configurations and pick the better one.
    # refine0: conservative
    # refine1: the figure above
    refine0 = ProvisionalRefinement(
        newbies = [ProvisionalTriangle(nodes=[n0, na, nc], parents=[element]),
                   ProvisionalTriangle(nodes=[n1, nb, na], parents=[element]),
                   ProvisionalTriangle(nodes=[n2, nc, nb], parents=[element]),
                   ProvisionalTriangle(nodes=[na, nb, nc], parents=[element])])
    refine1 = ProvisionalRefinement(    
        newbies = [ProvisionalQuad(nodes=[n0, na, nd, nc], parents=[element]),
                   ProvisionalQuad(nodes=[na, n1, nb, nd], parents=[element]),
                   ProvisionalQuad(nodes=[nd, nb, n2, nc], parents=[element])],
        internalNodes = [nd])
    return theBetter(newSkeleton, (refine0, refine1), alpha)
RefinementRule(liberalRuleSet, (1,1,1), rule111L)

#          2
#         /\
#        /||\
#       / || \
#      /  ||  \
#     /  |  |  \
#    /  |    |  \
#   /___|____|___\
#   0   a     b   1
def rule200(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    return (
        newSkeleton.newElement(nodes=[n0, na, n2], parents=[element]),
        newSkeleton.newElement(nodes=[na, nb, n2], parents=[element]),
        newSkeleton.newElement(nodes=[nb, n1, n2], parents=[element]))
RefinementRule(conservativeRuleSet, (2,0,0), rule200)


#          2
#         /\
#        / |\
#       /  | \
#      /  c|  \
#     /   /\   \
#    /   /  \   \ 
#   /___/____\___\     
#   0   a     b   1
def rule200L(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    pos = element.center()
    nc = newSkeleton.newNode(pos.x, pos.y)
    # refine0: conservative
    # refine1: the figure above
    refine0 = ProvisionalRefinement(
        newbies = [ProvisionalTriangle(nodes=[n0, na, n2], parents=[element]),
                   ProvisionalTriangle(nodes=[na, nb, n2], parents=[element]),
                   ProvisionalTriangle(nodes=[nb, n1, n2], parents=[element])])
    refine1 = ProvisionalRefinement(
        newbies = [ProvisionalQuad(nodes=[n0, na, nc, n2], parents=[element]),
                   ProvisionalTriangle(nodes=[na, nb, nc], parents=[element]),
                   ProvisionalQuad(nodes=[nb, n1, n2, nc], parents=[element])],
        internalNodes = [nc])
    return theBetter(newSkeleton, (refine0, refine1), alpha)
RefinementRule(liberalRuleSet, (2,0,0), rule200L)

#            2 
#            /\
#           / .\
#          /  . \d
#         /   . /\
#        /    ./  \
#       /     /____\c
#      /  .  /\e   /\
#     /.    /  \  /  \
#    0-----a----b/----1
def rule220(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%3][0]
    nd = edgenodes[(rotation+1)%3][1]
    pos = element.center()
    ne = newSkeleton.newNode(pos.x, pos.y)
    return (
        newSkeleton.newElement(nodes=[n0, ne, n2], parents=[element]),
        newSkeleton.newElement(nodes=[n0, na, ne], parents=[element]),
        newSkeleton.newElement(nodes=[ne, nd, n2], parents=[element]),
        newSkeleton.newElement(nodes=[na, nb, ne], parents=[element]),
        newSkeleton.newElement(nodes=[nb, nc, ne], parents=[element]),
        newSkeleton.newElement(nodes=[ne, nc, nd], parents=[element]),
        newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]))
RefinementRule(conservativeRuleSet, (2,2,0), rule220)


#          2
#         /\
#        /  \d
#       /   /\
#      /   /  \
#     /   /    \c
#    /   /     /\
#   /___/____ /__\
#   0   a     b   1
def rule220L(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%3][0]
    nd = edgenodes[(rotation+1)%3][1]
    pos = element.center()
    ne = newSkeleton.newNode(pos.x, pos.y)
    # refine0: conservarive
    # refine1: the figure above
    refine0 = ProvisionalRefinement(
        newbies = [ProvisionalTriangle(nodes=[n0, ne, n2], parents=[element]),
                   ProvisionalTriangle(nodes=[n0, na, ne], parents=[element]),
                   ProvisionalTriangle(nodes=[ne, nd, n2], parents=[element]),
                   ProvisionalTriangle(nodes=[na, nb, ne], parents=[element]),
                   ProvisionalTriangle(nodes=[nb, nc, ne], parents=[element]),
                   ProvisionalTriangle(nodes=[ne, nc, nd], parents=[element]),
                   ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element])],
        internalNodes = [ne])
    refine1 = ProvisionalRefinement(
        newbies = [ProvisionalQuad(nodes=[n0, na, nd, n2], parents=[element]),
                   ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element]),
                   ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1), alpha)
RefinementRule(liberalRuleSet, (2,2,0), rule220L)   

#            2 
#            /\
#           /  \
#         e/____\d
#         /\    /\
#        /  \  /  \
#      f/____\/____\c
#      /\    /\g   /\
#     /  \  /  \  /  \
#    0----\a----b/----1
def rule222(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%3][0]
    nd = edgenodes[(rotation+1)%3][1]
    ne = edgenodes[(rotation+2)%3][0]
    nf = edgenodes[(rotation+2)%3][1]
    pos = element.center()
    ng = newSkeleton.newNode(pos.x, pos.y)
    return (
        newSkeleton.newElement(nodes=[n0, na, nf], parents=[element]),
        newSkeleton.newElement(nodes=[na, ng, nf], parents=[element]),
        newSkeleton.newElement(nodes=[na, nb, ng], parents=[element]),
        newSkeleton.newElement(nodes=[nb, nc, ng], parents=[element]),
        newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
        newSkeleton.newElement(nodes=[nf, ng, ne], parents=[element]),
        newSkeleton.newElement(nodes=[ng, nd, ne], parents=[element]),
        newSkeleton.newElement(nodes=[ng, nc, nd], parents=[element]),
        newSkeleton.newElement(nodes=[ne, nd, n2], parents=[element]))
RefinementRule(conservativeRuleSet, (2,2,2), rule222)

#            2
#            /\
#           /  \
#         e/    \d
#         /\    /\
#        /  \  /  \
#      f/____\/____\c
#      /     /\g    \
#     /     /  \     \
#    0-----a----b-----1

#            2 
#            /\
#           /  \
#         e/____\d
#         /      \
#        /        \
#      f/__________\c
#      /\          /\
#     /  \        /  \
#    0----\a----b/----1

#            2 
#            /\
#           /  \
#         e/____\d
#         /\     \
#        /  \     \
#      f/    \     \c
#      /\     \    /\
#     /  \     \  /  \
#    0----\a----b/----1

#            2 
#            /\
#           /  \
#         e/____\d
#         /     /\
#        /     /  \
#      f/     /    \c
#      /\    /     /\
#     /  \  /     /  \
#    0----\a----b/----1

def rule222L(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%3][0]
    nd = edgenodes[(rotation+1)%3][1]
    ne = edgenodes[(rotation+2)%3][0]
    nf = edgenodes[(rotation+2)%3][1]
    pos = element.center()
    ng = newSkeleton.newNode(pos.x, pos.y)
    # refine0: conservative
    # the rest: figures above
    refine0 = ProvisionalRefinement(
        newbies= [ProvisionalTriangle(nodes=[n0, na, nf], parents=[element]),
                  ProvisionalTriangle(nodes=[na, ng, nf], parents=[element]),
                  ProvisionalTriangle(nodes=[na, nb, ng], parents=[element]),
                  ProvisionalTriangle(nodes=[nb, nc, ng], parents=[element]),
                  ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
                  ProvisionalTriangle(nodes=[nf, ng, ne], parents=[element]),
                  ProvisionalTriangle(nodes=[ng, nd, ne], parents=[element]),
                  ProvisionalTriangle(nodes=[ng, nc, nd], parents=[element]),
                  ProvisionalTriangle(nodes=[ne, nd, n2], parents=[element])],
        internalNodes = [ng])
    refine1 = ProvisionalRefinement(
        newbies = [ProvisionalQuad(nodes=[n0, na, ng, nf], parents=[element]),
                   ProvisionalTriangle(nodes=[na, nb, ng], parents=[element]),
                   ProvisionalQuad(nodes=[nb, n1, nc, ng], parents=[element]),
                   ProvisionalTriangle(nodes=[ng, nc, nd], parents=[element]),
                   ProvisionalQuad(nodes=[ng, nd, n2, ne], parents=[element]),
                   ProvisionalTriangle(nodes=[nf, ng, ne], parents=[element])],
        internalNodes = [ng])
    refine2 = ProvisionalRefinement(
        newbies = [ProvisionalTriangle(nodes=[n0, na, nf], parents=[element]),
                   ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
                   ProvisionalTriangle(nodes=[ne, nd, n2], parents=[element]),
                   ProvisionalQuad(nodes=[na, nb, nc, nf], parents=[element]),
                   ProvisionalQuad(nodes=[nf, nc, nd, ne], parents=[element])])
    refine3 = ProvisionalRefinement(
        newbies = [ProvisionalTriangle(nodes=[n0, na, nf], parents=[element]),
                   ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
                   ProvisionalTriangle(nodes=[ne, nd, n2], parents=[element]),
                   ProvisionalQuad(nodes=[na, nb, ne, nf], parents=[element]),
                   ProvisionalQuad(nodes=[nb, nc, nd, ne], parents=[element])])
    refine4 = ProvisionalRefinement(
        newbies = [ProvisionalTriangle(nodes=[n0, na, nf], parents=[element]),
                   ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
                   ProvisionalTriangle(nodes=[ne, nd, n2], parents=[element]),
                   ProvisionalQuad(nodes=[na, nd, ne, nf], parents=[element]),
                   ProvisionalQuad(nodes=[na, nb, nc, nd], parents=[element])])
    return theBetter(newSkeleton,
                     (refine0, refine1, refine2, refine3, refine4),
                     alpha)
RefinementRule(liberalRuleSet, (2,2,2), rule222L)

## TODO: Rules that mix bisection and trisection are commented out and
## maybe should be deleted.  They could be used by SnapRefine but not
## by Refine.

## #            2
## #            /\
## #           /  \
## #          /    \ 
## #        d/______\c
## #        /|      |\
## #       / |      | \ 
## #      /  |      |  \
## #     /   |      |   \
## #    0----a------b----1
## def rule211(element, rotation, edgenodes, newSkeleton, alpha):
##     n0, n1, n2 = baseNodes(element, rotation)
##     na = edgenodes[rotation][0]
##     nb = edgenodes[rotation][1]
##     nc = edgenodes[(rotation+1)%3][0]
##     nd = edgenodes[(rotation+2)%3][0]
##     return (
##         newSkeleton.newElement(nodes=[n0, na, nd], parents=[element]),
##         newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
##         newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
##         newSkeleton.newElement(nodes=[nd, nc, n2], parents=[element]))
## RefinementRule(liberalRuleSet, (2,1,1), rule211)

## #            2
## #            /\
## #           /  \
## #         e/    \d
## #         /\    /\
## #        /  \  /  \
## #       /    \/____\c
## #      /     /\f    \
## #     /     /  \     \
## #    0-----a----b-----1
## def rule221(element, rotation, edgenodes, newSkeleton, alpha):
##     n0, n1, n2 = baseNodes(element, rotation)
##     na = edgenodes[rotation][0]
##     nb = edgenodes[rotation][1]
##     nc = edgenodes[(rotation+1)%3][0]
##     nd = edgenodes[(rotation+1)%3][1]
##     ne = edgenodes[(rotation+2)%3][0]
##     pos = element.center()
##     nf = newSkeleton.newNode(pos.x, pos.y)
##     return (
##         newSkeleton.newElement(nodes=[n0, na, nf, ne], parents=[element]),
##         newSkeleton.newElement(nodes=[nf, nd, n2, ne], parents=[element]),
##         newSkeleton.newElement(nodes=[na, nb, nf], parents=[element]),
##         newSkeleton.newElement(nodes=[nf, nc, nd], parents=[element]),
##         newSkeleton.newElement(nodes=[nb, n1, nc, nf], parents=[element]))
## RefinementRule(liberalRuleSet, (2,2,1), rule221)

## #            2
## #            /\
## #           /  \
## #         e/    \d
## #         /\    /\
## #        /  \  /  \
## #       /    \/____\c
## #      /     /\f   /\
## #     /     /  \  /  \
## #    0-----a-----b----1
## def rule221(element, rotation, edgenodes, newSkeleton, alpha):
##     n0, n1, n2 = baseNodes(element, rotation)
##     na = edgenodes[rotation][0]
##     nb = edgenodes[rotation][1]
##     nc = edgenodes[(rotation+1)%3][0]
##     nd = edgenodes[(rotation+1)%3][1]
##     ne = edgenodes[(rotation+2)%3][0]
##     pos = element.center()
##     nf = newSkeleton.newNode(pos.x, pos.y)
##     return (
##         newSkeleton.newElement(nodes=[n0, na, nf, ne], parents=[element]),
##         newSkeleton.newElement(nodes=[nf, nd, n2, ne], parents=[element]),
##         newSkeleton.newElement(nodes=[na, nb, nf], parents=[element]),
##         newSkeleton.newElement(nodes=[nf, nc, nd], parents=[element]),
##         newSkeleton.newElement(nodes=[nb, nc, nf], parents=[element]),
##         newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]))
## RefinementRule(liberalRuleSet, (2,2,1), rule221)

# Unrefined quadrilateral
def rule0000(element, rotation, edgenodes, newSkeleton, alpha):
    el = newSkeleton.newElement(nodes=baseNodes(element, rotation),
                                parents=[element])
    return (el,)
RefinementRule(conservativeRuleSet, (0,0,0,0), rule0000)

#  3-------------------2
#  |\                 /|
#  | \               / |
#  |  \             /  |
#  |   \           /   |
#  |    \         /    |
#  |     \       /     |
#  |      \     /      |
#  |       \   /       |
#  |        \ /        |
#  0---------a---------1

#  3-------------------2
#  |\                  |
#  | \                 |
#  |  \                |
#  |   \               |
#  |    \              |
#  |     \             |
#  |      \            |
#  |       \           |
#  |        \          |
#  0---------a---------1

#  3-------------------2
#  |                  /|
#  |                 / |
#  |                /  |
#  |               /   |
#  |              /    |
#  |             /     |
#  |            /      |
#  |           /       |
#  |          /        |
#  0---------a---------1

#  3-------------------2
#  |.                . |
#  |  .             .  |
#  |    .         .    |
#  |      .     .      |
#  |        . .        |
#  |         b         |
#  |         |         |
#  |         |         |
#  |         |         |
#  0---------a---------1
def rule1000(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    pos = element.frommaster(Point(0., 0.), rotation) 
    nb = newSkeleton.newNode(pos.x, pos.y)
    refine0 = ProvisionalRefinement(
        newbies = [ProvisionalTriangle(nodes=[n0, na, n3], parents=[element]),
                   ProvisionalTriangle(nodes=[na, n2, n3], parents=[element]),
                   ProvisionalTriangle(nodes=[na, n1, n2], parents=[element])])
    refine1 = ProvisionalRefinement(
        newbies = [ProvisionalTriangle(nodes=[n0, na, n3], parents=[element]),
                   ProvisionalQuad(nodes=[na, n1, n2, n3], parents=[element])])
    refine2 = ProvisionalRefinement(
        newbies = [ProvisionalTriangle(nodes=[na, n1, n2], parents=[element]),
                   ProvisionalQuad(nodes=[n0, na, n2, n3], parents=[element])])
    refine3 = ProvisionalRefinement(
        newbies = [ProvisionalTriangle(nodes=[nb, n2, n3], parents=[element]),
                   ProvisionalQuad(nodes=[n0, na, nb, n3], parents=[element]),
                   ProvisionalQuad(nodes=[na, n1, n2, nb], parents=[element])],
        internalNodes = [nb])
    return theBetter(newSkeleton, (refine0, refine1, refine2, refine3), alpha)
RefinementRule(conservativeRuleSet, (1,0,0,0), rule1000)

#  3----------2
#  |\         |
#  | \        |
#  |  \       |
#  |   \ c    |
#  |    ----- b
#  |    |     |
#  |    |     |
#  |    |     |
#  0----a-----1
def rule1100(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%4][0]
    pos = element.frommaster(Point(0., 0.), rotation) 
    nc = newSkeleton.newNode(pos.x, pos.y)
    return (
        newSkeleton.newElement(nodes=[n0, na, nc, n3], parents=[element]),
        newSkeleton.newElement(nodes=[na, n1, nb, nc], parents=[element]),
        newSkeleton.newElement(nodes=[nc, nb, n2, n3], parents=[element]))
RefinementRule(conservativeRuleSet, (1,1,0,0), rule1100)

#  3----------2
#  |\       / |
#  | \     /  |
#  |  \   /   |
#  |   \ c    |
#  |    ----- b
#  |   /|     |
#  |  / |     |
#  | /  |     |
#  0----a-----1
def rule1100(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%4][0]
    pos = element.frommaster(Point(0., 0.), rotation) 
    nc = newSkeleton.newNode(pos.x, pos.y)
    # refine0: conservative
    # refine1: the figure above
    refine0 = ProvisionalRefinement(
        newbies = [ProvisionalQuad(nodes=[n0, na, nc, n3], parents=[element]),
                   ProvisionalQuad(nodes=[na, n1, nb, nc], parents=[element]),
                   ProvisionalQuad(nodes=[nc, nb, n2, n3], parents=[element])],
        internalNodes = [nc])
    refine1 = ProvisionalRefinement(
        newbies = [ProvisionalQuad(nodes=[na, n1, nb, nc], parents=[element]),
                   ProvisionalTriangle(nodes=[n0, na, nc], parents=[element]),
                   ProvisionalTriangle(nodes=[n0, nc, n3], parents=[element]),
                   ProvisionalTriangle(nodes=[nc, n2, n3], parents=[element]),
                   ProvisionalTriangle(nodes=[nc, nb, n2], parents=[element])],
        internalNodes = [nc])
    return theBetter(newSkeleton, (refine0, refine1), alpha)
RefinementRule(liberalRuleSet, (1,1,0,0), rule1100)

#  3-----b-----2
#  |     |     |
#  |     |     |
#  |     |     |
#  |     |     |
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
RefinementRule(conservativeRuleSet, (1,0,1,0), rule1010)

#  3----c-----2
#  |    |     |
#  |    |     |
#  |    |     |
#  |    |_____|b 
#  |   /|d    |
#  |  / |     |
#  | /  |     |
#  |/   |     |
#  0----a-----1

#  3----c-----2
#  |\   |     |
#  | \  |     |
#  |  \ |     |
#  |   \|_____|b 
#  |    |d    |
#  |    |     |
#  |    |     |
#  |    |     |
#  0----a-----1

#  3----c-----2
#  |\   |     |
#  | \  |     |
#  |  \ |     |
#  |   \|_____|b 
#  |   /|d    |
#  |  / |     |
#  | /  |     |
#  |/   |     |
#  0----a-----1
def rule1110(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[(rotation+1)%4][0]
    nc = edgenodes[(rotation+2)%4][0]
    pos = element.frommaster(Point(0., 0.), rotation)
    nd = newSkeleton.newNode(pos.x, pos.y)
    refine0 = ProvisionalRefinement(
        newbies = [ProvisionalQuad(nodes=[na, n1, nb, nd], parents=[element]),
                   ProvisionalQuad(nodes=[nd, nb, n2, nc], parents=[element]),
                   ProvisionalQuad(nodes=[n0, nd, nc, n3], parents=[element]),
                   ProvisionalTriangle(nodes=[n0, na, nd], parents=[element])],
        internalNodes = [nd])
    refine1 = ProvisionalRefinement(
        newbies = [ProvisionalQuad(nodes=[na, n1, nb, nd], parents=[element]),
                   ProvisionalQuad(nodes=[nd, nb, n2, nc], parents=[element]),
                   ProvisionalQuad(nodes=[n0, na, nd, n3], parents=[element]),
                   ProvisionalTriangle(nodes=[nd, nc, n3], parents=[element])],
        internalNodes = [nd])    
    refine2 = ProvisionalRefinement(
        newbies = [ProvisionalQuad(nodes=[na, n1, nb, nd], parents=[element]),
                   ProvisionalQuad(nodes=[nd, nb, n2, nc], parents=[element]),
                   ProvisionalTriangle(nodes=[n0, na, nd], parents=[element]),
                   ProvisionalTriangle(nodes=[n0, nd, n3], parents=[element]),
                   ProvisionalTriangle(nodes=[nd, nc, n3], parents=[element])],
        internalNodes = [nd])                      
    return theBetter(newSkeleton, (refine0, refine1, refine2), alpha)
RefinementRule(conservativeRuleSet, (1,1,1,0), rule1110)

#  3-----c-----2
#  |     |     |
#  |     |     |
#  |     |     |
#  d_____e_____b
#  |     |     |
#  |     |     |
#  |     |     |
#  |     |     |
#  0-----a-----1

def rule1111(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[0][0]
    nb = edgenodes[1][0]
    nc = edgenodes[2][0]
    nd = edgenodes[3][0]
    pos = element.frommaster(Point(0., 0.), rotation)
    ne = newSkeleton.newNode(pos.x, pos.y)
    return (
        newSkeleton.newElement(nodes=[n0, na, ne, nd], parents=[element]),
        newSkeleton.newElement(nodes=[na, n1, nb, ne], parents=[element]),
        newSkeleton.newElement(nodes=[ne, nb, n2, nc], parents=[element]),
        newSkeleton.newElement(nodes=[nd, ne, nc, n3], parents=[element]))
RefinementRule(conservativeRuleSet, (1,1,1,1), rule1111)

#   3____________________2
#   |\                  /|
#   | \                / |
#   |  \              /  |
#   |   \            /   |
#   |    \c________d/    |
#   |     |        |     |
#   |     |        |     |
#   |     |        |     |
#   |     |        |     |
#   0-----a--------b-----1
def rule2000(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    pos = element.frommaster(Point(-onethird, 0.), rotation)
    nc = newSkeleton.newNode(pos.x, pos.y)
    pos = element.frommaster(Point(onethird, 0.), rotation)
    nd = newSkeleton.newNode(pos.x, pos.y)
    return (
        newSkeleton.newElement(nodes=[n0, na, nc, n3], parents=[element]),
        newSkeleton.newElement(nodes=[na, nb, nd, nc], parents=[element]),
        newSkeleton.newElement(nodes=[nb, n1, n2, nd], parents=[element]),
        newSkeleton.newElement(nodes=[nc, nd, n2, n3], parents=[element]))
RefinementRule(conservativeRuleSet, (2,0,0,0), rule2000)

#   3__________________________2
#   |\                        /|
#   | \                      / |
#   |  \                    /  |
#   |   \                  /   |
#   |    \                /    |
#   |     \              /     |
#   |      \            /      |
#   |       \          /       |
#   |        \        /        |
#   0---------a------b---------1

def rule2000L(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    pos = element.frommaster(Point(-onethird, 0.), rotation)
    nc = newSkeleton.newNode(pos.x, pos.y)
    pos = element.frommaster(Point(onethird, 0.), rotation)
    nd = newSkeleton.newNode(pos.x, pos.y)
    # refine0: conservative
    # refine1: the figure above
    refine0 = ProvisionalRefinement(
        newbies = [ProvisionalQuad(nodes=[n0, na, nc, n3], parents=[element]),
                   ProvisionalQuad(nodes=[na, nb, nd, nc], parents=[element]),
                   ProvisionalQuad(nodes=[nb, n1, n2, nd], parents=[element]),
                   ProvisionalQuad(nodes=[nc, nd, n2, n3], parents=[element])],
        internalNodes = [nc, nd])
    refine1 = ProvisionalRefinement(
        newbies = [ProvisionalQuad(nodes=[na, nb, n2, n3], parents=[element]),
                   ProvisionalTriangle(nodes=[n0, na, n3], parents=[element]),
                   ProvisionalTriangle(nodes=[nb, n1, n2], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1), alpha)
RefinementRule(liberalRuleSet, (2,0,0,0), rule2000L)

#   3______________2
#   |\             | 
#   | \            | 
#   |  \           |
#   |   f__________d
#   |   |\         |
#   |   | \        |
#   |   |  \       |
#   |   |   \      |
#   |   |    \     |
#   |   |     e____c
#   |   |     |    |
#   |   |     |    |
#   |   |     |    |
#   |   |     |    |
#   0---a-----b----1
def rule2200(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    pos = element.frommaster(Point(15./33.,-15./33.), rotation)
    ne = newSkeleton.newNode(pos.x, pos.y)
    pos = element.frommaster(Point(1./33.,-1./33.), rotation)
    nf = newSkeleton.newNode(pos.x, pos.y)
    return (
        newSkeleton.newElement(nodes=[n0, na, nf, n3], parents=[element]),
        newSkeleton.newElement(nodes=[na, nb, ne, nf], parents=[element]),
        newSkeleton.newElement(nodes=[nb, n1, nc, ne], parents=[element]),
        newSkeleton.newElement(nodes=[ne, nc, nd, nf], parents=[element]),
        newSkeleton.newElement(nodes=[nf, nd, n2, n3], parents=[element]))
RefinementRule(conservativeRuleSet, (2,2,0,0), rule2200)

#   3___d_____c____2
#   |   |     |    |
#   |   |     |    |
#   |   |     |    |
#   |   |     |    |
#   |   |     |    |
#   |   |     |    |
#   |   |     |    |
#   |   |     |    |
#   |   |     |    |
#   |   |     |    |
#   0---a-----b----1
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
RefinementRule(conservativeRuleSet, (2,0,2,0), rule2020)

#    3______f_____e________2
#    |      |     |        |
#    |      |     |        |
#    |      |     |        |
#    |      |     |        |
#    |      j_____i________d
#    |      /\     \       |
#    |     /  \     \      |
#    |    /    \     \     |
#    |   /      \g____h____c
#    |  /       /     |    |
#    | /       /      |    |
#    |/       /       |    |
#    0-------a--------b----1    
def rule2220(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+2)%4][0]
    nf = edgenodes[(rotation+2)%4][1]
    pos = element.frommaster(Point(-0.0588,-0.4902), rotation)
    ng = newSkeleton.newNode(pos.x, pos.y)
    pos = element.frommaster(Point(0.4118,-0.4020), rotation)
    nh = newSkeleton.newNode(pos.x, pos.y)
    pos = element.frommaster(Point(0.3725,0.2157), rotation)
    ni = newSkeleton.newNode(pos.x, pos.y)
    pos = element.frommaster(Point(-0.2549,-0.0686), rotation)
    nj = newSkeleton.newNode(pos.x, pos.y)
    return (
        newSkeleton.newElement(nodes=[n0, na, ng, nj], parents=[element]),
        newSkeleton.newElement(nodes=[na, nb, nh, ng], parents=[element]),
        newSkeleton.newElement(nodes=[nb, n1, nc, nh], parents=[element]),
        newSkeleton.newElement(nodes=[ng, nh, ni, nj], parents=[element]),
        newSkeleton.newElement(nodes=[nh, nc, nd, ni], parents=[element]),
        newSkeleton.newElement(nodes=[nj, ni, ne, nf], parents=[element]),
        newSkeleton.newElement(nodes=[ni, nd, n2, ne], parents=[element]),
        newSkeleton.newElement(nodes=[n0, nj, nf, n3], parents=[element]))
RefinementRule(conservativeRuleSet, (2,2,2,0), rule2220)

#    3______f_______e______2
#    |      |       |.     |
#    |      |       |  .   |
#    |      |       |    . |
#    |      |       |     .|
#    |      |       |      d
#    |      |       |      |
#    |      |       |      |
#    |      |       |      |
#    |      |       |      c
#    |      |       |     .|
#    |      |       |   .  |
#    |      |       | .    |
#    0------a-------b------1
def rule2220L(element, rotation, edgenodes, newSkeleton, alpha):
    n0, n1, n2, n3 = baseNodes(element, rotation)
    na = edgenodes[rotation][0]
    nb = edgenodes[rotation][1]
    nc = edgenodes[(rotation+1)%4][0]
    nd = edgenodes[(rotation+1)%4][1]
    ne = edgenodes[(rotation+2)%4][0]
    nf = edgenodes[(rotation+2)%4][1]
    pos = element.frommaster(Point(-0.0588,-0.4902), rotation)
    ng = newSkeleton.newNode(pos.x, pos.y)
    pos = element.frommaster(Point(0.4118,-0.4020), rotation)
    nh = newSkeleton.newNode(pos.x, pos.y)
    pos = element.frommaster(Point(0.3725,0.2157), rotation)
    ni = newSkeleton.newNode(pos.x, pos.y)
    pos = element.frommaster(Point(-0.2549,-0.0686), rotation)
    nj = newSkeleton.newNode(pos.x, pos.y)
    # refine0: conservative
    # refine1: the figure above
    refine0 = ProvisionalRefinement(
        newbies =[ProvisionalQuad(nodes=[n0, na, ng, nj], parents=[element]),
                  ProvisionalQuad(nodes=[na, nb, nh, ng], parents=[element]),
                  ProvisionalQuad(nodes=[nb, n1, nc, nh], parents=[element]),
                  ProvisionalQuad(nodes=[ng, nh, ni, nj], parents=[element]),
                  ProvisionalQuad(nodes=[nh, nc, nd, ni], parents=[element]),
                  ProvisionalQuad(nodes=[nj, ni, ne, nf], parents=[element]),
                  ProvisionalQuad(nodes=[ni, nd, n2, ne], parents=[element]),
                  ProvisionalQuad(nodes=[n0, nj, nf, n3], parents=[element])],
        internalNodes = [ng, nh, ni, nj])
    refine1 = ProvisionalRefinement(
        newbies =[ProvisionalQuad(nodes=[n0, na, nf, n3], parents=[element]),
                  ProvisionalQuad(nodes=[na, nb, ne, nf], parents=[element]),
                  ProvisionalQuad(nodes=[nb, nc, nd, ne], parents=[element]),
                  ProvisionalTriangle(nodes=[nb, n1, nc], parents=[element]),
                  ProvisionalTriangle(nodes=[nd, n2, ne], parents=[element])])
    return theBetter(newSkeleton, (refine0, refine1), alpha)
RefinementRule(liberalRuleSet, (2,2,2,0), rule2220L)

#   3_____f_____e______2
#   |     |     |      | 
#   |     |     |      | 
#   g_____l_____k______d
#   |     |     |      |
#   |     |     |      |
#   h_____i_____j______c
#   |     |     |      |
#   |     |     |      |
#   0_____a_____b______1
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
    pos = element.frommaster(Point(-onethird,-onethird), rotation)
    ni = newSkeleton.newNode(pos.x, pos.y)
    pos = element.frommaster(Point(onethird,-onethird), rotation)
    nj = newSkeleton.newNode(pos.x, pos.y)
    pos = element.frommaster(Point(onethird,onethird), rotation)
    nk = newSkeleton.newNode(pos.x, pos.y)
    pos = element.frommaster(Point(-onethird,onethird), rotation)
    nl = newSkeleton.newNode(pos.x, pos.y)
    return (
        newSkeleton.newElement(nodes=[n0, na, ni, nh], parents=[element]),
        newSkeleton.newElement(nodes=[na, nb, nj, ni], parents=[element]),
        newSkeleton.newElement(nodes=[nb, n1, nc, nj], parents=[element]),
        newSkeleton.newElement(nodes=[nh, ni, nl, ng], parents=[element]),
        newSkeleton.newElement(nodes=[ni, nj, nk, nl], parents=[element]),
        newSkeleton.newElement(nodes=[nj, nc, nd, nk], parents=[element]),
        newSkeleton.newElement(nodes=[ng, nl, nf, n3], parents=[element]),
        newSkeleton.newElement(nodes=[nl, nk, ne, nf], parents=[element]),
        newSkeleton.newElement(nodes=[nk, nd, n2, ne], parents=[element]))
RefinementRule(conservativeRuleSet, (2,2,2,2), rule2222)  

## #   3__________d_________2
## #   |         /\         |
## #   |        /  \        |
## #   |       /    \       |
## #   |      /      \      |
## #   e____ f________g_____c
## #   |     |        |     |
## #   |     |        |     |
## #   |     |        |     |
## #   |     |        |     |
## #   0-----a--------b-----1
## def rule2111(element, rotation, edgenodes, newSkeleton, alpha):
##     n0, n1, n2, n3 = baseNodes(element, rotation)
##     na = edgenodes[rotation][0]
##     nb = edgenodes[rotation][1]
##     nc = edgenodes[(rotation+1)%4][0]
##     nd = edgenodes[(rotation+2)%4][0]
##     ne = edgenodes[(rotation+3)%4][0]
##     pos = element.frommaster(Point(-4./15.,0.), rotation)
##     nf = newSkeleton.newNode(pos.x, pos.y)
##     pos = element.frommaster(Point(4./15.,0.), rotation)
##     ng = newSkeleton.newNode(pos.x, pos.y)
##     return (
##         newSkeleton.newElement(nodes=[n0, na, nf, ne], parents=[element]),
##         newSkeleton.newElement(nodes=[na, nb, ng, nf], parents=[element]),
##         newSkeleton.newElement(nodes=[nb, n1, nc, ng], parents=[element]),
##         newSkeleton.newElement(nodes=[ne, nf, nd, n3], parents=[element]),
##         newSkeleton.newElement(nodes=[nf, ng, nd], parents=[element]),
##         newSkeleton.newElement(nodes=[ng, nc, n2, nd], parents=[element]))
## RefinementRule(conservativeRuleSet, (2,1,1,1), rule2111)

## #   3_____e______________2
## #   |     |              |
## #   |     |              |
## #   f_____|g_____________d
## #   |     |\             |
## #   |     | \            |
## #   |     |  \           |
## #   |     |   \          |
## #   |     |    h---------c
## #   |     |    |         |
## #   |     |    |         |
## #   0-----a----b---------1
## def rule2211(element, rotation, edgenodes, newSkeleton, alpha):
##     n0, n1, n2, n3 = baseNodes(element, rotation)
##     na = edgenodes[rotation][0]
##     nb = edgenodes[rotation][1]
##     nc = edgenodes[(rotation+1)%4][0]
##     nd = edgenodes[(rotation+1)%4][1]
##     ne = edgenodes[(rotation+2)%4][0]
##     nf = edgenodes[(rotation+3)%4][0]
##     pos = element.frommaster(Point(1./42.,-1./42.), rotation)
##     ng = newSkeleton.newNode(pos.x, pos.y)
##     pos = element.frommaster(Point(19./42.,-19./42.), rotation)
##     nh = newSkeleton.newNode(pos.x, pos.y)
##     return (
##         newSkeleton.newElement(nodes=[n0, na, ng, nf], parents=[element]),
##         newSkeleton.newElement(nodes=[na, nb, nh, ng], parents=[element]),
##         newSkeleton.newElement(nodes=[nb, n1, nc, nh], parents=[element]),
##         newSkeleton.newElement(nodes=[nh, nc, nd, ng], parents=[element]),
##         newSkeleton.newElement(nodes=[nf, ng, ne, n3], parents=[element]),
##         newSkeleton.newElement(nodes=[ng, nd, n2, ne], parents=[element]))
## RefinementRule(conservativeRuleSet, (2,2,1,1), rule2211)

## #   3_____e_____d______2
## #   |     |     |      |
## #   |     |     |      |
## #   |     |     |      |
## #   f_____g_____h______c
## #   |     |     |      |
## #   |     |     |      |
## #   |     |     |      |
## #   |     |     |      |
## #   0_____a_____b______1
## def rule2121(element, rotation, edgenodes, newSkeleton, alpha):
##     n0, n1, n2, n3 = baseNodes(element, rotation)
##     na = edgenodes[rotation][0]
##     nb = edgenodes[rotation][1]
##     nc = edgenodes[(rotation+1)%4][0]
##     nd = edgenodes[(rotation+2)%4][0]
##     ne = edgenodes[(rotation+2)%4][1]
##     nf = edgenodes[(rotation+3)%4][0]
##     pos = element.frommaster(Point(-onethird,0.), rotation)
##     ng = newSkeleton.newNode(pos.x, pos.y)
##     pos = element.frommaster(Point(onethird,0.), rotation)
##     nh = newSkeleton.newNode(pos.x, pos.y)
##     return (
##         newSkeleton.newElement(nodes=[n0, na, ng, nf], parents=[element]),
##         newSkeleton.newElement(nodes=[na, nb, nh, ng], parents=[element]),
##         newSkeleton.newElement(nodes=[nb, n1, nc, nh], parents=[element]),
##         newSkeleton.newElement(nodes=[nf, ng, ne, n3], parents=[element]),
##         newSkeleton.newElement(nodes=[ng, nh, nd, ne], parents=[element]),
##         newSkeleton.newElement(nodes=[nh, nc, n2, nd], parents=[element]))
## RefinementRule(conservativeRuleSet, (2,1,2,1), rule2121)

## #   3_____f_____e______2
## #   |     |     |      |
## #   |     |     |      |
## #   |     |     i______d
## #   |     |    /|      |
## #   |     |   / |      |
## #   |     |  /  |      |
## #   |     | /   |      |
## #   g_____j/    |      |
## #   |     |\    |      |
## #   |     | \   |      |
## #   |     |  \  |      |
## #   |     |   \ |      |
## #   |     |    \h______c
## #   |     |     |      |
## #   |     |     |      |
## #   0_____a_____b______1
## def rule2221(element, rotation, edgenodes, newSkeleton, alpha):
##     n0, n1, n2, n3 = baseNodes(element, rotation)
##     na = edgenodes[rotation][0]
##     nb = edgenodes[rotation][1]
##     nc = edgenodes[(rotation+1)%4][0]
##     nd = edgenodes[(rotation+1)%4][1]
##     ne = edgenodes[(rotation+2)%4][0]
##     nf = edgenodes[(rotation+2)%4][1]
##     ng = edgenodes[(rotation+3)%4][0]
##     pos = element.frommaster(Point(0.3846,-0.2667), rotation)
##     nh = newSkeleton.newNode(pos.x, pos.y)
##     pos = element.frommaster(Point(0.3846,0.2667), rotation)
##     ni = newSkeleton.newNode(pos.x, pos.y)
##     pos = element.frommaster(Point(-0.1795,0.), rotation)
##     nj = newSkeleton.newNode(pos.x, pos.y)
##     return (
##         newSkeleton.newElement(nodes=[n0, na, nj, ng], parents=[element]),
##         newSkeleton.newElement(nodes=[na, nb, nh, nj], parents=[element]),
##         newSkeleton.newElement(nodes=[nb, n1, nc, nh], parents=[element]),
##         newSkeleton.newElement(nodes=[nh, ni, nj], parents=[element]),
##         newSkeleton.newElement(nodes=[nh, nc, nd, ni], parents=[element]),
##         newSkeleton.newElement(nodes=[ng, nj, nf, n3], parents=[element]),
##         newSkeleton.newElement(nodes=[nj, ni, ne, nf], parents=[element]),
##         newSkeleton.newElement(nodes=[ni, nd, n2, ne], parents=[element]))
## RefinementRule(conservativeRuleSet, (2,2,2,1), rule2221)


