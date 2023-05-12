import random as r
import os
import time as t
import gui


class Map:
    def __init__(self, difficulty=1):
        self.difficulty = difficulty
        self.maps = [Dungeon(), EmptyRoom(), TreasureRoom()]

    def genLeft(self):
        mapLayout = []
        for i in range(9 + self.difficulty):
            room = r.randint(1, 2)
            mapLayout.append(self.maps[room])
        mapLayout.append(BossRoom())
        return mapLayout

    def genRight(self):
        mapLayout = []
        for i in range(9 + self.difficulty):
            room = r.randint(0, 1)
            mapLayout.append(self.maps[room])
        mapLayout.append(BossRoom())
        return mapLayout


class Dungeon:
    def enter(self):
        print("You have entered a dungeon")
        gui.actionMenu()

    def __repr__(self):
        return "Dungeon"


class TreasureRoom:
    def __repr__(self):
        return "Treasure"


class BossRoom:
    def __repr__(self):
        return "Boss"


class EmptyRoom:
    def __repr__(self):
        return "Empty"


class Shop:
    def __init__(self):
        os.system("clear")
        t.sleep(0.1)
        print("Welcome to the shop!")
        print("What would you like to buy?")
