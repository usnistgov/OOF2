# -*- python -*-
# $RCSfile: meshbdyanalysis.py,v $
# $Revision: 1.7 $
# $Author: langer $
# $Date: 2011/01/12 19:32:03 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.engine import bdyanalysis
from ooflib.SWIG.engine import planarity
from ooflib.common import debug
from ooflib.common import registeredclass
from ooflib.common.IO import formatchars
from ooflib.common.IO import parameter
from ooflib.engine.IO import meshparameters
import ooflib.SWIG.engine.flux

class MeshBdyAnalyzer(registeredclass.RegisteredClass):
    registry = []

    def analyze(self, meshctxt, time, boundary, destination):
        femesh = meshctxt.getObject()
        edgeset = femesh.getBoundary(boundary).edgeset
        result = self.do_analysis(femesh, edgeset) # defined in subclasses

        if formatchars.showTime():
            print >> destination, time,
        for x in result.valuePtr().value_list():
            print >> destination, x,
        print >> destination

        destination.flush()

    def printHeaders(self, destination, boundary):
        destination.comment(self.shortrepr())
        destination.comment("Boundary:", boundary)
        destination.comment("Columns:")
        cnames = self.columnNames() # defined in subclasses
        if formatchars.showTime():
            cnames = ["time"] + cnames
        for i, colname in enumerate(cnames):
            destination.comment("%d."%(i+1), colname)
        
        

    tip = "Post-solution computations on Mesh boundaries."
    discussion = """<para>
    <classname>MeshBdyAnalyzer</classname> objects are used as the
    <varname>analyzer</varname> argument to the <xref
    linkend="MenuItem-OOF.Mesh.Boundary_Analysis"/> command.  They
    represent different types of calculations that can be done on the
    boundary of a Mesh after it's been solved.
    </para>"""

class IntegrateBdyFlux(MeshBdyAnalyzer):
    def __init__(self, flux):
        self.flux = flux
    def do_analysis(self, femesh, edgeset):
        return bdyanalysis.integrateFlux(femesh, self.flux, edgeset)
    def shortrepr(self):
        return "Integrated " + self.flux.name()
    def columnNames(self):
        if isinstance(self.flux, ooflib.SWIG.engine.flux.VectorFlux):
            return ["normal(%s)" % self.flux.name()]
        it = self.flux.divergence_iterator()
        names = []
        while not it.end():
            names.append("normal(%s)[%s]" 
                         % (self.flux.name(), it.shortstring()))
            it.next()
        return names


registeredclass.Registration(
    "Integrate Flux",
    MeshBdyAnalyzer,
    IntegrateBdyFlux,
    ordering=2,
    params=[meshparameters.FluxParameter('flux', tip=parameter.emptyTipString)],
    tip="Integrate a Flux along a boundary.",
    discussion="""<para>
    Integrate the normal component of the given &flux; along a boundary.
    </para>""")


class AverageField(MeshBdyAnalyzer):
    def __init__(self, field):
        self.field = field
    def do_analysis(self, femesh, edgeset):
        return bdyanalysis.averageField(femesh, self.field, edgeset)
    def shortrepr(self):
        return "Average " + self.field.name()
    def columnNames(self):
        if self.field.ndof() == 1:
            return [self.field.name()]
        names = []
        it = self.field.iterator(planarity.ALL_INDICES)
        while not it.end():
            names.append("%s[%s]" % (self.field.name(), it.shortstring()))
            it.next()
        return names

registeredclass.Registration(
    "Average Field",
    MeshBdyAnalyzer,
    AverageField,
    ordering=1,
    params=[meshparameters.FieldParameter('field',
                                          tip=parameter.emptyTipString)],
    tip="Average a Field over a boundary.",
    discussion="<para>Average the given &field; along a boundary.</para>")
   

# def bdyAnalysis(meshcontext, time, boundary, analyzer, destination):
#     # Do the computation *before* writing the header, because we need
#     # the OutputVal type of the result to tell us what the columns
#     # are.
#     femesh = meshcontext.getObject()
#     edgeset = femesh.getBoundary(boundary).edgeset
#     result = analyzer(femesh, edgeset)
    
#     # Write header info
#     destination.comment(analyzer.shortrepr())
#     destination.comment("Boundary:", boundary)
#     destination.comment("Columns:")
#     cnames = analyzer.columnNames(result)
#     if formatchars.showTime():
#         cnames = ["time"] + cnames
#     for i, colname in enumerate(cnames):
#         destination.comment("%d."%(i+1), colname)
#     # Write data
#     if formatchars.showTime():
#         print >> destination, time,
#     for x in result.valuePtr().value_list():
#         print >> destination, x,
#     print >> destination

#     destination.flush()

