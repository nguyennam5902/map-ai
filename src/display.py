import math
import pygame

from const import *
from point import Point
from road import Road, TwoWayRoad


class Display:
    def __init__(self) -> None:
        self.maximized = True
        self.ratio = MINIMIZED_WINDOW_HEIGHT / MAXIMIZED_WINDOW_HEIGHT
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.big_start_icon = pygame.transform.scale(
            pygame.image.load("assets/start.png"), (64, 64))
        self.big_end_icon = pygame.transform.scale(
            pygame.image.load("assets/destination.png"), (64, 64))
        self.small_start_icon = pygame.transform.scale(
            pygame.image.load("assets/start.png"), (32, 32))
        self.small_end_icon = pygame.transform.scale(
            pygame.image.load("assets/destination.png"), (32, 32))

        self.toggle_show_defined = False
        self.mouse_pos = (0, 0)
        self.close_points = []

    def show_background(self, surface: pygame.Surface, img: pygame.Surface):
        if self.maximized:
            surface.blit(img, (0, 0))
        else:
            surface.blit(
                pygame.transform.scale(
                    img, (MINIMIZED_WINDOW_WIDTH, MINIMIZED_WINDOW_HEIGHT)),
                (0, 0))

    def show_ui(self, surface: pygame.Surface, start_point: Point,
                end_point: Point, start_time: float, end_time: float,
                route_length: float, is_click: bool):
        color = COLOR["WHITE"]
        pygame.draw.rect(surface, color,
                         pygame.Rect(UI_LEFT, UI_TOP, UI_WIDTH, UI_HEIGHT))

        UI_CENTER_x = UI_LEFT + UI_WIDTH // 2
        UI_CENTER_y = UI_TOP + UI_HEIGHT // 2
        start_icon_rect = self.big_start_icon.get_rect()
        start_icon_rect.x = UI_CENTER_x - 200
        start_icon_rect.y = UI_CENTER_y - 400

        end_icon_rect = self.big_end_icon.get_rect()
        end_icon_rect.x = UI_CENTER_x - 200
        end_icon_rect.y = UI_CENTER_y - 300

        time_text = ""
        if is_click:
            time_text = "Search time: {:.2f} ms".format(
                1000 * (end_time - start_time))
        search_time = self.font.render(time_text, True, 'black', 'white')
        search_time_rect = search_time.get_rect()
        search_time_rect.x = UI_CENTER_x - 200
        search_time_rect.y = UI_CENTER_y - 100

        length_text, length_text_font = "", 'black'
        if is_click:
            if start_point and end_point:
                length_text = "Length: {:.2f} m".format(
                    route_length) if route_length else "PATH NOT FOUND"
        if not route_length:
            length_text_font = 'red'
        route_length_text = self.font.render(length_text, True,
                                             length_text_font)
        route_length_rect = route_length_text.get_rect()
        route_length_rect.x = UI_CENTER_x - 200
        route_length_rect.y = UI_CENTER_y

        surface.blit(self.big_start_icon, start_icon_rect)
        surface.blit(self.big_end_icon, end_icon_rect)
        surface.blit(search_time, search_time_rect)
        surface.blit(route_length_text, route_length_rect)

        if start_point:
            start_location = self.font.render(str(start_point), True, 'black')
            start_location_rect = start_location.get_rect()
            start_location_rect.x = UI_CENTER_x - 120
            start_location_rect.y = UI_CENTER_y - 380
            surface.blit(start_location, start_location_rect)
        if end_point:
            end_location = self.font.render(str(end_point), True, 'red')
            end_location_rect = end_location.get_rect()
            end_location_rect.x = UI_CENTER_x - 120
            end_location_rect.y = UI_CENTER_y - 280
            surface.blit(end_location, end_location_rect)

    def show_locations(self, surface: pygame.Surface, start_point: Point,
                       end_point: Point):
        if start_point:
            surface.blit(self.small_start_icon,
                         (start_point[0] - 16, start_point[1] - 32))
        if end_point:
            surface.blit(self.small_end_icon,
                         (end_point[0] - 16, end_point[1] - 32))

    def draw_points(self, surface: pygame.Surface, points: list[Point]):
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

    def draw_roads(self,
                   surface: pygame.Surface,
                   roads: list[Road],
                   color=COLOR["BLACK"]):
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
                start_pos = (self.ratio * x1, self.ratio * y1)
                end_pos = (self.ratio * x2, self.ratio * y2)
                pygame.draw.line(surface, color, start_pos, end_pos, width)

    def draw_arrow(self,
                   surface: pygame.Surface,
                   start_pos: tuple,
                   end_pos: tuple,
                   color=COLOR["BLACK"]):
        width = ROAD_WIDTH

        x1, y1 = start_pos
        x2, y2 = end_pos

        angle = math.atan2(y2 - y1, x2 - x1)
        angle = math.degrees(angle)

        pygame.draw.line(surface, color, start_pos, end_pos, width)

        arrow_width = 10
        arrow_len = 15

        arrow_points = [(0, 0), (-arrow_len, -arrow_width / 2),
                        (-arrow_len, arrow_width / 2)]

        rotated_arrow_points = []

        for point in arrow_points:
            rotated_x = point[0] * math.cos(
                math.radians(angle)) - point[1] * math.sin(math.radians(angle))
            rotated_y = point[0] * math.sin(
                math.radians(angle)) + point[1] * math.cos(math.radians(angle))
            rotated_arrow_points.append((x2 + rotated_x, y2 + rotated_y))

        pygame.draw.polygon(surface, color, rotated_arrow_points)

    def draw_found_route(self, surface: pygame.Surface, roads: list[Road]):
        if roads is None: return
        color = COLOR["RED"]
        width = ROAD_WIDTH
        if self.maximized:
            self.draw_roads(surface, roads, color)
            # self.draw_arrow(surface, start_pos, end_pos, color)
        else:
            for road in roads:
                x1, y1 = road.from_pos
                x2, y2 = road.to_pos
                start_pos = (self.ratio * x1, self.ratio * y1)
                end_pos = (self.ratio * x2, self.ratio * y2)
                pygame.draw.line(surface, color, start_pos, end_pos, width)