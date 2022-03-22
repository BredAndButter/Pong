import pygame, sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((700, 600), 0, 32)
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
x = 700 / 2
y = 600 / 2
paddlelefty = 20
paddlerighty = 20
dx = 1
dy = -4
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        paddlelefty -= 5
    if keys[pygame.K_z]:
        paddlelefty += 5
    if keys[pygame.K_k]:
        paddlerighty -= 5
    if keys[pygame.K_m]:
        paddlerighty += 5
    if x < 0:
        x = 700 / 2
        y = 600 / 2
    if x > 700 - 15:
        x = 700 / 2
        y = 600 / 2
    if paddlelefty < 0:
        paddlelefty = 0
    if paddlelefty > 500:
        paddlelefty = 500
    if paddlerighty < 0:
        paddlerighty = 0
    if paddlerighty > 500:
        paddlerighty = 500
    screen.fill((0, 0, 0))
    puck = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x, y, 15, 15))
    paddleleft = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(20, paddlelefty, 20, 100))
    paddleright = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(660, paddlerighty, 20, 100))
    x += dx
    y += dy
    if y < 0:
        dy = -dy
    if y > 600-15:
        dy = -dy
    if x < 40 and x > 20 and y < paddlelefty+100 and y > paddlelefty:
        dx = -dx
    if x < 680-15 and x > 660-15 and y < paddlerighty+100 and y > paddlerighty:
        dx = -dx
    pygame.display.update()
    clock.tick(60)
