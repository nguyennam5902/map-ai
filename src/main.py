import sys
from pygame import *
from const import *
from app import App
from point import Point
from road import Road


class Main:
    def __init__(self):
        init()
        self.screen = display.set_mode((MINIMIZED_WINDOW_WIDTH, MINIMIZED_WINDOW_HEIGHT))
        display.set_caption('Map Hanoi')
        self.app = App()

    def mainloop(self):
        app = self.app
        screen = self.screen
        # Draw point
        # for i in range(len(MAP_POINTS)):
        #     app.draw_point(MAP_POINTS[i][0], MAP_POINTS[i][1])
        # print(len(app.points))

        # Draw roads
        for i in range(len(TWO_WAY_ROADS)):
            # print(f"{TWO_WAY_ROADS[i][0]} --> {TWO_WAY_ROADS[i][1]}")
            tmp_from = Point(TWO_WAY_ROADS[i][0][0], TWO_WAY_ROADS[i][0][1])
            tmp_to = Point(TWO_WAY_ROADS[i][1][0], TWO_WAY_ROADS[i][1][1])
            app.add_roads(Road(tmp_from, tmp_to))

        button_width, button_height = 160, 50
        button_location = (200, 20)
        button_color, button_border_color = Color("blue"), Color("white")
        start_point = None
        while True:
            app.show_display(screen)
            # button_rect = draw.rect(screen, button_color,(button_location[0], button_location[1],button_width, button_height))
            # text_surface = font.Font(None, 36).render("Search path", True,Color("white"))
            # text_rect = text_surface.get_rect(center=button_rect.center)
            # screen.blit(text_surface, text_rect)
            # draw.rect(screen, button_border_color,(button_location[0], button_location[1], button_width,button_height), 2)
            display.flip()
            for e in event.get():
                if e.type == MOUSEBUTTONDOWN:
                    # if button_rect.collidepoint(e.pos):
                    #     print("Button clicked!")
                    x, y = e.pos
                    app.start_point = start_point
                    app.dragging = True
                elif e.type == MOUSEBUTTONUP:
                    x, y = e.pos
                    # if e.button == 1:  # Left mouse button
                    #     print(f"Left mouse button clicked at {x} - {y}")
                    # elif e.button == 3:  # Right mouse button
                    #     print(f"Right mouse button clicked at {x} - {y}")
                    # app.draw_point(x, y)

                    end_point = None
                    no_close = True
                    for point in app.points:
                        if (x - point.x)**2 + (y - point.y)**2 <= POINT_RADIUS**2:
                            if e.button == 1:
                                start_point = point
                            elif e.button == 3:
                                end_point = point
                            no_close = False
                            break
                    if start_point is not None and end_point is not None and start_point != end_point:
                        tmp_road = Road(start_point, end_point)
                        app.add_roads(tmp_road)
                        print(
                            f"(({start_point.x}, {start_point.y}), ({end_point.x}, {end_point.y})),"
                        )
                    app.dragging = False

                elif e.type == KEYDOWN:
                    if e.key == K_r:
                        #undo
                        if (len(app.roads) > 0):
                            app.roads.pop()

                    elif e.key == K_c:
                        for i in range(len(POINTS) - 1):
                            x1, y1 = POINTS[i]
                            x2, y2 = POINTS[i + 1]
                            app.add_point(Point(x1, y1))
                            app.add_point(Point(x2, y2))
                            app.add_roads(Road(Point(x1, y1), Point(x2, y2)))
                    elif e.key == K_KP_ENTER:
                        for tmp_road in app.roads:
                            ...
                        # print(
                        #     f"{tmp_road.from_point.name} --> {tmp_road.to_point.name}"
                        # )
                elif e.type == QUIT:
                    quit()
                    sys.exit()


main = Main()
main.mainloop()