#!/usr/bin/env python

import sys
from PySide.QtGui import *

app = QApplication.instance()

ok = QPushButton("&OK")
cancel = QPushButton("&Cancel")

layout = QHBoxLayout()
layout.addWidget(ok)
layout.addWidget(cancel)

widget = QWidget()
widget.setLayout(layout)
widget.show()

try:
    sys.exit(app.exec_())
except SystemExit:
    pass