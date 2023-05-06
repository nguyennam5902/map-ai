import math
import pygame

from const import *
from road import TwoWayRoad

class Display:
    def __init__(self) -> None:
        self.maximized = True
        self.ratio = MINIMIZED_WINDOW_HEIGHT / MAXIMIZED_WINDOW_HEIGHT
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        self.toggle_show_defined = False
        self.mouse_pos = (0, 0)
        self.close_points = []

    def show_background(self, surface, img):
        if self.maximized:
            surface.blit(img, (0, 0))
        
        else:
            surface.blit(pygame.transform.scale(img, (MINIMIZED_WINDOW_WIDTH, MINIMIZED_WINDOW_HEIGHT)), (0, 0))

    def show_ui(self, surface):
        color = COLOR["WHITE"]
        pygame.draw.rect(surface, color, pygame.Rect(UI_LEFT, UI_TOP, UI_WIDTH, UI_HEIGHT))

        UI_CENTER_x = UI_LEFT + UI_WIDTH // 2
        UI_CENTER_y = UI_TOP + UI_HEIGHT // 2

        text = self.font.render( str(self.mouse_pos) , True, (0, 0, 0), (255, 255, 255))

        textRect = text.get_rect()
        textRect.center = (UI_CENTER_x, UI_CENTER_y)

        surface.blit(text, textRect)



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
                if isinstance(road, TwoWayRoad):
                    start_pos = road.from_pos
                    end_pos = road.to_pos
                    pygame.draw.line(surface, color, start_pos, end_pos, width)
                else:
                    start_pos = road.from_pos
                    end_pos = road.to_pos
                    self.draw_arrow(surface, start_pos, end_pos, color)
        else:
            for road in roads:
                x1, y1 = road.from_pos
                x2, y2 = road.to_pos
                start_pos = ( self.ratio * x1, self.ratio * y1)
                end_pos = (self.ratio * x2, self.ratio * y2)
                pygame.draw.line(surface, color, start_pos, end_pos, width)

    def draw_arrow(self, surface, start_pos, end_pos, color=COLOR["BLACK"]):
        width = ROAD_WIDTH

        x1, y1 = start_pos
        x2, y2 = end_pos

        angle = math.atan2(y2 - y1, x2 - x1)
        angle = math.degrees(angle)

        pygame.draw.line(surface, color, start_pos, end_pos, width)

        arrow_width = 10
        arrow_len = 15

        arrow_points = [(0, 0),
                        (-arrow_len, -arrow_width / 2),
                        (-arrow_len, arrow_width / 2)]
        
        rotated_arrow_points = []

        for point in arrow_points:
            rotated_x = point[0] * math.cos(math.radians(angle)) - point[1] * math.sin(math.radians(angle))
            rotated_y = point[0] * math.sin(math.radians(angle)) + point[1] * math.cos(math.radians(angle))
            rotated_arrow_points.append((x2 + rotated_x, y2 + rotated_y))

        pygame.draw.polygon(surface, color, rotated_arrow_points)

    def draw_found_route(self, surface, roads):
        if roads is None: return
        color = COLOR["RED"]
        width = ROAD_WIDTH
        if self.maximized:
            for road in roads:
                start_pos = road.from_pos
                end_pos = road.to_pos
                pygame.draw.line(surface, color, start_pos, end_pos, width)
                # self.draw_arrow(surface, start_pos, end_pos, color)
        else:
            for road in roads:
                x1, y1 = road.from_pos
                x2, y2 = road.to_pos
                start_pos = ( self.ratio * x1, self.ratio * y1)
                end_pos = (self.ratio * x2, self.ratio * y2)
                pygame.draw.line(surface, color, start_pos, end_pos, width)