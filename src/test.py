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
        self.screen = pygame.display.set_mode((MAXIMIZED_WINDOW_WIDTH, MAXIMIZED_WINDOW_HEIGHT))
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

        while True:

            display.show_background(screen, map.img)
            display.draw_points(screen, list(map.map_points.values()))
            display.draw_roads(screen, map.roads)
            display.draw_found_route(screen, self.route)
            display.show_ui(screen)
            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == MOUSEMOTION:
                    display.mouse_pos = event.pos
                    display.close_points = [ map.map_points[key].pos for key in map.map_points if map.map_points[key]._is_near(event.pos)]

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
                            self.screen = pygame.display.set_mode( (MAXIMIZED_WINDOW_WIDTH, MAXIMIZED_WINDOW_HEIGHT) )
                        else:
                            self.screen = pygame.display.set_mode( (MINIMIZED_WINDOW_WIDTH, MINIMIZED_WINDOW_HEIGHT) )

                    if event.key == K_r:
                        #print all roads:
                        for road in map.roads:
                            if (not isinstance(road, TwoWayRoad)):
                                print(road)

                    if event.key == K_1:
                        # create map
                        points_set = set([ from_pos for from_pos, to_pos in TWO_WAY_ROADS])
                        for from_pos, to_pos in TWO_WAY_ROADS:
                            points_set.add(to_pos)
                        for from_pos, to_pos in ONE_WAY_ROADS:
                            points_set.add(from_pos)
                            points_set.add(to_pos)
                        
                        for point in points_set:
                            self.map.map_points[str(point)] = Point(point)
                        
                        for from_pos, to_pos in TWO_WAY_ROADS:
                            self.map.roads.append(TwoWayRoad( map.map_points[str(from_pos)] , map.map_points[str(to_pos)] ))

                        for from_pos, to_pos in ONE_WAY_ROADS:
                            self.map.roads.append(Road( map.map_points[str(from_pos)] , map.map_points[str(to_pos)] ))

                    if event.key == K_2:
                        start_pos = (35, 825)
                        end_pos = (673, 762)
                        self.route = map.find_route(start_pos, end_pos)

                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()

main = Main()
main.mainloop()
