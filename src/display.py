import pygame

from const import *

class Display:
    def __init__(self) -> None:
        self.maximized = True
        self.ratio = MINIMIZED_WINDOW_HEIGHT / MAXIMIZED_WINDOW_HEIGHT

    def show_background(self, surface, img):
        if self.maximized:
            surface.blit(img, (0, 0))
        
        else:
            surface.blit(pygame.transform.scale(img, (MINIMIZED_WINDOW_WIDTH, MINIMIZED_WINDOW_HEIGHT)), (0, 0))

    def draw_points(self, surface, points):
        if self.maximized:
            for point in points:
                color = COLOR["BLACK"]
                center = point.pos
                radius = POINT_RADIUS
                pygame.draw.circle(surface, color, center, radius)
        else:
            for point in points:
                color = COLOR["BLACK"]
                center = (point.x * self.ratio, point.y * self.ratio)
                radius = POINT_RADIUS
                pygame.draw.circle(surface, color, center, radius)
            

    def draw_roads(self, surface, roads):
        color = COLOR["BLACK"]
        width = ROAD_WIDTH
        if self.maximized:
            for road in roads:
                start_pos = road.from_pos
                end_pos = road.to_pos
                pygame.draw.line(surface, color, start_pos, end_pos, width)
        else:
            for road in roads:
                x1, y1 = road.from_pos
                x2, y2 = road.to_pos
                start_pos = ( self.ratio * x1, self.ratio * y1)
                end_pos = (self.ratio * x2, self.ratio * y2)
                pygame.draw.line(surface, color, start_pos, end_pos, width)

    def draw_arrows(self, surface, road):
        pass

    def draw_found_route(self, surface, roads):
        if roads is None: return
        color = COLOR["RED"]
        width = ROAD_WIDTH
        if self.maximized:
            for road in roads:
                start_pos = road.from_pos
                end_pos = road.to_pos
                pygame.draw.line(surface, color, start_pos, end_pos, width)
        else:
            for road in roads:
                x1, y1 = road.from_pos
                x2, y2 = road.to_pos
                start_pos = ( self.ratio * x1, self.ratio * y1)
                end_pos = (self.ratio * x2, self.ratio * y2)
                pygame.draw.line(surface, color, start_pos, end_pos, width)