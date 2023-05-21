import sys
import os
import pygame
import time
from pygame.locals import *
from pygame.draw import rect
from pygame.font import Font
from pygame.display import set_mode, set_caption, flip
from pygame.event import get
from const import *
from display import Display
from initialize import *
from map import Map
from point import Point
from road import Road, TwoWayRoad


class Main:
    """Class used for run the application using `pygame`"""
    def __init__(self):
        pygame.init()
        self.screen = set_mode(
            (MAXIMIZED_WINDOW_WIDTH, MAXIMIZED_WINDOW_HEIGHT))
        set_caption('Map Truc Bach')
        self.route = None
        self.map = Map()
        self.display = Display()
        self.start_point = None
        self.dragging = False

    def mainloop(self):
        """The loop of the app"""
        screen = self.screen
        map = self.map
        display = self.display
        start_point, end_point, is_click = None, None, False
        start_time, end_time, route_length, ratio = 0.0, 0.0, 0.0, 1.12
        while True:
            display.show_background(screen, map.img)
            display.draw_points(screen, list(map.map_points.values()))
            display.draw_roads(screen, map.roads)
            display.draw_found_route(screen, self.route)
            display.show_ui(screen, start_point, end_point,
                            1000 * (end_time - start_time), route_length,
                            is_click)
            display.show_locations(screen, start_point, end_point)
            button_rect = rect(screen, 'blue', (UI_LEFT + 150, 250, 150, 50))
            text = Font(None, 36).render("Find route", True, Color("white"))
            screen.blit(text, text.get_rect(center=button_rect.center))
            flip()
            for event in get():
                if event.type == MOUSEBUTTONUP:
                    x, y = event.pos
                    is_click = False
                    if UI_LEFT > x > 16 and y > 32:
                        self.route = []
                        tmp_point = self.choose_point_from_mouse_click((x, y))
                        if event.button == 1:  # Left mouse button
                            if tmp_point != end_point:
                                start_point = tmp_point
                        elif event.button == 3:  # Right mouse button
                            if tmp_point != start_point:
                                end_point = tmp_point
                    if button_rect.collidepoint((x, y)):
                        is_click = True
                        if start_point and end_point:
                            start_time = time.time()
                            self.route = map.find_route(start_point, end_point)
                            end_time = time.time()
                            route_length = ratio * sum([
                                road.length for road in self.route
                            ]) if self.route else 0.0

                elif event.type == KEYDOWN:
                    if event.key == K_s:
                        # toggle map size
                        display.maximized = not display.maximized
                        if display.maximized:
                            self.screen = set_mode((MAXIMIZED_WINDOW_WIDTH,
                                                    MAXIMIZED_WINDOW_HEIGHT))
                        else:
                            self.screen = set_mode((MINIMIZED_WINDOW_WIDTH,
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

                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()

    def choose_point_from_mouse_click(self, start_point: tuple[int, int]):
        """
        Based on a mouse click, choose a point on the screen that its position is exists in the map data.

        :param start_point: A tuple with the (x, y) coordinates of the starting point.

        :return: A tuple with the (x, y) coordinates of the chosen point.
        """
        nearest_road_from, nearest_road_to, min_dist = None, None, 999
        for road in self.map.roads:
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
