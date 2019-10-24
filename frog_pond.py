from lilly_pad import LillyPad
from frog import Frog
from pond import Pond
import config

from shapely.geometry.point import Point


class FrogPond(object):

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

    def choose_frog_start_point(self):
        return Point(0, 0)

    def choose_lilly_pad_position(self):
        return self.choose_frog_start_point()

    def create_frog(self, num):
        position = self.choose_frog_start_point()
        return Frog(position, num)

    def create_lilly_pad(self):
        position = self.choose_lilly_pad_position()
        return LillyPad(position)
