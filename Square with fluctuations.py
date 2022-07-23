import sys, pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((200, 200))
screen.fill('blue')
CLOCK  = pygame.time.Clock()

surface = pygame.Surface((50 , 50))
surface.fill((255, 0, 0))
rotated_surface = surface
rect = surface.get_rect()
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('blue')
    angle += 5
    rotated_surface = pygame.transform.rotate(surface, angle)
    rect = rotated_surface.get_rect(center = (100, 100))
    screen.blit(rotated_surface, (rect.x, rect.y))

    pygame.display.update()
    CLOCK.tick(30)
