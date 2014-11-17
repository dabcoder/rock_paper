import random
import time


print("****************************************")
print("Welcome to the rock-paper-scissors game!")
print("****************************************")

#Create the data structure, a dictionary for the choices
options = {1: 'Paper', 2: 'Rock', 3:'Scissors'}
#and a tuple to list all the combinations
tup_comp = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

counter = 0
score = 0

while counter < 3:

	pchoice = int(input(print("Enter your choice: 1 - Rock, 2 - Paper, 3 - Scissors")))
	while pchoice > 3 or pchoice < 1:
		print("This is not a valid choice, try again")
		pchoice = int(input(print("Enter your choice: 1 - Rock, 2 - Paper, 3 - Scissors")))
	#Displays your choice
	print("you chose", options[pchoice])

	comp_choice = random.randrange(1, 3)
	print("processing")
	time.sleep(2)
	#Displays the computer's choice
	print("computer chose", options[comp_choice])

	result = (pchoice, comp_choice)

	time.sleep(2)


	if result == tup_comp[0] or result == tup_comp[4] or result == tup_comp[8]:
		print("it's a tie!")
	elif result == tup_comp[1] or result == tup_comp[5] or result == tup_comp[7]:
		print("you lose")
	elif result == tup_comp[2] or result == tup_comp[3] or result == tup_comp[6]:
		print("you win!")
		score += 1
	else:
		print("something wrong happened...")

	counter += 1

print("You beat the machine", score, " time(s)")

