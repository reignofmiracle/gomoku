import tkinter as tk

from gomoku.board import Board
from gomoku.domain import Player, Point


class BoardRenderer:
    def __init__(self, window: tk.Tk) -> None:
        self.window = window

        self.black = tk.PhotoImage(file="gomoku/resources/black.png")
        self.white = tk.PhotoImage(file="gomoku/resources/white.png")
        self.shadow = tk.PhotoImage(file="gomoku/resources/shadow.png")
        self.background = tk.PhotoImage(file="gomoku/resources/shinkaya.png")

        self.cw = self.black.width()
        self.ch = self.black.height()

        self.canvas = None

    def render(self, board: Board):
        self.render_window(board)
        self.render_stones(board)

        # canvas.create_image(0, 0, image=self.black)

        # canvas.create_image(100, 100, image=self.shadow)
        # canvas.create_image(100, 100, image=self.black)

        # label = tk.Label(image=self.black)
        # label.place(x=100, y=100)

    def render_window(self, board: Board):
        window_width = (board.num_cols + 3) * self.cw
        window_height = (board.num_rows + 3) * self.ch

        self.window.geometry(f"{window_width}x{window_height}")

        canvas_width = (board.num_cols + 1) * self.cw
        canvas_height = (board.num_rows + 1) * self.ch

        self.canvas = tk.Canvas(self.window, width=canvas_width,
                                height=canvas_height, background='gray')
        self.canvas.pack(padx=self.cw, pady=self.ch)

        # 배경 전시
        self.canvas.create_image(0, 0, image=self.background, anchor=tk.NW)

        # 격자 전시
        for row in range(0, board.num_rows):
            self.canvas.create_line(self.cw, (row + 1) * self.ch,
                                    canvas_width - self.cw, (row + 1) * self.ch, width=2)

        for col in range(0, board.num_cols):
            self.canvas.create_line((col + 1) * self.cw, self.ch,
                                    (col + 1) * self.cw, canvas_height - self.ch, width=2)

    def render_stones(self, board: Board):
        for item in board._grid:
            self.render_stone(board.get(item), item)
            pass

    def render_stone(self, player: Player, point: Point):
        x = point.col * self.cw
        y = point.row * self.ch
        if player == Player.white:
            self.canvas.create_image(x, y, image=self.white)
        else:
            self.canvas.create_image(x, y, image=self.black)
