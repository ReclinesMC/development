import random as r


class Deck:
    def __init__(self):
        suits = ["♠", "♥", "♣", "♦"]
        symbols = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cards = []
        for i in suits:
            for s in symbols:
                cards.append(Card(s, i))

        self.cards = cards

    def __str__(self):
        return str(self.cards)

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        r.shuffle(self.cards)
        return self.cards

    def draw(self):
        card = self.cards.pop(0)
        return card

    def deal(self, numHands, cards):
        hands = []
        for i in range(numHands):
            hands.append([])
            for c in range(cards):
                hands[i].append(self.draw())

        return hands


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        cardInfo = f"{self.value}{self.suit}"
        return cardInfo