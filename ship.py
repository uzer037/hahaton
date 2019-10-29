import pygame


class Ship:
    def __init__(self, screen, side, width, height, margin):
        self.screen = screen
        self.side = side
        self.width = width
        self.height = height
        self.margin = margin
        self.dir = 3
        self.picture = 'ship_right.png'
        pic = pygame.image.load('ship_right.png').convert_alpha()
        pic = pygame.transform.scale(pic, (side // 2, side // 2))
        screen.blit(pic, (margin, margin))

    def draw(self, x, y):
        if self.dir == 0:
            pic = pygame.image.load(self.picture).convert_alpha()
            pic = pygame.transform.scale(pic, (self.side // 2, self.side // 2))
            self.screen.blit(pic, (self.margin + self.side * x, self.margin + self.side * y))

    def move(self, dir, start_x, start_y, icebergs_x, icebergs_y):
        self.dir = dir
        if dir == 0:
            move_x = 0
            move_y = -1
            self.picture = 'ship_up.png'
        elif dir == 1:
            move_x = -1
            move_y = 0
            self.picture = 'ship_left.png'
        elif dir == 2:
            move_x = 0
            move_y = 1
            self.picture = 'ship_down.png'
        else:
            move_x = 1
            move_y = 0
            self.picture = 'ship_right.png'
        dest_x = start_x + move_x
        dest_y = start_y + move_y
        if dest_x < 0 or dest_x > self.width or dest_y < 0 or dest_y > self.height:
            self.draw(start_x, start_y)
            return 1
        elif (move_y == 0 and 2 * start_y == icebergs_y[0] and
              2 * min(start_x, dest_x) == icebergs_x[0] - 1 or
              move_x == 0 and 2 * start_x == icebergs_x[0] and
              2 * min(start_y, dest_y) == icebergs_y[0] - 1
              or
              move_y == 0 and 2 * start_y == icebergs_y[0] and
              2 * min(start_x, dest_x) == icebergs_x[0] - 1 or
              move_x == 0 and 2 * start_x == icebergs_x[0] and
              2 * min(start_y, dest_y) == icebergs_y[0] - 1):
            return 2
        else:
            self.draw(dest_x, dest_y)
            return 0