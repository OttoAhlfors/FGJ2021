import pygame, sys, os, random
import data.engine as e
clock = pygame.time.Clock()

from pygame.locals import *
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init() # initiates pygame
pygame.mixer.set_num_channels(64)

pygame.display.set_caption('Trouble in Teekkari Town')

WINDOW_SIZE = (1000,900)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window

display = pygame.Surface((300,200)) # used as the surface for rendering, which is scaled

moving_right = False
moving_left = False
moving_up = False
moving_down = False

true_scroll = [0,0]


TILE_SIZE = 32
def load_map(path):
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
        
    return game_map

class button_obj():
    def __init__(self, loc):
        self.loc = loc

    def render(self, surf, scroll):
        surf.blit(jumper_img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 8, 9)

    def collision_test(self, rect):
        button_rect = self.get_rect()
        return button_rect.colliderect(rect)
jumper_img = pygame.image.load("data/images/jumper.png")
game_map = load_map('data/map/MAPV1')
map_image = pygame.image.load("data/map/MAPv1.png")
e.load_animations('data/images/entities/')

pygame.mixer.music.load('data/audio/music.wav')
#pygame.mixer.music.play(-1)



player = e.entity(475,1115,5,13,'player')

#nappeja
koti = button_obj((2470, 1075))
jatkot = button_obj((2225, 107))
etkot = button_obj((110, 235))
garden1 = button_obj((2675, 1325))
garden2 = button_obj((2675, 1300))
garden3 = button_obj((2675, 1350))
strippiklubi = button_obj((3660, 1750))

testi = button_obj((200,200))

metsa = button_obj((490, 1750))

sauna = button_obj((3755, 45))


while True: # game loop
    display.fill((0,0,0)) # clear screen by filling it with black

    

    true_scroll[0] += (player.x-true_scroll[0]-152)/20
    true_scroll[1] += (player.y-true_scroll[1]-106)/20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])
    
    

    
    tile_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            
            x += 1
            if tile == "W":
                
                pygame.draw.rect(display, (0,0,0), pygame.Rect(x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1], TILE_SIZE,TILE_SIZE))
            
            if tile == "W":
                tile_rects.append(pygame.Rect(x * TILE_SIZE,y * TILE_SIZE,TILE_SIZE, TILE_SIZE))
        
        y +=1

    display.blit((map_image), (32-scroll[0],0-scroll[1]))
    

    


    player_movement = [0,0]
    if moving_right == True:
        player_movement[0] += 5
    if moving_left == True:
        player_movement[0] -= 5
    if moving_up:
        player_movement[1]-=5
    if moving_down:
        player_movement[1]+=5
    
    

    if player_movement[0] == 0:
        player.set_action('idle')
    if player_movement[0] > 0:
        player.set_flip(False)
        player.set_action('run')
    if player_movement[0] < 0:
        player.set_flip(True)
        player.set_action('run')
    if player_movement[1] > 0:
        player.set_flip(False)
        player.set_action('run')
    if player_movement[1] < 0:
        player.set_flip(True)
        player.set_action('run')

    collision_types = player.move(player_movement,tile_rects)

    

    player.change_frame(1)
    player.display(display,scroll)

    koti.render(display,scroll)
    etkot.render(display,scroll)
    jatkot.render(display,scroll)
    if jatkot.collision_test(player.obj.rect):
        player.set_pos(475,1115)
    strippiklubi.render(display,scroll)
    if strippiklubi.collision_test(player.obj.rect):
        player.set_pos(475,1115)

    testi.render(display,scroll)
    if testi.collision_test(player.obj.rect):
        player.set_pos(3755,45)
    
    sauna.render(display,scroll)
    if sauna.collision_test(player.obj.rect):
        player.set_pos(75,2100)

    garden2.render(display,scroll)
    garden1.render(display,scroll)
    garden3.render(display,scroll)
    if garden1.collision_test(player.obj.rect) or garden2.collision_test(player.obj.rect) or garden3.collision_test(player.obj.rect):
        player.set_pos(2850,1300)

    if metsa.collision_test(player.obj.rect):
        player.set_pos(75,2100)
        

    for event in pygame.event.get(): # event loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:

            if event.key == pygame.K_LEFT or event.key == ord('a'):
                #print("left")
                moving_left = True
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
              #  print("right")
                moving_right = True
            if event.key == pygame.K_UP or event.key == ord('w'):
                #print("up")
                moving_up = True
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                #print("down")
                moving_down = True

        if event.type == KEYUP:

            if event.key == pygame.K_LEFT or event.key == ord('a'):
                #print("left")
                moving_left = False
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                #print("right")
                moving_right = False
            if event.key == pygame.K_UP or event.key == ord('w'):
                #print("up")
                moving_up = False
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                #print("down")
                moving_down = False
        
    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
    clock.tick(60)
