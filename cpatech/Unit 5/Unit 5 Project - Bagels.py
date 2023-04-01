# Sean A
# Bagels
# Make a deductive logic game that allows for the user to guess a random number
import os as s
import random as r
import re
import time as t


def genRandomNum(numSize):
    randomNumber = ""

    for i in range(numSize):
        randomNumber += str(r.randint(1, 9))
    return randomNumber


def welcomeMsg():
    print(">>> Welcome to Bagels - the guessing game!\n")
    print("1. I am going to generate a random number of the size that you choose\n")
    print("2. You will be given 10 tries to guess the mystery number\n")
    print("3. For each guess you will be given a hint\n")
    print("4. Hint info will always be displayed at the top of your screen")

    starting = input("\nAre you ready to get started? (y/n)")
    if starting == "y":
        print("Okay! How many digits would you like your number to be?")
        return True
    elif starting == "n":
        return False
    else:
        s.system("clear")
        return welcomeMsg()


def getNumSize():
    size = input(">")
    regex = re.match(r"[0-9]+", size)
    if regex:
        size = int(size)
        if size > 50:
            print("You can't guess that big of a number! Please enter a lower amount")
            return getNumSize()
        elif size <= 2:
            print("That's too easy! Please input 3 or more.")
            return getNumSize()
    else:
        print("You must enter a positive number")
        return getNumSize()
    return size


def guessInterpreter(numSize, randomNum):
    print("Hints:")
    print("Pico - a digit is correct but in the wrong place")
    print("Fermi - a digit is correct and in the correct place")
    print("Bagels - no digits are correct")
    guesses = []
    for i in range(11):
        if i == 10:
            s.system("clear")
            print("You ran out of guesses!")
            print(f"The number was {randomNum}")
            print("restarting...")
            t.sleep(5)
            main()
        guessed = False
        while not guessed:
            guess = input(f"Guess #{i + 1} >> ")
            regex = re.match(r"[0-9]+", guess)
            if regex and len(guess) == numSize:
                guessed = True
                guesses.append(guess)
            else:
                print(f"You must enter a valid {numSize} digit number")
        giveHints(randomNum, guess)


def giveHints(randomNum, guess):
    hints = ""
    for i in range(len(guess)):
        if guess == randomNum:
            s.system("clear")
            print("You win!")
            print(f"The number was {randomNum}")
            print("restarting...")
            t.sleep(5)
            main()
        elif guess[i] == randomNum[i]:
            hints += "Fermi "
        elif guess[i] in randomNum:
            hints += "Pico "
    if not hints:
        hints += "Bagels "
    print(hints)


def main():
    # to generate a random nombreo ahhaahha
    s.system("clear")
    if welcomeMsg():
        numSize = getNumSize()
        s.system("clear")
        randomNum = genRandomNum(numSize)
        print(randomNum)
        guessInterpreter(numSize, randomNum)
    else:
        s.system("clear")
        print("Seeya later!")


if __name__ == "__main__":
    main()
