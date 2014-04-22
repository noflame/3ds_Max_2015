#!/usr/bin/env python

import sys
from PySide.QtGui import *

app = QApplication.instance()

button = QPushButton("&Quit")
button.clicked.connect(button.close)
button.show()

try:
    sys.exit(app.exec_())
except SystemExit:
    pass