import pygame
import sys
from pygame.locals import *
import random

pygame.init()

FPS = 16
FramePerSec = pygame.time.Clock()


screen_width = 599
screen_height = 599
block = 20  # the size of every square
score = 0
speed = 5
snake_color = (32, 32, 32)

background_color = (33, 181, 250)
food_color = (82, 237, 65)
text_color = (255, 234, 0)
border_color = (128, 128, 128)
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

score_font = pygame.font.SysFont("Arial", 15)

snake_list = [(15, 15)]  # snake list
go_x, go_y = 0, 0  # change in x and y direction. Initially (0, 0)
border_list = []  # creating borders

for i in range(0, screen_width // block + 1):
    border_list.append((i, 0))
    border_list.append((i, screen_height // block))

for i in range(0, screen_height // block + 1):
    border_list.append((0, i))
    border_list.append((screen_width // block, i))

def draw_borders():  # drawing borders
    for pos in border_list:
        pygame.draw.rect(screen, border_color, (pos[0] * block, pos[1] * block, block - 1, block - 1))


def draw_snake():  # draw snake
    for pos in snake_list:
        pygame.draw.rect(screen, snake_color, (pos[0] * block, pos[1] * block, block-1, block-1))

def get_random():  # get random place for new food
    global snake_list
    pos = []
    for i in range(1, screen_width // block):
        for j in range(1, screen_height // block):
            if (i, j) not in snake_list:
                pos.append((i, j))

    return random.choice(pos)

def check_for_collision(head):  # check for collision between snake head and wall and snake's body (except for head)
    global snake_list
    if (head in snake_list) or (head in border_list):
        return True
    else:
        return False

def draw_score():
    msg = score_font.render("score: " + str(score), True, (0, 0, 0))
    screen.blit(msg, (screen_width - 70, 5))


food_pos = get_random()
inc = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if (go_x, go_y) != (0, 1) and event.key == K_UP and event.key != K_DOWN:
                go_x, go_y = 0, -1
            elif (go_x, go_y) != (0, -1) and event.key == K_DOWN and event.key != K_UP:
                go_x, go_y = 0, 1
            elif (go_x, go_y) != (1, 0) and event.key == K_LEFT and event.key != K_RIGHT:
                go_x, go_y = -1, 0
            elif (go_x, go_y) != (-1, 0) and event.key == K_RIGHT and event.key != K_LEFT:
                go_x, go_y = 1, 0

    screen.fill(background_color)
    draw_borders()
    pygame.draw.rect(screen, food_color, (food_pos[0] * block, food_pos[1] * block, block-1, block-1))

    if (go_x, go_y) != (0, 0) and check_for_collision((snake_list[-1][0] + go_x, snake_list[-1][1] + go_y)):
        pygame.quit()
        sys.exit()

    snake_list.append((snake_list[-1][0] + go_x, snake_list[-1][1] + go_y))

    if snake_list[-1] == food_pos:
        score += 1
        inc += 1
        if inc >= 3:
            FPS += 1.5
            inc = 0
        food_pos = get_random()
    else:
        del snake_list[0]

    draw_snake()
    draw_score()

    pygame.display.update()
    FramePerSec.tick(FPS)


