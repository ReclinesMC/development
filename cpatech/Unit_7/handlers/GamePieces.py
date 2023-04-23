import random as r


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def __str__(self):
        diceInfo = f"A {self.sides} sided dice"
        return diceInfo

    def roll(self, times=1):
        count = 0
        for i in range(times):
            count += r.randint(0, self.sides)
        print(f"The {self.sides} sided die was rolled {times} time(s) and added up to {count}")
        return count


class Card:
    def __init__(self, number, type):
        self.number = number
        self.type = type

    def __str__(self):
        cardInfo = f"A {self.number} of {self.type}"
        return cardInfo


class Piece:
    def __init__(self, color="Black"):
        self.color = color

    def __str__(self):
        pieceInfo = f"A {self.color} playing piece"
        return pieceInfo
