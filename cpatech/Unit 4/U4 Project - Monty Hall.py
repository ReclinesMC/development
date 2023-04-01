# Sean A
# The Monty Hall Problem
# Using loops, simulate the Monty Hall problem

import os as s
import random as r

simCount = ""
doors = ["Zonk", "Zonk", "Car"]
montyChoose = ""
swap = 0
stay = 0
swin = 0
stwin = 0
stlosses = 0
slosses = 0
verbose = False

# Get the simulation amount, can only pass if it's an int
while type(simCount) != int:
    try:
        simCount = int(input("How many times would you like to simulate the Monty Hall problem?"))
    except:
        s.system("clear")
        print("You must enter a valid integer.")
        continue
    if simCount < 1:
        s.system("clear")
        print("You must enter a positive integer.")
        simCount = ""
        continue

# Print the good old simulations
s.system("clear")
print("[ Monty Hall Simulator ]".center(50, "="))
print(f"Simulations: {simCount}")
print("\n>> Simulating...\n")
if simCount >= 1000000:
    print(
        "This simulation may take some time, consider exiting the simulation and trying again with a smaller integer.\n")
for i in range(simCount):
    montyChoose = ""
    doors = ["Zonk", "Zonk", "Car"]
    doors = r.sample(doors, len(doors))
    simChoice = r.randint(0, 2)
    swapChoice = r.randint(0, 1)
    while montyChoose != "Zonk":
        montyNum = r.randint(0, 2)
        if montyNum == simChoice:
            continue
        montyChoose = doors[montyNum]
    doors[montyNum] = "Open"
    if verbose == True:
        print(doors)
    if swapChoice == 0:
        stay += 1
        if doors[simChoice] == "Car":
            stwin += 1
            if verbose == True:
                print("Stay win")
        else:
            stlosses += 1
            if verbose == True:
                print("Stay loss")
    elif swapChoice == 1:
        swap += 1
        simSwap = simChoice
        while simChoice == simSwap or simSwap == montyNum:
            simSwap = r.randint(0, 2)
        if doors[simSwap] == "Car":
            swin += 1
            if verbose == True:
                print("Swap win")
        else:
            slosses += 1
            if verbose == True:
                print("Swap loss")

if verbose == False:
    s.system("clear")
print("[ Monty Hall Simulator ]".center(50, "="))
print(f"Simulations: {simCount}")
print("\nWins:")
print(f"\tStay: {stwin} ({round(stwin / (stwin + swin) * 100, 2)}%)")
print(f"\tSwap: {swin} ({round(swin / (stwin + swin) * 100, 2)}%)")
print(f"\tTotal: {swin + stwin}")

print("\nLosses:")
print(f"\tStay: {stlosses} ({round(stlosses / (stlosses + slosses) * 100, 2)}%)")
print(f"\tSwap: {slosses} ({round(slosses / (stlosses + slosses) * 100, 2)}%)")
print(f"\tTotal: {slosses + stlosses}")

print("[ ]".center(50, "="))

print(
    "\nThe Monty Hall problem teaches us, that by swapping, you win an average of 1/3 more than you would by staying.")
print(
    f"As you can see, the simulation shows us that swapping increases the frequency of winning by approx. {round(((swin / (stwin + swin) * 100)) - (stwin / (stwin + swin) * 100), 2)}% more.")
