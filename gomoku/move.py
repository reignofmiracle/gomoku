from gomoku.domain import Point


class Move:
    def __init__(self, point: Point = None):
        assert (point is not None)
        self.point = point

    @classmethod
    def play(cls, point):
        return Move(point=point)

    def __str__(self):
        return "(r %d, c %d)" % (self.point.row, self.point.col)
