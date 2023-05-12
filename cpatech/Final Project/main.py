# Sean A
# The Dragon trail
# Using my extensive knowledge of classes make a big project that is a text adventure game

import os
import time as t
import gui
import saving


# If you see t.sleep(0.1) its to fix the screen clearing bug with trinket

def main():
    # Title
    print("\n" + "The Dragon Trail".center(60))
    print("A text adventure game".center(60))
    input("\n" + "Press ENTER to start your journey".center(60) + "\n".center(60))
    os.system('clear')
    saving.checkSave()
    t.sleep(0.5)
    os.system('clear')
    t.sleep(0.1)
    gui.introducePlayer()



if __name__ == "__main__":
    main()
