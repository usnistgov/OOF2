# -*- python -*-
# $RCSfile: meshwidget.py,v $
# $Revision: 1.7 $
# $Author: langer $
# $Date: 2009/07/08 21:44:40 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Widget for the SyncMeshParameter, which only allows Meshes which
# aren't currently out-of-sync.

from ooflib.common.IO import whoville
from ooflib.common.IO.GUI import whowidget
from ooflib.engine import mesh

def _nsync(who):
    return whoville.excludeProxies(who) and not (who.getClass() is mesh.meshes
                                                 and who.outOfSync())

class SyncMeshWidget(whowidget.WhoParameterWidget):
    def __init__(self, value=None, scope=None, name=None, sort=None):
        whowidget.WhoParameterWidget.__init__(
            self, mesh.meshes, value=value, scope=scope, name=name, sort=sort,
            condition=_nsync)

def _makeSMW(self, scope=None):
    return SyncMeshWidget(self.value, scope=scope, name=self.name)

mesh.SyncMeshParameter.makeWidget = _makeSMW
