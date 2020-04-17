import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import pyqtSignal
from PyQt5 import QtCore

class BoardInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self._parts = self.__create_parts()
        grid = self.__create_grid(self._parts)
        self.setLayout(grid)


    def __create_parts(self):
        parts = []
        labels = []
        for i in range(4):
            labels.append(BoardPart())
            parts.append(labels[i])
        return parts

    def __create_grid(self, parts):
        grid = QGridLayout()
        grid.addWidget(parts[0], 0, 0)
        grid.addWidget(parts[1], 1, 0)
        grid.addWidget(parts[2], 0, 1)
        grid.addWidget(parts[3], 1, 1)
        return grid


class BoardPart(QLabel):
    clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.check = False
        self.__set_img()

    def __set_img(self):
        if self.check:
            img = QPixmap('resources/board_part_click.png')
        else:
            img = QPixmap('resources/board_part.png')
        self.setPixmap(img)

    def mouseReleaseEvent(self, event):
        if self.check:
            self.check = False
        else:
            self.check = True
        self.__set_img()

    def keyPressEvent(self, e):
        if ((e.key() == QtCore.Qt.Key_Right) and self.check):
            self.check = False
            self.__set_img()
        elif ((e.key() == QtCore.Qt.Key_Left) and self.check):
            self.check = False
            self.__set_img()


def main():
    app = QApplication([])
    main_window = BoardInterface()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    sys.exit(main() or 0)