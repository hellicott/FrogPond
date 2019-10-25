from unittest import TestCase
from shapely.geometry.point import Point

from geometry_utilities import Circle
from frog_pond import FrogPond
from lilly_pad import LillyPad
from frog import Frog
from pond import Pond
import config


class TestFrogPond(TestCase):

    def test_set_constraints_sets_pond_radius(self):
        # arrange
        config.pond_radius = 10
        fp = FrogPond()
        # act
        fp._set_constraints()
        # assert
        assert Pond.radius == 10

    def test_set_constraints_sets_frog_min_range(self):
        # arrange
        config.frog_min_jump_distance = 2
        fp = FrogPond()
        # act
        fp._set_constraints()
        # assert
        assert Frog.min_range == 2

    def test_set_constraints_sets_frog_max_range(self):
        # arrange
        config.frog_max_jump_distance = 7
        fp = FrogPond()
        # act
        fp._set_constraints()
        # assert
        assert Frog.max_range == 7

    def test_set_constraints_sets_lilly_pad_min_radius(self):
        # arrange
        min_percent = 2
        config.pond_radius = 100
        fp = FrogPond()
        # act
        fp._set_constraints()
        # assert
        assert LillyPad.min_radius == min_percent

    def test_set_constraints_sets_lilly_pad_max_radius(self):
        # arrange
        config.lilly_pad_radius_max_percentage_of_pond_size = 10
        config.pond_radius = 100
        fp = FrogPond()
        # act
        fp._set_constraints()
        # assert
        assert LillyPad.max_radius == 10

    def test_create_frog_returns_frog_type(self):
        # arrange
        fp = FrogPond()
        # act
        frog = fp._create_frog(0)
        # assert
        assert type(frog) == Frog

    def test_create_lilly_pad_returns_lilly_pad_type(self):
        # arrange
        fp = FrogPond()
        # act
        pad = fp._create_lilly_pad()
        # assert
        assert type(pad) == LillyPad

    def test_choose_frog_start_point_returns_point(self):
        # arrange
        fp = FrogPond()
        # act
        point = fp._choose_frog_start_point()
        # assert
        assert type(point) == Point

    def test_choose_lilly_pad_position_returns_position_which_does_not_overlap_other_pads(self):
        # arrange
        fp = FrogPond()
        centre_pad = fp._create_centre_lilly_pad()
        pad1 = fp._create_lilly_pad()
        fp.lilly_pads = [centre_pad, pad1]
        pad2_radius = 3
        # act
        pad2_position = fp._choose_lilly_pad_position(pad2_radius)
        # assert
        pad2 = Circle(pad2_position, pad2_radius)
        assert not pad2.intersects_circle(pad1.circle) \
            and not pad2.intersects_circle(centre_pad.circle)

    def test_is_overlapping_current_lilly_pads_returns_true_when_overlapping(self):
        # arrange
        fp = FrogPond()
        centre_pad = fp._create_centre_lilly_pad()
        pad1 = fp._create_lilly_pad()
        fp.lilly_pads = [centre_pad, pad1]
        overlapping_pad = Circle(pad1.circle.centre_point, 3)
        # act
        result = fp._is_overlapping_current_lilly_pads(overlapping_pad)
        # assert
        assert result is True

    def test_is_overlapping_current_lilly_pads_returns_false_when_not_overlapping(self):
        # arrange
        fp = FrogPond()
        centre_pad = fp._create_centre_lilly_pad()
        pad1 = fp._create_lilly_pad()
        fp.lilly_pads = [centre_pad, pad1]
        overlapping_pad = Circle(Point(10000, 100000), 1)
        # act
        result = fp._is_overlapping_current_lilly_pads(overlapping_pad)
        # assert
        assert result is False

    def test_create_centre_lilly_pad_returns_lillypad_in_centre_of_pond(self):
        # arrange
        fp = FrogPond()
        # act
        centre_pad = fp._create_centre_lilly_pad()
        # assert
        assert centre_pad.circle.centre_point == fp.pond.circle.centre_point
