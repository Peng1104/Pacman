import random
from sprites.moveableSprite import MoveableSprite

ALL_MOVEMENT_OPTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)] # Movimentos possíveis

# Criando a classe dos fantasmas
class Ghost(MoveableSprite):
    
    # Cria um novo fantasma na posição x, y
    def __init__(self, x, y, img, game, moveDelay=300, *groups):
        super().__init__(x, y, img, game, moveDelay, groups)

    # Update dos fantasmas
    def update(self) -> bool:
        if self._willMoveNow(): # Verifica se é hora de mover
            if random.random() > 0.75 or not super().update(): # 25% de chance de mudar de direção
                # Muda a direção do fantasma

                options = list(filter(self.__canMoveTo, ALL_MOVEMENT_OPTIONS)) # Lista das opções de movimento

                if len(options) > 0: # Se houver opções de movimento
                    if len(options) == 1:
                        self.updateSpeed(*options[0]) # Atualiza a velocidade do fantasma
                    else:
                        if (self.dx, self.dy) in options:
                            options.remove((self.dx, self.dy)) # Remove a direção atual

                        if len(options) > 1 and (-self.dx, -self.dy) in options:
                            options.remove((-self.dx, -self.dy)) # Remove a direção oposta se houver mais de uma opção
                    
                        self.updateSpeed(*random.choice(options)) # Escolhe uma nova direção aleatória

                return super().update() # Atualiza a posição do fantasma
            return True
        return False

    # Verifica se o fantasma pode se mover para a posição x, y usado em changeDirection
    def __canMoveTo(self, direction) -> bool:
        return self.game.canMoveTo(self.x + direction[0], self.y + direction[1])