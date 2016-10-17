import os
import pygame
import time
import random




### Colors Constant
BLACK   = (0,0,0)
WHITE   = (255,255,255)
RED     = (255,0,0)
GREEN   = (0,255,0)



### Class and Function definitions

class gameImage:
    def __init__(self, path):
        self.img = pygame.image.load(path)
        (self.width, self.height) = self.img.get_rect().size
    
    def draw(self,x,y):
        gameDisplay.blit(self.img,(x,y))


def initImagePos():
    carImg.X = gameDisplay.get_rect().centerx - (int)(carImg.width/2)
    carImg.Y = (display_height - carImg.height - 10)

    for road in roadImg:
        road.X  = 0
        road.Y  = 0
    for tree in treeImg:
        tree.X  = 0
        tree.Y  = 0 -(tree.height)
    

def displayMsgCenter(text):
    largeText = font.render(text, True, BLACK)
    textpos = largeText.get_rect()
    textpos.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(largeText, textpos)
    pygame.display.update()
    time.sleep(2)
    

def gameLoop():
    
    gameExit = False
    roadNum = 0
    treeNum = random.randrange(0, 3)

    initImagePos()   
    
    x_change = 0
    ticks=pygame.time.get_ticks() #starter tick
    
    while gameExit != True:
        ### Draw and Update
        
        roadImg[roadNum].draw(roadImg[roadNum].X, roadImg[roadNum].Y)
        treeImg[treeNum].draw(treeImg[treeNum].X, treeImg[treeNum].Y)
        carImg.draw(carImg.X, carImg.Y)
        pygame.display.update()
        clock.tick(30)
    
        ### Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        carImg.X += x_change
        if (carImg.X > display_width - carImg.width) or (carImg.X < 0):
            displayMsgCenter("You Crashed!!!")
            initImagePos()
            treeNum = random.randrange(0, 3)

        if ((treeImg[treeNum].Y + treeImg[treeNum].height) >= carImg.Y) and (treeImg[treeNum].Y <= (carImg.Y + carImg.height)) and (carImg.X >= treeImg[treeNum].X and carImg.X < (treeImg[treeNum].X + treeImg[treeNum].width - 10)):
            displayMsgCenter("You Crashed!!!")
            initImagePos()
            treeNum = random.randrange(0, 3)

        if(pygame.time.get_ticks() - ticks) > 100:
            roadNum ^= 1
            treeImg[treeNum].Y += 10
            if treeImg[treeNum].Y > display_height:
                treeImg[treeNum].Y = 0 -(treeImg[treeNum].height)
                treeNum = random.randrange(0, 3)

            ticks=pygame.time.get_ticks()
            

pygame.init()
### Load Images
carImg = gameImage(os.path.join("image","Racecar2.png"))
roadImg = []
roadImg.append(gameImage(os.path.join("image","Road1.jpg")))
roadImg.append(gameImage(os.path.join("image","Road2.jpg")))
treeImg = []
treeImg.append(gameImage(os.path.join("image","tree1.png")))
treeImg.append(gameImage(os.path.join("image","tree2.png")))
treeImg.append(gameImage(os.path.join("image","tree3.png")))

display_width  = roadImg[0].width
display_height = roadImg[0].height

### Initialize Display
pygame.display.set_caption('CarDriving')
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

### Initialize Font
font = pygame.font.Font("freesansbold.ttf", 36)

gameLoop()
pygame.quit()
#quit()
