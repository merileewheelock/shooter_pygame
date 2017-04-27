import pygame
#Get the sys module so we can exit the program
import sys

def check_events():
	#The escape hatch (from while)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			#The user clicked the red X. Get out of the loop and kill the game.
			sys.exit()