import pygame


def get_name():
    xres, yres = 700, 700
    screen = pygame.display.set_mode((xres, yres))
    myfont = pygame.font.Font('cyrillic_pixel-7.ttf', 30)
    bg = pygame.image.load('menu_bg.png')
    bg = pygame.transform.scale(bg, (xres, yres))
    screen.blit(bg, (0, 0))

    screen.blit(myfont.render('Введите имя:', False, (255, 255, 255)), (10, 10))
    name = ''
    done = False
    while not done:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == 13:
                    done = True
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                    screen.blit(bg, (0, 0))
                    screen.blit(myfont.render('Введите имя:',
                                              False, (255, 255, 255)), (10, 10))
                    screen.blit(myfont.render(
                        name, False, (255, 255, 255)), (230, 10))
                elif len(name) < 15:
                    name += chr(event.key)
                    screen.blit(myfont.render(
                        name, False, (255, 255, 255)), (230, 10))
    return name
