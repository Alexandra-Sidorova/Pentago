class Move:
    def __init__(self, row, col, quarter, rotation):
        self._row = row
        self._col = col
        self._quarter = quarter  # 0 top right, 1 top left, 2 down left, 3 down right
        self._rotation = rotation  # 0 - left, 1 - right
