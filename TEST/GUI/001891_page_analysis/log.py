# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 


import tests

findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Microstructure
findWidget('OOF2').resize(593, 373)
findWidget('OOF2:Microstructure Page:Pane').set_position(225)
findWidget('OOF2:Microstructure Page:Pane').set_position(166)
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(320, 161)
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(170)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint active area status updated
checkpoint pixel page updated
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint microstructure page sensitized
checkpoint pixel page sensitized
checkpoint named boundary analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint mesh bdy page updated
checkpoint meshable button set
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint Solver page sensitized
checkpoint OOF.Microstructure.New
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2').resize(691, 373)
findWidget('OOF2:Materials Page:Pane').set_position(277)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(302, 97)
findWidget('Dialog-New material:gtk-ok').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.Material.New
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(249, 106)
setComboBox(findWidget('Dialog-Assign material material to pixels:pixels'), '<every>')
findWidget('Dialog-Assign material material to pixels:gtk-ok').clicked()
checkpoint OOF.Material.Assign
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((0,))
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1,), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1, 0), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((1, 0, 0))
checkpoint Materials page updated
checkpoint property deselected
checkpoint Materials page updated
checkpoint property selected
widget_0=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_0.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_0.window))
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.3975903614458e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.7951807228916e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1987951807229e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6783132530120e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9180722891566e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.3975903614458e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.8771084337349e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.1168674698795e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.3566265060241e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.5963855421687e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.8361445783133e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.3156626506024e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.7951807228916e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.5144578313253e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 6.4734939759036e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.1927710843373e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.4325301204819e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.1518072289157e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.3915662650602e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.8710843373494e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.1108433734940e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.3506024096386e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.5903614457831e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.8301204819277e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1, 3), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.8000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((1, 3, 0))
checkpoint Materials page updated
checkpoint property deselected
checkpoint Materials page updated
checkpoint property selected
widget_1=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_1.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_1.window))
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Fields & Equations')
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane').set_position(309)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2').resize(691, 374)
findWidget('OOF2:FE Mesh Page:Pane').set_position(474)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
checkpoint page installed Skeleton
findWidget('OOF2').resize(705, 430)
findWidget('OOF2:Skeleton Page:Pane').set_position(353)
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(400, 197)
findWidget('Dialog-New skeleton:gtk-ok').clicked()
findWidget('OOF2 Messages 1').resize(624, 200)
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint skeleton page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton page info updated
checkpoint skeleton selection page selection sensitized
checkpoint Solver page sensitized
checkpoint skeleton page info updated
checkpoint OOF.Skeleton.New
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Fields & Equations')
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane').set_position(315)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Pane').set_position(488)
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(330, 213)
findWidget('Dialog-Create a new mesh:gtk-ok').clicked()
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint mesh bdy page updated
checkpoint named boundary analysis chooser set
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.New
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Fields & Equations')
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Define
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Define
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Analysis')
checkpoint page installed Analysis
findWidget('OOF2:Analysis Page:bottom').set_position(354)
findWidget('OOF2').resize(788, 430)
findWidget('OOF2:Analysis Page:top').set_position(396)
findWidget('OOF2:Analysis Page:bottom').set_position(396)
findWidget('OOF2').resize(788, 438)
findWidget('OOF2').resize(791, 465)
findWidget('OOF2:Analysis Page:bottom').set_position(397)
findWidget('OOF2:Analysis Page:top').set_position(398)
findWidget('OOF2').resize(795, 508)
findWidget('OOF2:Analysis Page:bottom').set_position(400)
findWidget('OOF2:Analysis Page:top').set_position(400)
findWidget('OOF2').resize(795, 571)
findWidget('OOF2').resize(795, 584)
findWidget('OOF2').resize(795, 593)
findWidget('OOF2').resize(795, 612)
findWidget('OOF2').resize(795, 611)
findWidget('OOF2').resize(795, 609)
findWidget('OOF2').resize(795, 608)

# Scalar/Field/Component
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')


findWidget('OOF2:Analysis Page:top:Output:AggregateMode').clicked()
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint_count('named analysis chooser set')

# Aggregate/Field/Value Temperature
checkpoint_count("named analysis chooser set")
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

