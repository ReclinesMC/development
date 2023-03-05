# Sean A
# Leetspeak
# Turn normal chars into special chars from a user-inputted string
import random as r
leetText = []
# woohoo heading
print("[ Leetspeak Converter ]".center(50, "="))

charMap = {
  'a' : ['4', '@', '/-\\'],
  'c' : ['('],
  'd' : ['|)'],
  'e' : ['3'],
  'f' : ["ph"],
  'h' : ["]-[", "|-|"],
  'i' : ['1', '!', '|'],
  'k' : ["]<"],
  'o' : ['0'],
  's' : ['$', '5'],
  't' : ['7', '+'],
  'u' : ["|_|"],
  'v' : ["\\/"]
}


# Get the string to be converted into leetspeak
boringText = input("Enter the text that you would like to convert into leetspeak:")

# loop de doop
for i in range(len(boringText)):
  if boringText[i].lower() in charMap:
    leetText.append(r.choice(charMap[boringText[i].lower()]))
  else:
    leetText.append(boringText[i])

leetText = "".join(leetText)

print(f"\nYour leetspeak'd text is: {leetText}")
print(f"\nOriginal: {boringText} ")