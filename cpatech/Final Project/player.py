class Player:
    def __init__(self):
        self.inventory = []
        self.coins = 0
        self.pearls = 0

    def __str__(self):
        return str(self.inventory)
    def pickUp(self, item):
        self.inventory.append(item)
