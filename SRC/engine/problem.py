# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.engine import equation
from ooflib.SWIG.engine import field
from ooflib.SWIG.engine import fieldindex
from ooflib.SWIG.engine import flux
from ooflib.common import debug
from ooflib.common import utils
from ooflib.common.IO import xmlmenudump
from ooflib.engine import conjugate
from ooflib.engine import propertyregistration
import sys
import types

#=-=##=-=##=-=##=-=##=-=##=-=##=-=##=-=##=-=##=-=##=-=##=-=##=-=##=-=#

# Call this for all new CompoundFields.

## TODO PYTHON3: Rationalize the names of the functions here.
## newField used to be advertiseField, but it really does more than
## that, so I changed it to newField.  If the "advertise" methods were
## called from the Field, Flux, and Equation constructors it would
## make more sense.

def newField(fld):
    field.newCompoundField(fld)
    _advertise(fld)

    field.newField(_advertise(fld.c_time_derivative()))
    field.newField(_advertise(fld.c_out_of_plane()))
    field.newField(_advertise(fld.c_out_of_plane_time_derivative()))

    # "new field" is sent here, instead of from the Field constructor,
    # because it must be called *after* the field is defined in the
    # OOF namespace.
    switchboard.notify("new field")
    return fld

def _advertise(obj):
    utils.OOFdefine(obj.name(), obj)
    return obj

def advertiseFlux(flx):
    _advertise(flx)
    switchboard.notify("new flux")
    return flx

def advertiseEquation(eqn):
    _advertise(eqn)
    switchboard.notify("new equation")
    return eqn

def advertise(obj):
    # This code is ugly, but at least it's compact.
    ## TODO PYTHON3: Do this from the Field, Flux, etc. constructors?
    if isinstance(obj, field.Field):
        return newField(obj)
    if isinstance(obj, flux.Flux):
        return advertiseFlux(obj)
    if isinstance(obj, equation.Equation):
        return advertiseEquation(obj)
    raise ooferror.PyErrPyProgrammingError(
        "Don't know what to do with %s!"% obj)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Define a field.  This creates an object named 'Temperature' in the
# OOF namespace.
Temperature = advertise(field.ScalarField('Temperature'))
# Define a flux
Heat_Flux = advertise(flux.VectorFlux('Heat_Flux'))
# And equations
HeatBalanceEquation = advertise(equation.DivergenceEquation(
    'Heat_Eqn',
    Heat_Flux,
    1
    ))

HeatOutOfPlane = advertise(equation.PlaneFluxEquation(
    'Plane_Heat_Flux', Heat_Flux, 1))

## this creates the Displacement, Stress, and Mechanical Equilibrium equations
Displacement = advertise(field.TwoVectorField('Displacement'))
## When we started using Eigen's matrix solvers, we learned that we
## had been constructing *negative* definite matrices for the force
## balance equation.  The previous CG solver worked with them, but
## Eigen didn't.  Changing the sign of the force balance equation
## fixed the problem, but required changing the sign of the Stress.
## To make this sign change invisible to users, Stress is marked
## "negate" here via the second constructor argument.

Stress = advertise(flux.SymmetricTensorFlux('Stress', True))

ForceBalanceEquation = advertise(equation.DivergenceEquation(
    'Force_Balance',
    Stress,
    config.dimension()
    ))

ForcesOutOfPlane = advertise(equation.PlaneFluxEquation('Plane_Stress',
                                                        Stress, 3))


## Define electrostatic potential
Voltage = advertise(field.ScalarField('Voltage'))
## Define total polarization vector
Total_Polarization = advertise(flux.VectorFlux('Total_Polarization'))
## Differential form of Coulomb's Law
CoulombEquation = advertise(equation.DivergenceEquation(
    'Coulomb_Eqn', Total_Polarization, 1))
PolarizationOutOfPlane = advertise(equation.PlaneFluxEquation(
    'InPlanePolarization', Total_Polarization, 1))


# Plasticity -- start with the yield equation.
# TODO: Make hidden equations.

# YieldEquation = advertise(equation.NaturalEquation(
#     'Yield_Eqn',1))


#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

## Define conjugate quantities for all fields and equations

## Force balance equation
##
## In-plane components (u,v)
##
## The 3D displacement vector is (u, v, w),
## where
## u lies along the x-direction,
## v, along the y-direction,
## and w, out-of-the-plane, or along
## the z-direction
u = fieldindex.VectorFieldIndex(0)
v = fieldindex.VectorFieldIndex(1)

