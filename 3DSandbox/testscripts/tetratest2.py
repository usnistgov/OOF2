OOF.File.Load.Data(filename='/Users/vrc/OOF2/3DSandbox/testscripts/5colorms')
OOF.File.Load.Data(filename='/Users/vrc/OOF2/3DSandbox/testscripts/materials')
OOF.Material.Assign(material='blue', microstructure='slice*.tif', pixels='bluevoxels')
OOF.Material.Assign(material='white', microstructure='slice*.tif', pixels='whitevoxels')
OOF.Material.Assign(material='green', microstructure='slice*.tif', pixels='greenvoxels')
OOF.Material.Assign(material='yellow', microstructure='slice*.tif', pixels='yellowvoxels')
OOF.Material.Assign(material='red', microstructure='slice*.tif', pixels='redvoxels')
OOF.Windows.Graphics.New()
OOF.Skeleton.New(name='skeleton', microstructure='slice*.tif', x_elements=4, y_elements=4, z_elements=4, skeleton_geometry=TetraSkeleton(left_right_periodicity=False,top_bottom_periodicity=False,front_back_periodicity=False))


