# -*- python -*-
# $RCSfile: snaprefinemethod.py,v $
# $Author: langer $
# $Date: 2010/12/09 01:08:41 $
# $Revision: 1.12 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import utils
from ooflib.common import primitives
from ooflib.common import enum
from ooflib.common.IO import xmlmenudump

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

utils.OOFdefine('getSnapRefineRuleSet', getRuleSet)

#########################################

# The names of the refinement rule sets are stored in an Enum so that
# the UI can handle them correctly.

class RuleSet(enum.EnumClass(*[(r.name(), r.help())
                               for r in RefinementRuleSet.allRuleSets])):
    pass
##    def __repr__(self):
##	return "RuleSet('%s')" % self.name
utils.OOFdefine('SnapRefineRuleSet', RuleSet)

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
    def apply(self, element, signature_info, cats, edgenodes, newSkeleton, maxdelta2):
        if config.dimension() == 2:
            # in 2D, the first member of the signature_info is the rotation
            newels = self.function(element, signature_info[0], cats, edgenodes, newSkeleton, maxdelta2)
        elif config.dimension() == 3:
            newels = self.function(element, signature_info, cats, edgenodes, newSkeleton, maxdelta2)
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

##class ProvisionalRefinement:
##    def __init__(self, newbies = [], internalNodes = []):
##        self.newbies = newbies
##        self.internalNodes = internalNodes
##    def energy(self, skeleton, alpha):
##        energy = 0.0
##        for element in self.newbies:
##            energy += element.energyTotal(skeleton, alpha)
##        return energy/len(self.newbies)
##    def accept(self, skeleton):
##        return [element.accept(skeleton) for element in self.newbies]

##def theBetter(skeleton, candidates, alpha):
##    energy_min = 100000.                # much larger than any possible energy
##    theone = None
##    for candi in candidates:
##        energy = candi.energy(skeleton, alpha)
##        if energy < energy_min:
##            energy_min = energy
##            theone = candi
##    # Before returning the chosen refinement, we need to remove any internal
##    # nodes created for the refinements that were not chosen.
##    destroyedNodes = {}
##    for candi in candidates:
##        if candi is theone or not candi.internalNodes:
##            continue
##        for n in candi.internalNodes:
##            if n not in theone.internalNodes and n not in destroyedNodes:
##                n.destroy(skeleton)
##                destroyedNodes[n] = 1
                
##    return theone.accept(skeleton)

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

#
# Unmarked, unrefined element (triangle or quad)
#
def unrefinedelement(element, signature_info, newSkeleton):
    if config.dimension() == 2:
        bNodes = baseNodes(element, 0)
    elif config.dimension() == 3:
        bNodes = baseNodes(element)
    el = newSkeleton.newElement(nodes=bNodes,
                                parents=[element])
    return (el,)

##########################################

#            BEGIN 2D RULES

##########################################


if config.dimension() == 2:


