anothertest = 'ok'
from ooflib.TEST.UTILS.file_utils import reference_file
fname = reference_file("fundamental_data", "errorcmd.py")
OOF.File.Load.Script(filename=fname)
anothertest = 'not ok'
