import pygame
from pygame.locals import *
from enemies import draw_enemies, create_enemies, intelligence
from Snake import snake
from draw import draw_field
from ship import Ship
from icebergs import spawn, spawn_random

pygame.init()
width, height = 5, 2
side, thickness = 100, 1
margin = side
xres, yres = width * side + 2 * margin, height * side + 2 * margin
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


def start():
    xres, yres = width * side + 2 * margin, height * side + 2 * margin
    screen = pygame.display.set_mode((xres, yres))
    global path, player, turn, icebergs, enemies, steps, moves, time, steps_limit, time_limit, icebergs_number, enemies_number
    path = set()
    moves = [[0, 0]]
    player = Ship(screen, 0, 0, side, width, height, margin)
    turn = 0
    steps = 0
    time = 0
    icebergs_number = 5
    enemies_number = 1
    icebergs = []
    enemies = create_enemies(screen, side, width, height, margin, enemies_number)
    steps_limit = 70
    time_limit = -1
    draw_all()
    pygame.time.set_timer(USEREVENT, 1000)


def death():
    if time == 6 and steps == 66:
        snake()
    with open('output.txt', 'w') as file:
        for i in range(len(moves) - 1):
            file.write(','.join(map(str, moves[i])) + '->')
        file.write(','.join(map(str, moves[-1])))
        file.write('\n' + str(steps))
    start()


def draw_all(draw_player = True):
    draw_field(width + 2, height + 2, screen, side, path)
    if draw_player:
        player.draw()
    draw_enemies(enemies)
    spawn(width, height, screen, side, margin, icebergs)
    screen.blit(myfont.render(str(steps), False, (255, 255, 255)), (0, 0))
    screen.blit(myfont.render(str(time), False, (255, 255, 255)), (0, 30))
    pygame.display.flip()


done = False
icebergs = []
moves = [[0, 0]]

steps = 0
start()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif (event.key == pygame.K_w or event.key == pygame.K_a or
                  event.key == pygame.K_s or event.key == pygame.K_d):
                draw_all(False)
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

                    if turn == 2:
                        turn = 0
                        icebergs = spawn_random(
                            width, height, screen, side, margin, icebergs_number)

                    if len(path) == width * (height + 1) + (width + 1) * height:
                        start()
                    moves.append([player.x, player.y])
                    enemies, alive = intelligence(enemies, player)
                    if not alive:
                        print(1)
                        death()
                if steps > steps_limit:
                    death()
                draw_all()
        elif event.type == USEREVENT:
            time += 1
            if time > time_limit and time_limit != -1:
                death()
            draw_all()
