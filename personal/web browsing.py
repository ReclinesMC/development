import webbrowser as w

websites = [
    "https://www.mcdonalds.com/us/en-us/full-menu.html",
    "https://www.starbucks.com/menu", "https://www.chick-fil-a.com/menu",
    "https://www.tacobell.com/food/tacos",
    "https://www.wendys.com/en-uk/menu-categories/breakfast-sandwiches",
    "https://www.dunkindonuts.com/en/menu", "https://www.subway.com/en-US",
    "https://www.dominos.com/en/pages/order/menu#!/menu/category/viewall/",
    "https://www.chipotle.com/order/#menu"
]
for url in websites:
    w.open(url, new=2, autoraise=False)
