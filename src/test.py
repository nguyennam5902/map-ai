import sys
import os
import pygame
from pygame.locals import *
from const import *
from display import Display
from map import Map
from point import Point
from road import Road, TwoWayRoad


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (MAXIMIZED_WINDOW_WIDTH, MAXIMIZED_WINDOW_HEIGHT))
        pygame.display.set_caption('Map Truc Bach')
        self.route = None
        self.map = Map()
        self.display = Display()
        self.start_point = None
        self.dragging = False

    def mainloop(self):
        screen = self.screen
        map = self.map
        display = self.display
        start_point, end_point = None, None
        while True:
            display.show_background(screen, map.img)
            display.draw_points(screen, list(map.map_points.values()))
            display.draw_roads(screen, map.roads)
            display.draw_found_route(screen, self.route)
            display.show_ui(screen, start_point, end_point)
            display.show_locations(screen, start_point, end_point)
            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == MOUSEMOTION:
                    display.mouse_pos = event.pos
                    display.close_points = [
                        map.map_points[key].pos for key in map.map_points
                        if map.map_points[key]._is_near(event.pos)
                    ]

                if event.type == MOUSEBUTTONDOWN:
                    x1, y1 = event.pos

                    # start_pos = None
                    # no_point_close = True
                    # for point in list(map.map_points.values()):
                    #     if point._is_near( (x1, y1) ):
                    #         start_pos = point
                    #         no_point_close = False
                    #         break
                    # if no_point_close:
                    #     start_pos = Point(x1, y1)
                    #     map.map_points[str(start_pos)] = start_pos
                    # self.start_point = start_pos
                    # self.dragging = True

                elif event.type == MOUSEBUTTONUP:
                    x, y = event.pos
                    if UI_LEFT > x > 16 and y > 32:
                        if event.button == 1:  # Left mouse button
                            # print(f"Left mouse button clicked at {x} - {y}")
                            start_point = self.choose_point_from_mouse_click(
                                (x, y))

                        elif event.button == 3:  # Right mouse button
                            # print(f"Right mouse button clicked at {x} - {y}")
                            end_point = self.choose_point_from_mouse_click(
                                (x, y))
                            print
                    if start_point and end_point:
                        print(f'{start_point} --> {end_point}')
                    # if self.dragging:
                    #     x2, y2 = event.pos
                    #     end_point = None
                    #     no_point_close = True
                    #     for point in list(map.map_points.values()):
                    #         if point._is_near( (x2, y2) ):
                    #             end_point = point
                    #             no_point_close = False
                    #             break
                    #     if no_point_close:
                    #         end_point = Point(x2, y2)
                    #         map.map_points[str(end_point)] = end_point
                    #     if self.start_point != end_point:
                    #         road = Road(from_point=self.start_point, to_point=end_point)
                    #         map.roads.append(road)
                    # self.dragging = False
                    pass

                elif event.type == KEYDOWN:
                    if event.key == K_s:
                        # toggle map size
                        display.maximized = not display.maximized
                        if display.maximized:
                            self.screen = pygame.display.set_mode(
                                (MAXIMIZED_WINDOW_WIDTH,
                                 MAXIMIZED_WINDOW_HEIGHT))
                        else:
                            self.screen = pygame.display.set_mode(
                                (MINIMIZED_WINDOW_WIDTH,
                                 MINIMIZED_WINDOW_HEIGHT))

                    if event.key == K_r:
                        #print all roads:
                        for road in map.roads:
                            if (not isinstance(road, TwoWayRoad)):
                                print(road)

                    if event.key == K_1:
                        # create map
                        points_set = set(
                            [from_pos for from_pos, to_pos in TWO_WAY_ROADS])
                        for from_pos, to_pos in TWO_WAY_ROADS:
                            points_set.add(to_pos)
                        for from_pos, to_pos in ONE_WAY_ROADS:
                            points_set.add(from_pos)
                            points_set.add(to_pos)

                        for point in points_set:
                            self.map.map_points[str(point)] = Point(point)

                        for from_pos, to_pos in TWO_WAY_ROADS:
                            self.map.roads.append(
                                TwoWayRoad(map.map_points[str(from_pos)],
                                           map.map_points[str(to_pos)]))

                        for from_pos, to_pos in ONE_WAY_ROADS:
                            self.map.roads.append(
                                Road(map.map_points[str(from_pos)],
                                     map.map_points[str(to_pos)]))

                    if event.key == K_2:
                        # Terminal: (41, 837) --> (689, 748)
                        start_pos = start_point
                        end_pos = end_point
                        self.route = map.find_route(start_pos, end_pos)

                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()

    def choose_point_from_mouse_click(self, start_point):
        nearest_road_from = None
        nearest_road_to = None
        min_dist = 999
        for road in self.map.roads:
            # print(road.__class__.__name__)
            if road._is_look(start_point):
                tmp_dist = road._calc_dist(start_point)
                if tmp_dist < min_dist:
                    nearest_road_from = road.from_point
                    nearest_road_to = road.to_point
                    min_dist = tmp_dist
        if nearest_road_to and nearest_road_from:
            dist_from, dist_to = nearest_road_from._calc_dist(
                start_point), nearest_road_to._calc_dist(start_point)
            if dist_from < dist_to:
                start_point = (nearest_road_from.x, nearest_road_from.y)
            else:
                start_point = (nearest_road_to.x, nearest_road_to.y)

        return start_point


main = Main()
main.mainloop()
