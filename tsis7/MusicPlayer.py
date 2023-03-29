import pygame
import os

pygame.init()
screen = pygame.display.set_mode((334, 199+70))
pygame.display.set_caption("MusicPlayer")
music_library = []

for name in os.listdir("./music"):
    if name[0] != '.':
        music_library.append(
            dict(path=os.path.join("./music/", name), name=name[0:name.find('.')])
        )

music_index = 0
MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)
on_pause = False
started = False
image = pygame.image.load("./images/music_player.jpeg")
font = pygame.font.SysFont("AndaleMono", 15)

def change_music(change):
    global music_index
    global music_library
    music_index += change
    if music_index == len(music_library):
        music_index = 0
    if music_index == -1:
        music_index = len(music_library) - 1
    print(music_library[music_index].get("path"))
    pygame.mixer.music.load(music_library[music_index].get("path"))
    pygame.mixer.music.play()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == MUSIC_END:
            change_music(+1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            change_music(+1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            change_music(-1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not started:
                started = True
                pygame.mixer.music.load(music_library[music_index].get("path"))
                pygame.mixer.music.play()
            else:
                if on_pause:
                    on_pause = not on_pause
                    pygame.mixer.music.pause()
                else:
                    on_pause = not on_pause
                    pygame.mixer.music.unpause()
        screen.fill((255, 255, 255))
        text = font.render(music_library[music_index].get("name"), True, (0, 128, 0))
        screen.blit(image, (0, 70))
        screen.blit(text, (50, 85))
        pygame.display.update() #python3 MusicPlayer.py