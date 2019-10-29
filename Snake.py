import pygame
import random


def snake():
    def makeapple(arr):
        apple = [random.randrange(0, 50), random.randrange(0, 50)]

        same = False
        for i in arr:
            if i == apple:
                same = True

        if same:
            apple = makeapple(arr)
        return apple


    x1 = 500
    y1 = 500
    pygame.init()
    screen = pygame.display.set_mode((x1, y1))

    snake = [[25, 25], [24, 25], [23, 25]]
    apple = makeapple(snake)
    apple_surface = pygame.transform.scale(pygame.image.load('iceberg.png'), (10, 10))
    speedx = 0
    speedy = 0

    done = False
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill((0, 0, 0))

        for i in snake:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(i[0] * 10, i[1] * 10, 10, 10), 1)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a] and speedx != 1:
            speedx = -1
            speedy = 0
        elif pressed[pygame.K_d] and speedx != -1:
            speedx = 1
            speedy = 0
        elif pressed[pygame.K_w] and speedy != 1:
            speedx = 0
            speedy = -1
        elif pressed[pygame.K_s] and speedy != -1:
            speedx = 0
            speedy = 1

        snake.insert(0, [snake[0][0] + speedx, snake[0][1] + speedy])
        if snake[0] == apple:
            apple = makeapple(snake)
        else:
            screen.blit(apple_surface, (apple[0] * 10, apple[1] * 10))
            snake.pop(-1)

        if 0 > snake[0][0] or snake[0][0] > 49:
            done = True
        if 0 > snake[0][1] or snake[0][1] > 49:
            done = True

        for i in range(1, len(snake)):
            if snake[0] == snake[i] and (speedx or speedy):
                done = True

        pygame.display.flip()
        clock.tick(15)