import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))


pygame.display.set_caption('Alien')

#icon = pygame.image.load("apple.png")
#pygame.display.set_icon(icon)

white = (255,255,255)
black = (0,0,0)


red = (200,0,0)
light_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (34,177,76)
light_green = (0,255,0)

clock = pygame.time.Clock()

hit = 0


tankWidth = 40
tankHeight = 20

turretWidth = 5
wheelWidth = 5

fire = True


smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

#img = pygame.image.load('snakehead.png')
#appleimg = pygame.image.load('apple.png')

def score(score):

    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])


def text_objects(text, color,size = "small"):

    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)

def message_to_screen(msg,color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (int(display_width / 2), int(display_height / 2)+y_displace)
    gameDisplay.blit(textSurf, textRect)

def tank(x,y,turPos):
    x = int(x)
    y = int(y)


    possibleTurrets = [(x-0, y-35),
                       (x+0, y-35),
                       (x+0, y-35),
                       (x+0, y-35),
                       (x+0, y-35),
                       (x-0, y-35),
                       (x-0, y-35),
                       (x-0, y-35),
                       (x-0, y-35)
                       ]




    pygame.draw.circle(gameDisplay, black, (x,y), int(tankHeight/2))
    pygame.draw.rect(gameDisplay, black, (x-tankHeight, y, tankWidth, tankHeight))

    pygame.draw.line(gameDisplay, black, (x,y), possibleTurrets[turPos], turretWidth)

    pygame.draw.circle(gameDisplay, black, (x-15, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x-10, y+20), wheelWidth)


    pygame.draw.circle(gameDisplay, black, (x-15, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x-10, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x-5, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x+5, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x+10, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x+15, y+20), wheelWidth)

    return possibleTurrets[turPos]


def game_controls():

    gcont = True

    while gcont:
        for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


        gameDisplay.fill(white)
        message_to_screen("Controls",green,-100,size="large")
        message_to_screen("Fire: Spacebar",black,-30)
        message_to_screen("Move Tank: Left and Right arrows",black,50)
        message_to_screen("Pause: P",black,90)


        button("play", 150,500,100,50, green, light_green, action="play")
        button("Main", 350,500,100,50, yellow, light_yellow, action="main")
        button("quit", 550,500,100,50, red, light_red, action ="quit")



        pygame.display.update()

        clock.tick(15)


def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "controls":
                game_controls()

            if action == "play":
                gameLoop()

            if action == "main":
                game_intro()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))

    text_to_button(text,black,x,y,width,height)



def pause():

    paused = True
    message_to_screen("Paused",black,-100,size="large")
    message_to_screen("Press C to continue playing or Q to quit",black,25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()



        clock.tick(5)






'''''
def fireShell(xy,tankx,tanky,turpos):
    fire = True
    startingShell = list(xy)
    print("FIRE!",xy)
    shell_location = startingShell
    #pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5)
    while fire:
        time.sleep(0.005)
        startingShell[1] -= 10
        pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5)
        pygame.draw.circle(gameDisplay, white, (startingShell[0], startingShell[1] + 10), 5)
        if startingShell[1] < 0:
            fire = False
        check_x_1 = startingShell[0] <= randAlienX + 30
        check_x_2 = startingShell[0] >= randAlienX
        check_y_1 = startingShell[1] <= randAlienY
        check_y_2 = startingShell[1] >= randAlienY - 10
        if check_x_1 and check_x_2 and check_y_1:
            print("hit")
            fire = False
            hit = True
        pygame.display.update()
        #clock.tick(3000)
'''''

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro = False
                    elif event.key == pygame.K_q:

                        pygame.quit()
                        quit()

        gameDisplay.fill(white)
        message_to_screen("Alien Shooter!",green,-100,size="large")
        message_to_screen("The objective is to shoot and destroy aliens",black,-30)
        message_to_screen("The more enemies you destroy, the harder they get.",black,50)
        #message_to_screen("Press C to play, P to pause or Q to quit",black,180)


        button("play", 150,500,100,50, green, light_green, action="play")
        button("controls", 350,500,100,50, yellow, light_yellow, action="controls")
        button("quit", 550,500,100,50, red, light_red, action ="quit")



        pygame.display.update()

        clock.tick(15)



def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 30


    #barrier_width = 50

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0

    currentTurPos = 0
    changeTur = 0

    global randAlienX
    global randAlienY

    randAlienX = round(random.randrange(0, display_width - 30))  # /10.0)*10.0
    randAlienY = round(random.randrange(50, display_height - 100))  # /10.0)*10.0



    global hit
    hit = False


    def fireShell(xy, tankx, tanky, turpos):
        fire = True
        global hit

        startingShell = list(xy)
        print("FIRE!", xy)

        while fire:
            time.sleep(0.01)
            startingShell[1] -= 15
            pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5)
            pygame.draw.circle(gameDisplay, white, (startingShell[0], startingShell[1] + 15), 5)
            global check_x_1
            global check_x_2
            global check_y_1
            global check_y_2
            check_x_1 = startingShell[0] <= randAlienX + 30
            check_x_2 = startingShell[0] >= randAlienX
            check_y_1 = startingShell[1] <= randAlienY
            check_y_2 = startingShell[1] >= randAlienY + 10
            if startingShell[1] < 0:
                fire = False
            if check_x_1 and check_x_2 and check_y_1:
                print("hit")
                fire = False
                hit = True
            pygame.display.update()


    while not gameExit:

        if gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",red,-50,size="large")
            message_to_screen("Press C to play again or Q to exit",black,50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -20

                elif event.key == pygame.K_RIGHT:
                    tankMove = 20

                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_p:
                    pause()

                elif event.key == pygame.K_SPACE:
                    fireShell(gun, mainTankX, mainTankY, currentTurPos)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0






        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0


        #if mainTankX - (tankWidth/2) < xlocation+barrier_width:
            #mainTankX += 5

        gameDisplay.fill(white)
        gun = tank(mainTankX, mainTankY, currentTurPos)

        pygame.draw.rect(gameDisplay, red, [randAlienX, randAlienY, 30, 10])

        if hit:
            randAlienX = round(random.randrange(0, display_width - 30))  # /10.0)*10.0
            randAlienY = round(random.randrange(50, display_height - 100))  # /10.0)*10.0
            hit = False

        ##randAlienY = round(random.randrange(0, display_height - 30))  # /10.0)*10.0

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()
























































