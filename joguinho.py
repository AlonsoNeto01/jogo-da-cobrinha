from __future__ import division
import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'assets')
sounds_folder = path.join(path.dirname(__file__), 'sounds')

WIDTH = 480
HEIGHT = 600
FPS = 60
POWERUP_TIME = 5000
BAR_LENGTH = 100
BAR_HEIGHT = 10

# define colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
pygame.mixer.init() ##som
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')

def main_menu():
    global screen

    menu_soing = pygame.mixer.music.load(path.join(sounds_folder, 'menu.ogg'))

    pygame.mixer.music.play(-1)

    title = pygame.image.load(path.join(img_dir, 'main.png'))
    title = pygame.transform.scale(title, (WIDTH, HEIGHT),screen)

    screen.blit(title, (0,0))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOW:
            if ev.key == pygame.K_RETURN:
                break
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
        elif ev.type == pygame.QUIT:
            pygame.quit()
            quit()
        else:
            draw_text(screen,"press [ENTER] to being", 30,WIDTH/2, HEIGHT/2)
            draw_text(screen, "or [Q] to quit", 30,WIDTH/2, HEIGHT/2)+40
            pygame.display.update()