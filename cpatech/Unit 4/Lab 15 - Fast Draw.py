# Sean A
# Fast Draw
# Make a program that challenges a user to try and see how good their reaciton time is!

import os as s
import random as r
import time as t

times = []

delay = r.randint(1, 5)
stillPlaying = True
plays = 0

print("[ Reaction Timer ]".center(50, "="))
print("In this game you will test your reaction time!")
print("When you see \"GO\" press ENTER as fast as you can!\n")
print("Press enter to continue")
input()

while stillPlaying:

	# The game itself
	s.system("clear")
	print("READY...")
	t.sleep(r.randint(1, 3))
	print("SET..")
	t.sleep(delay)
	start = t.time()
	GO = input("GO!\n")
	end = t.time()
	time = round(end - start, 6)
	print(f"Your reaction time was: {time}\n")
	# Wow, great times
	if time < 0.180:
		print("Wow, you must be a world record holder!")
		print("This result will not be counted toward the final score.")
	elif time >= 0.180 and time <= 0.3:
		print("Wow! You're well above average.")
		times.append(time)
		plays += 1
	elif time > 0.3 and time <= 0.5:
		print("Good job, you're normal.")
		times.append(time)
		plays += 1
	elif time > 0.5:
		print("It seems your reaction time is slow. Maybe you should try again.")
		times.append(time)
		plays += 1

	# Keep playing... or else.
	# I'm so punny 😅
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
			print("You must choose y or n")
	if decision == "Y":
		delay = r.randint(1, 5)
		continue
	elif decision == "N":
		break

s.system("clear")
average = 0
try:
	for i in range(len(times)):
		average += times[i]
	average = round(average / plays, 6)
	slowest = round(max(times), 6)
	fastest = round(min(times), 6)

	print("Results:")
	print(f"Games played: {plays}")
	print(f"Average Reaction time: {average}")
	print(f"Slowest Reaction time: {slowest}")
	print(f"Fastest Reaction time: {fastest}")
except:
	print("Unable to display results.")
