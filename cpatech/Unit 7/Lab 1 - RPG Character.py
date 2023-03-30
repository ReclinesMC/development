# Sean A
# RPG Characters
# Using classes create a way to create a character for an RPG
import random as r




class Character:

	def __init__(self, name, chartype, weapon, strength, dexterity, wisdom, intelligence, charisma):
		self.name = name
		self.chartype = chartype
		self.weapon = weapon

		self.strength = strength + 5
		self.dexterity = dexterity + 5
		self.wisdom = wisdom + 5
		self.intellligence = intelligence + 5
		self.charisma = charisma + 5

		self.maxHP = r.randint(15, 90)
		self.HP = self.maxHP
		self.SP = r.randint(5, 30)
		self.BP = (r.randint(15, 90)) % 3
		self.level = r.randint(2, 12)
		self.attack = r.randint(5, 30)

	def __str__(self):
		char_description = f"{self.name} The {self.chartype}"
		return char_description

	def swap_weapon(self, weapon):
		print(f"{self.name} swapped from a {self.weapon} to a {weapon}")
		self.weapon = weapon
	def heal(self, HP):
		self.HP += HP
		if self.HP > self.maxHP:
			self.HP = self.maxHP

	def take_damage(self, damage):
		self.HP -= damage
		if self.HP < 0:
			self.HP = 0

	def level_up(self):
		self.maxHP += 5
		self.HP = self.maxHP
		self.SP += 5
		self.BP += 1
		self.EXP += 5
		self.attack += 5
	def character_sheet(self):
		print(f" {self.name} the {self.chartype} ".center(50, "~"))
		print(f"✨ Level {self.level} ✨".ljust(20).rjust(38))
		print(f"❤️  {self.HP}/{self.maxHP}  ❤️".ljust(20).rjust(38))
		print(f"🔪 {self.weapon} 🔪".ljust(20).rjust(38))
		print(f"💪 {self.strength} Strength ".ljust(15).rjust(25), end="")
		print(f"👟 {self.dexterity} Dexterity ")
		print(f"🦉 {self.wisdom} Wisdom ".ljust(15).rjust(25), end="")
		print(f"🧠 {self.intellligence} Intelligence")
		print(f"👑 {self.charisma} Charisma ".ljust(15).rjust(25), end="")
		print(f"🎯 {self.attack} Attack")
		print(f"🔮 {self.SP} SP".ljust(15).rjust(25), end="")
		print(f"🔥 {self.BP} BP")
		print("~" * 50)



def main():
	sean = Character("Sean", "Wizard", "Spellbook", 13, 16, 7, 17, 12)
	print(sean.character_sheet())
	print(sean)
	print(sean)
	print(sean)


if __name__ == "__main__":
	main()
