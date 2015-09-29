OOF.File.Load.Data(filename='skel3')
OOF.Skeleton.Modify(skeleton='slice*.tif:skeleton', modifier=Anneal(targets=AllNodes(),criterion=AverageEnergy(alpha=0.29999999999999999),T=0.0,delta=1.0,iteration=FixedIteration(iterations=5)))
