from pygame.transform import rotate, flip
from pygame.surface import Surface
from pygame.rect import Rect
from Objects import MoveableSprite
from assets import PACMAN_IMG

# Criando a classe pacman
class Pacman(MoveableSprite):

    def __init__(self, x, y, allSprites):
        super().__init__(x, y, PACMAN_IMG, allSprites)
        self.dx = 1 # Change the start speed of the pacman
        self.updateImage = True

    # Notifiy to update the image
    def updateSpeed(self, dx=0, dy=0) -> None:
        super().updateSpeed(dx, dy)
        self.updateImage = True

    # Update The pacman image
    def update(self) -> bool:
        if super().update():

            if self.updateImage:
                self.updateImage = False

                if self.dy < 0:
                    self.image = flip(PACMAN_IMG, False, True)
                elif self.dy > 0:
                    self.image = PACMAN_IMG
                
                if self.dx < 0:
                    self.image = rotate(self.image, 90)
                elif self.dx > 0:
                    self.image = rotate(self.image, -90)
            
            return True
        return False

    # Rotacionando o pacman
    def rotate(self, angle) -> tuple[Surface, Rect]:
        rotated_surface = rotate(self.image, -angle)
        rotated_rect = rotated_surface.get_rect(center = self.rect.center)
        return rotated_surface, rotated_rect