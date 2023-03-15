# Sean A
# Pizza per square inch
# Using functions and loops calculate the area of a pizza and the cost per sq inch
from math import pi


def calcArea():
	radius = diam / 2
	size = round(pi * radius ** 2, 2)
	print(f"Area: {size} sq. inches")
	return size


def calcSqInch(cost):
	sqInch = round(cost / area, 2)
	print(f"Cost per sq. inch: ${sqInch:02}")
	return sqInch


# size : [diameter, price]
pizzas = {
	"small": [10, 8.99],
	"medium": [12, 11.99],
	"large": [14, 13.99],
	"Xlarge": [16, 14.99]
}

for i in pizzas:
	diam = pizzas[i][0]
	print(f"=====[ {i.capitalize()} ]=====")
	print(f"Diameter: {diam} inches")
	area = calcArea()
	sqInch = calcSqInch(pizzas[i][1])
	print()
