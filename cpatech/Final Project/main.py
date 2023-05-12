# Sean A
# The Dragon trail
# Using my extensive knowledge of classes make a big project that is a text adventure game

import os
import time as t
import yaml
import saving
import player as p
import map as m


def main():
    # Title
    print("\n" + "The Dragon Trail".center(60))
    print("A text adventure game".center(60))
    input("\n" + "Press ENTER to start your journey".center(60) + "\n".center(60))
    os.system('clear')
    saving.checkSave()
    t.sleep(5)
    os.system('clear')
    t.sleep(0.1)
    map = introducePlayer()
    print(map)


def introducePlayer():
    path = ""
    delay = 2
    print("You are a young adventurer")
    t.sleep(delay)
    print("Your goal is to defeat the evil dragon")
    t.sleep(delay)
    print("To do this, you must choose a path...")
    t.sleep(delay * 2)
    while path != "1" and path != "2":
        os.system("clear")
        t.sleep(0.1)
        print("[ The Paths ]".center(60, "="))
        print("💎 Left 💎".center(26) + "|" + "🔥 Right 🔥".center(29))
        print("-".center(29) + "|" + " -".center(29))
        print("|".center(60))
        print("Treasure Rooms".center(29) + "|" + "Creature Rooms".center(29))
        print("Common Loot".center(29) + "|" + "Rare Loot".center(29))
        print("Beginner Friendly".center(29) + "|" + "Many Battles".center(29))
        print("   ".center(60, "="))
        print("\n")
        print("1. Left 💎")
        print("2. Right 🔥")
        path = input("\nChoose a path >>")
        if path == "1":
            map = m.Map().genLeft()
            return map
        elif path == "2":
            map = m.Map().genRight()
            return map
        else:
            print("\nIncorrect Input! A number is required")
            input("Press ENTER to continue")
        # Izzy was here loser


if __name__ == "__main__":
    main()




