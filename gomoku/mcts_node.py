from gomoku.domain import Player
from gomoku.game_state import GameState


class MCTSNode(object):
    def __init__(self, game_state: GameState, parent=None, move=None):
        self.game_state = game_state
        self.parent = parent
        self.move = move
        self.win_counts = {
            Player.black: 0,
            Player.white: 0
        }
        self.num_rollouts = 0
        self.children = []
        self.unvisited_moves = game_state.legal_moves()

    def add_child(self):
        pass

    def record_win(self, winner):
        pass

    def can_add_child(self):
        return len(self.unvisited_moves) > 0

    def is_terminal(self):
        return self.game_state.is_over()

    def winning_frac(self, player: Player):
        return float(self.win_counts[player]) / float(self.num_rollouts)
