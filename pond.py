from geometry_utilities import Circle

from shapely.geometry.point import Point


class Pond(object):

    def __init__(self, radius):
        self.circle = self.build_pond(radius)
        self.frogs = []
        self.lilly_pads = []

    @staticmethod
    def build_pond(radius):
        centre = Point(radius, radius)
        return Circle(centre, radius)

    def create_frog(self):
        pass

    def create_lilly_pad(self):
        pass
