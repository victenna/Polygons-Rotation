import pygame,sys
import math as m
from pygame.locals import *
pygame.init()
size = [900, 900]
screen = pygame.display.set_mode(size)
keep_going=True
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)
PURPLE=(128,0,128)
LIME=(0,255,0)
GREY=(128,128,18)
TEAL=(0,128,128)
x0,y0=400,400
radius=50
timer=pygame.time.Clock()
screen.fill('violet')
r=200
teta=0
#teta=36*m.pi/180
keep_going=True
while keep_going: # the main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('violet')
    teta=teta+m.pi/180
    x1=int(r * m.cos( m.pi / 10+teta))
    y1=int(r * m.sin( m.pi / 10+teta))
    Point1=(x0+x1,y0+y1)

    x2=int(r * m.cos( 5*m.pi / 10+teta))
    y2=int(r * m.sin(5*m.pi / 10+teta))
    Point3=(x0+x2,y0+y2)

    x3=int(r * m.cos( 9*m.pi / 10+teta))
    y3=int(r * m.sin(9*m.pi / 10+teta))
    Point5=(x0+x3,y0+y3)

    x4=int(r * m.cos( 13*m.pi / 10+teta))
    y4=int(r * m.sin(13*m.pi / 10+teta))
    Point2=(x0+x4,y0+y4)

    x5=int(r * m.cos( 17*m.pi / 10+teta))
    y5=int(r * m.sin(17*m.pi / 10+teta))
    Point4=(x0+x5,y0+y5)

       
    #-------------------------------------------------------------------------


    Width=5
    pygame.draw.lines(screen, BLUE, True,[Point1,Point2,Point3,Point4,\
                                          Point5],Width)     #   LINE 2
    
    #-----------------------------------------------------------------------
    pygame.display.update()
    timer.tick(50)
