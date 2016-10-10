import os
import pygame
import time


pygame.init()

# Colors Constant
BLACK   = (0,0,0)
WHITE   = (255,255,255)
RED     = (255,0,0)
GREEN   = (0,255,0)

# Load Images
carImg  = pygame.image.load(os.path.join("image","Racecar2.png"))
roadImg = pygame.image.load(os.path.join("image","Road.jpg"))

(car_width, car_height) = carImg.get_rect().size
(display_width, display_height) = roadImg.get_rect().size

# Initialize Display
pygame.display.set_caption('RaceCar')
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

# Initialize Font
font = pygame.font.Font("freesansbold.ttf", 36)


# Function definition
def drawCar(x,y):
    gameDisplay.blit(carImg,(x,y))

def drawRoad(x,y):
    gameDisplay.blit(roadImg,(x,y))

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
    roadX = 0
    roadY = 0

    x_change = 0
    
    while True:
        # Draw and Update
        drawRoad(roadX, roadY)
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
            


gameLoop()
#quit()
