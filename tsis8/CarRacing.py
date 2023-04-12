# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initialzing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
SCORE_COINS = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("./tsis8/images/AnimatedStreet.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./tsis8/images/coin.jpg")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() / 11, self.image.get_height() / 11))
        self.rect = self.image.get_rect(
            topleft=(random.randrange(15, SCREEN_WIDTH - 15), random.randrange(SCREEN_HEIGHT // 2, SCREEN_HEIGHT - 15)))
        self.exists = False

    def new_coin(self):
        self.rect.topleft = (
            random.randrange(15, SCREEN_WIDTH - 15), random.randrange(SCREEN_HEIGHT // 2, SCREEN_HEIGHT - 15))
        self.exists = True


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./tsis8/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./tsis8/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


# Setting up Sprites
P1 = Player()
E1 = Enemy()
coin = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Adding a new User event for occurring of coins each

NEW_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(NEW_COIN, 5000)

# adding a new User event for music end
MUSIC_END = pygame.USEREVENT + 3
pygame.mixer.music.set_endevent(MUSIC_END)
pygame.mixer.music.load("./tsis8/Music/background.wav")
pygame.mixer.music.play()
# Game Loop
while True:

    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == MUSIC_END:
            pygame.mixer.music.load("./tsis8/Music/background.wav")
            pygame.mixer.music.play()
        if event.type == INC_SPEED:
            SPEED += 0.3
        if event.type == NEW_COIN:
            coin.new_coin()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    scores_coin = font_small.render(str(SCORE_COINS), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(scores_coin, (SCREEN_WIDTH - 20, 10))  # right_top coin score

    # Draw coin in the position of its rect
    if coin.exists:
        DISPLAYSURF.blit(coin.image, coin.rect)

    if coin.exists and P1.rect.colliderect(coin.rect): # check if it collides p1
        coin.exists = False
        SCORE_COINS += 1

    if pygame.sprite.spritecollideany(coin, enemies): # check if it collides enemy
        coin.exists = False

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('./tsis8/Music/crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
