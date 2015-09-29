# -*- python -*-
# $RCSfile: exact_solns.py,v $
# $Revision: 1.6 $
# $Author: langer $
# $Date: 2010/11/08 15:59:50 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.


# Each scalar solution function definition is given by a Python
# lambda formula specifying "Solution" and two sets of boundary
# conditions: "DirichletBC" and "NeumannBC". The boundary conditions
# are a list of tuples of strings in the form:
# ( boundary, field_comp, eqn_comp, function, timeDeriv, timeDeriv2 )
#
# In the case of vector solutions, "Solution" is a triple of lambda
# functions and the boundary conditions are given by a list of tuples
# in the same form as those for scalar solution functions.

## TODO: The data for each solution here is found in many different
## places, which is a maintenance pain.  The solutions in this file
## correspond to Properties in various file (eg,
## nonlinear_heat_conductivity.C, nonconstant_heat_source.C,
## nonlinear_K_timedep_tests.py) and the numbers in those files don't
## correspond to the numbers in this file.  Each nonlinear test
## problem should be somehow completely defined in a single place.
## This may be difficult, since some of the expressions are in C++ and
## some in python.

import sys
from math import *


scalar_solns = [

    # Scalar solution no: 0

    { "Solution": "sin(2.0*pi*x) * sin(3.0*pi*y)",

      "InitialValue": 'sin(2.0*pi*x) * sin(3.0*pi*y)',

      "InitialTimeDeriv": '0.0',

      "DirichletBC": [ ('top',   '','','0.0','0.0','0.0'),
                       ('bottom','','','0.0','0.0','0.0'),
                       ('right', '','','0.0','0.0','0.0'),
                       ('left',  '','','0.0','0.0','0.0')  ] },

    # Scalar solution no: 1

    { "Solution": "x*x + y*y",

      "InitialValue": 'x*x + y*y',

      "InitialTimeDeriv": '0.0',

      "DirichletBC": [ ('top',   '','','x*x+1.','0.0','0.0'),
                       ('bottom','','','x*x',   '0.0','0.0'),
                       ('right', '','','y*y+1.','0.0','0.0'),
                       ('left',  '','','y*y',   '0.0','0.0')  ] },

    # Scalar solution no: 2

    { "Solution": "-2.*log(x+y+3.)",

      "InitialValue": ' -2.*log(x+y+3.)',

      "InitialTimeDeriv": '0.0',

      "DirichletBC": [ ('top',   '','','-2.*log(x+4.)','0.0','0.0'),
                       ('bottom','','','-2.*log(x+3.)','0.0','0.0'),
                       ('right', '','','-2.*log(y+4.)','0.0','0.0'),
                       ('left',  '','','-2.*log(y+3.)','0.0','0.0')  ] },

    # Scalar solution no: 3

    { "Solution": "exp(-1.5*t) * sin(2.0*pi*x) * sin(3.0*pi*y)",

      "InitialValue": 'sin(2.0*pi*x) * sin(3.0*pi*y)',

      "InitialTimeDeriv": '-1.5 * sin(2.0*pi*x) * sin(3.0*pi*y)',

      "DirichletBC": [ ('top',   '','','0.0','0.0','0.0'),
                       ('bottom','','','0.0','0.0','0.0'),
                       ('right', '','','0.0','0.0','0.0'),
                       ('left',  '','','0.0','0.0','0.0')  ] },

    # Scalar solution no: 4

    { "Solution": "(2.0*x + 3.0) / (x*x + 3.0*x + 6.0*t + 5.0)",

      "InitialValue": '(2.0*x + 3.0) / (x*x + 3.0*x + 5.0)',

      "InitialTimeDeriv": '-6.0 * (2.0*x + 3.0) / (x*x + 3.0*x + 5.0)**2',

      "DirichletBC": [ ('top',   '','',     '(2.*x+3.)/(x*x+3.*x+6.*t+5.)',
                                        '-6.*(2.*x+3.)/(x*x+3.*x+6.*t+5.)**2',
                                        '72.*(2.*x+3.)/(x*x+3.*x+6.*t+5.)**3'),
                       ('bottom','','',     '(2.*x+3.)/(x*x+3.*x+6.*t+5.)',
                                        '-6.*(2.*x+3.)/(x*x+3.*x+6.*t+5.)**2',
                                        '72.*(2.*x+3.)/(x*x+3.*x+6.*t+5.)**3'),
                       ('right', '','',  '5./(6.*t+9.)',
                                       '-30./(6.*t+9.)**2',
                                       '360./(6.*t+9.)**3'),
                       ('left', '','',   '3./(6.*t+5.)',
                                       '-18./(6.*t+5.)**2',
                                       '216./(6.*t+5.)**3')  ] },

    # Scalar solution no: 5

    { "Solution": "-log(2.0 + exp(x+y-2.0*t))",

      "InitialValue": '-log(2.0 + exp(x+y))',

      "InitialTimeDeriv": '2.0 * exp(x+y) / (2.0 + exp(x+y))',

      "DirichletBC": [ ('top',   '','',   '-log(2.0 + exp(x+1.-2.0*t))',
                                        '2.*exp(x+1.-2.*t)/(2.+exp(x+1.-2.*t))',
                                       '-8.*exp(x+1.-2.*t)/(2.+exp(x+1.-2.*t))**2'),
                       ('bottom','','',   '-log(2.0 + exp(x-2.0*t))',
                                        '2.*exp(x-2.*t)/(2.+exp(x-2.*t))',
                                       '-8.*exp(x-2.*t)/(2.+exp(x-2.*t))**2'),
                       ('right', '','',   '-log(2.0 + exp(1.+y-2.0*t))',
                                        '2.*exp(1.+y-2.*t)/(2.+exp(1.+y-2.*t))',
                                       '-8.*exp(1.+y-2.*t)/(2.+exp(1.+y-2.*t))**2'),
                       ('left',  '','',   '-log(2.0 + exp(y-2.0*t))',
                                        '2.*exp(y-2.*t)/(2.+exp(y-2.*t))',
                                       '-8.*exp(y-2.*t)/(2.+exp(y-2.*t))**2')  ] },

    # Scalar solution no: 6

    { "Solution": "-(x+y)",

      "InitialValue": '-(x+y)',

      "InitialTimeDeriv": '0.0',

      "DirichletBC": [ ('top',   '','','-(x+1.)','0.0','0.0'),
                       ('bottom','','','-x',     '0.0','0.0'),
                       ('right', '','','-(y+1.)','0.0','0.0'),
                       ('left',  '','','-y',     '0.0','0.0')  ] },

    # Scalar solution no: 7

    { "Solution": "-tan( (1.0/20.0) * (2.0*pi*cos(2.0*pi*x)*sin(3.0*pi*y) + 3.0*pi*sin(2.0*pi*x)*cos(3.0*pi*y)) )",

      "InitialValue": '-tan( (1.0/20.0) * (2.0*pi*cos(2.0*pi*x)*sin(3.0*pi*y) + 3.0*pi*sin(2.0*pi*x)*cos(3.0*pi*y)) )',

      "InitialTimeDeriv": '0.0',

      "DirichletBC": [ ('top',   '','', 'tan((3.*pi/20.)*sin(2.*pi*x))','0.0','0.0'),
                       ('bottom','','','-tan((3.*pi/20.)*sin(2.*pi*x))','0.0','0.0'),
                       ('right', '','','-tan((pi/10.)*sin(2.*pi*y))',   '0.0','0.0'),
                       ('left',  '','','-tan((pi/10.)*sin(2.*pi*y))',   '0.0','0.0')  ] },

    # Scalar solution no: 8

    { "Solution": "sin(2.0*pi*x) * sin(3.0*pi*y) * sin(pi*(x-1.5*t))",

      "InitialValue": 'sin(2.0*pi*x) * sin(3.0*pi*y) * sin(pi*x)',

      "InitialTimeDeriv": '-pi*1.5 * sin(2.0*pi*x) * sin(3.0*pi*y) * cos(pi*x)',

      "DirichletBC": [ ('top',   '','','0.0','0.0','0.0'),
                       ('bottom','','','0.0','0.0','0.0'),
                       ('right', '','','0.0','0.0','0.0'),
                       ('left',  '','','0.0','0.0','0.0')  ] },

    # Scalar solution no 9

    { "Solution": "(x*x-x)*(y*y-y)*exp(3*x*t)",
      "InitialValue": "not needed",
      "InitialTimeDeriv": "not needed",
      "DirichletBC": [('top',   '','','0.0','0.0','0.0'),
                      ('bottom','','','0.0','0.0','0.0'),
                      ('right', '','','0.0','0.0','0.0'),
                      ('left',  '','','0.0','0.0','0.0')] }
    

    ] # end of scalar_solns list


