from geometry_utilities import GeoUtils

from unittest import TestCase
from shapely.geometry import Point, Polygon


class TestGeoUtils(TestCase):
    def test_circle_method_returns_polygon_around_central_point(self):
        # arrange
        geo_utils = GeoUtils()
        centre_point = Point(2, 2)
        radius = 1
        # act
        circle_to_test = geo_utils.circle(centre_point, radius)
        # assert
        assert circle_to_test.centroid == centre_point