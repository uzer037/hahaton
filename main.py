import pygame
from pygame.locals import *
from numpy import ceil, array
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
xres, yres = 700, 700
screen = pygame.display.set_mode((xres, yres))
myfont = pygame.font.SysFont('Comic Sans MS', 30)


def get_dir(key):
    if key == pygame.K_w or key == pygame.K_UP:
        return 0
    elif key == pygame.K_a or key == pygame.K_LEFT:
        return 1
    elif key == pygame.K_s or key == pygame.K_DOWN:
        return 2
    elif key == pygame.K_d or key == pygame.K_RIGHT:
        return 3


def start(settings):
    global width, height, path, player, turn, icebergs, enemies, steps, current_settings
    global moves, time, steps_limit, time_limit, icebergs_number, enemies_number
    current_settings = settings
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
    enemies_number = settings[5]
    icebergs = []
    enemies = create_enemies(
        screen, side, width, height, margin, enemies_number)
    steps_limit = settings[2]
    time_limit = settings[3]
    draw_all()
    pygame.time.set_timer(USEREVENT, 1000)


def death():
    pygame.time.wait(200)
    global done, icebergs, moves, steps
    if time == 6 and steps == 66:
        snake()
    moves_string = ''
    for i in range(len(moves)):
        moves_string += ','.join(map(str,
                                     ceil(array(moves[i])).astype(int))) + '->'
    moves_string += ','.join(map(str, ceil(array(moves[-1])).astype(int)))
    screen = pygame.display.set_mode((xres, yres))
    myfont = pygame.font.SysFont('Comic Sans MS', 25)
    for i in range(len(moves_string) // 50 + 1):
        current = moves_string[i * 50:min((i + 1) * 50, len(moves_string))]
        if i > 10:
            current += '...'
        screen.blit(myfont.render(current, False, (0, 255, 0)), (0, i * 25))
        end = i * 25
        if i > 10:
            break
    myfont=pygame.font.SysFont('Comic Sans MS', 30)
    end += 50
    screen.blit(myfont.render(str(steps), False, (0, 255, 0)), (xres / 2 - 100, end))
    pygame.display.flip()
    pygame.time.wait(5000)
    mode=create_menu(screen, xres, yres, current_settings)
    if mode == -1:
        done=True
    else:
        done=False
        icebergs=[]
        moves=[[0, 0]]
        steps=0
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
    i=0
    while i < 50:
        if i < 45:
            player.x=(dest_x - move_x) + i * move_x / 50
            player.y=(dest_y - move_y) + i * move_y / 50
            draw_all()
            pygame.display.flip()
            pygame.time.wait(1)
            i += 1
        else:
            player.x=(dest_x - move_x) + i * move_x / 50
            player.y=(dest_y - move_y) + i * move_y / 50
            draw_all()
            pygame.display.flip()
            pygame.time.wait(i - 45)
            i += 1
    player.x=dest_x
    player.y=dest_y


mode=create_menu(screen, xres, yres)
done=True
if mode != -1:
    global moves, steps
    done=False
    moves=[[0, 0]]
    steps=0
    start(mode)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                death()
            elif (event.key == pygame.K_w or event.key == pygame.K_a or
                  event.key == pygame.K_s or event.key == pygame.K_d or
                  event.key == pygame.K_UP or event.key == pygame.K_LEFT or
                  event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT):
                dir=get_dir(event.key)
                steps += 1
                last_x, last_y=player.x, player.y
                res=player.move(dir, icebergs)
                if res == 1:
                    pass
                elif res[-1] == 2:
                    move_player(res[0], res[1], res[2], res[3])
                    moves.append([player.x, player.y])
                    death()
                else:
                    turn += 1
                    move_player(res[0], res[1], res[2], res[3])
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
                    enemies, alive=intelligence(enemies, player)
                    if not alive:
                        draw_all()
                        death()
                    if len(path) == width * (height + 1) + (width + 1) * height:
                        start(current_settings)
                    if turn == 2:
                        turn=0
                        icebergs=spawn_random(
                            width, height, screen, side, margin, icebergs_number)
                    moves.append([player.x, player.y])
                if steps > steps_limit and steps_limit != -1:
                    death()
                draw_all()
        elif event.type == USEREVENT:
            time += 1
            if time > time_limit and time_limit != -1:
                death()
            draw_all()