#################################################################################


vector2D_solns = [

    # Vector2D solution no: 0

    { "Solution": "( sin(2.0*pi*x) * sin(3.0*pi*y), sin(1.0*pi*x) * sin(2.0*pi*y) )",

      "InitialValue": ( 'sin(2.0*pi*x) * sin(3.0*pi*y)',
                        'sin(1.0*pi*x) * sin(2.0*pi*y)' ),

      "InitialTimeDeriv": ( '0.0', '0.0' ),

      "DirichletBC": [ ('top',   'x','x','0.0','0.0','0.0'),
                       ('bottom','x','x','0.0','0.0','0.0'),
                       ('right', 'x','x','0.0','0.0','0.0'),
                       ('left',  'x','x','0.0','0.0','0.0'),
                       ('top',   'y','y','0.0','0.0','0.0'),
                       ('bottom','y','y','0.0','0.0','0.0'),
                       ('right', 'y','y','0.0','0.0','0.0'),
                       ('left',  'y','y','0.0','0.0','0.0')  ] },

    # Vector2D solution no: 1

    { "Solution": "( ( 2.0*t + 3.0) * sin(2.0*pi*x) * sin(3.0*pi*y), (-4.0*t + 5.0) * sin(1.0*pi*x) * sin(2.0*pi*y) )",

      "InitialValue": ( '3.0 * sin(2.0*pi*x) * sin(3.0*pi*y)',
                        '5.0 * sin(1.0*pi*x) * sin(2.0*pi*y)' ),

      "InitialTimeDeriv": (  '2.0 * sin(2.0*pi*x) * sin(3.0*pi*y)',
                            '-4.0 * sin(1.0*pi*x) * sin(2.0*pi*y)' ),

      "DirichletBC": [ ('top',   'x','x','0.0','0.0','0.0'),
                       ('bottom','x','x','0.0','0.0','0.0'),
                       ('right', 'x','x','0.0','0.0','0.0'),
                       ('left',  'x','x','0.0','0.0','0.0'),
                       ('top',   'y','y','0.0','0.0','0.0'),
                       ('bottom','y','y','0.0','0.0','0.0'),
                       ('right', 'y','y','0.0','0.0','0.0'),
                       ('left',  'y','y','0.0','0.0','0.0')  ] },

    # Vector2D solution no: 2

    { "Solution": "( -2.0 * log(x+y+3.0), 0.5*log(5.0) - log(4.0*x-3.0*y+10.0) )",

      "InitialValue": ( '-2.0 * log(x+y+3.0)',
                         '0.5*log(5.0) - log(4.0*x-3.0*y+10.0)' ),

      "InitialTimeDeriv": ( '0.0', '0.0' ),

      "DirichletBC": [ ('top',   'x','x', '-2.0 * log(x+4.0)', '0.0','0.0'),
                       ('bottom','x','x', '-2.0 * log(x+3.0)', '0.0','0.0'),
                       ('right', 'x','x', '-2.0 * log(y+4.0)', '0.0','0.0'),
                       ('left',  'x','x', '-2.0 * log(y+3.0)', '0.0','0.0'),
                       ('top',   'y','y', '0.5*log(5.0) - log( 4.0*x+ 7.0)', '0.0', '0.0'),
                       ('bottom','y','y', '0.5*log(5.0) - log( 4.0*x+10.0)', '0.0', '0.0'),
                       ('right', 'y','y', '0.5*log(5.0) - log(-3.0*y+14.0)', '0.0', '0.0'),
                       ('left',  'y','y', '0.5*log(5.0) - log(-3.0*y+10.0)', '0.0', '0.0')  ] },

    # Vector2D solution no: 3

    { "Solution": "( sin(2.0*pi*x) * sin(3.0*pi*y), x*x + y*y )",

      "InitialValue": ( 'sin(2.0*pi*x) * sin(3.0*pi*y)',
                        'x*x + y*y' ),

      "InitialTimeDeriv": ( '0.0', '0.0' ),

      "DirichletBC": [ ('top',   'x','x','0.0',      '0.0','0.0'),
                       ('bottom','x','x','0.0',      '0.0','0.0'),
                       ('right', 'x','x','0.0',      '0.0','0.0'),
                       ('left',  'x','x','0.0',      '0.0','0.0'),
                       ('top',   'y','y','x*x + 1.0','0.0','0.0'),
                       ('bottom','y','y','x*x',      '0.0','0.0'),
                       ('right', 'y','y','y*y + 1.0','0.0','0.0'),
                       ('left',  'y','y','y*y',      '0.0','0.0')  ] },

    # Vector2D solution no: 4

    { "Solution": "( 4.0 * log(1.0 + 0.5*sin(2.0*x+t+3.0)), 1.0 / (1.0 + y*y - (t+4.0)**2) )",

      "InitialValue": ( '4.0 * log(1.0 + 0.5*sin(2.0*x+3.0))',
                        '1.0 / (y*y - 15.0)' ),

      "InitialTimeDeriv": ( '2.0*cos(2.0*x + 3.0) / (1.0 + 0.5*sin(2.0*x + 3.0))',
                            '8.0 / (y**2 - 15.0)**2' ),

      "DirichletBC": [ ('top',   'x','x',  '4.0 * log(1.0+.5*sin(2.0*x+t+3.0))',
                                           '2.*cos(t+2.*x+3.) / (1.+.5*sin(t+2.*x+3.))',
                                         '-(8.*sin(t+2.*x+3.)+4.) / (sin(t+2.*x+3.) + 2.)**2'),
                       ('bottom','x','x',  '4.0 * log(1.0+.5*sin(2.0*x+t+3.0))',
                                           '2.*cos(t+2.*x+3.) / (1.+.5*sin(t+2.*x+3.))',
                                         '-(8.*sin(t+2.*x+3.)+4.) / (sin(t+2.*x+3.) + 2.)**2'),
                       ('right', 'x','x',  '4.0 * log(1.0+.5*sin(t+5.0))',
                                           '2.*cos(t+5.) / (1.+.5*sin(t+5.))',
                                         '-(8.*sin(t+5.)+4.) / (sin(t+5.)+2.)**2'),
                       ('left',  'x','x',  '4.0 * log(1.0+.5*sin(t+3.0))',
                                           '2.*cos(t+3.) / (1.+.5*sin(t+3.))',
                                         '-(8.*sin(t+3.)+4.) / (sin(t+3.)+2.)**2'),
                       ('top',   'y','y',  '1.0 / (2.0 - (t+4.0)**2)',
                                          '(2.*t+8.) / (2.-(t+4.)**2)**2',
                                         '-(6.*t**2+48.*t+100.)/(t**2+8.*t+14.)**3'),
                       ('bottom','y','y',  '1.0 / (1.0 - (t+4.0)**2)',
                                          '(2.*t+8.) / (1.-(t+4.)**2)**2',
                                         '-(6.*t**2+48.*t+98.)/(t**2+8.*t+15.)**3'),
                       ('right', 'y','y',  '1.0 / (1.0 + y*y -(t+4.0)**2)',
                                          '(2.*t+8.) / (y**2-(t+4.)**2+1.)**2',
                                         '-(6.*t**2+48.*t+2.*y**2+98.)/(t**2+8.*t-y**2+15.)**3'),
                       ('left',  'y','y',  '1.0 / (1.0 + y*y -(t+4.0)**2)',
                                          '(2.*t+8.) / (y**2-(t+4.)**2+1.)**2',
                                         '-(6.*t**2+48.*t+2.*y**2+98.)/(t**2+8.*t-y**2+15.)**3')  ] },

    # Vector2D solution no: 5

    { "Solution": "( 0.05 * sin(2.0*pi*x) * sin(3.0*pi*y), 0.05 * (x*x + y*y) )",

      "InitialValue": ( '0.05 * sin(2.0*pi*x) * sin(3.0*pi*y)',
                        '0.05 * (x*x + y*y)' ),

      "InitialTimeDeriv": ( '0.0', '0.0' ),

      "DirichletBC": [ ('top',   'x','x','0.0','0.0','0.0'),
                       ('bottom','x','x','0.0','0.0','0.0'),
                       ('right', 'x','x','0.0','0.0','0.0'),
                       ('left',  'x','x','0.0','0.0','0.0'),
                       ('top',   'y','y','0.05*x*x + 0.05','0.0','0.0'),
                       ('bottom','y','y','0.05*x*x',       '0.0','0.0'),
                       ('right', 'y','y','0.05*y*y + 0.05','0.0','0.0'),
                       ('left',  'y','y','0.05*y*y',       '0.0','0.0')  ] },

    # Vector2D solution no: 6

    { "Solution": "( sin(2.0*pi*x) * sin(3.0*pi*y), sin(3.0*pi*x) * sin(2.0*pi*y) )",

      "InitialValue": ( 'sin(2.0*pi*x) * sin(3.0*pi*y)',
                        'sin(3.0*pi*x) * sin(2.0*pi*y)' ),

      "InitialTimeDeriv": ( '0.0', '0.0' ),

      "DirichletBC": [ ('top',   'x','x','0.0','0.0','0.0'),
                       ('bottom','x','x','0.0','0.0','0.0'),
                       ('right', 'x','x','0.0','0.0','0.0'),
                       ('left',  'x','x','0.0','0.0','0.0'),
                       ('top',   'y','y','0.0','0.0','0.0'),
                       ('bottom','y','y','0.0','0.0','0.0'),
                       ('right', 'y','y','0.0','0.0','0.0'),
                       ('left',  'y','y','0.0','0.0','0.0')  ] },

    # Vector2D solution no: 7

    { "Solution": "( 3.0*x*x + y*y, 2.0*x*x + 4.0*y*y )",

      "InitialValue": ( '3.0*x*x + y*y',
                        '2.0*x*x + 4.0*y*y' ),

      "InitialTimeDeriv": ( '0.0', '0.0' ),

      "DirichletBC": [ ('top',   'x','x','3.0*x*x + 1.0','0.0','0.0'),
                       ('bottom','x','x','3.0*x*x',      '0.0','0.0'),
                       ('right', 'x','x','3.0 + y*y',    '0.0','0.0'),
                       ('left',  'x','x',      'y*y',    '0.0','0.0'),
                       ('top',   'y','y','2.0*x*x + 4.0','0.0','0.0'),
                       ('bottom','y','y','2.0*x*x',      '0.0','0.0'),
                       ('right', 'y','y','2.0 + 4.0*y*y','0.0','0.0'),
                       ('left',  'y','y',      '4.0*y*y','0.0','0.0')  ] },

    ] # end of vector2D_solns list


