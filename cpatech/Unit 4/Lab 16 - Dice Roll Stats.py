# Sean A
# Dice Rolling Simulator
# Based on how many dices are rolled and how many times they are rolled, simulate the experience of rolling them
import os as s
import random as r

diceCount = ""
rollCount = ""
rolls = {}
num = 0
diceTotal = 0

# Get the dice count, can only pass if it's an int
while type(diceCount) != int:
    try:
        diceCount = int(input("How many six-sided dice would you like to roll?"))
    except:
        s.system("clear")
        print("You must enter a valid integer.")
        continue
    if diceCount < 1:
        s.system("clear")
        print("You must enter a positive integer.")
        diceCount = ""
        continue

# Get the roll count, only pass if int
while type(rollCount) != int:
    try:
        rollCount = int(input(f"How many times would you like to roll {diceCount} dice?"))
    except:
        s.system("clear")
        print("You must enter a valid integer.")
        continue
    if rollCount < 1:
        s.system("clear")
        print("You must enter a positive integer.")
        rollCount = ""
        continue

# Now I must use the roll count and dice count
s.system("clear")
print("[ Dice Roll Simulator ]".center(50, "="))
print(f"\nDice rolled: {diceCount}")
print(f"Rolls simualted: {rollCount}")
print("\n>> Simulating rolls...\n")

# Organizing the dictionary
for i in range(diceCount, diceCount * 6 + 1):
    rolls[i] = 0

for i in range(rollCount):
    for e in range(diceCount):
        diceTotal += r.randint(1, 6)
    #  print(diceTotal)
    rolls[diceTotal] += 1
    diceTotal = 0

for i in rolls:
    print(f"{i}: {str(rolls[i])} rolls ({round(rolls[i] / rollCount * 100, 2)}%)")
