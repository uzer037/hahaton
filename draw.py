import pygame


def draw_field(width, height, screen, size, path):
    water = pygame.image.load('water.png').convert_alpha()
    water = pygame.transform.scale(water, (size, size))
    pos = [(water, (size * (j % width), size * (j // width))) for j in range(width * height)]
    screen.blits(pos)

    pic = pygame.image.load('check_line.png').convert_alpha()
    pic = pygame.transform.scale(pic, (size, size))
    path = list(path)
    print(len(path))
    path = [(pygame.transform.rotate(pic, path[i][0]), (path[i][1][0] - 1, path[i][1][1] - 2)) for i in range(len(path))]
    screen.blits(path)
