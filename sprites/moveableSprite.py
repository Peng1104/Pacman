from pygame.time import get_ticks
from sprites.baseSprite import BaseSprite
from settings import TILESIZE

class MoveableSprite(BaseSprite):
	
	def __init__(self, x, y, image, game, moveDelay=60, *groups):
		super().__init__(x, y, image, groups)

		self.startX = x
		self.startY = y
		self.game = game
		
		self.moveDelay = moveDelay
		self.lastMovementTime = get_ticks() - moveDelay

		self.dx = 0
		self.dy = 0

	def reset(self) -> None:
		self.x = self.startX
		self.y = self.startY
		
		self.rect.x = self.startX * TILESIZE
		self.rect.y = self.startY * TILESIZE

		self.lastMovementTime = get_ticks() - self.moveDelay

		self.dx = 0
		self.dy = 0
	
	def updateSpeed(self, dx=0, dy=0) -> None:
		self.dx = dx
		self.dy = dy

	def update(self) -> bool:
		if self._willMoveNow() and self.game.canMoveTo(self.x + self.dx, self.y + self.dy):
			self.lastMovementTime = get_ticks()

			self.x += self.dx
			self.y += self.dy

			self.rect.x = self.x * TILESIZE
			self.rect.y = self.y * TILESIZE

			return True
		
		return False
	
	def _willMoveNow(self) -> bool:
		return (get_ticks() - self.lastMovementTime) >= self.moveDelay