from unittest import TestCase, mock
from shapely.geometry.point import Point

from frog import Frog
from lilly_pad import LillyPad


class TestFrog(TestCase):
    def test_get_range_circle_returns_circle_of_correct_size(self):
        # arrange
        position = Point(2, 2)
        frog = Frog(position, 0)
        # act
        range_circle = frog._get_range_circle()
        # assert
        assert frog.min_range < range_circle.radius < frog.max_range

    def test_find_possible_lilly_pads_returns_list_of_lilly_pads_when_some_are_available(self):
        # arrange
        position = Point(2, 2)
        frog = Frog(position, 0)
        pad = LillyPad(Point(2, 4))
        # act
        possible_pads = frog._find_possible_lilly_pads([pad])
        # assert
        assert pad in possible_pads

    def test_find_possible_lilly_pads_returns_empty_list_when_none_are_available(self):
        # arrange
        position = Point(20, 20)
        frog = Frog(position, 0)
        pad = LillyPad(Point(2, 4))
        # act
        possible_pads = frog._find_possible_lilly_pads([pad])
        # assert
        assert len(possible_pads) == 0

    def test_move_to_lilly_pad_calls_lilly_pad_visit_method(self):
        # arrange
        mock_pad = mock.create_autospec(LillyPad)
        mock_pad.centre = 2
        position = Point(2, 2)
        frog = Frog(position, 0)
        # act
        frog._move_to_lilly_pad(mock_pad)
        # assert
        assert mock_pad.visit.called

    def test_move_to_lilly_pad_sets_frog_position_to_lilly_pad_position(self):
        # arrange
        mock_pad = mock.create_autospec(LillyPad)
        mock_pad.centre = 2
        position = Point(2, 2)
        frog = Frog(position, 0)
        # act
        frog._move_to_lilly_pad(mock_pad)
        # assert
        assert frog.position == 2

    def test_move_to_lilly_pad_calls_leave_on_current_lilly_pad(self):
        # arrange
        mock_current_pad = mock.create_autospec(LillyPad)
        mock_dest_pad = mock.create_autospec(LillyPad)
        mock_dest_pad.centre = 2
        position = Point(2, 2)
        frog = Frog(position, 0)
        frog.current_lilly_pad = mock_current_pad
        # act
        frog._move_to_lilly_pad(mock_dest_pad)
        # assert
        assert mock_current_pad.leave.called

    def test_move_to_lilly_pad_updates_frog_current_lilly_pad(self):
        # arrange
        mock_pad = mock.create_autospec(LillyPad)
        mock_pad.centre = 2
        position = Point(2, 2)
        frog = Frog(position, 0)
        # act
        frog._move_to_lilly_pad(mock_pad)
        # assert
        assert frog.current_lilly_pad == mock_pad
