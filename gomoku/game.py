import tkinter as tk
from tkinter import messagebox
from gomoku.agent import Agent

from gomoku.board import Board
from gomoku.board_view import BoardView
from gomoku.domain import Player, Point
from gomoku.game_state import GameState
from gomoku.mcts_agent import MCTSAgent
from gomoku.move import Move


class Game:
    def __init__(self, game_state: GameState, agent: Agent) -> None:
        self.game_state = game_state
        self.agent = agent

        self.window = tk.Tk()

        self.board_view = BoardView(self.window, self.selected)
        self.board_view.update(self.game_state.board)

    def run(self):
        self.window.mainloop()

    def selected(self, point: Point):
        move = Move.play(point)
        if self.game_state.is_3_3(self.game_state.next_player, move):
            messagebox.showinfo(title="Info", message="3x3 is not allowed")
            return

        self.game_state = self.game_state.apply_move(Move.play(point))
        self.board_view.update(self.game_state.board)

        move = self.agent.select_move(self.game_state)
        self.game_state = self.game_state.apply_move(move)
        self.board_view.update(self.game_state.board)
