
import pygame, sys
from pygame.locals import *

'''
from pygame.locals imports all features because pygame.locals
contains several constant variables that are easy to identify as
being in the pygame.locals module without pygame.locals. in front
of them
'''

pygame.init() #function call - always called needed after import pygame
#function call returns pygame.Surface object
DISPLAYSURF = pygame.display.set_mode((400,300)) 
pygame.display.set_caption('Hello World!')
while True: #main game loop
    for event in pygame.event.get(): #function call returns list of event objects
        if event.type == QUIT: #QUIT is pygame.locals attribute
            pygame.quit()
            sys.exit()
        pygame.display.update()
