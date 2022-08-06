import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song



class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Room 1", 1000,)
        self.guest_1 = Guest("Adam", 50)
        self.guest_2 = Guest("Arwen", 100) 
        self.song_1 = Song("Under Pressure", "Queen", 5)
        self.song_2 = Song("Bat out of hell", "Meatloaf" ,15)


    def test_check_room(self):
        self.assertEqual("Room 1", self.room.name)

    def test_room_till(self):
        self.assertAlmostEqual(1000, self.room.till)
    
    def test_room_customers(self):
        self.assertAlmostEqual([], self.room.customers)

    def test_increase_till(self):
        self.room.increase_till(10)
        self.assertEqual(1010, self.room.till)

    def test_room_charge(self):
        self.guest_1.reduce_money(10)
        self.room.increase_till(10)
        self.assertEqual(1010, self.room.till)

    def test_room_can_add_song(self):
        self.room.add_song(self.song_1)
        self.assertEqual(1, self.room.song_count())

    def test_room_can_add_guest(self):
        self.room.add_guest(self.guest_2)
        self.assertEqual(1, self.room.guest_count())

    def test_remove_song(self):
        self.room.remove_song(self.song_1)
        self.assertEqual(0, self.room.song_count())

    def test_remove_guest(self):
        self.room.add_guest(self.guest_1)
        self.room.remove_guest(self.guest_1)
        self.assertEqual(0, self.room.guest_count())

    def test_room_limit(self):
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_2)
        self.room.room_limit()
        self.assertEqual(2, self.room.guest_count())
        


    # def test_party_time(self):
    #     self.room.add_guest(self.guest_1)
    #     self.room.add_guest(self.guest_2)
    #     self.guest_1.buy_song(self.song_1)
    #     self.guest_1.buy_song(self.song_2)
    #     self.room.add_song(self.song_1)
    #     self.room.add_song(self.song_2)
    #     self.assertEqual(0, self.room.guest_count())
    #     self.assertEqual(0, self.room.guest_count())
    #     self.assertEqual(0, self.room.guest_count())
    #     self.assertEqual(0, self.room.guest_count())
    #     self.assertEqual(0, self.room.guest_count())
    #     self.assertEqual(0, self.room.guest_count())
