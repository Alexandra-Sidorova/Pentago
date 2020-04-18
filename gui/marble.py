import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import pyqtSignal
from PyQt5 import QtCore

# -1 - default, 0 - white, 1 - black

class MarbleInterface(QLabel):
    def __init__(self, parent, x, y):
        super().__init__(parent)
        self.resize(60, 60)
        self._color = -1
        self.x = x
        self.y = y
        self.move(self.x, self.y)
        self.__set_img()
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)

    def __set_img(self):
        if self._color == -1:
            img = QPixmap('resources/default_marble.png')
        elif self._color == 0:
            img = QPixmap('resources/red_marble.png')
        elif self._color == 1:
            img = QPixmap('resources/black_marble.png')
        self.setPixmap(img)

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        self.move(self.x, self.y)

    def mouseReleaseEvent(self, event):
        if self._color == -1:
            pass