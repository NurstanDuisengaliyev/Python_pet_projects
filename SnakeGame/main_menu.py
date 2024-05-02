import pygame
import sys
from get_user import get_user


class InputBox:
    def __init__(self, x, y, w, h, font, text=''):
        self.font = font
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('lightskyblue3')
        self.text = text
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = pygame.Color('dodgerblue2') if self.active else pygame.Color('lightskyblue3')
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    pass  # Entered the Username. Now we have to take information from database
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


class Main_menu:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def runGame(self, SCREEN):
        pygame.display.set_caption("HomePage")
        clock = pygame.time.Clock()
        input_box = InputBox(self.width // 2 - 100, self.height // 2 - 40, 140, 40, pygame.font.SysFont('arial', 23))
        write_username_txt = pygame.font.SysFont("Graphic", 25).render("Write down your Username", True, (250, 0, 0))
        while True:
            clock.tick(30)
            SCREEN.fill((30, 30, 30))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(input_box.text) > 0:
                        current_state = get_user(input_box.text, self.width, self.height)
                        return current_state
                # Getting User from database

                input_box.handle_event(event)
            input_box.update()
            input_box.draw(SCREEN)
            SCREEN.blit(write_username_txt, (self.width // 2 - 100, self.height // 2 - 80))
            pygame.display.update()



