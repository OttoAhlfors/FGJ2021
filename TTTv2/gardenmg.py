import pygame, webbrowser, sys, random
WHITE = (255, 255, 255)

#TAUSTA
map_image = pygame.image.load("data/map/map.jpg")
player_image = pygame.image.load("data/images/entities/player/idle/idle_0.png")
kyykka_image = pygame.image.load("data/images/Kyykkä.png")

class Reuna(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.width=width
        self.height=height
        self.color =color

        #Reunan piirto
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

class Kyykka(pygame.sprite.Sprite):
    #Kyykän sprite

    def __init__(self, color, width, height, speed):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.width=width
        self.height=height
        self.color =color
        self.speed =speed

        #Kyykän piirto
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveRigth(self, pixels):
        self.rect.x += pixels
        
    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels

    def changeSpeed(self, speed):
        self.speed = speed

    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
def dodge():
    #Käynnistetään pelimoottori
    pygame.init()

    #Asetetaan värit
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    CYAN = (0, 255, 255)
    BLUE = (100, 100, 255)
    YELLOW = (255, 255, 0)

    speed = 4

    #player_rect = pygame.Rect(200,200,player_image.get_width(),player_image.get_height())
    #Avataan uusi ikkuna
    SCREENWIDTH = 1000
    SCREENHEIGHT = 900
    size = (SCREENWIDTH, SCREENHEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("FGJMiniGame")

    #sprite lista
    all_sprites_list = pygame.sprite.Group()

    player = Kyykka(WHITE, 60, 80, 70)
    player.rect = pygame.Rect(200,200,player_image.get_width(),player_image.get_height())
    player.rect.x = 450
    player.rect.y = SCREENHEIGHT - 100

    kyykka1 = Kyykka(WHITE, 50, 70, random.randint(50,400))
    kyykka1.rect = pygame.Rect(200,200,kyykka_image.get_width(),kyykka_image.get_height())
    kyykka1.rect.x = random.randint(5, 948)
    kyykka1.rect.y = random.randint(-1100, -100)
    
    kyykka2 = Kyykka(WHITE, 50, 70, random.randint(50,400))
    kyykka2.rect = pygame.Rect(200,200,kyykka_image.get_width(),kyykka_image.get_height())
    kyykka2.rect.x = random.randint(5, 948)
    kyykka2.rect.y = random.randint(-1100, -100)
    
    kyykka3 = Kyykka(WHITE, 50, 70, random.randint(50,400))
    kyykka3.rect = pygame.Rect(200,200,kyykka_image.get_width(),kyykka_image.get_height())
    kyykka3.rect.x = random.randint(5, 948)
    kyykka3.rect.y = random.randint(-1100, -100)
    
    kyykka4 = Kyykka(WHITE, 50, 70, random.randint(50,400))
    kyykka4.rect = pygame.Rect(200,200,kyykka_image.get_width(),kyykka_image.get_height())
    kyykka4.rect.x = random.randint(5, 948)
    kyykka4.rect.y = random.randint(-1100, -100)

    kyykka5 = Kyykka(WHITE, 50, 70, random.randint(50,400))
    kyykka5.rect = pygame.Rect(200,200,kyykka_image.get_width(),kyykka_image.get_height())
    kyykka5.rect.x = random.randint(5, 948)
    kyykka5.rect.y = random.randint(-1100, -100)

    kyykka8 = Kyykka(WHITE, 50, 70, random.randint(50,400))
    kyykka8.rect = pygame.Rect(200,200,kyykka_image.get_width(),kyykka_image.get_height())
    kyykka8.rect.x = random.randint(5, 948)
    kyykka8.rect.y = random.randint(-1100, -100)

    kyykka6 = Kyykka(WHITE, 50, 70, random.randint(50,400))
    kyykka6.rect = pygame.Rect(200,200,kyykka_image.get_width(),kyykka_image.get_height())
    kyykka6.rect.x = random.randint(5, 948)
    kyykka6.rect.y = random.randint(-1100, -100)

    kyykka7 = Kyykka(WHITE, 50, 70, random.randint(50,400))
    kyykka7.rect = pygame.Rect(200,200,kyykka_image.get_width(),kyykka_image.get_height())
    kyykka7.rect.x = random.randint(5, 948)
    kyykka7.rect.y = random.randint(-1100, -100)

    vasen_reuna = Reuna(RED, 50, 70)
    vasen_reuna.rect.x = -37
    vasen_reuna.rect.y = SCREENHEIGHT - 100

    oikea_reuna = Reuna(RED, 50, 70)
    oikea_reuna.rect.x = 988
    oikea_reuna.rect.y = SCREENHEIGHT - 100

    reuna_lista = pygame.sprite.Group()
    reuna_lista.add(vasen_reuna)
    reuna_lista.add(oikea_reuna)

    #all_coming_kyykka = pygame.sprite.Group()

    all_sprites_list.add(player)
    all_sprites_list.add(kyykka1)
    all_sprites_list.add(kyykka2)
    all_sprites_list.add(kyykka3)
    all_sprites_list.add(kyykka4)
    all_sprites_list.add(kyykka5)
    all_sprites_list.add(kyykka6)
    all_sprites_list.add(kyykka7)
    all_sprites_list.add(kyykka8)
    all_sprites_list.add(oikea_reuna)
    all_sprites_list.add(vasen_reuna)

    all_coming_kyykka = pygame.sprite.Group()
    all_coming_kyykka.add(kyykka1)
    all_coming_kyykka.add(kyykka2)
    all_coming_kyykka.add(kyykka3)
    all_coming_kyykka.add(kyykka4)
    all_coming_kyykka.add(kyykka5)
    all_coming_kyykka.add(kyykka6)
    all_coming_kyykka.add(kyykka7)
    all_coming_kyykka.add(kyykka8)
    #Loop pyörittää peliä, kunnes käyttäjä sammuttaa sen
    carryOn = True

    #Kello määrittää, kuinka usein näyttö päivittyy
    clock = pygame.time.Clock()
    counter, text = 0, '0'.rjust(3)
    infotext = 'Try to survive 40 sec!'
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    timerfont = pygame.font.SysFont('Consolas', 80)
    infofont = pygame.font.SysFont('Consolas', 20)

    WIN = False
    #Pääohjelma loop
    while carryOn:
        #Päätapahtuma loop
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    counter += 1
                    text = str(counter).rjust(3)
                    if counter == 40:
                        #pelin maali
                        WIN = True
                        carryOn = False
                if event.type == pygame.QUIT:
                    carryOn = False
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        carryOn = False
        
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                #player_image.moveLeft(10)
                player.moveLeft(10)
            if keys[pygame.K_RIGHT]:
                player.moveRigth(10)
                #player_image.moveLeft(10)

            ##GAME LOGIC
            for kyykka in all_coming_kyykka:
                speed+=0.0013
                kyykka.moveDown(speed)
                if kyykka.rect.y > SCREENWIDTH:
                    kyykka.changeSpeed(random.randint(10,50))
                    kyykka.rect.x = random.randint(5, 948)
                    kyykka.rect.y = random.randint(-1100, -100)
            kyykka_collision_list = pygame.sprite.spritecollide(player,all_coming_kyykka,False)
            reuna_collision_list = pygame.sprite.spritecollide(player, reuna_lista, False)
            #jos osuu reunaan
            for reuna in reuna_collision_list:
                print(counter)
                print("Ny ossui saatana!")
                webbrowser.open('https://www.youtube.com/watch?v=NUYvbT6vTPs')
                #End Of Game
                carryOn=False
            # jos osuu kyykkään
            for kyykka in kyykka_collision_list:
                print(counter)
                print("Ny ossui saatana!")
                #webbrowser.open('https://www.youtube.com/watch?v=NUYvbT6vTPs')
                #End Of Game
                carryOn=False
            all_sprites_list.update()

            #Piirretään kenttä, taustakuva, reunat ja timeri
            screen.fill(BLACK)
            dest = (50, 100)
            screen.blit(map_image, dest)
            #Teksti
            dest2 = (0, 100)
            screen.blit(timerfont.render(text, True, (255, 0, 0)), dest2)
            destinfo = (20, 0)
            screen.blit(timerfont.render(infotext, True, (255, 0, 0)), destinfo)
            #Reunat
            left_line = pygame.draw.line(screen, RED, [5, 0], [5, 1000], 15)
            right_line = pygame.draw.line(screen, RED, [995, 0], [995, 1000], 15)

            dest3 = (player.rect.x,player.rect.y)
            screen.blit(player_image, dest3)

            destkyykka1 = (kyykka1.rect.x,kyykka1.rect.y)
            screen.blit(kyykka_image, destkyykka1)
            destkyykka2 = (kyykka2.rect.x,kyykka2.rect.y)
            screen.blit(kyykka_image, destkyykka2)
            destkyykka3 = (kyykka3.rect.x,kyykka3.rect.y)
            screen.blit(kyykka_image, destkyykka3)
            destkyykka4 = (kyykka4.rect.x,kyykka4.rect.y)
            screen.blit(kyykka_image, destkyykka4)
            destkyykka5 = (kyykka5.rect.x,kyykka5.rect.y)
            screen.blit(kyykka_image, destkyykka5)
            destkyykka6 = (kyykka6.rect.x,kyykka6.rect.y)
            screen.blit(kyykka_image, destkyykka6)
            destkyykka7 = (kyykka7.rect.x,kyykka7.rect.y)
            screen.blit(kyykka_image, destkyykka7)
            destkyykka8 = (kyykka8.rect.x,kyykka8.rect.y)
            screen.blit(kyykka_image, destkyykka8)
            
            all_sprites_list.draw(screen)

            #
            pygame.display.flip()
            #Framerate limit = 60
            clock.tick(60)

    #
    return WIN