import pygame
#Get the sys module so we can exit the program
import sys
from Bullet import Bullet

def check_events(the_player, screen, bullets):
	#The escape hatch (from while)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			#The user clicked the red X. Get out of the loop and kill the game.
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == 273:
				the_player.should_move("up", True)
			elif event.key == 274:
				the_player.should_move("down", True)
			elif event.key == 276:
				the_player.should_move("left", True)
			elif event.key == 275:
				the_player.should_move("right", True)
			elif event.key == 32: #spacebar to FIRE
				for direction in range(1, 5):
					new_bullet  = Bullet(screen, the_player, direction)
					bullets.add(new_bullet)
		elif event.type == pygame.KEYUP:
			if event.key == 273:
				the_player.should_move("up", False)
			elif event.key == 274:
				the_player.should_move("down", False)
			elif event.key == 276:
				the_player.should_move("left", False)
			elif event.key == 275:
				the_player.should_move("right", False)