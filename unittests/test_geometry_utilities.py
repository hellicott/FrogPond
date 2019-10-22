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

    def test_point_in_polygon_returns_true_when_point_inside_polygon(self):
        # arrange
        geo_utils = GeoUtils()
        poly = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
        point = Point(0.4, 0.4)
        # act
        result = geo_utils.point_in_polygon(point, poly)
        # assert
        assert result is True

    def test_point_in_polygon_returns_false_when_point_inside_polygon(self):
        # arrange
        geo_utils = GeoUtils()
        poly = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
        point = Point(0.4, 1.4)
        # act
        result = geo_utils.point_in_polygon(point, poly)
        # assert
        assert result is False
