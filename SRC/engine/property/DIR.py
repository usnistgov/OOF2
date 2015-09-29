# -*- python -*-
# $RCSfile: DIR.py,v $
# $Revision: 1.10 $
# $Author: langer $
# $Date: 2014/09/27 21:41:10 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

dirname = 'property'

subdirs = [
    'color',
    'damping',
    'elasticity',
    'forcedensity',
    'heatcapacity',
    'heatconductivity',
    'heatsource',
    'massdensity',
    'orientation',
    'permittivity',
    'piezoelectricity',
    'pyroelectricity',
    'plasticity',
    'skeletonrelaxationrate',
    'thermalexpansion',
    'stressfreestrain',
    'interfaces' 
    ]

if DIM_3:
    subdirs.remove('interfaces')
