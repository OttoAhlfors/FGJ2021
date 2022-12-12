import pygame
import sys
import random
 
pygame.init()


class Control:
    def __init__(self):
        self.done = False
        self.fps = 60
        self.screen = pygame.display.set_mode((1000,900))
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]
    def flip_state(self):
        self.state.done = False
        previous,self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous
    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, dt)
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            self.state.get_event(event)
    def main_game_loop(self):
        #Pää while-looppi
        while not self.done:
            delta_time = self.clock.tick(self.fps)/1000.0
            self.event_loop()
            self.update(delta_time)
            pygame.display.update()
             
class MenuManager:
    def __init__(self):
        #Valikko tekstin värit
        self.selected_index = 0
        self.last_option = None
        self.selected_color = (0,200,0)
        self.deselected_color = (255,255,255)
         
    def draw_menu(self, screen):
        #Kuvat sun muut
        sauna_image = pygame.image.load("fgj2021\TTTv2\data\images\sauna.jpg")
        dest = (0, 0)
        screen.blit(sauna_image, dest)
        info = 'You are in a teekkarisauna!'
        info2 = 'but you do not remember your address'
        font = pygame.font.SysFont('arial', 50)
        desttext = (50, 80)
        screen.blit(font.render(info, True, (245,245,245)), desttext)
        font2 = pygame.font.SysFont('arial', 50)
        desttext2 = (60, 120)
        screen.blit(font2.render(info2, True, (245,245,245)), desttext2)
        for i,opt in enumerate(self.rendered["des"]):
            opt[1].center = (self.screen_rect.centerx, self.from_bottom+i*self.spacer)
            if i == self.selected_index:
                
                rend_img,rend_rect = self.rendered["sel"][i]
                rend_rect.center = opt[1].center
                screen.blit(rend_img,rend_rect)
            else:
                screen.blit(opt[0],opt[1])
    
    def update_menu(self):
        self.change_selected_option()
         
    def get_event_menu(self, event):
        if event.type == pygame.KEYDOWN:
            #VAlikko indeksi
            if event.key in [pygame.K_UP]:
                self.change_selected_option(-1)
            elif event.key in [pygame.K_DOWN]:
                self.change_selected_option(1)
            elif event.key == pygame.K_RETURN:
                self.select_option(self.selected_index)

    def pre_render_options(self):
        #Laittaa tekstin valikkoon
        font_deselect = pygame.font.SysFont("arial", 50)
        font_selected = pygame.font.SysFont("arial", 60)
 
        rendered_msg = {"des":[],"sel":[]}
        for option in self.options:
            d_rend = font_deselect.render(option, 1, self.deselected_color)
            d_rect = d_rend.get_rect()
            s_rend = font_selected.render(option, 1, self.selected_color)
            s_rect = s_rend.get_rect()
            rendered_msg["des"].append((d_rend,d_rect))
            rendered_msg["sel"].append((s_rend,s_rect))
        self.rendered = rendered_msg
 
    def select_option(self, i):
        if i == len(self.next_list):
            self.quit = True
        else:
            self.next = self.next_list[i]
            self.done = True
            self.selected_index = 0
 
    def change_selected_option(self, op=0):
        #Vaihtaa valikon
        if op:
            self.selected_index += op
            max_ind = len(self.rendered['des'])-1
            if self.selected_index < 0:
                self.selected_index = max_ind
            elif self.selected_index > max_ind:
                self.selected_index = 0

#Asettaa seuraavan valikon nimen      
class States(Control):
    def __init__(self):
        Control.__init__(self)
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None
   
#Päävalikko                 
class Menu(States, MenuManager):
    def __init__(self):
        States.__init__(self)
        MenuManager.__init__(self)
        self.next = 'options'
        self.options = ['Choose a key', 'Go back']
        self.next_list = ['options']
        self.pre_render_options()
        self.from_bottom = 200
        self.spacer = 75
    def cleanup(self):
        print('cleaning up Main Menu state stuff')
    def startup(self):
        print('starting Main Menu state stuff')
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        self.get_event_menu(event)
    def update(self, screen, dt):
        self.update_menu()
        self.draw(screen)
    def draw(self, screen):
        screen.fill((0,0,0))
        self.draw_menu(screen)

