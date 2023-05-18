import copy
from typing import List
from gomoku.board import Board
from gomoku.domain import Player, Point
from gomoku.move import Move


class GameState:
    def __init__(self, board: Board, next_player: Player, previous, move: Move):
        self.board = board
        self.next_player = next_player
        self.previous_state = previous
        if self.previous_state is None:
            self.previous_states = frozenset()
        else:
            self.previous_states = frozenset(
                previous.previous_states
                | {(previous.next_player, previous.board.zobrist_hash())}
            )
        self.last_move = move

    def apply_move(self, move: Move):
        next_board = copy.deepcopy(self.board)
        next_board.place_stone(self.next_player, move.point)
        return GameState(next_board, self.next_player.other, self, move)

    @classmethod
    def new_game(cls, board_size):
        if isinstance(board_size, int):
            board_size = (board_size, board_size)
        board = Board(*board_size)
        return GameState(board, Player.black, None, None)

    @property
    def situation(self):
        return (self.next_player, self.board)

    def is_valid_move(self, move):
        if self.is_over():
            return False
        return self.board.get(move.point) is None and not self.is_3_3(self.next_player, move)

    def is_over(self):
        if self.board.found_5 is not None:
            return True
        if self.last_move is None:
            return False

        return self.board.is_full()

    def is_3_3(self, player: Player, move: Move):
        count = 0

        if self.count(player, move,
                      1, 0) + self.count(player, move, -1, 0) == 2:
            count += 1

        if self.count(player, move,
                      0, 1) + self.count(player, move, 0, -1) == 2:
            count += 1

        if self.count(player, move,
                      -1, -1) + self.count(player, move, 1, 1) == 2:
            count += 1

        if self.count(player, move,
                      1, -1) + self.count(player, move, -1, 1) == 2:
            count += 1

        return count > 1

    def count(self, player: Player, move: Move, d_row: int, d_col: int):
        count = 0

        point = Point(move.point.row + d_row, move.point.col + d_col)
        while self.board.is_on_grid(point):
            if player != self.board.get(point):
                break

            count += 1

            point = Point(point.row + d_row, point.col + d_col)

        return count

    def legal_moves(self) -> List[Move]:
        moves = []
        for row in range(1, self.board.num_rows + 1):
            for col in range(1, self.board.num_cols + 1):
                move = Move.play(Point(row, col))
                if self.is_valid_move(move):
                    moves.append(move)

        return moves

    def winner(self) -> Player | None:
        return self.board.found_5
