from abc import ABC

import pygame
import sys
from math import sqrt
pygame.init()

screen_width, screen_height = 900, 900
screen = pygame.display.set_mode((screen_width, screen_height))
FONT = pygame.font.SysFont("Arial", 20)
colors = dict(
    {
        "black": [0, 0, 0],
        "white": [255, 255, 255],
        "yellow": [255, 255, 0],
        "green": [0, 255, 0],
        "blue": [0, 0, 255],
        "red": [255, 0, 0],
    }
)
current_color = "white"

class GameObject:
    def draw(self):
        raise NotImplementedError

    def handle(self):
        raise NotImplementedError

# Pen, Circle, Rectangle, Square, Rhombus, Eraser, RightT, EquilateralT

def relt_location(p1, p2):
    if p2[0] <= p1[0]:
        if p2[1] <= p1[1]:
            return "left-top"
        else:
            return "left-bottom"
    else:
        if p2[1] <= p1[1]:
            return "right-top"
        else:
            return "right-bottom" 


class Pen(GameObject):
    def __init__(self, start_pos):
        self.points = []
        self.color = "white"

    def draw(self):
        for idx, point in enumerate(self.points[:-1]):
            pygame.draw.line(
                screen,
                colors[self.color],
                start_pos=point,  # self.points[idx]
                end_pos=self.points[idx + 1],
                width=5,
            )

    def handle(self, mouse_pos, color):
        self.color = color
        self.points.append(mouse_pos)

class Circle(GameObject):
    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = "white"

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        width = end_pos_x - start_pos_x
        height = end_pos_y - start_pos_y
        min_side = min(width, height)

        center_x, center_y = start_pos_x + width / 2, start_pos_y + height / 2

        pygame.draw.circle(screen, colors[self.color], (center_x, center_y), min_side / 2, 5)

    def handle(self, mouse_pos, color):
        self.end_pos = mouse_pos
        self.color = color


