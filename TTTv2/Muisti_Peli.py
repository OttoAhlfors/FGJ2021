import random, sys, time, pygame
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 1000
WINDOWHEIGHT = 900
FLASHSPEED = 500 # in milliseconds
FLASHDELAY = 200 # in milliseconds
BUTTONSIZE = 200
BUTTONGAPSIZE = 20
TIMEOUT = 4 # seconds before game over if no button is pushed.

#                R    G    B
WHITE        = (255, 255, 255)
BLACK        = (  0,   0,   0)
BRIGHTRED    = (255,   0,   0)
RED          = (155,   0,   0)
BRIGHTGREEN  = (  0, 255,   0)
GREEN        = (  0, 155,   0)
BRIGHTBLUE   = (  0,   0, 255)
BLUE         = (  0,   0, 155)
BRIGHTYELLOW = (255, 255,   0)
YELLOW       = (155, 155,   0)
DARKGRAY     = ( 40,  40,  40)
BROWN        = (100, 40, 0)
PINK         = (255, 100, 180)
ORANGE       = (255, 100, 10)
GRAY         = (127, 127, 127)
COFFEE_BROWN = (200, 190, 140)
bgColor = GRAY

XMARGIN = 180
YMARGIN = 130

# Rect objects for each of the four buttons
YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
BLUERECT   = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
REDRECT    = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
GREENRECT  = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
WHITERECT  = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONSIZE + BUTTONGAPSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
BROWNRECT  = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONSIZE + BUTTONGAPSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
PINKRECT   = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONSIZE + BUTTONGAPSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
ORANGERECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONSIZE + BUTTONGAPSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
BLACKRECT  = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONSIZE + BUTTONGAPSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
WINS = False
def muistipelimg():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BEEP1, BEEP2, BEEP3, BEEP4

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Simulate')

    BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
    goalSurf = BASICFONT.render('Try to remember your phone pin!', 1, WHITE)
    infoSurf = BASICFONT.render('Match the pattern by clicking on the buttons.', 1, DARKGRAY)
    goalRect = goalSurf.get_rect()
    goalRect.topleft = (10, WINDOWHEIGHT - 890)
    infoRect = infoSurf.get_rect()
    infoRect.topleft = (10, WINDOWHEIGHT - 25)

    # Initialize some variables for a new game
    pattern = [] # stores the pattern of colors
    currentStep = 0 # the color the player must push next
    lastClickTime = 0 # timestamp of the player's last button push
    score = 0
    # when False, the pattern is playing. when True, waiting for the player to click a colored button:
    waitingForInput = False

    while True: # main game loop
        clickedButton = None # button that was clicked (set to YELLOW, RED, GREEN, or BLUE)
        DISPLAYSURF.fill(bgColor)
        drawButtons()

        scoreSurf = BASICFONT.render('Score: ' + str(score), 1, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 100, 10)
        DISPLAYSURF.blit(scoreSurf, scoreRect)

        DISPLAYSURF.blit(infoSurf, infoRect)
        DISPLAYSURF.blit(goalSurf, goalRect)

        checkForQuit()
        for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                clickedButton = getButtonClicked(mousex, mousey)
            elif event.type == KEYDOWN:
                if event.key == K_P7:
                    clickedButton = YELLOW
                elif event.key == K_P8:
                    clickedButton = BLUE
                elif event.key == K_P4:
                    clickedButton = RED
                elif event.key == K_KP5:
                    clickedButton = GREEN
                elif event.key == K_KP9:
                    clickedButton = WHITE
                elif event.key == K_KP6:
                    clickedButton = BROWN
                elif event.key == K_KP1:
                    clickedButton = PINK
                elif event.key == K_KP2:
                    clickedButton = ORANGE
                elif event.key == K_KP3:
                    clickedButton = BLACK



        if not waitingForInput:
            # play the pattern
            pygame.display.update()
            pygame.time.wait(1000)
            pattern.append(random.choice((YELLOW, BLUE, RED, GREEN, WHITE, ORANGE, PINK, BROWN, BLACK)))
            for button in pattern:
                flashButtonAnimation(button)
                pygame.time.wait(FLASHDELAY)
            waitingForInput = True
        else:
            # wait for the player to enter buttons
            if clickedButton and clickedButton == pattern[currentStep]:
                # pushed the correct button
                flashButtonAnimation(clickedButton)
                currentStep += 1
                lastClickTime = time.time()

                if currentStep == len(pattern):
                    # pushed the last button in the pattern
                    changeBackgroundAnimation()
                    score += 1
                    if score == 1:
                        WINS = True
                        return WINS
                    waitingForInput = False
                    currentStep = 0 # reset back to first step

            elif (clickedButton and clickedButton != pattern[currentStep]) or (currentStep != 0 and time.time() - TIMEOUT > lastClickTime):
                # pushed the incorrect button, or has timed out
                gameOverAnimation()
                # reset the variables for a new game:
                pattern = []
                currentStep = 0
                waitingForInput = False
                score = 0
                pygame.time.wait(1000)
                changeBackgroundAnimation()

        pygame.display.update()
        FPSCLOCK.tick(FPS)
    


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back


