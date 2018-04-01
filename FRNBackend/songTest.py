import unittest
import song

class loadSongsTest(unittest.TestCase):

    def test_basic(self):
        lines = []
        s = song.Song( lines )
        self.assertEqual(s.title, "")
        self.assertEqual(s.title, "")
        self.assertEqual(s.verses, [])
        self.assertEqual(s.chorus, "")
        self.assertEqual(s.prechorus, "")
        self.assertEqual(s.bridge, "")

    def test_title(self):
        lines = ['song title']
        s = song.Song( lines )
        self.assertEqual(s.title, "song title")
        
    def test_verse(self):
        lines = ['song title', 'verse00', 'verse01']
        s = song.Song( lines )
        self.assertEqual(s.title, "song title")
        self.assertEqual(s.verses, [['verse00', 'verse01']])
        
    def test_verse2(self):
        lines = ['song title', 'verse00', 'verse01', '', 'verse10']
        s = song.Song( lines )
        self.assertEqual(s.title, "song title")
        self.assertEqual(s.verses, [['verse00', 'verse01'], ['verse10']])
        
    def test_verse3(self):
        lines = ['song title', 'verse00', '', 'v10', 'v11', '', 'v3', 'v31']
        s = song.Song( lines )
        self.assertEqual(s.title, "song title")
        self.assertEqual(s.verses, [['verse00'], ['v10', 'v11'], ['v3', 'v31']])
        
    def test_chorus(self):
        lines = ['song title', '<Chorus>', 'c1']
        s = song.Song( lines )
        self.assertEqual(s.title, "song title")
        self.assertEqual(s.verses, [])
        self.assertEqual(s.chorus, ['c1'])
        
    def test_verse_chorus(self):
        lines = ['song title','v1', 'v2', '<Chorus>', 'c1']
        s = song.Song( lines )
        self.assertEqual(s.title, "song title")
        self.assertEqual(s.verses, [['v1', 'v2']])
        self.assertEqual(s.chorus, ['c1'])

    def test_multiverse_chorus(self):
        lines = ['song title','vone1', 'vone2', '<Chorus>', 'c1','', 'vtow1', '', 'vthree1', 'vthree2']
        s = song.Song( lines )
        self.assertEqual(s.title, "song title")
        self.assertEqual(s.verses, [['vone1', 'vone2'], ['vtow1'], ['vthree1', 'vthree2']])
        self.assertEqual(s.chorus, ['c1'])

    def test_verse_prechorus(self):
        lines = ['song title','v1', '<Prechorus>', 'pc', '<Chorus>', 'c1']
        s = song.Song( lines )
        self.assertEqual(s.title, "song title")
        self.assertEqual(s.verses, [['v1']])
        self.assertEqual(s.chorus, ['c1'])
        self.assertEqual(s.prechorus, ['pc'])

    def test_multiverse_prechorus(self):
        lines = ['song title','vone1', 'vone2', '<Prechorus>', 'pc1', 'pc2', '<Chorus>', 'c1','', 'vtow1', '', 'vthree1', 'vthree2']
        s = song.Song( lines )
        self.assertEqual(s.title, "song title")
        self.assertEqual(s.verses, [['vone1', 'vone2'], ['vtow1'], ['vthree1', 'vthree2']])
        self.assertEqual(s.chorus, ['c1'])
        self.assertEqual(s.prechorus, ['pc1', 'pc2'])
        
    def test_bridge_verse_prechorus(self):
        lines = ['song title','v1', '<Prechorus>', 'pc', '<Chorus>', 'c1','','<Bridge>', 'b1', 'b2']
        s = song.Song( lines )
        self.assertEqual(s.title, "song title")
        self.assertEqual(s.verses, [['v1']])
        self.assertEqual(s.chorus, ['c1'])
        self.assertEqual(s.prechorus, ['pc'])
        self.assertEqual(s.bridge, ['b1', 'b2'])

    def test_bridge_multiverse_prechorus(self):
        lines = ['song title','vone1', 'vone2', '<Prechorus>', 'pc1', 'pc2', '<Chorus>', 'c1','', 'vtow1', '', 'vthree1', 'vthree2', '<Bridge>', 'b1']
        s = song.Song( lines )
        self.assertEqual(s.title, "song title")
        self.assertEqual(s.verses, [['vone1', 'vone2'], ['vtow1'], ['vthree1', 'vthree2']])
        self.assertEqual(s.chorus, ['c1'])
        self.assertEqual(s.prechorus, ['pc1', 'pc2'])
        self.assertEqual(s.bridge, ['b1'])

if __name__ == '__main__':
    unittest.main()
    
