from enum import Enum

class Song:

    StanzaType = Enum( 'StanzaType', 'VERSE CHORUS', module=__name__ )

    def __init__(self, lines):
        self.lines = lines
        self.title = ""
        self.verse = []
        self.chorus = ""
        self.currentStanzaType = self.StanzaType.VERSE
        
        self.createSong()
        print( "song verses: ", self.verse )
        print( "song chorus: ", self.chorus )

    def createSong(self):
        linecount = len(self.lines)
        if linecount <= 0:
            return
        
        self.title = self.lines.pop(0)
        print("input lines ", self.lines)
        stn = []
        for line in self.lines:
            if line == '' or line == '<Chorus>':
                if stn != []:
                    self.addStanza(stn)
                    stn = []
            else:
                stn.append(line)

            if line == '<Chorus>':
                self.currentStanzaType = self.StanzaType.CHORUS
                print('hit chorus')
            if line == '':
                self.currentStanzaType = self.StanzaType.VERSE

        self.addStanza(stn)
        return

    def addStanza(self, stn):
        if self.currentStanzaType == self.StanzaType.VERSE:
            self.verse.append(stn)
                    
        if self.currentStanzaType == self.StanzaType.CHORUS:
            self.chorus = stn

