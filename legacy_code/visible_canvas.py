from tkinter import Canvas


class VisibleCanvas(Canvas):
    CIRCLE_COLOR = ""
    RECTANGLE_COLOR = ""
    BG_COLOR = "#161618"

    # TODO make the size of the canvas changeable
    def __init__(self, window):
        super().__init__(window, width=420, height=420, bg=self.BG_COLOR)
        # bg = self.canvas.create_rectangle(0, 0, 420, 420, fill=self.BG_COLOR)
        self.rectangle = self.create_rectangle(10, 10, 410, 410, fill="blue", width=0)
        self.circle = self.create_oval(10, 10, 410, 410, fill="red", width=0)

    def draw_point(self, x, y):
        self.create_oval(x - 1, y - 1, x + 1, y + 1, width=0, fill="black")