def flashButtonAnimation(color, animationSpeed=50):
    if color == YELLOW:
        flashColor = GRAY
        rectangle = YELLOWRECT
    elif color == BLUE:
        flashColor = GRAY
        rectangle = BLUERECT
    elif color == RED:
        flashColor = GRAY
        rectangle = REDRECT
    elif color == GREEN:
        flashColor = GRAY
        rectangle = GREENRECT
    elif color == WHITE:
        flashColor = GRAY
        rectangle = WHITERECT
    elif color == PINK:
        flashColor = GRAY
        rectangle = PINKRECT
    elif color == BROWN:
        flashColor = GRAY
        rectangle = BROWNRECT
    elif color == ORANGE:
        flashColor = GRAY
        rectangle = ORANGERECT
    elif color == BLACK:
        flashColor = GRAY
        rectangle = BLACKRECT

    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE))
    flashSurf = flashSurf.convert_alpha()
    r, g, b = flashColor
    #sound.play()
    for start, end, step in ((0, 255, 1), (255, 0, -1)): # animation loop
        for alpha in range(start, end, animationSpeed * step):
            checkForQuit()
            DISPLAYSURF.blit(origSurf, (0, 0))
            flashSurf.fill((r, g, b, alpha))
            DISPLAYSURF.blit(flashSurf, rectangle.topleft)
            pygame.display.update()
            FPSCLOCK.tick(FPS)
    DISPLAYSURF.blit(origSurf, (0, 0))


def drawButtons():
    pygame.draw.rect(DISPLAYSURF, YELLOW, YELLOWRECT)
    pygame.draw.rect(DISPLAYSURF, BLUE,   BLUERECT)
    pygame.draw.rect(DISPLAYSURF, RED,    REDRECT)
    pygame.draw.rect(DISPLAYSURF, GREEN,  GREENRECT)
    pygame.draw.rect(DISPLAYSURF, WHITE, WHITERECT)
    pygame.draw.rect(DISPLAYSURF, BROWN, BROWNRECT)
    pygame.draw.rect(DISPLAYSURF, PINK, PINKRECT)
    pygame.draw.rect(DISPLAYSURF, ORANGE, ORANGERECT)
    pygame.draw.rect(DISPLAYSURF, BLACK, BLACKRECT)

def changeBackgroundAnimation(animationSpeed=40):
    global bgColor
    newBgColor = GRAY

    newBgSurf = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
    newBgSurf = newBgSurf.convert_alpha()
    r, g, b = newBgColor
    for alpha in range(0, 255, animationSpeed): # animation loop
        checkForQuit()
        DISPLAYSURF.fill(bgColor)

        newBgSurf.fill((r, g, b, alpha))
        DISPLAYSURF.blit(newBgSurf, (0, 0))

        drawButtons() # redraw the buttons on top of the tint

        pygame.display.update()
        FPSCLOCK.tick(FPS)
    bgColor = newBgColor


def gameOverAnimation(color=WHITE, animationSpeed=50):
    # play all beeps at once, then flash the background
    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface(DISPLAYSURF.get_size())
    flashSurf = flashSurf.convert_alpha()
    r, g, b = color
    for i in range(3): # do the flash 3 times
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            # The first iteration in this loop sets the following for loop
            # to go from 0 to 255, the second from 255 to 0.
            for alpha in range(start, end, animationSpeed * step): # animation loop
                # alpha means transparency. 255 is opaque, 0 is invisible
                checkForQuit()
                flashSurf.fill((r, g, b, alpha))
                DISPLAYSURF.blit(origSurf, (0, 0))
                DISPLAYSURF.blit(flashSurf, (0, 0))
                drawButtons()
                pygame.display.update()
                FPSCLOCK.tick(FPS)



def getButtonClicked(x, y):
    if YELLOWRECT.collidepoint( (x, y) ):
        return YELLOW
    elif BLUERECT.collidepoint( (x, y) ):
        return BLUE
    elif REDRECT.collidepoint( (x, y) ):
        return RED
    elif GREENRECT.collidepoint( (x, y) ):
        return GREEN
    elif WHITERECT.collidepoint( (x, y) ):
        return WHITE
    elif BROWNRECT.collidepoint( (x, y) ):
        return BROWN
    elif PINKRECT.collidepoint( (x, y) ):
        return PINK
    elif ORANGERECT.collidepoint( (x, y) ):
        return ORANGE
    elif BLACKRECT.collidepoint( (x, y) ):
        return BLACK
    return None


if __name__ == '__main__':
    WINS = muistipelimg()
    print(WINS)