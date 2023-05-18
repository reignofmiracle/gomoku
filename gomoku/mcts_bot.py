import random


from gomoku.agent import Agent
from gomoku.board import Board
from gomoku.domain import Player, Point
from gomoku.game_state import GameState
from gomoku.move import Move


class MCTSBot(Agent):
    def __init__(self):
        Agent.__init__(self)

    def select_move(self, game_state: GameState):
        # 나의 5 완성
        found = MCTSBot.find_5_move(game_state, game_state.next_player)
        if found is not None:
            return found

        # 상대 5 완성 저지
        found = MCTSBot.find_5_move(game_state, game_state.next_player.other)
        if found is not None:
            return found

        legal_moves = game_state.legal_moves()
        if len(legal_moves) == 0:
            return None

        return random.choice(legal_moves)

    @staticmethod
    def find_5_move(game_state: GameState, player: Player) -> Move | None:
        for move in game_state.legal_moves():
            if MCTSBot.has_4(game_state.board, player, move.point):
                return move

        return None

    @staticmethod
    def has_4(board: Board, player: Player, point: Point):
        if MCTSBot.count(board, player, point,
                         1, 0) + MCTSBot.count(board, player, point, -1, 0) == 4:
            return True

        if MCTSBot.count(board, player, point,
                         0, 1) + MCTSBot.count(board, player, point, 0, -1) == 4:
            return True

        if MCTSBot.count(board, player, point,
                         -1, -1) + MCTSBot.count(board, player, point, 1, 1) == 4:
            return True

        if MCTSBot.count(board, player, point,
                         1, -1) + MCTSBot.count(board, player, point, -1, 1) == 4:
            return True

        return False

    @staticmethod
    def count(board: Board, player: Player, point: Point, d_row: int, d_col: int):
        count = 0

        point = Point(point.row + d_row, point.col + d_col)
        while board.is_on_grid(point):
            if player != board.get(point):
                break

            count += 1

            point = Point(point.row + d_row, point.col + d_col)

        return count