from hidden_canvas import HiddenCanvas
from visible_canvas import VisibleCanvas

from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import time
import matplotlib
import numpy
import random

matplotlib.use("TkAgg")


class MonteCarloPiEstimation:
    PI = 3.1415
    BG_COLOR = "#161618"
    FG_COLOR = "#42f442"

    def __init__(self):
        # -object variables
        self.simulation_paused = True
        self.circle_hits = 0
        self.total_amount = 0
        self.hits = []
        self.actual_pi = [self.PI] * 100

        # window settings
        self.window = Tk()
        self.window.config(bg=self.BG_COLOR)
        self.window.title("Monte Carlo Pi Estimation")
        self.window.iconbitmap("assets/pi.ico")
        self.hidden_canvas = HiddenCanvas(self.window)
        self.visible_canvas = VisibleCanvas(self.window)
        self.graph_frame = Frame(self.window, bg=self.BG_COLOR)
        self.pi_label = Label(self.window, text="", bg=self.BG_COLOR, fg=self.FG_COLOR)

        self.show_initial_graph()

        Button(self.window, text="||", width=20, command=self.change_simulation_status(), bg=self.BG_COLOR,
               fg=self.FG_COLOR).grid(row=1, column=0, padx=5, pady=5)
        self.pi_label.grid(row=1, column=4)
        self.graph_frame.grid(row=0, column=4)
        Button(self.window, text="save to file", width=20, command=self.save_plot, bg=self.BG_COLOR,
               fg=self.FG_COLOR).grid(row=1, column=1, padx=5, pady=5)

        self.window.bind(sequence="<space>", func=self.change_simulation_status())
        self.window.mainloop()

    def change_simulation_status(self):
        # make sure the interrupt variable doesn't stop the simulation
        if self.simulation_paused:
            self.simulation_paused = False
            self.run_simulation()
        else:
            self.simulation_paused = True

    def run_simulation(self, *args, amount=10000, offset=0.001):
        self.x_values = []
        self.y_values = []
        for i in range(amount):
            self.create_numpy_random_dot()
            time.sleep(offset)
            self.pi_label.config(text="pi estimation: {:1.4f}".format(self.estimate_pi()))
            self.window.update_idletasks()
            self.window.update()
            self.x_values.append(i)
            self.y_values.append(self.estimate_pi())
            if i % 10 == 0:
                self.a.cla()
                self.update_graph()

    def show_initial_graph(self):
        self.f = Figure(figsize=(4, 4), dpi=100)
        self.a = self.f.add_subplot(111)

        self.a.set_facecolor(self.BG_COLOR)
        self.a.spines["bottom"].set_color(self.FG_COLOR)
        self.a.spines["left"].set_color(self.FG_COLOR)
        self.a.spines["right"].set_color(self.BG_COLOR)
        self.a.spines["top"].set_color(self.BG_COLOR)

        self.a.tick_params(axis="x", colors=self.FG_COLOR)
        self.a.tick_params(axis="y", colors=self.FG_COLOR)

        self.f.patch.set_facecolor(self.BG_COLOR)

        self.canvas = FigureCanvasTkAgg(self.f, master=self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def update_graph(self):
        self.actual_pi_x = []
        for _ in range(10):
            self.actual_pi.append(self.PI)

        for x in range(len(self.actual_pi)):
            self.actual_pi_x.append(int(x))
        self.a.plot(self.actual_pi_x, self.actual_pi, "r-", self.x_values, self.y_values, "w-")

        self.canvas.draw()

    def save_plot(self):
        self.f.savefig('C:\\Users\\ollis\\Desktop\\foo.pdf')

    def create_random_dot(self):
        x = random.randint(10, 410)
        y = random.randint(10, 410)
        self.total_amount += 1
        self.visible_canvas.draw_point(x, y)
        if self.hidden_canvas.get_closest(x, y) == (2,):
            self.circle_hits += 1

    def create_numpy_random_dot(self):
        x = numpy.random.randint(10, 410)
        y = numpy.random.randint(10, 410)
        self.total_amount += 1
        self.visible_canvas.draw_point(x, y)
        if self.hidden_canvas.get_closest(x, y) == (2,):
            self.circle_hits += 1

    def estimate_pi(self):
        return 4 * self.circle_hits / self.total_amount




test = MonteCarloPiEstimation()