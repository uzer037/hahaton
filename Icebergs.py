from random import randrange
import pygame


def draw_field(screen, shift, size):
    water = pygame.image.load('water.png').convert_alpha()
    water = pygame.transform.scale(water, (size, size))


def spawn(n, m, screen, size, shift):
    iceberg = pygame.image.load('iceberg.png').convert_alpha()
    iceberg = pygame.transform.scale(iceberg, (size // 2, size // 2))
    x1, x2 = randrange(n * 2 + 1), randrange(n * 2 + 1)
    y1, y2 = randrange(m + 1), randrange(m + 1)
    if x1 == x2 and y1 == y2:
        if x1 > 0:
            x1 -= 1
        else:
            x1 += 1
    if x1 % 2 == 0:
        screen.blit(iceberg, (x1 // 2 * size + shift - size // 4, y1 * size + size // 4 + shift))
    else:
        screen.blit(iceberg, ((x1 // 2 + 1) * size + shift - size * 3 // 4, y1 * size - size // 4 + shift))

    if x2 % 2 == 0:
        screen.blit(iceberg, (x2 // 2 * size + shift - size // 4, y2 * size + size // 4 + shift))
    else:
        screen.blit(iceberg, ((x2 // 2 + 1) * size + shift - size * 3 // 4, y2 * size - size // 4 + shift))

    return x1, y1, x2, y2
