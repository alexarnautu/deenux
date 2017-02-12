import unittest
from src.deenuxapi.deezer.model.Track import Track
from src.deenuxapi.deezer.model.Artist import Artist
from src.deenuxapi.deezer.model.User import User


class MyTestCase(unittest.TestCase):

    def test_track(self):

        tst = Track.get(3135556)
        self.assertEqual(tst.id, 3135556)
        self.assertEqual(tst.title, "Harder Better Faster Stronger")
        self.assertEqual(tst.artist.name, "Daft Punk")
        self.assertEqual(tst.artist.id, 27)
        self.assertEqual(tst.duration, 224)

        tst = Track.get(94690252)
        self.assertEqual(tst.id, 94690252)
        self.assertEqual(tst.title, "Another You")
        self.assertEqual(tst.artist.name, "Of Mice & Men")
        self.assertEqual(tst.artist.id, 468724)
        self.assertEqual(tst.duration, 226)

        tst = Track.get(126338363)
        self.assertEqual(tst.id, 126338363)
        self.assertEqual(tst.title, "Silvera")
        self.assertEqual(tst.artist.name, "Gojira")
        self.assertEqual(tst.artist.id, 2993)
        self.assertEqual(tst.duration, 212)

    def test_artist(self):

        tst = Artist.get(863)
        self.assertEqual(tst.id, 863)
        self.assertEqual(tst.name, "Scorpions")

        tst = Artist.get(4069)
        self.assertEqual(tst.id, 4069)
        self.assertEqual(tst.name, "Porcupine Tree")

        tst = Artist.get(92)
        self.assertEqual(tst.id, 92)
        self.assertEqual(tst.name, "Linkin Park")

    def test_user(self):

        tst = User.get(561764861)
        self.assertEqual(tst.id, 561764861)
        self.assertEqual(tst.username, "wilversings")

        tst = User.get(202860905)
        self.assertEqual(tst.id, 202860905)
        self.assertEqual(tst.username, "Alexandru Arnăutu")

        tst = User.get(854639931)
        self.assertEqual(tst.id, 854639931)
        self.assertEqual(tst.username, "Mircea.Popoveniuc")


if __name__ == '__main__':
    unittest.main()
