from tkinter import Canvas


class HiddenCanvas(Canvas):
    def __init__(self, window):
        super().__init__(window, width=420, height=420)
        self.rectangle = self.create_rectangle(10, 10, 410, 410, fill="blue", width=0)
        self.circle = self.create_oval(10, 10, 410, 410, fill="red", width=0)

    def get_closest(self, x, y):
        return self.find_closest(x, y)

