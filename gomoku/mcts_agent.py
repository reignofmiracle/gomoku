from gomoku.agent import Agent
from gomoku.mcts_node import MCTSNode


class MCTSAgent(Agent):
    def __init__(self, num_rounds, temperature):
        Agent.__init__(self)
        self.num_rounds = num_rounds
        self.temperature = temperature

    def select_move(self, game_state):
        root = MCTSNode(game_state)

    def select_child(self, node):
        pass
