from ship import Ship
from random import randrange


def intelligence(enemy_list, player):
    for i in enemy_list:



def create_enemies(screen, size, width, height, shift):
    n = 1
    enemy_list = []
    for i in range(n):
        x = randrange(2 * width + 1)
        if x % 2 == 0:
            y = randrange(height)
        else:
            y = randrange(height + 1)

        match = False
        while not match:
            match = True
            for j in enemy_list:
                while x == j.x and y == j.y:
                    x = randrange(2 * width + 1)
                    if x % 2 == 0:
                        y = randrange(height)
                    else:
                        y = randrange(height + 1)
                    match = False

        enemy_list.append(Ship(screen, x, y, size, width, height, shift))
    return enemy_list
