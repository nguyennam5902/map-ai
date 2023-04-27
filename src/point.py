import math
import numpy as np
from const import *


class Point:
    def __init__(self, pos, pos2=None):
        #receive pos as (x,y)
        # self.name = name
        if pos2 is None:
            self.pos = pos
            self.x, self.y = pos
            self.adjacents = []  #(road, adj_point)

        #receive x, y
        else:
            self.pos = (pos, pos2)
            self.x = pos
            self.y = pos2
            self.adjacents = []

    # calculate distance to another position
    def _calc_dist(self, pos):
        return math.dist(self.pos, pos)

    # check if the position is near to another position
    def _is_near(self, pos):
        return self._calc_dist(pos) <= MIN_DIST_POINT

    # return the point's degree = number of adjacents road
    def _degree(self):
        return len(self.adjacents)

    def __eq__(self, _point: object):
        if self is None or _point is None:
            return (self is None) and (_point is None)
        return self.x == _point.x and self.y == _point.y

    def __str__(self):
        # return f'{self.name}{self.pos}'
        return f'{self.pos}'