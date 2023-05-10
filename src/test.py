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
            # Draw the button on the screen with the background color
            button_rect = pygame.draw.rect(screen, pygame.Color("blue"),
                                           (UI_LEFT + 150, 250, 150, 50))
            text_surface = pygame.font.Font(None,
                                            36).render("Find route", True,
                                                       pygame.Color("white"))
            screen.blit(text_surface,
                        text_surface.get_rect(center=button_rect.center))
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

                elif event.type == MOUSEBUTTONUP:
                    x, y = event.pos
                    if UI_LEFT > x > 16 and y > 32:
                        self.route = []
                        if event.button == 1:  # Left mouse button
                            start_point = self.choose_point_from_mouse_click(
                                (x, y))

                        elif event.button == 3:  # Right mouse button
                            end_point = self.choose_point_from_mouse_click(
                                (x, y))
                    if button_rect.collidepoint((x, y)):
                        if start_point and end_point:
                            self.route = map.find_route(start_point, end_point)

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
                        if start_point and end_point:
                            self.route = map.find_route(start_point, end_point)

                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()

    def choose_point_from_mouse_click(self, start_point: tuple[int, int]):
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
