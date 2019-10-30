import pygame


def render_text(screen, arr, myfont, xres, yres):
    pygame.init()
    screen.fill(0x0)
    pygame.mixer.music.load('317448__cornersting__poke1.mp3')

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for event in pygame.event.get():
                if event.type == event.type == pygame.KEYDOWN:
                    break
            pygame.mixer.music.play()
            screen.blit(myfont.render(arr[i][:j + 1], False, (255, 255, 255)), (xres // 24, yres // 24 * (i + 1)))
            pygame.display.flip()
            pygame.time.wait(50)
        pygame.time.wait(200)


def intro(screen, xres, yres):
    myfont = pygame.font.SysFont('Comic Sans MS', xres // 24)
    arr = ["One day, after decades",
           "of gathering and improving it's knowledge,",
           "humanity realised something.",
           "It has realised that it's not alone.",
           "It has realised that there are things, which",
           "can't be comprehended.",
           "And so, it began to think how to deal with",
           "such matters.",
           "After deep investigation, it was able to",
           "find the root of their problem.",
           "The root of their problem was at north pole.",
           "Because of this, you were sent there on the most",
           "technologically advanced ship of this time",
           "to put and end to this.",
           "Are you prepared to meet things that will",
           "lie there?"]
    render_text(screen, arr, myfont, xres, yres)


def victory(screen, xres, yres):
    myfont = pygame.font.SysFont('Comic Sans MS', xres // 24)
    arr = ["You won, congratulations."]
    render_text(screen, arr, myfont, xres, yres)


def lose(screen, xres, yres):
    myfont = pygame.font.SysFont('Comic Sans MS', xres // 24)
    arr = ["You were unable to solve",
           "the mysteries that lie beyond."]
    render_text(screen, arr, myfont, xres, yres)


# intro(pygame.display.set_mode((500, 500)), 500, 500)
