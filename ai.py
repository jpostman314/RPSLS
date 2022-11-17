from player import Player
from random import choice


class Ai(Player):

    def __init__(self):
        super().__init__()
        self.name = choice(["Computer Dave", "Computer R2D2", "Computer Pascal"])

    def choose_gesture(self):
        self.current_gesture = choice(self.gestures_list)
        print(f"{self.name} has chosen {self.current_gesture}." )