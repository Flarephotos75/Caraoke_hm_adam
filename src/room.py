class Room:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.customers = []
        self.songs = []

    def increase_till(self, amount):
        self.till += amount

    def song_count(self):
        return len(self.songs)

    def add_song(self,song):
        self.songs.append(song)

    def guest_count(self):
        return len(self.customers)

    def add_guest(self,customer):
        self.customers.append(customer)        
