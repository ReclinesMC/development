# Sean A
# Overtime Pay Calculator
# Use if statements to calculate and detect overtime work and account for that pay

name = input("what is your name?:")
hours = int(input("How many hours did you work during the week?"))

if hours > 40:
	overHours = (hours - 40) * 30
	underHours = 40 * 20
	print()
	print("{}'s pay for this week is ${}!".format(name, overHours + underHours))

if hours <= 40:
	pay = hours * 20
	print()
	print("{}'s pay for this week is ${}!".format(name, pay))
