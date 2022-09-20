import pygame
from settings import FPS

class BaseScreen:
    
    def __init__(self, window) -> None:
        self.window = window
        self.clock = pygame.time.Clock()
        self.clock.tick(FPS)
    
    def draw(self) -> None:
        pass

    def getNextState(self) -> int:
        pass