import copy
from gomoku.board import Board
from gomoku.domain import Player, Point
from gomoku.move import Move
from gomoku.game_result import GameResult


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

    def apply_move(self, move):
        if move.is_play:
            next_board = copy.deepcopy(self.board)
            next_board.place_stone(self.next_player, move.point)
        else:
            next_board = self.board
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
        if move.is_pass or move.is_resign:
            return True
        return self.board.get(move.point) is None and not self.is_3_3(self.next_player, move)

    def is_over(self):
        if self.last_move is None:
            return False
        if self.last_move.is_resign:
            return True
        second_last_move = self.previous_state.last_move
        if second_last_move is None:
            return False
        return self.last_move.is_pass and second_last_move.is_pass

    def is_3_3(self, player: Player, move: Move):
        if not move.is_play:
            return False

        count = 0

        if self.board.get(move.point.left()) == player and self.board.get(move.point.right()) == player:
            count += 1

        if self.board.get(move.point.up()) == player and self.board.get(move.point.down()) == player:
            count += 1

        if self.board.get(move.point.lt()) == player and self.board.get(move.point.rb()) == player:
            count += 1

        if self.board.get(move.point.lb()) == player and self.board.get(move.point.rt()) == player:
            count += 1

        return count > 1

    def legal_moves(self):
        moves = []
        for row in range(1, self.board.num_rows + 1):
            for col in range(1, self.board.num_cols + 1):
                move = Move.play(Point(row, col))
                if self.is_valid_move(move):
                    moves.append(move)

        moves.append(Move.pass_turn())
        moves.append(Move.resign())

        return moves

    def winner(self):
        if not self.is_over():
            return None
        if self.last_move.is_resign:
            return self.next_player
        return GameResult.compute(self)
