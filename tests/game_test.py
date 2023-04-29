import unittest
import sys
sys.path.append('.')


class GameTest(unittest.TestCase):
    def test_run(self):
        from gomoku.board import Board
        from gomoku.game import Game
        from gomoku.domain import Player, Point

        board = Board(19, 19)
        board.place_stone(Player.black, Point(2, 2))
        board.place_stone(Player.white, Point(1, 2))

        game = Game(board)
        game.run()


if __name__ == '__main__':
    unittest.main()
