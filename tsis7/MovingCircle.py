import pygame

width, height = 600, 600

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('MovingCircle')

clock = pygame.time.Clock()
x = width // 2
y = height // 2

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if y - 20 >= 25:
            y -= 20//3
    if keys[pygame.K_DOWN]:
        if y + 20 <= height - 25:
            y += 20//3
    if keys[pygame.K_LEFT]:
        if x - 20 >= 25:
            x -= 20//3
    if keys[pygame.K_RIGHT]:
        if x + 20 <= width - 25:
            x += 20//3
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    pygame.display.update()
