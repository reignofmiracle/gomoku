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
        found = MCTSBot.select_must_move(game_state)
        if found is not None:
            return found

        legal_moves = game_state.more_legal_moves2()
        if len(legal_moves) == 0:
            legal_moves = game_state.legal_moves()
            if len(legal_moves) == 0:
                return None

        return random.choice(legal_moves)

    @staticmethod
    def select_must_move(game_state: GameState) -> Move | None:
        # 나의 5 완성
        found = MCTSBot.find_5_move(game_state, game_state.next_player)
        if found is not None:
            return found

        # 상대 5 완성 저지
        found = MCTSBot.find_5_move(game_state, game_state.next_player.other)
        if found is not None:
            return found

        # 상대 4 완성 저지
        found = MCTSBot.find_4_move_full(
            game_state, game_state.next_player.other)
        if found is not None:
            return found

        # 나의 4 완성
        found = MCTSBot.find_4_move_full(game_state, game_state.next_player)
        if found is not None:
            return found

        return None

    @staticmethod
    def find_5_move(game_state: GameState, player: Player) -> Move | None:
        if len(game_state.board.states[player].continuous_full[4]) > 0:
            return Move.play(random.choice(game_state.board.states[player].continuous_full[4])[0])

        if len(game_state.board.states[player].continuous_half[4]) > 0:
            return Move.play(random.choice(game_state.board.states[player].continuous_half[4])[0])

        if len(game_state.board.states[player].discontinuous_full[4]) > 0:
            return Move.play(random.choice(game_state.board.states[player].discontinuous_full[4])[0])

        if len(game_state.board.states[player].discontinuous_half[4]) > 0:
            return Move.play(random.choice(game_state.board.states[player].discontinuous_half[4])[0])

        return None

    @staticmethod
    def find_4_move_full(game_state: GameState, player: Player) -> Move | None:
        if len(game_state.board.states[player].continuous_full[3]) > 0:
            return Move.play(random.choice(game_state.board.states[player].continuous_full[3])[0])

        if len(game_state.board.states[player].discontinuous_full[3]) > 0:
            return Move.play(random.choice(game_state.board.states[player].discontinuous_full[3])[0])

        return None

    @staticmethod
    def find_4_move_half(game_state: GameState, player: Player) -> Move | None:
        if len(game_state.board.states[player].continuous_half[3]) > 0:
            return Move.play(random.choice(game_state.board.states[player].continuous_half[3])[0])

        if len(game_state.board.states[player].discontinuous_half[3]) > 0:
            return Move.play(random.choice(game_state.board.states[player].discontinuous_half[3])[0])

        return None
