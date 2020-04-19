class Move:
    def __init__(self, col, row, quarter, rotation):
        self._col = col
        self._row = row
        self._quarter = quarter  # 0 top right, 1 top left, 2 down left, 3 down right
        self._rotation = rotation  # 0 - left, 1 - right
