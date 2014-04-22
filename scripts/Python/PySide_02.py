import sys
from PySide.QtGui import *

app = QApplication.instance()

button = QPushButton("H&ello!")
button.resize(200, 75)
button.move(500, 400)
button.setWindowTitle("Hello World")
button.show()

try:
    sys.exit(app.exec_())
except SystemExit:
    pass