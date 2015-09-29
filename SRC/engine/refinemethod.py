# -*- python -*-
# $RCSfile: refinemethod.py,v $
# $Author: langer $
# $Date: 2010/12/07 21:57:03 $
# $Revision: 1.43 $

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

if config.dimension() == 2:
    from ooflib.engine import skeletonelement
    ProvisionalQuad = skeletonelement.ProvisionalQuad
    ProvisionalTriangle = skeletonelement.ProvisionalTriangle
elif config.dimension() == 3:
    from ooflib.engine import skeletonelement3d
    ProvisionalTetra = skeletonelement3d.ProvisionalTetra
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
        if config.dimension() == 2:
            self.rules[signature] = rule
        if config.dimension() == 3:
            for sig in signature:
                self.rules[sig] = rule
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
        if config.dimension() == 2:
            # in 2D, the first member of the signature_info is the rotation
            newels = self.function(element, signature_info[0], edgenodes, newSkeleton, alpha)
        elif config.dimension() == 3:
            newels = self.function(element, signature_info, edgenodes, newSkeleton, alpha)
        return newels

##########################################

# This function is called with an old element and an integer
# 'rotation'.  It returns copies (children in the SkeletonSelectable
# sense) of the nodes of the old element, with the order shifted
# around by the rotation.  The new refined elements will be built from
# these base nodes.

if config.dimension() == 2:
    def baseNodes(element, rotation):
        nnodes = element.nnodes()
        return [element.nodes[(i+rotation)%nnodes].children[-1]
                for i in range(nnodes)]