#################################################################################


vector3D_solns = [

    # Vector3D solution no: 0

    { "Solution": "( -3.0*x, -4.0*y, -1.5*x - 2.0*y )",

      "InitialValue": ( '-3.0*x', '-4.0*y', '-1.5*x-2.0*y' ),

      "InitialTimeDeriv": ( '0.0', '0.0' ),

      "DirichletBC": [ ('top',   'x','x','-3.0*x',    '0.0','0.0'),
                       ('bottom','x','x','-3.0*x',    '0.0','0.0'),
                       ('right', 'x','x','-3.0',      '0.0','0.0'),
                       ('left',  'x','x', '0.0',      '0.0','0.0'),
                       ('top',   'y','y','-4.0',      '0.0','0.0'),
                       ('bottom','y','y', '0.0',      '0.0','0.0'),
                       ('right', 'y','y','-4.0*y',    '0.0','0.0'),
                       ('left',  'y','y','-4.0*y',    '0.0','0.0'),
                       ('top',   'z','z','-1.5*x-2.0','0.0','0.0'),
                       ('bottom','z','z','-1.5*x',    '0.0','0.0'),
                       ('right', 'z','z','-1.5-2.0*y','0.0','0.0'),
                       ('left',  'z','z',    '-2.0*y','0.0','0.0')  ] },

    # Vector3D solution no: 1

    { "Solution":
          "-tan( (2.0*pi/20.0) * cos(2.0*pi*x) * sin(3.0*pi*y)  ),"
      "-tan( (2.0*pi/20.0) * sin(3.0*pi*x) * cos(2.0*pi*y)  ),"
      "-tan( (2.0*pi/20.0) *(sin(3.0*pi*x) * cos(2.0*pi*y) +"
      "cos(2.0*pi*x) * sin(3.0*pi*y)) )",

      "InitialValue": ( '-tan( (2.0*pi/20.0) * cos(2.0*pi*x) * sin(3.0*pi*y)',
                        '-tan( (2.0*pi/20.0) * sin(3.0*pi*x) * cos(2.0*pi*y)',
                        '-tan( (2.0*pi/20.0) *(sin(3.0*pi*x) * cos(2.0*pi*y) + cos(2.0*pi*x) * sin(3.0*pi*y)) )' ),

      "InitialTimeDeriv": ( '0.0', '0.0' ),

      "DirichletBC": [ ('top',   'x','x',                      '0.0','0.0','0.0'),
                       ('bottom','x','x',                      '0.0','0.0','0.0'),
                       ('right', 'x','x','-tan(1/10*pi*sin(3*pi*y))','0.0','0.0'),
                       ('left',  'x','x','-tan(1/10*pi*sin(3*pi*y))','0.0','0.0'),
                       ('top',   'y','y','-tan(1/10*pi*sin(3*pi*x))','0.0','0.0'),
                       ('bottom','y','y','-tan(1/10*pi*sin(3*pi*x))','0.0','0.0'),
                       ('right', 'y','y',                      '0.0','0.0','0.0'),
                       ('left',  'y','y',                      '0.0','0.0','0.0'),
                       ('top',   'z','z','-tan(1/10*pi*sin(3*pi*x))','0.0','0.0'),
                       ('bottom','z','z','-tan(1/10*pi*sin(3*pi*x))','0.0','0.0'),
                       ('right', 'z','z','-tan(1/10*pi*sin(3*pi*y))','0.0','0.0'),
                       ('left',  'z','z','-tan(1/10*pi*sin(3*pi*y))','0.0','0.0')  ] }

    ] # end of vector3D_solns list


