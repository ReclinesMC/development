import subprocess as s
import time as t
try:
  import pyautogui as p
except:
  s.Popen("pip install pyautogui", shell=True)
  import pyautogui as p

height, width = p.size()
websites = [
  "https://www.mcdonalds.com/us/en-us/full-menu.html",
  "https://www.starbucks.com/menu", "https://www.chick-fil-a.com/menu",
  "https://www.tacobell.com/food/tacos",
  "https://www.wendys.com/en-uk/menu-categories/breakfast-sandwiches",
  "https://www.dunkindonuts.com/en/menu", "https://www.subway.com/en-US",
  "https://www.dominos.com/en/pages/order/menu#!/menu/category/viewall/",
  "https://www.chipotle.com/order/#menu"
]

delay = 1
p.press('winleft')
t.sleep(delay)
p.write('chrome')
t.sleep(delay)
p.press('enter')
t.sleep(delay)
p.moveTo(height / 2, width / 2)
p.click()
p.press('f6')
p.write('https://www.redlobster.com/menu')
p.press('enter')

for i in websites:
  p.hotkey('ctrl', 't')
  p.write(i)
  p.press('enter')
