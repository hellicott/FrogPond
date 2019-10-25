import random

from geometry_utilities import Circle
from shapely.geometry.point import Point


class Frog(object):

    min_range = 2
    max_range = 4

    def __init__(self, position: Point, radius, frog_id):
        self.position = position
        self.max_jump = radius
        self.frog_id = frog_id
        self.playing = True
        self.current_lilly_pad = None

    def get_range_circle(self):
        return Circle(self.position, self.max_jump)

    def _find_possible_lilly_pads(self, lilly_pad_list):
        possible_lilly_pads = []
        for lilly_pad in lilly_pad_list:
            if not lilly_pad.occupied() \
                    and not lilly_pad.visited_by(self.frog_id) \
                    and lilly_pad.within_reach(self.get_range_circle()):
                possible_lilly_pads.append(lilly_pad)
        return possible_lilly_pads

    def _move_to_lilly_pad(self, destination_lilly_pad):
        if self.current_lilly_pad is not None:
            self.current_lilly_pad.leave()
        self.position = destination_lilly_pad.centre
        destination_lilly_pad.visit(self.frog_id)
        self.current_lilly_pad = destination_lilly_pad

    @staticmethod
    def _find_centre_lilly_pad(lilly_pad_list):
        for lilly_pad in lilly_pad_list:
            if lilly_pad.centre_pad:
                return lilly_pad
        return None

    def _choose_destination_lilly_pad(self, possible_lilly_pads):
        centre_pad = self._find_centre_lilly_pad(possible_lilly_pads)
        if centre_pad is not None:
            return centre_pad, True
        else:
            return random.choice(possible_lilly_pads), False

    def jump(self, lilly_pad_list):
        possible_lilly_pads = self._find_possible_lilly_pads(lilly_pad_list)
        if len(possible_lilly_pads) > 0:
            destination_lilly_pad, centre = self._choose_destination_lilly_pad(possible_lilly_pads)
            self._move_to_lilly_pad(destination_lilly_pad)
            if centre:
                return "win"
            else:
                return
        else:
            self.playing = False
            return "out"
