from random import randrange
import pygame


def draw_field(width, height, screen, size):
    water = pygame.image.load('water.png').convert_alpha()
    water = pygame.transform.scale(water, (size, size))
    pos = [(water, (size * (j % width), size * (j // width))) for j in range(width * height)]
    screen.blits(pos)


def spawn_random(width, height, screen, size, shift, n):
    coords = []
    for i in range(n):
        x = randrange(2 * width + 1)
        if x % 2 == 0:
            y = randrange(height)
        else:
            y = randrange(height + 1)

        match = False
        while not match:
            match = True
            for j in coords:
                while x == j[0] and y == j[0]:
                    x = randrange(2 * width + 1)
                    if x % 2 == 0:
                        y = randrange(height)
                    else:
                        y = randrange(height + 1)
                    match = False

        coords.append([x, y])

    spawn(width, height, screen, size, shift, coords)
    return coords


def spawn(width, height, screen, size, shift, coords):
    iceberg = pygame.image.load('iceberg.png').convert_alpha()
    iceberg = pygame.transform.scale(iceberg, (size, size))
    for i in coords:
        if i[0] % 2 == 0:
            screen.blit(iceberg, (i[0] // 2 * size + shift - size // 2, (i[1] - 1) * size + shift))
        else:
            screen.blit(iceberg, (i[0] // 2 * size + shift, i[1] * size + shift - size // 2))
