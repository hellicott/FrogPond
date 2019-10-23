from unittest import TestCase
from shapely.geometry import Point, MultiPoint

from lilly_pad import LillyPad


class TestLillyPad(TestCase):

    def test_choose_radius_selects_radius_within_range(self):
        # arrange
        centre = Point(1, 1)
        max_rad = 5
        min_rad = 2
        pad = LillyPad(centre, min_rad, max_rad)
        # act
        radius = pad._choose_radius(min_rad, max_rad)
        # assert
        assert min_rad < radius < max_rad

    def test_calculate_polygon_returns_correct_size_polygon(self):
        # arrange
        centre = Point(1, 1)
        max_rad = 5
        min_rad = 2
        pad = LillyPad(centre, min_rad, max_rad)
        # act
        poly = pad._create_polygon(centre, 3)
        # assert
        poly_point = MultiPoint(poly.exterior.coords)[0]
        assert 2.9 < centre.distance(poly_point) < 3.1
