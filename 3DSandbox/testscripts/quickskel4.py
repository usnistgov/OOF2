OOF.Microstructure.Create_From_ImageFile(filename='../../TEST3D/ms_data/5color/slice*.tif', microstructure_name='slice*.tif', height=automatic, width=automatic, depth=automatic)
OOF.Image.AutoGroup(image='slice*.tif:slice*.tif')
OOF.Skeleton.New(name='skeleton', microstructure='slice*.tif', x_elements=4, y_elements=4, z_elements=4, skeleton_geometry=TetraSkeleton(left_right_periodicity=False,top_bottom_periodicity=False,front_back_periodicity=False))
