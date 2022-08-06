class Room:
    def __init__(self, name, till, customers):
        self.name = name
        self.till = till
        self.customers = []

    def increase_till(self, amount):
        self.till += amount

    def room_charge(self, cost_of_room):
        self.guest.reduce_money(cost_of_room)
        self.room.increase_till(cost_of_room)
