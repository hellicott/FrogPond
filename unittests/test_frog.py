from unittest import TestCase
from shapely.geometry.point import Point

from frog import Frog
from lilly_pad import LillyPad


class TestFrog(TestCase):
    def test_get_range_returns_circle_of_correct_size(self):
        # arrange
        position = Point(2, 2)
        max_jump = 1
        frog = Frog(position, max_jump, 0)
        # act
        range_circle = frog._get_range()
        # assert
        assert range_circle.radius == max_jump

    def test_find_possible_lilly_pads_returns_list_of_lilly_pads_when_some_are_available(self):
        # arrange
        position = Point(2, 2)
        max_jump = 3
        frog = Frog(position, max_jump, 0)
        pad = LillyPad(Point(2, 4))
        # act
        possible_pads = frog.find_possible_lilly_pads([pad])
        # assert
        assert pad in possible_pads