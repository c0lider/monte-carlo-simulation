from tkinter import Canvas

class HiddenCanvas:
    def __init__(self, window):
        self.canvas = Canvas(window, width=420, height=420)
        self.rectangle = self.canvas.create_rectangle(10, 10, 410, 410, fill="blue", width=0)
        self.circle = self.canvas.create_oval(10, 10, 410, 410, fill="red", width=0)

    def get_closest(self, x, y):
        return self.canvas.find_closest(x, y)

