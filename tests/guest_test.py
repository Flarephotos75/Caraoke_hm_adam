from asyncio.proactor_events import _ProactorBaseWritePipeTransport
import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song


class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.customer = Guest("Adam", 50.00)

    def test_guest_has_name(self):
        self.assertEqual("Adam", self.customer.name)

    def test_check_for_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    def test_reduce_money(self):
        self.customer.reduce_money(10)
        self.assertEqual(40, self.customer.wallet)

    def test_guest_can_buy_song(self):
        song = Song("Under Pressure","Queen", 5.00)
        self.customer.reduce_money(song.price)
        self.assertEqual(45, self.customer.wallet)
