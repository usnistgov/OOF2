# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

## Store and retrieve named sets of analysis parameters

from ooflib.SWIG.common import lock
from ooflib.common import debug
from ooflib.common import registeredclass
from ooflib.common import utils
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
from ooflib.engine import mesh
from ooflib.engine import meshbdyanalysis
from ooflib.engine.IO import analyze
from ooflib.engine.IO import scheduledoutput
from ooflib.engine.IO import outputdestination

import itertools

namelock = lock.SLock()

class _nameResolver:
    # Callable object for creating a unique name for a bulk or
    # boundary analysis.  
    def __init__(self, defaultname):
        self.defaultname = defaultname
    def __call__(self, param, name):
        if param.automatic():
            basename = self.defaultname
        else:
            basename = name
        return utils.uniqueName(
            basename,
            itertools.chain(
                NamedBulkAnalysis.allAnalyses.keys(),
                NamedBdyAnalysis.allAnalyses.keys()))
                
nameResolver = _nameResolver('analysis')
bdynameResolver = _nameResolver('bdy_analysis')

class NamedAnalysis:
    def __init__(self, name):
        self.name = name
        namelock.acquire()
        try:
            self.allAnalyses[name] = self
        finally:
            namelock.release()
    def destroy(self):
        namelock.acquire()
        # Remove from all OutputSchedules.  Each Mesh has a single
        # OutputSchedule, which may or may not use this NamedAnalysis.
        for msh in mesh.meshes.actualMembers():
            msh.outputSchedule.removeNamedAnalysis(self.name)
        # Remove from the list of all named analyses.
        try:
            del self.allAnalyses[self.name]
        finally:
            namelock.release()
        
        

class NamedBulkAnalysis(NamedAnalysis):
    allAnalyses = {}
    def __init__(self, name, operation, data, domain, sampling):
        NamedAnalysis.__init__(self, name)
        self.operation = operation
        self.data = data
        self.domain = domain
        self.sampling = sampling
    def start(self, meshcontext, time, continuing):
        self.domain.set_mesh(meshcontext.path())
        self.sampling.make_samples(self.domain)
    def perform(self, namedoutput, meshcontext, time, destination):
        self.domain.set_mesh(meshcontext.path())
        self.domain.read_lock()
        try:
            self.operation(time, self.data, self.domain, self.sampling,
                           destination)
        finally:
            self.domain.read_release()
    def finish(self, meshcontext):
        self.domain.set_mesh(None)

    def printHeaders(self, destination):
        from ooflib.engine.IO import analyzemenu
        analyzemenu.printBulkHeaders(destination, self.operation, self.data,
                                     self.domain, self.sampling)

class NamedBdyAnalysis(NamedAnalysis):
    allAnalyses = {}
    def __init__(self, name, boundary, analyzer):
        NamedAnalysis.__init__(self, name)
        self.boundary = boundary
        self.analyzer = analyzer
    def start(self, meshcontext, time, continuing):
        pass
    def perform(self, namedoutput, meshcontext, time, destination):
        self.analyzer.analyze(meshcontext, time, self.boundary, destination)
    def finish(self, meshcontext):
        pass
    def printHeaders(self, destination):
        self.analyzer.printHeaders(destination, self.boundary)

def getNamedBulkAnalysis(name):
    return NamedBulkAnalysis.allAnalyses[name]

def getNamedBdyAnalysis(name):
    return NamedBdyAnalysis.allAnalyses[name]

def getNamedAnalysis(name):
    try:
        return NamedBulkAnalysis.allAnalyses[name]
    except KeyError:
        return NamedBdyAnalysis.allAnalyses[name]

def bulkAnalysisNames():
    return list(NamedBulkAnalysis.allAnalyses.keys())

def bdyAnalysisNames():
    return list(NamedBdyAnalysis.allAnalyses.keys())

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def findNamedBulkAnalysis(operation, data, domain, sampling):
    for name, analysis in NamedBulkAnalysis.allAnalyses.items():
        if (analysis.operation == operation and
            analysis.data == data and
            analysis.domain == domain and
            analysis.sampling == sampling):
            return name
    return None

def findNamedBdyAnalysis(boundary, analyzer):
    for name, analysis in NamedBdyAnalysis.allAnalyses.items():
        if (analysis.boundary == boundary and
            analysis.analyzer == analyzer):
            return name
    return None

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class AnalysisNamesParameter(parameter.ListOfStringsParameter):
    pass
class AnalysisNameParameter(parameter.StringParameter):
    pass

class BulkAnalysisNamesParameter(parameter.ListOfStringsParameter):
    pass
class BulkAnalysisNameParameter(parameter.StringParameter):
    pass

class BdyAnalysisNamesParameter(parameter.ListOfStringsParameter):
    pass
class BdyAnalysisNameParameter(parameter.StringParameter):
    pass


class NamedAnalysisOutput(scheduledoutput.ScheduledOutput):
    # Performs either Bulk or Bdy analyses
    def __init__(self, analysis):
        self.analysis = analysis # just the name
        self.analysisObj = getNamedAnalysis(analysis)
        scheduledoutput.ScheduledOutput.__init__(self)
    def start(self, meshcontext, time, continuing):
        self.analysisObj.start(meshcontext, time, continuing)
        scheduledoutput.ScheduledOutput.start(self, meshcontext, time,
                                              continuing)
    def perform(self, meshcontext, time):
        self.destination.printHeadersIfNeeded(self)
        self.analysisObj.perform(self, meshcontext, time, self.destination)
    def finish(self, meshcontext):
        self.analysisObj.finish(meshcontext)
        scheduledoutput.ScheduledOutput.finish(self, meshcontext)
    def defaultName(self):
        return self.analysis
    def printHeaders(self, destination):
        self.analysisObj.printHeaders(destination)
    def save(self, datafile, meshctxt):
        # Before saving the ScheduledOutput, make sure the named
        # analysis is in the data file.
        from ooflib.engine.IO import analyzemenu
        analyzemenu.saveAnalysisDef(datafile, self.analysis)
        scheduledoutput.ScheduledOutput.save(self, datafile, meshctxt)

registeredclass.Registration(
    "Named Analysis",
    scheduledoutput.ScheduledOutput,
    NamedAnalysisOutput,
    ordering=3,
    destinationClass=outputdestination.TextOutputDestination,
    params=[
        AnalysisNameParameter(
            "analysis", 
            tip="Name of the analysis operation to perform.  Named analyses can be created on the Analysis and Boundary Analysis Pages.")
        ],
    tip="Use a predefined bulk or boundary Analysis method.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/namedanalysis.xml'),
    xrefs=["Section-Tasks-Analysis", "Section-Tasks-BdyAnalysis"]
)
        
