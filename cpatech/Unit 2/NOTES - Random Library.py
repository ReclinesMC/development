import random

print("The randint() function")
print(random.randint(0, 5))
print(random.randint(0, 5))
print(random.randint(5, 10))
print(random.randint(5, 20))

print("\nThe .choice() function")
options = ["cat", "dog", "rabbit", "mouse", "bird"]
print("Your perfect pet is a {}".format(random.choice(options)))