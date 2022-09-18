from pygame import Surface
from pygame.sprite import Group
from sprites.baseSprite import BaseSprite
from settings import TILESIZE, BLUE, WIDTH, HEIGHT

WALLS = Group() # Grupo contento todas as paredes

# Verifica se é possível mover para a posição x, y
def canMoveTo(x, y) -> bool:
	# Verifica se as coordenadas estão dentro do mapa
	if x <= 0 or y <= 0 or x >= WIDTH or y >= HEIGHT:
		return False
		
	# Verifica se as coordenadas estão dentro de uma parede
	for wall in WALLS:
		if wall.inside(x, y):
			return False
	
	return True

# Classe das paredes
class Wall(BaseSprite):

	# Cria uma nova parede na posição x, y
	def __init__(self, x, y):
		super().__init__(x, y, Surface((TILESIZE, TILESIZE)), WALLS)
		self.image.fill(BLUE)