setComboBox(findWidget('OOF2:Analysis Page:top:Output:Aggregate:Parameters:field'), 'Displacement')
checkpoint named analysis chooser set
checkpoint named analysis chooser set
# Aggregate/Field/Value Displacement
checkpoint named analysis chooser set
assert tests.operationOptions('Direct Output', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

setComboBox(findWidget('OOF2:Analysis Page:top:Output:Aggregate:Aggregate_0'), 'Material Constants')
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
# Cijkl
assert tests.operationOptions('Direct Output')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

setComboBox(findWidget('OOF2:Analysis Page:top:Output:Aggregate:Aggregate_2'), 'Mass Density')
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
# Mass density
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

setComboBox(findWidget('OOF2:Analysis Page:bottom:Operation:OperationRCF:Chooser'), 'Range')
checkpoint named analysis chooser set
checkpoint named analysis chooser set
# Mass density/ Range
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')


setComboBox(findWidget('OOF2:Analysis Page:bottom:Operation:OperationRCF:Chooser'), 'Average')
checkpoint named analysis chooser set
checkpoint named analysis chooser set
# Mass density/ Average
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Element Set', 'Grid Points', 'Spaced Grid Points', 'Pixels')

setComboBox(findWidget('OOF2:Analysis Page:top:Output:Aggregate:Aggregate_2'), 'Elastic Modulus C')
checkpoint named analysis chooser set
checkpoint named analysis chooser set
# Cijkl/ Direct Output
checkpoint named analysis chooser set
assert tests.operationOptions('Direct Output')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')


findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 1.6818181818182e+00)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 8.4090909090909e+00)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 2.1863636363636e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 3.7000000000000e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 5.0454545454545e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 6.0545454545455e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 7.2318181818182e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 7.4000000000000e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 7.2318181818182e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 6.3909090909091e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 5.5500000000000e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 4.5409090909091e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 3.3636363636364e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 2.0181818181818e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 1.0090909090909e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 8.4090909090909e+00)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 0.0000000000000e+00)
setComboBox(findWidget('OOF2:Analysis Page:top:Output:Aggregate:Aggregate_0'), 'Concatenate')
checkpoint named analysis chooser set
checkpoint named analysis chooser set
# Concatenate Field/Value Field/Value
checkpoint named analysis chooser set
checkpoint_count("named analysis chooser set")
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')


setComboBox(findWidget('OOF2:Analysis Page:bottom:Operation:OperationRCF:Chooser'), 'Range')
checkpoint named analysis chooser set
checkpoint named analysis chooser set
# Concatenate Field/Value/Temperature Field/Value/Temperature Range
checkpoint_count('named analysis chooser set')
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

setComboBox(findWidget('OOF2:Analysis Page:top:Output:Aggregate:Parameters:first:Parameters:field'), 'Displacement')
checkpoint named analysis chooser set
checkpoint named analysis chooser set
# Concatenate Field/Value/Displacement Field/Value/Temperature  Direct Output
checkpoint named analysis chooser set
checkpoint_count('named analysis chooser set')
assert tests.operationOptions('Direct Output', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

setComboBox(findWidget('OOF2:Analysis Page:top:Output:Aggregate:Parameters:first:Parameters:field'), 'Temperature')
checkpoint named analysis chooser set
checkpoint named analysis chooser set
# Concatenate Field/Value/Temperature Field/Value/Temperature  Direct Output
checkpoint named analysis chooser set
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

checkpoint_count('named analysis chooser set')
setComboBox(findWidget('OOF2:Analysis Page:bottom:Operation:OperationRCF:Chooser'), 'Range')
# Concatenate Field/Value/Temperature Field/Value/Temperature  Range
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint_count('named analysis chooser set')
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

setComboBox(findWidget('OOF2:Analysis Page:top:Output:Aggregate:Parameters:first:first_0'), 'Material Constants')
checkpoint named analysis chooser set
checkpoint named analysis chooser set
# Concatenate Cijkl Field/Value/Temperature  Direct Output
checkpoint named analysis chooser set
checkpoint_count('named analysis chooser set')
assert tests.operationOptions('Direct Output')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

setComboBox(findWidget('OOF2:Analysis Page:top:Output:Aggregate:Parameters:first:first_2'), 'Mass Density')
checkpoint named analysis chooser set
checkpoint named analysis chooser set
# Concatenate MassDensity Field/Value/Temperature  Direct Output
checkpoint named analysis chooser set
checkpoint_count("named analysis chooser set")
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

setComboBox(findWidget('OOF2:Analysis Page:bottom:Operation:OperationRCF:Chooser'), 'Range')
checkpoint named analysis chooser set
checkpoint named analysis chooser set
# Concatenate MassDensity Field/Value Temperature  Range
checkpoint_count("named analysis chooser set")
assert tests.operationOptions('Direct Output', 'Range', 'Average and Deviation', 'Average', 'Integral', 'Standard Deviation')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

setComboBox(findWidget('OOF2:Analysis Page:top:Output:Aggregate:Parameters:first:first_2'), 'Elastic Modulus C')
checkpoint named analysis chooser set
checkpoint named analysis chooser set
# Concatenate Cijkl Field/Value Temperature  DirectOutput
checkpoint named analysis chooser set
checkpoint_count("named analysis chooser set")
assert tests.operationOptions('Direct Output')
assert tests.samplingOptions('Grid Points', 'Spaced Grid Points', 'Pixels')

findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(350, 91)
findWidget('Questioner:gtk-delete').clicked()
