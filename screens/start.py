from tkinter import font
import pygame
from os import path
from screens.baseScreen import BaseScreen
from assets import PACMAN_LOGO, load_assets
from pygame.font import SysFont
from settings import WIDTH

from settings import *

# Definindo as cores
COLOR_INACTIVE = (100, 80, 255)
COLOR_ACTIVE = (100, 200, 255)
COLOR_LIST_INACTIVE = (255, 100, 100)
COLOR_LIST_ACTIVE = (255, 150, 150)

OPTIONS = ["Level 1", "Level 2", "Level 3"]
class StartScreen(BaseScreen):
    
    def __init__(self, color_menu, color_option, x, y, w, h, window):
        super().__init__(window, None)
        self.color_menu = color_menu
        self.color_option = color_option
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.showOptions = False
        self.assets = load_assets()
        self.boxes = []


    def draw(self) -> None:
        self.window.fill((0, 0, 0))

        self.__drawPacman()
        self.__draw_main()
        self.__draw_opt()

        pygame.display.flip()

    def __drawPacman(self):
        font = SysFont('calibri', 100)
        text = font.render('Pac-man', True, (255, 255, 51))
        self.window.blit(text, (WIDTH/3,50))
        self.window.blit(self.assets[PACMAN_LOGO], (WIDTH/3 + text.get_width() + 30, 60))

    def __draw_main(self):
        pygame.draw.rect(self.window, self.color_menu, (self.x, self.y, self.w, self.h), 0)
        
        msg = SysFont('calibri', 50).render('Select Level', True, (0, 0, 0))
        self.window.blit(msg, (self.x + (self.w / 2 - msg.get_width() / 2), self.y + (self.h / 2 - msg.get_height() / 2)))
        
    # Desehando a lista de niveis
    def __draw_opt(self):
        if self.showOptions:
            for counter, text in enumerate(OPTIONS):
                
                box = pygame.draw.rect(self.window, self.color_option, (self.x, self.y + (counter+1) * self.h, self.w, self.h), 0)
                
                self.boxes.append((box, text))

                # write each option
                msg = SysFont('calibri', 50).render(text, 1, (0, 0, 0))
                self.window.blit(msg, (self.x + (self.w / 2 - msg.get_width() / 2),
                                    self.y + (counter+1)*self.h + (self.h / 2 - msg.get_height() / 2)))

    def getNextState(self) -> int:
        super().getNextState()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                return QUIT

            # Para o menu
            if event.type == pygame.MOUSEMOTION:
                if self.__hasClickedMainMenu(pos):
                    self.color_menu = COLOR_ACTIVE
                else:
                    self.color_menu = COLOR_INACTIVE

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:                    
                if self.__hasClickedMainMenu(pos):
                    self.showOptions = not self.showOptions
                
                if self.__chooseOption(pos):
                    return PLAYING

        return INIT

    # Detectar quando o mouse está em cima da caixa dos niveis
    def __chooseOption(self, pos):
        for option in self.boxes:
            box, text = option
            
            if box.left < pos[0] < box.right and box.top < pos[1] < box.bottom:
                self.level = text
                return True
        
        return False
    
    def __hasClickedMainMenu(self, pos):
        if self.x < pos[0] < self.x + self.w and self.y < pos[1] < self.y + self.h:
            return True
        return False