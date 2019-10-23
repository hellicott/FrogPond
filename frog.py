from geometry_utilities import Circle
from shapely.geometry.point import Point


class Frog(object):

    def __init__(self, position: Point, max_jump, id):
        self.position = position
        self.max_jump = max_jump
        self.lilly_pads_visited = []
        self.id = id

    def _get_range(self):
        return Circle(self.position, self.max_jump)

#
#     def find_possible_lilly_pads(self, lilly_pad_list):
#         possible_lilly_pads = []
#         for lilly_pad in lilly_pad_list:
#             if lilly_pad.circle.intersects_circle(self._get_range()):
#                 possible_lilly_pads.append(lilly_pad)
#         return possible_lilly_pads
