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

    def test_add_frog_adds_to_list_of_frogs(self):
        # arrange
        pond = Pond()
        # act
        pond.add_frog("frog")
        # assert
        assert "frog" in pond.frogs

    def test_add_lilly_pad_adds_to_list_of_lilly_pads(self):
        # arrange
        pond = Pond()
        # act
        pond.add_lilly_pad("lilly pad")
        # assert
        assert "lilly pad" in pond.lilly_pads
