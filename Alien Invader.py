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

    randAlienX = round(random.randrange(0, display_width - 30))  # /10.0)*10.0
    randAlienY = round(random.randrange(50, display_height - 100))  # /10.0)*10.0

    randAlienX2 = round(random.randrange(0, display_width - 30))  # /10.0)*10.0
    randAlienY2 = round(random.randrange(50, display_height - 100))  # /10.0)*10.0

    randAlienX3 = round(random.randrange(0, display_width - 30))  # /10.0)*10.0
    randAlienY3 = round(random.randrange(50, display_height - 100))  # /10.0)*10.0

    randAlienX4 = round(random.randrange(0, display_width - 30))  # /10.0)*10.0
    randAlienY4 = round(random.randrange(50, display_height - 100))  # /10.0)*10.0

    randAlienX5 = round(random.randrange(0, display_width - 30))  # /10.0)*10.0
    randAlienY5 = round(random.randrange(50, display_height - 100))  # /10.0)*10.0

    randAlienX6 = round(random.randrange(0, display_width - 30))  # /10.0)*10.0
    randAlienY6 = round(random.randrange(50, display_height - 100))  # /10.0)*10.0

    randAlienX7 = round(random.randrange(0, display_width - 30))  # /10.0)*10.0
    randAlienY7 = round(random.randrange(50, display_height - 100))  # /10.0)*10.0

    randAlienX8 = round(random.randrange(0, display_width - 30))  # /10.0)*10.0
    randAlienY8 = round(random.randrange(50, display_height - 100))  # /10.0)*10.0

    randAlienX9 = round(random.randrange(0, display_width - 30))  # /10.0)*10.0
    randAlienY9 = round(random.randrange(50, display_height - 100))  # /10.0)*10.0

    randAlienX10 = round(random.randrange(0, display_width - 30))  # /10.0)*10.0
    randAlienY10 = round(random.randrange(50, display_height - 100))  # /10.0)*10.0

    randAlienX11 = round(random.randrange(0, display_width - 30))  # /10.0)*10.0
    randAlienY11 = round(random.randrange(50, display_height - 100))  # /10.0)*10.0

    randAlienX12 = round(random.randrange(0, display_width - 30))  # /10.0)*10.0
    randAlienY12 = round(random.randrange(50, display_height - 100))  # /10.0)*10.0

    randAlienX13 = round(random.randrange(0, display_width - 30))  # /10.0)*10.0
    randAlienY13 = round(random.randrange(50, display_height - 100))  # /10.0)*10.0

    randAlienX14 = round(random.randrange(0, display_width - 30))  # /10.0)*10.0
    randAlienY14 = round(random.randrange(50, display_height - 100))  # /10.0)*10.0

    randAlienX15 = round(random.randrange(0, display_width - 30))  # /10.0)*10.0
    randAlienY15 = round(random.randrange(50, display_height - 100))  # /10.0)*10.0

    global hit


    def fireShell(xy, tankx, tanky, turpos):
        fire = True
        global hit


        startingShell = list(xy)
        print("FIRE!", xy)

        shell_location = startingShell
        # pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5)

        while fire:
            time.sleep(0.0001)
            startingShell[1] -= 20
            pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5)
            pygame.draw.circle(gameDisplay, white, (startingShell[0], startingShell[1] + 20), 5)
            if startingShell[1] < 0:
                fire = False

            check_x_1 = startingShell[0] <= randAlienX + 30
            check_x_2 = startingShell[0] >= randAlienX
            check_y_1 = startingShell[1] <= randAlienY
            check_y_2 = startingShell[1] >= randAlienY - 10
            var0 = True
            var1 = True
            var2 = True
            var3 = True
            var4 = True
            var5 = True
            var6 = True
            var7 = True
            var8 = True
            var9 = True
            var10 = True
            var11 = True
            var12 = True
            var13 = True
            var14 = True
            var15 = True

            if check_x_1 and check_x_2 and check_y_1:
                print("hit")
                fire = False
                hit = hit + 1
                var0 = False
            pygame.display.update()

            check_x2_1 = startingShell[0] <= randAlienX2 + 30
            check_x2_2 = startingShell[0] >= randAlienX2
            check_y2_1 = startingShell[1] <= randAlienY2
            check_y2_2 = startingShell[1] >= randAlienY2 - 10

            if check_x2_1 and check_x2_2 and check_y2_1:
                print("hit")
                fire = False
                hit = hit + 1
                var1 = False
            pygame.display.update()

            check_x3_1 = startingShell[0] <= randAlienX3 + 30
            check_x3_2 = startingShell[0] >= randAlienX3
            check_y3_1 = startingShell[1] <= randAlienY3
            check_y3_2 = startingShell[1] >= randAlienY3 - 10

            if check_x3_1 and check_x3_2 and check_y3_1:
                print("hit")
                fire = False
                hit = hit + 1
                var2 = False
                var2 = False
            pygame.display.update()

            check_x4_1 = startingShell[0] <= randAlienX4 + 30
            check_x4_2 = startingShell[0] >= randAlienX4
            check_y4_1 = startingShell[1] <= randAlienY4
            check_y4_2 = startingShell[1] >= randAlienY4 - 10

            if check_x4_1 and check_x4_2 and check_y4_1 and check_y4_2:
                print("hit")
                fire = False
                hit = hit + 1
                var3 = False
            pygame.display.update()

            check_x5_1 = startingShell[0] <= randAlienX5 + 30
            check_x5_2 = startingShell[0] >= randAlienX5
            check_y5_1 = startingShell[1] <= randAlienY5
            check_y5_2 = startingShell[1] >= randAlienY5 - 10

            if check_x5_1 and check_x5_2 and check_y5_1 and check_y5_2:
                print("hit")
                fire = False
                hit = hit + 1
                var4 = False
            pygame.display.update()

            check_x6_1 = startingShell[0] <= randAlienX6 + 30
            check_x6_2 = startingShell[0] >= randAlienX6
            check_y6_1 = startingShell[1] <= randAlienY6
            check_y6_2 = startingShell[1] >= randAlienY6 - 10

            if check_x6_1 and check_x6_2 and check_y6_1 and check_y6_2:
                print("hit")
                fire = False
                hit = hit + 1
            pygame.display.update()

            check_x7_1 = startingShell[0] <= randAlienX7 + 30
            check_x7_2 = startingShell[0] >= randAlienX7
            check_y7_1 = startingShell[1] <= randAlienY7
            check_y7_2 = startingShell[1] >= randAlienY7 - 10

            if check_x7_1 and check_x7_2 and check_y7_1 and  check_y7_2:
                print("hit")
                fire = False
                hit = hit + 1
            pygame.display.update()

            check_x8_1 = startingShell[0] <= randAlienX8 + 30
            check_x8_2 = startingShell[0] >= randAlienX8
            check_y8_1 = startingShell[1] <= randAlienY8
            check_y8_2 = startingShell[1] >= randAlienY8 - 10

            if check_x8_1 and check_x8_2 and check_y8_1:
                print("hit")
                fire = False
                hit = hit + 1
            pygame.display.update()

            check_x9_1 = startingShell[0] <= randAlienX9 + 30
            check_x9_2 = startingShell[0] >= randAlienX9
            check_y9_1 = startingShell[1] <= randAlienY9
            check_y9_2 = startingShell[1] >= randAlienY9 - 10

            if check_x9_1 and check_x9_2 and check_y9_1 and check_y9_2:
                print("hit")
                fire = False
                hit = hit + 1
            pygame.display.update()

            check_x10_1 = startingShell[0] <= randAlienX10 + 30
            check_x10_2 = startingShell[0] >= randAlienX10
            check_y10_1 = startingShell[1] <= randAlienY10
            check_y10_2 = startingShell[1] >= randAlienY10 - 10

            if check_x10_1 and check_x10_2 and check_y10_1:
                print("hit")
                fire = False
                hit = hit + 1
            pygame.display.update()

            check_x11_1 = startingShell[0] <= randAlienX11 + 30
            check_x11_2 = startingShell[0] >= randAlienX11
            check_y11_1 = startingShell[1] <= randAlienY11
            check_y11_2 = startingShell[1] >= randAlienY11 - 10

            if check_x11_1 and check_x11_2 and check_y11_1 and check_y11_2:
                print("hit")
                fire = False
                hit = hit + 1
            pygame.display.update()

            check_x12_1 = startingShell[0] <= randAlienX12 + 30
            check_x12_2 = startingShell[0] >= randAlienX12
            check_y12_1 = startingShell[1] <= randAlienY12
            check_y12_2 = startingShell[1] >= randAlienY12 - 10

            if check_x12_1 and check_x12_2 and check_y12_1 and  check_y12_2:
                print("hit")
                fire = False
                hit = hit + 1
            pygame.display.update()

            check_x13_1 = startingShell[0] <= randAlienX13 + 30
            check_x13_2 = startingShell[0] >= randAlienX13
            check_y13_1 = startingShell[1] <= randAlienY13
            check_y13_2 = startingShell[1] >= randAlienY13 - 10

            if check_x13_1 and check_x13_2 and check_y13_1 and check_y13_2:
                print("hit")
                fire = False
                hit = hit + 1
            pygame.display.update()

            check_x14_1 = startingShell[0] <= randAlienX14 + 30
            check_x14_2 = startingShell[0] >= randAlienX14
            check_y14_1 = startingShell[1] <= randAlienY14
            check_y14_2 = startingShell[1] >= randAlienY14 - 10

            if check_x14_1 and check_x14_2 and check_y14_1 and check_y14_2:
                print("hit")
                fire = False
                hit = hit + 1
            pygame.display.update()

            check_x15_1 = startingShell[0] <= randAlienX15 + 30
            check_x15_2 = startingShell[0] >= randAlienX15
            check_y15_1 = startingShell[1] <= randAlienY15
            check_y15_2 = startingShell[1] >= randAlienY15 - 10

            if check_x15_1 and check_x15_2 and check_y15_1 and check_y15_2:
                print("hit")
                fire = False
                hit = hit + 1
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
        if hit ==  0:
            pygame.draw.rect(gameDisplay, red, [randAlienX, randAlienY, 30, 10])


        if hit == 1:
            pygame.draw.rect(gameDisplay, red, [randAlienX2, randAlienY2, 30, 10])


        if hit == 2:
            pygame.draw.rect(gameDisplay, red, [randAlienX3, randAlienY3, 30, 10])

        if hit == 3:
            pygame.draw.rect(gameDisplay, red, [randAlienX4, randAlienY4, 30, 10])

        if hit == 4:
            pygame.draw.rect(gameDisplay, red, [randAlienX5, randAlienY5, 30, 10])

        if hit == 5:
            pygame.draw.rect(gameDisplay, red, [randAlienX6, randAlienY6, 30, 10])

        if hit == 6:
            pygame.draw.rect(gameDisplay, red, [randAlienX7, randAlienY7, 30, 10])

        if hit == 7:
            pygame.draw.rect(gameDisplay, red, [randAlienX8, randAlienY8, 30, 10])

        if hit == 8:
            pygame.draw.rect(gameDisplay, red, [randAlienX9, randAlienY9, 30, 10])

        if hit == 9:
            pygame.draw.rect(gameDisplay, red, [randAlienX10, randAlienY10, 30, 10])

        if hit == 10:
            pygame.draw.rect(gameDisplay, red, [randAlienX11, randAlienY11, 30, 10])

        if hit == 11:
            pygame.draw.rect(gameDisplay, red, [randAlienX12, randAlienY12, 30, 10])

        if hit == 12:
            pygame.draw.rect(gameDisplay, red, [randAlienX13, randAlienY13, 30, 10])

        if hit == 13:
            pygame.draw.rect(gameDisplay, red, [randAlienX14, randAlienY14, 30, 10])

        if hit == 14:
            pygame.draw.rect(gameDisplay, red, [randAlienX15, randAlienY15, 30, 10])


        ##randAlienY = round(random.randrange(0, display_height - 30))  # /10.0)*10.0

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()































































