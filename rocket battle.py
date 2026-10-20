import pygame
from pygame.locals import*
from time import*

pygame.init()
screen=pygame.display.set_mode((600,600))
player_x=200
player_y=200
player=pygame.image.load("fuse.jpg")
background=pygame.image.load("espace.jpg")
while player_y <600:
    screen.blit(background,(0,0))
    screen.blit(player,(player_x,player_y))
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_UP:
                player_y-=50
            if event.key==K_DOWN:
                player_y+=50
            if event.key==K_RIGHT:
                player_x+=50
            if event.key==K_LEFT:
                player_x-=50
    player_y+=5
    sleep(0.05) 

    pygame.display.update()                    


