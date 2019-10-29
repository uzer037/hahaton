from random import randrange
import pygame


def draw_field(width, height, screen, size):
    water = pygame.image.load('water.png').convert_alpha()
    water = pygame.transform.scale(water, (size, size))
    pos = [(water, (size * (j % width), size * (j // width))) for j in range(width * height)]
    screen.blits(pos)


def spawn_random(width, height, screen, size, shift, n):
    iceberg = pygame.image.load('iceberg.png').convert_alpha()
    iceberg = pygame.transform.scale(iceberg, (size, size))
    x1, x2 = randrange(width * 2 + 1), randrange(width * 2 + 1)
    y1, y2 = randrange(height + 1), randrange(height + 1)
    if x1 == x2 and y1 == y2:
        if x1 > 0:
            x1 -= 1
        else:
            x1 += 1
    if x1 % 2 == 0:
        screen.blit(iceberg, (x1 // 2 * size + shift - size // 2, (y1 - 1) * size + shift))
    else:
        screen.blit(iceberg, (x1 // 2 * size + shift, y1 * size + shift - size // 2))

    if x2 % 2 == 0:
        screen.blit(iceberg, (x2 // 2 * size + shift - size // 2, (y2 - 1) * size + shift))
    else:
        screen.blit(iceberg, (x2 // 2 * size + shift, y2 * size + shift - size // 2))

    return x1, y1, x2, y2


def spawn(width, height, screen, size, shift, coords):

