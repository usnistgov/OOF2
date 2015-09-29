# -*- python -*- 
# $RCSfile: DIR.py,v $
# $Revision: 1.31 $
# $Author: langer $
# $Date: 2014/09/27 21:40:15 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

dirname = 'common'
subdirs = ['IO', 'EXTRA']
if not DIM_3:
    clib = 'oof2common'
else:
    clib = 'oof3dcommon'
clib_order = 0

if not DIM_3:

    cfiles = [
        'activearea.C', 'argv.C', 'bitmask.C', 'boolarray.C',
        'brushstyle.C', 'ccolor.C', 'cdebug.C', 'cmicrostructure.C',
        'colordifference.C', 'coord.C', 'cpixelselection.C', 'despeckle.C',
        'expandgrp.C', 'identification.C', 'intarray.C', 'lock.C',
        'ooferror.C', 'pixelattribute.C', 'pixelgroup.C', 'guitop.C',
        'pixelselectioncourier.C', 'pixelsetboundary.C', 'random.C',
        'sincos.C', 'swiglib.C', 'switchboard.C', 'threadstate.C',
        'timestamp.C', 'trace.C', 'pythonlock.C', 'progress.C',
        'direction.C', 'doublevec.C', 'smallmatrix.C', 'vectormath.C',
        'corientation.C',
        ]

    swigfiles = [
        'abstractimage.swg', 'activearea.swg', 'argv.swg',
        'boolarray.swg', 'brushstyle.swg', 'ccolor.swg', 'cdebug.swg',
        'cmicrostructure.swg', 'colordifference.swg', 'config.swg',
        'coord.swg', 'cpixelselection.swg', 'crandom.swg',
        'doublearray.swg', 'geometry.swg', 'intarray.swg', 'lock.swg',
        'ooferror.swg', 'pixelattribute.swg', 'pixelgroup.swg',
        'pixelselectioncourier.swg', 'switchboard.swg',
        'threadstate.swg', 'timestamp.swg', 'trace.swg', 'progress.swg',
        'guitop.swg', 'identification.swg', 'direction.swg', 'doublevec.swg',
        'smallmatrix.swg', 'corientation.swg',
        ]

    pyfiles = [ 
        'activeareamod.py', 'backEnd.py', 'color.py', 'cregisteredclass.py',
        'debug.py', 'director.py', 'enum.py', 'excepthook.py', 'garbage.py'
        'initialize.py', 'labeltree.py', 'mainthread.py',
        'microstructure.py', 'object_id.py', 'oof.py', 'oof_getopt.py',
        'oofversion.py', 'parallel_enable.py', 'parallel_object_manager.py',
        'parallel_performance.py', 'pixelselection.py', 'threadmanager.py',
        'pixelselectionmethod.py', 'pixelselectionmod.py', 'primitives.py',
        'quit.py', 'registeredclass.py', 'ringbuffer.py', 'strfunction.py',
        'subthread.py', 'thread_enable.py', 'timer.py', 'toolbox.py',
        'utils.py', 'version.py', 'worker.py', 'runtimeflags.py']

    swigpyfiles = [
        'ooferror.spy', 'colordifference.spy', 'coord.spy', 'geometry.spy',
        'switchboard.spy', 'pixelgroup.spy', 'timestamp.spy',
        'cdebug.spy', 'brushstyle.spy', 'pixelattribute.spy', 'guitop.spy',
        'activearea.spy', 'lock.spy', 'cmicrostructure.spy', 'doublevec.spy',
        'smallmatrix.spy',  'corientation.spy', 'direction.spy']


    hfiles = [
        'abstractimage.h', 'activearea.h', 'argv.h', 'array.h', 'bitmask.h',
        'boolarray.h', 'brushstyle.h', 'cachedvalue.h', 'ccolor.h',
        'cdebug.h', 'cmicrostructure.h', 'colordifference.h', 'coord.h',
        'cpixelselection.h', 'doublearray.h', 'geometry.h', 'guitop.h',
        'identification.h', 'intarray.h', 'lock.h', 'ooferror.h',
        'pixelattribute.h', 'pixelgroup.h', 'pixelselectioncourier.h',
        'pixelsetboundary.h', 'printvec.h', 'pythonexportable.h', 'random.h',
        'removeitem.h', 'sincos.h', 'swiglib.h', 'switchboard.h',
        'threadstate.h', 'timestamp.h', 'tostring.h', 'trace.h',
        'pythonlock.h', 'direction.h', 'doublevec.h', 'smallmatrix.h',
        'vectormath.h', 'corientation.h',]

else:

#     not in cfiles for 3D ['bitmask.C', 'brushstyle.C','despeckle.C',
#                           'expandgrp.C', 'intarray.C',
#                           'sincos.C']

    cfiles = [
        'activearea.C', 'argv.C', 'boolarray.C', 'cdebug.C', 'ccolor.C',
        'cmicrostructure.C', 'colordifference.C', 'coord.C',
        'cpixelselection.C', 'identification.C', 'lock.C', 'ooferror.C', 'pixelattribute.C',
        'pixelgroup.C', 'pixelselectioncourier.C', 'pixelsetboundary.C',
        'random.C', 'swiglib.C', 'switchboard.C', 'threadstate.C',
        'timestamp.C', 'pythonlock.C' ]

    swigfiles = [
        'abstractimage.swg', 'activearea.swg', 'argv.swg', 'boolarray.swg',
        'cdebug.swg', 'ccolor.swg','cmicrostructure.swg', 'colordifference.swg',
        'config.swg', 'coord.swg', 'cpixelselection.swg', 'crandom.swg',
        'doublearray.swg', 'geometry.swg', 'lock.swg', 'ooferror.swg',
        'pixelattribute.swg', 'pixelgroup.swg', 'pixelselectioncourier.swg',
        'switchboard.swg', 'threadstate.swg', 'timestamp.swg', ]

    pyfiles = [
        'color.py', 'debug.py', 'excepthook.py', 'garbage.py',
        'oof_getopt.py', 'oofversion.py', 'parallel_enable.py', 'quit.py',
        'subthread.py', 'thread_enable.py', 'utils.py', 'worker.py', ]

    swigpyfiles = [
        'activearea.spy', 'cmicrostructure.spy', 'colordifference.spy',
        'coord.spy', 'geometry.spy', 'lock.spy', 'ooferror.spy',
        'pixelattribute.spy', 'pixelgroup.spy', 'switchboard.spy', ]

    hfiles = [
        'abstractimage.h', 'activearea.h', 'argv.h', 'boolarray.h', 'cdebug.swg',
        'ccolor.h', 'cmicrostructure.h', 'colordifference.h', 'coord.h',
        'cpixelselection.h', 'doublearray.h', 'geometry.h', 'identification.h', 'lock.h',
        'ooferror.h', 'pixelattribute.h', 'pixelgroup.h',
        'pixelselectioncourier.h', 'pixelsetboundary.h', 'random.h',
        'swiglib.h', 'switchboard.h', 'threadstate.h', 'timestamp.h',
        'pythonlock.h', 'progress.h']


if HAVE_MPI:
    cfiles.extend(['mpitools.C'])
    swigfiles.extend(['mpitools.swg'])
    swigpyfiles.extend(['mpitools.spy'])
    hfiles.extend(['mpitools.h'])

def set_clib_flags(clib):
    if HAVE_MPI:
        clib.externalLibs.append('pmpich++')
        clib.externalLibs.append('mpich')
