# Sean A
# Magic 8 Ball
# Make a program to give a random output to yes or no questions
import os as s
import random as r
import time as t
from sys import stdout as sy

stillPlaying = True

replies = [
	"LET ME THINK ON THIS...", "AN INTERESTING QUESTION...",
	"SOME THINGS ARE BEST LEFT UNKNOWN...", "THE STARS SAY YES, BUT I SAY NO",
	"MOST DEFINITELY...", "THE SPIRITS ARE UNSURE...", "DOUBTFUL...",
	"DON'T COUNT ON IT...", "I BELIEVE SO...", "OUTLOOK IS POSITIVE..."
]
typing = 0.15  # <--- change this to 0 to make stuff a bit faster
delay = 3  # <--- same with this

print("[ Magic 8 Ball ]".center(50, "="))

welcome = "Welcome to the Magic 8 Ball. Proceed with caution as you ask it for the answers to your future..."

# Welcome message
for i in range(len(welcome)):
	sy.write(welcome[i])
	sy.flush()
	t.sleep(typing)
t.sleep(delay)
while stillPlaying:
	# Ask for question
	s.system("clear")
	print("[ Magic 8 Ball ]".center(50, "="))
	print("\nAsk me something, if you dare...")
	question = input()

	# The response
	reply = r.choice(replies)
	print()
	for i in range(len(reply)):
		sy.write(reply[i])
		sy.flush()
		t.sleep(typing)
	print()
	t.sleep(delay)

	decision = ""
	while decision != "Y":
		decision = input("Would you like to keep playing? (y\\n):").capitalize()
		if decision == "N":
			print("Okay, bye!")
			t.sleep(1)
			stillPlaying = False
			break
		elif decision != "N" and decision != "Y":
			s.system("clear")
			print("[ Magic 8 Ball ]".center(50, "="))
			print("\nYou must choose y or n")
	if decision == "Y":
		continue
	elif decision == "N":
		break
