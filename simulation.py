from visible_canvas import VisibleCanvas
from hidden_canvas import HiddenCanvas

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import tkinter
import time
import random
import numpy


class MonteCarloPiEstimation(tkinter.Tk):
    PI = 3.1415
    BG_COLOR = "#161618"
    FG_COLOR = "#42f442"
    NUMPY_DOT_COLOR = "#FF0000"
    RANDOM_DOT_COLOR = "#0000FF"

    def __init__(self):
        # window configuration
        super().__init__()
        self.config(bg=self.BG_COLOR)
        self.title("Monte-Carlo Pi Estimation")
        self.iconbitmap("assets/pi.ico")

        # simulation "parameter"
        self.paused = True
        self.simulation_cycles = 0
        self.random_dots_in_circle = 0
        self.numpy_dots_in_circle = 0
        self.actual_pi_list = []
        self.random_estimated_pi_list = []
        self.numpy_estimated_pi_list = []

        # window elements
        self.graph_frame = tkinter.Frame(self, bg=self.BG_COLOR)
        self.control_widget_frame = tkinter.Frame(self, bg=self.BG_COLOR)
        self.estimated_random_pi_label = tkinter.Label(self.control_widget_frame, text="Pi estimation(random):", bg=self.BG_COLOR, fg=self.FG_COLOR)
        self.estimated_numpy_pi_label = tkinter.Label(self.control_widget_frame, text="Pi estimation(numpy):", bg=self.BG_COLOR, fg=self.FG_COLOR)
        self.start_pause_button = tkinter.Button(self.control_widget_frame, text="Play", width=20, bg=self.BG_COLOR, fg=self.FG_COLOR, command=self.change_simulation_status)
        self.save_to_file_button = tkinter.Button(self.control_widget_frame, text="Save to file", width=20, bg=self.BG_COLOR, fg=self.FG_COLOR)
        self.visible_canvas = VisibleCanvas(self)
        self.hidden_canvas = HiddenCanvas(self)
        self.figure = Figure(figsize=(4, 4), dpi=100)
        self.subplot = self.figure.add_subplot(111)

        self.configure_graph()

        self.graph_canvas = FigureCanvasTkAgg(self.figure, master=self.graph_frame)
        self.graph_canvas.draw()
        self.graph_canvas.get_tk_widget().pack()

        # configure the widgets layout
        self.visible_canvas.grid(row=0, column=0)
        self.control_widget_frame.grid(row=0, column=1)
        self.graph_frame.grid(row=0, column=2)

        self.start_pause_button.grid(row=0, column=0, padx=10, pady=10)
        self.save_to_file_button.grid(row=1, column=0, padx=10, pady=10)
        self.estimated_random_pi_label.grid(row=2, column=0, padx=10, pady=10)
        self.estimated_numpy_pi_label.grid(row=3, column=0, padx=10, pady=10)

        self.bind(sequence="<Escape>", func=self.close_window)
        self.bind(sequence="<space>", func=self.change_simulation_status)

        self.mainloop()

    def configure_graph(self):
        self.subplot.set_facecolor(self.BG_COLOR)
        self.figure.patch.set_facecolor(self.BG_COLOR)

        self.subplot.spines["bottom"].set_color(self.FG_COLOR)
        self.subplot.spines["left"].set_color(self.FG_COLOR)
        self.subplot.spines["right"].set_color(self.BG_COLOR)
        self.subplot.spines["top"].set_color(self.BG_COLOR)

        self.subplot.tick_params(axis="x", colors=self.FG_COLOR)
        self.subplot.tick_params(axis="y", colors=self.FG_COLOR)

    def close_window(self, *event):
        self.destroy()
        quit()

    def change_simulation_status(self, *event):
        self.paused = not self.paused
        if not self.paused:
            self.start_pause_button.config(text="| |")
            self.run_simulation()
        else:
            self.start_pause_button.config(text="I>")

    def run_simulation(self):
        while True:
            self.update()
            if self.paused:
                break
            else:
                self.simulation_cycles += 1
                self.actual_pi_list.append(self.PI)
                self.create_random_dot()
                self.create_numpy_random_dot()
                self.estimated_random_pi_label.config(text="Pi estimation(random): {:1.4f}".format(self.estimate_random_pi()))
                self.estimated_numpy_pi_label.config(text="Pi estimation(numpy): {:1.4f}".format(self.estimate_numpy_random_pi()))

                self.random_estimated_pi_list.append(self.estimate_random_pi())
                self.numpy_estimated_pi_list.append(self.estimate_numpy_random_pi())
                if self.simulation_cycles % 20 == 0:
                    self.subplot.cla()
                    self.update_graph()

    def create_random_dot(self):
        random_x = random.randint(10, 410)
        random_y = random.randint(10, 410)
        self.visible_canvas.draw_point(random_x, random_y, self.RANDOM_DOT_COLOR)
        if self.hidden_canvas.get_closest(random_x, random_y) == (2, ):
            self.random_dots_in_circle += 1

    def create_numpy_random_dot(self):
        random_x = numpy.random.randint(10, 410)
        random_y = numpy.random.randint(10, 410)
        self.visible_canvas.draw_point(random_x, random_y, self.NUMPY_DOT_COLOR)
        if self.hidden_canvas.get_closest(random_x, random_y) == (2, ):
            self.numpy_dots_in_circle += 1

    def estimate_random_pi(self):
        return 4 * self.random_dots_in_circle / self.simulation_cycles

    def estimate_numpy_random_pi(self):
        return 4 * self.numpy_dots_in_circle / self.simulation_cycles

    def update_graph(self):
        self.subplot.plot(list([x] for x in range(len(self.actual_pi_list) + 100)), [self.PI] * (self.simulation_cycles + 100), "w-")
        self.subplot.plot(list([x] for x in range(self.simulation_cycles)), self.random_estimated_pi_list, color=self.RANDOM_DOT_COLOR, lw=2)
        self.subplot.plot(list([x] for x in range(self.simulation_cycles)), self.numpy_estimated_pi_list, color=self.NUMPY_DOT_COLOR, lw=2)
        self.graph_canvas.draw()


MonteCarloPiEstimation()