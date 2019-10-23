from shapely.geometry import Point


class Circle(object):

    def __init__(self, centre_point: Point, radius):
        self.centre_point = centre_point
        self.radius = radius

    def contains_point(self, other_point):
        distance = self.centre_point.distance(other_point)
        return distance <= self.radius
