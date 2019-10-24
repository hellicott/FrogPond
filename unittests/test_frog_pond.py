from unittest import TestCase

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
        frog = fp.create_frog(0)
        # assert
        assert type(frog) == Frog

    def test_lilly_pad_returns_lilly_pad_type(self):
        # arrange
        fp = FrogPond()
        # act
        pad = fp.create_lilly_pad()
        # assert
        assert type(pad) == LillyPad
