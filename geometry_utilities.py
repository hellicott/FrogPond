from shapely.geometry import Point, Polygon


class GeoUtils(object):

    def circle(self, centre_point: Point, radius):
        circle = centre_point.buffer(radius)
        return circle

    def point_in_polygon(self, point: Point, poly: Polygon):
        return poly.contains(point)
