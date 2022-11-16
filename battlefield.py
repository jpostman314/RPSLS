# *****CLASS THAT DETERMINES THE FLOW OF THE GAME*****


from player import Player

class Battlefield:

    def __init__(self) -> None:
        self.player_one = Player()
        self.player_two = Player()
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
        

    def choose_num_of_players(self):
        valid_response = False
        
        while valid_response == False:
            number_of_players = int(input("How many players? Please type 1 or 2: "))
            if number_of_players == 1:
                self.player_one.name = input("What is your name Player 1? ")
                print(f"Welcome to the game {self.player_one.name}!")
                valid_response = True
            elif number_of_players == 2:
                self.player_one.name = input("What is your name Player 1? ")
                print(f"Welcome to the game {self.player_one.name}!")
                self.player_two.name = input("What is your name Player 2? ")
                print(f"Welccome to the game {self.player_two.name}!")
                valid_response = True
            else:
                print("")
                print("That is an invalid response. Please type 1 or 2.")
                print("")
        

    def battle_phase(self):
        pass

    def display_winner(self):
        pass


