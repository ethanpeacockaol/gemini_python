# shebang thing python whats windows?

#TODO: get the computer to generate a random number, and the user tries to guess it


# while loop until game quit
# limit range 0 to 10 inclusive
# take input through into or lowercase forced word string
# validate
# yes or no
# repeat if not quit

# clear the screen
import os



# game on flag
run_game = True

def welcome():
	"""
	this prints the welcome screen and selection menu
	"""
	# clear screen
	os.system(' clear')
	# set width of border
	cell_width = 30
	# print border
	_ = [print('~', end='') for i in range(cell_width)]
	print()
	print("Number Guessing Game")
	print()
	# print border
	_ = [print('~', end='') for i in range(cell_width)]
	
def start_game():
	# start menu
	welcome()

# prevent execution on import
if __name__ == "__main__":
	start_game()