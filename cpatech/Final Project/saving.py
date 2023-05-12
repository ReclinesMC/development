import os


def checkSave():
    if os.path.isfile("save.yml"):
        print("Found a save file")
        print("Saving will be implemented later")
        return True
    else:
        return False


def loadSave():
    pass
