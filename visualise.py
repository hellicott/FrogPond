from geometry_utilities import Circle

from tkinter import Tk, Canvas


class Visualise(object):

    def __init__(self, size):
        master = Tk()
        self.canvas = Canvas(master, width=size, height=size)
        self.canvas.pack()
        master.mainloop()


    def draw_circle(self, circle: Circle):
        self.canvas.create_oval(circle.)


Visualise(300)