# Unrefined triangle or
#
#          2
#         /\
#        / |\
#       /  | \
#     C/  ..  \B
#     / .  a . \
#    /.        .\
#   /____________\
#   0     A      1
#
# where "a" may be the center, or a transition point along the
# line from one vertex to the midpoint of the opposite side

    def rule000(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2 = baseNodes(element, rotation)
        rcats=[cats[(i+rotation)%3] for i in range(3)]
        A=rcats[0][0]
        B=rcats[1][0]
        C=rcats[2][0]
        na=None
        if A==B and B==C:
            return (
                newSkeleton.newElement(nodes=[n0, n1, n2],
                                       parents=[element]),)
        elif A!=B and B==C:
            n2pt=n2.position()
            n01Midpt=0.5*(n0.position()+n1.position())
            transpt=newSkeleton.MS.transitionPointWithPoints_unbiased(n2pt,n01Midpt)
            if transpt:
                d2=(transpt-n2pt)**2
                d01=(transpt-n01Midpt)**2
            if transpt and d2>maxdelta2 and d01>maxdelta2:
                na = newSkeleton.newNode(transpt.x, transpt.y)
            else:
                pos = element.center()
                na = newSkeleton.newNode(pos.x, pos.y)
        elif B!=C and C==A:
            n0pt=n0.position()
            n12Midpt=0.5*(n1.position()+n2.position())
            transpt=newSkeleton.MS.transitionPointWithPoints_unbiased(n0pt,n12Midpt)
            if transpt:
                d0=(transpt-n0pt)**2
                d12=(transpt-n12Midpt)**2
            if transpt and d0>maxdelta2 and d12>maxdelta2:
                na = newSkeleton.newNode(transpt.x, transpt.y)
            else:
                pos = element.center()
                na = newSkeleton.newNode(pos.x, pos.y)
        elif C!=A and A==B:
            n1pt=n1.position()
            n20Midpt=0.5*(n2.position()+n0.position())
            transpt=newSkeleton.MS.transitionPointWithPoints(n1pt,n20Midpt)
            if transpt:
                d1=(transpt-n1pt)**2
                d20=(transpt-n20Midpt)**2
            if transpt and d1>maxdelta2 and d20>maxdelta2:
                na = newSkeleton.newNode(transpt.x, transpt.y)
            else:
                pos = element.center()
                na = newSkeleton.newNode(pos.x, pos.y)
        else:
            pos = element.center()
            na = newSkeleton.newNode(pos.x, pos.y)
        return (
            newSkeleton.newElement(nodes=[na, n0, n1], parents=[element]),
            newSkeleton.newElement(nodes=[na, n1, n2], parents=[element]),
            newSkeleton.newElement(nodes=[na, n2, n0], parents=[element]))
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
    #
    # OR
    #          2
    #         /\
    #        / |\
    #       /  | \
    #      /  b|  \
    #     /   .|.  \
    #    /  .  |  . \
    #   /______|_____\
    #   0      a      1

    def rule100(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2 = baseNodes(element, rotation)
        rcats=[cats[(i+rotation)%3] for i in range(3)]
        na = edgenodes[rotation][0]
        if rcats[0][1]!=rcats[1][0] and rcats[2][0]!=rcats[0][0]:
            napt=na.position()
            n2pt=n2.position()
            nb = newSkeleton.newNode(0.5*(napt.x+n2pt.x),0.5*(napt.y+n2pt.y))
            return (newSkeleton.newElement(nodes=[nb, n0, na], parents=[element]),
                    newSkeleton.newElement(nodes=[nb, na, n1], parents=[element]),
                    newSkeleton.newElement(nodes=[nb, n1, n2], parents=[element]),
                    newSkeleton.newElement(nodes=[nb, n2, n0], parents=[element]))
        else:
            return (newSkeleton.newElement(nodes=[na, n2, n0], parents=[element]),
                    newSkeleton.newElement(nodes=[na, n1, n2], parents=[element]))
    RefinementRule(conservativeRuleSet, (1,0,0), rule100)

    #          2
    #         /\
    #        /  \
    #       /    \
    #      /      b
    #     /      / \
    #    /      /   \
    #   /______/_____\
    #   0      a      1
    #
    # OR
    #
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
    #        /  \D
    #       /    \
    #     E/    . b
    #     /  .   / \
    #    /.     /   \C
    #   /______/_____\
    #   0  A   a  B   1
    #
    # OR (B!=C)
    #
    #          2
    #         /\
    #        /  \D
    #       /    \
    #     E/      b
    #     /      / \
    #    /     .c.  \C
    #   /._____/____.\
    #   0  A   a  B   1
    #
    # OR
    #
    #          2
    #         /\
    #        /  \D
    #       /  . \
    #     E/      b
    #     /     ./ \
    #    /      c.  \C
    #   /______/____.\
    #   0  A   a  B   1
    #
    # OR
    #
    #          2
    #         /\
    #        /  \D
    #       /  . \
    #     E/      b
    #     /     ./ \
    #    /     .c.  \C
    #   /._____/____.\
    #   0  A   a  B   1


    def rule110(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2 = baseNodes(element, rotation)
        rcats=[cats[(i+rotation)%3] for i in range(3)]
        A=rcats[0][0]
        B=rcats[0][1]
        C=rcats[1][0]
        D=rcats[1][1]
        E=rcats[2][0]
        na = edgenodes[rotation][0]
        nb = edgenodes[(rotation+1)%3][0]
        if B==C:
            if D==E and E!=A:
                return (newSkeleton.newElement(nodes=[nb, n0, na], parents=[element]),
                        newSkeleton.newElement(nodes=[nb, na, n1], parents=[element]),
                        newSkeleton.newElement(nodes=[nb, n2, n0], parents=[element]))
            elif D!=E and E==A:
                return (newSkeleton.newElement(nodes=[na, n2, n0], parents=[element]),
                        newSkeleton.newElement(nodes=[nb, na, n1], parents=[element]),
                        newSkeleton.newElement(nodes=[nb, n2, na], parents=[element]))
            else:
                return (newSkeleton.newElement(nodes=[nb, n2, n0, na], parents=[element]),
                        newSkeleton.newElement(nodes=[nb, na, n1], parents=[element]))
        else: #if B!=C
            if D==E and E!=A:
                napt=na.position()
                nbpt=nb.position()
                nc = newSkeleton.newNode(0.5*(napt.x+nbpt.x),0.5*(napt.y+nbpt.y))
                return (newSkeleton.newElement(nodes=[nc, n0, na], parents=[element]),
                        newSkeleton.newElement(nodes=[nc, na, n1], parents=[element]),
                        newSkeleton.newElement(nodes=[nc, n1, nb], parents=[element]),
                        newSkeleton.newElement(nodes=[nc, nb, n2, n0], parents=[element]))
            elif D!=E and E==A:
                napt=na.position()
                nbpt=nb.position()
                nc = newSkeleton.newNode(0.5*(napt.x+nbpt.x),0.5*(napt.y+nbpt.y))
                return (newSkeleton.newElement(nodes=[nc, nb, n2], parents=[element]),
                        newSkeleton.newElement(nodes=[nc, na, n1], parents=[element]),
                        newSkeleton.newElement(nodes=[nc, n1, nb], parents=[element]),
                        newSkeleton.newElement(nodes=[nc, n2, n0, na], parents=[element]))
            elif D!=E and E!=A:
                napt=na.position()
                nbpt=nb.position()
                nc = newSkeleton.newNode(0.5*(napt.x+nbpt.x),0.5*(napt.y+nbpt.y))
                return (newSkeleton.newElement(nodes=[nc, nb, n2], parents=[element]),
                        newSkeleton.newElement(nodes=[nc, na, n1], parents=[element]),
                        newSkeleton.newElement(nodes=[nc, n1, nb], parents=[element]),
                        newSkeleton.newElement(nodes=[nc, n2, n0], parents=[element]),
                        newSkeleton.newElement(nodes=[nc, n0, na], parents=[element]))
            else:
                return (newSkeleton.newElement(nodes=[nb, n2, n0, na], parents=[element]),
                        newSkeleton.newElement(nodes=[nb, na, n1], parents=[element]))        
    #RefinementRule(conservativeRuleSet, (1,1,0), rule110)
    RefinementRule(liberalRuleSet, (1,1,0), rule110)

    #          2
    #         /\
    #        /  \ 
    #       /    \
    #      c______b
    #     / \    / \ 
    #    /   \  /   \
    #   /_____\/_____\
    #   0      a      1
    #
    # OR
    #
    #          2
    #         /\
    #       E/  \D
    #       /    \
    #      c______b
    #     / \.     \ 
    #   F/   \  .   \C
    #   /_____\ ___._\
    #   0  A   a  B   1
    #
    # OR
    #
    #          2
    #         /\
    #       E/. \D
    #       / .  \
    #      c  .   b
    #     / \ .  / \ 
    #   F/   \. /   \C
    #   /_____\/_____\
    #   0  A   a  B   1
    #
    # OR
    #
    #          2
    #         /\
    #       E/  \D
    #       /    \
    #      c_____ b
    #     /    . / \ 
    #   F/  .   /   \C
    #   /.____ /_____\
    #   0  A   a  B   1

    def rule111(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2 = baseNodes(element, rotation)
        rcats=[cats[(i+rotation)%3] for i in range(3)]
        A=rcats[0][0]
        B=rcats[0][1]
        C=rcats[1][0]
        D=rcats[1][1]
        E=rcats[2][0]
        F=rcats[2][1]
        na = edgenodes[rotation][0]
        nb = edgenodes[(rotation+1)%3][0]
        nc = edgenodes[(rotation+2)%3][0]
        if B!=C and D==E and F==A:
            return (
                newSkeleton.newElement(nodes=[n0, na, nc], parents=[element]),
                newSkeleton.newElement(nodes=[n1, nc, na], parents=[element]),
                newSkeleton.newElement(nodes=[n1, nb, nc], parents=[element]),
                newSkeleton.newElement(nodes=[n2, nc, nb], parents=[element]))
        elif B==C and D!=E and F==A:
            return (
                newSkeleton.newElement(nodes=[n0, na, nc], parents=[element]),
                newSkeleton.newElement(nodes=[n1, nb, na], parents=[element]),
                newSkeleton.newElement(nodes=[n2, na, nb], parents=[element]),
                newSkeleton.newElement(nodes=[n2, nc, na], parents=[element]))
        elif B==C and D==E and F!=A:
            return (
                newSkeleton.newElement(nodes=[n0, na, nb], parents=[element]),
                newSkeleton.newElement(nodes=[n0, nb, nc], parents=[element]),
                newSkeleton.newElement(nodes=[n1, nb, na], parents=[element]),
                newSkeleton.newElement(nodes=[n2, nc, nb], parents=[element]))
        else:
            return (
                newSkeleton.newElement(nodes=[n0, na, nc], parents=[element]),
                newSkeleton.newElement(nodes=[n1, nb, na], parents=[element]),
                newSkeleton.newElement(nodes=[n2, nc, nb], parents=[element]),
                newSkeleton.newElement(nodes=[na, nb, nc], parents=[element]))
    RefinementRule(conservativeRuleSet, (1,1,1), rule111)

    # Quads
    #
    # Unrefined quadrilateral or
    #    C
    # 3------2
    # |\    /|
    # | \  / |
    # | a\/  |
    #D|  /\  |B
    # | /  \ |
    # |/    \|
    # 0------1
    #    A
    #
    # (where "a" may be the center or a transition point
    # from the midpoint of one edge to the midpoint of
    # the opposite edge)
    #
    #    C
    # 3------2
    # |     /|
    # |    / |
    # |   /  |
    #D|  /   |B
    # | /    |
    # |/     |
    # 0------1
    #    A
    #
    #    C
    # 3------2
    # |\     |
    # | \    |
    # |  \   |
    #D|   \  |B
    # |    \ |
    # |     \|
    # 0------1
    #    A

    def rule0000(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        rcats=[cats[(i+rotation)%4] for i in range(4)]
        A=rcats[0][0]
        B=rcats[1][0]
        C=rcats[2][0]
        D=rcats[3][0]
        if A==B and B==C and C==D:
            return (
                newSkeleton.newElement(nodes=[n0, n1, n2, n3],
                                        parents=[element]),)
        elif A!=B and B==C and  D==A:
            return (
                newSkeleton.newElement(nodes=[n0, n1, n3], parents=[element]),
                newSkeleton.newElement(nodes=[n1, n2, n3], parents=[element]))
        elif A==B and B!=C and C==D:
            return (
                newSkeleton.newElement(nodes=[n0, n1, n2], parents=[element]),
                newSkeleton.newElement(nodes=[n0, n2, n3], parents=[element]))
        elif A!=B and B==C and C==D:
            n01Midpt=0.5*(n0.position()+n1.position())
            n23Midpt=0.5*(n2.position()+n3.position())
            transpt=newSkeleton.MS.transitionPointWithPoints_unbiased(n23Midpt,n01Midpt)
            if transpt:
                d23=(transpt-n23Midpt)**2
                d01=(transpt-n01Midpt)**2
            if transpt and d23>maxdelta2 and d01>maxdelta2:
                na = newSkeleton.newNode(transpt.x, transpt.y)
            else:
                pos = element.frommaster(Point(0., 0.), rotation)
                na = newSkeleton.newNode(pos.x, pos.y)
        elif B!=C and C==D and D==A:
            n12Midpt=0.5*(n1.position()+n2.position())
            n30Midpt=0.5*(n3.position()+n0.position())
            transpt=newSkeleton.MS.transitionPointWithPoints_unbiased(n30Midpt,n12Midpt)
            if transpt:
                d30=(transpt-n30Midpt)**2
                d12=(transpt-n12Midpt)**2
            if transpt and d30>maxdelta2 and d12>maxdelta2:
                na = newSkeleton.newNode(transpt.x, transpt.y)
            else:
                pos = element.frommaster(Point(0., 0.), rotation)
                na = newSkeleton.newNode(pos.x, pos.y)
        elif C!=D and D==A and A==B:
            n23Midpt=0.5*(n2.position()+n3.position())
            n01Midpt=0.5*(n0.position()+n1.position())
            transpt=newSkeleton.MS.transitionPointWithPoints_unbiased(n01Midpt,n23Midpt)
            if transpt:
                d01=(transpt-n01Midpt)**2
                d23=(transpt-n23Midpt)**2
            if transpt and d01>maxdelta2 and d23>maxdelta2:
                na = newSkeleton.newNode(transpt.x, transpt.y)
            else:
                pos = element.frommaster(Point(0., 0.), rotation)
                na = newSkeleton.newNode(pos.x, pos.y)
        elif D!=A and A==B and B==C:
            n30Midpt=0.5*(n3.position()+n0.position())
            n12Midpt=0.5*(n1.position()+n2.position())
            transpt=newSkeleton.MS.transitionPointWithPoints_unbiased(n12Midpt,n30Midpt)
            if transpt:
                d12=(transpt-n12Midpt)**2
                d30=(transpt-n30Midpt)**2
            if transpt and d12>maxdelta2 and d30>maxdelta2:
                na = newSkeleton.newNode(transpt.x, transpt.y)
            else:
                pos = element.frommaster(Point(0., 0.), rotation)
                na = newSkeleton.newNode(pos.x, pos.y)
        else:
            pos = element.frommaster(Point(0., 0.), rotation)
            na = newSkeleton.newNode(pos.x, pos.y)
        return (
            newSkeleton.newElement(nodes=[na, n0, n1], parents=[element]),
            newSkeleton.newElement(nodes=[na, n1, n2], parents=[element]),
            newSkeleton.newElement(nodes=[na, n2, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, n3, n0], parents=[element]))
    RefinementRule(liberalRuleSet, (0,0,0,0), rule0000)

    #            D
    #  3-------------------2
    #  |\                 /|
    #  | \               / |
    #  |  \             /  |
    #  |   \           /   |
    # E|    \         /    |C
    #  |     \       /     |
    #  |      \     /      |
    #  |       \   /       |
    #  |        \ /        |
    #  0---------a---------1
    #       A         B

    #  3-------------------2
    #  |\ .                |
    #  | \  .              |
    #  |  \   .            |
    #  |   \    .          |
    #  |    \     .        |
    #  |     \      .      |
    #  |      \       .    |
    #  |       \        .  |
    #  |        \         .|
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
    #  |                . /|
    #  |              .  / |
    #  |            .   /  |
    #  |          .    /   |
    #  |        .     /    |
    #  |      .      /     |
    #  |    .       /      |
    #  |  .        /       |
    #  |.         /        |
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

    def rule1000(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        rcats=[cats[(i+rotation)%4] for i in range(4)]
        A=rcats[0][0]
        B=rcats[0][1]
        C=rcats[1][0]
        D=rcats[2][0]
        E=rcats[3][0]
        na = edgenodes[rotation][0]
        if B!=C and C==D and D!=E and E==A:
            return (
                newSkeleton.newElement(nodes=[n0, na, n3], parents=[element]),
                newSkeleton.newElement(nodes=[na, n1, n3], parents=[element]),
                newSkeleton.newElement(nodes=[n1, n2, n3], parents=[element]))
        elif B==C and C==D and D!=E and E==A:
            return (
                newSkeleton.newElement(nodes=[n0, na, n3], parents=[element]),
                newSkeleton.newElement(nodes=[na, n1, n2, n3], parents=[element]))
        elif B==C and C!=D and D==E and E!=A:
            return (
                newSkeleton.newElement(nodes=[n3, n0, n2], parents=[element]),
                newSkeleton.newElement(nodes=[n0, na, n2], parents=[element]),
                newSkeleton.newElement(nodes=[na, n1, n2], parents=[element]))
        elif B==C and C!=D and D==E and E==A:
            return (
                newSkeleton.newElement(nodes=[na, n1, n2], parents=[element]),
                newSkeleton.newElement(nodes=[n3, n0, na, n2], parents=[element]))
        else:
            return (
                newSkeleton.newElement(nodes=[n3, n0, na], parents=[element]),
                newSkeleton.newElement(nodes=[n2, n3, na], parents=[element]),
                newSkeleton.newElement(nodes=[n1, n2, na], parents=[element]))
    RefinementRule(liberalRuleSet, (1,0,0,0), rule1000)

    #       E
    #  3----------2
    #  |          |
    #  |          |D
    #  |          |
    # F|          |
    #  |          b
    #  |          |
    #  |          |C
    #  |          |
    #  0----a-----1
    #    A     B
    #

    #  3------------2
    #  |\ .         |
    #  | \  .       |
    #  |  \   .     |
    #  |   \    .   |
    #  |    \     . b
    #  |     \     /|
    #  |      \   / |
    #  |       \ /  |
    #  0--------a---1
    #
    # OR
    #
    #       E
    #  3----------2
    #  |         /|
    #  |        / |D
    #  |       /  |
    # F|      /   |
    #  |     /   /b
    #  |    /   / |
    #  |   /   /  |C
    #  |  /   /   |
    #  | /   /    |
    #  0----a-----1
    #    A     B
    #
    # (It is straightforward to add more cases...)

    def rule1100(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        rcats=[cats[(i+rotation)%4] for i in range(4)]
        A=rcats[0][0]
        B=rcats[0][1]
        C=rcats[1][0]
        D=rcats[1][1]
        E=rcats[2][0]
        F=rcats[3][0]
        na = edgenodes[rotation][0]
        nb = edgenodes[(rotation+1)%4][0]
        if D!=E and E==F and F!=A:
            return (
                newSkeleton.newElement(nodes=[na, n1, nb], parents=[element]),
                newSkeleton.newElement(nodes=[na, nb, n2, n0], parents=[element]),
                newSkeleton.newElement(nodes=[n0, n2, n3], parents=[element]))
        else:
            return (
                newSkeleton.newElement(nodes=[na, n1, nb], parents=[element]),
                newSkeleton.newElement(nodes=[nb, n2, n3], parents=[element]),
                newSkeleton.newElement(nodes=[na, nb, n3], parents=[element]),
                newSkeleton.newElement(nodes=[na, n3, n0], parents=[element]))
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
    #
    # OR (various vays of splitting the two quads (x9))
    #    E      D
    #  3-----b-----2
    #  |     |     |
    #  |     |     |
    # F|     |     |C
    #  |     |     |
    #  |     |     |
    #  0-----a-----1
    #    A      B
    def rule1010(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        rcats=[cats[(i+rotation)%4] for i in range(4)]
        A=rcats[0][0]
        B=rcats[0][1]
        C=rcats[1][0]
        D=rcats[2][0]
        E=rcats[2][1]
        F=rcats[3][0]
        na = edgenodes[rotation][0]
        nb = edgenodes[(rotation+2)%4][0]
        newelements=()
        # Examine left quad
        if E==F and F!=A:
            newelements+=(
                newSkeleton.newElement(nodes=[n0, nb, n3], parents=[element]),
                newSkeleton.newElement(nodes=[n0, na, nb], parents=[element]))
        elif E!=F and F==A:
            newelements+=(
                newSkeleton.newElement(nodes=[n0, na, n3], parents=[element]),
                newSkeleton.newElement(nodes=[n3, na, nb], parents=[element]))
        else:
            newelements+=(
                newSkeleton.newElement(nodes=[n0, na, nb, n3], parents=[element]),)
        # Examine right quad
        if B==C and C!=D:
            newelements+=(
                newSkeleton.newElement(nodes=[na, n1, n2], parents=[element]),
                newSkeleton.newElement(nodes=[na, n2, nb], parents=[element]))
        elif B!=C and C==D:
            newelements+=(
                newSkeleton.newElement(nodes=[na, n1, nb], parents=[element]),
                newSkeleton.newElement(nodes=[n1, n2, nb], parents=[element]))
        else:
            newelements+=(
                newSkeleton.newElement(nodes=[na, n1, n2, nb], parents=[element]),)
        return newelements
    RefinementRule(liberalRuleSet, (1,0,1,0), rule1010)

    #    F     E
    #  3----c-----2
    #  |    |     |
    #  |    |     |D
    # G|    |     |
    #  |    |_____|b 
    #  |   /|d    |
    #  |  / |     |
    #  | /  |     |C
    #  |/   |     |
    #  0----a-----1
    #    A     B
    # OR
    #
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
    #
    # OR
    #
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
    #

    def rule1110(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        rcats=[cats[(i+rotation)%4] for i in range(4)]
        A=rcats[0][0]
        B=rcats[0][1]
        C=rcats[1][0]
        D=rcats[1][1]
        E=rcats[2][0]
        F=rcats[2][1]
        G=rcats[3][0]
        na = edgenodes[rotation][0]
        nb = edgenodes[(rotation+1)%4][0]
        nc = edgenodes[(rotation+2)%4][0]
        napt=na.position()
        ncpt=nc.position()
        nd = newSkeleton.newNode(0.5*(napt.x+ncpt.x), 0.5*(napt.y+ncpt.y))
        #Add the two right quads
        newelements=(
            newSkeleton.newElement(nodes=[na, n1, nb, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nd, nb, n2, nc], parents=[element]))
        #Choices for splitting the left quad
        if F==G and G!=A:
            newelements+=(
                newSkeleton.newElement(nodes=[n0, na, nd], parents=[element]),
                newSkeleton.newElement(nodes=[n0, nd, nc, n3], parents=[element]))
        elif F!=G and G==A:
            newelements+=(
                newSkeleton.newElement(nodes=[n3, nd, nc], parents=[element]),
                newSkeleton.newElement(nodes=[n3, n0, na, nd], parents=[element]))
        else:
            newelements+=(
                newSkeleton.newElement(nodes=[n0, na, nd], parents=[element]),
                newSkeleton.newElement(nodes=[nd, nc, n3], parents=[element]),
                newSkeleton.newElement(nodes=[n0, nd, n3], parents=[element]))
        return newelements
    ##    refine0 = ProvisionalRefinement(
    ##        newbies = [ProvisionalQuad(nodes=[na, n1, nb, nd], parents=[element]),
    ##                   ProvisionalQuad(nodes=[nd, nb, n2, nc], parents=[element]),
    ##                   ProvisionalQuad(nodes=[n0, nd, nc, n3], parents=[element]),
    ##                   ProvisionalTriangle(nodes=[n0, na, nd], parents=[element])],
    ##        internalNodes = [nd])
    ##    refine1 = ProvisionalRefinement(
    ##        newbies = [ProvisionalQuad(nodes=[na, n1, nb, nd], parents=[element]),
    ##                   ProvisionalQuad(nodes=[nd, nb, n2, nc], parents=[element]),
    ##                   ProvisionalQuad(nodes=[n0, na, nd, n3], parents=[element]),
    ##                   ProvisionalTriangle(nodes=[nd, nc, n3], parents=[element])],
    ##        internalNodes = [nd])    
    ##    refine2 = ProvisionalRefinement(
    ##        newbies = [ProvisionalQuad(nodes=[na, n1, nb, nd], parents=[element]),
    ##                   ProvisionalQuad(nodes=[nd, nb, n2, nc], parents=[element]),
    ##                   ProvisionalTriangle(nodes=[n0, na, nd], parents=[element]),
    ##                   ProvisionalTriangle(nodes=[n0, nd, n3], parents=[element]),
    ##                   ProvisionalTriangle(nodes=[nd, nc, n3], parents=[element])],
    ##        internalNodes = [nd])                      
    ##    return theBetter(newSkeleton, (refine0, refine1, refine2), alpha)
    RefinementRule(liberalRuleSet, (1,1,1,0), rule1110)

    #     F     E
    #  3-----c-----2
    #  |     |     |
    # G|     |     |D
    #  |     |     |
    #  d_____e_____b
    #  |     |     |
    # H|     |     |C
    #  |     |     |
    #  |     |     |
    #  0-----a-----1
    #     A     B
    #
    # OR
    #
    #     F     E
    #  3-----c-----2
    #  |    / \    |
    # G|   /   \   |D
    #  |  /     \  |
    #  d /       \ b
    #  | \       / |
    # H|  \     /  |C
    #  |   \   /   |
    #  |    \ /    |
    #  0-----a-----1
    #     A     B

    def rule1111(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        rcats=[cats[(i+rotation)%4] for i in range(4)]
        A=rcats[0][0]
        B=rcats[0][1]
        C=rcats[1][0]
        D=rcats[1][1]
        E=rcats[2][0]
        F=rcats[2][1]
        G=rcats[3][0]
        H=rcats[3][1]
        #The rotation should not be necessary (also see refinemethod.py)
        na = edgenodes[rotation][0]
        nb = edgenodes[(rotation+1)%4][0]
        nc = edgenodes[(rotation+2)%4][0]
        nd = edgenodes[(rotation+3)%4][0]
        if (B==C and F==G and C==F) or (D==E and H==A and E==H):
            return (
                newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
                newSkeleton.newElement(nodes=[n0, na, nd], parents=[element]),
                newSkeleton.newElement(nodes=[na, n1, nb], parents=[element]),
                newSkeleton.newElement(nodes=[nb, n2, nc], parents=[element]),
                newSkeleton.newElement(nodes=[nd, nc, n3], parents=[element]))
        else:
            napt=na.position()
            ncpt=nc.position()
            ne = newSkeleton.newNode(0.5*(napt.x+ncpt.x), 0.5*(napt.y+ncpt.y))
            return (
                newSkeleton.newElement(nodes=[n0, na, ne, nd], parents=[element]),
                newSkeleton.newElement(nodes=[na, n1, nb, ne], parents=[element]),
                newSkeleton.newElement(nodes=[ne, nb, n2, nc], parents=[element]),
                newSkeleton.newElement(nodes=[nd, ne, nc, n3], parents=[element]))
    RefinementRule(liberalRuleSet, (1,1,1,1), rule1111)


    #################################################################################
    # Cases with at least one edge being trisected.
    # These don't use the edge categories (yet).

    ### Quads, cases 2XXX ###

    #
    #  3-----------------------2
    #  |\                     /|
    #  | \                   / |
    #  |  \                 /  |
    #  |   \               /   |
    #  |    \             /    |
    #  |     \           /     |
    #  |      \         /      |
    #  |       \       /       |
    #  |        \     /        |
    #  0---------a---b---------1
    #

    def rule2000(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        return (
            newSkeleton.newElement(nodes=[n0, na, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, n2, n3], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, n2], parents=[element]))
    RefinementRule(liberalRuleSet, (2,0,0,0), rule2000)

    #
    #  3-----------------------2
    #  |                    * /|
    #  |                *    / |
    #  |            *       /  |
    #  |        *          /   |
    #  |    *             /    |
    #  c *               /     |
    #  |   *            /      |
    #  |     *         /       |
    #  |       *      /        |
    #  0---------a---b---------1
    #

    def rule2001(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+3)%4][0]
        return (
            newSkeleton.newElement(nodes=[n0, na, nc], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, n2, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, n2], parents=[element]),
            newSkeleton.newElement(nodes=[nc, n2, n3], parents=[element]))
    RefinementRule(liberalRuleSet, (2,0,0,1), rule2001)

    #
    #  3---------c-------------2
    #  |         *             |
    #  |                       |
    #  |        * *            |
    #  |                       |
    #  |       *   *           |
    #  |                       |
    #  |      *     *          |
    #  |                       |
    #  |     *       *         |
    #  0----a---------b--------1
    #

    def rule2010(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+2)%4][0]
        return (
            newSkeleton.newElement(nodes=[n0, na, nc, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, n2, nc], parents=[element]))
    RefinementRule(liberalRuleSet, (2,0,1,0), rule2010)

    #
    #  3---------c-------------2
    #  |        **             |
    #  |      *                |
    #  |    *     *            |
    #  |  *                    |
    #  d*          *           |
    #  |\                      |
    #  | \          *          |
    #  |  \                    |
    #  |   \         *         |
    #  0----a---------b--------1
    #

    def rule2011(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+2)%4][0]
        nd = edgenodes[(rotation+3)%4][0]
        return (
            newSkeleton.newElement(nodes=[n0, na, nd], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, n2, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nd, nc, n3], parents=[element]))
    RefinementRule(liberalRuleSet, (2,0,1,1), rule2011)

    #
    #  3-----------------------2
    #  |\ *                    |
    #  | \      *              |
    #  |  \            *       |
    #  |   \                 * c
    #  |    \                 *|
    #  |     \              *  |
    #  |      \           *    |
    #  |       \        *      |
    #  |        \     *        |
    #  0---------a---b---------1
    #

    def rule2100(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+1)%4][0]
        return (
            newSkeleton.newElement(nodes=[n0, na, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, n3], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nc, n2, n3], parents=[element]))
    RefinementRule(liberalRuleSet, (2,1,0,0), rule2100)

    #
    #  3-----------------------2
    #  |                       |
    #  |                       |
    #  |                       |
    #  d-----------------------c
    #  |*                     *|
    #  |  *                 *  |
    #  |    *             *    |
    #  |      *         *      |
    #  |        *     *        |
    #  0---------a---b---------1
    #

    def rule2101(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+1)%4][0]
        nd = edgenodes[(rotation+3)%4][0]
        return (
            newSkeleton.newElement(nodes=[n0, na, nd], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nc, n2, n3, nd], parents=[element]))
    RefinementRule(liberalRuleSet, (2,1,0,1), rule2101)

    #
    #  3--------------d--------2
    #  |             / *       |
    #  |            /    *     |
    #  |           /       *   |
    #  |          /          * |
    #  |         /             c
    #  |        /             /|
    #  |       /             / |
    #  |      /             /  |
    #  |     /             /   |
    #  0----a-------------b----1
    #

    def rule2110(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+1)%4][0]
        nd = edgenodes[(rotation+2)%4][0]
        return (
            newSkeleton.newElement(nodes=[n0, na, nd, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nd, nc, n2], parents=[element]))
    RefinementRule(liberalRuleSet, (2,1,1,0), rule2110)

    #
    #  3----------d------------2
    #  |       *     *         |
    #  |    *            *     |
    #  | *                  *  |
    #  e-----------------------c
    #  |*                     *|
    #  |  *                 *  |
    #  |    *             *    |
    #  |      *         *      |
    #  |        *     *        |
    #  0---------a---b---------1
    #

    def rule2111(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+1)%4][0]
        nd = edgenodes[(rotation+2)%4][0]
        ne = edgenodes[(rotation+3)%4][0]
        return (
            newSkeleton.newElement(nodes=[n0, na, ne], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, ne], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nc, n2, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nc, nd, ne], parents=[element]),
            newSkeleton.newElement(nodes=[n3, ne, nd], parents=[element]))
    RefinementRule(liberalRuleSet, (2,1,1,1), rule2111)

    ### Quads, cases 22XX ###

    #
    #  3-----------------------2
    #  |\ *                    |
    #  | \     *               |
    #  |  \        *           |
    #  |   \            *      |
    #  |    \                * d
    #  |     \               * |
    #  |      \           *    c
    #  |       \       *     * |
    #  |        \   *      *   |
    #  0---------a--------b----1
    #

    def rule2200(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+1)%4][0]
        nd = edgenodes[(rotation+1)%4][1]
        return (
            newSkeleton.newElement(nodes=[n0, na, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nd, n2, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, nd, n3], parents=[element]))
    RefinementRule(liberalRuleSet, (2,2,0,0), rule2200)

    #
    #  3-----------------------2
    #  |                       |
    #  |                       |
    #  |                       |
    #  |                       |
    #  e-----------------------d
    #  |                     * |
    #  |                  *    c
    #  |               *     * |
    #  |            *      *   |
    #  0---------a--------b----1
    #

    def rule2201(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
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
    RefinementRule(liberalRuleSet, (2,2,0,1), rule2201)

    #
    #  3---------e-------------2
    #  |         |*            |
    #  |         |   *         |
    #  |         |      *      |
    #  |         |         *   |
    #  |         |            *d
    #  |         |           * |
    #  |         |        *    c
    #  |         |     *     * |
    #  |         |  *      *   |
    #  0---------a--------b----1
    #

    def rule2210(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+1)%4][0]
        nd = edgenodes[(rotation+1)%4][1]
        ne = edgenodes[(rotation+2)%4][0]
        return (
            newSkeleton.newElement(nodes=[n0, na, ne, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nd, n2, ne], parents=[element]),
            newSkeleton.newElement(nodes=[na, nd, ne], parents=[element]))
    RefinementRule(liberalRuleSet, (2,2,1,0), rule2210)

    #
    #  3---------e-------------2
    #  |        *\*            |
    #  |      *   \  *         |
    #  |    *      \    *      |
    #  |  *         \      *   |
    #  f *           \        *d
    #  | *            \        |
    #  |   *           \       c
    #  |     *          \    * |
    #  |       *         \ *   |
    #  0---------a--------b----1
    #

    def rule2211(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+1)%4][0]
        nd = edgenodes[(rotation+1)%4][1]
        ne = edgenodes[(rotation+2)%4][0]
        nf = edgenodes[(rotation+3)%4][0]
        return (
            newSkeleton.newElement(nodes=[n0, na, nf], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, ne, nf], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nd, n2, ne], parents=[element]),
            newSkeleton.newElement(nodes=[n3, nf, ne], parents=[element]),
            newSkeleton.newElement(nodes=[ne, nb, nc, nd], parents=[element]))
    RefinementRule(liberalRuleSet, (2,2,1,1), rule2211)

    ### Quads, cases 222X ###

    #
    #  3------f-------e--------2
    #  |      |       |  *     |
    #  |      |       |     *  |
    #  |      |       |       *d
    #  |      |       |        |
    #  |      |       |        |
    #  |      |       |       *c
    #  |      |       |     *  |
    #  |      |       |   *    |
    #  |      |       | *      |
    #  0------a-------b--------1
    #

    def rule2220(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+1)%4][0]
        nd = edgenodes[(rotation+1)%4][1]
        ne = edgenodes[(rotation+2)%4][0]
        nf = edgenodes[(rotation+2)%4][1]
        return (
            newSkeleton.newElement(nodes=[n0, na, nf, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, ne, nf], parents=[element]),
            newSkeleton.newElement(nodes=[nb, nc, nd, ne], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nd, n2, ne], parents=[element]))
    RefinementRule(liberalRuleSet, (2,2,2,0), rule2220)

    #
    #  3------f-------e--------2
    #  |     *|       |  *     |
    #  |      |       |     *  |
    #  |   *  |       |       *d
    #  |      |       |        |
    #  g *    |       |        |
    #  |  *   |       |       *c
    #  |   *  |       |     *  |
    #  |    * |       |   *    |
    #  |     *|       | *      |
    #  0------a-------b--------1
    #

    def rule2221(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+1)%4][0]
        nd = edgenodes[(rotation+1)%4][1]
        ne = edgenodes[(rotation+2)%4][0]
        nf = edgenodes[(rotation+2)%4][1]
        ng = edgenodes[(rotation+3)%4][0]
        return (
            newSkeleton.newElement(nodes=[n0, na, ng], parents=[element]),
            newSkeleton.newElement(nodes=[ng, na, nf], parents=[element]),
            newSkeleton.newElement(nodes=[nf, n3, ng], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, ne, nf], parents=[element]),
            newSkeleton.newElement(nodes=[nb, nc, nd, ne], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nd, n2, ne], parents=[element]))
    RefinementRule(liberalRuleSet, (2,2,2,1), rule2221)

    ### Quads, cases 2X2X ###

    #
    #  3------d-------c--------2
    #  |      |       |        |
    #  |      |       |        |
    #  |      |       |        |
    #  |      |       |        |
    #  |      |       |        |
    #  |      |       |        |
    #  |      |       |        |
    #  |      |       |        |
    #  |      |       |        |
    #  0------a-------b--------1
    #

    def rule2020(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+2)%4][0]
        nd = edgenodes[(rotation+2)%4][1]
        return (
            newSkeleton.newElement(nodes=[n0, na, nd, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, n2, nc], parents=[element]))
    RefinementRule(liberalRuleSet, (2,0,2,0), rule2020)

    #
    #  3------e-------d--------2
    #  |      |       |*       |
    #  |      |       |  *     |
    #  |      |       |    *   |
    #  |      |       |      * |
    #  |      |       |        c
    #  |      |       |      * |
    #  |      |       |    *   |
    #  |      |       |  *     |
    #  |      |       |*       |
    #  0------a-------b--------1
    #

    #The case 2021 should reduce to the ff. case.
    def rule2120(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+1)%4][0]
        nd = edgenodes[(rotation+2)%4][0]
        ne = edgenodes[(rotation+2)%4][1]
        return (
            newSkeleton.newElement(nodes=[n0, na, ne, n3], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nd, ne], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nc, n2, nd], parents=[element]))
    RefinementRule(liberalRuleSet, (2,1,2,0), rule2120)

    #
    #  3------e-------d--------2
    #  |               *       |
    #  |   *             *     |
    #  |                   *   |
    #  |*                    * |
    #  f---------------------- c
    #  |*                    * |
    #  |                   *   |
    #  |   *             *     |
    #  |               *       |
    #  0------a-------b--------1
    #

    def rule2121(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+1)%4][0]
        nd = edgenodes[(rotation+2)%4][0]
        ne = edgenodes[(rotation+2)%4][1]
        nf = edgenodes[(rotation+3)%4][0]
        return (
            newSkeleton.newElement(nodes=[nf, nc, nd, ne], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nf], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nd, nc, n2], parents=[element]),
            newSkeleton.newElement(nodes=[n0, na, nf], parents=[element]),
            newSkeleton.newElement(nodes=[nf, ne, n3], parents=[element]))
    RefinementRule(liberalRuleSet, (2,1,2,1), rule2121)

    ### Quad, case 2222 ###


    #
    #  3------f-------e--------2
    #  |    * |       |  *     |
    #  |  *   |       |     *  |
    #  g*     |       |       *d
    #  |      |       |        |
    #  h*     |       |        |
    #  |      |       |       *c
    #  |  *   |       |     *  |
    #  |      |       |   *    |
    #  |     *|       | *      |
    #  0------a-------b--------1
    #

    def rule2222(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2, n3 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+1)%4][0]
        nd = edgenodes[(rotation+1)%4][1]
        ne = edgenodes[(rotation+2)%4][0]
        nf = edgenodes[(rotation+2)%4][1]
        ng = edgenodes[(rotation+3)%4][0]
        nh = edgenodes[(rotation+3)%4][1]
        return (
            newSkeleton.newElement(nodes=[na, nf, ng, nh], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, ne, nf], parents=[element]),
            newSkeleton.newElement(nodes=[nb, nc, nd, ne], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nd, n2, ne], parents=[element]),
            newSkeleton.newElement(nodes=[n0, na, nh], parents=[element]),
            newSkeleton.newElement(nodes=[ng, nf, n3], parents=[element]))
    RefinementRule(liberalRuleSet, (2,2,2,2), rule2222)

    ### Triangles, cases 2XX ###

    #                
    #                2
    #               /\
    #              /  \
    #             /    \
    #            / *  * \
    #           /        \
    #          /          \
    #         /   *    *   \
    #        /              \ 
    #       /                \
    #      /_____*______*_____\
    #      0     a       b     1
    #

    def rule200(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        return (
            newSkeleton.newElement(nodes=[n0, na, n2], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, n2], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, n2], parents=[element]))
    RefinementRule(liberalRuleSet, (2,0,0), rule200)

    #                
    #                2
    #               /\
    #              /  \
    #             /    \
    #            c      \
    #           /|\      \
    #          / | \      \
    #         /  |  \      \
    #        /   |   \      \ 
    #       /    |    \      \
    #      /_____|_____\______\
    #      0     a       b     1
    #

    def rule201(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+2)%3][0]
        return (
            newSkeleton.newElement(nodes=[n0, na, nc], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc], parents=[element]),
            newSkeleton.newElement(nodes=[nb, n1, n2, nc], parents=[element]))
    RefinementRule(liberalRuleSet, (2,0,1), rule201)

    #                
    #                2
    #               /\
    #              /  \
    #             /    \
    #            /      \
    #           /        c
    #          /        /|\
    #         /        / | \
    #        /        /  |  \ 
    #       /        /   |   \
    #      /________/____|____\
    #      0       a     b     1
    #

    def rule210(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+1)%3][0]
        return (
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc], parents=[element]),
            newSkeleton.newElement(nodes=[n0, na, nc, n2], parents=[element]))
    RefinementRule(liberalRuleSet, (2,1,0), rule210)

    #                
    #                2
    #               /\
    #              /  \
    #             /    \
    #            /      \
    #           d--------c
    #          /|        |\
    #         / |        | \
    #        /  |        |  \ 
    #       /   |        |   \
    #      /____|________|____\
    #      0    a        b     1
    #

    def rule211(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+1)%3][0]
        nd = edgenodes[(rotation+2)%3][0]
        return (
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[n0, na, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nc, n2, nd], parents=[element]))
    RefinementRule(liberalRuleSet, (2,1,1), rule211)

    ### Triangles, cases 22X ###

    #                
    #                2
    #               /\
    #              /  \
    #             /    \
    #            /      \
    #           /        d
    #          /        / \
    #         /        /   \
    #        /        /    /c 
    #       /        /    /  \
    #      /________/____/____\
    #      0       a     b     1
    #

    def rule220(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+1)%3][0]
        nd = edgenodes[(rotation+1)%3][1]
        return (
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[n0, na, nd, n2], parents=[element]))
    RefinementRule(liberalRuleSet, (2,2,0), rule220)

    #                
    #                2
    #               /\
    #              /  \
    #             /    \
    #            /      \
    #           e------- d
    #          /*       / \
    #         /        /   \
    #        /   *    /    /c 
    #       /        /    /  \
    #      /______*_/____/____\
    #      0       a     b     1
    #

    def rule221(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+1)%3][0]
        nd = edgenodes[(rotation+1)%3][1]
        ne = edgenodes[(rotation+2)%3][0]
        return (
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nd], parents=[element]),
            newSkeleton.newElement(nodes=[n0, na, ne], parents=[element]),
            newSkeleton.newElement(nodes=[ne, na, nd], parents=[element]),
            newSkeleton.newElement(nodes=[nd, n2, ne], parents=[element]))
    RefinementRule(liberalRuleSet, (2,2,1), rule221)

    ### Triangle, case 222 ###

    #                
    #                2
    #               /\
    #              /  \
    #             /    \
    #            /      \
    #           e--------d
    #          /          \
    #         /            \
    #        f--------------c 
    #       / \           /  \
    #      /___\_________/____\
    #      0    a        b     1
    #

    def rule222(element, rotation, cats, edgenodes, newSkeleton, maxdelta2):
        n0, n1, n2 = baseNodes(element, rotation)
        na = edgenodes[rotation][0]
        nb = edgenodes[rotation][1]
        nc = edgenodes[(rotation+1)%3][0]
        nd = edgenodes[(rotation+1)%3][1]
        ne = edgenodes[(rotation+2)%3][0]
        nf = edgenodes[(rotation+2)%3][1]
        return (
            newSkeleton.newElement(nodes=[nb, n1, nc], parents=[element]),
            newSkeleton.newElement(nodes=[na, nb, nc, nf], parents=[element]),
            newSkeleton.newElement(nodes=[n0, na, nf], parents=[element]),
            newSkeleton.newElement(nodes=[ne, nd, n2], parents=[element]),
            newSkeleton.newElement(nodes=[nf, nc, nd, ne], parents=[element]))
    RefinementRule(liberalRuleSet, (2,2,2), rule222)

