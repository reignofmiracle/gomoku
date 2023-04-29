
import tkinter as tk
import os
from PIL import ImageTk, Image

from gomoku.board import Board
from gomoku.board_renderer import BoardRenderer


class Game:
    def __init__(self, board: Board) -> None:
        self.board = board

        self.window = tk.Tk()

        self.board_renderer = BoardRenderer(self.window)
        self.board_renderer.render(self.board)

    def run(self):
        self.window.mainloop()
