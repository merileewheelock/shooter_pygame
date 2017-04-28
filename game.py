#The reason you have access to this mmodule is because you ran $pip install pygame
#pygame is NOT part of core like math or random
import pygame
#Import the player class from Player
from Player import Player
#Import check_events from the game_functions module
from game_functions import check_events
#Get the enemy class
from Enemy import Enemy
#Get groupcollide and Group from the sprite module
from pygame.sprite import Group, groupcollide

#The core game functionality/loop
def run_game():
	#Init all pygame stuff
	pygame.init() #pygame is an object and init() is a method
	#Set up a tuple for the screen_size(horiz, vert)
	screen_size = (1000,800)
	#Set up a tuple for the background color
	background_color = (82,111,53) #RGB
	#Create a pygame screen to use
	screen = pygame.display.set_mode(screen_size) #set_mode is looking for a tuple from the pygame docs
	#Set a caption on the terminal window
	pygame.display.set_caption("A Heroic 3rd Person Shooter")

	the_player = Player(screen, "./images/Hero.png", 100, 100)
	bad_guy = Enemy(screen)
	the_player_group = Group()
	the_player_group.add(the_player) #"add" is like append since this is owned by pygame
	enemies = Group()
	enemies.add(bad_guy)
	bullets = Group()

	tick = 0

	#Main game loop. Run forever... (or until break)
	while 1: #use "while 1" if the code is fairly simple (game_on = True for more complex)
		tick += 1
		if tick % 50 == 0:
			enemies.add(Enemy(screen))
		screen.fill(background_color)

		check_events(the_player, screen, bullets)
		
		#Draw the player
		for player in the_player_group: #player will only be drawn based on hero_died below
			player.draw_me()

		#Update and draw the bullets
		for bullet in bullets:
			bullet.update()
			bullet.draw_bullet()

		#Update and draw the bad guy
		for bad_guy in enemies:
			bad_guy.update_me(the_player)
			bad_guy.draw_me()

		#Check for collisions...
		hero_died = groupcollide(the_player_group, enemies, True, False) #will make hero die when they collide
		# print hero_died
		groupcollide(bullets, enemies, True, True)

		#Clear the screen for the next time through the loop
		pygame.display.flip()

#Start the game!
run_game()