import random
import time

print("****************************************")
print("Welcome to the rock-paper-scissors game!")
print("****************************************")

#Create the data structure, a dictionary for the choices
options = {1: 'Paper', 2: 'Rock', 3:'Scissors'}

#Store the player's choice
def players_choice():
	#Get the players choice
	while True:
		pchoice = int(input("Enter your choice:\n 1 - Paper\n 2 - Rock\n 3 - Scissors\n"))
		if (pchoice >= 1 and pchoice <= 3):
			break
		print("you chose", options[pchoice])
	return pchoice

def computers_choice():
	#Computer chooses 
	comp_choice = random.randrange(1, 3)
	#Displays the computer's choice
	print("computer chose", options[comp_choice])
	return comp_choice

def compare(pchoice, comp_choice):
	result = (pchoice, comp_choice)
	#comparisons
	if result == (1, 1) or result == (2, 2) or result == (3, 3):
		print("it's a tie!")
	elif result == (1, 2) or result == (2, 3) or result == (3, 1):
		print("you win")
	elif result == (1, 3) or result == (2, 1) or result == (3, 2):
		print("you lose!")
	else:
		print("Something went wrong")

def turns():
	for counter in range(1, 4):
		print("this is round", counter)
		pchoice = players_choice()
		comp_choice = computers_choice()
		compare(pchoice, comp_choice)
	exit()

if __name__ == '__main__':
	turns()
