# Sean A
# Caesar Cipher 2
# Using functions make a lab that can decrypt a message using Caesar Ciphering
import os as s

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def choice():
    # Checks if the user wants to encrypt or decrypt and saves their choice
    userChoice = ""
    chose = False
    while not chose:
        userChoice = input("Would you like to encrypt or decrypt using the Caesar Cipher?")
        if userChoice.lower() == "encrypt":
            chose = True
        elif userChoice.lower() == "decrypt":
            chose = True
        else:
            s.system("clear")
            print("Please enter \"encrypt\" or \"decrypt\"")
    return userChoice


def getKey(text, userChoice):
    # Grabs the key (and makes sure it is an int) to be used for encryption/decryption
    count = ""
    while type(count) != int:
        try:
            print(f"What key would you like to use for {userChoice}ion?")
            count = int(input("> "))
        except:
            s.system("clear")
            print("You must enter a valid integer.")
            print(f"Text to be {userChoice}ed: \"{text}\"")
            continue
        if count < 1:
            s.system("clear")
            print("You must enter a positive integer.")
            print(f"Text to be {userChoice}ed: \"{text}\"")
            count = ""
            continue
    return count


# num + thingy % 26
def getText(userChoice):
    # Gets the the text to be encrypted/decrypted
    print(f"What text would you like to {userChoice}?")
    text = input(">").lower()
    return text


def encrypter(text, key):
    cryptedMsg = []
    for i in range(len(text)):
        # Letters
        if text[i] in alphabet:
            cryptedMsg.append(alphabet[(key + alphabet.index(text[i])) % 26])
        else:
            cryptedMsg.append(text[i])

    cryptedMsg = ''.join(cryptedMsg)
    return cryptedMsg


def decrypter(text, key):
    decryptedMsg = []
    for i in range(len(text)):
        #  Letters
        if text[i] in alphabet:
            decryptedMsg.append(alphabet[abs((alphabet.index(text[i]) - key) % 26)])
        # Numbers, symbols, spaces
        else:
            decryptedMsg.append(text[i])

    decryptedMsg = ''.join(decryptedMsg)
    return decryptedMsg


def printResults(text, key, userChoice, msg):
    # Prints the results using the variables/info given
    s.system("clear")
    print(f"Original: \n{text}")
    print(f"\n{userChoice.capitalize()}ed: \n{msg}")
    print(f"\nKey: {key}")


def main():
    # Get all variables
    userChoice = choice()
    text = getText(userChoice)
    key = getKey(text, userChoice)
    # Print the results
    if userChoice == "encrypt":
        encryptedMsg = encrypter(text, key)
        printResults(text, key, userChoice, encryptedMsg)

    elif userChoice == "decrypt":
        decryptedMsg = decrypter(text, key)
        printResults(text, key, userChoice, decryptedMsg)


if __name__ == "__main__":
    main()
