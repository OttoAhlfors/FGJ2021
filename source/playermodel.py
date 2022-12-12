import pygame
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (210, 210 ,210)
GREEN = (20, 255, 140)
RED = (255, 0, 0)
PLAYERSKIN = (255, 160, 122)

class Playermodel(pygame.sprite.Sprite):
    speed = 2
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.ogimage = pygame.Surface([width, height])
        self.ogimage.fill(WHITE)
        self.ogimage.set_colorkey(WHITE)
        self.image = self.ogimage

        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
        pygame.draw.ellipse(self.image, PLAYERSKIN, [25, 15, 50, 30])
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

SCREENWIDTH = 1000
SCREENHEIGHT = 700
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FGJPeli-model-testi")

all_sprites_list = pygame.sprite.Group()

playerModel = Playermodel(RED, 100, 60)
playerModel.rect.x = 175
playerModel.rect.y = 200

all_sprites_list.add(playerModel)

carryOn = True
clock = pygame.time.Clock()

while carryOn:
    #Päätapahtuma loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            playerModel.moveUp(5)
        if keys[pygame.K_DOWN]:
            playerModel.moveDown(5)
        if keys[pygame.K_RIGHT]:
            playerModel.moveRight(5)
        if keys[pygame.K_LEFT]:
            playerModel.moveLeft(5)

        all_sprites_list.update()
        screen.fill(WHITE)
        all_sprites_list.draw(screen)

        playerModel.update()

        pygame.display.flip()
        clock.tick(60)
pygame.quit()