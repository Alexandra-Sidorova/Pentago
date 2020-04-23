from src.board import Board


class Game:
    def __init__(self, player_1, player_2):
        self._player_1 = player_1
        self._player_2 = player_2
        self._board = Board()
        self._next_step = 1
