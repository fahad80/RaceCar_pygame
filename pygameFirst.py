import os
import pygame
pygame.init()


# Colors Constant
BLACK   = (0,0,0)
WHITE   = (255,255,255)
RED     = (255,0,0)
GREEN   = (0,255,0)


carImg  = pygame.image.load(os.path.join("image","Racecar2.png"))
roadImg = pygame.image.load(os.path.join("image","Road.jpg"))

(car_width, car_height) = carImg.get_rect().size
(display_width, display_height) = roadImg.get_rect().size


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('RaceCar')
clock = pygame.time.Clock()


def drawCar(x,y):
    gameDisplay.blit(carImg,(x,y))

def drawRoad(x,y):
    gameDisplay.blit(roadImg,(x,y))

def gameLoop():
    carX = gameDisplay.get_rect().centerx - (int)(car_width/2)
    carY = (display_height - car_height - 10)
    roadX = 0
    roadY = 0

    x_change = 0
    gameExit = False

    while not gameExit:

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

        carX += x_change
        if (carX > display_width - car_width) or (carX < 0):
            gameExit = True

        #gameDisplay.fill(white)
        drawRoad(roadX, roadY)
        drawCar(carX, carY)
        pygame.display.update()
        clock.tick(30)


gameLoop()
pygame.quit()
#quit()
