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
        # arrange
        centre = Point(3, 3)
        circle = Circle(centre, 2)
        point_outside_circle = Point(3, 1)
        # act
        result = circle.contains_point(point_outside_circle)
        # assert
        assert result is True

    def test_intersects_circle_returns_true_when_circles_overlap(self):
        # arrange
        circle1 = Circle(Point(3, 3), 1)
        circle2 = Circle(Point(2, 1), 2)
        # act
        result = circle1.intersects_circle(circle2)
        # assert
        assert result is True

    def test_intersects_circle_returns_false_when_circles_do_not_overlap(self):
        # arrange
        circle1 = Circle(Point(10, 10), 1)
        circle2 = Circle(Point(2, 1), 2)
        # act
        result = circle1.intersects_circle(circle2)
        # assert
        assert result is False

    def test_get_points_on_circle_returns_list_of_points(self):
        # arrange
        circle = Circle(Point(3, 3), 2)
        # act
        point_list = circle.get_points_on_circle()
        # assert
        assert type(point_list) == list \
            and type(point_list[0][0]) == float

    def test_contains_circle_returns_true_when_circle_contained(self):
        # arrange
        circle_outside = Circle(Point(5, 5), 5)
        circle_inside = Circle(Point(7, 4), 1)
        # act
        result = circle_outside.contains_circle(circle_inside)
        # assert
        assert result is True

    def test_contains_circle_returns_false_when_circle_not_contained(self):
        # arrange
        circle1 = Circle(Point(10, 10), 2)
        circle2 = Circle(Point(3, 10), 2)
        # act
        result = circle1.contains_circle(circle2)
        # assert
        assert result is False

    def test_get_bounds(self):
        # arrange
        circle = Circle(Point(3, 3), 1)
        # act
        bounds = circle.get_bounds()
        # assert
        assert bounds == (2, 2, 4, 4)