exact_solns = { "scalar"   : scalar_solns,
                "vector2D" : vector2D_solns,
                "vector3D" : vector3D_solns }


#################################################################################


# The following functions are used to compute the L^2 error of a computed
# field (scalar, vector2D, vector3D) on a given mesh with respect to
# a specified exact solution function. The mesh is assumed to consist of
# rectangular elements of size hx*hy*hz (hx=1/numX,hy=1/numY,hz=1/numZ)
# and the L^2 error is approximated by trhe square root of
#
#   hx*hy*hz \sum_{all nodes} ((value at node) - exact_func_value(x,y,z,time))^2
#


def computeScalarErrorL2(soln_func,mesh,field,numX=1,numY=1,numZ=1,time=0.0):

    fn = eval('lambda x,y,z,t: ' + soln_func)

    hx = 1. / numX
    hy = 1. / numY
    hz = 1. / numZ

    total_error = 0.
    for node in mesh.funcnode_iterator():
        value = field.value( mesh, node, 0 )
        x = node.position().x
        y = node.position().y
        z = 0.0
        exact_value = fn( x, y, z, time )
        total_error += ( value - exact_value )**2

    total_error = sqrt( hx*hy*hz * total_error )

    return total_error


def computeVector2DErrorL2(soln_func,mesh,field,numX=1,numY=1,numZ=1,time=0.0):
    
    fn = eval('lambda x,y,z,t: (%s)' % soln_func)

    hx = 1. / numX
    hy = 1. / numY
    hz = 1. / numZ

    total_error = 0.
    for node in mesh.funcnode_iterator():
        value = ( field.value( mesh, node, 0 ),
                  field.value( mesh, node, 1 ) )
        x = node.position().x
        y = node.position().y
        z = 0.0
        exact_value = fn( x, y, z, time )
        total_error +=  ( ( value[0] - exact_value[0] )**2
                          + ( value[1] - exact_value[1] )**2 )
    total_error = sqrt( hx*hy*hz * total_error )

    return total_error


def computeVector3DErrorL2(soln_func,mesh,field,numX=1,numY=1,numZ=1,time=0.0):
    fn = eval('lambda x,y,z,t: (%s)' % soln_func)

    hx = 1. / numX
    hy = 1. / numY
    hz = 1. / numZ

    total_error = 0.
    for node in mesh.funcnode_iterator():
        value = ( field.value( mesh, node, 0 ),
                  field.value( mesh, node, 1 ),
                  field.value( mesh, node, 2 ) )
        x = node.position().x
        y = node.position().y
        z = 0.0
        exact_value = fn( x, y, z, time )
        total_error += ( ( value[0] - exact_value[0] )**2
                         + ( value[1] - exact_value[1] )**2
                         + ( value[2] - exact_value[2] )**2 )
    total_error = sqrt( hx*hy*hz * total_error )

    return total_error
