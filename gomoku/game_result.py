from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gomoku.game_state import GameState

from gomoku.board import Board
from gomoku.domain import Player, Point


class GameResult:
    @staticmethod
    def compute(game_state: GameState) -> Player | None:
        return GameResult.find_5(game_state.board)

    @staticmethod
    def find_5(board: Board) -> Player | None:
        for row in range(board.num_rows):
            for col in range(board.num_cols):
                point = Point(row + 1, col + 1)
                if GameResult.has_5(board, point):
                    return board.get(point)

        return None

    @staticmethod
    def has_5(board: Board, point: Point):
        if GameResult.count(board, point,
                            1, 0) + GameResult.count(board, point, -1, 0) - 1 == 5:
            return True

        if GameResult.count(board, point,
                            0, 1) + GameResult.count(board, point, 0, -1) - 1 == 5:
            return True

        if GameResult.count(board, point,
                            -1, -1) + GameResult.count(board, point, 1, 1) - 1 == 5:
            return True

        if GameResult.count(board, point,
                            1, -1) + GameResult.count(board, point, -1, 1) - 1 == 5:
            return True

        return False

    @staticmethod
    def count(board: Board, point: Point, d_row: int, d_col: int):
        player = None
        count = 0

        while board.is_on_grid(point):
            if player is None:
                player = board.get(point)
            elif player != board.get(point):
                break

            if player is None:
                break

            count += 1

            point = Point(point.row + d_row, point.col + d_col)

        return count
