from src.player import *

class Node:
    def __init__(self, board, depth):
        self._board = board.copy()
        self._depth = depth
        self._children = []

    def set_children(self):
        children_boards = self._board.list_children()
        for i in range(len(children_boards)):
            self._children.append(Node(children_boards[i]))

    def get_child(self, i):
        return self._children(i)

    def get_current_board(self):
        return self._board

    def count_children(self):
        return len(self._children)


class AI_MinMax(Player):
    def __init__(self, name, color, type = 0, depth = 2):
        super().__init__(name, color)
        self._type = type # 0 - minimax, 1 - alphabeta
        self._max_depth = depth
        self._max = None
        self._best_board = None

    def __minmax(self, node, player, depth): # 0 - max, 1 - min
        best_value = 0
        if depth == self._max_depth:
            return node.get_current_board().get_utility(self._color)
        if player == 0:
            best_value = -9999999
            node.set_children()
            for i in range(node.count_children()):
                this_value = self.__minmax(node.get_child(i), 1, depth + 1)
                if best_value < this_value:
                    best_value = this_value
                    self._best_board = node.get_child(i).get_current_board()
            return best_value
        else:
            best_value = 9999999
            node.set_children()
            for i in range(node.count_children()):
                this_value = self.__minmax(node.get_child(i), 0, depth + 1)
                if best_value > this_value:
                    best_value = this_value
            return best_value

    def __best_move(self, board):
        self.__minmax(Node(board, 0), 1, 0)

    def move(self, board):
        self._prev_move = self._best_board.last_move
        board.make_move(self._prev_move, self._color)


