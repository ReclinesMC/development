import weapons


class Person:
    def __init__(self):
        self.weapon = weapons.Pencil()
        self.inventory = []
        self.coins = 0
        self.pearls = 0
        self.strength = 0
        self.health = 100

    def __str__(self):
        return str(self.name)

    def pickUp(self, item):
        self.inventory.append(item)

    def attack(self, enemy):
        damage = self.weapon.damage
        print("You attacked {enemy} for {damage} damage!")
        enemy.takeDamage(damage)

    def takeDamage(self, damage, enemy):
        print("{enemy} attacked you for {damage} damage")
        self.health -= damage


Player = Person()
