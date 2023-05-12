import random as r


class Map:
    def __init__(self, difficulty=1):
        self.difficulty = difficulty
        self.maps = [Dungeon(), EmptyRoom(), TreasureRoom()]

    def genLeft(self):
        map = []
        for i in range(9 + self.difficulty):
            room = r.randint(1, 2)
            map.append(self.maps[room])
        map.append(BossRoom())
        print(map)
        return map

    def genRight(self):
        map = []
        for i in range(9 + self.difficulty):
            room = r.randint(0, 1)
            map.append(self.maps[room])
        map.append(BossRoom())
        print(map)
        return map

    # PathL will have a higher chance of dungeons


# PathR higher chance of treasure


class Dungeon:
    def __repr__(self):
        return "Dungeon Room"


class TreasureRoom:
    def __repr__(self):
        return "Treasure Room"


class BossRoom:
    def __repr__(self):
        return "Boss Room"


class EmptyRoom:
    def __repr__(self):
        return "Empty Room"


class Shop:
    pass