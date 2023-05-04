from gomoku.domain import Player


class GameResult:
    @staticmethod
    def compute(game_state) -> Player:
        return Player.white
