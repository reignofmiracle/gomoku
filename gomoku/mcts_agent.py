import math
from gomoku.agent import Agent
from gomoku.domain import Player
from gomoku.game_state import GameState
from gomoku.mcts_node import MCTSNode
from gomoku.mcts_bot import MCTSBot
from gomoku.move import Move


class MCTSAgent(Agent):
    def __init__(self, num_rounds: int, temperature: float):
        Agent.__init__(self)
        self.num_rounds = num_rounds
        self.temperature = temperature

    def select_move(self, game_state: GameState) -> Move:
        move = MCTSBot.select_must_move(game_state)
        if move is not None:
            return move

        root = MCTSNode(game_state)
        for i in range(self.num_rounds):
            node = root
            while (not node.can_add_child()) and (not node.is_terminal()):
                node = self.select_child(node)

            if node.can_add_child():
                node = node.add_child()

            winner = self.simulate_random_game(node.game_state)

            while node is not None:
                node.record_win(winner)
                node = node.parent

        scored_moves = [
            (child.winning_frac(game_state.next_player),
             child.move, child.num_rollouts)
            for child in root.children
        ]
        scored_moves.sort(key=lambda x: x[0], reverse=True)
        for s, m, n in scored_moves[:10]:
            print('%s - %.3f (%d)' % (m, s, n))

        best_move = None
        best_pct = -1.0
        for child in root.children:
            child_pct = child.winning_frac(game_state.next_player)
            if child_pct > best_pct:
                best_pct = child_pct
                best_move = child.move
        print('Select move %s with win pct %.3f' % (best_move, best_pct))
        return best_move

    def select_child(self, node) -> MCTSNode:
        total_rollouts = sum(child.num_rollouts for child in node.children)
        log_rollouts = math.log(total_rollouts)

        best_score = -1
        best_child = None
        for child in node.children:
            win_percentage = child.winning_frac(node.game_state.next_player)
            exploration_factor = math.sqrt(log_rollouts / child.num_rollouts)
            uct_score = win_percentage + self.temperature * exploration_factor
            if uct_score > best_score:
                best_score = uct_score
                best_child = child
        return best_child

    @staticmethod
    def simulate_random_game(game_state: GameState) -> Player:
        bots = {
            Player.black: MCTSBot(),
            Player.white: MCTSBot(),
        }

        while not game_state.is_over():
            bot_move = bots[game_state.next_player].select_move(game_state)
            if bot_move is None:
                break

            game_state = game_state.apply_move(bot_move)

        return game_state.winner()
