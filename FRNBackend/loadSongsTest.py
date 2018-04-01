import unittest
import loadSongs

class loadSongsTest(unittest.TestCase):

    def test_basic(self):
        ls = loadSongs.LoadSongs()
        self.assertEqual(ls.songs, [])

    def test_invalidFileName(self):
        ls = loadSongs.LoadSongs()
        self.assertRaises( TypeError, ls.getSongs, 5 )

    def test_simpleContent(self):
        ls = loadSongs.LoadSongs()
        songs = ls.getSongs('testdata/emtyfile.txt')
        self.assertEqual(ls.songs, [])
        self.assertEqual(len(songs), 0)

        songs = ls.getSongs("testdata/title.txt")
        self.assertEqual(ls.songs, [])
        self.assertEqual(len(songs), 0)

        songs = ls.getSongs("testdata/4emptytitles.txt")
        self.assertEqual(ls.songs, [])
        self.assertEqual(len(songs), 0)

    def test_titles(self):
        ls = loadSongs.LoadSongs()
        songs = ls.getSongs("testdata/3titles.txt")
        self.assertEqual(len(songs), 3)
        self.assertEqual(songs[0].title, "first song title")
        self.assertEqual(songs[0].verses, [])
        self.assertEqual(songs[0].chorus, "")
        self.assertEqual(songs[0].prechorus, "")
        self.assertEqual(songs[0].bridge, "")

        self.assertEqual(songs[1].title, "second song title")
        self.assertEqual(songs[1].verses, [])
        self.assertEqual(songs[1].chorus, "")
        self.assertEqual(songs[1].prechorus, "")
        self.assertEqual(songs[1].bridge, "")

        self.assertEqual(songs[2].title, "third song title")
        self.assertEqual(songs[2].verses, [])
        self.assertEqual(songs[2].chorus, "")
        self.assertEqual(songs[2].prechorus, "")
        self.assertEqual(songs[2].bridge, "")
        
    def test_fullsongs(self):
        ls = loadSongs.LoadSongs()
        songs = ls.getSongs("testdata/2songs.txt")
        self.assertEqual(len(songs), 2)

        self.assertEqual(songs[0].title, "Above all")
        self.assertEqual(songs[0].verses, [['Above all powers, above all kings','Above all nature and all created things','Above all wisdom and all the ways of man','You were here before the world began'],['Above all kingdoms above all thrones','Above all wonders ','The world has ever known','Above all wealth and treasures of the earth',"There's no way to measure ","What You're worth"]])
        self.assertEqual(songs[0].chorus, ['Crucified laid behind a stone', 'You lived to die rejected and alone', 'Like a rose trampled on the ground', 'You took the fall and thought of me', 'Above all'])
        self.assertEqual(songs[0].prechorus, "")
        self.assertEqual(songs[0].bridge, "")

        self.assertEqual(songs[1].title, "Blessed be the name of the Lord")
        self.assertEqual(songs[1].verses, [['Blessed be Your name in the land that is plentiful where Your streams of abundance flow Blessed be Your name', "Blessed be Your name when I'm found in the desert place though I walk through the wilderness Blessed be Your name"], ['Blessed be Your name when the sun\'s shining down on me. When the world\'s "all as it should be Blessed be Your name', "Blessed be Your name on the road marked with suffering Though there's pain in the offering Blessed be Your name"]])
        self.assertEqual(songs[1].chorus, ['Blessed be the name of the Lord', 'Blessed be Your name', 'Blessed be the name of the Lord', 'Blessed be Your glorious name'])
        self.assertEqual(songs[1].prechorus, ["Every blessing You pour out I'll", 'turn back to praise.', 'When the darkness closes in, Lord', 'Still I will say'])
        self.assertEqual(songs[1].bridge, ['Give and take away', 'You give and take away', 'Heart will choose to say', 'Lord, blessed be Your name'])
    
if __name__ == '__main__':
    unittest.main()
