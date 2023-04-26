import unittest

from gomoku.board import Board
from gomoku.domain import Point


class BoardTest(unittest.TestCase):
    def test_a(self):
        board = Board(19, 19)
        self.assertTrue(board.is_on_grid(Point(1, 1)))
        pass


if __name__ == '__main__':
    unittest.main()
