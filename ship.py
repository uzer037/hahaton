import pygame


class Ship:
    def __init__(self, screen, side, width, height):
        self.screen = screen
        self.side = side
        self.width = width
        self.height = height
         = pygame.image.load('iceberg.png')
         = pygame.transform.scale(iceberg, (size // 2, size // 2))
        screen.blit(, (x1 * size + shift, y1 * size + size // 4 + shift))
        screen.blit(iceberg, (x2 * size + shift, y2 * size + size // 4 + shift))
    def __move__(dir, start_x, start_y, icebergs_x, icebergs_y):
