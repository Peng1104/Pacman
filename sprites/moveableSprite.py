from pygame.time import get_ticks
from sprites.wall import canMoveTo
from sprites.baseSprite import BaseSprite
from settings import TILESIZE

class MoveableSprite(BaseSprite):
	
	def __init__(self, x, y, image, moveDelay=60, *groups):
		super().__init__(x, y, image, groups)
		
		self.moveDelay = moveDelay
		self.lastMovementTime = get_ticks()

		self.dx = 0
		self.dy = 0
	
	def updateSpeed(self, dx=0, dy=0) -> None:
		self.dx = dx
		self.dy = dy

	def update(self) -> bool:
		if self._willMoveNow() and canMoveTo(self.x + self.dx, self.y + self.dy):
			self.lastMovementTime = get_ticks()

			self.x += self.dx
			self.y += self.dy

			self.rect.x = self.x * TILESIZE
			self.rect.y = self.y * TILESIZE

			return True
		
		return False
	
	def _willMoveNow(self) -> bool:
		return (get_ticks() - self.lastMovementTime) >= self.moveDelay