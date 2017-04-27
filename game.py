#The reason you have access to this mmodule is because you ran $pip install pygame
#pygame is NOT part of core like math or random
import pygame
#Import the player class from Player
from Player import Player
#Import check_events from the game_functions module
from game_functions import check_events

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

	the_player = Player(screen)

	#Main game loop. Run forever... (or until break)
	while 1: #use "while 1" if the code is fairly simple (game_on = True for more complex)
		screen.fill(background_color)

		check_events()
		
		#Draw the player
		the_player.draw_me()

		#Clear the screen for the next time through the loop
		pygame.display.flip()

#Start the game!
run_game()