from geometry_utilities import Circle
from frog import Frog
from lilly_pad import LillyPad

from shapely.geometry.point import Point


class Pond(object):

    radius = 10

    def __init__(self):
        self.circle = self.build_pond()
        self.frogs = []
        self.lilly_pads = []

    def build_pond(self):
        centre = Point(self.radius, self.radius)
        return Circle(centre, self.radius)

    def add_frog(self, frog: Frog):
        self.frogs.append(frog)

    def add_lilly_pad(self, pad: LillyPad):
        self.lilly_pads.append(pad)
