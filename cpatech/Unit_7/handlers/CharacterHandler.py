# Create one of each type of character and use each of their methods at least once.


import random as r


class Character:

    def __init__(self, name, strength, dexterity, wisdom, intelligence, charisma):
        self.name = name

        self.strength = strength + 5
        self.dexterity = dexterity + 5
        self.wisdom = wisdom + 5
        self.intelligence = intelligence + 5
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

    def print_stat(self, stat):
        # Had to do some wonky stuff to get this to work
        print(f"{self.name}'s {stat} is {getattr(self, stat)}")

    def character_sheet(self):
        print(f" {self.name} the {self.chartype} ".center(50, "~"))
        print(f"✨ Level {self.level} ✨".ljust(20).rjust(38))
        print(f"❤️  {self.HP}/{self.maxHP}  ❤️".ljust(20).rjust(38))
        print(f"🔪 {self.weapon} 🔪".ljust(20).rjust(37))
        print(f"💪 {self.strength} Strength ".ljust(15).rjust(25), end="")
        print(f"👟 {self.dexterity} Dexterity ")
        print(f"🦉 {self.wisdom} Wisdom ".ljust(15).rjust(25), end="")
        print(f"🧠 {self.intelligence} Intelligence")
        print(f"👑 {self.charisma} Charisma ".ljust(15).rjust(25), end="")
        print(f"🎯 {self.attack} Attack")
        print(f"🔮 {self.SP} SP".ljust(15).rjust(25), end="")
        print(f"🔥 {self.BP} BP")
        print("~" * 50)


class Fighter(Character):
    def __init__(self, name, strength, dexterity, wisdom, intelligence, charisma):
        super().__init__(name, strength, dexterity, wisdom, intelligence, charisma)
        self.chartype = "Fighter"
        self.weapon = "Sword"
        self.strength += 10

    def take_damage(self, damage):
        if r.randint(0, 100) <= 30:
            print(f"{self.name} blocked the attack!")
        else:
            super().take_damage(damage)


class Rogue(Character):
    def __init__(self, name, strength, dexterity, wisdom, intelligence, charisma):
        super().__init__(name, strength, dexterity, wisdom, intelligence, charisma)
        self.chartype = "Rogue"
        self.weapon = "Dagger"
        self.dexterity += 10

    def take_damage(self, damage):
        if r.randint(0, 100) <= self.level * 2.5:
            print(f"{self.name} dodged the attack!")
        else:
            super().take_damage(damage)


class Sorcerer(Character):
    def __init__(self, name, strength, dexterity, wisdom, intelligence, charisma):
        super().__init__(name, strength, dexterity, wisdom, intelligence, charisma)
        self.chartype = "Sorcerer"
        self.weapon = "Orb"
        self.wisdom += 10
        self.SP += 10

    def cast_fireball(self):
        self.SP -= 10
        if self.SP < 0:
            print(f"{self.name} did not have enough SP")
            self.SP += 10
            return False
        print(f"{self.name} cast a Fireball! They are now at {self.SP} SP")


class Wizard(Character):
    def __init__(self, name, strength, dexterity, wisdom, intelligence, charisma):
        super().__init__(name, strength, dexterity, wisdom, intelligence, charisma)
        self.chartype = "Wizard"
        self.weapon = "Spellbook"
        self.intelligence += 10
        self.SP += 10

    def cast_healingHands(self, other):
        self.SP -= 30
        if self.SP < 0:
            print(f"{self.name} did not have enough SP")
            self.SP += 30
            return False
        other.HP = other.maxHP
        print(f"{self.name} cast Healing Hands on {other.name}! They are now at {other.HP} HP")
        print(f"{self.name} is now at {self.SP} SP")
        return True


class Bard(Character):
    def __init__(self, name, strength, dexterity, wisdom, intelligence, charisma):
        super().__init__(name, strength, dexterity, wisdom, intelligence, charisma)
        self.chartype = "Bard"
        self.weapon = "Lyre"
        self.charisma += 10

    def gift_of_life(self, other):
        if r.randint(0, 100) <= self.charisma * 1.2:
            if other.HP >= 15:
                self.HP += 15
                other.HP -= 15
                print(f"{self.name} convinced {other.name} to donate 15 HP! They are now at {self.HP} HP")
                print(f"{other.name} is now at {other.HP}/{other.maxHP} HP")
            elif 15 > other.HP > 0:
                self.HP += other.HP
                other.HP = 0
                print(f"{self.name} convinced {other.name} to donate all of their HP! They are now at {self.HP} HP")
                print(f"{other.name} is now at {other.HP}/{other.maxHP} HP")
            else:
                print(f"{other.name} had no HP to donate!")
        else:
            print(f"{self.name} failed to convince {other.name} to donate 15 HP!")

