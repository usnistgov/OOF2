# This test just brings up all of the SkeletonModifier widgets, which
# ensures that they're not running on the wrong thread (which had
# happened in version 2.0.1.)

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 511)
event(Gdk.EventType.BUTTON_PRESS,x= 6.9000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(210, 236)
findWidget('OOF2').resize(782, 545)
findWidget('Dialog-Create Microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
checkpoint mesh bdy page updated
checkpoint pixel page sensitized
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint Solver page sensitized
checkpoint OOF.Microstructure.New
event(Gdk.EventType.BUTTON_PRESS,x= 8.6000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton
findWidget('OOF2:Skeleton Page:Pane').set_position(417)
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(346, 254)
findWidget('Dialog-New skeleton:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton page sensitized
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton page info updated
checkpoint skeleton selection page selection sensitized Element
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.New
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton page info updated
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 8.8888888888889e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 8.7500000000000e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 8.4722222222222e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 8.1944444444444e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 7.6388888888889e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 7.2222222222222e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 6.9444444444444e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 6.8055555555556e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 6.5277777777778e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 6.3888888888889e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 6.2500000000000e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 6.1111111111111e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 5.8333333333333e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 5.6944444444444e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 5.5555555555556e-01)
event(Gdk.EventType.BUTTON_PRESS,x= 1.0500000000000e+02,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:criterion:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Minimum Area']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2').resize(782, 578)
event(Gdk.EventType.BUTTON_PRESS,x= 4.6000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:criterion:Minimum Area:units').get_window())
checkpoint toplevel widget mapped chooserPopup-units
findMenu(findWidget('chooserPopup-units'), ['Physical']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-units') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 1.0800000000000e+02,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:degree:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Bisection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 7.8000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:degree:Bisection:rule_set').get_window())
checkpoint toplevel widget mapped chooserPopup-rule_set
findMenu(findWidget('chooserPopup-rule_set'), ['liberal']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-rule_set') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 2.9059829059829e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 3.0769230769231e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 3.2478632478632e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 3.6752136752137e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 3.7606837606838e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 3.8461538461538e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 3.9316239316239e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 4.1025641025641e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 4.2735042735043e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 4.3589743589744e-01)
event(Gdk.EventType.BUTTON_PRESS,x= 1.3100000000000e+02,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Relax']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(492)
checkpoint skeleton page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 5.9000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Snap Nodes']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(437)
checkpoint skeleton page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 9.9000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Split Quads']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(430)
checkpoint skeleton page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 9.3000000000000e+01,y= 2.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Split Quads:split_how:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Trial and Error']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 7.0000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Split Quads:targets:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Heterogeneous Elements']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(410)
event(Gdk.EventType.BUTTON_PRESS,x= 1.2000000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Anneal']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(437)
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Anneal:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 4.3055555555556e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Anneal:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 4.4444444444444e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Anneal:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 4.7222222222222e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Anneal:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 4.8611111111111e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Anneal:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 5.0000000000000e-01)
event(Gdk.EventType.BUTTON_PRESS,x= 6.1000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Anneal:iteration:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Conditional Iteration']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2').resize(782, 667)
findWidget('OOF2:Skeleton Page:Pane').set_position(293)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Anneal:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 5.5555555555556e+00)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Anneal:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 9.7222222222222e+00)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Anneal:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 1.2500000000000e+01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Anneal:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 1.5277777777778e+01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Anneal:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 1.6666666666667e+01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Anneal:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 1.8055555555556e+01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Anneal:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 1.9444444444444e+01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Anneal:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 2.0833333333333e+01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Anneal:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 2.2222222222222e+01)
event(Gdk.EventType.BUTTON_PRESS,x= 1.4800000000000e+02,y= 2.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Smooth']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(437)
checkpoint skeleton page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 1.1500000000000e+02,y= 6.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Smooth:criterion:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Limited Average Energy']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(390)
event(Gdk.EventType.BUTTON_PRESS,x= 1.2500000000000e+02,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Smooth:iteration:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Conditional Iteration']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2').resize(782, 703)
findWidget('OOF2:Skeleton Page:Pane').set_position(293)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Smooth:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 2.2222222222222e+01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Smooth:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 2.3611111111111e+01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Smooth:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 2.5000000000000e+01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Smooth:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 2.9166666666667e+01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Smooth:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 3.0555555555556e+01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Smooth:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 3.3333333333333e+01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Smooth:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 3.4722222222222e+01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Smooth:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 3.8888888888889e+01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Smooth:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 4.0277777777778e+01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Smooth:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 4.1666666666667e+01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Smooth:iteration:Conditional Iteration:condition:Acceptance Rate:acceptance_rate:slider').get_adjustment().set_value( 4.3055555555556e+01)
event(Gdk.EventType.BUTTON_PRESS,x= 1.2600000000000e+02,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Smooth:targets:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Nodes in Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2').resize(782, 734)
checkpoint skeleton page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 1.2400000000000e+02,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Swap Edges']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(437)
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 1.0600000000000e+02,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Swap Edges:targets:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Selected Elements']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 1.0200000000000e+02,y= 2.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Swap Edges:criterion:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Unconditional']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 8.0000000000000e+01,y= 7.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Merge Triangles']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
checkpoint skeleton page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 8.7000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Merge Triangles:targets:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Elements In Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
checkpoint skeleton page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 7.4000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Merge Triangles:criterion:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Limited Unconditional']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(390)
event(Gdk.EventType.BUTTON_PRESS,x= 1.2200000000000e+02,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Rationalize']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(285)
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 1.5400000000000e+02,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Rationalize:method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Automatic']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(437)
event(Gdk.EventType.BUTTON_PRESS,x= 1.1900000000000e+02,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Rationalize:method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Specified']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(285)
event(Gdk.EventType.BUTTON_PRESS,x= 1.3200000000000e+02,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Fix Illegal Elements']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(550)
checkpoint skeleton page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 2.1000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Snap Anneal']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(437)
checkpoint skeleton page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 8.8000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Anneal:iteration:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Conditional Iteration']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(293)
event(Gdk.EventType.BUTTON_PRESS,x= 1.2700000000000e+02,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Anneal:targets:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Elements in Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
checkpoint skeleton page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 1.4300000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Snap Refine']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(389)
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 5.6944444444444e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 5.9722222222222e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 6.1111111111111e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 6.2500000000000e-01)
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(336, 86)
findWidget('Questioner:Don"t Save').clicked()
