from frog import Frog
from lilly_pad import LillyPad
from pond import Pond
import config


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
