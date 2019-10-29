import pygame
import random


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
speedx = 1
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
    if pressed[pygame.K_LEFT] and speedx != 1:
        speedx = -1
        speedy = 0
    elif pressed[pygame.K_RIGHT] and speedx != -1:
        speedx = 1
        speedy = 0
    elif pressed[pygame.K_UP] and speedy != 1:
        speedx = 0
        speedy = -1
    elif pressed[pygame.K_DOWN] and speedy != -1:
        speedx = 0
        speedy = 1

    snake.insert(0, [snake[0][0] + speedx, snake[0][1] + speedy])
    if snake[0] == apple:
        apple = makeapple(snake)
    else:
        # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(apple[0] * 10, apple[1] * 10, 10, 10))
        screen.blit(apple_surface, (apple[0] * 10, apple[1] * 10))
        snake.pop(-1)

    if 0 > snake[0][0] or snake[0][0] > 49:
        snake = [[25, 25], [24, 25], [23, 25]]
    if 0 > snake[0][1] or snake[0][1] > 49:
        snake = [[25, 25], [24, 25], [23, 25]]

    for i in range(1, len(snake)):
        if snake[0] == snake[i]:
            snake = [[25, 25], [24, 25], [23, 25]]
            break

    pygame.display.flip()
    clock.tick(15)
