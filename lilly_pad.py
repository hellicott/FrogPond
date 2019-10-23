import random

from geometry_utilities import Circle


class LillyPad(object):

    min_radius = 2
    max_radius = 5

    def __init__(self, position):
        self.radius = self._choose_radius()
        self.circle = Circle(position, self.radius)
        self.centre = position
        self.currently_occupied = False
        self.visited_frogs = []

    def _choose_radius(self):
        return random.uniform(self.min_radius, self.max_radius)

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

