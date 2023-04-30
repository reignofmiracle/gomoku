import tkinter as tk

from gomoku.board import Board
from gomoku.board_view import BoardView
from gomoku.domain import Player, Point


class Game:
    def __init__(self, board: Board) -> None:
        self.board = board

        self.window = tk.Tk()

        self.board_view = BoardView(self.window, self.selected)
        self.board_view.update(self.board)

    def run(self):
        self.window.mainloop()

    def selected(self, point: Point):
        print(point.col, point.row)
        if len(self.board._grid) % 2 == 0:
            self.board.place_stone(Player.black, point)
        else:
            self.board.place_stone(Player.white, point)
        self.board_view.update(self.board)
