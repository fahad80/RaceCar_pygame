import os
import pygame
import time
import random


pygame.init()

# Colors Constant
BLACK   = (0,0,0)
WHITE   = (255,255,255)
RED     = (255,0,0)
GREEN   = (0,255,0)

# Load Images
carImg  = pygame.image.load(os.path.join("image","Racecar2.png"))
roadImg = []
roadImg.append(pygame.image.load(os.path.join("image","Road1.jpg")))
roadImg.append(pygame.image.load(os.path.join("image","Road2.jpg")))
treeImg = []
treeImg.append(pygame.image.load(os.path.join("image","tree2.png")))
treeImg.append(pygame.image.load(os.path.join("image","tree3.png")))

(car_width, car_height) = carImg.get_rect().size
(display_width, display_height) = roadImg[0].get_rect().size

# Initialize Display
pygame.display.set_caption('RaceCar')
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

# Initialize Font
font = pygame.font.Font("freesansbold.ttf", 36)


# Function definition
def drawCar(x,y):
    gameDisplay.blit(carImg,(x,y))

def drawRoad(x,y, roadNum):
    gameDisplay.blit(roadImg[roadNum],(x,y))

def drawTree(x,y,treeNum):
    gameDisplay.blit(treeImg[treeNum],(x,y))

def displayMsgCenter(text):
    largeText = font.render(text, True, BLACK)
    textpos = largeText.get_rect()
    textpos.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(largeText, textpos)
    pygame.display.update()
    time.sleep(2)
    

def gameLoop():
    carX = gameDisplay.get_rect().centerx - (int)(car_width/2)
    carY = (display_height - car_height - 10)

    roadNum = 0
    roadX   = 0
    roadY   = 0
    
    treeNum = random.randrange(0, 100)%2
    treeX   = 0
    treeY   = 0 -(treeImg[treeNum].get_rect().size[1])
   
    
    x_change = 0
    ticks=pygame.time.get_ticks() #starter tick
    
    while True:
        # Draw and Update
        
        drawRoad(roadX, roadY, roadNum)
        drawTree(treeX,treeY, treeNum)
        drawCar(carX, carY)
        pygame.display.update()
        clock.tick(30)
    
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        carX += x_change
        if (carX > display_width - car_width) or (carX < 0):
            displayMsgCenter("You Crashed!!!")
            carX = gameDisplay.get_rect().centerx - (int)(car_width/2)
            carY = (display_height - car_height - 10)
            treeX   = 0
            treeY   = 0 -(treeImg[treeNum].get_rect().size[1])

        if(pygame.time.get_ticks() - ticks) > 100:
            roadNum ^= 1
            treeY += 7
            if treeY > display_height:
                treeY = 0 -(treeImg[treeNum].get_rect().size[1])
                treeNum = random.randrange(0, 100)%2

            ticks=pygame.time.get_ticks()
            


gameLoop()
#quit()
