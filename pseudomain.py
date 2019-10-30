import pygame
import menu
pygame.init()
xsz = 500
ysz = 500
screen = pygame.display.set_mode((xsz,ysz))
menu.create(screen, xsz, ysz)
done = False
while(not done):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            quit()

