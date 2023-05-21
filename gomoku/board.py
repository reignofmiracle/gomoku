from typing import List, Tuple
from gomoku.domain import Player, Point
import gomoku.zobrist as zobrist


class BoardState:
    def __init__(self, keys: List[int]) -> None:
        self.continuous_full = {}
        self.continuous_half = {}

        self.discontinuous_full = {}
        self.discontinuous_half = {}

        for i in keys:
            self.continuous_full[i] = []
            self.continuous_half[i] = []

            self.discontinuous_full[i] = []
            self.discontinuous_half[i] = []

    def remove(self, point: Point):
        for k in self.continuous_full:
            self.continuous_full[k] = [
                item for item in self.continuous_full[k] if point not in item]

        for k in self.continuous_half:
            self.continuous_half[k] = [
                item for item in self.continuous_half[k] if point not in item]

        for k in self.discontinuous_full:
            self.discontinuous_full[k] = [
                item for item in self.discontinuous_full[k] if point not in item]

        for k in self.discontinuous_half:
            self.discontinuous_half[k] = [
                item for item in self.discontinuous_half[k] if point not in item]

    def remove_continuous_key(self, point: Point, key: int):
        for k in self.continuous_full:
            if k < key:
                self.continuous_full[k] = [
                    item for item in self.continuous_full[k] if point not in item]

        for k in self.continuous_half:
            if k < key:
                self.continuous_half[k] = [
                    item for item in self.continuous_half[k] if point not in item]

    def remove_discontinuous_key(self, point: Point, key: int):
        for k in self.discontinuous_full:
            if k < key:
                self.discontinuous_full[k] = [
                    item for item in self.discontinuous_full[k] if point not in item]

        for k in self.discontinuous_half:
            if k < key:
                self.discontinuous_half[k] = [
                    item for item in self.discontinuous_half[k] if point not in item]


class Board:
    def __init__(self, num_rows: int, num_cols: int) -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._grid = {}
        self._hash = zobrist.EMPTY_BOARD

        self.place_size = self.num_rows * self.num_cols
        self.found_5 = None

        self.keys = [3, 4]
        self.states = {
            Player.black: BoardState(self.keys),
            Player.white: BoardState(self.keys),
        }

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

        self.states[player].remove(point)
        self.states[player.other].remove(point)

        for key in self.keys:
            self.update_continuous(player, point, key)
            self.update_discontinuous(player, point, key)

    def get(self, point: Point) -> Player:
        return self._grid.get(point)

    def zobrist_hash(self) -> int:
        return self._hash

    def is_empty(self) -> bool:
        return len(self._grid) == 0

    def is_full(self) -> bool:
        return self.place_size == 0

    def check_5(self, player: Player, point: Point) -> bool:
        if self.count(player, point,
                      -1, 0)[0] + self.count(player, point, 1, 0)[0] + 1 == 5:
            return True

        if self.count(player, point,
                      0, -1)[0] + self.count(player, point, 0, 1)[0] + 1 == 5:
            return True

        if self.count(player, point,
                      -1, -1)[0] + self.count(player, point, 1, 1)[0] + 1 == 5:
            return True

        if self.count(player, point,
                      1, -1)[0] + self.count(player, point, -1, 1)[0] + 1 == 5:
            return True

        return False

    def update_continuous(self, player: Player, point: Point, size: int) -> None:
        self.states[player].remove_continuous_key(point, size)

        self.update_continuous_unit(player, point, -1, 0, 1, 0, size)
        self.update_continuous_unit(player, point, 0, -1, 0, 1, size)
        self.update_continuous_unit(player, point, -1, -1, 1, 1, size)
        self.update_continuous_unit(player, point, 1, -1, -1, 1, size)

    def update_continuous_unit(self, player: Player, point: Point | None, ax: int, ay: int, bx: int, by: int, size: int) -> None:
        if point is None:
            return

        a = self.count(player, point, ax, ay)
        b = self.count(player, point, bx, by)

        if a[0] + b[0] + 1 == size:
            if a[1] is not None and b[1] is not None:
                self.states[player].continuous_full[size].append([a[1], b[1]])
            elif a[1] is not None:
                self.states[player].continuous_half[size].append([a[1]])
            elif b[1] is not None:
                self.states[player].continuous_half[size].append([b[1]])

    def update_discontinuous(self, player: Player, point: Point, size: int) -> None:
        self.states[player].remove_discontinuous_key(point, size)

        self.update_discontinuous_unit(
            player, self.find_first_space(point, 1, 0), 1, 0, -1, 0, size)
        self.update_discontinuous_unit(
            player, self.find_first_space(point, -1, 0), 1, 0, -1, 0, size)

        self.update_discontinuous_unit(
            player, self.find_first_space(point, 0, -1), 0, -1, 0, 1, size)
        self.update_discontinuous_unit(
            player, self.find_first_space(point, -1, 0), 0, -1, 0, 1, size)

        self.update_discontinuous_unit(
            player, self.find_first_space(point, -1, -1), -1, -1, 1, 1, size)
        self.update_discontinuous_unit(
            player, self.find_first_space(point, 1, 1), -1, -1, 1, 1, size)

        self.update_discontinuous_unit(
            player, self.find_first_space(point, 1, -1), 1, -1, -1, 1, size)
        self.update_discontinuous_unit(
            player, self.find_first_space(point, -1, 1), 1, -1, -1, 1, size)

    def find_first_space(self, point: Point, ax: int, ay: int) -> Point | None:
        point = Point(point.row + ax, point.col + ay)
        while self.is_on_grid(point):
            if self.get(point) is None:
                break

            point = Point(point.row + ax, point.col + ay)

        if not self.is_on_grid(point):
            return None

        return point

    def update_discontinuous_unit(self, player: Player, point: Point | None, ax: int, ay: int, bx: int, by: int, size: int) -> None:
        if point is None:
            return

        a = self.count(player, point, ax, ay)
        b = self.count(player, point, bx, by)

        if a[0] + b[0] == size:
            if a[1] is not None and b[1] is not None:
                self.states[player].discontinuous_full[size].append([point])
            elif a[1] is not None:
                self.states[player].discontinuous_half[size].append([point])
            elif b[1] is not None:
                self.states[player].discontinuous_half[size].append([point])

    def count(self, player: Player, point: Point, d_row: int, d_col: int) -> Tuple[int, Point]:
        count = 0
        point = Point(point.row + d_row, point.col + d_col)
        while self.is_on_grid(point):
            if self.get(point) is not player:
                break

            count += 1
            point = Point(point.row + d_row, point.col + d_col)

        if not self.is_on_grid(point) or self.get(point) is not None:
            point = None

        return count, point
