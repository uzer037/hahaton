from random import randrange
import pygame


class Enemy:
    def __init__(self, screen, x, y, side, width, height, margin):
        self.screen = screen
        self.side = side
        self.width = width
        self.height = height
        self.margin = margin
        self.x = x
        self.y = y
        pic = pygame.image.load('iceberg.png').convert_alpha()
        self.picture = pygame.transform.scale(pic, (side // 2, side // 2))
        screen.blit(self.picture, (margin - side // 4, margin - side // 4))

    def draw(self):
        self.screen.blit(self.picture, (self.margin + self.side * self.x - self.side // 4,
                               self.margin + self.side * self.y - self.side // 4))


def intelligence(enemy_list, player):
    alive = True
    for i in range(len(enemy_list)):
        diffx = enemy_list[i].x - player.x
        diffy = enemy_list[i].y - player.y

        if abs(diffx) > abs(diffy):
            if diffx < 0:
                enemy_list[i].x += 1
            else:
                enemy_list[i].x -= 1
        else:
            if diffy < 0:
                enemy_list[i].y += 1
            else:
                enemy_list[i].y -= 1

        if diffx == diffy == 0:
            alive = False

    return enemy_list, alive


def draw_enemies(enemy_list):
    for i in enemy_list:
        i.draw()


def create_enemies(screen, size, width, height, shift, n):
    enemy_list = []
    for i in range(n):
        x = randrange(1, width)
        y = randrange(1, height)

        match = False
        while not match:
            match = True
            for j in enemy_list:
                while x == j.x and y == j.y:
                    x = randrange(width)
                    y = randrange(height)
                    match = False

        enemy_list.append(Enemy(screen, x, y, size, width, height, shift))
    return enemy_list
