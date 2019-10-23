from unittest import TestCase
from shapely.geometry.point import Point

from pond import Pond


class TestPond(TestCase):
    def test_pond_has_circle_in_expected_position(self):
        # arrange
        radius = 5
        # act
        pond = Pond(radius)
        # assert
        assert pond.circle.centre_point == Point(radius, radius)
