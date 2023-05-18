from gomoku.domain import Player, Point
import gomoku.zobrist as zobrist


class Board:
    def __init__(self, num_rows: int, num_cols: int) -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._grid = {}
        self._hash = zobrist.EMPTY_BOARD

        self.place_size = self.num_rows * self.num_cols
        self.found_5 = None

    def is_on_grid(self, point: Point) -> bool:
        return 1 <= point.row <= self.num_rows and 1 <= point.col <= self.num_cols

    def place_stone(self, player: Player, point: Point) -> None:
        assert self.is_on_grid(point)
        if self._grid.get(point) is not None:
            print('Illegal play on %s' % str(point))
        assert self._grid.get(point) is None

        self._grid[point] = player
        self._hash ^= zobrist.HASH_CODE[point, player]
        self.place_size -= 1
        self.found_5 = player if self.check_5(player, point) else None

    def get(self, point: Point) -> Player:
        return self._grid.get(point)

    def zobrist_hash(self) -> int:
        return self._hash

    def is_full(self) -> bool:
        return self.place_size == 0

    def check_5(self, player: Player, point: Point) -> bool:
        if self.count(player, point,
                      1, 0) + self.count(player, point, -1, 0) + 1 == 5:
            return True

        if self.count(player, point,
                      0, 1) + self.count(player, point, 0, -1) + 1 == 5:
            return True

        if self.count(player, point,
                      -1, -1) + self.count(player, point, 1, 1) + 1 == 5:
            return True

        if self.count(player, point,
                      1, -1) + self.count(player, point, -1, 1) + 1 == 5:
            return True

        return False

    def count(self, player: Player, point: Point, d_row: int, d_col: int) -> int:
        count = 0
        point = Point(point.row + d_row, point.col + d_col)
        while self.is_on_grid(point):
            if self.get(point) is not player:
                break

            count += 1
            point = Point(point.row + d_row, point.col + d_col)

        return count
