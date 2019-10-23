from geometry_utilities import Circle

from unittest import TestCase
from shapely.geometry import Point


class TestCircle(TestCase):
    def test_contains_point_returns_true_when_point_in_circle(self):
        # arrange
        centre = Point(3, 3)
        circle = Circle(centre, 2)
        point_in_circle = Point(2, 2)
        # act
        result = circle.contains_point(point_in_circle)
        # assert
        assert result is True

    def test_contains_point_returns_false_when_point_outside_circle(self):
        # arrange
        centre = Point(3, 3)
        circle = Circle(centre, 2)
        point_outside_circle = Point(0, 0)
        # act
        result = circle.contains_point(point_outside_circle)
        # assert
        assert result is False

    def test_contains_point_returns_true_when_point_on_boundary_of_circle(self):
        centre = Point(3, 3)
        circle = Circle(centre, 2)
        point_outside_circle = Point(3, 1)
        # act
        result = circle.contains_point(point_outside_circle)
        # assert
        assert result is True
