import unittest
import sys


sys.path.append(".")


class GameTest(unittest.TestCase):
    def test_run(self):
        from gomoku.board import Board
        from gomoku.game import Game
        from gomoku.game_state import GameState
        from gomoku.domain import Player, Point
        from gomoku.mcts_agent import MCTSAgent

        board = Board(19, 19)
        game_state = GameState(board, Player.black, None, None)
        game = Game(game_state, MCTSAgent(50, 1.5))
        game.run()


if __name__ == "__main__":
    unittest.main()
