import pygame


import pygame
def click(self):
         waiting = True
         while waiting:
             self.clock.tick(FPS)
             for evento in pygame.event.get():
                 if evento.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                 if evento.type == pygame.KEYUP:
                    waiting = False