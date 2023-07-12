# After using skeleton_generate.py to create potential new reference
# files for skeleton_basic_test tests, use this script to compare the
# new files to the old.  Run it like this:
#  % oof2 --command="name='filename'" --sc skelcomp.py
# where filename is the name of the reference file in the
# skeleton_data directory.

# skeleton_generate.py creates a new reference file called
# "skel_[filename]" in the current directory.  To accept the new file,
# run
#  % mv skel[filename] skeleton_data/[filename]

OOF.File.Load.Data(filename="skel_"+name)
OOF.Microstructure.Rename(microstructure='skelcomp', name='new')
OOF.Settings.Graphics_Defaults.New_Layer_Policy(policy='Single')
OOF.Windows.Graphics.New()
OOF.Graphics_1.Layer.Select(n=4)
OOF.File.Load.Data(filename='/Users/langer/FE/OOF2/TEST/skeleton_data/' + name)
OOF.Graphics_1.Layer.New(category='Skeleton', what='skelcomp:reference', how=SkeletonEdgeDisplay(color=TranslucentGray(value=0.516129,alpha=1),width=5.))
OOF.Graphics_1.Layer.Lower.One_Level(n=5)
