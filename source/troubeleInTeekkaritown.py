import pygame, sys
clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()

pygame.display.set_caption("Trouble in Teekkari Town")

WINDOW_SIZE = (1200,800)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)
display = pygame.Surface((300,200)) 

true_scroll = [0,0]

player_image = pygame.image.load("Hahmo.png")
map_image = pygame.image.load("MAPv1.png")
#player_image.set_colorkey((255,255,255))

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

game_map = load_map('MAPV1')

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {"top":False,"bottom":False,"left":False,"right":False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types["left"] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types["rigth"] = True
    
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types["bottom"] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types["top"] = True
    return rect, collision_types

moving_left = False
moving_right = False
moving_up = False
moving_down = False



player_rect = pygame.Rect(450,1100,player_image.get_width(),player_image.get_height())



while True:
    display.fill((0,0,0))

    true_scroll[0] += (player_rect.x-true_scroll[0]-77)/10
    true_scroll[1] += (player_rect.y-true_scroll[1]-56)/10
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])


    display.blit((map_image), (32-scroll[0],0-scroll[1]))

    
    tile_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            
            x += 1
            if tile == "W":
                #display.blit((0,0,0), (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
                pygame.draw.rect(display, (0,0,0), pygame.Rect(x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1], TILE_SIZE,TILE_SIZE))
            if tile == "E":
                end_rect = pygame.Rect(x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1], TILE_SIZE,TILE_SIZE)
            if tile == "G":
                test_rect = pygame.Rect(x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1], TILE_SIZE,TILE_SIZE)
                
            if tile == "W":
                tile_rects.append(pygame.Rect(x * TILE_SIZE,y * TILE_SIZE,TILE_SIZE, TILE_SIZE))
        
        y +=1

    

    
    pygame.draw.rect(display, (255, 0, 0), end_rect)
    pygame.draw.rect(display, (255, 0, 0), test_rect)
    player_movement = [0,0]

    if moving_left:
        player_movement[0]-=5
    if moving_right:
        player_movement[0]+=5
    if moving_up:
        player_movement[1]-=5
    if moving_down:
        player_movement[1]+=5

    player_rect,collisions = move(player_rect,player_movement,tile_rects)
    display.blit(player_image,(player_rect.x - scroll[0],player_rect.y - scroll[1]))


    if player_rect.colliderect(end_rect):
        print("Hit E")
    if player_rect.colliderect(end_rect):
        print("Hit G")


    for event in pygame.event.get():
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
    
    surf = pygame.transform.scale(display,WINDOW_SIZE)
    screen.blit(surf,(0,0))
    pygame.display.update()
    clock.tick(60)

