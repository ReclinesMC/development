
class Song:
    def __init__(self, songInfo):
        self.name = songInfo[0]
        self.artist = songInfo[1]
        duration = songInfo[2].split(":")
        duration = duration[0] + "." + duration[1]
        self.dur = float(duration)

    def __str__(self):
        info = f"{self.name} by {self.artist}"
        return info