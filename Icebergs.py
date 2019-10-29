from random import randrange
import pygame


def spawn(n, m, screen, size):
    iceberg = pygame.image.load('iceberg.png')
    iceberg = pygame.transform.scale(iceberg, (size // 3, size // 3))
    x1, x2 = randrange(n), randrange(n)
    y1, y2 = randrange(m), randrange(m)
    if x1 == x2 and y1 == y2:
        if x1 > 0:
            x1 -= 1
        else:
            x1 += 1
    screen.blit(iceberg, (x1 * size, y1 * size + size // 3))
    screen.blit(iceberg, (x2 * size, y2 * size + size // 3))
