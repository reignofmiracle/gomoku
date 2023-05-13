import unittest
import sys
import tkinter as tk


sys.path.append('.')


class ScoringTest(unittest.TestCase):

    def test_case_1(self):
        from gomoku.board import Board
        from gomoku.domain import Player, Point
        from gomoku.game_result import GameResult

        board = Board(10, 10)

        board.place_stone(Player.black, Point(1, 1))
        board.place_stone(Player.black, Point(2, 1))
        board.place_stone(Player.black, Point(3, 1))
        board.place_stone(Player.black, Point(4, 1))
        board.place_stone(Player.black, Point(5, 1))

        self.assertTrue(GameResult.has_5(board, Point(3, 1)))

    def test_case_2(self):
        from gomoku.board import Board
        from gomoku.domain import Player, Point
        from gomoku.game_result import GameResult

        board = Board(10, 10)

        board.place_stone(Player.black, Point(1, 1))
        board.place_stone(Player.black, Point(1, 2))
        board.place_stone(Player.black, Point(1, 3))
        board.place_stone(Player.black, Point(1, 4))
        board.place_stone(Player.black, Point(1, 5))

        self.assertTrue(GameResult.has_5(board, Point(1, 3)))

    def test_case_3(self):
        from gomoku.board import Board
        from gomoku.domain import Player, Point
        from gomoku.game_result import GameResult

        board = Board(10, 10)

        board.place_stone(Player.black, Point(1, 1))
        board.place_stone(Player.black, Point(2, 2))
        board.place_stone(Player.black, Point(3, 3))
        board.place_stone(Player.black, Point(4, 4))
        board.place_stone(Player.black, Point(5, 5))

        self.assertTrue(GameResult.has_5(board, Point(3, 3)))

    def test_case_4(self):
        from gomoku.board import Board
        from gomoku.domain import Player, Point
        from gomoku.game_result import GameResult

        board = Board(10, 10)

        board.place_stone(Player.black, Point(1, 5))
        board.place_stone(Player.black, Point(2, 4))
        board.place_stone(Player.black, Point(3, 3))
        board.place_stone(Player.black, Point(4, 2))
        board.place_stone(Player.black, Point(5, 1))

        self.assertTrue(GameResult.has_5(board, Point(3, 3)))


if __name__ == '__main__':
    unittest.main()
