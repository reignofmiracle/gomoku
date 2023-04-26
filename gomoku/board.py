class Board:
    def __init__(self, num_rows: int, num_cols: int) -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._grid = {}

    def is_on_grid(self, point) -> bool:
        return 1 <= point.row <= self.num_rows and 1 <= point.col <= self.num_cols
