import random

from geometry_utilities import GeoUtils


class LillyPad(object):

    def __init__(self, position, min_radius, max_radius):
        pass

    def _choose_radius(self, min_radius, max_radius):
        return random.uniform(min_radius, max_radius)

    def _create_polygon(self, position, radius):
        geo_utils = GeoUtils()
        return geo_utils.circle(position, radius)
