import numpy
import random
import tkinter

from hidden_canvas import HiddenCanvas
from visible_canvas import VisibleCanvas

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class MonteCarloPiEstimation(tkinter.Tk):
    PI = 3.1415
    _BG_COLOR = "#161618"
    _FG_COLOR = "#ee4d2e"
    _NUMPY_DOT_COLOR = "#7fc7ff"
    _RANDOM_DOT_COLOR = "#1cb992"
    _ACTUAL_PI_LINE_COLOR = "#888888"

    def __init__(self):
        # window configuration
        super().__init__()
        self.config(bg=self._BG_COLOR)
        self.title("Monte-Carlo Pi Estimation")
        self.iconbitmap("assets/pi.ico")

        # simulation "parameter"
        self.paused = True
        self.simulation_cycles = 0
        self._random_dots_in_circle = 0
        self._numpy_dots_in_circle = 0
        self._actual_pi_list = []
        self.random_estimated_pi_list = []
        self.numpy_estimated_pi_list = []

        # window elements
        # ---frames
        self._graph_frame = tkinter.Frame(self, bg=self._BG_COLOR)
        self._control_widget_frame = tkinter.Frame(self, bg=self._BG_COLOR)
        # ---canvas
        self._visible_canvas = VisibleCanvas(self)
        self._hidden_canvas = HiddenCanvas(self)
        # ---buttons
        self._start_pause_button = tkinter.Button(self._control_widget_frame, text="Start Simulation", width=20)
        self._start_pause_button.config(bg=self._BG_COLOR, fg=self._FG_COLOR, command=self.change_simulation_status)
        self._save_to_file_button = tkinter.Button(self._control_widget_frame, text="Save to file", width=20)
        self._save_to_file_button.config(bg=self._BG_COLOR, fg=self._FG_COLOR, command=self.save_plot_to_file)
        self._reset_button = tkinter.Button(self._control_widget_frame, text="Reset", width=20)
        self._reset_button.config(bg=self._BG_COLOR, fg=self._FG_COLOR, command=self.reset_simulation)
        # ---labels
        self._estimated_random_pi_label = tkinter.Label(self._control_widget_frame, text="")
        self._estimated_random_pi_label.config(width=25, anchor=tkinter.W, bg=self._BG_COLOR, fg=self._RANDOM_DOT_COLOR)
        self._estimated_numpy_pi_label = tkinter.Label(self._control_widget_frame, text="")
        self._estimated_numpy_pi_label.config(width=25, anchor=tkinter.W, bg=self._BG_COLOR, fg=self._NUMPY_DOT_COLOR)
        self.info_label = tkinter.Label(self._control_widget_frame, text="Welcome to the Monte-Carlo PI estimation!")
        self.info_label.config(width=50, bg=self._BG_COLOR, fg=self._FG_COLOR)
        # ---graph
        self._figure = Figure(figsize=(4, 4), dpi=100)
        self._subplot = self._figure.add_subplot(111)
        self._configure_graph()
        self._graph_canvas = FigureCanvasTkAgg(self._figure, master=self._graph_frame)
        self._graph_canvas.draw()
        self._draw_initial_graph()

        # con_figure the widgets' layout
        # ---left column
        self._visible_canvas.grid(row=0, column=0, padx=10, pady=10)
        # ---center column
        self.info_label.grid(row=0, column=0)
        self._control_widget_frame.grid(row=0, column=1)
        self._start_pause_button.grid(row=1, column=0, padx=10, pady=10)
        self._save_to_file_button.grid(row=2, column=0, padx=10, pady=10)
        self._reset_button.grid(row=3, column=0, padx=10, pady=10)
        self._estimated_random_pi_label.grid(row=4, column=0, padx=10, pady=10)
        self._estimated_numpy_pi_label.grid(row=5, column=0, padx=10, pady=10)
        # ---right column
        self._graph_frame.grid(row=0, column=2)
        self._graph_canvas.get_tk_widget().pack()

        # bind keys to functions
        self.bind(sequence="<Escape>", func=self.close_window)
        self.bind(sequence="<space>", func=self.change_simulation_status)
        self.bind(sequence="<s>", func=self.save_plot_to_file)
        self.bind(sequence="<r>", func=self.reset_simulation)

        self.mainloop()

    def _configure_graph(self):
        self._subplot.set_facecolor(self._BG_COLOR)
        self._figure.patch.set_facecolor(self._BG_COLOR)

        self._subplot.spines["bottom"].set_color(self._FG_COLOR)
        self._subplot.spines["left"].set_color(self._FG_COLOR)
        self._subplot.spines["right"].set_color(self._BG_COLOR)
        self._subplot.spines["top"].set_color(self._BG_COLOR)

        self._subplot.tick_params(axis="x", colors=self._FG_COLOR)
        self._subplot.tick_params(axis="y", colors=self._FG_COLOR)

    def _draw_initial_graph(self):
        x_values = list([x] for x in range(100))
        y_values = [self.PI] * 100
        self._subplot.plot(x_values, y_values, color=self._ACTUAL_PI_LINE_COLOR, lw=1)

    def close_window(self, *args):
        self.destroy()
        quit()

    def reset_simulation(self, *args):
        self._reset_params()
        self._reset_canvas()
        self._reset_widgets()
        self._subplot.cla()
        self._draw_initial_graph()
        self._graph_canvas.draw()

    def _reset_canvas(self):
        self._hidden_canvas.destroy()
        self._visible_canvas.destroy()

        self._hidden_canvas = HiddenCanvas(self)
        self._visible_canvas = VisibleCanvas(self)
        self._visible_canvas.grid(row=0, column=0, padx=10, pady=10)

    def _reset_params(self):
        self.paused = True
        self.simulation_cycles = 0

        self._random_dots_in_circle = 0
        self._numpy_dots_in_circle = 0
        self._actual_pi_list = []
        self.random_estimated_pi_list = []
        self.numpy_estimated_pi_list = []

    def _reset_widgets(self):
        self._start_pause_button.config(text="Start simulation")
        self._estimated_random_pi_label.config(text="")
        self._estimated_numpy_pi_label.config(text="")
        self.info_label.config(text="Simulation has been reset.")

    def change_simulation_status(self, *args):
        self.paused = not self.paused
        if not self.paused:
            self._start_pause_button.config(text="| |")
            self.run_simulation()
        else:
            self._start_pause_button.config(text="I>")

    def run_simulation(self):
        while True:
            self.update()
            if self.paused:
                break
            else:
                self.simulation_cycles += 1
                self.info_label.config(text="{} simulation cycles have been run.".format(self.simulation_cycles))
                self._actual_pi_list.append(self.PI)
                self._create_random_dot()
                self._create_numpy_random_dot()
                self._estimated_random_pi_label.config(text="Estimation(random):\t{:1.4f}".format(self._estimate_random_pi()))
                self._estimated_numpy_pi_label.config(text="Estimation(numpy):\t{:1.4f}".format(self._estimate_numpy_random_pi()))

                self.random_estimated_pi_list.append(self._estimate_random_pi())
                self.numpy_estimated_pi_list.append(self._estimate_numpy_random_pi())
                if self.simulation_cycles % 20 == 0:
                    self._subplot.cla()
                    self._update_graph()

    def _create_random_dot(self):
        random_x = random.randint(20, 4180)
        random_y = random.randint(20, 4180)
        self._visible_canvas._draw_point(random_x // 10, random_y // 10, self._RANDOM_DOT_COLOR)
        if self._hidden_canvas._get_closest(random_x, random_y) == (2, ):
            self._random_dots_in_circle += 1

    def _create_numpy_random_dot(self):
        random_x = numpy.random.randint(20, 4180)
        random_y = numpy.random.randint(20, 4180)
        self._visible_canvas._draw_point(random_x // 10, random_y // 10, self._NUMPY_DOT_COLOR)
        if self._hidden_canvas._get_closest(random_x, random_y) == (2, ):
            self._numpy_dots_in_circle += 1

    def _estimate_random_pi(self):
        return 4 * self._random_dots_in_circle / self.simulation_cycles

    def _estimate_numpy_random_pi(self):
        return 4 * self._numpy_dots_in_circle / self.simulation_cycles

    def _update_graph(self):
        x_values = list([x] for x in range(self.simulation_cycles))
        x_values_actual_pi = list([x] for x in range(len(self._actual_pi_list) + len(self._actual_pi_list) // 10))
        y_values_actual_pi = [self.PI] * (self.simulation_cycles + len(self._actual_pi_list) // 10)

        self._subplot.plot(x_values_actual_pi, y_values_actual_pi, color=self._ACTUAL_PI_LINE_COLOR, lw=1)
        self._subplot.plot(x_values, self.random_estimated_pi_list, color=self._RANDOM_DOT_COLOR, lw=1)
        self._subplot.plot(x_values, self.numpy_estimated_pi_list, color=self._NUMPY_DOT_COLOR, lw=1)

        self._graph_canvas.draw()

    def save_plot_to_file(self, *args):
        save_path = "pi_estimation.pdf"
        self._figure.savefig(save_path)
        self.info_label.config(text="Plot saved as '{}'.".format(save_path))


MonteCarloPiEstimation()
