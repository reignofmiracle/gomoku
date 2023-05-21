import enum
from collections import namedtuple


class Player(enum.Enum):
    black = 1
    white = 2

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white


class Point(namedtuple('Point', 'row, col')):
    def neighbors(self):
        return [
            Point(self.row - 1, self.col),
            Point(self.row + 1, self.col),
            Point(self.row, self.col - 1),
            Point(self.row, self.col + 1),
            Point(self.row - 1, self.col - 1),
            Point(self.row - 1, self.col + 1),
            Point(self.row + 1, self.col - 1),
            Point(self.row + 1, self.col + 1),
        ]

    def neighbors2(self):
        return [
            Point(self.row - 1, self.col),
            Point(self.row - 2, self.col),
            Point(self.row + 1, self.col),
            Point(self.row + 2, self.col),
            Point(self.row, self.col - 1),
            Point(self.row, self.col - 2),
            Point(self.row, self.col + 1),
            Point(self.row, self.col + 2),
            Point(self.row - 1, self.col - 1),
            Point(self.row - 2, self.col - 2),
            Point(self.row - 1, self.col + 1),
            Point(self.row - 2, self.col + 2),
            Point(self.row + 1, self.col - 1),
            Point(self.row + 2, self.col - 2),
            Point(self.row + 1, self.col + 1),
            Point(self.row + 2, self.col + 2),

            Point(self.row - 2, self.col - 1),
            Point(self.row - 2, self.col + 1),
            Point(self.row + 2, self.col - 1),
            Point(self.row + 2, self.col + 1),
            Point(self.row - 1, self.col - 2),
            Point(self.row + 1, self.col - 2),
            Point(self.row - 1, self.col + 2),
            Point(self.row + 1, self.col + 2),
        ]

    def up(self):
        return Point(self.row - 1, self.col)

    def down(self):
        return Point(self.row + 1, self.col)

    def left(self):
        return Point(self.row, self.col - 1)

    def right(self):
        return Point(self.row, self.col + 1)

    def lt(self):
        return Point(self.row - 1, self.col - 1)

    def rt(self):
        return Point(self.row - 1, self.col + 1)

    def lb(self):
        return Point(self.row + 1, self.col - 1)

    def rb(self):
        return Point(self.row + 1, self.col + 1)
