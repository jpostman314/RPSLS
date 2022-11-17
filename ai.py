from player import Player
from random import choice


class Ai(Player):

    def __init__(self):
        super().__init__()
        self.name = choice(["Dave", "R2D2", "Pascal"])

    def choose_gesture(self):
        self.current_gesture = choice(self.gestures_list)
        print(f"{self.name} has chosen {self.current_gesture}." )