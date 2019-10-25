from geometry_utilities import Circle
from shapely.geometry.point import Point

from tkinter import Tk, Canvas


class Visualise(object):

    def __init__(self, size):
        master = Tk()
        self.canvas = Canvas(master, width=size, height=size)
        self.draw_circle(Circle(Point(100, 100), 25))
        self.canvas.pack()
        master.mainloop()

    def draw_circle(self, circle: Circle, colour="red"):
        self.canvas.create_oval(circle.get_bounds(), fill=colour)


Visualise(300)