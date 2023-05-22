import unittest

import tkinter as tk
from tkinter import messagebox


class TkinterTest(unittest.TestCase):
    # @unittest.skip("test")
    def test_message_box(self):
        root = tk.Tk()
        root.geometry("300x200")

        messagebox.showinfo("showinfo", "info")

        root.mainloop()


if __name__ == '__main__':
    unittest.main()
