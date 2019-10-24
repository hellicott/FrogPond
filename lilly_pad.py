import random

from geometry_utilities import Circle


class LillyPad(object):

    min_radius = 2
    max_radius = 5

    def __init__(self, position, radius, centre_pad=False):
        self.circle = Circle(position, radius)
        self.centre_pad = centre_pad
        self.currently_occupied = False
        self.visited_frogs = []

    def visited_by(self, frog_id):
        return frog_id in self.visited_frogs

    def within_reach(self, frog_circle):
        return self.circle.intersects_circle(frog_circle)

    def occupied(self):
        return self.currently_occupied

    def visit(self, frog_id):
        self.visited_frogs.append(frog_id)
        self.currently_occupied = True

    def leave(self):
        self.currently_occupied = False