class Rectangle(GameObject):
    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = "white"

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.rect(
            screen,
            colors[self.color],
            (
                start_pos_x,
                start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=5,
        )

    def handle(self, mouse_pos, color):
        self.end_pos = mouse_pos
        self.color = color

class Square(GameObject):
    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = "white"

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        width = end_pos_x - start_pos_x
        height = end_pos_y - start_pos_y
        min_side = min(width, height)

        center_x, center_y = start_pos_x + width / 2, start_pos_y + height / 2

        pygame.draw.rect(
            screen,
            colors[self.color],
            (
                start_pos_x,
                start_pos_y,
                min_side,
                min_side,
            ),
            width=5,
        )

    def handle(self, mouse_pos, color):
        self.end_pos = mouse_pos
        self.color = color

class RightT(GameObject):
    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.width = 0
        self.height = 0
        self.color = "white"

    def draw(self):
        location = relt_location(self.start_pos, self.end_pos)
        if location == "left-top":
            x, y = self.start_pos
            width, height = self.width, self.height
            point_list = [(x, y), (x, y - height), (x - width, y)]
            pygame.draw.polygon(screen, colors[self.color], point_list, 5)
        if location == "left-bottom":
            x, y = self.start_pos
            width, height = self.width, self.height
            point_list = [(x, y), (x, y + height), (x - width, y)]
            pygame.draw.polygon(screen, colors[self.color], point_list, 5)
        if location == "right-top":
            x, y = self.start_pos
            width, height = self.width, self.height
            point_list = [(x, y), (x, y - height), (x + width, y)]
            pygame.draw.polygon(screen, colors[self.color], point_list, 5)
        if location == "right-bottom":
            x, y = self.start_pos
            width, height = self.width, self.height
            point_list = [(x, y), (x, y + height), (x + width, y)]
            pygame.draw.polygon(screen, colors[self.color], point_list, 5)

    def handle(self, mouse_pos, color):
        self.end_pos = mouse_pos
        self.color = color
        self.width = max(self.start_pos[0], self.end_pos[0]) - min(self.start_pos[0], self.end_pos[0]) 
        self.height = max(self.start_pos[1], self.end_pos[1]) - min(self.start_pos[1], self.end_pos[1]) 

class EquilateralT(GameObject):
    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.width = 0
        self.height = 0
        self.color = "white"

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        width = end_pos_x - start_pos_x
        height = end_pos_y - start_pos_y

        s = min(width, height)
        x, y = start_pos_x, start_pos_y

        point_list = [(x, y), (x + s, y), (x + s / 2, y - sqrt(3) * s / 2)]
        pygame.draw.polygon(screen, colors[self.color], point_list, 5)

    def handle(self, mouse_pos, color):
        self.end_pos = mouse_pos
        self.color = color
        self.width = max(self.start_pos[0], self.end_pos[0]) - min(self.start_pos[0], self.end_pos[0]) 
        self.height = max(self.start_pos[1], self.end_pos[1]) - min(self.start_pos[1], self.end_pos[1]) 


class Rhombus(GameObject):
    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.width = 0
        self.height = 0
        self.color = "white"

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        width, height = self.width, self.height

        x, y = start_pos_x + width/2, start_pos_y + height/2

        point_list = [(x, y - height//2), (x + width//2, y), (x, y + height//2), (x - width//2, y)]
        pygame.draw.polygon(screen, colors[self.color], point_list, 5)

    def handle(self, mouse_pos, color):
        self.end_pos = mouse_pos
        self.color = color
        self.width = max(self.start_pos[0], self.end_pos[0]) - min(self.start_pos[0], self.end_pos[0]) 
        self.height = max(self.start_pos[1], self.end_pos[1]) - min(self.start_pos[1], self.end_pos[1]) 

class Eraser(GameObject):
    def __init__(self, start_pos):
        self.points = []
        self.color = "black"

    def draw(self):
        for idx, point in enumerate(self.points[:-1]):
            pygame.draw.line(
                screen,
                colors[self.color],
                start_pos=point,  # self.points[idx]
                end_pos=self.points[idx + 1],
                width=100,
            )

    def handle(self, mouse_pos, color):
        self.points.append(mouse_pos)

class Button:
    def __init__(self, shape, rect):
        self.type = shape
        self.rect = rect

    def draw(self):
        if self.type == "Circle" or self.type == "Pen" or self.type == "Color":
            pygame.draw.circle(screen, colors[current_color], self.rect.center, self.rect.height // 2)
        if self.type == "Rectangle" or self.type == "Square" or self.type == "Eraser":
            pygame.draw.rect(screen, colors[current_color], self.rect)
        if self.type == "Rhombus":
            x, y = self.rect.center
            width, height = self.rect.width, self.rect.height
            point_list = [(x, y - height//2), (x + width//2, y), (x, y + height//2), (x - width//2, y)]
            pygame.draw.polygon(screen, colors[current_color], point_list)
        if self.type == "RightT":
            x, y = self.rect.left, self.rect.bottom
            width, height = self.rect.width, self.rect.height
            point_list = [(x, y), (x, y - height), (x + width, y)]
            pygame.draw.polygon(screen, colors[current_color], point_list)
        if self.type == "EquilateralT":
            x, y = self.rect.left, self.rect.bottom
            width, height = self.rect.width, self.rect.height
            s = width
            point_list = [(x, y), (x + width, y), (x + width / 2, y - sqrt(3) * s / 2)]
            pygame.draw.polygon(screen, colors[current_color], point_list)
# Color, Eraser, Pen, Circle, Rectangle, Square, Rhombus, RightT, EquilateralT

def main():
    global current_color
    color_pos = 0
    color_list = ["white", "yellow", "green", "blue", "red"]
    current_shape = 'pen'
    clock = pygame.time.Clock()
    active_object = None
    objects = []
    button_list = []
    button_list.append(Button("Color", pygame.Rect(50, 10, 20, 20)))
    button_list.append(Button("Eraser", pygame.Rect(150, 10, 20, 20)))
    button_list.append(Button("Pen", pygame.Rect(250, 10, 20, 20)))
    button_list.append(Button("Circle", pygame.Rect(350, 10, 20, 20)))
    button_list.append(Button("Square", pygame.Rect(450, 10, 20, 20)))
    button_list.append(Button("Rhombus", pygame.Rect(550, 10, 20, 20)))
    button_list.append(Button("RightT", pygame.Rect(650, 10, 20, 20)))
    button_list.append(Button("EquilateralT", pygame.Rect(750, 10, 20, 20)))
    button_list.append(Button("Rectangle", pygame.Rect(850, 10, 20, 20)))
    
    while True:
        screen.fill(colors["black"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                check_for_button = False
                for button in button_list:
                    if button.type != "Color" and button.rect.collidepoint(pygame.mouse.get_pos()):
                        current_shape = button.type
                        check_for_button = True
                    if button.type == "Color" and button.rect.collidepoint(pygame.mouse.get_pos()):
                        check_for_button = True
                        color_pos = (color_pos + 1) % len(color_list)
                        current_color = color_list[color_pos]

                # Color, Eraser, Pen, Circle, Rectangle, Square, Rhombus, RightT, EquilateralT
                if not check_for_button:
                    if current_shape == "Eraser":
                        active_object = Eraser(start_pos= event.pos)
                    if current_shape == "Pen":
                        active_object = Pen(start_pos= event.pos)
                    if current_shape == "Circle":
                        active_object = Circle(start_pos= event.pos)
                    if current_shape == "Rectangle":
                        active_object = Rectangle(start_pos= event.pos)
                    if current_shape == "Square":
                        active_object = Square(start_pos=event.pos)
                    if current_shape == "Rhombus":
                        active_object = Rhombus(start_pos=event.pos)
                    if current_shape == "RightT":
                        active_object = RightT(start_pos=event.pos)
                    if current_shape == "EquilateralT":
                        active_object = EquilateralT(start_pos=event.pos)
            if event.type == pygame.MOUSEMOTION and active_object is not None:
                active_object.handle(mouse_pos=pygame.mouse.get_pos(), color=current_color)
                active_object.draw()
            if event.type == pygame.MOUSEBUTTONUP and active_object is not None:
                objects.append(active_object)
                active_object = None

        for button in button_list:
            button.draw()

        for obj in objects:
            obj.draw()

        clock.tick(60)
        pygame.display.update()

if __name__ == '__main__':
    main()