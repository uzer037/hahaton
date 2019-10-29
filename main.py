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
pygame.draw.rect(screen, (255, 255, 255), (0, 0, xres, yres))

def draw_field():
    for i in range(width):
        for j in range(height):
            pygame.draw.rect(screen, (0, 0, 0), (i * side + margin, j * side + margin, side, side), 1)

def draw_ship(x, y):
    pygame.draw.rect(screen, (0, 255, 0), (x * side + margin, y * side + margin, 10, 10))

spawn(width, height, screen, side, margin)
draw_field()
#draw_ship()
pygame.display.flip()
done = False
while not done:
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            done = True