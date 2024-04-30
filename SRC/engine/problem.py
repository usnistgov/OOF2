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

# Define instances of Fields, Fluxes, and Equations and the conjugacy
# relations among them.

# The constructors for all of the objects also export them into the
# main OOF2 namespace.

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Define a field.
Temperature = field.ScalarField('Temperature')
# Define a flux
Heat_Flux = flux.VectorFlux('Heat_Flux')
# And equations
HeatBalanceEquation = equation.DivergenceEquation('Heat_Eqn', Heat_Flux, 1)
HeatOutOfPlane = equation.PlaneFluxEquation('Plane_Heat_Flux', Heat_Flux, 1)

## this creates the Displacement, Stress, and Mechanical Equilibrium equations
Displacement = field.TwoVectorField('Displacement')
## When we started using Eigen's matrix solvers, we learned that we
## had been constructing *negative* definite matrices for the force
## balance equation.  The previous CG solver worked with them, but
## Eigen didn't.  Changing the sign of the force balance equation
## fixed the problem, but required changing the sign of the Stress.
## To make this sign change invisible to users, Stress is marked
## "negate" here via the second constructor argument.

Stress = flux.SymmetricTensorFlux('Stress', True)

ForceBalanceEquation = equation.DivergenceEquation(
    'Force_Balance', Stress, config.dimension())

ForcesOutOfPlane = equation.PlaneFluxEquation('Plane_Stress', Stress, 3)


## Define electrostatic potential
Voltage = field.ScalarField('Voltage')
## Define total polarization vector
Total_Polarization = flux.VectorFlux('Total_Polarization')
## Differential form of Coulomb's Law
CoulombEquation = equation.DivergenceEquation(
    'Coulomb_Eqn', Total_Polarization, 1)
PolarizationOutOfPlane = equation.PlaneFluxEquation(
    'InPlanePolarization', Total_Polarization, 1)


# Plasticity -- start with the yield equation.
# TODO: Make hidden equations.

# YieldEquation = equation.NaturalEquation('Yield_Eqn',1)


#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

## Define conjugate quantities for all fields and equations

## Force balance equation
##
## In-plane components (u,v)
##
## The 3D displacement vector is (u, v, w), where u lies along the
## x-direction, v, along the y-direction, and w, out-of-the-plane, or
## along the z-direction

conjugate.conjugatePair("Elasticity",
                        ForceBalanceEquation,
                        ForceBalanceEquation.components(),
                        Displacement,
                        Displacement.components())

## out-of-plane components

## \sigma_{zz} is conjugate to \frac{\partial w}{\partial z}
## \sigma_{xz} is conjugate to \frac{\partial u}{\partial z}
## \sigma_{yz} is conjugate to \frac{\partial v}{\partial z}

# OutOfPlaneSymTensorIndex.components() returns the components in
# Voigt-index order, which does NOT correspond to the order of
# ThreeVectorField.components():
#   Displacement.out_of_plane().components() =
#     [VectorFieldIndex(0),                  u_xz
#      VectorFieldIndex(1),                  u_yz
#      VectorFieldIndex(2)]                  u_zz
#   ForcesOutOfPlane.components() =
#     [OutOfPlaneSymTensorIndex(2, 2),       sigma_zz
#      OutOfPlaneSymTensorIndex(1, 2),       sigma_yz
#      OutOfPlaneSymTensorIndex(0, 2)]       sigma_xz

# So we need to change the order of one of them when calling conjugatePair.
uz = list(Displacement.out_of_plane().components())

conjugate.conjugatePair("Elasticity",
                        ForcesOutOfPlane, ForcesOutOfPlane.components(),
                        Displacement.out_of_plane(),
                        [uz[2], uz[1], uz[0]])
###############################################################
##
## Heat flux equation
##
## In-plane components, T
##
# T = fieldindex.ScalarFieldIndex()
# DivJ = fieldindex.ScalarFieldIndex()
# $\nabla \cdot \vec{J}$ is conjugate to T

conjugate.conjugatePair("ThermalConductivity",
                        HeatBalanceEquation,
                        HeatBalanceEquation.components(),
                        Temperature,
                        Temperature.components())

## out-of-plane components, $\frac{\partial T}{\partial z}$
# T_z = fieldindex.OutOfPlaneVectorFieldIndex(2)
# J_z = fieldindex.OutOfPlaneVectorFieldIndex(2)
# $J_{z}$ is conjugate to $\frac{\partial T}{\partial z}$

conjugate.conjugatePair("ThermalConductivity",
                        HeatOutOfPlane,
                        HeatOutOfPlane.components(),
                        Temperature.out_of_plane(),
                        Temperature.out_of_plane().components())

###############################################################
##
## Coulomb equation
##
## In-plane components, phi
##
# phi = fieldindex.ScalarFieldIndex()
# DivD = fieldindex.ScalarFieldIndex()
 ## $\nabla \cdot \vec{D}$ is conjugate to D

conjugate.conjugatePair("DielectricPermittivity",
                        CoulombEquation,
                        CoulombEquation.components(),
                        Voltage,
                        Voltage.components())

## out-of-plane components, $\frac{\partial D}{\partial z}$
# phi_z = fieldindex.OutOfPlaneVectorFieldIndex(2)
# D_z = fieldindex.OutOfPlaneVectorFieldIndex(2)
##  $D_{z}$ is conjugate to $\frac{\partial phi}{\partial z}$

conjugate.conjugatePair("DielectricPermittivity",
                        PolarizationOutOfPlane,
                        PolarizationOutOfPlane.components(),
                        Voltage.out_of_plane(),
                        Voltage.out_of_plane().components())




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
    for eqn in equation.allEquations():
        print("<listitem><simpara>", file=phile)
        print("<link linkend='Equation-%s'><varname>%s</varname></link>" % (eqn.name(), eqn.name()), file=phile)
        print("</simpara></listitem>", file=phile)
    print("</itemizedlist>", file=phile)
    # Reference page for each Equation
    links = {'PlaneFluxEquation' : 'Section-Concepts-Mesh-Equation-PlaneFlux',
             'DivergenceEquation' : 'Section-Concepts-Mesh-Equation-Divergence'}
    for eqn in equation.allEquations():
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