elif config.dimension() == 3:
    def baseNodes(element):
        nnodes = element.nnodes()
        return [element.nodes[i].children[-1]
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

if config.dimension() == 2:
    liberalRuleSet = RefinementRuleSet(
        'liberal',
        parent='conservative',
        help="If there's a choice, choose the refinement that minimizes E, without trying to preserve topology.")

##########################################

#            BEGIN 2D RULES

##########################################


if config.dimension() == 2:
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
    # SwapEdges routine in 2D. For now, the tetrahedral rules do not
    # use this either in order to keep the face matching problem
    # simple.
    
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


##########################################

#             END 2D RULES

#            BEGIN 3D RULES

##########################################


# For bisection, triangular faces with two edge markings have two
# possibilities for sub-triangularization which are both essential.
# Triangular faces with three edge markings have four possibilities,
# but it is possible to leave out three (see above) - each of the
# rules that have a face with three markings can be tetrahedralized in
# such a way that only one triangulation is used.  For the rules that
# have multiple possibilities for face triangulation (any rule that
# has one or more faces with two edge markings: twoEdgeAdjacent,
# fourEdges1, fourEdges2, and fiveEdges, threeEdgeZigZag) we need to
# get the face triangulation of any neighbors that have already been
# tetrahedralized and choose a rule that is consistent.  Certain face
# triangulations can only be tetrahedralized by adding a point in the
# middle.  We want to avoid this, so these rules are given priority so
# that the "deadlocking" is less likely.  The rules subject to this
# are fourEdges2 and threeEdgesOnePoint (possibly others - check
# this).



elif config.dimension() == 3:

    def nullRule(element, signature, edgenodes, newSkeleton, alpha):
        el = newSkeleton.newElement(nodes=baseNodes(element),
                                    parents=[element])
        return (el,)
    RefinementRule(conservativeRuleSet, [()], nullRule)


    def singleEdge(element, signature, edgenodes, newSkeleton, alpha):
        ne = edgenodes[signature[0]][0]
        bNodes = baseNodes(element)
        idxs = element.segToNodeMap()[signature[0]]
        nodes1 = bNodes[:]
        nodes1[idxs[0]] = ne
        nodes2 = bNodes[:]
        nodes2[idxs[1]] = ne
        el1 = newSkeleton.newElement(nodes1, parents=[element])
        el2 = newSkeleton.newElement(nodes2, parents=[element])
        return (el1,el2)
    RefinementRule(conservativeRuleSet, [(0,),(1,),(2,),(3,),(4,),(5,)], singleEdge)

    def twoEdgeAdjacent(element, signature, edgenodes, newSkeleton, alpha):
        en0 = edgenodes[signature[0]][0]
        en1 = edgenodes[signature[1]][0]
        idxs = list(element.segToNodeMap()[signature[0]])
        idxs2 = list(element.segToNodeMap()[signature[1]])
        if idxs[0] in idxs2:
            idxs.reverse()
        for id in idxs2:
            if id not in idxs:
                idxs.append(id)
        bNodes = baseNodes(element)
        seg1 = newSkeleton.findSegment(en0,bNodes[idxs[2]])
        seg2 = newSkeleton.findSegment(bNodes[idxs[0]],en1)
        if seg1 is not None and seg2 is not None:
            raise ooferror.ErrPyProgrammingError("inconsistent refinement on tet face")
        refine = []
        # tet0 is in both possible refinements
        nodes0 = bNodes[:]
        nodes0[idxs[0]] = en0
        nodes0[idxs[2]] = en1
        tet0 = ProvisionalTetra(nodes=nodes0, parents=[element])
        if seg2 is None:
            nodes1 = bNodes[:]
            nodes1[idxs[1]] = en0
            tet1 = ProvisionalTetra(nodes=nodes1, parents=[element])
            nodes2 = bNodes[:]
            nodes2[idxs[0]] = en0
            nodes2[idxs[1]] = en1
            tet2 = ProvisionalTetra(nodes=nodes2, parents=[element])
            refine.append(ProvisionalRefinement(newbies=[tet0, tet1, tet2]))
        if seg1 is None:
            nodes3 = bNodes[:]
            nodes3[idxs[1]] = en1
            tet3 = ProvisionalTetra(nodes=nodes3, parents=[element])
            nodes4 = bNodes[:]
            nodes4[idxs[1]] = en0
            nodes4[idxs[2]] = en1
            tet4 = ProvisionalTetra(nodes=nodes4, parents=[element])
            refine.append(ProvisionalRefinement(newbies=[tet0, tet3, tet4]))
        return theBetter(newSkeleton, tuple(refine), alpha)
    RefinementRule(conservativeRuleSet, [(0,1), (0,2), (0,3), (0,4), (1,2), (1,4),
                                         (1,5), (2,3), (2,5), (3,4), (3,5), (4,5)],
                   twoEdgeAdjacent)


    def twoEdgeOpposite(element, signature, edgenodes, newSkeleton, alpha):
        ne0 = edgenodes[signature[0]][0]
        ne1 = edgenodes[signature[1]][0]
        idxs = list(element.segToNodeMap()[signature[0]])
        idxs.extend(list(element.segToNodeMap()[signature[1]]))
        bNodes = baseNodes(element)
        nodes0 = bNodes[:]
        nodes0[idxs[0]] = ne0
        nodes0[idxs[2]] = ne1
        el0 = newSkeleton.newElement(nodes=nodes0, parents=[element])
        nodes1 = bNodes[:]
        nodes1[idxs[0]] = ne0
        nodes1[idxs[3]] = ne1
        el1 = newSkeleton.newElement(nodes=nodes1, parents=[element])
        nodes2 = bNodes[:]
        nodes2[idxs[1]] = ne0
        nodes2[idxs[2]] = ne1
        el2 = newSkeleton.newElement(nodes=nodes2, parents=[element])
        nodes3 = bNodes[:]
        nodes3[idxs[1]] = ne0
        nodes3[idxs[3]] = ne1
        el3 = newSkeleton.newElement(nodes=nodes3, parents=[element])
        return (el0,el1,el2,el3)
    RefinementRule(conservativeRuleSet, [(0,5), (1,3), (2,4)], twoEdgeOpposite)


    def threeEdgeTriangle(element, signature, edgenodes, newSkeleton, alpha):
        ne0 = edgenodes[signature[0]][0]
        ne1 = edgenodes[signature[1]][0]
        ne2 = edgenodes[signature[2]][0]
        idxs = list(element.segToNodeMap()[signature[0]])
        idxs2 = list(element.segToNodeMap()[signature[1]])
        if idxs[0] in idxs2:
            idxs.reverse()
        for id in idxs2:
            if id not in idxs:
                idxs.append(id)
        bNodes = baseNodes(element)
        nodes0 = bNodes[:]
        nodes0[idxs[1]] = ne0
        nodes0[idxs[2]] = ne2
        el0 = newSkeleton.newElement(nodes=nodes0, parents=[element])
        nodes1 = bNodes[:]
        nodes1[idxs[0]] = ne0
        nodes1[idxs[2]] = ne1
        el1 = newSkeleton.newElement(nodes=nodes1, parents=[element])
        nodes2 = bNodes[:]
        nodes2[idxs[0]] = ne2
        nodes2[idxs[1]] = ne0
        nodes2[idxs[2]] = ne1
        el2 = newSkeleton.newElement(nodes=nodes2, parents=[element])
        nodes3 = bNodes[:]
        nodes3[idxs[0]] = ne2
        nodes3[idxs[1]] = ne1
        el3 = newSkeleton.newElement(nodes=nodes3, parents=[element])
        return (el0,el1,el2,el3)
        # The following refinements use the alternative triangulation
        # of a face with three marked edges
        # refine0 = ProvisionalRefinement(newbies=[el0,el1,el2,el3])
        # nodes4 = bNodes[:]
        # nodes4[idxs[0]] = ne0
        # nodes4[idxs[1]] = ne1
        # el4 = ProvisionalTetra(nodes=nodes4, parents=[element])
        # nodes5 = bNodes[:]
        # nodes5[idxs[0]] = ne2
        # nodes5[idxs[1]] = ne0
        # el5 = ProvisionalTetra(nodes=nodes5, parents=[element])
        # refine1 = ProvisionalRefinement(newbies=[el4,el5,el0,el1])
        # nodes6 = bNodes[:]
        # nodes6[idxs[0]] = ne0
        # nodes6[idxs[2]] = ne2
        # el6 = ProvisionalTetra(nodes=nodes6, parents=[element])
        # nodes7 = bNodes[:]
        # nodes7[idxs[0]] = ne2
        # nodes7[idxs[2]] = ne1
        # el7 = ProvisionalTetra(nodes=nodes7, parents=[element])
        # refine2 = ProvisionalRefinement(newbies=[el6,el7,el0,el3])
        # nodes8 = bNodes[:]
        # nodes8[idxs[1]] = ne0
        # nodes8[idxs[2]] = ne1
        # el8 = ProvisionalTetra(nodes=nodes8, parents=[element])
        # nodes9 = bNodes[:]
        # nodes9[idxs[1]] = ne1
        # nodes9[idxs[2]] = ne2
        # el9 = ProvisionalTetra(nodes=nodes9, parents=[element])
        # refine3 = ProvisionalRefinement(newbies=[el8,el9,el1,el3])
        # return theBetter(newSkeleton, (refine0,refine1,refine2,refine3), alpha)
    RefinementRule(conservativeRuleSet, [(0,3,4), (0,1,2), (2,3,5), (1,4,5)],
                   threeEdgeTriangle)


    def threeEdgeZigZag(element, signature, edgenodes, newSkeleton, alpha):
        # we want the nodes and transition points in a particular
        # topological order, but the signature gives the affected
        # segments in numerical order.
        if signature in [(0,2,4),(0,1,3),(1,2,4)]:
            # the first segment is the middle segment
            signature = (signature[1],signature[0],signature[2])
        #if signature in [(0,1,5),(0,2,5),(1,2,3),(0,3,5),(2,3,4),(0,4,5)]:
            # the second segment is the middle segment - leave the signature in order
        if signature in [(1,3,4),(1,3,5),(2,4,5)]:
            # the last segment is the middle segment
            signature = (signature[0],signature[2],signature[1])
        ne = [edgenodes[signature[i]][0] for i in range(3)]
        idxs = list(element.segToNodeMap()[signature[0]])
        idxs2 = list(element.segToNodeMap()[signature[1]])
        if idxs[0] in idxs2:
            idxs.reverse()
        idxs2.extend(element.segToNodeMap()[signature[2]])
        for idx in idxs2:
            if idx not in idxs:
                idxs.append(idx)
        bNodes = baseNodes(element)
        seg1 = newSkeleton.findSegment(ne[1],bNodes[idxs[3]])
        seg2 = newSkeleton.findSegment(ne[2],bNodes[idxs[1]])
        seg3 = newSkeleton.findSegment(ne[1],bNodes[idxs[0]])
        seg4 = newSkeleton.findSegment(ne[0],bNodes[idxs[2]])
        if (seg1 is not None and seg2 is not None) or \
                (seg3 is not None and seg4 is not None):
            raise ooferror.ErrPyProgrammingError("inconsistent refinement on tet face")
        refine = []
        # tet0 is in all of the possible refinements
        nodes0 = bNodes[:]
        nodes0[idxs[1]] = ne[0]
        nodes0[idxs[2]] = ne[2]
        tet0 = ProvisionalTetra(nodes=nodes0, parents=[element])
        if seg1 is None:
            nodes1 = bNodes[:]
            nodes1[idxs[0]] = ne[0]
            nodes1[idxs[2]] = ne[2]
            tet1 = ProvisionalTetra(nodes=nodes1, parents=[element])
            nodes2 = bNodes[:]
            nodes2[idxs[0]] = ne[0]
            nodes2[idxs[2]] = ne[1]
            nodes2[idxs[3]] = ne[2]
            tet2 = ProvisionalTetra(nodes=nodes2, parents=[element])
            newbies1 = [tet0,tet1,tet2]
        if seg2 is None:
            nodes3 = bNodes[:]
            nodes3[idxs[0]] = ne[0]
            nodes3[idxs[2]] = ne[1]
            tet3 = ProvisionalTetra(nodes=nodes3, parents=[element])
            nodes4 = bNodes[:]
            nodes4[idxs[0]] = ne[0]
            nodes4[idxs[1]] = ne[1]
            nodes4[idxs[2]] = ne[2]
            tet4 = ProvisionalTetra(nodes=nodes4, parents=[element])
            newbies2 = [tet0,tet3,tet4]
        if seg3 is None:
            nodes5 = bNodes[:]
            nodes5[idxs[0]] = ne[0]
            nodes5[idxs[1]] = ne[1]
            nodes5[idxs[3]] = ne[2]
            tet5 = ProvisionalTetra(nodes=nodes5, parents=[element])
            nodes6 = bNodes[:]
            nodes6[idxs[1]] = ne[0]
            nodes6[idxs[3]] = ne[2]
            tet6 = ProvisionalTetra(nodes=nodes6, parents=[element])
            newbies3 = [tet5,tet6]
            if seg1 is None:
                refine.append(ProvisionalRefinement(newbies=(newbies1+newbies3)))
            if seg2 is None:
                refine.append(ProvisionalRefinement(newbies=(newbies2+newbies3)))
        if seg4 is None:
            nodes7 = bNodes[:]
            nodes7[idxs[1]] = ne[0]
            nodes7[idxs[2]] = ne[1]
            nodes7[idxs[3]] = ne[2]
            tet7 = ProvisionalTetra(nodes=nodes7, parents=[element])
            nodes8 = bNodes[:]
            nodes8[idxs[1]] = ne[1]
            nodes8[idxs[3]] = ne[2]
            tet8 = ProvisionalTetra(nodes=nodes8, parents=[element])
            newbies4 = [tet7,tet8]
            if seg1 is None:
                refine.append(ProvisionalRefinement(newbies=(newbies1+newbies4)))
            if seg2 is None:
                refine.append(ProvisionalRefinement(newbies=(newbies2+newbies4)))
        return theBetter(newSkeleton, tuple(refine), alpha)
    RefinementRule(conservativeRuleSet, [(0,2,4), (0,1,5), (0,1,3), (1,2,4), (0,2,5), 
                                         (1,2,3), (1,3,5), (2,3,4), (0,4,5), (1,3,4), 
                                         (0,3,5), (2,4,5)], threeEdgeZigZag)


    def threeEdgeOnePoint(element, signature, edgenodes, newSkeleton, alpha):
        # We want the basenodes in a particular order and we need the
        # signature to match.  The first three nodes are on the
        # segments given by the signature, respective.  These must be
        # in an order which defines a normal pointing towards the
        # fourth node.
        if signature == (3,4,5):
            idxs = (0,1,2,3)
        if signature == (0,1,4):
            idxs = (0,2,3,1)
        if signature == (0,2,3):
            idxs = (1,3,2,0)
            signature = (0,3,2)
        if signature == (1,2,5):
            idxs = (1,0,3,2)
        ne = [edgenodes[signature[i]][0] for i in range(3)]
        bNodes1 = baseNodes(element)
        bNodes = [bNodes1[i] for i in idxs]        

        segA = [newSkeleton.findSegment(ne[0],bNodes[1]),
                newSkeleton.findSegment(ne[1],bNodes[2]),
                newSkeleton.findSegment(ne[2],bNodes[0])]
        segB = [newSkeleton.findSegment(ne[1],bNodes[0]),
                newSkeleton.findSegment(ne[2],bNodes[1]),
                newSkeleton.findSegment(ne[0],bNodes[2])]

        # the top tet - this one is in all of the possible refinements
        # for this rule
        kingtet = ProvisionalTetra(nodes=[ne[0],ne[1],ne[2],bNodes[3]], parents=[element])
        refine = []

        # There are two basic cases: all segments can tilt the same
        # way (all A or all B - leading to the need for an internal
        # node) or one out of the three is different
        
        # the one in three is different cases:
        for i in range(3):
            if segA[(i+2)%3] is None and segB[i] is None:
                tet1 = ProvisionalTetra(nodes=[bNodes[0],bNodes[1],bNodes[2],ne[i]], parents=[element])
                if segB[(i+1)%3] is None:
                    nodes2 = bNodes[:]
                    nodes2[3] = ne[(i+1)%3]
                    nodes2[i] = ne[i]
                    tet2 = ProvisionalTetra(nodes=nodes2, parents=[element])
                    nodes3 = bNodes[:]
                    nodes3[3] = ne[(i+2)%3]
                    nodes3[i] = ne[i]
                    nodes3[(i+1)%3] = ne[(i+1)%3]
                    tet3 = ProvisionalTetra(nodes=nodes3, parents=[element])
                    refine.append(ProvisionalRefinement(newbies=[kingtet,tet1,tet2,tet3]))
                if segA[(i+1)%3] is None:
                    nodes4 = bNodes[:]
                    nodes4[3] = ne[(i+2)%3]
                    nodes4[i] = ne[i]
                    tet4 = ProvisionalTetra(nodes=nodes4, parents=[element])
                    nodes5 = bNodes[:]
                    nodes5[3] = ne[(i+1)%3]
                    nodes5[i] = ne[i]
                    nodes5[(i+2)%3] = ne[(i+2)%3]
                    tet5 = ProvisionalTetra(nodes=nodes5, parents=[element])
                    refine.append(ProvisionalRefinement(newbies=[kingtet,tet1,tet4,tet5]))
                    
        if len(refine) == 0: 
            pos = (bNodes[0].position()+bNodes[1].position()+bNodes[2].position()+\
                       ne[0].position()+ne[1].position()+ne[2].position())/6
            nc = newSkeleton.newNode(pos.x,pos.y,pos.z)
            tet6 = ProvisionalTetra(nodes=[bNodes[0],bNodes[1],bNodes[2],nc], parents=[element])
            tet7 = ProvisionalTetra(nodes=[ne[2],ne[1],ne[0],nc], parents=[element])
            tets = [kingtet,tet6,tet7]

            if segA[0] is not None and segA[1] is not None and segA[2] is not None:
                tets.append(ProvisionalTetra(nodes=[bNodes[0],ne[0],bNodes[1],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[ne[0],ne[1],bNodes[1],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[bNodes[1],ne[1],bNodes[2],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[bNodes[2],ne[1],ne[2],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[bNodes[2],ne[2],bNodes[0],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[ne[2],ne[0],bNodes[0],nc], parents=[element]))

            if segB[0] is not None and segB[1] is not None and segB[2] is not None:
                tets.append(ProvisionalTetra(nodes=[ne[0],ne[1],bNodes[0],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[bNodes[0],ne[1],bNodes[1],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[bNodes[1],ne[1],ne[2],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[bNodes[1],ne[2],bNodes[2],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[bNodes[2],ne[2],ne[0],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[ne[0],bNodes[0],bNodes[2],nc], parents=[element]))
            refine.append(ProvisionalRefinement(newbies=tets))

        return theBetter(newSkeleton, tuple(refine), alpha)
    RefinementRule(conservativeRuleSet, [(3,4,5), (0,1,4), (0,2,3), (1,2,5)],
                   threeEdgeOnePoint)


    def fourEdges1(element, signature, edgenodes, newSkeleton, alpha):
        # we want the nodes and transition points in a particular
        # topological order, but the signature gives the affected
        # segments in numerical order.  The segment that's not on the
        # face with the other three must be first and the three that
        # form a face must in an order such that they define a normal
        # that points in the direction of the fourth point.
        if signature == (0,1,3,4):
            signature = (1,0,3,4)
        if signature == (0,2,3,4):
            signature = (2,3,4,0)
        if signature == (0,3,4,5):
            signature = (5,4,0,3)
        if signature == (0,1,4,5):
            signature = (0,4,5,1)
        if signature == (1,2,4,5):
            signature = (2,1,4,5)
        if signature == (1,3,4,5):
            signature = (3,5,1,4)
        if signature == (0,2,3,5):
            signature = (0,2,5,3)
        if signature == (1,2,3,5):
            signature = (1,5,3,2)
        if signature == (2,3,4,5):
            signature = (4,3,2,5)
        if signature == (0,1,2,3):
            signature = (3,0,1,2)
        if signature == (0,1,2,4):
            signature = (4,1,2,0)
        if signature == (0,1,2,5):
            signature = (5,2,0,1)
        ne = [edgenodes[signature[i]][0] for i in range(4)]
        bNodes = baseNodes(element)
        idxs = list(element.segToNodeMap()[signature[0]])
        idxs2 = list(element.segToNodeMap()[signature[1]])
        if idxs[0] in idxs2:
            idxs.reverse()
        idxs2.extend(element.segToNodeMap()[signature[2]])
        for idx in idxs2:
            if idx not in idxs:
                idxs.append(idx)
        # TODO 3D: Here and in snapnodes, clean up code putting things
        # in order, we can reorder bNodes instead of doing [] in a []


        # tet0 and tet1 are in all possible refinements for this rule
        tet0 = ProvisionalTetra(nodes=[bNodes[idxs[1]],ne[1],ne[3],ne[0]], parents=[element])
        tet1 = ProvisionalTetra(nodes=[ne[1],ne[2],ne[3],ne[0]], parents=[element])

        seg1 = newSkeleton.findSegment(ne[0],bNodes[idxs[2]])
        seg2 = newSkeleton.findSegment(ne[1],bNodes[idxs[0]])
        seg3 = newSkeleton.findSegment(ne[0],bNodes[idxs[3]])
        seg4 = newSkeleton.findSegment(ne[3],bNodes[idxs[0]])

        refine = []
        
        if seg1 is None:
            tet2 = ProvisionalTetra(nodes=[bNodes[idxs[0]],ne[1],ne[0],ne[2]], parents=[element])
            tet3 = ProvisionalTetra(nodes=[bNodes[idxs[0]],bNodes[idxs[2]],ne[1],ne[2]], parents=[element])
            newbies1 = [tet0,tet1,tet2,tet3]
        if seg2 is None:
            tet4 = ProvisionalTetra(nodes=[bNodes[idxs[2]],ne[1],ne[0],ne[2]], parents=[element])
            tet5 = ProvisionalTetra(nodes=[bNodes[idxs[0]],bNodes[idxs[2]],ne[0],ne[2]], parents=[element])
            newbies2 = [tet0,tet1,tet4,tet5]
        if seg3 is None:
            tet6 = ProvisionalTetra(nodes=[ne[3],bNodes[idxs[3]],bNodes[idxs[0]],ne[2]], parents=[element])
            tet7 = ProvisionalTetra(nodes=[ne[0],ne[3],bNodes[idxs[0]],ne[2]], parents=[element])
            newbies3 = [tet6,tet7]
            if seg1 is None:
                refine.append(ProvisionalRefinement(newbies=(newbies1+newbies3)))
            if seg2 is None:
                refine.append(ProvisionalRefinement(newbies=(newbies2+newbies3)))
        if seg4 is None:
            tet8 = ProvisionalTetra(nodes=[ne[3],bNodes[idxs[3]],ne[0],ne[2]], parents=[element])
            tet9 = ProvisionalTetra(nodes=[ne[0],bNodes[idxs[3]],bNodes[idxs[0]],ne[2]], parents=[element])
            newbies4 = [tet8,tet9]
            if seg1 is None:
                refine.append(ProvisionalRefinement(newbies=(newbies1+newbies4)))
            if seg2 is None:
                refine.append(ProvisionalRefinement(newbies=(newbies2+newbies4)))
        return theBetter(newSkeleton, tuple(refine), alpha)
    RefinementRule(conservativeRuleSet, [(0,1,3,4), (0,2,3,4), (0,3,4,5), (0,1,4,5),
                                         (1,2,4,5), (1,3,4,5), (0,2,3,5), (1,2,3,5), 
                                         (2,3,4,5), (0,1,2,3), (0,1,2,4), (0,1,2,5)],
                   fourEdges1)

    def fourEdges2(element, signature, edgenodes, newSkeleton, alpha):
        # We need to get the edge numbers in the signature and the
        # node id's of the other edges in a particular order so that
        # we can construct legal elements in the subdivisions below.
        # The four edge nodes must be clockwise as viewed from the
        # edge defined by the first two nodes in oen.  The first two
        # edge nodes must be on edges adjacent to the first node in
        # oen.  The second and third edge nodes must be adjacent to
        # the third node in oen.  Fortunately there are only three
        # cases.
        if signature == (0,2,4,5):
            signature = (0,4,5,2)
            oen = ((1,2),(3,0)) # other edge nodes
        if signature == (0,1,3,5):
            signature = (1,0,3,5)
            oen = ((1,3),(0,2))
        if signature == (1,2,3,4):
            signature = (2,3,4,1)
            oen = ((0,1),(3,2))
        ne = [edgenodes[signature[i]][0] for i in range(4)]
        bNodes = baseNodes(element)
        # One possibility is to split the tet along the quad defined
        # by the four edge nodes.  Then we have two wedges (where the
        # four points defining the quad that separates the two are not
        # necessarily in a plane).  The wedges can be split into tets
        # four possible ways.  Then we match up the pairs of wedge
        # subdivisions which are compatible along the quad defined by
        # the four edge nodes for a total of 8 possibilities with 6
        # tets.
        ## TODO 3D: There's actually (at least) 6 ways to
        ## tetrahedralize each wedge - implement the other ways.
        topwedges = [[],[]]
        bottomwedges = [[],[]]
        wedges = topwedges
        for ids in oen:
            nn = [bNodes[i] for i in ids]

            segA = [newSkeleton.findSegment(ne[3],nn[0]),
                    newSkeleton.findSegment(ne[2],nn[0])]
            segB = [newSkeleton.findSegment(ne[0],nn[1]),
                    newSkeleton.findSegment(ne[1],nn[1])]
            if segA[0] is not None and segB[0] is not None:
                raise ooferror.ErrPyProgrammingError("inconsistent refinement on tet face")
            if segA[1] is not None and segB[1] is not None:
                raise ooferror.ErrPyProgrammingError("inconsistent refinement on tet face")
                
            wedges.append([])
            # these tets all have segment ne[2] - ne[0]
            tet0 = ProvisionalTetra(nodes=[ne[2],ne[1],ne[0],nn[0]], parents=[element])
            tet1 = ProvisionalTetra(nodes=[ne[3],ne[2],ne[0],nn[0]], parents=[element])
            tet2 = ProvisionalTetra(nodes=[ne[2],ne[3],nn[1],nn[0]], parents=[element])
            if segB[0] is None and segB[1] is None:
                wedges[0].append([tet0,tet1,tet2])
            tet3 = ProvisionalTetra(nodes=[ne[2],ne[1],ne[0],nn[1]], parents=[element])
            tet4 = ProvisionalTetra(nodes=[ne[3],ne[2],ne[0],nn[1]], parents=[element])
            tet5 = ProvisionalTetra(nodes=[ne[0],ne[1],nn[0],nn[1]], parents=[element])
            if segA[0] is None and segA[1] is None:
                wedges[0].append([tet3,tet4,tet5])
            tet6 = ProvisionalTetra(nodes=[nn[0],ne[2],nn[1],ne[0]], parents=[element])
            if segA[0] is None and segB[1] is None:
                wedges[0].append([tet6,tet0,tet4])
            # the rest cross the other way
            tet7 = ProvisionalTetra(nodes=[ne[3],ne[1],ne[0],nn[0]], parents=[element])
            tet8 = ProvisionalTetra(nodes=[ne[3],ne[2],ne[1],nn[0]], parents=[element])
            if segB[0] is None and segB[1] is None:
                wedges[1].append([tet7,tet8,tet2])
            tet9 = ProvisionalTetra(nodes=[ne[3],ne[1],ne[0],nn[1]], parents=[element])
            tet10 = ProvisionalTetra(nodes=[ne[3],ne[2],ne[1],nn[1]], parents=[element])
            if segA[0] is None and segA[1] is None:
                wedges[1].append([tet9,tet10,tet5])
            tet11 = ProvisionalTetra(nodes=[nn[0],ne[1],nn[1],ne[3]], parents=[element])
            if segA[1] is None and segB[0] is None:
                wedges[1].append([tet11,tet10,tet7])
            # reorder the edge nodes so that we produce legal elements
            # in the second iteration
            temp = [ne[2],ne[1],ne[0],ne[3]]
            ne = temp
            wedges = bottomwedges
                
        refine = []
        for k in (0,1):
            for twedge in topwedges[k]:
                for bwedge in bottomwedges[k]:
                    tets = twedge[:]
                    tets.extend(bwedge)
                    refine.append(ProvisionalRefinement(newbies=tets))

        if len(refine) == 0:
            pos = element.center()
            nc = newSkeleton.newNode(pos.x, pos.y, pos.z)
            nn0 = [bNodes[i] for i in oen[0]]
            nn1 = [bNodes[i] for i in oen[1]]
            # the ne are back in their original order
            tet12 = ProvisionalTetra(nodes=[ne[0],ne[1],nn0[0],nc], parents=[element])
            tet13 = ProvisionalTetra(nodes=[ne[3],nn0[1],ne[2],nc], parents=[element])
            tet14 = ProvisionalTetra(nodes=[ne[2],ne[1],nn1[0],nc], parents=[element])
            tet15 = ProvisionalTetra(nodes=[nn1[1],ne[0],ne[3],nc], parents=[element])
            tets = [tet12,tet13,tet14,tet15]
            # there are two cases, but we only have to test one edge
            # to be sure which case is relevant
            if newSkeleton.findSegment(ne[3],nn0[0]) is not None:
                tets.append(ProvisionalTetra(nodes=[ne[0],nn0[0],ne[3],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[ne[3],nn0[0],nn0[1],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[nn0[0],ne[1],nn0[1],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[nn0[1],ne[1],ne[2],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[nn1[1],nn1[0],ne[0],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[ne[0],nn1[0],ne[1],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[nn1[1],ne[2],nn1[0],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[nn1[1],ne[3],ne[2],nc], parents=[element]))
            if newSkeleton.findSegment(ne[0],nn0[1]) is not None:
                tets.append(ProvisionalTetra(nodes=[ne[3],ne[0],nn0[1],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[ne[0],nn0[0],nn0[1],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[nn0[1],nn0[0],ne[2],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[ne[2],nn0[0],ne[1],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[ne[0],nn1[1],ne[1],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[nn1[1],nn1[0],ne[1],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[nn1[1],ne[3],nn1[0],nc], parents=[element]))
                tets.append(ProvisionalTetra(nodes=[ne[3],ne[2],nn1[0],nc], parents=[element]))
            refine.append(ProvisionalRefinement(newbies=tets))

                    
        return theBetter(newSkeleton, tuple(refine), alpha)
    RefinementRule(conservativeRuleSet, [(1,2,3,4), (0,2,4,5), (0,1,3,5)],
                   fourEdges2)



    def fiveEdges(element, signature, edgenodes, newSkeleton, alpha):
        # Again, we need the edge numbers in a specific order.  The
        # five edge markings can be thought of as the fourEdges2 case
        # plus one edge.  We put the edges which form the fourEdges2
        # formation first, in an order such that the form a clockwise
        # loop as viewed from the unmarked edge.
        bNodes = baseNodes(element)
        if signature == (0,1,2,3,4):
            signature = (4,3,2,1,0)
            uen = [bNodes[i] for i in (3,2)] # unmarked edge nodes
            oen = [bNodes[i] for i in (0,1)] # opposite (the unmarked edge) edge nodes 
        if signature == (0,1,2,3,5):
            signature = (1,0,3,5,2)
            uen = [bNodes[i] for i in (1,3)]
            oen = [bNodes[i] for i in (0,2)]
        if signature == (0,1,2,4,5):
            signature = (5,4,0,2,1)
            uen = [bNodes[i] for i in (3,0)]
            oen = [bNodes[i] for i in (1,2)]
        if signature == (0,1,3,4,5):
            signature = (3,0,1,5,4)
            uen = [bNodes[i] for i in (0,2)]
            oen = [bNodes[i] for i in (1,3)]
        if signature == (0,2,3,4,5):
            signature = (0,4,5,2,3)
            uen = [bNodes[i] for i in (1,2)]
            oen = [bNodes[i] for i in (3,0)]
        if signature == (1,2,3,4,5):
            signature = (2,3,4,1,5)
            uen = [bNodes[i] for i in (0,1)]
            oen = [bNodes[i] for i in (3,2)]
        ne = [edgenodes[signature[i]][0] for i in range(5)]
         # the following two tets are used in every possible refinement
        tet0 = ProvisionalTetra(nodes=[ne[1],ne[2],ne[4],oen[0]], parents=[element])
        tet1 = ProvisionalTetra(nodes=[ne[0],ne[4],ne[3],oen[1]], parents=[element])
        # We can split the remaining space between these two tets and
        # the first four edge nodes in two different ways.  We can
        # then combine that with the "bottom wedge" which can be
        # refined as above.
        topwedges = []
        tet2 = ProvisionalTetra(nodes=[ne[0],ne[1],ne[2],ne[4]], parents=[element])
        tet3 = ProvisionalTetra(nodes=[ne[0],ne[2],ne[3],ne[4]], parents=[element])
        topwedges.append([tet0,tet1,tet2,tet3])
        tet4 = ProvisionalTetra(nodes=[ne[0],ne[1],ne[3],ne[4]], parents=[element])
        tet5 = ProvisionalTetra(nodes=[ne[1],ne[2],ne[3],ne[4]], parents=[element])
        topwedges.append([tet0,tet1,tet4,tet5])

        # now find refinements for the bottom wedge
        segA = [newSkeleton.findSegment(ne[3],uen[0]),
                newSkeleton.findSegment(ne[2],uen[0])]
        segB = [newSkeleton.findSegment(ne[0],uen[1]),
                newSkeleton.findSegment(ne[1],uen[1])]
        bottomwedges = [[],[]]
        tet6 = ProvisionalTetra(nodes=[ne[2],ne[1],ne[0],uen[0]], parents=[element])
        tet7 = ProvisionalTetra(nodes=[ne[3],ne[2],ne[0],uen[0]], parents=[element])
        tet8 = ProvisionalTetra(nodes=[ne[2],ne[3],uen[1],uen[0]], parents=[element])
        if segB[0] is None and segB[1] is None:
            bottomwedges[0].append([tet6,tet7,tet8])
        tet9 = ProvisionalTetra(nodes=[ne[2],ne[1],ne[0],uen[1]], parents=[element])
        tet10 = ProvisionalTetra(nodes=[ne[3],ne[2],ne[0],uen[1]], parents=[element])
        tet11 = ProvisionalTetra(nodes=[ne[0],ne[1],uen[0],uen[1]], parents=[element])
        if segA[0] is None and segA[1] is None:
            bottomwedges[0].append([tet9,tet10,tet11])
        tet12 = ProvisionalTetra(nodes=[uen[0],ne[2],uen[1],ne[0]], parents=[element])
        if segA[0] is None and segB[1] is None:
            bottomwedges[0].append([tet12,tet6,tet10])
        # the rest cross the other way
        tet13 = ProvisionalTetra(nodes=[ne[3],ne[1],ne[0],uen[0]], parents=[element])
        tet14 = ProvisionalTetra(nodes=[ne[3],ne[2],ne[1],uen[0]], parents=[element])
        if segB[0] is None and segB[1] is None:
            bottomwedges[1].append([tet13,tet14,tet8])
        tet15 = ProvisionalTetra(nodes=[ne[3],ne[1],ne[0],uen[1]], parents=[element])
        tet16 = ProvisionalTetra(nodes=[ne[3],ne[2],ne[1],uen[1]], parents=[element])
        if segA[0] is None and segA[1] is None:
            bottomwedges[1].append([tet15,tet16,tet11])
        tet17 = ProvisionalTetra(nodes=[uen[0],ne[1],uen[1],ne[3]], parents=[element])
        if segA[1] is None and segB[0] is None:
            bottomwedges[1].append([tet17,tet16,tet13])
        refine = []
        for k in (0,1):
            for bwedge in bottomwedges[k]:
                tets = topwedges[k][:]
                tets.extend(bwedge)
                refine.append(ProvisionalRefinement(newbies=tets))
        
        return theBetter(newSkeleton, tuple(refine), alpha)            
    RefinementRule(conservativeRuleSet, [(0,1,2,3,4),(0,1,2,3,5),(0,1,2,4,5),
                                         (0,1,3,4,5),(0,2,3,4,5),(1,2,3,4,5)], 
                   fiveEdges)

       
    def sixEdges(element, signature, edgenodes, newSkeleton, alpha):
        bNodes = baseNodes(element)
        edgeMap = element.segToNodeMap()
        cornerTets = []
        # create the four outer corner tets where node i is the only
        # node not replaced
        for i in range(4):
            newnodes = bNodes[:]
            for j in range(4):
                if i != j:
                    try:
                        edgeNodeIds = (i,j)
                        edgeId = edgeMap.index(edgeNodeIds)
                    except ValueError:
                        edgeNodeIds = (j,i)
                        edgeId = edgeMap.index(edgeNodeIds)
                    newnodes[j] = edgenodes[edgeId][0]
            cornerTets.append(ProvisionalTetra(nodes=newnodes, parents=[element]))
        # now, with the six edge nodes, there are three ways to divide
        # them into four tetrahedra without adding new nodes
        opposites = [(0,5), (1,3), (2,4)]
        faces = element.getFaceToEdgesMap()
        refine = []
        for pair in opposites:
            insideTets = []
            for face in faces:
                if pair[0] not in face: 
                    oppnode = edgenodes[pair[0]][0]
                else:
                    oppnode = edgenodes[pair[1]][0]
                newnodes = [edgenodes[face[2]][0],edgenodes[face[1]][0],
                            edgenodes[face[0]][0],oppnode]
                insideTets.append(ProvisionalTetra(nodes=newnodes, parents=[element]))
            thenewbies = cornerTets[:]
            thenewbies.extend(insideTets)
            refine.append(ProvisionalRefinement(newbies=thenewbies))
        return theBetter(newSkeleton, tuple(refine), alpha)
    RefinementRule(conservativeRuleSet, [(0,1,2,3,4,5)], 
                   sixEdges)

    deadlockableSignatures = [(3,4,5), (0,1,4), (0,2,3), (1,2,5),
                              (1,2,3,4), (0,2,4,5), (0,1,3,5)]
