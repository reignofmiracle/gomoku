import unittest
import sys

sys.path.append('.')


class MCTSAgentTest(unittest.TestCase):

    def test_simulate_random_game(self):
        from gomoku.domain import Point
        from gomoku.game import Game
        from gomoku.board import Board
        from gomoku.mcts_agent import MCTSAgent
        from gomoku.game_state import GameState
        from gomoku.domain import Player
        from gomoku.r_bot import R_Bot

        board = Board(10, 10)
        game_state = GameState(board, Player.black, None, None)

        bots = {
            Player.black: R_Bot(),
            Player.white: R_Bot(),
        }

        while not game_state.is_over():
            bot_move = bots[game_state.next_player].select_move(game_state)
            if bot_move is None:
                break
            
            game_state = game_state.apply_move(bot_move)

        # test = Game(game_state.board)
        # test.run()


if __name__ == '__main__':
    unittest.main()
