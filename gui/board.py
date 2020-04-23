import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import pyqtSignal
from PyQt5 import QtCore
from gui.marble import MarbleInterface
from src.board import Board


class BoardInterface(QWidget):
    def __init__(self, board):
        super().__init__()
        self.resize(500, 500)
        self._parts = self.__create_parts()
        self._marbles = self.__update(board.get_marbles())

    def __create_parts(self):
        parts = []
        labels = []
        for i in range(4):
            labels.append(BoardPart(self))
            parts.append(labels[i])
            parts[i].show()
        parts[0].move(0, 0)
        parts[1].move(251, 0)
        parts[2].move(0, 251)
        parts[3].move(251, 251)
        return parts

    def __update(self, marbles):
        marbles_list = []
        for x in range(6):
            for y in range(6):
                if x >= 3:
                    step_x = 25
                else:
                    step_x = 15
                if y >= 3:
                    step_y = 25
                else:
                    step_y = 15
                marble = MarbleInterface(self, step_x + x * 80, step_y + y * 80, marbles[x][y])
                marbles_list.append(marble)
        return marbles_list


class BoardPart(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)
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
    board = Board()
    main_window = BoardInterface(board)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    sys.exit(main() or 0)