import random as r
import os
import time as t
import gui


class Map:
    def __init__(self, difficulty=1):
        self.difficulty = difficulty
        self.maps = [Dungeon(), Empty(), Treasure()]

    def genLeft(self):
        mapLayout = []
        mapLayout.append(Treasure())
        for i in range(8 + self.difficulty):
            room = r.randint(1, 2)
            mapLayout.append(self.maps[room])
        mapLayout.append(Boss())
        return mapLayout

    def genRight(self):
        mapLayout = []
        mapLayout.append(Dungeon())
        for i in range(8 + self.difficulty):
            room = r.randint(0, 1)
            mapLayout.append(self.maps[room])
        mapLayout.append(Boss())
        return mapLayout


class Rooms:
    def __init__(self):
        self.room = None

    def enter(self):
        print(f"You have entered a {self.room} room")
        gui.actionMenu()

    def __repr__(self):
        return str(self.room)


class Dungeon(Rooms):
    def __init__(self):
        super().__init__()
        self.room = "Dungeon"


class Treasure(Rooms):

    def __init__(self):
        super().__init__()
        self.room = "Treasure"


class Boss(Rooms):
    def __init__(self):
        super().__init__()
        self.room = "Boss"


class Empty(Rooms):
    def __init__(self):
        super().__init__()
        self.room = "Empty"


class Shop:
    def __init__(self):
        os.system("clear")
        t.sleep(0.1)
        print("Welcome to the shop!")
        print("What would you like to buy?")
