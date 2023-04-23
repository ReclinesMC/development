# Sean A
# Game Pieces
# Make a bunch of model game pieces using classes
try:
    import GamePieces as gp
except:
    from cpatech.Unit_7.handlers import GamePieces as gp

def Dice_test():
    sixSided = gp.Die()
    print(sixSided)
    print(sixSided.sides)
    sixSided.roll()  # roll 1 six sided dice
    sixSided.roll(2)  # roll 2 six sided dice
    print()

    sevenSided = gp.Die(7)
    print(sevenSided)
    print(sevenSided.sides)
    sevenSided.roll()
    sevenSided.roll(2)
    print()

    eightSided = gp.Die(8)
    print(eightSided)
    print(eightSided.sides)
    eightSided.roll()
    print(eightSided.roll(2))
    print()


def Cards_test():
    diamonds5 = gp.Card("5", "Diamonds")
    print(diamonds5)

    clubs9 = gp.Card("9", "Clubs")
    print(clubs9)

    spades3 = gp.Card("3", "Spades")
    print(spades3)

    print()


def Pieces_test():
    redPiece = gp.Piece("Red")
    print(redPiece)

    bluePiece = gp.Piece("Blue")
    print(bluePiece)

    purplePiece = gp.Piece("Purple")
    print(purplePiece)

    print()


def main():
    print("[ Dice ]".center(50, "="))
    Dice_test()
    print("[ Cards ]".center(50, "="))
    Cards_test()
    print("[ Pieces ]".center(50, "="))
    Pieces_test()


if __name__ == "__main__":
    main()
