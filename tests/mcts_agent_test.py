import unittest
import sys
sys.path.append('.')


class MCTSAgentTest(unittest.TestCase):

    def test_simulate_random_game(self):
        from gomoku.domain import Point
        from gomoku.board import Board
        from gomoku.mcts_agent import MCTSAgent
        from gomoku.game_state import GameState
        from gomoku.domain import Player

        board = Board(10, 10)
        game_state = GameState(board, Player.black, None, None)

        winner = MCTSAgent.simulate_random_game(game_state)
        print(winner)


if __name__ == '__main__':
    unittest.main()
