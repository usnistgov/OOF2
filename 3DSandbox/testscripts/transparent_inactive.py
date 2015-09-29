OOF.Microstructure.Create_From_ImageFile(filename='../../TEST3D/ms_data/5color/slice*.tif', microstructure_name='slice*.tif', height=automatic, width=automatic, depth=automatic)
OOF.Image.AutoGroup(image='slice*.tif:slice*.tif')
OOF.Windows.Graphics.New()
OOF.ActiveArea.Activate_Pixel_Group_Only(microstructure='slice*.tif', group='RGBColor(red=0.93725490196078431,green=0.074509803921568626,blue=0.074509803921568626)')
