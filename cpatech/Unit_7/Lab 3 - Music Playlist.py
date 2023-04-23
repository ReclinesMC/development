# Sean A
# Music Playlist
# Make a fake music player that plays a playlist of songs
try:
    import SonghHandler as sh
except:
    from cpatech.Unit_7.handlers import SongHandler as sh
import os as s
import time as t

playlist = [
    ['Flowers', 'Miley Cyrus', '3:21'],
    ['Kill Bill', 'SZA', '2:35'],
    ['Unholy', 'Sam Smith', '2:36'],
    ["Creepin'", 'Metro Boomin', '3:42'],
    ['Escapism', 'RAYE', '4:32'],
    ['Anti-Hero', 'Taylor Swift', '3:21'],
    ['Calm Down', 'Rema', '3:40'],
    ['LET GO', 'Central Cee', '2:54'],
    ['As It Was', 'Harry Styles', '2:47'],
    ['CUFF IT', 'Beyonce', '3:45'],
    ['golden hour', 'JVKE', '3:29'],
    ["I'm Good (Blue)", 'David Guetta', '2:55'],
    ['La Jumpa', 'Arcangel', '4:16'],
    ['Nobody Gets Me', 'SZA', '3:00'],
    ['Here With Me', 'd4vd', '4:03'],
    ['I Like You', 'Post Malone', '3:13'],
    ['Rich Flex', 'Drake', '3:59'],
    ['10:35', 'Tiesto', '2:52'],
    ['Made You Look', 'Meghan Trainor', '2:14'],
    ['Late Night Talking', 'Harry Styles', '2:58'],
    ['Lavender Haze', 'Taylor Swift', '3:22'],
    ['Ditto', 'NewJeans', '3:05'],
    ['Miss You', 'Oliver Tree', '3:26'],
    ['Just Wanna Rock', 'Lil Uzi Vert', '2:24'],
    ['Shirt', 'SZA', '3:02'],
    ["STAR WALKIN'", 'Lil Nas X', '3:30'],
    ["I Ain't Worried", 'OneRepublic', '2:28'],
    ['La Bachata', 'Manuel Turizo', '2:42'],
    ['Until I Found You', 'Stephen Sanchez', '2:57']]


def testSong():
    # For your convenience
    testSong = ["Test", "Artist", "0:05"]

    playlist.insert(0, testSong)


def main():
    # testSong()

    # Create list of song objects
    songs = []
    for i in playlist:
        songs.append(sh.Song(i))
    print(songs)
    # Play every song
    for song in range(len(songs)):
        print(f"Now Playing: {songs[song]}")
        print()
        if song != len(songs) - 1:
            print(f"Up Next: {songs[song + 1]}")
        else:
            print(f"Up Next: None")
        t.sleep(songs[song].dur)
        s.system("clear")
        t.sleep(0.1)
    print("You have reached the end of the playlist!")


if __name__ == "__main__":
    main()
