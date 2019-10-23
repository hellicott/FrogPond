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
