import pygame
from settings import FPS

class BaseScreen:
    
    def __init__(self, window, level) -> None:
        self.window = window
        self.level = level

        self.clock = pygame.time.Clock()
        self.clock.tick(FPS)
    
    def draw(self) -> None:
        pass

    def getNextState(self) -> int:
        self.draw()
        pass