import numpy as np
import pygame
import time
from Icebergs import spawn

pygame.init()
width, height = 10, 3
side, thickness = 100, 1
margin = side
xres, yres = width * side + 2 * margin, height * side + 2 * margin
screen = pygame.display.set_mode((xres, yres))


def get_dir(key):
    if key == pygame.KEY_w:
        return 0
    elif key == pygame.KEY_a:
        return 1
    elif key == pygame.KEY_s:
        return 2
    elif key == pygame.KEY_d:
        return 3


def draw_field():
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, xres, yres))
    for i in range(width):
        for j in range(height):
            pygame.draw.rect(screen, (0, 0, 0), (i * side +
                                                 margin, j * side + margin, side, side), 1)


spawn(width, height, screen, side, margin)
draw_field()
#player = ship()
turn = 0
pygame.display.flip()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif (event.key == pygame.K_w or event.key == pygame.K_a or
                  event.key == pygame.K_s or event.key == pygame.K_d):
                dir = get_dir(event.key)
                # res = ship.move()
                # if res == 2:
                #    restart()
                # elif res == 1:
                #     pass
                # else:
                turn += 1
                if turn == 2:
                    turn = 0
                    draw_field()
                    spawn(width, height, screen, side, margin)
                pygame.display.flip()
