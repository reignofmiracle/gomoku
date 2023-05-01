from gomoku.domain import Player
from gomoku.game_state import GameState


class GameResult:
    @staticmethod
    def compute(game_state: GameState) -> Player:
        return Player.white
