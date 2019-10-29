from random import randrange
import pygame


def draw_field(width, height, screen, size, path):
    water = pygame.image.load('water.png').convert_alpha()
    water = pygame.transform.scale(water, (size, size))
    pos = [(water, (size * (j % width), size * (j // width))) for j in range(width * height)]
    screen.blits(pos)
    pic = pygame.image.load('check_line.png').convert_alpha()
    pic = pygame.transform.scale(pic, (2 * size, 2 * size))
    for i in path:
        screen.blit(pic, (size // 2 * i[0] - size, size // 2 * i[1] - size // 2))