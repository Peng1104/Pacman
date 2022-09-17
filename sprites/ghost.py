import random
from pygame.sprite import Group
from pygame.time import get_ticks
from Objects import MoveableSprite
from assets import GHOST_IMG
from Wall import canMoveTo

GHOSTS = Group() # Grupo contento todos os fantasmas

ALL_MOVEMENT_OPTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)] # Movimentos possíveis

# Criando a classe dos fantasmas
class Ghost(MoveableSprite):
    
    # Cria um novo fantasma na posição x, y
    def __init__(self, x, y, allSprites, moveDelay=300):
        super().__init__(x, y, GHOST_IMG, GHOSTS, allSprites)

        self.dx = -1 # Velocidade inicial do fantasma
        self.lastMovementTime = get_ticks()
        self.moveDelay = moveDelay

    # Update dos fantasmas
    def update(self) -> bool:
        if (get_ticks() - self.lastMovementTime) >= self.moveDelay: # Verifica se é hora de mover
            self.lastMovementTime = get_ticks() # Atualiza o tempo para o último movimento
        
            if random.random() > 0.75 or not super().update(): # 25% de chance de mudar de direção
                # Muda a direção do fantasma

                options = list(filter(self.__canMoveTo, ALL_MOVEMENT_OPTIONS)) # Lista das opções de movimento

                if len(options) == 1:
                    self.updateSpeed(*options[0]) # Atualiza a velocidade do fantasma
                
                else:
                    options.remove((self.dx, self.dy)) # Remove a direção atual

                    if len(options) > 1:
                        options.remove((-self.dx, -self.dy)) # Remove a direção oposta se houver mais de uma opção
                
                    self.updateSpeed(*random.choice(options)) # Escolhe uma nova direção aleatória

                return super().update() # Atualiza a posição do fantasma
            return True
        return False

    # Verifica se o fantasma pode se mover para a posição x, y usado em changeDirection
    def __canMoveTo(self, dx, dy) -> bool:
        return canMoveTo(self.x + dx, self.y + dy)