# Sean A
# Spongecase
# Create a program to convert any text into spongecase


sponge = input("Please enter the text you would like to be spongeified:")

sponge = list(sponge)

for text in range(len(sponge)):
	if text % 2 == 0:
		sponge[text] = sponge[text].upper()
	else:
		sponge[text] = sponge[text].lower()

sponge = "".join(sponge)

print("\nYour sponge text is: {}".format(sponge))
