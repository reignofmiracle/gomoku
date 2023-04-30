import unittest
import sys

sys.path.append(".")


class GameTest(unittest.TestCase):
    def test_run(self):
        from gomoku.board import Board
        from gomoku.game import Game
        from gomoku.domain import Player, Point

        board = Board(10, 10)
        board.place_stone(Player.black, Point(2, 2))
        board.place_stone(Player.white, Point(1, 2))
        board.place_stone(Player.black, Point(1, 1))

        game = Game(board)
        game.run()


if __name__ == "__main__":
    unittest.main()
