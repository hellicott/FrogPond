from unittest import TestCase, mock
from shapely.geometry.point import Point

from frog import Frog
from lilly_pad import LillyPad
from geometry_utilities import Circle


class TestFrog(TestCase):
    def test_get_range_circle_returns_circle_of_correct_size(self):
        # arrange
        position = Point(2, 2)
        max_jump = 3
        frog = Frog(position, 3, 0)
        # act
        range_circle = frog.get_range_circle()
        # assert
        assert range_circle.radius == max_jump

    def test_find_possible_lilly_pads_returns_list_of_lilly_pads_when_some_are_available(self):
        # arrange
        position = Point(2, 2)
        frog = Frog(position, 1, 0)
        pad = LillyPad(Point(2, 4), 1)
        # act
        possible_pads = frog._find_possible_lilly_pads([pad])
        # assert
        assert pad in possible_pads

    def test_find_possible_lilly_pads_returns_empty_list_when_none_are_available(self):
        # arrange
        position = Point(20, 20)
        frog = Frog(position, 1, 0)
        pad = LillyPad(Point(2, 4), 1)
        # act
        possible_pads = frog._find_possible_lilly_pads([pad])
        # assert
        assert len(possible_pads) == 0

    def test_find_possible_pads_returns_no_pads_if_nearby_pad_occupied(self):
        # arrange
        position = Point(2, 2)
        frog = Frog(position, 5, 0)
        pad = LillyPad(Point(2, 4), 1)
        pad.currently_occupied = True
        # act
        possible_pads = frog._find_possible_lilly_pads([pad])
        # assert
        assert len(possible_pads) == 0

    def test_move_to_lilly_pad_calls_lilly_pad_visit_method(self):
        # arrange
        mock_pad = mock.create_autospec(LillyPad)
        mock_pad.circle = Circle(Point(0, 0), 3)
        position = Point(2, 2)
        frog = Frog(position, 1, 0)
        # act
        frog._move_to_lilly_pad(mock_pad)
        # assert
        assert mock_pad.visit.called

    def test_move_to_lilly_pad_sets_frog_position_to_lilly_pad_position(self):
        # arrange
        mock_pad = mock.create_autospec(LillyPad)
        mock_pad.circle = Circle(Point(0, 0), 3)
        position = Point(2, 2)
        frog = Frog(position, 1, 0)
        # act
        frog._move_to_lilly_pad(mock_pad)
        # assert
        assert frog.position == Point(0, 0)

    def test_move_to_lilly_pad_calls_leave_on_current_lilly_pad(self):
        # arrange
        mock_current_pad = mock.create_autospec(LillyPad)
        mock_dest_pad = mock.create_autospec(LillyPad)
        mock_dest_pad.circle = Circle(Point(0, 0), 3)
        position = Point(2, 2)
        frog = Frog(position, 1, 0)
        frog.current_lilly_pad = mock_current_pad
        # act
        frog._move_to_lilly_pad(mock_dest_pad)
        # assert
        assert mock_current_pad.leave.called

    def test_move_to_lilly_pad_updates_frog_current_lilly_pad(self):
        # arrange
        mock_pad = mock.create_autospec(LillyPad)
        mock_pad.circle = Circle(Point(0, 0), 3)
        position = Point(2, 2)
        frog = Frog(position, 1, 0)
        # act
        frog._move_to_lilly_pad(mock_pad)
        # assert
        assert frog.current_lilly_pad == mock_pad

    def test_find_centre_lilly_pad_returns_lilly_pad_where_centre_is_true(self):
        # arrange
        frog = Frog(Point(2, 2), 3, 0)
        pad1 = mock.create_autospec(LillyPad)
        pad1.centre_pad = False
        pad2 = mock.create_autospec(LillyPad)
        pad2.centre_pad = True
        # act
        centre_pad = frog._find_centre_lilly_pad([pad1, pad2])
        # assert
        assert centre_pad == pad2
