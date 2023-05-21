import random

from gomoku.domain import Player
from gomoku.game_state import GameState
from gomoku.move import Move


class MCTSNode(object):
    def __init__(self, game_state: GameState, parent=None, move: Move = None):
        self.game_state = game_state
        self.parent = parent
        self.move = move
        self.win_counts = {
            Player.black: 0,
            Player.white: 0
        }
        self.num_rollouts = 0
        self.children = []
        if game_state.board.is_empty():
            self.unvisited_moves = random.sample(game_state.legal_moves(), 5)
        else:
            self.unvisited_moves = game_state.more_legal_moves()

    def add_child(self):
        index = random.randint(0, len(self.unvisited_moves) - 1)
        new_move = self.unvisited_moves.pop(index)
        new_game_state = self.game_state.apply_move(new_move)
        new_node = MCTSNode(new_game_state, self, new_move)
        self.children.append(new_node)
        return new_node

    def record_win(self, winner: Player):
        if winner is not None:
            self.win_counts[winner] += 1
        self.num_rollouts += 1

    def can_add_child(self):
        return len(self.unvisited_moves) > 0

    def is_terminal(self):
        return self.game_state.is_over()

    def winning_frac(self, player: Player):
        return float(self.win_counts[player]) / float(self.num_rollouts)
