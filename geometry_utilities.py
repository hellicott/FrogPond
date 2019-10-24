from shapely.geometry import Point


class Circle(object):

    def __init__(self, centre_point: Point, radius):
        self.centre_point = centre_point
        self.radius = radius

    def contains_point(self, other_point: Point):
        distance = self.centre_point.distance(other_point)
        return distance <= self.radius

    def intersects_circle(self, other_circle):
        distance = self.centre_point.distance(other_circle.centre_point)
        max_distance = self.radius + other_circle.radius
        return distance <= max_distance

    def get_points_on_circle(self):
        circle_polygon = self.centre_point.buffer(self.radius)
        circle_points = list(circle_polygon.exterior.coords)
        return circle_points

    def contains_circle(self, other_circle):
        bound_radius = self.radius - other_circle.radius
        bound_circle = Circle(self.centre_point, bound_radius)
        return bound_circle.contains_point(other_circle.centre_point)
