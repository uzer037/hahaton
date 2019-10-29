import numpy as np
import pygame
import time
from Icebergs import spawn

pygame.init()
width, height = 10, 3
side, thickness = 100, 1
xres, yres = width * side, height * side
screen = pygame.display.set_mode((xres, yres))
screenarr = pygame.PixelArray(screen)
pygame.draw.rect(screen, (255, 255, 255), (0, 0, xres, yres))

def draw_field():
    for i in range(width):
        for j in range(height):
            pygame.draw.rect(screen, (0, 0, 0), (i * side, j * side, side, side), 1)


spawn(width, height, screen, side)
draw_field()
#draw_ship()
pygame.display.flip()
done = False
while not done:
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            done = True
