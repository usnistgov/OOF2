anothertest = 'ok'
from oof2.TEST.UTILS.file_utils import reference_file
fname = reference_file("fundamental_data", "errorcmd.py")
OOF.File.Load.Script(filename=fname)
anothertest = 'not ok'
