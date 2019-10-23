from unittest import TestCase
from shapely.geometry import Point

from geometry_utilities import Circle
from lilly_pad import LillyPad


class TestLillyPad(TestCase):

    def test_choose_radius_selects_radius_within_range(self):
        # arrange
        centre = Point(1, 1)
        pad = LillyPad(centre)
        # act
        radius = pad._choose_radius()
        # assert
        assert LillyPad.min_radius < radius < LillyPad.max_radius

    def test_lilly_pad_has_circle_attribute_of_expected_size(self):
        # arrange
        centre = Point(1, 1)
        # act
        pad = LillyPad(centre)
        # assert
        assert LillyPad.min_radius < pad.circle.radius < LillyPad.max_radius

    def test_lilly_pad_has_circle_attribute_in_expected_position(self):
        # arrange
        centre = Point(1, 1)
        # act
        pad = LillyPad(centre)
        # assert
        assert pad.circle.centre_point == centre

    def test_visited_returns_true_when_frog_visited(self):
        # arrange
        centre = Point(1, 1)
        pad = LillyPad(centre)
        frog_id = 2
        pad.visited_frogs = [frog_id]
        # act
        result = pad.visited_by(frog_id)
        # assert
        assert result is True

    def test_visited_returns_false_when_frog_not_visited(self):
        # arrange
        centre = Point(1, 1)
        pad = LillyPad(centre)
        frog_id = 2
        pad.visited_frogs = [frog_id+1]
        # act
        result = pad.visited_by(frog_id)
        # assert
        assert result is False

    def test_within_reach_returns_true_when_frog_can_reach_lilly_pad(self):
        # arrange
        frog_circle = Circle(Point(2, 2), 2)
        lilly_pad_centre = Point(1, 1)
        pad = LillyPad(lilly_pad_centre)
        # act
        result = pad.within_reach(frog_circle)
        # assert
        assert result is True

    def test_within_reach_returns_false_when_frog_cannot_reach_lilly_pad(self):
        # arrange
        frog_circle = Circle(Point(20, 20), 2)
        lilly_pad_centre = Point(1, 1)
        pad = LillyPad(lilly_pad_centre)
        # act
        result = pad.within_reach(frog_circle)
        # assert
        assert result is False