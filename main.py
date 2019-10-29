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
    global path, player, turn, icebergs, steps, moves
    path = set()
    if len(moves) > 1:
        for i in range(len(moves) - 1):
            print(','.join(map(str, moves[i])), end='->')
        print(','.join(map(str, moves[-1])))
    moves = [[0, 0]]
    icebergs = []
    player = Ship(screen, side, width, height, margin)
    turn = 0
    steps = 0
    draw_field(width + 2, height + 2, screen, side, path)
    player.draw()
    pygame.display.flip()


done = False
icebergs = []
moves = [[0, 0]]

t = pygame.time.get_ticks()
steps = 0
start()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif (event.key == pygame.K_w or event.key == pygame.K_a or
                  event.key == pygame.K_s or event.key == pygame.K_d):
                dir = get_dir(event.key)
                steps += 1
                last_x, last_y = player.x, player.y
                res = player.move(dir, icebergs)
                if res == 2:
                    start()
                elif res == 1:
                    draw_field(width + 2, height + 2, screen, side, path)
                    player.draw()
                    spawn(width, height, screen, side, margin, icebergs)
                    screen.blit(myfont.render(str(steps), False, (255, 255, 255)), (0, 0))
                    pygame.display.flip()
                else:
                    turn += 1
                    if dir == 0:
                        path.add((90, ((last_x + 1) * side, last_y * side)))
                    elif dir == 1:
                        path.add((0, (last_x * side, (last_y + 1) * side)))
                    elif dir == 2:
                        path.add((90, ((last_x + 1) * side, (last_y + 1) * side)))
                    else:
                        path.add((0, ((last_x + 1) * side, (last_y + 1) * side)))

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
                    moves.append([player.x, player.y])
                    screen.blit(myfont.render(str(steps), False, (255, 255, 255)), (0, 0))
                    pygame.display.flip()

    t = pygame.time.get_ticks()
