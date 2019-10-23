import random

from geometry_utilities import Circle


class LillyPad(object):

    def __init__(self, position, min_radius, max_radius):
        radius = self._choose_radius(min_radius, max_radius)
        self.circle = Circle(position, radius)

    @staticmethod
    def _choose_radius(min_radius, max_radius):
        return random.uniform(min_radius, max_radius)