#######################################################
#
#               BEGIN 3D RULES
#
#######################################################
# TODO: some code overlaps with refinemethod -- it should be combined
# when moving to C

elif config.dimension() == 3:

    def zeroEdgeMarkings(element, signature, cats, edgenodes, newSkeleton, maxdelta2):
        numcats = len(set(cats))
        bNodes = baseNodes(element)
        if numcats == 1:
            return (newSkeleton.newElement(nodes=bNodes, parents=[element]),)
        #print cats, set(cats), numcats
        sets = set(cats)
        cat1 = sets.pop()
        cat2 = sets.pop()
        if numcats == 2:
            #print cats.count(cat1), cats.count(cat2)
            idxs1 = [i for i in range(6) if cats[i] == cat1]
            idxs2 = [i for i in range(6) if cats[i] == cat2]
            if len(idxs1) > len(idxs2):
                temp = idxs1
                idxs1 = idxs2
                idxs2 = temp
            #if len(idxs1) == 1:
                #print idxs1, idxs2
        return []
    RefinementRule(conservativeRuleSet, [()], zeroEdgeMarkings)


    def singleEdge(element, signature, cats, edgenodes, newSkeleton, maxdelta2):
        ne = edgenodes[signature[0]][0]
        bNodes = baseNodes(element)
        idxs = element.segToNodeMap()[signature[0]]
        numcats = len(set(cats))
        #print signature, numcats, idxs[0], idxs[1], ne.position()
        #for node in bNodes:
        #    print node.position()
        if numcats == 2:
            nodes1 = bNodes[:]
            nodes1[idxs[0]] = ne
            nodes2 = bNodes[:]
            nodes2[idxs[1]] = ne
            el1 = newSkeleton.newElement(nodes1, parents=[element])
            el2 = newSkeleton.newElement(nodes2, parents=[element])
            return (el1,el2)      
        else:
            return []
    RefinementRule(conservativeRuleSet, [(0,),(1,),(2,),(3,),(4,),(5,)], singleEdge)

    def twoEdgeAdjacent(element, signature, cats, edgenodes, newSkeleton, maxdelta2):
