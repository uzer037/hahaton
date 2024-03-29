import pygame


class Ship:
    def __init__(self, screen, x, y, side, width, height, margin):
        self.screen = screen
        self.side = side
        self.width = width
        self.height = height
        self.margin = margin
        self.dir = 3
        self.picture = 'ship_right.png'
        self.x = x
        self.y = y
        pic = pygame.image.load(self.picture).convert_alpha()
        pic = pygame.transform.scale(pic, (3 * side // 4, 3 * side // 4))
        screen.blit(pic, (margin - 3 * side // 8, margin - 3 * side // 8))

    def draw(self):
        pic = pygame.image.load(self.picture).convert_alpha()
        pic = pygame.transform.scale(
            pic, (3 * self.side // 4, 3 * self.side // 4))
        self.screen.blit(pic, (self.margin + int(self.side * self.x) - 3 * self.side // 8,
                               self.margin + int(self.side * self.y) - 3 * self.side // 8))

    def move(self, dir, icebergs):
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
        dest_x = self.x + move_x
        dest_y = self.y + move_y
        if dest_x < 0 or dest_x > self.width or dest_y < 0 or dest_y > self.height:
            return 1
        for iceberg in icebergs:
            if (move_y == 0 and self.y == iceberg[1] and
                2 * min(self.x, dest_x) == iceberg[0] - 1 or
                move_x == 0 and 2 * self.x == iceberg[0] and
                    min(self.y, dest_y) == iceberg[1]):
                return (dest_x - 2 * move_x / 3, dest_y - 2 * move_y / 3, move_x / 3, move_y / 3, 2)
        return (dest_x, dest_y, move_x, move_y, 0)
