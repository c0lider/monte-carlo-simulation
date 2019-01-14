from visible_canvas import VisibleCanvas
from hidden_canvas import HiddenCanvas

import tkinter
import time


class MonteCarloPiEstimation(tkinter.Tk):
    PI = 3.1415
    BG_COLOR = "#161618"
    FG_COLOR = "#42f442"

    def __init__(self):
        # window configuration
        super().__init__()
        self.config(bg=self.BG_COLOR)
        self.title("Monte-Carlo Pi Estimation")
        self.iconbitmap("assets/pi.ico")

        # window elements
        self.graph_frame = tkinter.Frame(self, bg=self.BG_COLOR)
        self.estimated_pi_label = tkinter.Label(self, text="", bg=self.BG_COLOR, fg=self.FG_COLOR)
        # add command to button
        self.start_pause_button = tkinter.Button(self, text="Play", width=20, bg=self.BG_COLOR, fg=self.FG_COLOR)
        self.save_to_file_button = tkinter.Button(self, text="Save to file", width=20, bg=self.BG_COLOR, fg=self.FG_COLOR)
        self.visible_canvas = VisibleCanvas(self)
        self.hidden_canvas = HiddenCanvas(self)

        self.mainloop()


MonteCarloPiEstimation()