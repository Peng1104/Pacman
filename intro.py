import pygame
import os
import sprites
import settings

class screem:
    def start(self):
        pygame.init()
        pygame.mixer.init()
        self.screem = pygame.display.set.mode((settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption(settings.GAMETITTLE)
        self.tick = pygame.time.clok()
        self.running = True 
        self.load_effect()

    def load_effects(self):
        image_path = os.path.join(os.getcwd(), 'img')
    print (image_path)