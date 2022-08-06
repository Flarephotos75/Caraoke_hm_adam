from asyncio.proactor_events import _ProactorBaseWritePipeTransport
import unittest
from src.guest import Guest


class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.customer = Guest("Adam", 50)

    def test_guest_has_name(self):
        self.assertEqual("Adam", self.customer.name)

    def test_check_for_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    def test_reduce_money(self):
        self.customer.reduce_money(10)
        self.assertEqual(40, self.customer.wallet)

