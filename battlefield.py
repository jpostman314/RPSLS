# *****CLASS THAT DETERMINES THE FLOW OF THE GAME*****



from human import Human
from ai import Ai
class Battlefield:

    def __init__(self) -> None:
        self.player_one = "player_one"
        self.player_two = "player_two"
        pass

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.choose_num_of_players()
        self.battle_phase()
        self.display_winner()


    def display_welcome(self):
        print("")
        print("                             Welcome to Rock Paper Scissors Lizard Spock!")
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
        
    def display_gestures(self):
        print("")
        print("Your possible gesture choices are: ")
        print("")
        print("Type 0 for Rock.")
        print("Type 1 for Paper.")
        print("Type 2 for Scissors.")
        print("Type 3 for Lizard.")
        print("Type 4 for Spock.")
        print("")
        print("Please select your gesture using the number keys.")
        print("")


    def choose_num_of_players(self):
        valid_response = False
        
        while valid_response == False:
            number_of_players = int(input("How many players? Please type 1 or 2: "))
            if number_of_players == 1:
                self.player_one = Human()
                self.player_two = Ai()
                self.player_one.name = input("What is your name Player 1? ")
                print(f"Welcome to the game {self.player_one.name}!")
                print(f"Welcome to the game {self.player_two.name}!")
                valid_response = True
                
            elif number_of_players == 2:
                self.player_one = Human()
                self.player_two = Human()
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
        games_played = 0
        turn_counter = 0
        while games_played < 3:
            if turn_counter % 2 == 0 and games_played < 4:
                self.display_gestures()
                self.player_one.choose_gesture()
                player_ones_choice = self.player_one.current_gesture
                turn_counter += 1
            elif turn_counter % 2 != 0 and games_played < 4:
                self.display_gestures()
                self.player_two.choose_gesture()
                player_twos_choice = self.player_two.current_gesture
                turn_counter += 1
            
                if player_ones_choice == "Rock":
                    if player_twos_choice == "Rock":
                        print(f"You have both chosen Rock. It's a tie!")
                    elif player_twos_choice == "Paper":
                        print(f"Paper covers rock. {self.player_two.name} wins this round!")
                        self.player_two.score += 1
                    elif player_twos_choice == "Scissors":
                        print(f"Rock crushes Scissors. {self.player_one.name} wins this round!")
                        self.player_one.score += 1
                    elif player_twos_choice == "Lizard":
                        print(f"Rock crushes Lizard. {self.player_one.name} wins this round!")
                        self.player_one.score += 1
                    elif player_twos_choice == "Spock":
                        print(f"Spock vaporizes Rock. {self.player_two.name} wins this round!")
                        self.player_two.score += 1
                    print(f"{self.player_one.name}'s score is now {self.player_one.score}.")
                    print(f"{self.player_two.name}'s score is now {self.player_two.score}.")
                    games_played += 1

                elif player_ones_choice == "Paper":
                    if player_twos_choice == "Rock":
                        print(f"Paper covers Rock. {self.player_one.name} wins this round!")
                        self.player_one.score += 1
                    elif player_twos_choice == "Paper":
                        print(f"You have both chosen Paper. It's a tie!")
                    elif player_twos_choice == "Scissors":
                        print(f"Scissors cut Paper. {self.player_two.name} wins this round!")
                        self.player_two.score += 1
                    elif player_twos_choice == "Lizard":
                        print(f"Lizard eats Paper. {self.player_two.name} wins this round!")
                        self.player_two.score += 1
                    elif player_twos_choice == "Spock":
                        print(f"Paper disproves Spock. {self.player_one.name} wins this round!")
                        self.player_one.score += 1
                    print(f"{self.player_one.name}'s score is now {self.player_one.score}.")
                    print(f"{self.player_two.name}'s score is now {self.player_two.score}.")
                    games_played += 1

                elif player_ones_choice == "Scissors":
                    if player_twos_choice == "Rock":
                        print(f"Rock crushes Scissors. {self.player_two.name} wins this round!")
                        self.player_two.score += 1
                    elif player_twos_choice == "Paper":
                        print(f"Scissors cut Paper. {self.player_one.name} wins this round!")
                        self.player_one.score += 1
                    elif player_twos_choice == "Scissors":
                        print(f"You have both chosen Scissors. It's a tie!")
                    elif player_twos_choice == "Lizard":
                        print(f"Scissors decapitates Lizard. {self.player_one.name} wins this round!")
                        self.player_one.score += 1
                    elif player_twos_choice == "Spock":
                        print(f"Spock smashes Scissors. {self.player_two.name} wins this round!")
                        self.player_two.score += 1
                    print(f"{self.player_one.name}'s score is now {self.player_one.score}.")
                    print(f"{self.player_two.name}'s score is now {self.player_two.score}.")
                    games_played += 1

                elif player_ones_choice == "Lizard":
                    if player_twos_choice == "Rock":
                        print(f"Rock crushes Lizard. {self.player_two.name} wins this round!")
                        self.player_two.score += 1
                    elif player_twos_choice == "Paper":
                        print(f"Lizard eats Paper. {self.player_one.name} wins this round!")
                        self.player_one.score += 1
                    elif player_twos_choice == "Scissors":
                        print(f"Scissors decapitates Lizard. {self.player_two.name} wins this round!")
                        self.player_two.score += 1
                    elif player_twos_choice == "Lizard":
                        print(f"You have both chosen Lizard. It's a tie!")
                    elif player_twos_choice == "Spock":
                        print(f"Lizard poisons Spock. {self.player_one.name} wins this round!")
                        self.player_one.score += 1
                    print(f"{self.player_one.name}'s score is now {self.player_one.score}.")
                    print(f"{self.player_two.name}'s score is now {self.player_two.score}.")
                    games_played += 1

                elif player_ones_choice == "Spock":
                    if player_twos_choice == "Rock":
                        print(f"Spock vaporizes Rock. {self.player_one.name} wins this round!")
                        self.player_one.score += 1
                    elif player_twos_choice == "Paper":
                        print(f"Paper disproves Spock. {self.player_two.name} wins this round!")
                        self.player_two.score += 1
                    elif player_twos_choice == "Scissors":
                        print(f"Spock smashes Scissors. {self.player_one.name} wins this round!")
                        self.player_one.score += 1
                    elif player_twos_choice == "Lizard":
                        print(f"Lizard poisons Spock. {self.player_two.name} wins this round!")
                        self.player_two.score += 1
                    elif player_twos_choice == "Spock":
                        print(f"You have both chosen Spock. It's a tie!")
                        self.player_one.score += 1
                    print(f"{self.player_one.name}'s score is now {self.player_one.score}.")
                    print(f"{self.player_two.name}'s score is now {self.player_two.score}.")
                    games_played += 1


    def display_winner(self):
        print("")
        print("The final score is:")
        print(f"{self.player_one.name}'s final score is {self.player_one.score}.")
        print(f"{self.player_two.name}'s final score is {self.player_two.score}.")
        print("")
        if self.player_one.score > self.player_two.score:
            print(f"{self.player_one.name} wins! Congratulations!!")
        elif self.player_two.score > self.player_one.score:
            print(f"{self.player_two.name} wins! Congratulations!!")
        elif self.player_one.score == self.player_two.score:
            print("It's a tie!")
        pass
        


