# *****CLASS THAT DETERMINES THE FLOW OF THE GAME*****
from player import Player

class Battlefield:

    def __init__(self) -> None:
        self.player_one = Player("Josh")
        self.player_two = Player("Kendra")
        pass

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.choose_num_of_players()
        self.battle_phase()
        self.display_winner()


    def display_welcome(self):
        print("")
        print("Welcome to Rock Paper Scissors Lizard Spock!")
        print("")

    def display_rules(self):
        print("")
        print("Each match will be the best out of 3 rounds.")
        print("You will use the number keys to make your selections throughout the game.")
        print("")
        print("Scissors cut Paper.")
        print("Paper covers Rock.")
        print("Rock crushes Lizard.")
        print("Lizard poisons Spock.")
        print("Spock smashes Scissors.")
        print("Scissors decapitates Lizard.")
        print("Lizard eats Paper.")
        print("Paper disproves Spock.")
        print("Spock vaporizes Rock.")
        print("Rock crushes Scissors.")
        print("")
        pass

    def choose_num_of_players(self):
        number_of_players = int(input("How many players? Please type 1 or 2: "))
        pass

    def battle_phase(self):
        pass

    def display_winner(self):
        pass


