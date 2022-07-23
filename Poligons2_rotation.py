import pygame,sys,math
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
radius=50
timer=pygame.time.Clock()
screen.fill('violet')
numSides=4
tiltAngle=0  #degrees
tiltAngle=tiltAngle*3.14159/180
x=400
y=400
radius=100
radius1=100
screen.fill('violet')

x0,y0=600,400
    
    
keep_going=True
while keep_going: # the main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('violet')
    tiltAngle=tiltAngle+10*3.14159/180
    
    pts = []
    for i in range(numSides):
        x = x + radius * math.cos(tiltAngle + math.pi * 2 * i / numSides)
        y = y + radius1 * math.sin(tiltAngle + math.pi * 2 * i / numSides)

        #x = x0 + radius * math.cos(tiltAngle + math.pi * 2 * i / numSides)
        #y = y0 + radius1 * math.sin(tiltAngle + math.pi * 2 * i / numSides)
        
        pts.append([int(x), int(y)])
    
    pygame.draw.polygon(screen, 'brown', pts)
    pygame.display.update()
    timer.tick(10)


#x=x+(x-x0)*math.cos(tiltAngle + math.pi * 2 * i / numSides)-(y-y0)*math.sin(tiltAngle + math.pi * 2 * i / numSides)
#y=y+(x-x0)*math.sin(tiltAngle + math.pi * 2 * i / numSides)+(y-y0)*math.cos(tiltAngle + math.pi * 2 * i / numSides)



