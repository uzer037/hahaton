from random import randrange
import pygame


def spawn(n, m, screen, size, shift):
    iceberg = pygame.image.load('iceberg.png')
    iceberg = pygame.transform.scale(iceberg, (size // 2, size // 2))
    x1, x2 = randrange(n), randrange(n)
    y1, y2 = randrange(m), randrange(m)
    if x1 == x2 and y1 == y2:
        if x1 > 0:
            x1 -= 1
        else:
            x1 += 1
    screen.blit(iceberg, (x1 * size + shift, y1 * size + size // 4 + shift))
    screen.blit(iceberg, (x2 * size + shift, y2 * size + size // 4 + shift))
    return x1, y1, x2, y2
