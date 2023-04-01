# Sean A
# Rock Paper Scissors
# Use loops to determine a winner in a 3-round match
import os
import time
from random import choice

rps = ["Rock", "Paper", "Scissors"]

cwins = 0
pwins = 0
print("Rock Paper Scissors, best of 3!")

while cwins < 2 and pwins < 2:
    userChoice = input("Please enter your move (Rock/Paper/Scissors):").capitalize()
    pyChoice = choice(rps)

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
            cwins += 1
        elif pyChoice == "Scissors":
            print("You win!")
            pwins += 1
        elif pyChoice == "Rock":
            print("It's a tie!")

    # User chooses paper
    elif userChoice == "Paper":
        if pyChoice == "Scissors":
            print("You lose!")
            cwins += 1
        elif pyChoice == "Rock":
            print("You win!")
            pwins += 1
        elif pyChoice == "Paper":
            print("It's a tie!")

    # User chooses scissors
    elif userChoice == "Scissors":
        if pyChoice == "Rock":
            print("You lose!")
            cwins += 1
        elif pyChoice == "Paper":
            print("You win!")
            pwins += 1
        elif pyChoice == "Scissors":
            print("It's a tie!")
    else:
        print("Unable to determine a result, you may have typed your choice incorrectly.")

# Clearing the Screen
time.sleep(0.5)
os.system("clear")

# Determining final winner
if cwins == 2:
    print("The computer !")
elif pwins == 2:
    print("Congratulations, you won!")

# Printing the score
print("\nFinal Score")
print(f"Player: {pwins}")
print(f"Computer: {cwins}")
