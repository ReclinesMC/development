# Sean A
# Clickbait Generator
# Using word lists and template headlines, randomly generate clickbait titles
import random as r
import os as s

OBJECT_PRONOUNS = ["Her", "Him", "Them"]
POSSESSIVE_PRONOUNS = ["Her", "His", "Their"]
PERSONAL_PRONOUNS = ["She", "He", "They"]
STATES = [
	"Pennsylvania", "California", "Wyoming", "Maryland", "Florida", "Ohio", "Georgia",
	"New Hampshire", "Illinois", "Michigan", "North Carolina", "Texas", "Nebraska"]
NOUNS = ["Athlete", "Clown", "Shovel", "Doctor", "Parent", "Cat", "Dog", "Chicken", "Robot",
		 "Video Game", "Avocado", "Plastic Straw", "Serial Killer", "Telephone Psychic"]
PLACES = ["House", "Attic", "Bank Deposit Box", "School", "Basement", "Workplace",
		  "Donut Shop", "Apocalypse Bunker"]
WHEN = ["Soon", "This Year", "Later Today", "RIGHT NOW", "Next Week"]


def getNum():
	count = ""
	while type(count) != int:
		try:
			print("How many clickbait titles would you like to generate?")
			count = int(input("> "))
		except:
			s.system("clear")
			print("You must enter a valid integer.")
			continue
		if count < 1:
			s.system("clear")
			print("You must enter a positive integer.")
			count = ""
			continue
	return count


def industryKiller():  # 0
	print(f"Are Millenials killing the {r.choice(NOUNS)} Industry?")


def bigCompanyHate():  # 1
	print(
		f"Big Companies Hate {r.choice(OBJECT_PRONOUNS)}! See How This {r.choice(STATES)} {r.choice(NOUNS)} Invented a Cheaper {r.choice(NOUNS)}")


def stateFound():  # 2
	print(
		f"You Won't Believe What This {r.choice(STATES)} {r.choice(NOUNS)} Found in {r.choice(POSSESSIVE_PRONOUNS)} {r.choice(PLACES)}!")


def dontKnow():  # 3
	print(f"What {r.choice(NOUNS)}s Don't Want You To Know About {r.choice(NOUNS)}s ")


def giftIdea():  # 4
	print(f"{r.randint(10, 50)} Gift Ideas to Give Your {r.choice(NOUNS)} From {r.choice(STATES)}")


def interestingReason():  # 5
	reasons = r.randint(10, 40)
	print(
		f"{reasons} Reasons Why {r.choice(NOUNS)} Are More Interesting Than You Think (Number {r.randint(2, reasons)} Will Surprise You!)")


def main():
	count = getNum()
	for i in range(count):
		print()
		title = r.randint(0, 5)
		if title == 0:
			industryKiller()
		elif title == 1:
			bigCompanyHate()
		elif title == 2:
			stateFound()
		elif title == 3:
			dontKnow()
		elif title == 4:
			giftIdea()
		elif title == 5:
			interestingReason()


if __name__ == "__main__":
	main()