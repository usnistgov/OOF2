# -*- python -*-
# $RCSfile: units.py,v $
# $Revision: 1.7 $
# $Author: langer $
# $Date: 2014/09/27 21:40:28 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.common import enum

if config.dimension() == 2:
    pixel = "pixel"
    Pixel = "Pixel"
if config.dimension() == 3:
    pixel = "voxel"
    Pixel = "Voxel"


class Units(enum.EnumClass(
    (Pixel, 'Lengths are relative to the '+pixel+' size'),
    ('Physical', 'Lengths are given in physical units'),
    ('Fractional', 'Lengths are fractions of the dimensions of the microstructure')
    )):
    tip="Specify units for inputs"
    discussion="""<para>

    This type is used to specify whether a length is being given in
    <link linkend="Section-Concepts-Microstructure-Coordinates">physical</link>
    units, or as a multiple of the """+pixel+""" size in the relevant &micro;,
    or as a fraction of the microstructure dimensions.

    </para>"""
