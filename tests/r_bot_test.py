import unittest
import sys

sys.path.append('.')


class RBotTest(unittest.TestCase):

    def test_select_move(self):
        from gomoku.board import Board
        from gomoku.domain import Point
        from gomoku.game_state import GameState
        from gomoku.domain import Player
        from gomoku.r_bot import R_Bot

        board = Board(10, 10)
        board.place_stone(Player.black, Point(1, 5))
        board.place_stone(Player.black, Point(2, 5))
        board.place_stone(Player.black, Point(3, 5))
        board.place_stone(Player.black, Point(4, 5))

        game_state = GameState(board, Player.black, None, None)

        found = R_Bot.find_5_move(game_state, Player.black)
        self.assertIsNotNone(found)

    def test_find_5_move_1(self):
        from gomoku.board import Board
        from gomoku.domain import Point
        from gomoku.game_state import GameState
        from gomoku.domain import Player
        from gomoku.r_bot import R_Bot

        board = Board(10, 10)
        board.place_stone(Player.black, Point(1, 5))
        board.place_stone(Player.black, Point(2, 5))
        board.place_stone(Player.black, Point(3, 5))
        board.place_stone(Player.black, Point(4, 5))

        game_state = GameState(board, Player.black, None, None)

        found = R_Bot.find_5_move(game_state, Player.black)
        self.assertIsNotNone(found)

    def test_find_5_move_2(self):
        from gomoku.board import Board
        from gomoku.domain import Point
        from gomoku.game_state import GameState
        from gomoku.domain import Player
        from gomoku.r_bot import R_Bot

        board = Board(10, 10)

        board.place_stone(Player.black, Point(1, 2))
        board.place_stone(Player.black, Point(1, 3))
        board.place_stone(Player.black, Point(1, 4))
        board.place_stone(Player.black, Point(1, 6))

        game_state = GameState(board, Player.black, None, None)

        found = R_Bot.find_5_move(game_state, Player.black)
        self.assertIsNotNone(found)

    def test_find_5_move_3(self):
        from gomoku.board import Board
        from gomoku.domain import Point
        from gomoku.game_state import GameState
        from gomoku.domain import Player
        from gomoku.r_bot import R_Bot

        board = Board(10, 10)

        board.place_stone(Player.black, Point(1, 1))
        board.place_stone(Player.black, Point(2, 2))
        board.place_stone(Player.black, Point(3, 3))
        board.place_stone(Player.black, Point(4, 4))

        game_state = GameState(board, Player.black, None, None)

        found = R_Bot.find_5_move(game_state, Player.black)
        self.assertIsNotNone(found)

    def test_find_5_move_4(self):
        from gomoku.board import Board
        from gomoku.domain import Point
        from gomoku.game_state import GameState
        from gomoku.domain import Player
        from gomoku.r_bot import R_Bot

        board = Board(10, 10)

        board.place_stone(Player.black, Point(1, 9))
        board.place_stone(Player.black, Point(2, 8))
        board.place_stone(Player.black, Point(3, 7))
        board.place_stone(Player.black, Point(4, 6))

        game_state = GameState(board, Player.black, None, None)

        found = R_Bot.find_5_move(game_state, Player.black)
        self.assertIsNotNone(found)


if __name__ == '__main__':
    unittest.main()
