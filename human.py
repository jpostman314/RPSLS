from player import Player

class Human(Player):

    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        print("")
        print("Choose 0 for Rock.")
        print("Choose 1 for Paper.")
        print("Choose 2 for Scissors.")
        print("Choose 3 for Lizard.")
        print("Choose 4 for Spock.")
        print("")
        self.current_gesture = input(f"Which gesture would you like to choose {self.name}? ")
        print(f"{self.name} has chosen {self.gestures_list[int(self.current_gesture)]}." )
        return self.current_gesture
    def player_name(self):
        pass