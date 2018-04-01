from enum import Enum

class Song:

    StanzaType = Enum( 'StanzaType', 'VERSE CHORUS PRECHORUS BRIDGE', module=__name__ )

    def __init__(self, lines):
        self.lines = lines
        self.title = ""
        self.verses = []
        self.chorus = ""
        self.prechorus = ""
        self.bridge = ""
        self.currentStanzaType = self.StanzaType.VERSE
        
        self.createSong()
        #print( "song verses: ", self.verses )
        #print( "song chorus: ", self.chorus )
        #print( "song prechorus: ", self.prechorus )
        #print( "song bridge: ", self.bridge )

    def createSong(self):
        linecount = len(self.lines)
        if linecount <= 0:
            return
        
        self.title = self.lines.pop(0)
        stn = []
        for line in self.lines:
            if line == '' or line == '<Chorus>' or line == '<Prechorus>' or line == '<Bridge>':
                if stn != []:
                    self.addStanza(stn)
                    stn = []
            else:
                stn.append(line)

            if line == '<Chorus>':
                self.currentStanzaType = self.StanzaType.CHORUS

            if line == '<Prechorus>':
                self.currentStanzaType = self.StanzaType.PRECHORUS

            if line == '<Bridge>':
                self.currentStanzaType = self.StanzaType.BRIDGE

            if line == '':
                self.currentStanzaType = self.StanzaType.VERSE

        self.addStanza(stn)
        return

    def addStanza(self, stn):
        if stn == []:
            return
        
        if self.currentStanzaType == self.StanzaType.VERSE:
            self.verses.append(stn)

        if self.currentStanzaType == self.StanzaType.CHORUS:
            self.chorus = stn

        if self.currentStanzaType == self.StanzaType.PRECHORUS:
            self.prechorus = stn

        if self.currentStanzaType == self.StanzaType.BRIDGE:
            self.bridge = stn
