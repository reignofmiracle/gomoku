from gomoku.game_state import GameState
from gomoku.move import Move


class Agent:
    def __init__(self):
        pass

    def select_move(self, game_state: GameState) -> Move:
        raise NotImplementedError()
