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

        # simulation "parameter"
        self.paused = True

        # window elements
        self.graph_frame = tkinter.Frame(self, bg=self.BG_COLOR)
        self.estimated_pi_label = tkinter.Label(self, text="", bg=self.BG_COLOR, fg=self.FG_COLOR)
        # add command to button
        self.start_pause_button = tkinter.Button(self, text="Play", width=20, bg=self.BG_COLOR, fg=self.FG_COLOR)
        self.save_to_file_button = tkinter.Button(self, text="Save to file", width=20, bg=self.BG_COLOR, fg=self.FG_COLOR)
        self.visible_canvas = VisibleCanvas(self)
        self.hidden_canvas = HiddenCanvas(self)

        # configure the widgets layout
        self.visible_canvas.grid(row=0, column=0, columnspan=4)
        self.start_pause_button.grid(row=1, column=0, padx=0, pady=10)
        self.save_to_file_button.grid(row=1, column=1, padx=0, pady=10)

        self.bind(sequence="<Escape>", func=self.close_window)
        self.bind(sequence="<space>", func=self.change_simulation_status)

        self.mainloop()

    def close_window(self, event):
        self.destroy()
        quit()

    def change_simulation_status(self, event):
        print("status changed")
        self.paused = not self.paused
        if not self.paused:
            self.run_simulation()

    def run_simulation(self):
        while True:
            self.update()
            if self.paused:
                break
            else:
                time.sleep(1)
                print(self.paused)


MonteCarloPiEstimation()