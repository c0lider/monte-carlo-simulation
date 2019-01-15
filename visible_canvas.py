from tkinter import Canvas


class VisibleCanvas(Canvas):
    CIRCLE_COLOR = "#000000"
    RECTANGLE_COLOR = "#FFFFFF"
    BG_COLOR = "#161618"

    def __init__(self, window):
        super().__init__(window, width=420, height=420, borderwidth=0)
        self.rectangle = self.create_rectangle(0, 0, 420, 420, fill=self.RECTANGLE_COLOR, width=0)
        self.circle = self.create_oval(0, 0, 420, 420, fill=self.CIRCLE_COLOR, width=0)

    def draw_point(self, x, y, color):
        self.create_oval(x, y, x + 1, y + 1, width=0, fill=color)
