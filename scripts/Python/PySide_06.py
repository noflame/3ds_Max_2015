#!/usr/bin/env python

import sys
from PySide.QtCore import * #for Qt.Horizontal
from PySide.QtGui import *

app = QApplication.instance()

spinBox = QSpinBox()
spinBox.setPrefix("$")
spinBox.setRange(0, 100)

slider = QSlider(Qt.Horizontal)
slider.setRange(0, 100)

spinBox.valueChanged.connect(slider.setValue)
slider.valueChanged.connect(spinBox.setValue)

layout = QHBoxLayout()
layout.addWidget(spinBox)
layout.addWidget(slider)

widget = QWidget()
widget.setLayout(layout)
widget.show()

try:
    sys.exit(app.exec_())
except SystemExit:
    pass