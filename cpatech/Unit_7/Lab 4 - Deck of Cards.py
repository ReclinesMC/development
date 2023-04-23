try:
    # noinspection PyUnresolvedReferences
    from CardHandler import *
except:
    from cpatech.Unit_7.handlers.CardHandler import *


### DO NOT CHANGE THIS FUNCTION! ###
def TEST_deck():
    print(" Create a Deck of Cards ".center(50, "~"))
    d = Deck()
    print(d, "\n\n")

    print(" Shuffle Cards ".center(50, "~"))
    d.shuffle()
    print(d, "\n\n")

    print(" Draw 3 Cards ".center(50, "~"))
    print(f"Cards in deck: {len(d)}")
    c1 = d.draw()
    c2 = d.draw()
    c3 = d.draw()
    print(f"Cards drawn: {c1}, {c2}, {c3}")
    print(f"Cards remaining in deck: {len(d)}\n\n")

    print(" Deal Cards ".center(50, "~"))
    print("The deck has dealt 4 hands of 7 cards: ")
    hands = d.deal(4, 7)

    print(f"Hand 1: {hands[0]}")
    print(f"Hand 2: {hands[1]}")
    print(f"Hand 3: {hands[2]}")
    print(f"Hand 4: {hands[3]}")

    print(f"\nRemaining deck: {d}")
    print(f"Cards remaining in deck: {len(d)}\n\n")


def main():
    Deck()
    TEST_deck()


if __name__ == "__main__":
    main()