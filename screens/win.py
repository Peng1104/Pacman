import pygame
from os import path
from screens.baseScreen import BaseScreen

from settings import IMG_DIR, FPS, INIT, QUIT, WIN

class WinScreen(BaseScreen):

    def __init__(self, window):
       super().__init__(window)

    def draw(self) -> None:
        # Carrega o fundo da tela inicial
        background = pygame.image.load(path.join(IMG_DIR, 'win.png')).convert()
        background_rect = background.get_rect()
        
        self.window.blit(background, background_rect)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    
    def getNextState(self) -> int:
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                return QUIT

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    return INIT
        
        return WIN