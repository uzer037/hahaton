import pygame


def play(screen, xres, yres):
    pygame.init()
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
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            pygame.event.get()
            screen.blit(myfont.render(arr[i][:j + 1], False, (255, 255, 255)), (xres // 24, xres // 24 * (i + 1)))
            pygame.display.flip()
            pygame.time.wait(100)
        pygame.time.wait(100)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True


# play(pygame.display.set_mode((500, 500)), 500, 500)
