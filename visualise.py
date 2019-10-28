from geometry_utilities import Circle
from frog_pond import FrogPond

from shapely.geometry.point import Point
from tkinter import Tk, Canvas


class Visualise(object):

    def __init__(self, frog_pond: FrogPond):
        master = Tk()
        self.buffer = 50
        size = (frog_pond.get_pond_circle().radius + self.buffer) * 2
        self.frog_pond = frog_pond
        self.canvas = Canvas(master, width=size, height=size, bg="forestgreen")
        self._draw_board()
        self.canvas.pack()
        master.mainloop()

    def _draw_circle(self, circle: Circle, colour="red"):
        self.canvas.create_oval(circle.get_bounds(self.buffer, self.buffer), fill=colour)

    def _draw_circles(self, circle_list, colour="red"):
        for circle in circle_list:
            self._draw_circle(circle, colour)

    def _draw_board(self):
        self._draw_circle(self.frog_pond.get_pond_circle(), "blue")
        self._draw_circles(self.frog_pond.get_lilly_pad_circles(), "limegreen")
        self._draw_circle(self.frog_pond.get_centre_lilly_pad_circle(), "greenyellow")
        self._draw_circles(self.frog_pond.get_frog_circles(), "darkgreen")
