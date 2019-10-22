import random


class LillyPad(object):

    def __init__(self, position,min_radius, max_radius):
        pass

    def _choose_radius(self, min_radius, max_radius):
        return random.uniform(min_radius, max_radius)
