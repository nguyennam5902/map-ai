import math
from const import *
from point import Point
from road import TwoWayRoad


class Map:
    def __init__(self):
        self.img = None
        
        points = set()
        for from_pos, to_pos in ROADS:
            points.add(from_pos)
            points.add(to_pos)
        
        self.map_points = { str(point): Point("", point) for point in points }
        self.roads = [ TwoWayRoad(self.map_points[str(from_pos)], self.map_points[str(to_pos)]) for from_pos, to_pos in ROADS ]
        self.current_route = []
        
    def show_bg(self):
        pass
    
    def show_definedRoad(self):
        pass
    
    def show_definedPoint(self):
        pass
    
    def find_route(self, start_pos, end_pos):
            
        process_point = {}
        for key in self.map_points:
            process_point[key] = ProcessPoint(self.map_points[key])
            
        if self.map_points[str(start_pos)] is None:
            process_point[str(start_pos)] = ProcessPoint(start_pos)
            
        if self.map_points[str(end_pos)] is None:
            process_point[str(end_pos)] = ProcessPoint(end_pos)
            
        open_lst = {str(start_pos)} 
        closed_lst = set()
        
        found = False
        
        while len(open_lst) > 0:
            # find node with the least f on the open list -> q
            minf = min([ process_point[key].f for key in open_lst])
            q = None
            for key in open_lst:
                if minf == process_point[key].f:
                    q = key
                    break
            
            # pop q from open list
            open_lst.remove(q)
            closed_lst.add(q)
            
            # generate q's successors and set their parent to q
            current_point = process_point[q]
            for road, to_point in current_point.point.adjacents:
                
                # if successor is the goal, stop searching and output
                process_to_point = process_point[str(to_point)]
                current_f = process_to_point.f
                if process_to_point.pos == end_pos:
                    process_to_point.parent = current_point
                    
                    stack = []
                    k = process_to_point
                    while k is not None:
                        stack.append(k)
                        k = k.parent
                    
                    while len(stack) > 0:
                        print(stack[-1].pos)
                        stack.pop()
                    
                    found = True
                    return
                
                elif not str(to_point) in closed_lst:
                    g_new = current_point.g + road.length
                    h_new = current_point._calc_dist(end_pos)
                    f_new = g_new + h_new
                    
                    if str(to_point) not in open_lst or current_f > f_new:
                        open_lst.add(str(to_point))
                        
                        process_to_point.f = f_new
                        process_to_point.g = g_new
                        process_to_point.h = h_new
                        process_to_point.parent = current_point
                        
        if not found:
            print("CAN'T FIND ROUTE")
    
class ProcessPoint:
    
    def __init__(self, point):
        self.point = point
        self.pos = point.pos
        self.f = INFINITY
        self.g = INFINITY
        self.h = INFINITY
        self.parent = None
        
    def _calc_dist(self, pos):
        return math.dist(self.pos, pos)
        
    def __str__(self):
        return f'{self.pos}'

map = Map()
map.find_route((781, 733), (81, 701))