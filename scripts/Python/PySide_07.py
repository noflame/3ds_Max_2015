#!/usr/bin/env python
#物件導向的寫法

import sys
from PySide.QtCore import * #for Qt.Horizontal
from PySide.QtGui import *

class MyWidget(QWidget):
    def __init__(self, parent = None):
        super(MyWidget, self).__init__(parent)
        self.createLayout()
        self.spinBox.valueChanged.connect(self.slider.setValue)
        self.slider.valueChanged.connect(self.spinBox.setValue)
    
    def createLayout(self):
        self.spinBox = QSpinBox()
        self.spinBox.setPrefix("$")
        self.spinBox.setRange(0, 100)
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        
        layout = QHBoxLayout()
        layout.addWidget(self.spinBox)
        layout.addWidget(self.slider)
        self.setLayout(layout)


app = QApplication.instance()

widget = MyWidget()
widget.show()

try:
    sys.exit(app.exec_())
except SystemExit:
    pass