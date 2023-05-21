import unittest
import sys

sys.path.append('.')


class BoardTest(unittest.TestCase):
    @unittest.skip("test")
    def test_update_continuous(self):
        from gomoku.domain import Point
        from gomoku.board import Board
        from gomoku.domain import Player

        board = Board(19, 19)
        board.place_stone(Player.black, Point(1, 1))
        board.place_stone(Player.black, Point(2, 1))
        board.place_stone(Player.black, Point(3, 1))

        board.place_stone(Player.black, Point(1, 2))
        board.place_stone(Player.black, Point(2, 2))
        board.place_stone(Player.black, Point(3, 2))
        board.place_stone(Player.black, Point(4, 2))

        board.place_stone(Player.black, Point(2, 3))
        board.place_stone(Player.black, Point(3, 3))
        board.place_stone(Player.black, Point(4, 3))

        board.place_stone(Player.black, Point(2, 4))
        board.place_stone(Player.black, Point(3, 4))
        board.place_stone(Player.black, Point(4, 4))
        board.place_stone(Player.black, Point(5, 4))

        print(f'continuous_full: {board.states[Player.black].continuous_full}')
        print(f'continuous_half: {board.states[Player.black].continuous_half}')

    @unittest.skip("test")
    def test_update_discontinuous(self):
        from gomoku.domain import Point
        from gomoku.board import Board
        from gomoku.domain import Player

        board = Board(19, 19)
        board.place_stone(Player.black, Point(1, 1))
        board.place_stone(Player.black, Point(2, 1))
        board.place_stone(Player.black, Point(4, 1))

        board.place_stone(Player.black, Point(1, 2))
        board.place_stone(Player.black, Point(2, 2))
        board.place_stone(Player.black, Point(3, 2))
        board.place_stone(Player.black, Point(5, 2))

        board.place_stone(Player.black, Point(2, 3))
        board.place_stone(Player.black, Point(3, 3))
        board.place_stone(Player.black, Point(5, 3))

        board.place_stone(Player.black, Point(2, 4))
        board.place_stone(Player.black, Point(3, 4))
        board.place_stone(Player.black, Point(4, 4))
        board.place_stone(Player.black, Point(6, 4))

        print(
            f'discontinuous_full: {board.states[Player.black].discontinuous_full}')
        print(
            f'discontinuous_half: {board.states[Player.black].discontinuous_half}')

    def test_update_discontinuous2(self):
        from gomoku.domain import Point
        from gomoku.board import Board
        from gomoku.domain import Player

        board = Board(19, 19)
        board.place_stone(Player.white, Point(1, 1))
        board.place_stone(Player.black, Point(1, 2))
        board.place_stone(Player.black, Point(1, 3))
        board.place_stone(Player.black, Point(1, 5))
        board.place_stone(Player.black, Point(1, 6))

        print(
            f'discontinuous_full: {board.states[Player.black].discontinuous_full}')
        print(
            f'discontinuous_half: {board.states[Player.black].discontinuous_half}')

    @unittest.skip("test")
    def test_found_5(self):
        from gomoku.domain import Point
        from gomoku.board import Board
        from gomoku.domain import Player

        board = Board(19, 19)
        board.place_stone(Player.black, Point(1, 2))
        board.place_stone(Player.black, Point(2, 2))
        board.place_stone(Player.black, Point(3, 2))
        board.place_stone(Player.black, Point(4, 2))
        board.place_stone(Player.black, Point(5, 2))

        print(f'found_5: {board.found_5}')

    def test_is_on_grid(self):
        from gomoku.domain import Point
        from gomoku.board import Board

        board = Board(19, 19)
        self.assertTrue(board.is_on_grid(Point(1, 1)))

    def test_is_on_grid(self):
        from gomoku.domain import Point
        from gomoku.board import Board

        board = Board(19, 19)
        self.assertTrue(board.is_on_grid(Point(1, 1)))


if __name__ == '__main__':
    unittest.main()
