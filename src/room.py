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

    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)

    def remove_guest(self,customer):
        self.customers.remove(customer)

    def under_room_limit(self): 
        if self.customers < 10:
            print("Come in")

    def over_room_limit(self):
        if self.customers >= 11:
            print("Too busy")

    def party_time(self, song):
        self.add_guest()
        self.add_guest()
        self.customers.buy_song
        self.customers.buy_song
        self.customers.reduce_money
        self.customers.reduce_money
        self.till += song.price
        self.till += song.price
        

    
