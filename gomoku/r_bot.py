from gomoku.agent import Agent
from gomoku.game_state import GameState
from gomoku.move import Move


class R_Bot(Agent):
    def __init__(self):
        Agent.__init__(self)

    def select_move(self, game_state: GameState):
        return Move.pass_turn()
