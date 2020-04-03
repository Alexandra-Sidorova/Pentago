from src.move import Move


class Player:
    def __init__(self, name, color):
        self._name = name
        self._color = color  # 0 white, 1 black
        self._prev_move = None

    def move(self, row, col, quarter, rotation):
        self._prev_move = Move(row, col, quarter, rotation)