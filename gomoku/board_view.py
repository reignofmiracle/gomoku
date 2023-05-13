import tkinter as tk
import string
from gomoku.board import Board
from gomoku.domain import Player, Point


class BoardView:
    def __init__(self, window: tk.Tk, callback) -> None:
        self.window = window
        self.callback = callback

        self.canvas = None

        self.black = tk.PhotoImage(file="gomoku/resources/black.png")
        self.white = tk.PhotoImage(file="gomoku/resources/white.png")
        self.shadow = tk.PhotoImage(file="gomoku/resources/shadow.png")
        self.background = tk.PhotoImage(file="gomoku/resources/shinkaya.png")

        self.cell_width = self.black.width()
        self.cell_height = self.black.height()

        self.margin_selection = 20

    def selected(self, event):
        row = int(event.y / self.cell_height)
        if event.y % self.cell_height > self.cell_height * 0.5:
            row += 1

        row_min = row * self.cell_height - self.margin_selection
        row_max = row * self.cell_height + self.margin_selection
        if event.y < row_min or event.y > row_max:
            return

        col = int(event.x / self.cell_width)
        if event.x % self.cell_width > self.cell_width * 0.5:
            col += 1

        col_min = col * self.cell_width - self.margin_selection
        col_max = col * self.cell_width + self.margin_selection
        if event.x < col_min or event.x > col_max:
            return

        self.callback(Point(row, col))

    def update(self, board: Board):
        self.render_board(board)
        self.render_stones(board)

    def render_board(self, board: Board):
        window_width = (board.num_cols + 3) * self.cell_width
        window_height = (board.num_rows + 3) * self.cell_height

        self.window.geometry(f"{window_width}x{window_height}")

        canvas_width = (board.num_cols + 1) * self.cell_width
        canvas_height = (board.num_rows + 1) * self.cell_height

        if self.canvas:
            self.canvas.destroy()
        self.canvas = tk.Canvas(
            self.window, width=canvas_width, height=canvas_height, background="gray"
        )
        self.canvas.pack(padx=self.cell_width, pady=self.cell_height)
        self.canvas.bind("<Button-1>", self.selected)

        # 배경 전시
        self.canvas.create_image(0, 0, image=self.background, anchor=tk.NW)

        # 격자 전시
        for row in range(0, board.num_rows):
            self.canvas.create_line(
                self.cell_width,
                (row + 1) * self.cell_height,
                canvas_width - self.cell_width,
                (row + 1) * self.cell_height,
                width=2,
            )

        for col in range(0, board.num_cols):
            self.canvas.create_line(
                (col + 1) * self.cell_width,
                self.cell_height,
                (col + 1) * self.cell_width,
                canvas_height - self.cell_height,
                width=2,
            )

        # 인덱스 전시
        for col in range(0, board.num_cols):
            label = tk.Label(
                self.window, text=string.ascii_uppercase[col], font=(
                    "Arial", 12)
            )
            label.place(
                x=((col + 1) * self.cell_width + self.cell_width * 0.75),
                y=(self.cell_height * 0.5),
            )

        for row in range(0, board.num_rows):
            label = tk.Label(self.window, text=str(
                row + 1), font=("Arial", 12))
            label.place(
                x=(self.cell_width * 0.5),
                y=((row + 1) * self.cell_height + self.cell_height * 0.75),
            )

    def render_stones(self, board: Board):
        for item in board._grid:
            self.render_stone(board.get(item), item)

    def render_stone(self, player: Player, point: Point):
        x = point.col * self.cell_width
        y = point.row * self.cell_height
        if player == Player.white:
            self.canvas.create_image(x, y, image=self.shadow)
            self.canvas.create_image(x, y, image=self.white)
        else:
            self.canvas.create_image(x, y, image=self.shadow)
            self.canvas.create_image(x, y, image=self.black)
