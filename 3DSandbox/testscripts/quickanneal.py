OOF.Microstructure.Create_From_ImageFile(filename='../../TEST3D/ms_data/5color/slice*.tif', microstructure_name='slice*.tif', height=automatic, width=automatic, depth=automatic)
OOF.Image.AutoGroup(image='slice*.tif:slice*.tif')
OOF.Skeleton.New(name='skeleton', microstructure='slice*.tif', x_elements=3, y_elements=3, z_elements=3, skeleton_geometry=TetraSkeleton(arrangement='moderate',left_right_periodicity=False,top_bottom_periodicity=False,front_back_periodicity=False))
OOF.Skeleton.Modify(skeleton='slice*.tif:skeleton', modifier=Anneal(targets=AllNodes(),criterion=AverageEnergy(alpha=0.29999999999999999),T=0.0,delta=1.0,iteration=FixedIteration(iterations=1)))
