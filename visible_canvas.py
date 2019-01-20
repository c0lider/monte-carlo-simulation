from tkinter import Canvas


class VisibleCanvas(Canvas):
    CIRCLE_COLOR = "#000000"
    RECTANGLE_COLOR = "#888888"
    BG_COLOR = "#888888"

    def __init__(self, window):
        super().__init__(window, width=420, height=420, borderwidth=0, bg=self.BG_COLOR)
        self._rectangle = self.create_rectangle(0, 0, 420, 420, fill=self.RECTANGLE_COLOR, width=0)
        self._circle = self.create_oval(2, 2, 420, 420, fill=self.CIRCLE_COLOR, width=0)

    def _draw_point(self, x, y, color):
        self.create_oval(x, y, x + 1, y + 1, width=0, fill=color)
