import unittest
import sys
sys.path.append('.')


class BoardTest(unittest.TestCase):

    def test_a(self):
        from gomoku.domain import Point
        from gomoku.board import Board

        board = Board(19, 19)
        self.assertTrue(board.is_on_grid(Point(1, 1)))
        pass


if __name__ == '__main__':
    unittest.main()
