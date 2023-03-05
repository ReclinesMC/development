# Sean A
# Fibonacci Sequence
# Using functions get a specified amount of terms in the Fibonacci sequence
import os as s

def getNum():
  termCount = ""
  while type(termCount) != int:
    try:
      print("How many terms of the Fibonacci sequence would you like to get?")
      print("Type \"exit\" to exit")
      termCount = input("> ")
      if termCount.lower() == "exit":
        break
      else:
        termCount = int(termCount)
    except:
      s.system("clear")
      print("You must enter a valid integer.")
      continue
    if termCount < 1:
      s.system("clear")
      print("You must enter a positive integer.")
      termCount = ""
      continue
  return termCount

def fib(termCount):
  global fibNums
  fibNums = [0, 1]
  print(f"The first {termCount} Fibonacci numbers are:")
  print("(Five numbers per row)")
  for i in range(termCount):
    fibNums.append(fibNums[i] + fibNums[i + 1])
    if i % 5 == 0:
      print("\n")
    if i == termCount-1:
      print(fibNums[i])
    else:
      print(fibNums[i],end=", ")
  print()


def main():
  termCount = getNum()
  while termCount != "exit":
    fib(termCount)
    termCount = getNum()
if __name__ == "__main__":
  main()