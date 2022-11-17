

class Player:

    def __init__(self):
        self.name = "Player 1"
        self.score = 0
        self.current_gesture = "Empty"
        self.gestures_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]


    def player_name(self):
        pass

    def add_to_player_score(self):
        self.score += 1

    def choose_gesture(self):
        pass