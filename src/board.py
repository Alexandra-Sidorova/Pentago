from src.player import Player

""""
00 01 02  03 04 05
10 11 12  13 14 15
20 21 22  23 24 25

30 31 32  33 34 35
40 41 42  43 44 45
50 51 52  53 54 55
"""


class Board:
    def __init__(self, marbles=[]):
        self._marbles = marbles
        self._count_col = 6
        self._count_row = 6

    def new(self):
        self._marbles = [-1] * self._count_col
        for i in range(self._count_col):
            self._marbles[i] = [-1] * self._count_row

    def copy(self):
        copy_board = Board(self._marbles)
        return copy_board

    def put_marble(self, col, row, color):
        self._marbles[col][row] = color

    def make_left_rotation_top_right(self):
        tmp_board = self.copy()
        for i in range(3):
            self._marbles[i][3] = tmp_board._marbles[0][self._count_row - i - 1]
        for i in range(3):
            self._marbles[2][3 + i] = tmp_board._marbles[i][3]
        for i in range(3):
            self._marbles[i][5] = tmp_board._marbles[2][self._count_row - i - 1]
        for i in range(3):
            self._marbles[0][3 + i] = tmp_board._marbles[i][5]

    def make_right_rotation_top_right(self):
        tmp_board = self.copy()
        for i in range(3):
            self._marbles[i][3] = tmp_board._marbles[2][3 + i]
        for i in range(3):
            self._marbles[0][3 + i] = tmp_board._marbles[3 - i - 1][3]
        for i in range(3):
            self._marbles[i][5] = tmp_board._marbles[0][3 + i]
        for i in range(3):
            self._marbles[2][3 + i] = tmp_board._marbles[3 - i - 1][5]

    def make_left_rotation_top_left(self):
        tmp_board = self.copy()
        for i in range(3):
            self._marbles[i][0] = tmp_board._marbles[0][3 - i - 1]
        for i in range(3):
            self._marbles[2][i] = tmp_board._marbles[i][0]
        for i in range(3):
            self._marbles[i][2] = tmp_board._marbles[2][3 - i - 1]
        for i in range(3):
            self._marbles[0][i] = tmp_board._marbles[i][2]

    def make_right_rotation_top_left(self):
        tmp_board = self.copy()
        for i in range(3):
            self._marbles[i][0] = tmp_board._marbles[2][i]
        for i in range(3):
            self._marbles[0][i] = tmp_board._marbles[3 - i - 1][0]
        for i in range(3):
            self._marbles[i][2] = tmp_board._marbles[0][i]
        for i in range(3):
            self._marbles[2][i] = tmp_board._marbles[3 - i - 1][2]

    def make_left_rotation_down_left(self):
        tmp_board = self.copy()
        for i in range(3):
            self._marbles[3 + i][0] = tmp_board._marbles[3][3 - i - 1]
        for i in range(3):
            self._marbles[5][i] = tmp_board._marbles[3 + i][0]
        for i in range(3):
            self._marbles[3 + i][2] = tmp_board._marbles[5][3 - i - 1]
        for i in range(3):
            self._marbles[3][i] = tmp_board._marbles[3 + i][2]

    def make_right_rotation_down_left(self):
        tmp_board = self.copy()
        for i in range(3):
            self._marbles[3 + i][0] = tmp_board._marbles[5][i]
        for i in range(3):
            self._marbles[3][i] = tmp_board._marbles[self._count_row - i - 1][0]
        for i in range(3):
            self._marbles[3 + i][2] = tmp_board._marbles[3][i]
        for i in range(3):
            self._marbles[5][i] = tmp_board._marbles[self._count_row - i - 1][2]

    def make_left_rotation_down_right(self):
        tmp_board = self.copy()
        for i in range(3):
            self._marbles[3 + i][3] = tmp_board._marbles[3][self._count_row - i - 1]
        for i in range(3):
            self._marbles[5][3 + i] = tmp_board._marbles[3 + i][3]
        for i in range(3):
            self._marbles[3 + i][5] = tmp_board._marbles[5][self._count_row - i - 1]
        for i in range(3):
            self._marbles[3][3 + i] = tmp_board._marbles[3 + i][5]

    def make_right_rotation_down_right(self):
        tmp_board = self.copy()
        for i in range(3):
            self._marbles[3 + i][3] = tmp_board._marbles[5][3 + i]
        for i in range(3):
            self._marbles[3][3 + i] = tmp_board._marbles[self._count_row - i - 1][3]
        for i in range(3):
            self._marbles[3 + i][5] = tmp_board._marbles[3][3 + i]
        for i in range(3):
            self._marbles[5][3 + i] = tmp_board._marbles[self._count_row - i - 1][5]

    def make_rotation(self, quarter, rotation):
        if quarter == 0:
            if rotation == 0:
                self.make_left_rotation_top_right()
            else:
                self.make_right_rotation_top_right()
        elif quarter == 1:
            if rotation == 0:
                self.make_left_rotation_top_left()
            else:
                self.make_right_rotation_top_left()
        elif quarter == 2:
            if rotation == 0:
                self.make_left_rotation_down_left()
            else:
                self.make_right_rotation_down_left()
        elif quarter == 3:
            if rotation == 0:
                self.make_left_rotation_down_right()
            else:
                self.make_right_rotation_down_right()

    def make_move(self, move, color):
        self.put_marble(move.col, move.row, color)
        self.make_rotation(move.quarter, move.rotation)
