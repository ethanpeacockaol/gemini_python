# Number Guessing Game

import os




# Pipeline blueprint

# show welcome screen 1

# ask user when to start 2

# ask user for range and if they want to exclude any numbers
# allow negative numbers
# allow floats up to specified decimal place

# start the game

# yes no yes no yes no yes no

# stop by typing q



def welcome_screen():
	'''print the welcome screen.

	Args:
		None
	Returns:
		None
	'''
	# start by clearing the screen (unix only)
	os.system('clear')

	# get terminal size
	rows, columns = os.popen('stty size', 'r').read().split()
	rows = int(rows)
	columns = int(columns)

	# print game banner
	_ = [[print('~', end='') for i in range(columns)] for i in range(rows-1)]
	a = input(_ = [print('-', end='') for i in range(columns)])






if __name__ == '__main__':
    # show welcome screen
    welcome_screen()
