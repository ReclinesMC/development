# Sean A
# Number Guessser
# Let the users guess a randomly generated number between 1-100 and display which was closer
from random import randint

num = randint(1, 100)

try:
    # user 1
    user1 = int(input("Pick a number 1-100:"))
    user2 = int(input("Pick a number 1-100:"))

    if user1 < 1 or user1 > 100:
        Print("")

    # user 2
    elif user2 < 1 or user1 > 100:
        Print("")

    # converting nums
    close1 = abs(num - user1)
    close2 = abs(num - user2)

    # checking nums
    print()
    if close1 > close2:
        print("The second user was the closest to {}".format(num))
    elif close2 > close1:
        print("The first user was the closest to {}".format(num))

    if close2 == close1:
        print("You were both close to {}".format(num))

except:
    print("You must enter an integer between 1 and 100 ")
