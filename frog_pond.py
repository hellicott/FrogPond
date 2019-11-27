from geometry_utilities import Circle
from lilly_pad import LillyPad
from frog import Frog
from pond import Pond

from shapely.geometry.point import Point
import random


class FrogPond(object):

    def __init__(self, config):
        self.config = config
        self._set_constraints()
        self.pond = Pond()
        self.lilly_pads = []
        self.frogs = []
        self.create_all_frogs()
        self.create_all_lilly_pads()

    def _set_constraints(self):
        # Pond
        Pond.radius = self.config.pond_radius

        # Frog
        Frog.min_range = self.config.frog_min_jump_distance
        Frog.max_range = self.config.frog_max_jump_distance

        # LillyPad
        LillyPad.min_radius = 2/100 * self.config.pond_radius
        LillyPad.max_radius = self.config.lilly_pad_radius_max_percentage_of_pond_size/100 * self.config.pond_radius

    def _choose_frog_start_point(self):
        point = random.choice(self.pond.get_frog_start_coords())
        return Point(point[0], point[1])

    def _choose_lilly_pad_position(self, pad_radius):
        min_x, min_y, max_x, max_y = self.pond.circle.get_bounds()
        while True:
            x = random.uniform(min_x, max_x)
            y = random.uniform(min_y, max_y)
            pad = Circle(Point(x, y), pad_radius)
            if self.pond.lilly_pad_in_pond(pad) and not self._is_overlapping_current_lilly_pads(pad):
                return Point(x, y)

    def _is_overlapping_current_lilly_pads(self, circle):
        for lilly_pad in self.lilly_pads:
            if self._lilly_pads_overlap(circle, lilly_pad):
                return True
        return False

    @staticmethod
    def _lilly_pads_overlap(circle, lilly_pad):
        return circle.intersects_circle(lilly_pad.circle)

    @staticmethod
    def _choose_radius(min_radius, max_radius):
        return random.uniform(min_radius, max_radius)

    def _create_frog(self, num):
        position = self._choose_frog_start_point()
        radius = self._choose_radius(Frog.min_range, Frog.max_range)
        return Frog(position, radius, num)

    def _create_lilly_pad(self):
        radius = self._choose_radius(LillyPad.min_radius, LillyPad.max_radius)
        position = self._choose_lilly_pad_position(radius)
        return LillyPad(position, radius)

    def _create_centre_lilly_pad(self):
        position = self.pond.circle.centre_point
        radius = self._choose_radius(LillyPad.min_radius, LillyPad.max_radius)
        return LillyPad(position, radius, centre_pad=True)

    def create_all_frogs(self):
        for num in range(self.config.number_of_frogs_in_game):
            self.frogs.append(self._create_frog(num))

    def create_all_lilly_pads(self):
        self.lilly_pads.append(self._create_centre_lilly_pad())
        for num in range(self.config.number_of_lilly_pads_on_pond - 1):
            self.lilly_pads.append(self._create_lilly_pad())

    def get_frog_circles(self):
        return [frog.get_range_circle() for frog in self.frogs]

    def get_pond_circle(self):
        return self.pond.circle

    def get_centre_lilly_pad_circle(self):
        return self.lilly_pads[0].circle

    def get_lilly_pad_circles(self):
        return [pad.circle for pad in self.lilly_pads]
