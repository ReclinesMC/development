# Sean A
# The Dragon trail
# Using my extensive knowledge of classes make a big project that is a text adventure game

import os
import time as t
import yaml
import saving
import player as p


def main():
    # Title
    print("\n" + "The Dragon Trail".center(50))
    print("A text adventure game".center(50))
    input("\n" + "Press ENTER to start your journey".center(50))
    os.system('cls||clear')
    saving.checkSave()
    t.sleep(2)
    os.system('cls||clear')
    introducePlayer()


def introducePlayer():
    print("You are a young adventurer who has set out to slay the dragon that has been terrorizing the kingdom")

    print("In order to slay the dragon, you must first go through a series of rooms and defeat the monsters that inhabit"
          " them")


if __name__ == "__main__":
    main()
