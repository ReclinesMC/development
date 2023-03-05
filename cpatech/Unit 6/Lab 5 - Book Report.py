# Sean A
# Book Report
# Using the book given, get the title, author, word count, and most frequent word
import FileTools as ft

book = "Peter_Pan"
outputFile = "allWords"


def getBookInfo(text):
	# Getting the book title
	title = ""
	for i in text[0]:
		if i != "\n":
			title += i
	title = title.split()
	for i in range(len(title)):
		title[i] = title[i].capitalize()
	title = ' '.join(title)

	# Getting the author
	author = ""
	for i in text[1][2:]:
		if i != "\n":
			author += i

	return title, author


def getWords():
	# Getting the word count
	text = ft.handleFile(book, "clean")
	text = text.split()
	wordCount = len(text)

	# Getting each unique word
	words = {}
	for i in text:
		if i in words:
			words[i] += 1
		else:
			words[i] = 1

	# convert ze word count into ze file
	allWords = ""

	for i in words:
		allWords += i
		allWords += ": "
		allWords += str(words[i])
		allWords += "\n"

	ft.handleFile(outputFile, "create", allWords)

	# Get the biggest word and its count
	bigWord = max(words, key=words.get)
	bigWordCount = words[bigWord]

	return wordCount, bigWord, bigWordCount


def reportBook(title, author, bigWord, bigWordCount, wordCount):
	print("[ Book Report ]".center(50, "="))
	print(f"Title: {title}")
	print(f"Author: {author}")
	print(f"Words: {wordCount}")
	print()
	print(f"The most frequent word was \"{bigWord}\" with {bigWordCount} occurences.")
	print()
	print(f"Every word and its amount of occurences has been outputted into the {outputFile} file.")


def main():
	readBook = ft.handleFile(book, "parse")
	if readBook:
		title, author = getBookInfo(readBook)
		wordCount, bigWord, bigWordCount = getWords()
		reportBook(title, author, bigWord, bigWordCount, wordCount)


if __name__ == "__main__":
	main()