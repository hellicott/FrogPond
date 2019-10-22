from shapely.geometry.point import Point


class GeoUtils(object):

    def circle(self, centre_point: Point, radius):
        circle = centre_point.buffer(radius)
        return circle
