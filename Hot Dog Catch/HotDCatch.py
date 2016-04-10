import pygame
import random
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Hot Dog Catcher')

gameExit = False

BlockMove = 10

clock = pygame.time.Clock()

def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])






def GameLoop():

    gameExit = False
    gameOver = False

    lead_x = 450
    lead_y = 450

    lead_x_change = 0
    lead_y_change = 0

    randDogX = round(random.randrange(0, 800))/10.0)*10.0
    randDogY = round(random.randrange(0, 175))/10.0)*10.0

   

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -BlockMove
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = BlockMove
                    lead_y_change = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                    lead_x_change = 0


        lead_x += lead_x_change
        lead_y += lead_y_change

        HdogThicknessX = 40
        HdogThicknessY = 40
        
        
        gameDisplay.fill(white)
        


        dogY = 100
        dogX = 400
        dogY_change = 0

        

        for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN:
                dogY_change = 10

        dogY += dogY_change

        pygame.draw.rect(gameDisplay,red,[dogX,dogY,40,40])

        pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,40,10])

        pygame.display.update()



        
            
 

        clock.tick(60)
        

    pygame.quit()
    quit()

GameLoop() 

























