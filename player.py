

class Player:

    def __init__(self):
        self.name = "Player 1"
        self.wins = 0
        self.losses = 0

    def player_name(self):
        self.player_name = input("What is your name? ")
        print(self.name)

    def add_player_win(self):
        self.wins += 1

    def add_player_loss(self):
        self.losses -= 1