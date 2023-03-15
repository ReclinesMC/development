# Sean A
# Rock Paper Scissors
# Use if and elif to make rock paper scissors choose a winner
import time
from random import choice

rps = ["Rock", "Paper", "Scissors"]

userChoice = input("Please enter your move (Rock/Paper/Scissors):").capitalize()
pyChoice = choice(rps)

print("Prepare for battle...")
time.sleep(1.5)
print("\nRock")
time.sleep(0.5)
print("Paper")
time.sleep(0.5)
print("Scissors")
time.sleep(0.4)
print("Shoot!")

print("\nYou chose {} and I chose {}!".format(userChoice, pyChoice))
print()

# User chooses rock
if userChoice == "Rock":
	if pyChoice == "Paper":
		print("You lose!")
	elif pyChoice == "Scissors":
		print("You win!")
	elif pyChoice == "Rock":
		print("It's a tie!")

# User chooses paper
elif userChoice == "Paper":
	if pyChoice == "Scissors":
		print("You lose!")
	elif pyChoice == "Rock":
		print("You win!")
	elif pyChoice == "Paper":
		print("It's a tie!")

# User chooses scissors
elif userChoice == "Scissors":
	if pyChoice == "Rock":
		print("You lose!")
	elif pyChoice == "Paper":
		print("You win!")
	elif pyChoice == "Scissors":
		print("It's a tie!")
else:
	print("Unable to determine a result, you may have typed your choice incorrectly.")
