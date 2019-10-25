from unittest import TestCase
from shapely.geometry.point import Point

from pond import Pond


class TestPond(TestCase):
    def test_pond_has_circle_in_expected_position(self):
        # arrange
        radius = 5
        Pond.radius = radius
        # act
        pond = Pond()
        # assert
        assert pond.circle.centre_point == Point(radius, radius)

    def test_get_frog_start_coords_returns_list_of_coordinates(self):
        # arrange
        pond = Pond()
        # act
        coord_list = pond.get_frog_start_coords()
        # assert
        assert type(coord_list) == list \
            and type(coord_list[0][0]) == float
