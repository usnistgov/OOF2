# -*- python -*-
# $RCSfile: animationtimes.py,v $
# $Revision: 1.9 $
# $Author: langer $
# $Date: 2011/04/29 20:22:42 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.common import debug
from ooflib.common import registeredclass
from ooflib.common.IO import parameter
from ooflib.common.IO import placeholder
from ooflib.common.IO import xmlmenudump

# AnimationTimes specifies which times to use for the frames of an
# animation.  Each subclass must have a function, times(), that
# returns the times, given a start and finish time.  times() may be a
# generator function.

## TODO: Add a subclass that uses a list of specific user-provided
## times.

class AnimationTimes(registeredclass.RegisteredClass):
    registry = []
    tip="Ways to choose frames for an animation."
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/reg/animationtimes.xml')

def isPlaceHolder(time):
    return (time is placeholder.earliest or
            time is placeholder.latest)

def resolvePlaceHolder(time, times):
    if time is placeholder.earliest: 
        return times[0]
    if time is placeholder.latest:
        return times[-1]
    return time

class FixedFrames(AnimationTimes):
    def __init__(self, nframes):
        self.nframes = nframes
    def times(self, start, finish, gfxwindow):
        if isPlaceHolder(start) or isPlaceHolder(finish):
            alltimes = gfxwindow.findAnimationTimes()
            start = resolvePlaceHolder(start, alltimes)
            finish = resolvePlaceHolder(finish, alltimes)
        nframes = max(self.nframes, 2)
        dt = (finish - start)/(nframes - 1)
        for i in xrange(nframes - 1):
            yield start + dt*i
        yield finish            # avoid round off, hit finish exactly.
        
registeredclass.Registration(
    "Fixed Number of Frames",
    AnimationTimes,
    FixedFrames,
    params=[parameter.IntParameter(
            'nframes', 10, tip='Number of frames to display.')],
    ordering=2,
    tip="Generate the specified number of uniformly spaced frames.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/reg/fixedframes.xml'))
                                   
class FixedSpacing(AnimationTimes):
    def __init__(self, dt):
        self.dt = dt
    def times(self, start, finish, gfxwindow):
        if isPlaceHolder(start) or isPlaceHolder(finish):
            alltimes = gfxwindow.findAnimationTimes()
            start = resolvePlaceHolder(start, alltimes)
            finish = resolvePlaceHolder(finish, alltimes)
        t = start
        while t < finish:
            ## TODO: Don't return t if finish-t < machine epsilon
            yield t
            t += self.dt
        # If final step overstepped the finish, time, take a shorter
        # step and hit it exactly.
        if t >= finish:
            yield finish
    
registeredclass.Registration(
    "Fixed Time Between Frames",
    AnimationTimes,
    FixedSpacing,
    params=[parameter.FloatParameter(
            'dt', 0.01, tip='Time difference between consecutive frames.')],
    ordering=3,
    tip="Generate frames at the specified time interval.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/reg/fixedspacing.xml'))