#        print "twoEdgeAdjacent"
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

        return []
    RefinementRule(conservativeRuleSet, [(0,1), (0,2), (0,3), (0,4), (1,2), (1,4),
                                         (1,5), (2,3), (2,5), (3,4), (3,5), (4,5)],
                   twoEdgeAdjacent)


    def twoEdgeOpposite(element, signature, cats, edgenodes, newSkeleton, maxdelta2):
#        print "twoEdgeOpposite"
        return []    
    RefinementRule(conservativeRuleSet, [(0,5), (1,3), (2,4)], twoEdgeOpposite)


    def threeEdgeTriangle(element, signature, cats, edgenodes, newSkeleton, maxdelta2):
#        print "threeEdgeTriangle"
        return []
    RefinementRule(conservativeRuleSet, [(0,3,4), (0,1,2), (2,3,5), (1,4,5)],
                   threeEdgeTriangle)


    def threeEdgeZigZag(element, signature, cats, edgenodes, newSkeleton, maxdelta2):
#        print "threeEdgeZigZag"
        return []    
    RefinementRule(conservativeRuleSet, [(0,2,4), (0,1,5), (0,1,3), (1,2,4), (0,2,5), 
                                         (1,2,3), (1,3,5), (2,3,4), (0,4,5), (1,3,4), 
                                         (0,3,5), (2,4,5)], threeEdgeZigZag)


    def threeEdgeOnePoint(element, signature, cats, edgenodes, newSkeleton, maxdelta2):