fx = fieldindex.VectorFieldIndex(0)
fy = fieldindex.VectorFieldIndex(1)

# fx is conjugate to u and fy is conjugate to v for Elasticity
conjugate.conjugatePair("Elasticity", ForceBalanceEquation, [fx, fy],
                    Displacement, [u, v]) 

## out-of-plane compoments

## The available out-of-plane components of stress are $\sigma_{zz},
## \sigma_{zy}, \sigma_{zx}$, in *that* order, (0, 1, 2).  The
## out-of-plane displacement is (\frac{\partial u}{\partial z},
## \frac{\partial v}{partial z}, \frac{\partial w}{\partial z}.

u_xz = fieldindex.VectorFieldIndex(0)
u_yz = fieldindex.VectorFieldIndex(1)
u_zz = fieldindex.VectorFieldIndex(2)
sigma_xz = fieldindex.OutOfPlaneSymTensorIndex(2,0)
sigma_yz = fieldindex.OutOfPlaneSymTensorIndex(2,1)
sigma_zz = fieldindex.OutOfPlaneSymTensorIndex(2,2)

## \sigma_{zz} is conjugate to \frac{\partial w}{\partial z}
## \sigma_{xz} is conjugate to \frac{\partial u}{\partial z}
## \sigma_{yz} is conjugate to \frac{\partial v}{\partial z}

conjugate.conjugatePair("Elasticity",
                        ForcesOutOfPlane, [sigma_zz, sigma_xz, sigma_yz],
                        Displacement.out_of_plane(), [u_zz, u_xz, u_yz])


###############################################################
##
## Heat flux equation
##
## In-plane components, T
##
T = fieldindex.ScalarFieldIndex()
DivJ = fieldindex.ScalarFieldIndex()

conjugate.conjugatePair("ThermalConductivity", HeatBalanceEquation, DivJ,
                        Temperature, T)
## $\nabla \cdot \vec{J}$ is conjugate to T

## out-of-plane components, $\frac{\partial T}{\partial z}$
T_z = fieldindex.OutOfPlaneVectorFieldIndex(2)
J_z = fieldindex.OutOfPlaneVectorFieldIndex(2)

conjugate.conjugatePair("ThermalConductivity", HeatOutOfPlane, J_z,
                        Temperature.out_of_plane(), T_z)
##  $J_{z}$ is conjugate to $\frac{\partial T}{\partial z}$

###############################################################
##
## Coulomb equation
##
## In-plane components, phi
##
phi = fieldindex.ScalarFieldIndex()
DivD = fieldindex.ScalarFieldIndex()

conjugate.conjugatePair("DielectricPermittivity",
                        CoulombEquation, DivD,
                        Voltage, phi)
 ## $\nabla \cdot \vec{D}$ is conjugate to D

## out-of-plane components, $\frac{\partial D}{\partial z}$
phi_z = fieldindex.OutOfPlaneVectorFieldIndex(2)
D_z = fieldindex.OutOfPlaneVectorFieldIndex(2)

conjugate.conjugatePair("DielectricPermittivity",
                        PolarizationOutOfPlane, D_z,
                        Voltage.out_of_plane(), phi_z)
##  $D_{z}$ is conjugate to $\frac{\partial phi}{\partial z}$



#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#
#--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#=
#-=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#=-

# xmldump generates the manual page for the built-in physics.

