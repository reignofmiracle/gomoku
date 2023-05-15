import unittest
import sys

sys.path.append(".")


class GameStateTest(unittest.TestCase):
    def test_cross1(self):
        from gomoku.board import Board
        from gomoku.domain import Player, Point
        from gomoku.game_state import GameState
        from gomoku.move import Move

        board = Board(10, 10)
        game_state = GameState(board, Player.black, None, None)

        board.place_stone(Player.black, Point(2, 1))
        board.place_stone(Player.black, Point(2, 3))
        self.assertFalse(game_state.is_3_3(Player.black, Move(Point(2, 2))))

        board.place_stone(Player.black, Point(1, 2))
        board.place_stone(Player.black, Point(3, 2))
        self.assertTrue(game_state.is_3_3(Player.black, Move(Point(2, 2))))

        board.place_stone(Player.black, Point(5, 3))
        board.place_stone(Player.black, Point(5, 4))
        self.assertFalse(game_state.is_3_3(Player.black, Move(Point(5, 2))))

        board.place_stone(Player.black, Point(6, 2))
        board.place_stone(Player.black, Point(7, 2))
        self.assertTrue(game_state.is_3_3(Player.black, Move(Point(5, 2))))

    def test_cross2(self):
        from gomoku.board import Board
        from gomoku.domain import Player, Point
        from gomoku.game_state import GameState
        from gomoku.move import Move

        board = Board(10, 10)
        game_state = GameState(board, Player.black, None, None)

        board.place_stone(Player.black, Point(1, 1))
        board.place_stone(Player.black, Point(3, 3))
        self.assertFalse(game_state.is_3_3(Player.black, Move(Point(2, 2))))

        board.place_stone(Player.black, Point(3, 1))
        board.place_stone(Player.black, Point(1, 3))
        self.assertTrue(game_state.is_3_3(Player.black, Move(Point(2, 2))))

        board.place_stone(Player.black, Point(6, 6))
        board.place_stone(Player.black, Point(7, 7))
        self.assertFalse(game_state.is_3_3(Player.black, Move(Point(5, 5))))

        board.place_stone(Player.black, Point(3, 7))
        board.place_stone(Player.black, Point(4, 6))
        self.assertTrue(game_state.is_3_3(Player.black, Move(Point(5, 5))))


if __name__ == "__main__":
    unittest.main()