#        print "threeEdgeOnePoint"
        return []    
    RefinementRule(conservativeRuleSet, [(3,4,5), (0,1,4), (0,2,3), (1,2,5)],
                   threeEdgeOnePoint)


    def fourEdges1(element, signature, cats, edgenodes, newSkeleton, maxdelta2):
#        print "fourEdges1"
        return []    
    RefinementRule(conservativeRuleSet, [(0,1,3,4), (0,2,3,4), (0,3,4,5), (0,1,4,5),
                                         (1,2,4,5), (1,3,4,5), (0,2,3,5), (1,2,3,5), 
                                         (2,3,4,5), (0,1,2,3), (0,1,2,4), (0,1,2,5)],
                   fourEdges1)

    def fourEdges2(element, signature, cats, edgenodes, newSkeleton, maxdelta2):
#        print "fourEdges2"
        return [] 
    RefinementRule(conservativeRuleSet, [(1,2,3,4), (0,2,4,5), (0,1,3,5)],
                   fourEdges2)



    def fiveEdges(element, signature, cats, edgenodes, newSkeleton, maxdelta2):
#        print "fiveEdges"
        return []              
    RefinementRule(conservativeRuleSet, [(0,1,2,3,4),(0,1,2,3,5),(0,1,2,4,5),
                                         (0,1,3,4,5),(0,2,3,4,5),(1,2,3,4,5)], 
                   fiveEdges)

       
    def sixEdges(element, signature, cats, edgenodes, newSkeleton, maxdelta2):
#        print "sixEdges!"
        return []  
    RefinementRule(conservativeRuleSet, [(0,1,2,3,4,5)], 
                   sixEdges)

    deadlockableSignatures = [(3,4,5), (0,1,4), (0,2,3), (1,2,5),
                              (1,2,3,4), (0,2,4,5), (0,1,3,5)]
