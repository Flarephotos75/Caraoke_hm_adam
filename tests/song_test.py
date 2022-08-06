import unittest
from src.song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Under Pressure","Queen", 5)

    def test_song_name(self):
        self.assertEqual("Under Pressure", self.song.name)

    def test_song_artist(self):
        self.assertEqual("Queen", self.song.artist)

    def test_song_price(self):
        self.assertEqual(5, self.song.price)
