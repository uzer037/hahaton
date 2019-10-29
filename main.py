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
    global path, player, turn, icebergs
    path = set()
    icebergs = []
    player = Ship(screen, side, width, height, margin)
    turn = 0
    draw_field(width + 2, height + 2, screen, side, path)
    player.draw()
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
                    if dir == 0:
                        path.add((90, (last_x * side, last_y * side)))
                    elif dir == 1:
                        path.add((180, (last_x * side, last_y * side)))
                    elif dir == 2:
                        path.add((90, (last_x * side, (last_y + 1) * side)))
                    else:
                        path.add((180, ((last_x + 1) * side, last_y * side)))

                    draw_field(width + 2, height + 2, screen, side, path)
                    player.draw()
                    if turn == 2:
                        turn = 0
                        icebergs = spawn_random(
                            width, height, screen, side, margin, 5)
                    else:
                        spawn(width, height, screen, side, margin, icebergs)

                    if len(path) == width * (height + 1) + (width + 1) * height:
                        start()
                    pygame.display.flip()
