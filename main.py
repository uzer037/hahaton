import pygame
from draw import draw_field
from ship import Ship
from icebergs import spawn, spawn_random

pygame.init()
width, height = 5, 2
side, thickness = 100, 1
margin = side
xres, yres = width * side + 2 * margin, height * side + 2 * margin
screen = pygame.display.set_mode((xres, yres))


def get_dir(key):
    if key == pygame.K_w:
        return 0
    elif key == pygame.K_a:
        return 1
    elif key == pygame.K_s:
        return 2
    elif key == pygame.K_d:
        return 3


def start():
    global path
    path = set()
    draw_field(width + 2, height + 2, screen, side, path)
    global player, turn
    player = Ship(screen, side, width, height, margin)
    turn = 0
    pygame.display.flip()


done = False
icebergs = []

start()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif (event.key == pygame.K_w or event.key == pygame.K_a or
                  event.key == pygame.K_s or event.key == pygame.K_d):
                dir = get_dir(event.key)
                last_x, last_y = player.x, player.y
                res = player.move(dir, icebergs)
                if res == 2:
                    start()
                elif res == 1:
                    draw_field(width + 2, height + 2, screen, side, path)
                    player.draw()
                    spawn(width, height, screen, side, margin, icebergs)
                    pygame.display.flip()
                else:
                    turn += 1
                    if dir == 0 or dir == 2:
                        path.add((2 * last_x + 1, 2 * max(last_y, player.y)))
                    else:
                        path.add((2 * max(last_x, player.x), 2 * last_y + 1))
                    draw_field(width + 2, height + 2, screen, side, path)
                    player.draw()
                    if turn == 2:
                        turn = 0
                        icebergs = spawn_random(
                            width, height, screen, side, margin, 2)
                    else:
                        spawn(width, height, screen, side, margin, icebergs)
                    pygame.display.flip()
