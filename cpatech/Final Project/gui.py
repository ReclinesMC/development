import map
import os
import time as t
import map as m

header = "The Dragon Trail".center(50, " ")


def introducePlayer():
    path = ""
    delay = 0.1
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
            mapLayout = m.Map().genLeft()
        elif path == "2":
            mapLayout = m.Map().genRight()
            print("This path will be implemented in the future")
            continue
        else:
            print("\nIncorrect Input! A number is required")
            input("Press ENTER to continue")
        # Izzy was here loser
        gameplay(mapLayout)


def gameplay(mapLayout):
    for i in mapLayout:
        i.enter()


def actionMenu():
    pass