def xmldump(phile):
    print("<section id='Section-Builtin'>", file=phile)
    print(" <title>Built-In Physics: Fields, Fluxes, Equations, and Properties</title>", file=phile)
    print("""<para>
    &oof2; is designed to be extendible, so it is easy to add new
    &properties;, &fields;, &fluxes;, and &equations;.  That means
    that the following lists of <emphasis>built-in</emphasis>
    objects may not be complete.  </para>""", file=phile)

    # Property documentation.  propdict is a dictionary listing the
    # Properties that contribute to each Equation and Flux, or use
    # each Field.
    propdict = propertyregistration.xmldocs(phile)

    # Fields
    print("<section id='Section-Fields'>", file=phile)
    print("<title>Fields</title>", file=phile)
    print("""<para>

This list contains all of the predefined &fields; in &oof2;.  Click on
a &field; to see a brief description and a list of all &properties;
that use the &field;.

</para>""", file=phile)
    print("<itemizedlist>", file=phile)
    # List of Fields.
    for fld in field.allCompoundFields.values():
        print("<listitem><simpara>", file=phile)
        print("<link linkend='Field-%s'><varname>%s</varname></link>"\
            % (fld.name(), fld.name()), file=phile)
        print("</simpara></listitem>", file=phile)
    print("</itemizedlist>", file=phile)
    # Reference page for each Field.
    for fld in list(field.allCompoundFields.values()):
        name = fld.name()
        xmlmenudump.xmlIndexEntry(name, 'Field', 'Field-%s' % name)
        print("<refentry xreflabel='%s' id='Field-%s'>" % (name, name), file=phile)
        print(" <refnamediv>", file=phile)
        print("  <refname>%s</refname>" % name, file=phile)
        print("  <refpurpose></refpurpose>", file=phile)
        print(" </refnamediv>", file=phile)
        print(" <refsect1>", file=phile)
        print("  <title>Details</title>", file=phile)
        print("  <itemizedlist>", file=phile)
        print("   <listitem><simpara>", file=phile)
        print("     Class: <classname>%s</classname>" % fld.__class__.__name__, file=phile)
        print("   </simpara></listitem>", file=phile)
        print("   <listitem><simpara>", file=phile)
        print("     Dimension: ", fld.ndof(), file=phile)
        print("   </simpara></listitem>", file=phile)

        try:
            properties = propdict[fld]
        except KeyError:
            pass
        else:
            print("<listitem><para>", file=phile)
            print("<varname>%s</varname> is used by the following &properties;:" % name, file=phile)
            print("<itemizedlist>", file=phile)
            for prop in properties:
                print("<listitem><simpara>", file=phile)
                print("<xref linkend='Property-%s'/>" % (
                    prop.name().replace(':', '-')), file=phile)
                print("</simpara></listitem>", file=phile)
            print("</itemizedlist>", file=phile)
            print("</para></listitem>", file=phile)
            
        print("  </itemizedlist>", file=phile)
        print("</refsect1> <!-- Details -->", file=phile)

        print("<refsect1>", file=phile)
        print("<title>Description</title>", file=phile)
        try:
            src = open("DISCUSSIONS/engine/builtin/field-%s.xml" % name, "r")
        except IOError:
            print("<para>MISSING DISCUSSION for %s</para>" % name, file=phile)
        else:
            print(src.read(), file=phile)
            src.close()
        print("</refsect1>", file=phile)
        print("</refentry> <!-- %s -->" % fld.name(), file=phile)
    print("</section> <!-- Fields -->", file=phile)

    # Fluxes
    print("<section id='Section-Fluxes'>", file=phile)
    print("<title>Fluxes</title>", file=phile)
    print("""<para>
This list contains all of the predefined &fluxes; in &oof2;.  Click on
a &flux; to see a brief description and a list of all &properties;
that contribute to the &flux;.
</para>""", file=phile)
    # List of Fluxes
    print("<itemizedlist>", file=phile)
    for flx in flux.allFluxes:
        print("<listitem><simpara>", file=phile)
        print("<link linkend='Flux-%s'><varname>%s</varname></link>"\
            % (flx.name(), flx.name()), file=phile)
        print("</simpara></listitem>", file=phile)
    print("</itemizedlist>", file=phile)
    # Reference page for each Flux
    for flx in flux.allFluxes:
        name = flx.name()
        xmlmenudump.xmlIndexEntry(name, 'Flux', 'Flux-%s' % name)
        print("<refentry xreflabel='%s' id='Flux-%s'>" % (name, name), file=phile)
        print("<refnamediv>", file=phile)
        print("<refname>%s</refname>" % name, file=phile)
        print("<refpurpose></refpurpose>", file=phile)
        print("</refnamediv>", file=phile)
        print("<refsect1>", file=phile)
        print("<title>Details</title>", file=phile)
        print("<itemizedlist>", file=phile)
        print("<listitem><simpara>", file=phile)
        print("Class: <classname>%s</classname>" % (
            flx.__class__.__name__), file=phile) 
        print("</simpara></listitem>", file=phile)
        print("<listitem><simpara>", file=phile)
        print("Dimension: ", flx.ndof(), file=phile)
        print("</simpara></listitem>", file=phile)
        try:
            properties = propdict[flx]
        except KeyError:
            pass
        else:
            print("<listitem><simpara>", file=phile)
            print("The following &properties; contribute to <varname>%s</varname>:" % name, file=phile)
            print("<itemizedlist>", file=phile)
            for prop in properties:
                print("<listitem><simpara>", file=phile)
                print("<xref linkend='Property-%s'/>" % (
                    prop.name().replace(':', '-')), file=phile)
                print("</simpara></listitem>", file=phile)
            print("</itemizedlist>", file=phile)
            print("</simpara></listitem>", file=phile)

        print("</itemizedlist>", file=phile)
        print("</refsect1> <!-- Details -->", file=phile)
        print("<refsect1>", file=phile)
        print("<title>Description</title>", file=phile)
        try:
            src = open('DISCUSSIONS/engine/builtin/flux-%s.xml' % name, "r")
        except IOError:
            print("<para>MISSING DISSCUSSION FOR %s</para>" % name, file=phile)
        else:
            print(src.read(), file=phile)
            src.close()
        print("</refsect1> <!--Description-->", file=phile)
        print("</refentry>", file=phile)
    print("</section> <!-- Fluxes -->", file=phile)

    print("<section id='Section-Equations'>", file=phile)
    print("<title>Equations</title>", file=phile)
    print("""<para>
This is a list of all of the predefined &equations; in &oof2;.  Click
on an &equation; to see a description and a list of all &properties;
that contribute to the &equation;.
</para>""", file=phile)
    # List of Equations
    print("<itemizedlist>", file=phile)
    for eqn in equation.allEquations:
        print("<listitem><simpara>", file=phile)
        print("<link linkend='Equation-%s'><varname>%s</varname></link>" % (eqn.name(), eqn.name()), file=phile)
        print("</simpara></listitem>", file=phile)
    print("</itemizedlist>", file=phile)
    # Reference page for each Equation
    links = {'PlaneFluxEquation' : 'Section-Concepts-Mesh-Equation-PlaneFlux',
             'DivergenceEquation' : 'Section-Concepts-Mesh-Equation-Divergence'}
    for eqn in equation.allEquations:
        name = eqn.name()
        xmlmenudump.xmlIndexEntry(name, 'Equation', 'Equation-%s' % name)
        classname = eqn.__class__.__name__
        print("<refentry xreflabel='%s' id='Equation-%s'>" % (
            name, name), file=phile)
        print("<refnamediv>", file=phile)
        print("<refname>%s</refname>" % name, file=phile)
        print("<refpurpose></refpurpose>", file=phile)
        print("</refnamediv>", file=phile)
        print("<refsect1>", file=phile)
        print("<title>Details</title>", file=phile)
        print("<itemizedlist>", file=phile)
        print("<listitem><simpara>", file=phile)
        print("Type: <link linkend='%s'><classname>%s</classname></link>" % (links[classname], classname), file=phile)
        print("</simpara></listitem>", file=phile)
        print("<listitem><simpara>", file=phile)
        print("Flux: <link linkend='Flux-%s'><varname>%s</varname></link>" % (eqn.fluxname(), eqn.fluxname()), file=phile)
        print("</simpara></listitem>", file=phile)
        print("<listitem><simpara>", file=phile)
        print("Dimension:", eqn.ndof(), file=phile)
        print("</simpara></listitem>", file=phile)
        try:
            properties = propdict[eqn]
        except KeyError:
            pass
        else:
            print("<listitem><simpara>", file=phile)
            print("The following &properties; make direct contributions to this &equation;:", file=phile)
            print("<itemizedlist>", file=phile)
            for prop in properties:
                print("<listitem><simpara>", file=phile)
                print("<xref linkend='Property-%s'/>" % (
                    prop.name().replace(':','-')), file=phile)
                print("</simpara></listitem>", file=phile)
            print("</itemizedlist>", file=phile)
            print("Other &properties; make indirect contributions to the &equation; through the <link linkend='Flux-%s'><classname>%s</classname></link>." % (eqn.fluxname(), eqn.fluxname()), file=phile)
            print("</simpara></listitem>", file=phile)
        print("</itemizedlist>", file=phile)
        print("</refsect1> <!-- Details -->", file=phile)
        print("<refsect1>", file=phile)
        print("<title>Description</title>", file=phile)
        try:
            src = open("DISCUSSIONS/engine/builtin/eqn-%s.xml" % name, "r")
        except IOError:
            print("<para>MISSING DISCUSSION FOR %s</para>" % name, file=phile)
        else:
            print(src.read(), file=phile)
            src.close()
        print("</refsect1> <!-- Description-->", file=phile)
        
        print("</refentry>", file=phile)
        
    print("</section> <!-- Equations -->", file=phile)

    print("</section> <!-- Built-In Physics -->", file=phile)
    

xmlmenudump.addSection(xmldump, 5)


