# Sean A
# Rock Paper Scissors
# Use lists and the random choice function to create a fun rock paper scissors experience
import time
from random import choice

rps = ["Rock", "Paper", "Scissors"]

userChoice = input("Please enter your move (Rock/Paper/Scissors):")
pyChoice = choice(rps)

print("Prepare for battle...")
time.sleep(2)
print("\nRock")
time.sleep(0.5)
print("Paper")
time.sleep(0.5)
print("Scissors")
time.sleep(0.4)
print("Shoot!")


print("\nYou chose {} and I chose {}!".format(userChoice, pyChoice))

