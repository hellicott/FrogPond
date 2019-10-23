import random

from geometry_utilities import Circle


class LillyPad(object):

    min_radius = 2
    max_radius = 5

    def __init__(self, position):
        radius = self._choose_radius()
        self.circle = Circle(position, radius)
        self.current_frog_id = None
        self.visited_frogs = []

    def _choose_radius(self):
        return random.uniform(self.min_radius, self.max_radius)

    def visited_by(self, frog_id):
        return frog_id in self.visited_frogs

    def within_reach(self, frog_circle):
        return self.circle.intersects_circle(frog_circle)

    def occupied(self):
        return self.current_frog_id is not None
