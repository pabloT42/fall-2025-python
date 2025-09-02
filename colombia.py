import pygame; #bring in this module
pygame.init() #get it ready to use
screen =pygame.display.set_mode((900,600)); #create game screen
pygame.display.set_caption("Colombia") #set screen window title

img1=pygame.transform.smoothscale(pygame.image.load("colombia.png").convert_alpha(),(240,180)) #load picture
img2=pygame.transform.smoothscale(pygame.image.load("colombiayum1.jpg").convert_alpha(),(240,180)) #load picture
img3=pygame.transform.smoothscale(pygame.image.load("colombiaforest.jpg").convert_alpha(),(240,180)) #load picture

pygame.mixer.music.load("colombia.ogg"); #load music
pygame.mixer.music.play(-1) #start playing music

font1=pygame.font.SysFont("arial",48,True); #choose font
text1=font1.render("Colombia",True,(255,255,255)); #say what to print to screen

text2=font1.render("Libertad y Orden",True,(255,255,255)); #say what to print to screen

screen.fill((0,0,0)) #background color for screen

pygame.draw.rect(screen,(252,209,22),(440,40,420,260)) #yellow stripe
pygame.draw.rect(screen,(0,56,147),(440, 180, 420,110)) #blue stripe
pygame.draw.rect(screen,(206,17,38),(440, 260, 420,80)) #red stripe


screen.blit(img1,(40,360)); #draw jpg

screen.blit(img2,(340,360)); #draw jpg

screen.blit(img3,(640,360)); #draw jpg 

screen.blit(text1,(40,20)); #draw text

screen.blit(text2,(40,60)); #draw text

pygame.display.flip() #display all images on screen
