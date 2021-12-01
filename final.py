import pygame
import random
from os import path
from click import click

from settings import *

def final_screen(self):
        if not self.running:
            return 
        self.screen.fill(BLACK)
        self.draw_text('Game Over', 30, WHITE, WIDTH/2, HEIGHT/4)
        self.draw_text('Click for try again', 22, WHITE, WIDTH/2, HEIGHT * 4/5)

        pygame.display.flip()
        self.click()
        pass
