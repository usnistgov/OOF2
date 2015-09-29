# -*- python -*-
# $RCSfile: animationstyle.py,v $
# $Revision: 1.4 $
# $Author: langer $
# $Date: 2011/04/24 03:52:12 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import progress
from ooflib.common import registeredclass
from ooflib.common import utils

class AnimationStyle(registeredclass.RegisteredClass):
    registry = []
    tip="Ways of animating time dependent solutions"
    discussion=\
"""<para>This class describes different ways of running animations of
time dependent solutions.  It's used by <xref
linkend="MenuItem-OOF.Graphics_n.File.Animate"/>.</para>"""

class IndefiniteAnimation(AnimationStyle):
    def getProgressStyle(self):
        return progress.INDEFINITE

class FiniteAnimation(AnimationStyle):
    def getProgressStyle(self):
        return progress.DEFINITE

#########

class ForwardAnimation(FiniteAnimation):
    def getTimes(self, times):
        for t in times:
            yield t

registeredclass.Registration(
    'Forward',
    AnimationStyle,
    ForwardAnimation,
    ordering=0,
    tip="Run the animation once.",
    discussion=
    "<para>Run the animation only once, in the forward direction.</para>"
    )
    

#########

class ReverseAnimation(FiniteAnimation):
    def getTimes(self, times):
        return reversed(utils.degenerate(times))

registeredclass.Registration(
    'Reverse',
    AnimationStyle,
    ReverseAnimation,
    ordering=1,
    tip="Run the animation once in reverse.",
    discussion="<para>Run the animation only once, in reverse.</para>")

#########

class LoopAnimation(IndefiniteAnimation):
    def getTimes(self, times):
        times = utils.degenerate(times)
        while True:
            for t in times:
                yield t

registeredclass.Registration(
    'Loop',
    AnimationStyle,
    LoopAnimation,
    ordering=2,
    tip="Run the animation indefinitely.",
    discussion="""
<para>Run the animation repeatedly, in the forward direction each
time.  To make it stop, use the <guibutton>Stop</guibutton> button in
the <xref linkend="Section-Windows-ActivityViewer"/>.</para>"""
    )

#########

class BackAndForthAnimation(IndefiniteAnimation):
    def getTimes(self, times):
        times = utils.degenerate(times)
        n = len(times)
        if n == 0:
            return
        i = 0
        step = 1
        while True:
            yield times[i]
            i += step
            if i == n or i == -1:
                step *= -1
                i += 2*step

registeredclass.Registration(
    'Back and Forth',
    AnimationStyle,
    BackAndForthAnimation,
    ordering=3,
    tip="Run the animation forward, then backwards, then forwards again, ad infinitum.",
    discussion=
"""<para>Run the animation repeatedly, switching directions each time.
 To make it stop, use the <guibutton>Stop</guibutton> button in the
 <xref linkend="Section-Windows-ActivityViewer"/>.</para>"""
    )
            
