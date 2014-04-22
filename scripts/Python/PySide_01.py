import sys
from PySide import QtGui

app = QtGui.QApplication.instance()

wid = QtGui.QWidget()
wid.resize(250, 150)
wid.setWindowTitle('Simple')
wid.show()

try:
    sys.exit(app.exec_())
except SystemExit:
    pass