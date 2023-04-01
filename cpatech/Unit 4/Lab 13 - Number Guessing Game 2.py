# Sean A
# Number Guessser
# Let the users guess a randomly generated number for as long as they want with loops!

import os
from random import randint

num = randint(1, 100)

keepPlaying = True
passUser = False
p1 = 0
p2 = 0

while keepPlaying:
    while passUser != True:
        try:
            # user 1
            user1 = int(input("Player 1: Pick a number 1-100:"))

            if user1 < 1 or user1 > 100:
                os.system("clear")
                print("You must enter an integer between 1 and 100")
                continue


        except:
            os.system("clear")
            print("You must enter an integer between 1 and 100 ")
            continue
        passUser = True

    while keepPlaying:
        try:
            # user 2
            user2 = int(input("Player 2: Pick a number 1-100:"))

            if user2 < 1 or user2 > 100:
                os.system("clear")
                print("You must enter an integer between 1 and 100")
                print(f"Player 1: {user1}")
                continue

            # converting nums
            close1 = abs(num - user1)
            close2 = abs(num - user2)
            # checking nums
            print()
            if close1 > close2:
                print("The second user was the closest to {}".format(num))
                passUser = False
                p1 += 1
                break
            elif close2 > close1:
                print("The first user was the closest to {}".format(num))
                passUser = False
                p2 += 1
                break
            if close2 == close1:
                print("You were both close to {}".format(num))
                passUser = False
                p1 += 1
                p2 += 1
                break

        except:
            print("You must enter an integer between 1 and 100 ")

    decision = ""
    while decision != "Y":
        decision = input("Would you like to keep playing? (y\\n):").capitalize()
        if decision == "N":
            print("Okay, bye!")
            break
        elif decision != "N" and decision != "Y":
            os.system("clear")
            print("You must choose y or n")

    if decision == "Y":
        num = randint(1, 100)
        continue
    elif decision == "N":
        keepPlaying = False
        break

os.system("clear")
print("Game Over!")
print("\nScores:")
print(f"Player 1: {p1}")
print(f"Player 2: {p2}")
print()
if p1 > p2:
    print("Player 1 wins!")
elif p2 > p1:
    print("Player 2 wins!")
elif p1 == p2:
    print("It's a tie!")
