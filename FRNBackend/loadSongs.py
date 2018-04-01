import string
import song

class LoadSongs:
    """A class to load the songs present in a text file"""

    def __init__(self):
        self.songs = []

    def getSongs( self, fileName ):
        if type(fileName) != str:
            raise TypeError("Invalid fileName")

        songlines = []
        f = open(fileName, 'r')
        lines = f.readlines()
        f.close()
        #print(lines)
        for line in lines:
            line = line.replace( '\n', '' )
            if line == "<Title>":
                if songlines != []:
                    self.songs.append(song.Song(songlines))
                    songlines = []

            else:
                songlines.append(line)

        if songlines != []:
            self.songs.append(song.Song(songlines))

        return self.songs
        
