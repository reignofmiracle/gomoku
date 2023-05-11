from gomoku.domain import Player, Point
import gomoku.zobrist as zobrist


class Board:
    def __init__(self, num_rows: int, num_cols: int) -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._grid = {}
        self._hash = zobrist.EMPTY_BOARD

    def is_on_grid(self, point) -> bool:
        return 1 <= point.row <= self.num_rows and 1 <= point.col <= self.num_cols

    def place_stone(self, player: Player, point: Point) -> None:
        assert self.is_on_grid(point)
        if self._grid.get(point) is not None:
            print('Illegal play on %s' % str(point))
        assert self._grid.get(point) is None

        self._grid[point] = player
        self._hash ^= zobrist.HASH_CODE[point, player]  # <3>

    def get(self, point) -> Player:
        return self._grid.get(point)

    def zobrist_hash(self) -> int:
        return self._hash
