# Sean A
# Dice Roll simulation
# Work with the time and math library to create a dice roll simulation
import os
from random import randint
from time import sleep

dice1 = randint(1, 6)
dice2 = randint(1, 6)

pause = input("Press enter to roll the dice")
os.system("clear")
print("Rolling your dice.")
sleep(0.5)
os.system("clear")
print("Rolling your dice..")
sleep(0.5)
os.system("clear")
print("Rolling your dice...")
sleep(0.5)
os.system("clear")

print("It looks like you have rolled a {} and a {}!\n".format(dice1, dice2))

# Dice 1
print(" {}{}{}{} ".format(chr(95), chr(95), chr(95), chr(95)))
print("{} {} {}".format(chr(166), "  ", chr(166)))
print("{} {} {}{}".format(chr(166), dice1, " ", chr(166)))
print("{} {} {}".format(chr(166), "  ", chr(166)))
print(" {}{}{}{} ".format(chr(175), chr(175), chr(175), chr(175)))

# Dice 2
print(" {}{}{}{} ".format(chr(95), chr(95), chr(95), chr(95)))
print("{} {} {}".format(chr(166), "  ", chr(166)))
print("{} {} {}{}".format(chr(166), dice2, " ", chr(166)))
print("{} {} {}".format(chr(166), "  ", chr(166)))
print(" {}{}{}{} ".format(chr(175), chr(175), chr(175), chr(175)))
