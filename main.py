import pygame
from pygame.locals import *
from numpy import ceil, array
from Story import intro, lose, victory
from get_name import get_name
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
timerfont = pygame.font.Font('cyrillic_pixel-7.ttf', 30)


intro(screen, xres, yres)


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


def death(win):
    global done, icebergs, moves, steps
    pygame.time.wait(200)
    screen = pygame.display.set_mode((xres, yres))
    if win:
        victory(screen, xres, yres)
    else:
        lose(screen, xres, yres)
    write_name(get_name(), len(path))
    if time == 6 and steps == 66:
        snake()
    bg = pygame.image.load('menu_bg.png')
    bg = pygame.transform.scale(bg, (xres, yres))
    screen.blit(bg, (0, 0))
    moves_string = ''
    for i in range(len(moves)):
        moves_string += ','.join(map(str,
                                     ceil(array(moves[i])).astype(int))) + '->'
    moves_string += ','.join(map(str, ceil(array(moves[-1])).astype(int)))
    myfont = pygame.font.SysFont('Comic Sans MS', 25)
    for i in range(len(moves_string) // 50 + 1):
        current = moves_string[i * 50:min((i + 1) * 50, len(moves_string))]
        if i > 10:
            current += '...'
        screen.blit(myfont.render(current, False, (255, 255, 255)), (0, i * 25))
        end = i * 25
        if i > 10:
            break
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    end += 50
    screen.blit(myfont.render('Всего шагов: ' + str(steps), False,
                              (255, 255, 255)), (xres / 2 - 150, end))
    end += 50
    screen.blit(myfont.render('Нажмите любую клавишу чтобы продолжить', False,
                              (255, 255, 255)), (20, end))
    done = False
    while not done:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                done = True
    pygame.display.flip()
    mode = create_menu(screen, xres, yres, current_settings)
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
    if steps_limit == -1:
        screen.blit(timerfont.render('Шагов: ' + str(steps) +
                                     '/oo', False, (255, 255, 255)), (5, 5))
    else:
        screen.blit(timerfont.render('Шагов: ' + str(steps) +
                                     '/oo' + str(steps_limit), False, (255, 255, 255)), (5, 5))
    if time_limit == -1:
        screen.blit(timerfont.render('Время: ' + str(time) +
                                     '/oo', False, (255, 255, 255)), (5, 35))
    else:
        screen.blit(timerfont.render('Время: ' + str(time) + '/oo' +
                                     str(time_limit), False, (255, 255, 255)), (5, 35))
    pygame.display.flip()


def move_player(dest_x, dest_y, move_x, move_y):
    i = 0
    while i < 50:
        if i < 45:
            player.x = (dest_x - move_x) + i * move_x / 50
            player.y = (dest_y - move_y) + i * move_y / 50
            draw_all()
            pygame.display.flip()
            pygame.time.wait(1)
            i += 1
        else:
            player.x = (dest_x - move_x) + i * move_x / 50
            player.y = (dest_y - move_y) + i * move_y / 50
            draw_all()
            pygame.display.flip()
            pygame.time.wait(i - 45)
            i += 1
    player.x = dest_x
    player.y = dest_y


def write_name(name, score):
    arr = []
    try:
        inp = open('scores.txt', 'r')
        s = inp.readline().rstrip().split()
        while s:
            s[0] = int(s[0])
            arr.append(s)
            s = inp.readline().rstrip().split()
        inp.close()
    except:
        pass
    arr.append([score, name])
    arr.sort(reverse=True)
    out = open('scores.txt', 'w')
    for i in range(min(5, len(arr))):
        print(arr[i][0], arr[i][1], file=out)
    out.close()


mode = create_menu(screen, xres, yres)
done = True
if mode != -1:
    global moves, steps
    done = False
    moves = [[0, 0]]
    steps = 0
    start(mode)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                death(False)
            elif (event.key == pygame.K_w or event.key == pygame.K_a or
                  event.key == pygame.K_s or event.key == pygame.K_d or
                  event.key == pygame.K_UP or event.key == pygame.K_LEFT or
                  event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT):
                dir = get_dir(event.key)
                steps += 1
                last_x, last_y = player.x, player.y
                res = player.move(dir, icebergs)
                if res == 1:
                    pass
                elif res[-1] == 2:
                    move_player(res[0], res[1], res[2], res[3])
                    moves.append([player.x, player.y])
                    death(False)
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
                    enemies, alive = intelligence(enemies, player)
                    if not alive:
                        draw_all()
                        death(False)
                    if len(path) == width * (height + 1) + (width + 1) * height:
                        death(True)
                    if turn == 2:
                        turn = 0
                        icebergs = spawn_random(
                            width, height, screen, side, margin, icebergs_number)
                    moves.append([player.x, player.y])
                if steps > steps_limit and steps_limit != -1:
                    death(False)
                draw_all()
        elif event.type == USEREVENT:
            time += 1
            if time > time_limit and time_limit != -1:
                death(False)
            draw_all()
