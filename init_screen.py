import pygame
import random
from os import path

from settings import *

# Define color
COLOR_INACTIVE = (100, 80, 255)
COLOR_ACTIVE = (100, 200, 255)
COLOR_LIST_INACTIVE = (255, 100, 100)
COLOR_LIST_ACTIVE = (255, 150, 150)

class DropDown():
    # Test List
    option_list = ["Calibration", "Test"]

    def __init__(self, color_menu, color_option, x, y, w, h, screen):
        self.color_menu = color_menu
        self.color_option = color_option
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.screen = screen
        self.draw = False
        self.opt_list = []

    # Draw the initial button 'select mode'
    def draw_main(self, text=''):
        pygame.draw.rect(self.screen, self.color_menu, (self.x, self.y, self.w, self.h), 0)
        if text != '':
            font = pygame.font.SysFont(None, 50)
            msg = font.render(text, 1, (0, 0, 0))
            self.screen.blit(msg, (self.x + (self.w / 2 - msg.get_width() / 2), self.y + (self.h / 2 - msg.get_height() / 2)))
        
    # Draw list of option 'calibration' and 'test'
    def draw_opt(self, text=[]):
        if self.draw:
            for i, el in enumerate(text):
                box = pygame.draw.rect(
                    self.screen,
                    self.color_option,
                    (self.x, self.y + (i+1) * self.h, self.w, self.h),
                    0
                )
                
                self.opt_list.append((box, el))

                # write each option
                font = pygame.font.SysFont(None, 50)
                msg = font.render(el, 1, (0, 0, 0))
                self.screen.blit(msg, (self.x + (self.w / 2 - msg.get_width() / 2),
                                    self.y + (i+1)*self.h + (self.h / 2 - msg.get_height() / 2)))

    # Detect when the mouse is within the 'select mode' box
    def choose_main(self, pos):
        if self.x < pos[0] < self.x + self.w and self.y < pos[1] < self.y + self.h:
            return True
        else:
            return False
   
    # Detect when the mouse is within the option list
    def choose_opt(self, pos):
        for opt in self.opt_list:
            box, text = opt
            
            if box.left < pos[0] < box.right and box.top < pos[1] < box.bottom:
                return text
        
        return None

def init_screen(window):
    clock = pygame.time.Clock()

    # Declare element
    list1 = DropDown(COLOR_INACTIVE, COLOR_LIST_INACTIVE, WIDTH/3.25, HEIGHT/3, 400, 100, window)

    # Run program
    menu = True
    while menu:
        window.fill((0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # For the menu
            if event.type == pygame.MOUSEMOTION:
                if list1.choose_main(pos):
                    list1.color_menu = COLOR_ACTIVE
                else:
                    list1.color_menu = COLOR_INACTIVE

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and list1.choose_main(pos):
                    if list1.draw == False:
                        list1.draw = True
                    elif list1.draw == True:
                        list1.draw = False
                elif event.button == 1 and list1.choose_opt(pos):
                    return list1.choose_opt(pos)

        PACMAN_IMG = pygame.image.load(path.join(IMG_DIR, 'pacman.png')).convert_alpha()
        PACMAN_IMG = pygame.transform.scale(PACMAN_IMG, (50, 50))
    
        font = pygame.font.SysFont(None, 100)
        text = font.render('Pac-man', True, (255, 255, 51))
        window.blit(text, (WIDTH/3,50))
        window.blit(PACMAN_IMG, (WIDTH/3 + text.get_width() + 30, 60))
        list1.draw_main("Select level")
        list1.draw_opt(["Level 1", "Level 2", "Level 3"])

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()