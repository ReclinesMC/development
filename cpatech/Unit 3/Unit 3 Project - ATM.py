# Sean A
# ATM Emulator
# Make code for a fake ATM that is user friendly and meets the requirements
import os
import time as t

Customers = {
	"Tiger": ["iAMdeath1234!", 5980.82],
	"Snake": ["MICETASTEREALLYGOOD5", 1204.26],
	"Treefrog": ["TheCuteKiller9872", 3167.73],
	"Parrot": ["FluffyFeathers94", 9821.19],
	"Monkey": ["BANANNANANANANA", 1234.28],
	#  "A" : ["a", 1293578.90] # <---- Quick access user, remove comment for convenience
}

# Welcome Message
print("[ Rainforest ATM ]".center(50, "="))
print("Welcome! Please enter your username and password\n")

# Logging in
user = input("Username:").capitalize()
password = input("Password:")

if user in Customers:
	if password == Customers[user][0]:
		# Login delay

		os.system("clear")
		print("Authorizing.")
		t.sleep(0.5)
		os.system("clear")
		print("Authorizing..")
		t.sleep(0.6)
		os.system("clear")
		print("Authorizing...")
		t.sleep(0.7)

		os.system("clear")
		# Giving the user choices
		print("[ Rainforest ATM ]".center(50, "="))
		print("Welcome {}!".format(user))
		if user == "A":
			print("!!! This is a quick-access user, not to be used in production.")
		print("\n1 - Check your balance")
		print("2 - Withdraw from your account")
		print("3 - Deposit into your account\n")
		try:
			choice = (input("\nPlease choose an option:"))
			# User Choices
			if choice == "1" or choice.capitalize() == "Check":
				print("Your balance is currently ${}".format(Customers[user][1]))
			elif choice == "2" or choice.capitalize() == "Withdraw":
				try:
					withdraw = round(float(input("How much money would you like to withdraw?:")), 2)
					if withdraw > Customers[user][1]:
						print("You do not have enough money in your account to withdraw that much!")
					elif withdraw > 2000:
						print("You cannot withdraw this much money!")
					elif withdraw == 0:
						print("Withdrawing nothing is pointless.")
					elif withdraw < 0:
						print("You cannot withdraw a negative amount!")
					elif withdraw <= Customers[user][1]:
						Customers[user][1] = Customers[user][1] - withdraw
						print("Successfully withdrew ${} from your account".format(withdraw))
						print("Your balance is now ${:.2f}".format(Customers[user][1]))
				except:
					print("You must enter a valid amount of money to withdraw")
			elif choice == "3" or choice.capitalize() == "Deposit":
				try:
					deposit = round(float(input("How much money would you like to deposit?")), 2)
					if deposit == 0:
						print("Depositing nothing is pointless.")
					elif deposit > 5000:
						print("You cannot deposit this much in one session!")
					elif deposit < 0:
						print("You cannot deposit a negative amount!")
					elif deposit > 0:
						Customers[user][1] = Customers[user][1] + deposit
						print("Successfully deposited ${} into your account".format(deposit))
						print("Your balance is now ${:.2f}".format(Customers[user][1]))
				except:
					print("You must enter a valid amount of money to deposit")
			else:
				print("\nPlease pick an option that is listed")
		except:
			print("\nPlease pick an option that is listed)")
	else:
		os.system("clear")
		print("Invalid username or password")
else:
	os.system("clear")
	print("Invalid username or password")
