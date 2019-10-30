import pygame
from pygame.locals import *
from menu import create as create_menu, settings
from enemies import draw_enemies, create_enemies, intelligence
from Snake import snake
from draw import draw_field
from ship import Ship
from icebergs import spawn, spawn_random

pygame.init()
width, height = 5, 2
side, thickness = 100, 1
margin = side
xres, yres = 500, 500
screen = pygame.display.set_mode((xres, yres))
myfont = pygame.font.SysFont('Comic Sans MS', 30)


def get_dir(key):
    if key == pygame.K_w:
        return 0
    elif key == pygame.K_a:
        return 1
    elif key == pygame.K_s:
        return 2
    elif key == pygame.K_d:
        return 3


def start(settings):
    global width, height, path, player, turn, icebergs, enemies, steps
    global moves, time, steps_limit, time_limit, icebergs_number, enemies_number
    width = settings[0]
    height = settings[1]
    xres, yres = width * side + 2 * margin, height * side + 2 * margin
    screen = pygame.display.set_mode((xres, yres))
    path = set()
    moves = [[0, 0]]
    player = Ship(screen, 0, 0, side, width, height, margin)
    turn = 0
    steps = 0
    time = 0
    icebergs_number = settings[4]
    enemies_number = 0
    icebergs = []
    enemies = create_enemies(
        screen, side, width, height, margin, enemies_number)
    steps_limit = settings[2]
    time_limit = settings[3]
    draw_all()
    pygame.time.set_timer(USEREVENT, 1000)


def death():
    global done, icebergs, moves, steps
    if time == 6 and steps == 66:
        snake()
    with open('output.txt', 'w') as file:
        for i in range(len(moves) - 1):
            file.write(','.join(map(str, moves[i])) + '->')
        file.write(','.join(map(str, moves[-1])))
        file.write('\n' + str(steps))
    xres, yres = 500, 500
    screen = pygame.display.set_mode((xres, yres))
    mode = create_menu(screen, 500, 500)
    if mode == -1:
        done = True
    else:
        done = False
        icebergs = []
        moves = [[0, 0]]
        steps = 0
        start(mode)


def draw_all():
    draw_field(width + 2, height + 2, screen, side, path)
    player.draw()
    draw_enemies(enemies)
    spawn(width, height, screen, side, margin, icebergs)
    screen.blit(myfont.render(str(steps), False, (255, 255, 255)), (0, 0))
    screen.blit(myfont.render(str(time), False, (255, 255, 255)), (0, 30))
    pygame.display.flip()


def move_player(dest_x, dest_y, move_x, move_y):
    i = 0
    while i < 100:
        if i < 5:
            player.x = (dest_x - move_x) + i * move_x / 100
            player.y = (dest_y - move_y) + i * move_y / 100
            draw_all()
            pygame.display.flip()
            pygame.time.wait(5 - i)
            i += 1
        elif i < 80:
            player.x = (dest_x - move_x) + i * move_x / 100
            player.y = (dest_y - move_y) + i * move_y / 100
            draw_all()
            pygame.display.flip()
            pygame.time.wait(1)
            i += 1
        else:
            player.x = (dest_x - move_x) + i * move_x / 100
            player.y = (dest_y - move_y) + i * move_y / 100
            draw_all()
            pygame.display.flip()
            pygame.time.wait(i - 80)
            i += 1
    player.x = dest_x
    player.y = dest_y


mode = create_menu(screen, 500, 500)
done = True
if mode != -1:
    global icebergs, moves, steps
    done = False
    icebergs = []
    moves = [[0, 0]]
    steps = 0
    start(mode)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                death()
            elif (event.key == pygame.K_w or event.key == pygame.K_a or
                  event.key == pygame.K_s or event.key == pygame.K_d):
                dir = get_dir(event.key)
                steps += 1
                last_x, last_y = player.x, player.y
                res = player.move(dir, icebergs)
                if res == 2:
                    death()
                elif res == 1:
                    pass
                else:
                    turn += 1
                    enemies, alive = intelligence(enemies, player)
                    if not alive:
                        death()
                    move_player(res[0], res[1], res[2], res[3])
                    moves.append([player.x, player.y])
                    if dir == 0:
                        path.add((90, ((last_x + 1) * side, last_y * side)))
                    elif dir == 1:
                        path.add((0, (last_x * side, (last_y + 1) * side)))
                    elif dir == 2:
                        path.add(
                            (90, ((last_x + 1) * side, (last_y + 1) * side)))
                    else:
                        path.add(
                            (0, ((last_x + 1) * side, (last_y + 1) * side)))
                    if len(path) == width * (height + 1) + (width + 1) * height:
                        start()
                    if turn == 2:
                        turn = 0
                        icebergs = spawn_random(
                            width, height, screen, side, margin, icebergs_number)
                if steps > steps_limit and steps_limit != -1:
                    death()
                draw_all()
        elif event.type == USEREVENT:
            time += 1
            if time > time_limit and time_limit != -1:
                death()
            draw_all()
