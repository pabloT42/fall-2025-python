import pygame
import random
import math

#boilerplate code
pygame.init()
gamescreen = pygame.display.set_mode((900,900))
pygame.display.set_caption("single particle movement")
clock = pygame.time.Clock()

#particle setup
xpos = [] #positions of the particles
ypos = []
xvel = [] # velocity of particles
yvel = []
speed = 2
ticker = [0] #useless



#game loop-----------------------------------------------------------------
while True:
    clock.tick(60)
    
    
    #create new particles--------------------------------------------------
    for i in range(100):
        if len(xpos) < 1000:
            
            #random velocities
            velx = random.uniform(-1,1)
            vely = random.uniform(-1,1)
    
    #calculate magnitude of velocity vector
            magnitude = math.sqrt(velx**2 + vely**2)
    
    #normlize velocity vector to have constant speed
            if magnitude != 0:
                normalizevelx = speed * velx / magnitude
                normalizevely = speed * vely / magnitude
            else:
                normalizevelx = 0
                normalizevely = 0
        
            xpos.append(450)
            ypos.append(450)
            xvel.append(normalizevelx)
            yvel.append(normalizevely)
    
    #event handling--------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        
    #physics---------------------------------------------------------------
    for i in range(100):
     #update position
        xpos[i] += xvel[i]
        ypos[i] += yvel[i]
    
    #boundary checking
        if xpos[i] < 0 or xpos[i] > 900 or ypos[i] < 0 or ypos[i] > 900:
            xpos[i] = 450 
            ypos[i] = 450
            
            #random velocities
            velx = random.uniform(-1,1)
            vely = random.uniform(-1,1)
    
    #calculate magnitude of velocity vector
            magnitude = math.sqrt(velx**2 + vely**2)
    
    #normlize velocity vector to have constant speed
            if magnitude != 0:
                normalizevelx = speed * velx / magnitude
                normalizevely = speed * vely / magnitude
            else:
                normalizevelx = 0
                normalizevely = 0
        
    #render section-------------------------------------------------------
    gamescreen.fill((0,0,0))
    for i in range(100):
        pygame.draw.circle(gamescreen, (255,255,255), (xpos[i], ypos[i]), 5)
    pygame.display.flip()
    
    
#end of game loop---------------------------------------------------------
pygame.quit()
