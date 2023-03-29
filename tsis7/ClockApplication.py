import pygame
import time

def new_sizex(x):
    return x.get_width() / 2

def new_sizey(y):
    return y.get_height() / 2

def blitRotate(surf, image, pos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0], pos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)

pygame.init()

pygame.display.set_caption("Mickey Clock")

screen = pygame.display.set_mode((700, 525))
clock_image = pygame.image.load("./images/main-clock.jpeg")
minute_image = pygame.image.load("./images/right-hand.png")
second_image = pygame.image.load("./images/left-hand.png")

clock_image = pygame.transform.scale(clock_image, (new_sizex(clock_image), new_sizey(clock_image)))
minute_image = pygame.transform.scale(minute_image, (new_sizex(minute_image), new_sizey(minute_image)))
second_image = pygame.transform.scale(second_image, (new_sizex(second_image), new_sizey(second_image)))

check = True
while check:

    pygame.display.update()
    screen.blit(clock_image, (0, 0))
    current_time = time.localtime()
    min_angle = current_time.tm_min * 6 + current_time.tm_sec / 10.0
    sec_angle = current_time.tm_sec * 6

    pos = (350, 262.5)
    blitRotate(screen, minute_image, pos, -min_angle - 220)
    blitRotate(screen, second_image, pos, -sec_angle - 220)

    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()

    time.sleep(1)