import unittest
import song

class loadSongsTest(unittest.TestCase):

    def test_basic(self):
        lines = []
        s = song.Song( lines )
        self.assertEqual(s.title, "")
        
    def test_title(self):
        lines = ['song title']
        s = song.Song( lines )
        self.assertEqual(s.title, "song title")
        
    def test_verse(self):
        lines = ['song title', 'verse00', 'verse01']
        s = song.Song( lines )
        self.assertEqual(s.title, "song title")
        
    def test_verse2(self):
        lines = ['song title', 'verse00', 'verse01', '', 'verse10']
        s = song.Song( lines )
        self.assertEqual(s.title, "song title")
        
    def test_verse3(self):
        lines = ['song title', 'verse00', '', 'v10', 'v11', '', 'v3', 'v31']
        s = song.Song( lines )
        self.assertEqual(s.title, "song title")
        
    def test_chorus(self):
        lines = ['song title', '<Chorus>', 'c1']
        s = song.Song( lines )
        self.assertEqual(s.title, "song title")
        
    def test_verse_chorus(self):
        lines = ['song title','lkdfd jdf', 'jfkd', '<Chorus>', 'c1']
        s = song.Song( lines )
        self.assertEqual(s.title, "song title")

    
if __name__ == '__main__':
    unittest.main()
