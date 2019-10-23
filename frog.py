from geometry_utilities import Circle
from shapely.geometry.point import Point


class Frog(object):

    def __init__(self, position: Point, max_jump):
        self.position = position
        self.max_jump = max_jump
        self.range_circle = self._get_range()

    def _get_range(self):
        return Circle(self.position, self.max_jump)
