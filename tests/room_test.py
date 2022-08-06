import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song



class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Room 1", 1000, [])
        self.guest = Guest("Adam", 50)
        self.song =Song("Under Pressure", "Queen", 5)

    def test_check_room(self):
        self.assertEqual("Room 1", self.room.name)

    def test_room_till(self):
        self.assertAlmostEqual(1000, self.room.till)
    
    def test_room_customers(self):
        self.assertAlmostEqual([], self.room.customers)

    def test_increase_till(self):
        self.room.increase_till(10)
        self.assertEqual(1010, self.room.till)

    def test_room_charge(self, cost_of_room):
        self.guest.reduce_money(cost_of_room)
        self.room.increase_till(cost_of_room)
        self.assertEquals(10, cost_of_room)