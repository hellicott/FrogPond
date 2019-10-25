from geometry_utilities import Circle

from shapely.geometry.point import Point


class Pond(object):

    radius = 10

    def __init__(self):
        self.circle = self.build_pond()

    def build_pond(self):
        centre = Point(self.radius, self.radius)
        return Circle(centre, self.radius)

    def get_frog_start_coords(self):
        return self.circle.get_points_on_circle()

    def lilly_pad_in_pond(self, pad_circle):
        return self.circle.contains_circle(pad_circle)
