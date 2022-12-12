#Käynnistetään pelimoottori
import pygame, random
from car import Car
pygame.init()

#Asetetaan värit
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
GREY = (220, 220, 220)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
YELLOW = (255, 255, 0)

speed = 1
colorList = (PURPLE, YELLOW, CYAN, BLUE, RED)

#Avataan uusi ikkuna
SCREENWIDTH = 800
SCREENHEIGHT = 600
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FGJPeli")

#sprite lista
all_sprites_list = pygame.sprite.Group()

playerCar = Car(RED, 60, 80, 70)
playerCar.rect.x = 160
playerCar.rect.y = SCREENHEIGHT - 100

car1 = Car(PURPLE, 60, 80, random.randint(50,100))
car1.rect.x = 60
car1.rect.y = -100
 
car2 = Car(YELLOW, 60, 80, random.randint(50,100))
car2.rect.x = 160
car2.rect.y = -600
 
car3 = Car(CYAN, 60, 80, random.randint(50,100))
car3.rect.x = 260
car3.rect.y = -300
 
car4 = Car(BLUE, 60, 80, random.randint(50,100))
car4.rect.x = 360
car4.rect.y = -900

all_sprites_list.add(playerCar)
all_sprites_list.add(car1)
all_sprites_list.add(car2)
all_sprites_list.add(car3)
all_sprites_list.add(car4)

all_coming_cars = pygame.sprite.Group()
all_coming_cars.add(car1)
all_coming_cars.add(car2)
all_coming_cars.add(car3)
all_coming_cars.add(car4)

#Loop pyörittää peliä, kunnes käyttäjä sammuttaa sen
carryOn = True

#Kello määrittää, kuinka usein näyttö päivittyy
clock = pygame.time.Clock()

#Pääohjelma loop
while carryOn:
    #Päätapahtuma loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                caryyOn = False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                    playerCar.moveRight(10)
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            playerCar.moveRigth(5)
        if keys[pygame.K_UP]:
            playerCar.moveUp(5)
        if keys[pygame.K_DOWN]:
            playerCar.moveDown(5)

        ##GAME LOGIC
        for car in all_coming_cars:
            car.moveUp(speed)
            if car.rect.y > SCREENHEIGHT:
                car.changeSpeed(random.randint(50,100))
                car.repaint(random.choice(colorList))
                car.rect.y = -200
        car_collision_list = pygame.sprite.spritecollide(playerCar,all_coming_cars,False)
        for car in car_collision_list:
            print("Car crash!")
            #End Of Game
            carryOn=False
        all_sprites_list.update()

        ##
        #Ruutu valkoiseksi
        screen.fill(WHITE)
        #Piirretään background
        pygame.draw.rect(screen, GREEN, [600, 0, 500, 500], 0)
        pygame.draw.rect(screen, GREEN, [0, 0, 100, 500], 0)
        pygame.draw.rect(screen, GREY, [100, 0, 500, 500], 0)
        pygame.draw.line(screen, WHITE, [100, 0], [100, 500], 5)
        pygame.draw.line(screen, WHITE, [200, 0], [200, 500], 5)
        pygame.draw.line(screen, WHITE, [300, 0], [300, 500], 5)
        pygame.draw.line(screen, WHITE, [400, 0], [400, 500], 5)
        pygame.draw.line(screen, WHITE, [500, 0], [500, 500], 5)

        all_sprites_list.draw(screen)

        #
        pygame.display.flip()

        #Framerate limit = 60
        clock.tick(60)

#
pygame.quit()