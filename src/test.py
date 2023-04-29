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
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    x1, y1 = event.pos
                    start_pos = list(map.map_points.values())[0]
                    for point in list(map.map_points.values()):
                        if point._calc_dist((x1, y1)) < start_pos._calc_dist((x1, y1)):
                            start_pos = point

                    self.start_point = start_pos
                    self.dragging = True


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
                    #         road = TwoWayRoad(from_point=self.start_point, to_point=end_point)
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
                            print(road)

                    if event.key == K_1:
                        # create map
                        points_set = set([ from_pos for from_pos, to_pos in TWO_WAY_ROADS])
                        for from_pos, to_pos in TWO_WAY_ROADS:
                            points_set.add(to_pos)
                        
                        for point in points_set:
                            self.map.map_points[str(point)] = Point(point)
                        
                        for from_pos, to_pos in TWO_WAY_ROADS:
                            self.map.roads.append(TwoWayRoad( map.map_points[str(from_pos)] , map.map_points[str(to_pos)] ))

                    if event.key == K_2:
                        start_pos = (411, 172)
                        end_pos = (673, 762)
                        self.route = map.find_route(start_pos, end_pos)
                                

                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()

main = Main()
main.mainloop()