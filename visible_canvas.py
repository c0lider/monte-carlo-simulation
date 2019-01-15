from tkinter import Canvas


class VisibleCanvas(Canvas):
    CIRCLE_COLOR = "#000000"
    RECTANGLE_COLOR = "#FFFFFF"
    BG_COLOR = "#161618"

    # TODO make the size of the canvas changeable
    def __init__(self, window):
        super().__init__(window, width=420, height=420, bg=self.BG_COLOR)
        self.rectangle = self.create_rectangle(10, 10, 410, 410, fill=self.RECTANGLE_COLOR, width=0)
        self.circle = self.create_oval(10, 10, 410, 410, fill=self.CIRCLE_COLOR, width=0)

    def draw_point(self, x, y, color):
        self.create_oval(x - 1, y - 1, x + 1, y + 1, width=0, fill=color)
