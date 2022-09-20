import pygame
from os import path
from screens.baseScreen import BaseScreen
from assets import PACMAN_LOGO, load_assets
from pygame.font import SysFont

from settings import *

# Definindo as cores
COLOR_INACTIVE = (100, 80, 255)
COLOR_ACTIVE = (100, 200, 255)
COLOR_LIST_INACTIVE = (255, 100, 100)
COLOR_LIST_ACTIVE = (255, 150, 150)
class StartScreen(BaseScreen):
    
    def __init__(self, color_menu, color_option, x, y, w, h, window, isDrawn=False, optionList=["Level 1", "Level 2", "Level 3"]):
        super().__init__(window)
        self.color_menu = color_menu
        self.color_option = color_option
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.isDrawn = isDrawn
        self.optionList = optionList
        self.assets = load_assets()


    def draw(self) -> None:
        self.__drawPacman()
        self.__draw_main('Select Level')
        self.__draw_opt(self.optionList)


    def __drawPacman(self):
        font = SysFont(None, 100)
        text = font.render('Pac-man', True, (255, 255, 51))
        self.window.blit(text, (WIDTH/3,50))
        self.window.blit(self.assets[PACMAN_LOGO], (WIDTH/3 + text.get_width() + 30, 60))

    # Desenhando o botão inicial 'select mode'
    def __draw_main(self, text=''):
        pygame.draw.rect(self.window, self.color_menu, (self.x, self.y, self.w, self.h), 0)
        if text != '':
            font = SysFont(None, 50)
            msg = font.render(text, 1, (0, 0, 0))
            self.window.blit(msg, (self.x + (self.w / 2 - msg.get_width() / 2), self.y + (self.h / 2 - msg.get_height() / 2)))
        
    # Desehando a lista de niveis
    def __draw_opt(self, text=[]):
        if self.isDrawn:
            for i, el in enumerate(text):
                box = pygame.draw.rect(
                    self.window,
                    self.color_option,
                    (self.x, self.y + (i+1) * self.h, self.w, self.h),
                    0
                )
                
                self.optionList.append((box, el))

                # write each option
                font = pygame.font.SysFont(None, 50)
                msg = font.render(el, 1, (0, 0, 0))
                self.window.blit(msg, (self.x + (self.w / 2 - msg.get_width() / 2),
                                    self.y + (i+1)*self.h + (self.h / 2 - msg.get_height() / 2)))

    def getNexState(self) -> int:

        while True:
            self.window.fill((0, 0, 0))
            self.__processEvent()
        
         
            self.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return QUIT

    def __processEvent(self) -> None:
        for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                # Para o menu
                if event.type == pygame.MOUSEMOTION:
                    if self.__chooseMain(pos):
                        self.color_menu = COLOR_ACTIVE
                    else:
                        self.color_menu = COLOR_INACTIVE

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.__chooseMain(pos):
                        if self.isDrawn == False:
                            self.isDrawn = True
                        elif self.isDrawn == True:
                            self.isDrawn = False
                    elif event.button == 1 and self.__chooseOption(pos):
                        return self.__chooseOption(pos)

    def __chooseMain(self, pos):
        if self.x < pos[0] < self.x + self.w and self.y < pos[1] < self.y + self.h:
            return True
        else:
            return False

    # Detectar quando o mouse está em cima da caixa dos niveis
    def __chooseOption(self, pos):
        for option in self.optionList:
            box, text = option
            
            if box.left < pos[0] < box.right and box.top < pos[1] < box.bottom:
                return text
        
        return None