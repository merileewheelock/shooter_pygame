import pygame
from pygame.sprite import Sprite
import math

class Enemy(Sprite):
	def __init__(self, screen):
		super(Enemy,self).__init__()
		self.image = pygame.image.load("./images/2.png")
		self.speed = 3
		self.x = 900
		self.y = 400
		self.screen = screen
		self.rect = self.image.get_rect()

	def update_me(self, the_player):
		dx = self.x - the_player.x
		dy = self.y - the_player.y
		dist = math.hypot(dx, dy)
		dx = dx / dist
		dy = dy / dist
		self.x -= dx * self.speed
		self.y -= dy * self.speed
		self.rect.left = self.x
		self.rect.top = self.y

	def draw_me(self):
		self.screen.blit(self.image, [self.x, self.y])