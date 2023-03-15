# Sean A
# Dice Roller
# Make a program that simulates rolling a specified amount of dice with a specified amount of sides
import os as s
import random as r
import re


def getDiceRolls():
	print(
		"Enter your input using the following format: <rolls>d<sides>\n\nExamples: \n3d6 >> rolls 3 six-sided dice.\n1d10 >> rolls 1 ten-sided dice ")
	SidesRolls = input(">").lower()
	return validifyDiceRolls(SidesRolls)


def validifyDiceRolls(diceRolls):
	regex = re.match(r"([0-9]+)d([0-9]+)", diceRolls)
	if regex:
		rolls = int(regex.group(1))
		sides = int(regex.group(2))
		if rolls != 0 and sides != 0:
			return rolls, sides
		else:
			s.system("clear")
			print("Please don't use the number 0.")
			return getDiceRolls()
	else:
		s.system("clear")
		print("Invalid Input, please try again.")
		return getDiceRolls()


def getModifier(rolls, sides):
	modifier = ""
	s.system("clear")
	while type(modifier) != int:
		print(f"Rolls: {rolls}")
		print(f"Sides: {sides}")
		try:
			modifier = int(input(
				"If you would like modify the final sum, please enter the amount you would like to add/subtract, or 0 for no modifier:"))
			s.system("clear")
			return modifier
		except:
			s.system("clear")
			print("You must enter a valid integer.")


def rollDice(rolls, sides):
	AllRolls = []
	for i in range(rolls):
		AllRolls.append(str(r.randint(1, sides)))
	return AllRolls


def outputWithModifier(AllRolls, modifier):
	sum = 0
	for i in range(len(AllRolls)):
		print(f"Roll #{i + 1}: {AllRolls[i]}")
		sum += int(AllRolls[i])
	print(f"Sum without modifier: {sum}")
	if modifier != 0:
		print(f"Sum with modifier: {sum + modifier}")


def main():
	print("Welcome to The Dice Roller™")
	# get numbers and make sure they are bueno
	rolls, sides = getDiceRolls()
	# Get the Modifier
	modifier = getModifier(rolls, sides)
	# Rolls the dice(s)
	AllRolls = rollDice(rolls, sides)
	# Output the results
	outputWithModifier(AllRolls, modifier)


if __name__ == "__main__":
	main()
