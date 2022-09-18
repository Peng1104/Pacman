from pygame.transform import rotate, flip
from pygame.surface import Surface
from pygame.rect import Rect
from sprites.moveableSprite import MoveableSprite

# Criando a classe pacman
class Pacman(MoveableSprite):

    def __init__(self, x, y, img, allSprites, moveDelay=120):
        super().__init__(x, y, img, moveDelay, allSprites)
        self.originalImage = img
        self.updateImage = True

    # Notifiy to update the image
    def updateSpeed(self, dx=0, dy=0) -> None:
        super().updateSpeed(dx, dy)
        self.updateImage = True

    def reset(self) -> None:
        self.image = self.originalImage
        super().reset()

    # Update The pacman image
    def update(self) -> bool:
        if super().update():

            if self.updateImage:
                self.updateImage = False

                if self.dx < 0:
                    self.image = flip(self.originalImage, True, False)
                elif self.dx > 0:
                    self.image = self.originalImage
                
                if self.dy < 0:
                    self.image = rotate(self.originalImage, 90)
                elif self.dy > 0:
                    self.image = rotate(self.originalImage, -90)
            
            return True
        return False

    # Rotacionando o pacman
    def rotate(self, angle) -> tuple[Surface, Rect]:
        rotated_surface = rotate(self.image, -angle)
        rotated_rect = rotated_surface.get_rect(center = self.rect.center)
        return rotated_surface, rotated_rect