#Tässä valitaan avain
class Options(States, MenuManager):
    def __init__(self):
        States.__init__(self)
        MenuManager.__init__(self)
        self.next = 'end'
        self.options = ['Key - Laserpuisto', 'Key - Punkkerikatu', 'Key - Timppa', 'Return']
        self.next_list = ['end1', 'end2', 'end3', 'menu']
        self.from_bottom = 200
        self.spacer = 75
        self.selected_color = (0,200,0)
        self.deselected_color = (255,255,255)
        self.pre_render_options()
    def cleanup(self):
        print('cleaning up Options state stuff')
    def startup(self):
        print('starting Options state stuff')
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        self.get_event_menu(event)
    def update(self, screen, dt):
        self.update_menu()
        self.draw(screen)
    def draw(self, screen):
        screen.fill((0,0,0))
        self.draw_menu(screen)
        self.next = 'menu'

#Laserpuisto avain
class End1(States, MenuManager):
    def __init__(self):
        States.__init__(self)
        MenuManager.__init__(self)
        self.next = 'options'
        self.options = ['Carrying: Laserpuisto key']
        self.next_list = []
        self.from_bottom = 200
        self.spacer = 75
        self.selected_color = (0,200,0)
        self.deselected_color = (255,255,255)
        self.pre_render_options()
    def cleanup(self):
        print('cleaning up End1 state stuff')
        AVAIN = 1
    def startup(self):
        print('starting End1 state stuff')
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        self.get_event_menu(event)
    def update(self, screen, dt):
        self.update_menu()
        self.draw(screen)
    def draw(self, screen):
        screen.fill((0,0,0))
        self.draw_menu(screen)
        self.next = 'menu'

#Punkkerikatu avain
class End2(States, MenuManager):
    def __init__(self):
        States.__init__(self)
        MenuManager.__init__(self)
        self.next = 'options'
        self.options = ['Carrying: Punkkerikatu key']
        self.next_list = []
        self.from_bottom = 200
        self.spacer = 75
        self.selected_color = (0,200,0)
        self.deselected_color = (255,255,255)
        self.pre_render_options()
    def cleanup(self):
        print('cleaning up End2 state stuff')
        AVAIN = 2
    def startup(self):
        print('starting End2 state stuff')
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        self.get_event_menu(event)
    def update(self, screen, dt):
        self.update_menu()
        self.draw(screen)
    def draw(self, screen):
        screen.fill((0,0,0))
        self.draw_menu(screen)
        self.next = 'menu'

#Timppa avain
class End3(States, MenuManager):
    def __init__(self):
        States.__init__(self)
        MenuManager.__init__(self)
        self.next = 'options'
        self.options = ['Carrying: Timppa key',]
        self.next_list = []
        self.from_bottom = 200
        self.spacer = 75
        self.selected_color = (0,200,0)
        self.deselected_color = (255,255,255)
        self.pre_render_options()
    def cleanup(self):
        print('cleaning up End3 state stuff')
        AVAIN = 3
    def startup(self):
        print('starting End3 state stuff')
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        self.get_event_menu(event)
    def update(self, screen, dt):
        self.update_menu()
        self.draw(screen)
    def draw(self, screen):
        screen.fill((0,0,0))
        self.draw_menu(screen)
        self.next = 'menu'

 #Itse ohjelma
def minigame_key():
    app = Control()
    #mahd. valikkopaikat
    state_dict = {
        'menu': Menu(),
        'options': Options(),
        'end1': End1(),
        'end2': End2(),
        'end3': End3()
    }
    app.setup_states(state_dict, 'menu')
    app.main_game_loop()
    AVAIN = random.randint(1,3)
    return AVAIN