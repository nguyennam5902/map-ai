import os
import pygame

from point import Point
from road import Road


class App:
    def __init__(self):
        self.points = []
        self.roads = []
        self.map = None

        self.start_point = None
        self.dragging = False

    def show_display(self, surface):
        #TODO: circle button
        self.show_bg(surface)
        self.show_route(surface)
        self.show_lines(surface)

    def show_bg(self, surface):
        bg_texture = os.path.join(f'assets/truc_bach_map.png')
        self.map = pygame.image.load(bg_texture).convert()
        surface.blit(self.map, [0, 0])

    def show_route(self, surface):
        for point in self.points:
            color = (0, 0, 0)
            center = (point.x, point.y)
            radius = 5
            pygame.draw.circle(surface, color, center, radius)

    def show_lines(self, surface):
        color = (0, 0, 0)
        width = 5
        for road in self.roads:
            start_pos = road.from_pos
            end_pos = road.to_pos
            pygame.draw.line(surface, color, start_pos, end_pos, width)

    def add_point(self, point):
        self.points.append(point)

    def add_roads(self, road: Road):
        self.roads.append(road)
        # print(str(road) + ",")

    def draw_point(self, x: int, y: int):
        self.add_point(Point(x, y))

    def find_path(self, start_point: Point, end_point: Point):
        print(start_point.name + " -->" + end_point.name)
