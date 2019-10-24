from lilly_pad import LillyPad
from frog import Frog
from pond import Pond
import config

from shapely.geometry.point import Point
import random


class FrogPond(object):

    def __init__(self):
        self._set_constraints()
        self.pond = Pond()

    @staticmethod
    def _set_constraints():
        # Pond
        Pond.radius = config.pond_radius

        # Frog
        Frog.min_range = config.frog_min_jump_distance
        Frog.max_range = config.frog_max_jump_distance

        # LillyPad
        LillyPad.min_radius = 2/100 * config.pond_radius
        LillyPad.max_radius = config.lilly_pad_radius_max_percentage_of_pond_size/100 * config.pond_radius

    def _choose_frog_start_point(self):
        point = random.choice(self.pond.get_frog_start_points())
        return Point(point[0], point[1])

    def _choose_lilly_pad_position(self):
        return False

    @staticmethod
    def _choose_radius(min_radius, max_radius):
        return random.uniform(min_radius, max_radius)

    def create_frog(self, num):
        position = self._choose_frog_start_point()
        radius = self._choose_radius(Frog.min_range, Frog.max_range)
        return Frog(position, radius, num)

    def create_lilly_pad(self):
        position = self._choose_lilly_pad_position()
        radius = self._choose_radius(LillyPad.min_radius, LillyPad.max_radius)
        return LillyPad(position, radius)
