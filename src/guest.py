class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def reduce_money(self, amount):
        self.wallet -= amount

    def buy_song(self, amount):
        self.wallet -= amount.price

