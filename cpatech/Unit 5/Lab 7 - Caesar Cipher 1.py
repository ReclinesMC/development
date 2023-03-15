# Sean A
# Caesar Cipher 1
# Using functions make a lab that encrypts a message using Caesar Ciphering
import os as s

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
cAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']


def getKey(text):
	count = ""
	while type(count) != int:
		try:
			print("What key would you like to use for encryption?")
			count = int(input("> "))
		except:
			s.system("clear")
			print("You must enter a valid integer.")
			print(f"Text to be encrypted: \"{text}\"")
			continue
		if count < 1:
			s.system("clear")
			print("You must enter a positive integer.")
			print(f"Text to be encrypted: \"{text}\"")
			count = ""
			continue
	return count


# num + thingy % 26
def getText():
	print("What text would you like to encrypt?")
	text = input(">")
	return text


def encrypter(text, key):
	cryptedMsg = []
	for i in range(len(text)):
		if text[i].isupper():
			cryptedMsg.append(cAlphabet[(key + cAlphabet.index(text[i])) % 26])
		elif text[i].islower():
			cryptedMsg.append(alphabet[(key + alphabet.index(text[i])) % 26])
		else:
			cryptedMsg.append(text[i])

	cryptedMsg = ''.join(cryptedMsg)
	return cryptedMsg


def main():
	text = getText()
	key = getKey(text)
	cryptedMsg = encrypter(text, key)
	s.system("clear")
	print(f"Original: {text}")
	print(f"Encrypted: {cryptedMsg}")
	print(f"Key: {key}")


if __name__ == "__main__":
	main()
