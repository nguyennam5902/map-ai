import math
import numpy as np
from numpy.linalg import norm
from const import *
from point import Point


# we can only move from an end to another end
class Road:
    def __init__(self, from_point: Point, to_point: Point):
        self.from_point = from_point
        self.to_point = to_point
        self.from_pos = from_point.pos
        self.to_pos = to_point.pos

        self.length = math.dist(from_point.pos, to_point.pos)
        self.from_point.adjacents.append((self, to_point))

    # calculate distance from a position to the road
    def _calc_dist(self, pos):
        p1 = np.asarray(self.from_pos)
        p2 = np.asarray(self.to_pos)
        p3 = np.asarray(pos)

        return np.abs(np.cross(p2 - p1, p1 - p3)) / norm(p2 - p1)

    # is a position is near to road
    def _is_near(self, pos):
        x, y = pos
        x1, y1 = self.from_pos
        x2, y2 = self.to_pos

        is_x_middle = (x >= x1 and x <= x2) or (x <= x1 and x >= x2)
        is_y_middle = (y >= y1 and y <= y2) or (y <= y1 and y >= y2)

        return self._calc_dist(pos) <= MIN_DIST_ROAD and (is_x_middle
                                                          or is_y_middle)

    def __eq__(self, _road: object):
        return self.from_pos == _road.from_pos and self.to_pos == _road.to_pos

    def __str__(self):
        return f'({self.from_pos.__str__()}, {self.to_pos.__str__()})'


# We can move from an end to another end and vice versa
class TwoWayRoad(Road):
    def __init__(self, from_point, to_point):
        super().__init__(from_point, to_point)
        self.to_point.adjacents.append((self, from_point))
