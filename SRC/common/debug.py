# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import threadstate
from ooflib.common import mainthread
from ooflib.common import parallel_enable
from ooflib.common import thread_enable
import ooflib.SWIG.common.lock

import gc
import os
import string
import sys
import traceback
import types



_debug_mode = 0

# The lock makes sure that threads don't intermix their debug lines.
lock = ooflib.SWIG.common.lock.SLock()

##class DebugLock:
##    # A rather insecure lock for debugging purposes.
##    def acquire(self): pass
##    def release(self): pass
##lock = DebugLock()
##print >> sys.stderr, "******* NOT using debug.lock! *********"

def set_debug_mode():
    global _debug_mode
    _debug_mode = 1

def clear_debug_mode():
    global _debug_mode
    _debug_mode = 0

def debug():
    return _debug_mode

def dumpTrace(start=0, end=-1):
    ## Use start=-3, end=-2 if you only want to see the calling
    ## function of the function that calls dumpTrace.
    lock.acquire()
    try:
        stack = traceback.extract_stack()
        depth = len(stack)
        thread = threadstate.findThreadNumber()
        if parallel_enable.enabled():
            from ooflib.SWIG.common import mpitools
            rank="%02d" % mpitools.Rank()
        else:
            rank='--'
            
        lines = ['+++-%04d-%02d-%s--------- debug.dumpTrace --------------'
                 % (depth, thread, rank)
                 ]
        for line in stack[start:end]:
            lines.append('+++%30s:%3d\t%s\t\t%s' % (line[0],line[1],
                                                        line[2],line[3]))
        lines.append('+++-------------- end trace -----------------')
        print(string.join(lines, '\n'), file=sys.stderr)
    finally:
        lock.release()

def dumpCaller(offset=0):
    if _debug_mode:
        print(callerID(-4-offset), file=sys.stderr)

def callerID(depth=-3):
    if _debug_mode:
        lock.acquire()
        try:
            stack = traceback.extract_stack()
            thread = threadstate.findThreadNumber()
            if parallel_enable.enabled():
                from ooflib.SWIG.common import mpitools
                rank = "%02d" % mpitools.Rank()
            else:
                rank = ""
            line = stack[depth]
            return '+++%02d++%s+++%30s:%3d\t%s\t\t%s' % \
                  (thread, rank, line[0], line[1], line[2], line[3])
        finally:
            lock.release()


def msg(*args):
    if _debug_mode:
        lock.acquire()
        try:
            stack = traceback.extract_stack()
            depth = len(stack)
            thread = threadstate.findThreadNumber()
            if parallel_enable.enabled():
                from ooflib.SWIG.common import mpitools
                rank="%02d" % mpitools.Rank()
            else:
                rank='--'
            print(('-%04d-%02d-%s'%(depth,thread,rank))+'-'*(depth-1), \
                  string.join(list(map(str, args)), ' '), file=sys.stderr)
        finally:
            lock.release()

def fmsg(*args):
    ## Importing ooferror here hangs the program when a binary data
    ## file is loaded if fmsg is used in OOFIdleCallback.  WTF?  There
    ## may be no real need to import ooferror here, but it was
    ## imported here once, and mysteriously caused a problem.
    ## (There's a comment in mainthreadGUI that refers to this
    ## comment.)
#     from ooflib.SWIG.common import ooferror
    if _debug_mode:
        lock.acquire()
        try:
            stack = traceback.extract_stack()
            depth = len(stack)
            filename = string.split(stack[-2][0], '/')[-1]
            func = stack[-2][2]
            line = stack[-2][1]
            try:
                thread = "%02d"% threadstate.findThreadNumber()
            except:
                thread = '??'
            if parallel_enable.enabled():
                from ooflib.SWIG.common import mpitools
                rank="%02d" % mpitools.Rank()
            else:
                rank='--'
            print(('-%04d-%s-%s'%(depth,thread,rank))+'-'*(depth-1), \
                  '%s(%d):%s'%(filename, line, func),\
                  string.join(list(map(str, args)), ' '), file=sys.stderr)
        finally:
            lock.release()


def mainthreadTest():
    if _debug_mode:
        if not mainthread.mainthread():
            fmsg("NOT IN MAIN THREAD")
            dumpTrace()
            os.abort()

def subthreadTest():
    if _debug_mode:
        if thread_enable.query() and mainthread.mainthread():
            fmsg("IN MAIN THREAD")
            dumpTrace()
            os.abort()

############################

def dumpReferrers(obj, levels=0, exclude=[], _level=0):
    if _debug_mode:
        refs = gc.get_referrers(obj)
        if _level==0:
            print(len(refs), "references", \
                [type(ref) for ref in refs], file=sys.stderr)
        for ref in refs:
            reftype = type(ref)
            if reftype is types.FrameType:
                print("-> %2d"%_level, "  "*_level, end=' ', file=sys.stderr)
                print("frame", ref.f_code.co_filename, \
                    ref.f_code.co_name, ref.f_lineno, file=sys.stderr)
            elif ref is not obj and ref not in exclude:
                print("-> %2d"%_level, "  "*_level, end=' ', file=sys.stderr)
                if reftype is types.InstanceType:
                    print("instance", ref.__class__.__name__, ref, file=sys.stderr)
                elif reftype is dict:
                    for key,val in list(ref.items()):
                        if key is obj:
                            print("dict key", file=sys.stderr)
                            break
                        if val is obj:
                            print("dict val, key =", key, file=sys.stderr)
                            break
                    else:
                        print("obj not found in dict?", file=sys.stderr)
#                     if ref is globals():
#                         print >> sys.stderr, "globals"
#                     elif ref is locals():
#                         print >> sys.stderr, "locals"
#                 elif reftype is types.FrameType:
#                     print >> sys.stderr, "frame", dir(ref)
                else:
                    print("other", type(ref), ref, file=sys.stderr)
                if _level < levels:
                    dumpReferrers(ref, levels,
                                  exclude=exclude+[locals(), refs], 
                                  _level=_level+1)


