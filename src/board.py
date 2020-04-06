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
            self._marbles[3][i] = tmp_board._marbles[self._count_row - i - 1][0]
        for i in range(3):
            self._marbles[3 + i][2] = tmp_board._marbles[3][0]
        for i in range(3):
            self._marbles[5][i] = tmp_board._marbles[self._count_row - i - 1][2]
        for i in range(3):
            self._marbles[3 + i][0] = tmp_board._marbles[5][i]

    def make_right_rotation_top_right(self):
        tmp_board = self.copy()
        for i in range(3):
            self._marbles[3][i] = tmp_board._marbles[3 + i][2]
        for i in range(3):
            self._marbles[3 + i][0] = tmp_board._marbles[3][3 - i - 1]
        for i in range(3):
            self._marbles[5][i] = tmp_board._marbles[3 + i][0]
        for i in range(3):
            self._marbles[3 + i][2] = tmp_board._marbles[5][3 - i - 1]

    def make_left_rotation_top_left(self):
        tmp_board = self.copy()
        for i in range(3):
            self._marbles[0][i] = tmp_board._marbles[3 - i - 1][0]
        for i in range(3):
            self._marbles[i][2] = tmp_board._marbles[0][i]
        for i in range(3):
            self._marbles[2][i] = tmp_board._marbles[3 - i - 1][2]
        for i in range(3):
            self._marbles[i][0] = tmp_board._marbles[2][i]

    def make_right_rotation_top_left(self):
        tmp_board = self.copy()
        for i in range(3):
            self._marbles[0][i] = tmp_board._marbles[i][2]
        for i in range(3):
            self._marbles[i][0] = tmp_board._marbles[0][3 - i - 1]
        for i in range(3):
            self._marbles[2][i] = tmp_board._marbles[i][0]
        for i in range(3):
            self._marbles[i][2] = tmp_board._marbles[2][3 - i - 1]

    def make_left_rotation_down_left(self):
        tmp_board = self.copy()
        for i in range(3):
            self._marbles[0][3 + i] = tmp_board._marbles[3 - i - 1][3]
        for i in range(3):
            self._marbles[i][5] = tmp_board._marbles[0][3 + i]
        for i in range(3):
            self._marbles[2][3 + i] = tmp_board._marbles[3 - i - 1][5]
        for i in range(3):
            self._marbles[i][3] = tmp_board._marbles[2][3 + i]

    def make_right_rotation_down_left(self):
        tmp_board = self.copy()
        for i in range(3):
            self._marbles[0][3 + i] = tmp_board._marbles[i][5]
        for i in range(3):
            self._marbles[i][3] = tmp_board._marbles[0][self._count_row - i - 1]
        for i in range(3):
            self._marbles[2][3 + i] = tmp_board._marbles[i][3]
        for i in range(3):
            self._marbles[i][5] = tmp_board._marbles[2][self._count_row - i - 1]

    def make_left_rotation_down_right(self):
        tmp_board = self.copy()
        for i in range(3):
            self._marbles[3][3 + i] = tmp_board._marbles[self._count_row - i - 1][3]
        for i in range(3):
            self._marbles[3 + i][5] = tmp_board._marbles[3][3 + i]
        for i in range(3):
            self._marbles[5][3 + i] = tmp_board._marbles[self._count_row - i - 1][5]
        for i in range(3):
            self._marbles[3 + i][3] = tmp_board._marbles[5][3 + i]

    def make_right_rotation_down_right(self):
        tmp_board = self.copy()
        for i in range(3):
            self._marbles[3][3 + i] = tmp_board._marbles[3 + i][5]
        for i in range(3):
            self._marbles[3 + i][3] = tmp_board._marbles[3][self._count_row - i - 1]
        for i in range(3):
            self._marbles[5][3 + i] = tmp_board._marbles[3 + i][3]
        for i in range(3):
            self._marbles[3 + i][5] = tmp_board._marbles[5][self._count_row - i - 1]

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

    def check_horizontal_and_vertical(self):
        win_list = []
        for i in range(self._count_col):
            for step in range(2):
                color_horizontal = self._marbles[step][i]
                color_vertical = self._marbles[i][step]
                check_horizontal = True
                check_vertical = True
                for j in range(step, 4 + step):
                    if color_horizontal != self._marbles[j][i] and self._marbles[j][i] != -1:
                        check_horizontal = False
                    if color_vertical != self._marbles[i][j] and self._marbles[i][j] != -1:
                        check_vertical = False
                if check_horizontal:
                    for j in range(step, 4 + step):
                        win_list[j - step].append([j, i])
                    return win_list
                if check_vertical:
                    for j in range(step, 4 + step):
                        win_list[j - step].append([i, j])
                    return win_list
        return None

    def check_diagonal(self):
        win_list = []
        for step in range(2):
            color_left = self._marbles[step][step]
            color_right = self._marbles[5 - step][step]
            check_left = True
            check_right = True
            for i in range(step, 4 + step):
                if color_left != self._marbles[i][i] and self._marbles[i][i] != -1:
                    check_left = False
                if color_right != self._marbles[5 - i][i] and self._marbles[5 - i][i] != -1:
                    check_right = False
            if check_left:
                for i in range(step, 4 + step):
                    win_list[i - step].append([i, i])
                return win_list
            if check_right:
                for i in range(step, 4 + step):
                    win_list[i - step].append([5 - i, i])
                return win_list
        for step in range(2):
            color = self._marbles[1 - step][step]
            check = True
            for i in range(5):
                if color != self._marbles[1 - step + i][step + i]:
                    check = False
                    break
            if check:
                for i in range(5):
                    win_list[i].append([1 - step + i, step + i])
                return win_list
        for step in range(2):
            color = self._marbles[4 + step][step]
            check = True
            for i in range(5):
                if color != self._marbles[4 + step - i][step + i]:
                    check = False
                    break
            if check:
                for i in range(5):
                    win_list[i].append([4 + step - i, step + i])
                return win_list
        return None

    def check_win_line(self):
        win_line = self.check_horizontal_and_vertical()
        if win_line is not None:
# todo - win
            return win_line
        win_line = self.check_diagonal()
        if win_line is not None:
# todo - win 
            return win_line




