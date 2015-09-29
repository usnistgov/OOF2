checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.7 $
# $Author: langer $
# $Date: 2014/09/27 21:41:57 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# This test just brings up all of the SkeletonModifier widgets, which
# ensures that they're not running on the wrong thread (which had
# happened in version 2.0.1.)

setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
findWidget('OOF2:Microstructure Page:Pane').set_position(150)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(314, 168)
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(153)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint active area status updated
checkpoint pixel page updated
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint OOF.Microstructure.New
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
findWidget('OOF2').resize(593, 434)
findWidget('OOF2:Skeleton Page:Pane').set_position(249)
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
checkpoint skeleton page sensitized
findWidget('Dialog-New skeleton').resize(334, 152)
findWidget('Dialog-New skeleton:gtk-ok').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
findWidget('OOF2:Skeleton Page:Pane').set_position(249)
checkpoint OOF.Skeleton.New
checkpoint_count("skeleton selection page sensitized")
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:criterion:Chooser'), 'Minimum Area')
findWidget('OOF2').resize(593, 486)
findWidget('OOF2:Skeleton Page:Pane').set_position(249)
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:criterion:Minimum Area:units'), 'Physical')
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:degree:Chooser'), 'Bisection')
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:degree:Bisection:rule_set'), 'liberal')
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 2.9487179487179e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 3.0128205128205e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 3.1410256410256e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 5.0641025641026e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 5.3846153846154e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 5.4487179487179e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 5.6410256410256e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 5.7692307692308e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 5.8333333333333e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 5.8974358974359e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 5.9615384615385e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 6.0256410256410e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 6.0897435897436e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 6.1538461538462e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 6.2179487179487e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 6.2820512820513e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 6.3461538461538e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 6.4102564102564e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 6.4743589743590e-01)
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:criterion:Chooser'), 'Unconditional')
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:degree:Bisection:rule_set'), 'conservative')
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Chooser'), 'Selected Elements')
findWidget('OOF2:Skeleton Page:Pane').set_position(264)
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:criterion:Chooser'), 'Minimum Area')
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:criterion:Chooser'), 'Unconditional')
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:degree:Chooser'), 'Trisection')
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:degree:Chooser'), 'Bisection')
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Chooser'), 'Elements In Group')
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Chooser'), 'All Elements')
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Chooser'), 'Aspect Ratio')
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Chooser'), 'Heterogeneous Segments')
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Pane').set_position(204)
checkpoint skeleton page sensitized
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Segments:choose_from:Chooser'), 'Selected Segments')
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Segments:choose_from:Chooser'), 'All Segments')
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Chooser'), 'Selected Segments')
findWidget('OOF2:Skeleton Page:Pane').set_position(264)
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Chooser'), 'Segments in Group')
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Chooser'), 'Adaptive Mesh Refinement')
findWidget('OOF2').resize(604, 614)
findWidget('OOF2:Skeleton Page:Pane').set_position(105)
checkpoint skeleton page sensitized
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(358, 94)
findWidget('Questioner:gtk-delete').clicked()
