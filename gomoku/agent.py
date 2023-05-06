from gomoku.game_state import GameState


class Agent:
    def __init__(self):
        pass

    def select_move(self, game_state: GameState):
        raise NotImplementedError()
