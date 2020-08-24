setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
checkpoint page installed Microstructure
findWidget('OOF2').resize(593, 373)
findWidget('OOF2:Microstructure Page:Pane').set_position(225)
findWidget('OOF2:Microstructure Page:Pane').set_position(166)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:NewFromFile').clicked()
checkpoint toplevel widget mapped Dialog-Load Image and create Microstructure
findWidget('Dialog-Load Image and create Microstructure').resize(351, 138)
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small.pgm')
findWidget('Dialog-Load Image and create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(170)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
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
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Create_From_ImageFile
findWidget('OOF2:Microstructure Page:NewFromFile').clicked()
checkpoint toplevel widget mapped Dialog-Load Image and create Microstructure
findWidget('Dialog-Load Image and create Microstructure').resize(351, 138)
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cyallow.png')
findWidget('Dialog-Load Image and create Microstructure:gtk-ok').clicked()
findWidget('OOF2 Messages 1').resize(465, 200)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint microstructure page sensitized
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
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Create_From_ImageFile
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Image')
checkpoint page installed Image
findWidget('OOF2').resize(605, 373)
findWidget('OOF2:Image Page:Pane').set_position(394)
setComboBox(findWidget('OOF2:Image Page:Microstructure'), 'K1_small.pgm')
findWidget('OOF2:Image Page:Load').clicked()
checkpoint toplevel widget mapped Dialog-Load Image
findWidget('Dialog-Load Image').resize(310, 147)
findWidget('Dialog-Load Image:filename').set_text('examples/K1_small.pgm')
findWidget('Dialog-Load Image:gtk-ok').clicked()
findWidget('OOF2 Messages 1').resize(469, 200)
checkpoint microstructure page sensitized
checkpoint OOF.File.Load.Image
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(174)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Auto').clicked()
checkpoint toplevel widget mapped Dialog-AutoGroup
findWidget('Dialog-AutoGroup').resize(325, 303)
# cyallow
findWidget('Dialog-AutoGroup:minsize').set_text('10')
findWidget('Dialog-AutoGroup:gtk-ok').clicked()
findWidget('OOF2 Messages 1').resize(670, 200)
findWidget('OOF2:Microstructure Page:Pane').set_position(229)
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint microstructure page sensitized
# group_0 (2160) group_1 (1440)
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.AutoGroup
setComboBox(findWidget('OOF2:Microstructure Page:Microstructure'), 'K1_small.pgm')
findWidget('OOF2:Microstructure Page:Pane').set_position(174)
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Auto').clicked()
checkpoint toplevel widget mapped Dialog-AutoGroup
findWidget('Dialog-AutoGroup').resize(343, 303)
# K1_small.pgm
setComboBox(findWidget('Dialog-AutoGroup:grouper:Color:image:Image'), 'K1_small.pgm<2>')
# K1_small.pgm<2>
findWidget('Dialog-AutoGroup:minsize').set_text('')
findWidget('Dialog-AutoGroup:minsize').set_text('4')
findWidget('Dialog-AutoGroup:minsize').set_text('40')
findWidget('Dialog-AutoGroup:gtk-ok').clicked()
findWidget('OOF2 Messages 1').resize(728, 200)
findWidget('OOF2:Microstructure Page:Pane').set_position(229)
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
# group_0 (8302) group_1(70)
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.AutoGroup
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Auto').clicked()
checkpoint toplevel widget mapped Dialog-AutoGroup
findWidget('Dialog-AutoGroup').resize(343, 303)
setComboBox(findWidget('Dialog-AutoGroup:grouper:Color:image:Image'), 'K1_small.pgm<2>')
# K1_small.pgm<2>
setComboBox(findWidget('Dialog-AutoGroup:grouper:Color:image:Image'), 'K1_small.pgm')
# K1_small.pgm
findWidget('Dialog-AutoGroup:gtk-ok').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.AutoGroup
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(350, 91)
findWidget('Questioner:gtk-delete').clicked()
