class Treasure:
    pass


class Coin:
    def __str__(self):
        return "A shiny object that allows you to use the shop"

    def __repr__(self):
        return "Coin"


class Pearl:
    def __str__(self):
        return "A rare object that allows you to purchase rare items"

    def __repr__(self):
        return "Pearl"


class Star:
    def __str__(self):
        return "Boosts your max HP while in your inventory"

    def __repr__(self):
        return "Star"


class Ruby:
    def __str__(self):
        return "Boosts your damage while in your inventory"

    def __repr__(self):
        return "Ruby"
