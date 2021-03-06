from src.move import Move


class Player:
    def __init__(self, name, color):
        self._name = name
        self._color = color  # 0 white, 1 black
        self._prev_move = None

    def name(self):
        return self._name

    def color(self):
        return self._color

    def move(self, board, row, col, quarter, rotation):
        self._prev_move = Move(row, col, quarter, rotation)
        board.make_move(self._prev_move, self._color)