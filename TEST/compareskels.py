initialskel = 'skeleton_data/modgroups'
reference = 'skeleton_data/snapnodes_0'
# modifier = Refine(
#     targets=CheckHeterogeneousSegments(threshold=1,choose_from=FromAllSegments()),
#     divider=TransitionPoints(minlength=2.0),
#     rules="Quick",
#     alpha=0.5)

modifier = SnapNodes(targets=SnapAll(),criterion=AverageEnergy(alpha=0.8))

OOF.File.Load.Data(filename=initialskel)
OOF.File.Load.Data(filename=reference)
OOF.Skeleton.Copy(skeleton='skeltest:modtest', name='original')
OOF.Windows.Graphics.New()
OOF.Graphics_1.Layer.New(category='Image', what='skeltest:small.ppm', how=BitmapDisplayMethod())
OOF.Graphics_1.Layer.New(category='Skeleton', what='skeltest:original', how=SkeletonEdgeDisplay(color=TranslucentGray(value=0.75,alpha=1.0),width=6))
OOF.Graphics_1.Layer.New(category='Skeleton', what='reference:modtest', how=SkeletonEdgeDisplay(color=RGBAColor(red=1,green=0.75,blue=0.458333,alpha=1),width=3))
OOF.Graphics_1.Layer.New(category='Skeleton', what='skeltest:modtest', how=SkeletonEdgeDisplay(color=TranslucentGray(value=0.0,alpha=1.0),width=0.5))


#OOF.Skeleton.Modify(skeleton='skeltest:modtest', modifier=SnapRefine(targets=CheckHeterogeneousEdges(threshold=1,choose_from=FromAllSegments()),criterion=Unconditionally(),min_distance=1))
OOF.Graphics_1.Settings.Zoom.Fill_Window()
#OOF.Skeleton.Undo(skeleton='skeltest:modtest')

OOF.Skeleton.Modify(skeleton='skeltest:modtest', modifier=modifier)
