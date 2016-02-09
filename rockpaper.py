import random
import time
import random

print("****************************************")
print("Welcome to the rock-paper-scissors game!")
print("****************************************")

#Create the data structure, a dictionary for the choices
options = {1: 'Paper', 2: 'Rock', 3:'Scissors'}
#and a tuple to list all the combinations
tup_comp = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

#Store the player's choice
def players_choice():
	#Get the players choice
	pchoice = int(input(print("Enter your choice:\n 1 - Rock\n 2 - Paper\n 3 - Scissors")))
	while pchoice > 3 or pchoice < 1:
		print("This is not a valid choice, try again")
		pchoice = int(input(print("Enter your choice:\n 1 - Rock\n 2 - Paper\n 3 - Scissors")))
	#Displays your choice
	print("you chose", options[pchoice])
	return pchoice

def computers_choice():
	#Computer chooses 
	comp_choice = random.randrange(1, 3)
	#Displays the computer's choice
	print("computer chose", options[comp_choice])
	return comp_choice

def compare(pchoice, comp_choice):
	print("comparing...")
	result = (players_choice(), computers_choice())
	#comparisons
	print(result)
	if result == tup_comp[0] or result == tup_comp[4] or result == tup_comp[8]:
		print("it's a tie!")
	elif result == tup_comp[1] or result == tup_comp[5] or result == tup_comp[6]:
		print("you lose")
	elif result == tup_comp[2] or result == tup_comp[3] or result == tup_comp[7]:
		print("you win!")
	else:
		print("Something went wrong")

def turns():
	counter = 1
	#I originally wanted to make 3 rounds but it doesn't seem to work
	while counter < 4:
		print("this is round", counter)
		pchoice = players_choice()
		comp_choice = computers_choice()
		compare(pchoice, comp_choice)
		counter += 1
	exit()

turns()
