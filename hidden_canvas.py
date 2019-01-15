from tkinter import Canvas


class HiddenCanvas(Canvas):
    def __init__(self, window):
        super().__init__(window, width=4200, height=4200)
        self.rectangle = self.create_rectangle(20, 20, 4180, 4180, fill="blue", width=0)
        self.circle = self.create_oval(20, 20, 4180, 4180, fill="red", width=0)

    def get_closest(self, x, y):
        return self.find_closest(x, y)

