# Sean A
# RPG Characters
# Using classes create a way to create a character for an RPG

import random as r
import time as t


class Character:

    def __init__(self, name, chartype, weapon, strength, dexterity, wisdom, intelligence, charisma):
        self.name = name.capitalize()
        self.chartype = chartype.capitalize()
        self.weapon = weapon.capitalize()

        self.strength = strength + 5
        self.dexterity = dexterity + 5
        self.wisdom = wisdom + 5
        self.intellligence = intelligence + 5
        self.charisma = charisma + 5

        self.maxHP = self.roll_dice(15)
        self.HP = self.maxHP
        self.SP = self.roll_dice(5)
        self.BP = self.roll_dice(15) % 3
        self.level = self.roll_dice(2)
        self.attack = self.roll_dice(5)

    def roll_dice(self, amount, sides=6):
        count = 0
        for i in range(amount):
            count += r.randint(1, sides)
        return count

    def __str__(self):
        char_description = f"{self.name} The {self.chartype} ({self.HP}/{self.maxHP} HP)"
        return char_description

    def swap_weapon(self, weapon):
        weapon = weapon.capitalize()
        print(f"{self.name} swapped from a {self.weapon} to a {weapon}")
        self.weapon = weapon

    def heal(self, HP):
        self.HP += HP
        if self.HP > self.maxHP:
            self.HP = self.maxHP
        print(f"{self.name} healed {HP} HP! They are now at {self.HP} HP")

    def take_damage(self, damage):
        self.HP -= damage
        if self.HP < 0:
            self.HP = 0

        print(f"{self.name} took {damage} damage! They are now at {self.HP} HP")

    def level_up(self):
        self.maxHP += 5
        self.HP = self.maxHP
        self.SP += 5
        self.BP += 1
        self.level += 1
        self.attack += 5
        print(f"{self.name} is now level {self.level}!")

    def character_sheet(self):
        print(f" {self.name} the {self.chartype} ".center(50, "~"))
        print(f"✨ Level {self.level} ✨".ljust(20).rjust(38))
        print(f"❤️  {self.HP}/{self.maxHP}  ❤️".ljust(20).rjust(38))
        print(f"🔪 {self.weapon} 🔪".ljust(20).rjust(37))
        print(f"💪 {self.strength} Strength ".ljust(15).rjust(25), end="")
        print(f"👟 {self.dexterity} Dexterity ")
        print(f"🦉 {self.wisdom} Wisdom ".ljust(15).rjust(25), end="")
        print(f"🧠 {self.intellligence} Intelligence")
        print(f"👑 {self.charisma} Charisma ".ljust(15).rjust(25), end="")
        print(f"🎯 {self.attack} Attack")
        print(f"🔮 {self.SP} SP".ljust(15).rjust(25), end="")
        print(f"🔥 {self.BP} BP")
        print("~" * 50)


def test_sean():
    sean = Character("Sean", "Wizard", "Spellbook", 13, 16, 7, 17, 12)
    print(sean)
    sean.character_sheet()
    sean.swap_weapon("breadstick")
    sean.take_damage(10)
    sean.heal(5)
    sean.take_damage(10)
    sean.level_up()
    sean.character_sheet()


def test_peyton():
    peyton = Character("Peyton", "Rogue", "Dagger", 14, 17, 6, 12, 13)
    print(peyton)
    peyton.character_sheet()
    peyton.swap_weapon("Flying Car")
    peyton.take_damage(20)
    peyton.heal(5)
    peyton.take_damage(7)
    peyton.level_up()
    peyton.character_sheet()


def test_kieran():
    kieran = Character("Kieran", "Fighter", "Sword", 15, 7, 3, 6, 2)
    print(kieran)
    kieran.character_sheet()
    kieran.swap_weapon("Cheese Puffs")
    kieran.take_damage(30)
    kieran.heal(5)
    kieran.take_damage(2)
    kieran.level_up()
    kieran.character_sheet()


def main():
    test_sean()
    t.sleep(10)
    print("\n" * 2)
    test_peyton()
    t.sleep(10)
    print("\n" * 2)
    test_kieran()


if __name__ == "__main__":
    main()
