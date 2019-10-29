import pygame
from Icebergs import spawn, draw_field
from ship import Ship

pygame.init()
width, height = 10, 3
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
    draw_field(width + 2, height + 2, screen, side)
    global player, turn
    player = Ship(screen, side, width, height, margin)
    turn = 0
    pygame.display.flip()


start()

done = False
icebergs = [-1] * 4
while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif (event.key == pygame.K_w or event.key == pygame.K_a or
                  event.key == pygame.K_s or event.key == pygame.K_d):
                dir = get_dir(event.key)
                res = player.move(dir, (icebergs[0], icebergs[2]), (icebergs[1], icebergs[3]))
                if res == 2:
                    start()
                elif res == 1:
                    pass
                else:
                    turn += 1
                    if turn == 2:
                        turn = 0
                        draw_field(width + 2, height + 2, screen, side)
                        player.draw()
                        icebergs = spawn(width, height, screen, side, margin)
                    pygame.display.flip()
